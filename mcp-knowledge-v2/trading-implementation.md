# Trading Implementation

*Practical guidance on order management, market behavior, and execution patterns*

## Fill-or-Kill Order Status Behavior

**Context:** Understanding the complete lifecycle of Fill-or-Kill (FOK) orders for proper trade management

**Problem:** Developer needed to understand FOK order status transitions, particularly around PENDING vs EXPIRED states and how they appear in streaming data

**Solution:** Complete FOK order behavior explanation:

**Order Status Flow:**
- FOK orders go directly from PENDING → EXECUTION_COMPLETE (if matched) or EXPIRED (if not matched)
- The order stream only shows "E" (executable) or "EC" (execution complete) - never shows EXPIRED status
- EXPIRED status appears in order reports/placeOrders response, not in streaming data
- Both matched and unmatched FOK orders show status="EC" in streaming

**Key Distinction:**
```python
# Matched FOK order in streaming data
{
    "status": "EC",  # Execution complete
    "sc": 0,         # Size cancelled = 0 (fully matched)
    "sm": 10.0       # Size matched = full order size
}

# Unmatched FOK order in streaming data  
{
    "status": "EC",  # Execution complete (misleading!)
    "sc": 10.0,      # Size cancelled = full order size
    "sm": 0          # Size matched = 0
}
```

**Expert:** mzaja provided detailed analysis with real data examples

**Why it matters:** Proper order lifecycle understanding is critical for trade management. The streaming data for FOK orders can be misleading - you must check `sc` (size cancelled) to determine if the order was actually filled.

---

## Starting Price (SP) Auction Participation

**Context:** Understanding which orders participate in Starting Price auctions and the risks involved

**Problem:** "Will LimitOrder with persistence_type='PERSIST' be considered for SP matching?"

**Solution:** Complete SP auction behavior:

**Order Types and SP Participation:**
```python
# WILL participate in SP auction
limit_order = LimitOrder(
    price=2.5, 
    size=10.0, 
    persistence_type="PERSIST"
)

# Will NOT participate in SP auction (default behavior)
limit_order = LimitOrder(
    price=2.5, 
    size=10.0, 
    persistence_type="LAPSE"  # Default
)
```

**Critical Warnings:**
- Orders with PERSIST will be matched at whatever SP is determined, regardless of your original limit price
- You cannot cancel LimitOnCloseOrder once placed
- SP can be dramatically different from your limit price, creating unexpected exposure

**Risk Management:**
```python
# Safer approach for SP participation
if estimated_sp <= acceptable_price_threshold:
    place_order_with_persist()
else:
    logger.warning(f"SP estimate {estimated_sp} exceeds threshold")
```

**Expert:** liam provided authoritative guidance as maintainer

**Why it matters:** SP auction participation can dramatically affect order execution and risk. Getting matched at SP without proper risk controls can result in significant unintended exposure if SP is distorted.

---

## Order Placement Strategy Patterns

**Context:** Effective patterns for placing orders in different market conditions

**Problem:** Balancing fill probability with favorable pricing in volatile markets

**Solution:** Multi-tier order placement strategy:

```python
class AdaptiveOrderStrategy:
    def place_back_order(self, runner, target_size, market_conditions):
        """Adaptive order placement based on market conditions"""
        
        available_prices = runner.ex.available_to_back
        if not available_prices:
            return None
            
        # Market condition assessment
        if market_conditions['volatility'] == 'HIGH':
            # More aggressive pricing in volatile markets
            target_price = available_prices[0]['price'] - 0.01
            order_type = LimitOrder(target_price, target_size)
            
        elif market_conditions['liquidity'] == 'LOW':
            # Take available prices in thin markets
            target_price = available_prices[0]['price']
            order_type = LimitOrder(target_price, target_size)
            
        else:
            # Standard approach - try for better price
            if len(available_prices) > 2:
                target_price = available_prices[1]['price']
            else:
                target_price = available_prices[0]['price'] - 0.01
            order_type = LimitOrder(target_price, target_size)
            
        return self.place_order(order_type)
    
    def assess_market_conditions(self, market_book):
        """Assess current market conditions for order strategy"""
        conditions = {}
        
        # Volatility assessment
        price_changes = self.get_recent_price_changes(market_book)
        conditions['volatility'] = 'HIGH' if price_changes > 0.05 else 'NORMAL'
        
        # Liquidity assessment  
        total_liquidity = sum(
            level['size'] for runner in market_book.runners 
            for level in runner.ex.available_to_back[:3]
        )
        conditions['liquidity'] = 'LOW' if total_liquidity < 1000 else 'NORMAL'
        
        return conditions
```

