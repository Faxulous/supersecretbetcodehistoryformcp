# API & Data Issues

*Common Betfair API problems and data handling challenges with working solutions*

## Streaming Data - Getting Zero Values for total_matched

**Context:** Developer trying to access total_matched field in streaming data but consistently getting zeros

**Problem:** "I'm trying to add total_matched into my streaming output but I'm just getting 0's for everything... is there something I'm missing?"

**Solution:** This is a delayed key limitation. `total_matched` data requires a paid/non-delayed API key from Betfair. With a delayed key (free tier), you won't get `total_matched` values.

**Code/Steps:**
1. Check your API key status: https://apps.betfair.com/visualisers/api-ng-account-operations/
2. Upgrade to paid data access if you need real-time `total_matched`
3. Ensure streaming filter is properly configured for the data you have access to

**Expert:** liam (core maintainer) identified the delayed key limitation

**Why it matters:** This is a common gotcha for developers - you need to pay for non-delayed data to access `total_matched` values. The API doesn't clearly indicate this limitation, leading to confusion.

---

## TOO_MUCH_DATA Error Solutions

**Context:** API calls failing with "TOO_MUCH_DATA" error when requesting market catalogues

**Problem:** `betfairlightweight.exceptions.APIError` with error code `TOO_MUCH_DATA` when calling `listMarketCatalogue`

**Solution:** Multiple approaches to resolve:

1. **Remove unnecessary projections:**
   ```python
   # Remove RUNNER_METADATA if not needed
   market_projection = [
       'RUNNER_DESCRIPTION', 
       # 'RUNNER_METADATA',  # Remove this
       'COMPETITION', 
       'EVENT', 
       'MARKET_DESCRIPTION'
   ]
   ```

2. **Reduce time window:**
   ```python
   # Smaller time ranges
   market_filter = {
       'marketStartTime': {
           'from': 'start_time',
           'to': 'end_time'  # Reduce this window
       }
   }
   ```

3. **Use maxResults effectively:**
   ```python
   # Limit results per call
   catalogue = client.betting.list_market_catalogue(
       filter=market_filter,
       market_projection=market_projection,
       max_results=50  # Reduce from default 150
   )
   ```

**Expert:** tone shared the RUNNER_METADATA removal solution

**Why it matters:** TOO_MUCH_DATA errors can block critical data retrieval operations. Understanding which projections and filters contribute most to response size helps optimize API usage.

---

## Market Catalogue Loading for Backtesting

**Context:** Need to load both market data and catalogue data simultaneously for comprehensive backtesting

**Problem:** "I have market data saved in *.gz and catalogue data saved in *.json.gz file. How to load both market data and catalogue data at the same time?"

**Solution:** Use flumine middleware to automatically load catalogue data alongside market data

**Code/Steps:**
```python
import json
import os
from betfairlightweight.resources import MarketCatalogue
from flumine.markets.middleware import Middleware

MARKET_CATALOGUE_PATH = "/path/to/catalogue/files"

class MarketCatalogueMiddleware(Middleware):
    def add_market(self, market) -> None:
        catalogue_file_path = os.path.join(
            MARKET_CATALOGUE_PATH, 
            f"{market.market_id}.json.gz"
        )
        if os.path.exists(catalogue_file_path):
            with open(catalogue_file_path, "r") as f:
                catalogue_data = json.load(f)
                market.market_catalogue = MarketCatalogue(**catalogue_data)

# Usage in flumine setup
framework.add_market_middleware(MarketCatalogueMiddleware())
```

**Expert:** liam provided the complete middleware implementation

**Why it matters:** Proper catalogue loading is essential for strategies that need market metadata (runners, event details, etc.). The middleware pattern ensures data is available when markets are processed.

---

## AWS S3 Direct Reading for Historical Data

**Context:** Optimizing data access for backtesting with historical data stored in AWS S3

**Problem:** Currently copying all market files from S3 to EC2 instances for backtesting - wondering about more efficient approaches

**Solution:** Multiple strategies depending on your access patterns:

**Option 1: Direct S3 streaming (single-read scenarios)**
```python
from smart_open import open

# Read directly from S3 without local copies
with open('s3://bucket/path/market_data.gz', 'rb') as f:
    market_data = f.read()
```

**Option 2: Hybrid caching (multiple reads)**
```python
import os
from smart_open import open

def get_market_data(s3_path, local_cache_dir):
    local_path = os.path.join(local_cache_dir, os.path.basename(s3_path))
    
    if os.path.exists(local_path):
        # Use cached version
        with open(local_path, 'rb') as f:
            return f.read()
    else:
        # Download and cache
        with open(s3_path, 'rb') as s3_file:
            data = s3_file.read()
            with open(local_path, 'wb') as local_file:
                local_file.write(data)
        return data
```

**Expert:** Maurice suggested `smart_open`, liam shared hybrid caching approach

**Why it matters:** Data access patterns significantly impact backtesting performance and AWS costs. Direct streaming saves storage costs but may be slower for repeated access. Choose based on your usage patterns.

---

## Authentication Session Management

**Context:** Managing authentication sessions effectively to avoid repeated login overhead

**Problem:** Frequent re-authentication causing delays and potential rate limiting

**Solution:** Implement proper session management with token reuse:

```python
import betfairlightweight
from datetime import datetime, timedelta

class SessionManager:
    def __init__(self):
        self.client = None
        self.session_expires = None
        
    def get_client(self):
        if self.client is None or self._session_expired():
            self._create_new_session()
        return self.client
        
    def _session_expired(self):
        return datetime.now() > self.session_expires
        
    def _create_new_session(self):
        self.client = betfairlightweight.APIClient(
            username="your_username",
            password="your_password",
            app_key="your_app_key"
        )
        self.client.login()
        # Sessions typically last 8 hours
        self.session_expires = datetime.now() + timedelta(hours=7)
```

**Why it matters:** Proper session management reduces authentication overhead and avoids hitting Betfair's login rate limits, which can temporarily block access to your applications.

---

## Data Quality Validation

**Context:** Ensuring data quality in backtesting and live trading environments

**Problem:** Inconsistent or missing data can lead to incorrect strategy behavior and unreliable backtesting results

**Solution:** Implement comprehensive data validation:

```python
def validate_market_data(market_book):
    """Validate market data quality before processing"""
    issues = []
    
    # Check for missing total matched
    if market_book.total_matched is None:
        issues.append("Missing total_matched - likely delayed key")
    
    # Check for reasonable prices
    for runner in market_book.runners:
        if runner.ex.available_to_back:
            best_back = runner.ex.available_to_back[0]['price']
            if best_back < 1.01 or best_back > 1000:
                issues.append(f"Suspicious back price: {best_back}")
                
    # Check timestamp recency
    last_update = market_book.publish_time
    if last_update < datetime.now() - timedelta(minutes=5):
        issues.append("Stale data detected")
        
    return issues

# Usage
data_issues = validate_market_data(market_book)
if data_issues:
    logger.warning(f"Data quality issues: {data_issues}")
```

**Why it matters:** Poor data quality can lead to incorrect trading decisions. Validation helps identify when you're working with incomplete or suspicious data, allowing you to adjust strategy behavior accordingly.