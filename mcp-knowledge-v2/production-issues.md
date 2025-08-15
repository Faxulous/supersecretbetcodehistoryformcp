# Production Issues

*Real problems encountered in live trading environments with proven solutions*

## Memory Leak in Long-Running Flumine Processes

**Context:** Production flumine instance consuming increasingly more memory over time in 24/7 operation

**Problem:** Memory usage gradually increases from normal baseline to problematic levels that can crash the system

**Solution:** This is a known issue with flumine memory management in production. Community has identified several mitigation strategies:
- Monitor memory usage actively and restart processes before critical thresholds
- Use containerized deployments with memory limits to prevent system-wide impact
- Implement proper garbage collection tuning for Python processes

**Expert:** Multiple community members have encountered this in production

**Why it matters:** Memory leaks will eventually crash your trading system, potentially during important market periods. Monitoring and mitigation strategies are essential for reliable operation.

---

## Database Writing Strategy Crashes on Market Close

**Context:** System experienced crashes when attempting to write ~150 markets to database during market close events

**Problem:** Direct database writes in strategy close events caused system to spiral and eventually killed the flumine instance

**Solution:** **Never write directly to database in strategy close events.** Best practice approach:
1. Use market recorder to capture raw data during live operation
2. Process data to database/CSV in separate batch processes  
3. Use middleware or worker processes for heavy I/O operations
4. Keep strategy close events lightweight and fast

**Code/Steps:**
```python
# DON'T DO THIS in strategy.market_close()
def market_close(self, market):
    # Heavy database write - BAD!
    self.database.write_market_data(market)
    
# DO THIS instead
def market_close(self, market):
    # Queue for background processing - GOOD!
    self.processing_queue.put(market)
```

**Expert:** liam recommended the market recorder pattern as established practice

**Why it matters:** Heavy synchronous operations during market close can overwhelm flumine's event loop. The market recorder pattern separates real-time data capture from heavy processing.

---

## Order Size Restrictions - max_order_exposure Gotcha

**Context:** Strategy working perfectly in simulation but failing to place larger orders in live mode

**Problem:** Orders with larger sizes (e.g., 12.0 units) weren't executing, while smaller sizes worked fine. No obvious error messages.

**Solution:** The issue was `max_order_exposure` configuration silently rejecting orders above the threshold. Check flumine settings and adjust exposure limits for your use case.

**Code/Steps:**
```python
# Check your flumine configuration
config = Config(
    max_order_exposure=1000.0,  # Increase if needed
    # ... other settings
)
```

**Expert:** Community solved through systematic log checking

**Why it matters:** Flumine has built-in risk controls that can silently reject orders. Always check logs when orders aren't executing as expected, especially when moving from simulation to live trading.

---

## Docker SSL Certificate Issues with Betfair Login

**Context:** betfairlightweight authentication failing in Docker containers with SSL errors

**Problem:** SSL error during Betfair login: "HTTPSConnectionPool(host='identitysso-cert.betfair.com', port=443): Max retries exceeded... SSLError(398, '[SSL: CA_MD_TOO_WEAK] ca md too weak')"

**Solution:** Docker container's `openssl.cnf` missing required SSL client configuration

**Code/Steps:**
Add this section to your Docker container's `openssl.cnf`:
```
[ ssl_client ]
basicConstraints = CA:FALSE
nsCertType = client
keyUsage = digitalSignature, keyEncipherment
extendedKeyUsage = clientAuth
```

**Expert:** river_shah discovered and shared the working solution

**Why it matters:** This specific Docker configuration issue can completely block authentication in containerized environments. The solution is simple but the error message doesn't make the fix obvious.

---

## Each-Way Market Execution Challenges

**Context:** Consistently poor fill rates on Each-Way markets compared to WIN markets

**Problem:** "Whenever I try to take a price in EACH_WAY markets it's almost always gone by the time my bet gets there, which is not true of WIN market"

**Solution:** Each-Way markets are cross-matched with WIN and PLACE markets, making them effectively composite markets with different liquidity dynamics. Adjust execution strategies accordingly:
- Expect higher latency on Each-Way markets
- Use more conservative price targets
- Consider trading WIN/PLACE separately instead of Each-Way

**Expert:** Maurice (Mo) confirmed the cross-matching behavior

**Why it matters:** Understanding market structure is crucial for execution strategies. Each-Way markets behave fundamentally differently due to their composite nature, requiring adjusted trading approaches.

---

## Restricted Countries Authentication (Denmark, etc.)

**Context:** Users in restricted countries like Denmark unable to authenticate with standard certificate methods

**Problem:** Danish users couldn't use certificate-based authentication and weren't receiving session IDs properly

**Solution:** Denmark and other restricted countries cannot use certificate/non-interactive login. Must use interactive login with country-specific handling.

**Code/Steps:** 
- Use interactive login methods
- Reference NemID login implementation: https://liampauling.github.io/betfair/advanced/#nemid-login
- Check Betfair's country restrictions for your jurisdiction

**Expert:** liam provided geographic-specific guidance

**Why it matters:** Geographic restrictions affect authentication methods. Users in restricted countries need entirely different authentication flows, not just configuration changes.