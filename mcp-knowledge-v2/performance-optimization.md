# Performance Optimization

*Proven techniques for improving speed, reducing latency, and optimizing resource usage*

## BetfairLightweight Streaming Performance Breakthrough

**Context:** Major performance improvement delivered in betfairlightweight version 2.12.0b0

**Problem:** Previous streaming implementation was slow, significantly impacting backtesting and live trading performance

**Solution:** Complete streaming refactor delivered massive performance gains:

**Performance Improvements Achieved:**
- **Lightweight mode:** 2.3x improvement (6.860s → 2.998s)
- **Non-lightweight mode:** 3.4x improvement (36.005s → 10.625s)  
- **With flumine patching:** 2.8x improvement (13.896s → 5.005s)
- **CPU usage:** Halved in live trading environments
- **Flumine now runs faster than the previous lightweight implementation**

**Implementation Notes:**
```python
# Upgrade to benefit from performance improvements
pip install betfairlightweight>=2.12.0b0

# Performance monitoring in your code
import time
start_time = time.time()
# Your streaming operations here
duration = time.time() - start_time
logger.info(f"Streaming operation took {duration:.3f}s")
```

**Expert:** liam (core maintainer) delivered and announced the improvements

**Why it matters:** This represents the largest performance gain in betfairlightweight history. The improvements make complex backtesting feasible and reduce latency in live trading significantly.

---

## Memory Optimization for Live Trading

**Context:** Optimizing memory usage for long-running trading processes to prevent leaks and improve stability

**Problem:** Production trading systems gradually consuming more memory over time, eventually causing crashes

**Solution:** Multi-faceted memory optimization approach:

**1. Data Structure Optimization:**
```python
from collections import deque
import numpy as np

class MemoryEfficientPriceHistory:
    """Memory-efficient price history using ring buffers"""
    
    def __init__(self, max_size=1000):
        self.prices = deque(maxlen=max_size)  # Automatic size limiting
        self.timestamps = deque(maxlen=max_size)
        
    def add_price(self, price, timestamp):
        self.prices.append(price)
        self.timestamps.append(timestamp)
        
    def get_moving_average(self, periods):
        if len(self.prices) < periods:
            return None
        # Use numpy for efficient calculation
        return np.mean(list(self.prices)[-periods:])

# Instead of growing lists that consume unlimited memory
class MemoryHeavyHistory:
    def __init__(self):
        self.all_prices = []  # This grows forever - BAD!
```

**2. Garbage Collection Tuning:**
```python
import gc

# Force garbage collection at strategic points
def cleanup_after_market_close():
    """Clean up memory after market processing"""
    # Clear large data structures
    market_data_cache.clear()
    
    # Force garbage collection
    collected = gc.collect()
    logger.info(f"Garbage collection freed {collected} objects")

# Monitor memory usage
import psutil
def log_memory_usage():
    process = psutil.Process()
    memory_mb = process.memory_info().rss / 1024 / 1024
    logger.info(f"Memory usage: {memory_mb:.1f} MB")
```

**3. Process Restart Strategy:**
```python
import os
import sys
from datetime import datetime, timedelta

class ProcessManager:
    def __init__(self, restart_interval_hours=12):
        self.start_time = datetime.now()
        self.restart_interval = timedelta(hours=restart_interval_hours)
        
    def should_restart(self):
        """Check if process should restart for memory hygiene"""
        uptime = datetime.now() - self.start_time
        return uptime > self.restart_interval
        
    def graceful_restart(self):
        """Restart process gracefully"""
        logger.info("Initiating graceful restart for memory cleanup")
        # Close resources, save state, etc.
        self.cleanup_resources()
        
        # Restart process
        os.execv(sys.executable, ['python'] + sys.argv)
```

**Why it matters:** Memory optimization is critical for production stability. Uncontrolled memory growth will eventually crash your trading system, potentially during important market periods.

---

## Data Processing Pipeline Optimization

**Context:** Optimizing data processing pipelines for real-time trading decisions

**Problem:** Complex calculations causing latency spikes that affect order placement timing

**Solution:** Optimized processing pipeline using vectorization and caching:

**1. Vectorized Calculations:**
```python
import numpy as np
import pandas as pd

class OptimizedCalculations:
    """Vectorized calculations for better performance"""
    
    def __init__(self):
        # Pre-allocate arrays for better memory performance
        self.price_buffer = np.zeros(1000, dtype=np.float64)
        self.volume_buffer = np.zeros(1000, dtype=np.float64)
        self.buffer_index = 0
        
    def add_market_data(self, price, volume):
        """Add data using pre-allocated buffers"""
        idx = self.buffer_index % len(self.price_buffer)
        self.price_buffer[idx] = price
        self.volume_buffer[idx] = volume
        self.buffer_index += 1
        
    def calculate_vwap(self, periods):
        """Vectorized VWAP calculation"""
        if self.buffer_index < periods:
            return None
            
        # Get last N periods using numpy slicing
        end_idx = self.buffer_index % len(self.price_buffer)
        start_idx = (end_idx - periods) % len(self.price_buffer)
        
        if start_idx < end_idx:
            prices = self.price_buffer[start_idx:end_idx]
            volumes = self.volume_buffer[start_idx:end_idx]
        else:
            # Handle wrap-around
            prices = np.concatenate([
                self.price_buffer[start_idx:],
                self.price_buffer[:end_idx]
            ])
            volumes = np.concatenate([
                self.volume_buffer[start_idx:],
                self.volume_buffer[:end_idx]
            ])
        
        return np.sum(prices * volumes) / np.sum(volumes)

# Performance comparison
def slow_vwap_calculation(price_history, volume_history, periods):
    """Slow approach using loops - AVOID"""
    total_pv = 0
    total_v = 0
    for i in range(-periods, 0):
        total_pv += price_history[i] * volume_history[i]
        total_v += volume_history[i]
    return total_pv / total_v
```