**Why it matters:** Market conditions significantly affect optimal order placement strategy. Static approaches often result in poor fill rates or suboptimal pricing.

---

## Order Size Optimization

**Context:** Determining optimal order sizes for different market conditions and strategies

**Problem:** Balancing order size with fill probability and market impact

**Solution:** Dynamic sizing based on available liquidity and market depth:

```python
def calculate_optimal_size(runner, target_exposure, market_depth_factor=0.3):
    """Calculate optimal order size based on market liquidity"""
    
    available_liquidity = runner.ex.available_to_back
    if not available_liquidity:
        return 0
    
    # Calculate available liquidity at best 3 price levels
    total_available = sum(level['size'] for level in available_liquidity[:3])
    
    # Don't exceed market_depth_factor of available liquidity
    max_size_by_liquidity = total_available * market_depth_factor
    
    # Don't exceed our target exposure
    optimal_size = min(target_exposure, max_size_by_liquidity)
    
    # Minimum viable size check
    min_size = 2.0  # Betfair minimum
    
    return max(optimal_size, min_size) if optimal_size >= min_size else 0

# Usage in strategy
optimal_size = calculate_optimal_size(
    runner=runner, 
    target_exposure=strategy_target,
    market_depth_factor=0.2  # More conservative in thin markets
)

if optimal_size > 0:
    place_order(LimitOrder(price, optimal_size))
```

**Why it matters:** Order size optimization prevents market impact while maximizing fill probability. Large orders in thin markets often result in poor execution or no fills.

---

## Trade Lifecycle Management

**Context:** Managing complete trade lifecycle from order placement through profit/loss realization

**Problem:** Tracking trade performance and managing exit strategies effectively

**Solution:** Comprehensive trade management system:

```python
class TradeManager:
    def __init__(self):
        self.active_trades = {}
        self.completed_trades = []
        
    def open_trade(self, market_id, selection_id, order_result):
        """Track new trade opening"""
        trade_id = f"{market_id}_{selection_id}_{order_result.id}"
        
        self.active_trades[trade_id] = {
            'market_id': market_id,
            'selection_id': selection_id,
            'order_id': order_result.id,
            'entry_price': order_result.price_matched,
            'entry_size': order_result.size_matched,
            'entry_time': datetime.now(),
            'side': 'BACK' if order_result.side == 'B' else 'LAY',
            'status': 'OPEN'
        }
        
        return trade_id
    
    def update_trade_pnl(self, trade_id, current_market_book):
        """Update unrealized P&L for active trade"""
        if trade_id not in self.active_trades:
            return
            
        trade = self.active_trades[trade_id]
        runner = self._find_runner(current_market_book, trade['selection_id'])
        
        if not runner or not runner.ex.available_to_lay:
            return
            
        current_price = runner.ex.available_to_lay[0]['price']
        
        if trade['side'] == 'BACK':
            # Back bet P&L
            pnl = (current_price - trade['entry_price']) * trade['entry_size']
        else:
            # Lay bet P&L  
            pnl = (trade['entry_price'] - current_price) * trade['entry_size']
            
        trade['unrealized_pnl'] = pnl
        trade['current_price'] = current_price
        
    def close_trade(self, trade_id, exit_price, exit_time):
        """Close trade and calculate final P&L"""
        trade = self.active_trades.pop(trade_id)
        
        if trade['side'] == 'BACK':
            realized_pnl = (exit_price - trade['entry_price']) * trade['entry_size']
        else:
            realized_pnl = (trade['entry_price'] - exit_price) * trade['entry_size']
            
        trade.update({
            'exit_price': exit_price,
            'exit_time': exit_time,
            'realized_pnl': realized_pnl,
            'status': 'CLOSED'
        })
        
        self.completed_trades.append(trade)
        return realized_pnl
```

**Why it matters:** Proper trade lifecycle management enables accurate performance tracking and informed decision-making about position sizing and exit strategies.