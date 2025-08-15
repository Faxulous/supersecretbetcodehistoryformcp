# Implementation Patterns

*Proven code patterns and examples from the community*

## Code Patterns

**Reference:** [https://github.com/betcode-org/flumine/blob/a9cd71befc6062b52ce65ca695b50a56a2e81344/flumine/config.py#L26](https://github.com/betcode-org/flumine/blob/a9cd71befc6062b52ce65ca695b50a56a2e81344/flumine/config.py#L26)

```python
t20_events_today = pd.DataFrame({
```

```python
import os

import logging

import psutil

import threading



logger = logging.getLogger(__name__)



PID = os.getpid()

_TWO_20 = float(2 ** 20)





def memory_profiler(context: dict, flumine, interval=1) -&gt; None:

    # get process

    process = psutil.Process(PID)

    # cpu

    cpu = psutil.cpu_percent(interval=interval)

    # ram

    memory_used = process.memory_info()[0] / _TWO_20

    memory = {

        "used": round(memory_used, 1),

        "percentage": round(process.memory_percent(), 1),

    }

    [http://logger.info|logger.info](http://logger.info|logger.info)(

        "memory_profiler",

        extra={"cpu": cpu, "memory": memory, "threads": threading.enumerate()},

    )
```

```python
import time

import logging

import betfairlightweight

from betfairlightweight.filters import streaming_market_filter

from pythonjsonlogger import jsonlogger

from flumine import Flumine, clients, BaseStrategy

from flumine.order.trade import Trade

from flumine.order.ordertype import LimitOrder

from flumine.order.order import OrderStatus

from flumine.utils import get_price



logger = logging.getLogger()



custom_format = "%(asctime) %(levelname) %(message)"

log_handler = logging.StreamHandler()

formatter = jsonlogger.JsonFormatter(custom_format)

formatter.converter = time.gmtime

log_handler.setFormatter(formatter)

logger.addHandler(log_handler)

logger.setLevel([http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))





class ExampleStrategy(BaseStrategy):

    def start(self):

        # subscribe to streams

        print("starting strategy 'ExampleStrategy'")



    def check_market_book(self, market, market_book):

        # process_market_book only executed if this returns True

        if market_book.status != "CLOSED":

            return True



    def process_market_book(self, market, market_book):

        # process marketBook object

        self.log_validation_failures = True

        for runner in market_book.runners:

            if (

                runner.status == "ACTIVE"

                and runner.last_price_traded

                and get_price(runner.ex.available_to_back, 0) &gt;= 20



            ):

                trade = Trade(

                    market_id=market_book.market_id,

                    selection_id=runner.selection_id,

                    handicap=runner.handicap,

                    strategy=self,

                )

                order = trade.create_order(

                    side="LAY", order_type=LimitOrder(price=1.01, size=2.00)

                )

                market.place_order(order)



    def process_orders(self, market, orders):

        for order in orders:

            if order.status == OrderStatus.EXECUTABLE:

                if order.elapsed_seconds and order.elapsed_seconds &gt; 1:

                    if order.size_remaining == 2.00:

                        market.replace_order(order,2)



trading = betfairlightweight.APIClient("username")

client = clients.BetfairClient(trading, paper_trade=True)





framework = Flumine(client=client)



strategy = ExampleStrategy(

    market_filter=streaming_market_filter(

            event_type_ids=['7'],

            country_codes=['GB','IE','AU','US'],

            market_types=['WIN']),

)

framework.add_strategy(strategy)



framework.run()
```

```python
with framework.simulated_datetime.real_time():

    print(datetime.datetime.utcnow())
```

---

## Error Patterns

```python
&lt;html&gt;&lt;head&gt;&lt;title&gt;Object moved&lt;/title&gt;&lt;/head&gt;&lt;body&gt; &lt;h2&gt;Object moved to &lt;a href="/#/error.html"&gt;here&lt;/a&gt;.&lt;/h2&gt; &lt;/body&gt;&lt;/html&gt;
```

**Reference:** [https://github.com/betcode-org/betfair/blob/master/examples/examplestreaming.py|examples](https://github.com/betcode-org/betfair/blob/master/examples/examplestreaming.py|examples)

```python
for m in flumine.markets:

    do_stuff(m)
```

```python
order.violation_msg = "strategy.validate_order failed: trade_count ({0}) &gt;= max_trade_count ({1})".format(
```

```python
current_order_list = trading.betting.list_current_orders(

    order_by="BY_MATCH_TIME",

    sort_dir="LATEST_TO_EARLIEST",

    record_count="20",

    lightweight=False)





print(current_order_list._data)
```

---

## Question Patterns

```python
{"asctime": "2022-05-25 08:37:27,870", "levelname": "INFO", "message": "Market removed", "market_id": "1.199544108", "event_id": "31480130", "events": {"31481118": ["&lt;flumine.markets.market.Market object at 0x7f4b93bf72d0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f9a7b10&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f94b3d0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90a650&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90a490&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90a190&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90a7d0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90a710&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90a850&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90a590&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90a810&gt;"], "31481103": ["&lt;flumine.markets.market.Market object at 0x7f4b8f90aa10&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90a790&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90aad0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90a9d0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90aa90&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90ab90&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90ad50&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90ac90&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90add0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90ab10&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90ad90&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90af90&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f90ad10&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922050&gt;"], "31481164": ["&lt;flumine.markets.market.Market object at 0x7f4b8f922090&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922110&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922150&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922210&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922250&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f9222d0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922490&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f9223d0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922510&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f9221d0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f9224d0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f9226d0&gt;"], "31481038": ["&lt;flumine.markets.market.Market object at 0x7f4b8f922450&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922790&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922690&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922750&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f9227d0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f9228d0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922a90&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f9229d0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922b10&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922850&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922ad0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922cd0&gt;"], "31481066": ["&lt;flumine.markets.market.Market object at 0x7f4b8f922a50&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922d50&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922ed0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bc0d0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bcc90&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bcf50&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8d40d0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8d4190&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8d4210&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bcd10&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8ee410&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8ee4d0&gt;"], "31481108": ["&lt;flumine.markets.market.Market object at 0x7f4b8f922d90&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bc310&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bc450&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bc410&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bc4d0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bc850&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bc750&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bc910&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bc6d0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bc390&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bcb10&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bc9d0&gt;"], "31481135": ["&lt;flumine.markets.market.Market object at 0x7f4b8f922c90&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f922dd0&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bc090&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bc150&gt;", "&lt;flumine.markets.market.Market object at 0x7f4b8f8bc190&gt;", " + 30k more chars
```

**Reference:** [https://github.com/betfair-down-under/autoHubTutorials/tree/master/FastTrack](https://github.com/betfair-down-under/autoHubTutorials/tree/master/FastTrack)

```python
market_filter=streaming_market_filter(

    event_type_ids=s['7'],

    country_codes=['GB','IE','US'],

    market_types=['WIN','PLACE', 'EACH_WAY'],
```

**Reference:** [https://github.com/betcode-org/flumine/blob/master/flumine/strategy/strategy.py#L154](https://github.com/betcode-org/flumine/blob/master/flumine/strategy/strategy.py#L154)

```python
.

I create a bunch of orders for different runners using
```

---