**2. Intelligent Caching:**
```python
from functools import lru_cache
import time

class CachedCalculations:
    def __init__(self):
        self.calculation_cache = {}
        self.cache_expiry = {}
        
    @lru_cache(maxsize=128)
    def expensive_model_calculation(self, market_data_hash, model_params):
        """Cache expensive calculations with LRU eviction"""
        # Expensive calculation here
        return complex_model_result
        
    def get_cached_result(self, key, calculation_func, ttl_seconds=30):
        """Get cached result with TTL"""
        now = time.time()
        
        if key in self.calculation_cache:
            if now - self.cache_expiry[key] < ttl_seconds:
                return self.calculation_cache[key]
                
        # Calculate new result
        result = calculation_func()
        self.calculation_cache[key] = result
        self.cache_expiry[key] = now
        
        return result
```

**Expert:** Community insights from performance optimization discussions

**Why it matters:** Processing latency directly affects trading performance. Optimized calculations can mean the difference between getting fills at target prices versus missing opportunities.

---

## Network and API Optimization

**Context:** Reducing network latency and API overhead for time-sensitive trading operations

**Problem:** API calls and network round-trips adding unnecessary latency to trading decisions

**Solution:** Network optimization strategies:

**1. Connection Pooling and Keep-Alive:**
```python
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

class OptimizedAPIClient:
    def __init__(self):
        self.session = requests.Session()
        
        # Configure retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=0.1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        
        # Configure adapter with connection pooling
        adapter = HTTPAdapter(
            max_retries=retry_strategy,
            pool_connections=10,
            pool_maxsize=20
        )
        
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        
        # Keep connections alive
        self.session.headers.update({'Connection': 'keep-alive'})
```

**2. Batch API Calls:**
```python
def batch_market_updates(market_ids, batch_size=10):
    """Process markets in batches to reduce API overhead"""
    results = []
    
    for i in range(0, len(market_ids), batch_size):
        batch = market_ids[i:i + batch_size]
        
        # Single API call for multiple markets
        batch_result = client.betting.list_market_book(
            market_ids=batch,
            price_projection={'priceData': ['EX_BEST_OFFERS']}
        )
        results.extend(batch_result)
        
    return results
```

**3. Streaming Optimization:**
```python
class OptimizedStreaming:
    def __init__(self):
        self.subscription_manager = None
        
    def optimize_subscription(self, market_ids):
        """Optimize streaming subscription for minimal latency"""
        
        # Use minimal data requirements
        price_filter = {
            'priceData': ['EX_BEST_OFFERS'],  # Only best prices
            'virtualise': False,              # Reduce processing
            'rollupModel': 'STAKE'           # Minimal rollup
        }
        
        market_filter = {
            'marketIds': market_ids,
            'ladderLevels': 3               # Only top 3 price levels
        }
        
        return self.create_subscription(market_filter, price_filter)
```

**Why it matters:** Network optimization can reduce latency by 10-50ms per operation, which is significant for high-frequency trading strategies where timing matters.

---

## Database Query Optimization

**Context:** Optimizing database operations for historical data retrieval and trade logging

**Problem:** Slow database queries affecting backtesting performance and real-time logging

**Solution:** Database optimization techniques:

**1. Efficient Indexing Strategy:**
```sql
-- Optimize for time-series queries
CREATE INDEX idx_market_data_time ON market_data (market_id, timestamp);
CREATE INDEX idx_trades_market_time ON trades (market_id, timestamp);

-- Optimize for P&L calculations  
CREATE INDEX idx_trades_pnl ON trades (strategy_id, market_id, realized_pnl);
```

**2. Batch Database Operations:**
```python
import sqlite3
from contextlib import contextmanager

class OptimizedDatabase:
    def __init__(self, db_path):
        self.db_path = db_path
        
    @contextmanager
    def batch_transaction(self):
        """Context manager for batch operations"""
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute('BEGIN TRANSACTION')
            yield conn
            conn.execute('COMMIT')
        except Exception:
            conn.execute('ROLLBACK')
            raise
        finally:
            conn.close()
            
    def batch_insert_trades(self, trades_data):
        """Insert multiple trades in single transaction"""
        with self.batch_transaction() as conn:
            conn.executemany(
                "INSERT INTO trades (market_id, price, size, timestamp) VALUES (?, ?, ?, ?)",
                trades_data
            )
```

**Why it matters:** Database optimization can improve backtesting speed by 5-10x and ensure real-time logging doesn't introduce latency into trading operations.