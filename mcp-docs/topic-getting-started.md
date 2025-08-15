# Getting Started - Community Knowledge

*682 relevant conversations from across all channels*

---

## 2025-01-14 15:32:15 - strategies channel

**Unknown**

Apologies in advance to anyone I've already asked about this...

I've been working on a model for GB dogs. No price data or market signals involved at all - it is all fundamental modelling using data freely available to anyone. I'm usually of the opinion that models from such data are going to be worthless but I decided to give it a go anyway.

I've come up with a model that I believe has squeezed as much as it can from the data available. Model summary as follows:

1. Model built to generate win probabilities for dogs ONLY for A grade races

2. Model built using data from 2018 to 2023 (inclusive) using classical statistical modelling only

I've taken the model parameters and using 2024 data have generated some rough numbers to see how well calibrated it is. I've also run a quick and dirty backtest by approximating profit backing to BSP whenever BSP is greated than my model's 0EV price (I realise this step may well be pointless). For what it is worth, this test shows tiny profit after commission.



Looking at the numbers (attached) it looks like the model is reasonably well calibrated - I do have some concerns that it lacks the power to predict high probabilies for runners as the vast majority of fitted prbabilities are 0.4 or under. This might be OK though as these are graded races where each dog is supposed to be roughly the same current standard.



My questions are as follows:



1. Is the model shite and can/should it be abandoned now based on attached numbers

2. Assuming no to 1. what is a "good" next step to take (e.g. full backtest using highest price traded, full backtest using price X seconds from scheduled start etc.)

3. Again assuming no to 1. is it "good enough" to be worth pursuing with the view to augmenting the dataset with some more obscure/less easily available data

A lot of questions here but pre-off fundamental models are new to me. Inplay, backtesting or running strategies without backtest is easier to grasp - you know your model value has a finite lifetime and you need to pull any unmatched money before it gets too stale. Pre-off, your probability is fixed - but the market changes so how do you evaluate the execution (literature tells you value is not around for a long time with bookies, but betfair pre-off dog and horse markets suggest othewise - do you ride a trend in your favour until it reverses or fill your boots while you can) ??



I was going to keep asking people things via DM, but I figured that this is generic enough of a modelling problem to possibly be worth asking about publicly and resulting discourse might be helpful to others (even if only as an example of something that is ultimately useless and should be abandoned)

---

## 2025-01-12 11:40:47 - random channel

**D C**

I personally see no value in sticking with an older LTS (although I don't use flumine) but if that wors for you then do it. When setting up new instances I just go with the latest LTS version then install whatever is needed on top of that and tweak any things that needed tweaking and go from there. You might get a few SSL issues that need resolving (I think I did when moving up from 20.04) due to having "older" BF cert files but I'd say it's worth sticking with the latest if you are setting up something new. I should be honest though and say that other than an initial update on a fresh install, once things are running I don't run updates as that requires restart usually.

In general I like to run the same OS on AWS as I am doing my dev work on and that's always going to be latest LTS ubuntu. Might review that if AWS start offering other linux flavours in future though.

---

## 2025-01-10 18:40:28 - random channel

**PeterLe**

Ah I see



GPT explained that for me:

Yes—*if* Flumine is calling your `process_sports_data` method and passing in a valid `market` object, it means Flumine has already recognized that sports-data (“raceSubscription”) update *belongs* to one of the markets it’s tracking. In other words, Flumine does the internal ID matching (the RaceStream `'mid'` vs. the strategy’s `'market_id'`).

When It “Just Works”

In many cases (particularly UK racing), Betfair’s `'mid'` from the RaceStream *matches* the `'market_id'` in the MarketStream. Flumine will say:

• “I see a sports-data update for `'mid' = 1.23456...'`.”

• “I have a known Market object for `'market_id' = 1.23456...'`.”

• “So I’ll call `process_sports_data(market, sports_data)` with that Market object.”

That’s why in `process_sports_data`, you can trust `market.market_id` is the same ID Betfair used in `'mid'`. So you can store the GPS data under `self.gps_data[market_id]` safely.

When You See “Market Not Present for Sports Data”

This arises if Betfair sends `'rcm'` messages with a `'mid'` that *does not* match any Market object Flumine is currently tracking. In that scenario, Flumine logs something like *“Market not present”* or doesn’t call your `process_sports_data` for that `'mid'`. That mismatch usually happens if:

1. You’re subscribed to additional markets/venues (like US or Irish racing) that come through the same RaceStream feed but you aren’t actually “watching” them in your `market_filter`.

2. You see the RaceStream `'mid'` is slightly different (e.g. `'1.23456...'` in RaceStream vs `'1.23457...'` in MarketStream). Rare, but it can happen.

Bottom Line

• *Yes*, if `process_sports_data` is being invoked with a valid Market, you essentially have “correctly mapped” RaceStream data to that Market.

• If you ever see a mismatch (`"Market not present..."`) in the logs, that means Betfair sent RaceStream data for an `'mid'` Flumine does not recognize as an active Market object. That’s the scenario where you’d either *ignore* that data (since you’re not betting on it) or implement a “mapping” workaround if you suspect Betfair’s `'mid'` and `'market_id'` differ.

In most standard UK racing setups, you *won’t* need a custom mapping. Flumine’s built-in logic does the ID match automatically, and you’ll receive `process_sports_data(market, ...)` calls whenever the RaceStream `'mid'` matches your `'market_id'`.



...and on the dummy strategy:



Exactly—Flumine can subscribe to multiple data streams (Market and Race) simultaneously, and it handles the matching between those streams under the hood. The “dummy strategy” approach is one way to ensure you’re actively subscribing to all the right race data (the so-called raceSubscription stream). Meanwhile, your main strategy can use the same feed (or a separate feed) to place bets.

Why a “Dummy Strategy” Sometimes Helps

• *Two different filters*: You can run one strategy (the “dummy”) with a market filter that explicitly subscribes to certain markets or events, possibly with a custom sports data filter. This dummy strategy may not place bets but ensures Flumine is pulling in the RaceStream data for those markets.

• *Another strategy* (the “main” strategy) can also see that same data (or a subset) and perform the actual betting logic.

In practice, though, *a single strategy* that sets both:

```python





market_filter=streaming_market_filter(...),

sports_data_filter=["raceSubscription"],```

often suffices. Flumine will then:

1. Identify your target markets (via `market_filter`).

2. Subscribes to the race data (via `sports_data_filter=["raceSubscription"]`).

3. Calls `process_sports_data(market, sports_data)` with the correct *`market` object* whenever Betfair’s RaceStream updates arrive.

4. Calls `process_market_book(market, market_book)` whenever MarketStream updates arrive for that same market.

If Betfair provides matching IDs for both Market and Race streams (which is usually the case for UK/GB markets), you get the “best of both worlds” without needing an additional “dummy” subscription.

That said, if you see mismatches or logs complaining “Market not present for sports data,” using a “dummy strategy” (or broad filter) can force Flumine to track _all_ possible markets, thereby capturing RaceStream updates even for those you don’t necessarily plan to bet on. Then your real strategy can “cherry-pick” from that data.

In Short

• *Yes*, Flumine does the heavy lifting once you tell it which markets (`market_filter`) and which data feed(s) (`sports_data_filter`) you want.

• You _can_ use a dummy strategy to ensure you subscribe to as many RaceStreams as you want, but it’s not strictly necessary if your single strategy is set up with the correct filters and streams.

• Typically, you only need a second “dummy” strategy if the streams you want to subscribe to are intentionally more encompassing than what your main betting strategy handles. If all you need are your main markets plus the RaceStream for them, a single strategy does the job

Thanks Liam, I understand now

---

## 2025-01-03 14:42:14 - general channel

**Tim**

Happy New year everyone! -- Extremely new to the group but have found it immensely useful so far.



I have a background working for market making firms in options + crypto space, interested in seeing how well this can translate into market making on a betting exchange. 



Hoping that with sound market making logic, I can create a profitable strategy that won't need a strong edge in terms of valuation.

---

## 2025-01-01 19:13:33 - general channel

**Mo**

Happy new year. As I’ve already mentioned to some of you, towards the end of last year I started working on some of my own strategies for the first time. Those of you who are familiar with my background and current circumstances will know that prior to this point, all of my betting activity has been part of syndicates that I’ve been a founding member of



My completely ludicrous goal for this year is for my take home pay from my own strategies to meet or exceed my take home pay from my existing syndicate strategies. I’m going to be documenting this process by providing a weekly update on the Slack comparing (axis free thank you very much) equity curves for the two, in addition to a running commentary on strategy developments and upcoming plans 

---

## 2025-01-01 15:35:11 - issues channel

**Brøndby IF**

[@UUCD6P13J](@UUCD6P13J) thanks! In this case, here in Brazil, it was changed from `.com` to `.[http://bet.br|bet.br](http://bet.br|bet.br)` and the `locale` in the Cookie appears as `pt_BR`



I'm going to research to learn how to edit an installed library using pip because I have no idea how to do it. Haha

---

## 2024-12-12 21:03:31 - issues channel

**ian mcneill**

Hi - apologies noob noob trying to reboot attempts at this. I have a fail when trying to install flumine  as output below shows. I will read line by line and try to resolve myself but if anyone can ident my idiocity easily and point me in the right direction, that's great - I'll keep this window open :wink:



Using cached typing_extensions-4.12.2-py3-none-any.whl (37 kB)

Building wheels for collected packages: pydantic-core

  Building wheel for pydantic-core (pyproject.toml) ... error

  error: subprocess-exited-with-error



  × Building wheel for pydantic-core (pyproject.toml) did not run successfully.

  │ exit code: 1

  ╰─&gt; [115 lines of output]

      Running `maturin pep517 build-wheel -i /Users/ian/miniconda3/envs/fex/bin/python --compatibility off`

      :package: Including license file "/private/var/folders/b6/6bn7gvx54lv2p4kjxcdz2s0h0000gn/T/pip-install-9p34jo51/pydantic-core_97eb83b395414c3f9cf1c80056b9a571/LICENSE"

      :tropical_drink: Building a mixed python/rust project

      :link: Found pyo3 bindings

      :snake: Found CPython 3.13 at /Users/ian/miniconda3/envs/fex/bin/python

      :satellite_antenna: Using build options features, bindings from pyproject.toml

      :computer: Using `MACOSX_DEPLOYMENT_TARGET=11.0` for aarch64-apple-darwin by default

         Compiling autocfg v1.1.0

         Compiling proc-macro2 v1.0.76

         Compiling unicode-ident v1.0.10

         Compiling target-lexicon v0.12.9

         Compiling python3-dll-a v0.2.9

         Compiling libc v0.2.147

         Compiling once_cell v1.18.0

         Compiling version_check v0.9.4

         Compiling cfg-if v1.0.0

         Compiling static_assertions v1.1.0

         Compiling heck v0.4.1

         Compiling zerocopy v0.7.32

         Compiling parking_lot_core v0.9.8

         Compiling rustversion v1.0.13

         Compiling scopeguard v1.1.0

         Compiling lexical-util v0.8.5

         Compiling allocator-api2 v0.2.16

         Compiling smallvec v1.11.2

         Compiling tinyvec_macros v0.1.1

         Compiling serde v1.0.195

         Compiling tinyvec v1.6.0

         Compiling memchr v2.6.3

         Compiling equivalent v1.0.1

         Compiling unicode-bidi v0.3.13

         Compiling regex-syntax v0.8.2

         Compiling ahash v0.8.7

         Compiling num-traits v0.2.16

         Compiling num-integer v0.1.45

         Compiling lock_api v0.4.10

         Compiling memoffset v0.9.0

         Compiling num-bigint v0.4.4

         Compiling lexical-write-integer v0.8.5

         Compiling lexical-parse-integer v0.8.6

         Compiling unicode-normalization v0.1.22

         Compiling lexical-write-float v0.8.5

         Compiling lexical-parse-float v0.8.5

         Compiling aho-corasick v1.0.2

         Compiling indoc v2.0.4

         Compiling serde_json v1.0.109

         Compiling percent-encoding v2.3.1

         Compiling unindent v0.2.3

         Compiling form_urlencoded v1.2.1

         Compiling regex-automata v0.4.3

         Compiling lexical-core v0.8.5

         Compiling idna v0.5.0

         Compiling ryu v1.0.14

         Compiling itoa v1.0.8

         Compiling uuid v1.6.1

         Compiling base64 v0.21.7

         Compiling url v2.5.0

         Compiling regex v1.10.2

         Compiling quote v1.0.35

         Compiling syn v2.0.48

         Compiling pyo3-build-config v0.20.2

         Compiling getrandom v0.2.10

         Compiling parking_lot v0.12.1

         Compiling hashbrown v0.14.3

         Compiling pyo3-ffi v0.20.2

         Compiling pyo3 v0.20.2

         Compiling pydantic-core v2.16.3 (/private/var/folders/b6/6bn7gvx54lv2p4kjxcdz2s0h0000gn/T/pip-install-9p34jo51/pydantic-core_97eb83b395414c3f9cf1c80056b9a571)

         Compiling indexmap v2.0.0

      error: failed to run custom build command for `pydantic-core v2.16.3 (/private/var/folders/b6/6bn7gvx54lv2p4kjxcdz2s0h0000gn/T/pip-install-9p34jo51/pydantic-core_97eb83b395414c3f9cf1c80056b9a571)`



      Caused by:

        process didn't exit successfully: `/private/var/folders/b6/6bn7gvx54lv2p4kjxcdz2s0h0000gn/T/pip-install-9p34jo51/pydantic-core_97eb83b395414c3f9cf1c80056b9a571/target/release/build/pydantic-core-39a2e9245b501e5a/build-script-build` (exit status: 101)

        --- stdout

        cargo:rustc-cfg=Py_3_6

        cargo:rustc-cfg=Py_3_7

        cargo:rustc-cfg=Py_3_8

        cargo:rustc-cfg=Py_3_9

        cargo:rustc-cfg=Py_3_10

        cargo:rustc-cfg=Py_3_11

        cargo:rustc-cfg=Py_3_12

        cargo:rustc-cfg=Py_3_13

        cargo:rerun-if-changed=python/pydantic_core/core_schema.py

        cargo:rerun-if-changed=generate_self_schema.py



        --- stderr

        Traceback (most recent call last):

          File "/private/var/folders/b6/6bn7gvx54lv2p4kjxcdz2s0h0000gn/T/pip-install-9p34jo51/pydantic-core_97eb83b395414c3f9cf1c80056b9a571/generate_self_schema.py", line 192, in eval_forward_ref

            return type_._evaluate(core_schema.__dict__, None, set())

                   ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        TypeError: ForwardRef._evaluate() missing 1 required keyword-only argument: 'recursive_guard'



        During handling of the above exception, another exception occurred:



        Traceback (most recent call last):

          File "/private/var/folders/b6/6bn7gvx54lv2p4kjxcdz2s0h0000gn/T/pip-install-9p34jo51/pydantic-core_97eb83b395414c3f9cf1c80056b9a571/generate_self_schema.py", line 240, in &lt;module&gt;

            main()

            ~~~~^^

          File "/private/var/folders/b6/6bn7gvx54lv2p4kjxcdz2s0h0000gn/T/pip-install-9p34jo51/pydantic-core_97eb83b395414c3f9cf1c80056b9a571/generate_self_schema.py", line 210, in main

            value = get_schema(s, definitions)

          File "/private/var/folders/b6/6bn7gvx54lv2p4kjxcdz2s0h0000gn/T/pip-install-9p34jo51/pydantic-core_97eb83b395414c3f9cf1c80056b9a571/generate_self_schema.py", line 54, in get_schema

            return type_dict_schema(obj, definitions)

          File "/private/var/folders/b6/6bn7gvx54lv2p4kjxcdz2s0h0000gn/T/pip-install-9p34jo51/pydantic-core_97eb83b395414c3f9cf1c80056b9a571/generate_self_schema.py", line 152, in type_dict_schema

            field_type = eval_forward_ref(field_type)

          File "/private/var/folders/b6/6bn7gvx54lv2p4kjxcdz2s0h0000gn/T/pip-install-9p34jo51/pydantic-core_97eb83b395414c3f9cf1c80056b9a571/generate_self_schema.py", line 195, in eval_forward_ref

            return type_._evaluate(core_schema.__dict__, None)

                   ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        TypeError: ForwardRef._evaluate() missing 1 required keyword-only argument: 'recursive_guard'

        thread 'main' panicked at [http://build.rs:29:9|build.rs:29:9](http://build.rs:29:9|build.rs:29:9):

        generate_self_schema.py failed with exit status: 1

        note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

      warning: build failed, waiting for other jobs to finish...

      :boom: maturin failed

        Caused by: Failed to build a native library through cargo

        Caused by: Cargo build finished with "exit status: 101": `env -u CARGO MACOSX_DEPLOYMENT_TARGET="11.0" PYO3_ENVIRONMENT_SIGNATURE="cpython-3.13-64bit" PYO3_PYTHON="/Users/ian/miniconda3/envs/fex/bin/python" PYTHON_SYS_EXECUTABLE="/Users/ian/miniconda3/envs/fex/bin/python" "cargo" "rustc" "--features" "pyo3/extension-module" "--message-format" "json-render-diagnostics" "--manifest-path" "/private/var/folders/b6/6bn7gvx54lv2p4kjxcdz2s0h0000gn/T/pip-install-9p34jo51/pydantic-core_97eb83b395414c3f9cf1c80056b9a571/Cargo.toml" "--release" "--lib" "--crate-type" "cdylib" "--" "-C" "link-arg=-undefined" "-C" "link-arg=dynamic_lookup" "-C" "link-args=-Wl,-install_name,@rpath/pydantic_core._pydantic_core.cpython-313-darwin.so"`

      Error: command ['maturin', 'pep517', 'build-wheel', '-i', '/Users/ian/miniconda3/envs/fex/bin/python', '--compatibility', 'off'] returned non-zero exit status 1

      [end of output]



  note: This error originates from a subprocess, and is likely not a problem with pip.

  ERROR: Failed building wheel for pydantic-core

Failed to build pydantic-core

ERROR: ERROR: Failed to build installable wheels for some pyproject.toml based projects (pydantic-core)

---

## 2024-12-02 10:34:50 - general channel

**JFP**

VPS noob question. Setting up a VPS for the first time to run my betting strats and have a question regarding security. There is plenty of info available on how to harden for external threats but how do you protect your data from the VPS provider? Does anyone here take extra steps to hide their setup when running on a VPS vs on their desktop?

---

## 2024-11-28 14:26:02 - general channel

**birchy**

My production setup is currently 2.6.0 and I upgraded that from 2.4.x and had no issues, so can't see it being any different for you.

---

## 2024-11-27 17:42:08 - general channel

**PeterLe**

I'm current using Flumine 2.4.1 and have been reluctant to upgrade it as its been rock solid...

I see the current version is 2.6.8



As I've not upgraded before (and as i still consider myself a beginner to Python :slightly_smiling_face: )...Is it a relatively straight forward?

Thanks

---

## 2024-11-27 09:48:52 - issues channel

**Tom**

2024-11-27 20:43:25,730 [DEBUG] __main__: Found order: Order 369539252565: Execution complete. Status: OrderStatus.EXECUTION_COMPLETE

2024-11-27 20:43:25,731 [DEBUG] __main__: Found order: Order 369539257045: Execution complete. Status: OrderStatus.EXECUTION_COMPLETE

2024-11-27 20:43:25,731 [DEBUG] __main__: Found order: Order 369541038302: Execution complete. Status: OrderStatus.EXECUTION_COMPLETE

2024-11-27 20:43:25,731 [ERROR] __main__: Print Marketbook delayed None

2024-11-27 20:43:25,731 [ERROR] __main__: Cross matching is False

2024-11-27 20:43:25,731 [ERROR] __main__: Version is 6300260619

2024-11-27 20:43:25,731 [ERROR] __main__: Market staleness check returned None.

2024-11-27 20:43:25,731 [WARNING] flumine.baseflumine: High latency between current time and MarketBook publish time

2024-11-27 20:43:25,731 [INFO] flumine.baseflumine: Adding: 1.236494334 to markets

2024-11-27 20:43:25,732 [DEBUG] urllib3.connectionpool: Starting new HTTPS connection (1): [http://api.betfair.com:443|api.betfair.com:443](http://api.betfair.com:443|api.betfair.com:443)

2024-11-27 20:43:25,803 [DEBUG] urllib3.connectionpool: [https://api.betfair.com:443](https://api.betfair.com:443) "POST /exchange/betting/json-rpc/v1 HTTP/11" 200 2392

2024-11-27 20:43:25,806 [INFO] root: OrdersMiddleware: Processing order 369500134776

2024-11-27 20:43:25,807 [INFO] root: OrdersMiddleware: New order trade created

2024-11-27 20:43:25,808 [INFO] flumine.order.order: Order status update: Execution complete

2024-11-27 20:43:25,808 [INFO] flumine.order.trade: Trade status update: Complete

2024-11-27 20:43:25,808 [INFO] root: OrdersMiddleware: Processing order 369502827322

2024-11-27 20:43:25,808 [INFO] root: OrdersMiddleware: New order trade created



Ok I wasn't logging very effectively. This is coming up inbetween running markets for the first time. The problem occurs after running a while as well though.



What kind of logs will be useful to see? Startup logs look normal

---

## 2024-11-27 08:48:02 - issues channel

**liam**

To confirm you have logging setup, no latency warnings, just all logs stop whilst you receive stale market books?

---

## 2024-11-23 20:33:14 - strategies channel

**Jhonny**

I'm new to this, but I store live esa and historical data in xtdb. previously, it was just in an binary format, which meant I had to read the whole file to query the market. xtdb time slices are pretty much instant, and allows me to play with many markets at once. drawback is it takes quite the amount of disk space

---

## 2024-11-01 19:03:25 - issues channel

**Unknown**

Hi all, I am receiving the following when trying to install flumine and create a marketrecorder. Any pointers to where I am going wrong would be really appreciated.

---

## 2024-10-31 15:54:00 - general channel

**Jhonny**

Hi everyone, I keep getting NOT_AUTHORIZED error when trying to use the esa api. I haven't used it in about 2 months; my live key just got accepted and it's my first time trying it out:



```:event {:op connection, :connectionId 206-311024154911-133459}

:event {:op status, :statusCode FAILURE, :errorCode NOT_AUTHORIZED, :errorMessage Connection is not authenticated: MarketSubscriptionMessage{marketFilter=MarketFilter{marketIds=[1.235241223], bspMarket=null, bettingTypes=null, eventTypeIds=null, eventIds=null, turnInPlayEnabled=null, marketTypes=null, venues=null, countryCodes=null, raceTypes=null}, marketDataFilter=com.betfair.platform.exchange.stream.api.domain.market.MarketDataFilter@70734c3a, initialClk='null', clk='null', conflateMs=null, heartbeatMs=null}, :connectionClosed true, :connectionId 206-311024154911-133459}

:stream-closed```

Last I tested with the delayed key, it worked. However, both live and delay keys are currently not working. Would appreciate anyone's help, thanks

---

## 2024-10-31 10:28:25 - general channel

**James**

Following on from Paul’s recommendation, I work with AWS in my day job extensively but don’t have the same limitations he does. Lightsail and Fargate serverless containers, and s3 for storage. Along with using a neon Postgres or digital ocean Postgres (for no cold start) is what I use for my market catalogues and betting records. Most of your record keeping can happen in background threads and can afford to be a little slower. 



Lightsail and neon are a bit more batteries included and a good place to start, and less knobs go turn. Fargate and a dedicated DB can let you squeeze some more out as you get deeper into it. 



This setup means my costs are low. I run my sims on my own hardware, even if slow it doesn’t cost me anything except electricity :relaxed: 

---

## 2024-10-23 10:20:15 - general channel

**liam**

`pip install flumine`

---

## 2024-10-19 15:22:05 - general channel

**Mo**

1. Look at the [https://github.com/betcode-org/betfair/tree/master/|source code](https://github.com/betcode-org/betfair/tree/master/|source code), especially [https://github.com/betcode-org/betfair/tree/master/examples|the examples](https://github.com/betcode-org/betfair/tree/master/examples|the examples) and [https://github.com/betcode-org/betfair/blob/master/betfairlightweight/resources/bettingresources.py|the resources](https://github.com/betcode-org/betfair/blob/master/betfairlightweight/resources/bettingresources.py|the resources) 

2. Familiarise yourself with the [https://betfair-developer-docs.atlassian.net/wiki/spaces/1smk3cen4v3lu3yomq5qye0ni/pages/2687473/Reference+Guide|Betfair API documentation](https://betfair-developer-docs.atlassian.net/wiki/spaces/1smk3cen4v3lu3yomq5qye0ni/pages/2687473/Reference+Guide|Betfair API documentation)

3. Install and use a decent IDE like [https://www.jetbrains.com/pycharm/|PyCharm](https://www.jetbrains.com/pycharm/|PyCharm) that will allow you to debug which will let you step through code line by line and examine the Python objects involved

---

## 2024-10-17 09:21:58 - issues channel

**NT**

Rookie question, is there a limit to how many times you can call trading.keep_alive()?



I am trying to keep my session alive to both: 1) read price data, and 2) make trades.



My strategy for doing this has been to: 1) call the keep alive endpoint and 2) use trading.keep_alive().



I'm pretty new to the betfairlightweights library, so sorry if I've missed something obvious on where to find this information!

---

## 2024-10-14 11:50:13 - random channel

**D C**

Surely the Benter edge stems from that hard earned data though (at least the raw edge from pricing). You could scrape racing post and apply the same statistical technique to build a model but I'd imagine it would perform poorly. I've enough confidence in that opinion to have so far not bothered doing it but who knows, maybe I've been sitting on a gold mine all this time. I know the HK racing setup is very different to racing in other countries, but I'm just talking in general - freely available generic data versus specifically formulated data requiring hundreds of man hours to get hold of is always going to lose out.

---

## 2024-10-07 14:20:04 - general channel

**liam**

How do you have this setup? ie. are you using tenacity or another way to restart on error?

---

## 2024-09-25 23:17:08 - general channel

**D C**

How old are your certs? I remember having to do an openssl hack ages ago because my certs were generated with an older encryption and I had to lower the security setting in the openssl configs (or something like that). I ended up generating newer certs in the end and the problem went away. I think the cause was something to do with a newer version of openssl.

Might not be related to your issue but thought I'd mention anyway as I've had SSL cert issues on fresh installs before.

---

## 2024-09-25 20:54:57 - general channel

**AndyL**

Hi, I am trying to setup a new AWS Ubuntu 24.04 VM, and have all the python bits and pieces setup, and my certs folder, but am getting the following SSL error. I'm sure i've had this before, but can't remember how I resolved it, any ideas anyone? I'm thinking maybe an OpenSSL problem?

```HTTPSConnectionPool(host='[http://identitysso-cert.betfair.com|identitysso-cert.betfair.com](http://identitysso-cert.betfair.com|identitysso-cert.betfair.com)', port=443): Max retries exceeded with url: /api/certlogin (Caused by SSLError(SSLError(524297, '[SSL] PEM lib (_ssl.c:3895)'```

---

## 2024-09-13 14:20:46 - random channel

**Paul**

I was listening to Nate Silver’s latest book, and as predicted he’s drifting like a boat :slightly_smiling_face:, but the other night I got to the point where he was talking about slots advantage players, and it actually does sound like there is +EV strategy lurking in there, just not widely known. Some of the podcasts I listen to (Risk of Ruin for example), sometimes cover video slots APs who seem to make a decent living with much less risk than Blackjack card counting, and with less variance than poker (even cash games), so I do wonder if I’m just being a prig about it. Silver made the point that many players don’t even want to win (sirens going off, staff coming over to shake your hand, becoming the centre of attention, etc.), which is indicative of a problem to me. But it does seem winnable as a form of gambling with the right approach (casino machines with particular payout mechanics, knowledge of the games themselves, etc.). Not my thing (haven’t the patience to spend 10 hours trawling around checking machines for a possible +EV setup), but I do wonder if it’s the approach to the game that’s the problem, not the game sometimes…

---

## 2024-09-05 19:04:15 - general channel

**Rob**

I'm just about ready to use flumine for live betting for the first time (rather than simulation).



Based on what I've read here, I know I'm doing more heavy computation that others. I'm happy with the speed of simulation but that's using 10 cores, and I'm not clear if flumine can use >1 core when running live? If a `process_market_book` call is still running when the next update arrives, what happens?



I'll try it tomorrow night so I guess I can also find out that way :slightly_smiling_face:

---

## 2024-09-04 13:38:53 - random channel

**D C**

Oh I agree and I don't absolve the industry of the harm it causes completely. But ultimately we do things we know we shouldn't or that will have a negative impact and ultimately that lies with the individual. Having said all that, if I were to place blame anywhere I would place it with credit card companies. Obviously it is very specific to my case, but the way these companies make it so so easy to just borrow more is disgraceful. Not sure if it still happens now, but every time I would near my credit limit, the companies would increase it by a couple of grand - without notice and not at my request. It is a complex setup because if I were not already heavily gambling to reduce my debt, I would never have made use of that extra credit and so the situation just got worse and worse until I reached the point of saying enough was enough. Strangely, it was taking out a Wonga payday loan that provided the biggest wake up call and I got myself straight after that point (after several years).

The strangest thing for me though is that the only issue I would have was with RNG games - never with sports betting and it really irks me that the UKGC refuse to distinguish between these types of betting. That said, many are able to play them for entertainment and suffer no problems at all so it really is a complicated issue.

---

## 2024-08-29 15:33:23 - issues channel

**casper**

[@U4H19D1D2](@U4H19D1D2) I’m using poetry and when going from 2.20.1 to the latest 2.20.2 version it uninstalls ciso8601 module. I have the following line:

```betfairlightweight = { version = "2.20.2", extras = ["speed"], source = "pypi-store" }```

So simply bumping the version here uninstalls ciso8601 for me (one of the “speed” requirements). Going back to 2.20.1 installs ciso8601 again. Any ideas what might be happening?

---

## 2024-08-25 09:45:28 - random channel

**Ralegh**

Bit of hassle first time but worth it, there’s a few awkward things with AWS like you need to add a security group to enable ssh and I think you need an IAM thing set up for S3 

---

## 2024-08-25 09:43:42 - random channel

**Ralegh**

My workflow is store everything in S3, then just write a few python/bash scripts to install all requirements and download the data i need, if the output is fitted model then you can just upload back to S3, boto3 is fine for that

---

## 2024-08-11 23:49:15 - general channel

**Paul**

Things that spring to mind others didn’t mention 



1. If you’re making rather than taking, and your prices are more than 1-2 pips away from each other (back/lay spread on US racing can be very broad), someone new could be doing the same strategy “inside” your prices. Can you go back and check what volume was matched at a price other than your own?

2. Your hosting setup has changed. Data centres get new links, retire old ones, your VPS could now have a noisy neighbour sucking bandwidth, and so on, and so on. Doesn’t take much to add 10ms latency onto a box. Even worse if you’re running from home (residential broadband especially over OpenReach makes no guarantees about anything, ever)

3. You were betting against another bot, you’ve taken their money, they’re gone.

4. Variance. Law of large numbers says you’ll have bad runs now and again and sounds like this has been running for a long time. I know you asked how to check it’s not chance alone, but one easy check is to wait another few days where the odds become smaller and smaller

---

## 2024-08-10 14:53:24 - general channel

**ShaunW**

.... Wish mine was user error, the source, config and server setup haven't been changed since July 2022.:thinking_face:

---

## 2024-08-08 10:35:14 - strategies channel

**Mo**

I have two different setups, both relatively old school. For the first there is an EC2 instance running 24/7 that processes new data on an hourly basis using a cron job. That “new data” is a combination of data scraped from APIs into an RDS Postgres database and log files uploaded to S3 from trading servers



For the second it’s a one off daily pipeline, also running on an EC2 box as a cron job. AWS EventBridge used to bring the box up and down so it’s only running for the duration of the pipeline. Database this time is Aurora Serverless for, in principle, cheaper database costs. In practice, regularly get fucked in the arse by IOPS

---

## 2024-08-06 21:58:03 - strategies channel

**birchy**

While we're mentioning S3... I'm at a point where I've got millions of markets saved via flumine market recorder and am wondering how others are filtering the files? e.g. say I want all GB horse races that turn inplay, what's the nicest way to find them? I've currently got a somewhat convoluted boto3 setup that paginates the market catalogues and then returns a list of market IDs that match my filters. I then download the files to local storage. I've played around with creating a local index file but it gets very big very quickly. I'm also pondering streaming direct from S3 -&gt; flumine rather than downloading them all as, similarly to [@U4H19D1D2](@U4H19D1D2), I'm processing through flumine to format data for model training.

---

## 2024-08-04 10:09:09 - strategies channel

**Aryan Kapoor**

Was wondering what the quickest way to get your "current position" one a particular runner within a market would be in flumine. Pretty new to flumine and currently running it in simulation mode but not having much luck. Have tried runner.matches which just returns an empty list continuously even though I am getting matches on a couple orders in the backtest.

---

## 2024-07-30 17:38:10 - strategies channel

**A**

Fairly new to Python.



After profiling and openeing in snakeviz, it looks as though most of the work is slowed down by things in `functools`  module - guess it’s the `@cachedproperty`  decorators I used.



Will have a play with that.



Thanks for the pointers :pray:

---

## 2024-07-30 08:25:25 - general channel

**liam**

So it looks like you have a good setup for simulating strategies however you need to be careful not to use this for signal creation i.e overfitting on historical data



[@UGV299K6H](@UGV299K6H) I would agree when it comes to inplay and/or strategies with a high edge but with pre race I have always found you need a lot of data.



With TPD I built something off the test data betfair had from Monday and went live on Tuesday thinking the edge would last a few weeks at best :joy: 

---

## 2024-07-27 19:28:16 - issues channel

**Derek C**

I think the problem I'm having is that the middleware is calling 'list_current_orders' each time a new market comes onto the stream, which at startup is quite a heavy workload in my particular setup. I changed it to only list orders for the market that was being added and that got me past my blocker.

---

## 2024-07-17 13:01:56 - general channel

**liam**

He is missed, I wonder if he ever recovered from going live for the first time with his 'model'

---

## 2024-07-07 11:26:06 - general channel

**Rob**

I'm looking to migrate my home rolled code to flumine, and so far everything seems to work well. I'll try to limit the beginner questions as much as I can, but wanted to check how people handle storing runner data to be able to use data like the last traded price over time, or traded volume in the last x minutes.



As far as I can tell, flumine doesn't offer anything like this out of the box?



Assuming I haven't missed anything, then I realise there are lots of options, including:



• a database, like postgres (or perhaps something like timescaledb if I can make the patterns fit), which is what I do with  my own code

• store as much data as I need in memory in Python, maybe using pandas/polars, or perhaps something like DuckDB?

• doing some heroics with the streaming market data in flumine to calculate what I need on the fly from the data that flumine already has?

Just checking if there's a consensus, or if I've missed other options?

---

## 2024-07-05 08:57:29 - issues channel

**Unknown**

here is the exact same setup on England server. this is probably what an AWS setup looks like

---

## 2024-07-04 17:37:11 - general channel

**birchy**

Having just seen the other thread on this subject, you could setup a simple scraper for yahoo finance and adjust the timestamps in the URL to match the betfair trading times. I'd probably go for hourly timestamps and save them all to a database or lookup table.

---

## 2024-06-09 23:55:23 - general channel

**Adrian**

Ok, so thanks for the suggestions. I tried using the backtestloggingcontrol example. A couple of things about the orders.txt output:

• It only recorded one of my bets in the first market when I had two

• It seems like `_process_cleared_markets` isn't running at all as I am not seeing any of those 'extra' fields appear

The logs are recording these things just fine, however, so it's just an issue with how the example is writing to orders.txt

Here is the code I'm running. the logging control is unchanged from the example. Any ideas?

```# Logger setup

logger = logging.getLogger()

custom_format = "%(asctime)s %(levelname) %(message)s"

formatter = jsonlogger.JsonFormatter(custom_format)

formatter.converter = time.gmtime

# Adding StreamHandler to output to sys.stderr

log_handler_stream = logging.StreamHandler()

log_handler_stream.setFormatter(formatter)

logger.addHandler(log_handler_stream)

# Adding FileHandler to output to a specified file

log_file_path = '/Users/adrian/Data/logs/betting.log'

log_handler_file = logging.FileHandler(log_file_path)

log_handler_file.setFormatter(formatter)

logger.addHandler(log_handler_file)

logger.setLevel(logging.INFO)

...

control = backtestloggingcontrol.BacktestLoggingControl()

framework.add_logging_control(control)

framework.run()```

Here is the output in the log file (correct and complete):

```{"asctime": "2024-06-09 11:24:35,566", "levelname": "INFO", "message": "Market level cleared", "taskName": null, "market_id": "1.229732924", "profit": -3.01, "bet_count": 2}

{"asctime": "2024-06-09 11:24:35,567", "levelname": "INFO", "message": "Cleared market", "taskName": null, "market_id": "1.229732924", "bet_count": 2, "profit": -3.01, "commission": 0.0}```

And here is the output from the backtestlogging control's orders.txt (incomplete):

```bet_id,strategy_name,market_id,selection_id,trade_id,date_time_placed,price,price_matched,size,size_matched,profit,side,elapsed_seconds_executable,order_status,market_note,trade_notes,order_notes

351219139942,take_bsp,1.229732924,9541871,8902a6e5-5745-4fbf-85ab-f68b02de316d,2024-06-09 11:21:00.429400,3.0,2.761065519504482,2.0,2,-2.0,BACK,54.478439,Execution complete,"2.68,2.74,2.68",,"2.507662997872342,2.0"```

---

## 2024-05-29 12:50:45 - general channel

**George**

OK got it. The order of the pip install matters. Flumine uninstalls Betconnect 0.2.1 and enforces 0.1.7

---

## 2024-05-11 08:57:55 - general channel

**Ammar**

Our entire AWS spend at work 8-10k / month for a pretty sophisticated setup… there’s probably some fat in what they’re doing there

---

## 2024-05-08 02:15:41 - general channel

**Unknown**

`seconds_to_start` done. moved this solely to listener instead of in `check_market_book`

`betfairlightweight==speed` done. downloaded it using `pip install 'betfairlightweight[speed]'` (needed the quotes to make it work)

`listener_kwargs` done. moved all market selection to `market_filter` instead of `check_market_book`

`dict.___get___` done. made better use of context objects to store selection_ids instead of looking up dictionary every time

`regex` not sure how to compile the code. I'm using pycharm; I thought it was done automatically when you run the code.



Other things: it would be great to implement the jupyterloggingcontrol with multiprocessing, but not sure if that's possible? I can get multiprocessing working without logging, but ideally I would like to be able to analyse my results as well. Any ideas?

---

## 2024-04-30 15:16:15 - strategies channel

**Ger Gleeson**

Ill piggy back on this thread. Also pretty new in this space. Im looking to move running my scripts from running on my local machine to run within the cloud etc. My scripts are pretty straight forward (at the moment). I just to have them hosted in IRE / UK to avoid geoblocking etc, and also run in "background". Im used to running scipts through Anaconda / jupyter lab / chrome etc but this seems vey slow (start up, general navigation etc) on a 1GB RAM setup within AWS lightsail. Anaconda documentation seems to recommend 4BG+ RAM, which looking at the lightsail pricing per month is coming out at 40 USD per month. Can anyone suggest simplier set up i can go with which requires less RAM etc would allow a cheaper rate per month

---

## 2024-04-23 10:54:22 - general channel

**Ammar**

If you partition by a market filter when opening flumine, you will get one connection per filter, so number of markets will be lower per stream / connection. 



I have not seen any posts about anyone hit a stream performance issue tho, so it may not be necessary. But my experience w the framework is still quite limited so I may be missing something



Also I believe betfair limits each api key to 10 streaming connections. 



You could try it and see … it may be a case of trial and error to get the right hardware and stream filter setup for your use case 

---

## 2024-04-18 23:02:57 - general channel

**Lee**

Look at how to setup logging from the examples, you should then see the reason 

---

## 2024-04-17 15:37:46 - general channel

**Massimo Abitante**

Hi everybody! Sorry for the dumb question but I'm a beginner.

When I subscribe to the markets stream (subscribe_to_markets) I get the updates regarding prices and sizes on the market.

I need to do some stuff only when prices change. My idea was to create my own "cache" saving the prices so when I get an update I can compare old prices (saved in my cache) with new prices (received from the stream).

Here I've seen this "cache" code that looks like something I could use instead of my own cache.

How can I access that cache? Is it something that betfairlightweight populates automatically or do I need to initialize it somehow?



Thank you very much

---

## 2024-04-15 11:23:07 - random channel

**Paul**

The best parts from the perspective of this group are how he got the job (he figured out how to market make in a game the bank setup, but in a way that others didn’t), and then how he made his money was stupendously easy.

---

## 2024-04-11 22:50:53 - issues channel

**Matthew Lawrence**

Hi, trying to use flumine for the first time. I'm starting off by testing an adjusted version of betfair data scientists: how to automate 2. I can see from the logging that the bets are never being matched, although they are being requested at the correct price and size. Any help would be appreciated.

```trading = betfairlightweight.APIClient('...','...!',app_key='...')

client = clients.BetfairClient(trading, interactive_login=True)



# Login

client = clients.SimulatedClient()

framework = FlumineSimulation(client=client)



# Logging

logger = logging.getLogger()

custom_format = "%(asctime) %(levelname) %(message)"

log_handler = logging.StreamHandler()

formatter = jsonlogger.JsonFormatter(custom_format)

formatter.converter = time.gmtime

log_handler.setFormatter(formatter)

logger.addHandler(log_handler)

logger.setLevel([http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))  # Set to logging.CRITICAL to speed up simulation



class BackFavStrategy(BaseStrategy):



    # Defines what happens when we start our strategy i.e. this method will run once when we first start running our strategy

    def start(self) -&gt; None:

        print("starting strategy 'BackFavStrategy'")



    def check_market_book(self, market: Market, market_book: MarketBook) -&gt; bool:

        # process_market_book only executed if this returns True

        if market_book.status != "CLOSED":

            return True



    def process_market_book(self, market: Market, market_book: MarketBook) -&gt; None:



        # Collect data on last price traded and the number of bets we have placed

        snapshot_last_price_traded = []

        snapshot_runner_context = []

        for runner in market_book.runners:

                snapshot_last_price_traded.append([runner.selection_id,runner.last_price_traded])

                # Get runner context for each runner

                runner_context = self.get_runner_context(

                    market.market_id, runner.selection_id, runner.handicap

                )

                snapshot_runner_context.append([runner_context.selection_id, runner_context.executable_orders, runner_context.live_trade_count, runner_context.trade_count])



        # Convert last price traded data to dataframe

        snapshot_last_price_traded = pd.DataFrame(snapshot_last_price_traded, columns=['selection_id','last_traded_price'])

        # Find the selection_id of the favourite

        snapshot_last_price_traded = snapshot_last_price_traded.sort_values(by = ['last_traded_price'])

        fav_selection_id = snapshot_last_price_traded['selection_id'].iloc[0]

        [http://logging.info|logging.info](http://logging.info|logging.info)(snapshot_last_price_traded) # logging



        # Convert data on number of bets we have placed to a dataframe

        snapshot_runner_context = pd.DataFrame(snapshot_runner_context, columns=['selection_id','executable_orders','live_trade_count','trade_count'])

        [http://logging.info|logging.info](http://logging.info|logging.info)(snapshot_runner_context) # logging



        for runner in market_book.runners:

            if runner.status == "ACTIVE" and market.seconds_to_start &lt; 60 and market_book.inplay == False and runner.selection_id == fav_selection_id and snapshot_runner_context.iloc[:,1:].sum().sum() == 0:

                trade = Trade(

                    market_id=market_book.market_id,

                    selection_id=runner.selection_id,

                    handicap=runner.handicap,

                    strategy=self,

                )

                order = trade.create_order(

                    side="BACK", order_type=LimitOrder(price=runner.last_price_traded, size=5)

                )

                market.place_order(order)



# Fields we want to log in our simulations

FIELDNAMES = [

    "bet_id",

    "strategy_name",

    "market_id",

    "selection_id",

    "trade_id",

    "date_time_placed",

    "price",

    "price_matched",

    "size",

    "size_matched",

    "profit",

    "side",

    "elapsed_seconds_executable",

    "order_status",

    "market_note",

    "trade_notes",

    "order_notes",

]



# Log results from simulation into csv file named sim_hta_2.csv

# If the csv file doesn't exist then it is created, otherwise we append results to the csv file

class BacktestLoggingControl(LoggingControl):

    NAME = "BACKTEST_LOGGING_CONTROL"



    def __init__(self, *args, **kwargs):

        super(BacktestLoggingControl, self).__init__(*args, **kwargs)

        self._setup()



    def _setup(self):

        if os.path.exists("sim_hta_2.csv"):

            [http://logging.info|logging.info](http://logging.info|logging.info)("Results file exists")

        else:

            with open("sim_hta_2.csv", "w") as m:

                csv_writer = csv.DictWriter(m, delimiter=",", fieldnames=FIELDNAMES)

                csv_writer.writeheader()



    def _process_cleared_orders_meta(self, event):

        orders = event.event

        with open("sim_hta_2.csv", "a") as m:

            for order in orders:

                if order.order_type.ORDER_TYPE == OrderTypes.LIMIT:

                    size = order.order_type.size

                else:

                    size = order.order_type.liability

                if order.order_type.ORDER_TYPE == OrderTypes.MARKET_ON_CLOSE:

                    price = None

                else:

                    price = order.order_type.price

                try:

                    order_data = {

                        "bet_id": order.bet_id,

                        "strategy_name": order.trade.strategy,

                        "market_id": order.market_id,

                        "selection_id": order.selection_id,

                        "trade_id": order.trade.id,

                        "date_time_placed": order.responses.date_time_placed,

                        "price": price,

                        "price_matched": order.average_price_matched,

                        "size": size,

                        "size_matched": order.size_matched,

                        "profit": order.simulated.profit,

                        "side": order.side,

                        "elapsed_seconds_executable": order.elapsed_seconds_executable,

                        "order_status": order.status.value,

                        "market_note": order.trade.market_notes,

                        "trade_notes": order.trade.notes_str,

                        "order_notes": order.notes_str,

                    }

                    csv_writer = csv.DictWriter(m, delimiter=",", fieldnames=FIELDNAMES)

                    csv_writer.writerow(order_data)

                except Exception as e:

                    logger.error(

                        "_process_cleared_orders_meta: %s" % e,

                        extra={"order": order, "error": e},

                    )



        [http://logger.info|logger.info](http://logger.info|logger.info)("Orders updated", extra={"order_count": len(orders)})



    def _process_cleared_markets(self, event):

        cleared_markets = event.event

        for cleared_market in cleared_markets.orders:

            [http://logger.info|logger.info](http://logger.info|logger.info)(

                "Cleared market",

                extra={

                    "market_id": cleared_market.market_id,

                    "bet_count": cleared_market.bet_count,

                    "profit": cleared_market.profit,

                    "commission": cleared_market.commission,

                },

            )



# Searches for all betfair data files within the folder sample_monthly_data_output

data_folder = r"C:\Users\matth\OneDrive\Documents\output_2022_02"

data_files = os.listdir(data_folder,)

data_files = [f'{data_folder}/{path}' for path in data_files]



# Set Flumine to simulation mode

client = clients.SimulatedClient()

framework = FlumineSimulation(client=client)



# Set parameters for our strategy

strategy = BackFavStrategy(

    # market_filter selects what portion of the historic data we simulate our strategy on

    # markets selects the list of betfair historic data files

    # market_types specifies the type of markets

    # listener_kwargs specifies the time period we simulate for each market

    market_filter={

        "markets": data_files,

        'market_types':['MATCH_ODDS', 'BOTH_TEAMS_TO_SCORE'],

        "listener_kwargs": {"inplay": False, "seconds_to_start": 80},

        },

    max_order_exposure=1000,

    max_selection_exposure=1000,

)

# Run our strategy on the simulated market

framework.add_strategy(strategy)

framework.add_logging_control(

    BacktestLoggingControl()

)

framework.run()```



---

## 2024-04-08 20:56:09 - general channel

**foxwood**

Put the logs into INFO mode - you'll then see stuff like "Starting OrderStream 1000" in the default flumine setup.

---

## 2024-04-08 08:53:32 - issues channel

**Johnnb**

That's the only log I've got sorry. I'm pretty new to linux and aws. I ran the code from the command line in a detached shell. Could that have caused the issue?

---

## 2024-03-29 19:13:51 - general channel

**liam**

Yeah, just setup cloudwatch and all your problems will be solved. Then you can add something like sentry to tell you when something bad happens (Err/Critical) 

---

## 2024-03-29 18:31:37 - random channel

**Oliver**

numba is good if your code is slowed down by the python logic gluing all the pandas bits together (assuming you can't just use pandas more efficiently), so you can use something like `@numba.jit` to compile some block of code into machine code without you having to deal with it much. Its unlikely to be of huge value to you right now if pandas and numpy are new to you though as it is usually the use of pandas that can be improved most first.



PyArrow can be used as an alternative backend/storage engine for pandas, it has some merits, in particular if you write your data to disk and read it back later. Still fairly new in pandas so could be an excuse to avoid it as well, but it can read a CSV in parallel and be a lot faster.



I'd have thought you could get a fair bit more speed out of of pandas/python if you wanted as 250 rows a second sounds fairly slow to me so I imagine there's other places you can get speed first. I'd recommend profiling a run with a subset of data using [https://github.com/P403n1x87/austin?tab=readme-ov-file#synopsis|austin](https://github.com/P403n1x87/austin?tab=readme-ov-file#synopsis|austin) and then viewing the results with [https://github.com/jlfwong/speedscope?tab=readme-ov-file#speedscope|speedscope](https://github.com/jlfwong/speedscope?tab=readme-ov-file#speedscope|speedscope). This is probably to key combination I've found for optimising this kind of code.



Then again it sounds like you/your house benifits from the processing time [https://xkcd.com/303/](https://xkcd.com/303/)

---

## 2024-03-29 17:23:32 - general channel

**PeterLe**

Is it good practice to save your log files?

At the moment my stuff is just sent to the terminal window.

It seems I can do it like so :



`import logging`

`import time`

`from pythonjsonlogger import jsonlogger`



`# Logger setup`

`logger = logging.getLogger()`

`custom_format = "%(asctime)s %(levelname)s %(message)s"`

`formatter = jsonlogger.JsonFormatter(custom_format)`

`formatter.converter = time.gmtime`



`# Adding StreamHandler to output to sys.stderr`

`log_handler_stream = logging.StreamHandler()`

`log_handler_stream.setFormatter(formatter)`

`logger.addHandler(log_handler_stream)`



`# Adding FileHandler to output to a specified file`

`log_file_path = 'path/to/your/logfile.log'`

`log_handler_file = logging.FileHandler(log_file_path)`

`log_handler_file.setFormatter(formatter)`

`logger.addHandler(log_handler_file)`



`logger.setLevel([http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))`



What happens if you encounter an issue (Eg latency high )which generates lots of messages, is there not a danger you could fill your disk space up quickly with the output etc?

I expect the answer will be yes - save your log files, but what is considered good sys management ? do you clear them out each day etc?

Thanks in advance

---

## 2024-03-29 13:05:07 - issues channel

**Ammar**

Hi guys - first time Flumine user, bit stuck, can’t see what I’ve done wrong :thread:

---

## 2024-03-08 17:22:21 - random channel

**Paul**

I’m willing to wager a pint that some people here haven’t typed `pip install flumine --upgrade` in a long time… :slightly_smiling_face:

---

## 2024-03-07 14:46:54 - issues channel

**foxwood**

Had an issue last week with a test strategy running live. It was going through the runners placing bets and then hit an outlier not allowed for that resulted in a divide by zero. Flumine neatly ate the exception and fed the next `mc` to the strategy which placed bets, hit the outlier again and crashed again - rinse and repeat.



The impact of this was to start draining the bank rather quickly - fortunately I was monitoring it but it still took a big bite. After investigating, I discovered that flumine ate non-flumine exceptions due to `config.raise_errors = False` Taken 2+ years to fall down that hole. I know all the guff about testing and defensive code etc but the reality is that most of us are in permanent beta and things slip through.



I think this should default to `True` which would stop any runaways like mine and, more importantly, would be the expected behaviour for people new to flumine. In the meantime all my flumine wrappers set it to `True` right at the start.

---

## 2024-03-03 22:58:59 - general channel

**Unknown**

Hello, I'm new to simulating bets with Flumine and am having problems with a LAY bet at SP. Here's my code:



```client = clients.SimulatedClient()

framework = FlumineSimulation(client=client)



...



order = trade.create_order(

    side = "LAY",

    order_type = LimitOrder(price=2, size=10, persistence_type="MARKET_ON_CLOSE"),

)

market.place_order(order)```

As you can see my stake is £10. In my test market the runner BSP is 4.00. Let's say the runner wins, I expect to lose £30. But Flumine says I lost £3.29, treating £10 as the liability.



Based on the attached Betfair docs, this would be correct with a *MarketOnCloseOrder*. But not with a *LimitOrder*: Betfair treats the latter's stake as the stake and not liability.



Is my understanding incorrect?

---

## 2024-02-26 07:59:58 - general channel

**Mo**

I've just tried running the above Python code with the following changes:



1. `market_id` set to `1.225270654`

2. Added `app_key=""` argument to `betfairlightweight.APIClient`

With the following output:



```[&lt;RaceCard&gt;]

RaceCard £9000.00 1 Indian Louis, 2 Travail D'orfevre, 3 Nights In Venice

Fia Fuinidh (IRE) Made all in 2m handicap hurdle here last winter and promise when runner-up twice in 2m handicap chases this winter. Faded into fourth back from wind surgery here (2m) 13 days ago and remains to be seen whether this step up in trip suits.

Indian Louis (IRE) Dual point winner who left his qualifying runs over hurdles behind when making a winning chase debut at Musselburgh (2½m) on New Year's Day. Let down by his jumping when only fifth over C&amp;D since but he's probably worth another chance.

Travail D'orfevre (FR) Scored at Carlisle (2m) on his return and good runner-up efforts on all 3 outings since, including C&amp;D. Enters calculations again.

Jolly Nellerie (FR) Fairly useful winning hurdler in France but yet to fire in 4 starts so far for his current trainer, including switched to fences at Newcastle before Christmas. Sports first-time blinkers back from a short break.

Nights In Venice Fair maiden handicap hurdler who took to chasing when fourth of 12 over 3m at Carlisle 3 weeks ago but he didn't deliver much off the bridle (not for first time). Possible the return to shorter,

Ardera Cross (IRE) Nine-time course winner, the latest when accounting for Fia Fuinidh over 2m as the turn of the year. Does need to shrug off a poor run back here since, though.

[{'raceId': '1.2.1240226.1', 'markets': [{'marketId': '1.225270654', 'marketType': 'WIN', 'numberOfWinners': 1}, {'marketId': '1.225270659', 'marketType': 'EACH_WAY', 'numberOfWinners': 2}, {'marketId': '1.225270656', 'marketType': 'PLACE', 'numberOfWinners': 2}, {'marketId': '1.225270658', 'marketType': 'OTHER_PLACE', 'numberOfWinners': 3}, {'marketId': '924.395521980', 'marketType': 'WIN', 'numberOfWinners': 1}, {'marketId': '927.264606400', 'marketType': 'WIN', 'numberOfWinners': 1}], 'distance': 4510, 'startDate': '2024-02-26T14:05:00.000Z', 'raceClassification': {'code': 'H', 'classification': 'Handicap', 'classificationAbbr': 'Hcap', 'displayName': 'Handicap Chase', 'displayNameAbbr': 'HcapCh'}, 'raceTitle': 'New Bet-In-Race With Coral Handicap Chase (Qualifier) (4)', 'raceType': {'key': 'C', 'abbr': 'Ch', 'full': 'Chase'}, 'raceClass': 4, 'course': {'courseId': '1.2', 'name': 'Ayr', 'country': 'Scotland', 'countryCode': 'GB', 'courseType': 'Both', 'timeformCourseCode': 'Ayr', 'surfaceType': 'Turf', 'timezone': 'Europe/London'}, 'going': {'key': 'V', 'abbr': 'Hy', 'full': 'Heavy'}, 'prizeMoney': '£9000.00', 'eligibilityCriteria': {'ageLimitText': '5yo+'}, 'betfairMeetingId': '33052007', 'raceIdExchange': '33052007.1405', 'resultsStatus': 'NoResults'}]

{'raceId': '1.2.1240226.1', 'markets': [{'marketId': '1.225270654', 'marketType': 'WIN', 'numberOfWinners': 1}, {'marketId': '1.225270659', 'marketType': 'EACH_WAY', 'numberOfWinners': 2}, {'marketId': '1.225270656', 'marketType': 'PLACE', 'numberOfWinners': 2}, {'marketId': '1.225270658', 'marketType': 'OTHER_PLACE', 'numberOfWinners': 3}, {'marketId': '924.395521980', 'marketType': 'WIN', 'numberOfWinners': 1}, {'marketId': '927.264606400', 'marketType': 'WIN', 'numberOfWinners': 1}], 'distance': 4510, 'startDate': '2024-02-26T14:05:00.000Z', 'raceClassification': {'code': 'H', 'classification': 'Handicap', 'classificationAbbr': 'Hcap', 'displayName': 'Handicap Chase', 'displayNameAbbr': 'HcapCh'}, 'raceTitle': 'New Bet-In-Race With Coral Handicap Chase (Qualifier) (4)', 'raceType': {'key': 'C', 'abbr': 'Ch', 'full': 'Chase'}, 'raceClass': 4, 'course': {'courseId': '1.2', 'name': 'Ayr', 'country': 'Scotland', 'countryCode': 'GB', 'courseType': 'Both', 'timeformCourseCode': 'Ayr', 'surfaceType': 'Turf', 'timezone': 'Europe/London'}, 'going': {'key': 'V', 'abbr': 'Hy', 'full': 'Heavy'}, 'prizeMoney': '£9000.00', 'eligibilityCriteria': {'ageLimitText': '5yo+'}, 'betfairMeetingId': '33052007', 'raceIdExchange': '33052007.1405', 'resultsStatus': 'NoResults'}```

---

## 2024-02-20 12:51:33 - general channel

**Michael**

[@U06KP54CEMR](@U06KP54CEMR) I think years and years ago I based my first python based bot on something you published, back in the days of polling. Does that sound right? That was my first contact with python and the first time I stepped away from using third party software. It was super simple, just a big loop of a handful of functions and nothing else. If that is right I think maybe [@U4H19D1D2](@U4H19D1D2) based his early efforts on the same thing. If I've got this right then I've a lot to thank you for.

---

## 2024-02-20 12:19:12 - general channel

**Mark Littlewood**

Hi All I am new to this chat so looking forward to exploring the content. My background is in Machine Learning modelling for sports. I have also written a series of blog posts on accessing the Betfair API. For those of you interested in no code required sports betting modelling I have created a GUI based approach to ML modelling sports data called MySportsAI. My blog is [https://markatsmartersig.wordpress.com/](https://markatsmartersig.wordpress.com/)

---

## 2024-02-13 21:33:20 - issues channel

**Derek C**

Am I right in thinking that the flumine historical stream (RaceStream) doesn't like races that started early? For example, if the race id ends in, ".1924" then these hours and minutes will be taken as the race_cache.start_time. If, however, the race started early then the updates will have a 'pt' publish time before this and be ignored. I'm trying to track down an elusive issue in my simulation setup. In my example, the updates in the historical stream file all have a 'pt' value earlier than the expected start time embedded in the race id and this seems to cause the whole file to be ignored by FlumineRaceStream._process()

---

## 2024-02-13 09:22:39 - strategies channel

**Unknown**

[@UPMUFSGCR](@UPMUFSGCR) as you know, i'm only a beginner at this sort of thing..but this is the output of shap when i tried it.

I thought it may help you visualise it.

(For what it is worth; this is in-play horses and the top feature was something that Id never even focused on before. It surprised me that it was even listed (but made total sense after I thought about it ). So worthwhile playing around with it

---

## 2024-02-05 09:46:11 - random channel

**D C**

I'd be surprised if this doesn't breach T&amp;C to be honest. For example, I've been logging horses and dogs for years. But tomorrow I might fancy analysing football and the only way I could do that is to buy historical data. If this were setup, I could just piggyback other users historical data. Surely it's no different to data sharing?

---

## 2024-02-01 15:43:56 - general channel

**Simon Chan**

Thank for the info. I try the same VPN provider on my smartphone and placing bets seems to work

. I use Surfshark with their dedicated IP setup. It looks like my laptop might be part of the problem. I will debug it further tomorrow

---

## 2024-02-01 12:53:59 - issues channel

**Brian Morton**

Guy's I am not new to trading but I am new to Flumine and I am now starting to follow the instructions in 'How To Automate 1' in Betfair



What is your take on the paragraph



You can use the Flumine package with or without certificates. There have been quite a lot of discussions of how useful the security certificates are on the [https://betcode-org.slack.com/ssb/redirect|Betcode (formerly Betfairlightweight) slack group](https://betcode-org.slack.com/ssb/redirect|Betcode (formerly Betfairlightweight) slack group), but the general consensus is that its not too useful. Considering it is an extreme hassle to create the certificates and there is no really added benefit I prefer to log in without the certificates.



Do you guys use certificates or not.

---

## 2024-02-01 12:51:43 - issues channel

**Brian Morton**

Guy's I am not new to trading but I am new to Flumine and I am now starting to follow the instructions in 'How To Automate 1' in Betfair

---

## 2024-01-28 10:17:04 - general channel

**Unknown**

1. Download this file: [https://betcode-org.slack.com/files/U4H19D1D2/F06E327EJM8/betcode_slack_export_mar_11_2017_-_jan_16_2024.zip](https://betcode-org.slack.com/files/U4H19D1D2/F06E327EJM8/betcode_slack_export_mar_11_2017_-_jan_16_2024.zip)

2. Install the slack-export-viewer Python package; [https://github.com/hfaran/slack-export-viewer](https://github.com/hfaran/slack-export-viewer)

3. Unzip the export

4. `slack-export-viewer -z ./betcode\ Slack\ export\ Mar\ 11\ 2017\ -\ Jan\ 16\ 2024`

---

## 2024-01-28 08:16:40 - general channel

**Jonjonjon**

Wasn't Misha still at the getting started phase? But with a big starting bankroll? He was kind enough to share his record and it was super volatile.

---

## 2024-01-28 08:09:11 - general channel

**liam**

That would explain a lot, I remember the slack having evidence of some professionals but the discord seems to be more of a getting started help forum. They need Misha to come back..

---

## 2024-01-28 03:42:14 - issues channel

**Adrian**

Thanks birchy, i'll try this tonight when i get home. It's just a fresh Linux install so I haven't changed anything other than installing the default python that comes with miniconda

---

## 2024-01-23 09:20:27 - general channel

**Jared King**

my 'setup' is like (eg):

```horseracing_main.py - trading, client and framework created here

greyhounds_main.py

strategies/

   horseracing1.py - BaseStrategy classes

   horseracing2.py

   horseracing3.py

   greyhounds1.py```

---

## 2024-01-18 14:52:41 - random channel

**PeterLe**

Thanks for your help folks; helps keep it interesting as a beginner :+1:

---

## 2024-01-18 13:01:49 - random channel

**PeterLe**

Thanks [@UBS7QANF3](@UBS7QANF3) I hadnt thought of looking in your utils package. When I comapred your version with the ChatGpt version it stated that there were some pros ie :

(Where it states 'Your' it means betfairutils)

• Complexity: Your version adds a bit more complexity due to additional type checks and handling different scenarios (like the `Side.BACK` check). While this might be necessary for your specific use case, it can introduce slight overhead compared to the more streamlined version.

• Flexibility: Your version is more flexible in handling different data structures (like `PriceSize` objects and dictionaries), which can be advantageous if your data comes in various formats.

• Error Handling: Neither version uses explicit exception handling within the loop, which is good for performance. However, the reliance on external functions like `get_best_price_size` and `iterate_active_runners` means that error handling should be considered within these functions to avoid unexpected crashes.

• Readability and Maintainability: The use of type hints and clear separation of logic in your version can make the code more readable and maintainable, albeit at a slight cost to performance.

and conclusion ;

Conclusion:

• Performance: The streamlined version I provided is likely to be slightly faster due to its simplicity and direct approach. However, the difference might be marginal depending on the implementation details of the helper functions you use.

• Applicability: If your codebase frequently deals with different data structures for market data or requires additional checks like the `Side.BACK` logic, your version could be more suitable despite the potential slight performance trade-off.

So it may suit the more accomplished/better programmer than me (mine is just very basic stuff)? Ill need to just try and understand it better really and see if it would benefit me?

Hi [@UUCD6P13J](@UUCD6P13J) no ive never used cprofile before. Is it worth learning as a relative beginner or is it more intended for the advanced programmer?

---

## 2024-01-16 12:29:45 - random channel

**Mo**

This is well and truly random but I've been playing this game recently: [https://store.steampowered.com/app/1404850/Luck_be_a_Landlord/](https://store.steampowered.com/app/1404850/Luck_be_a_Landlord/) (also available on iOS and Android) and thought it might appeal to some of you other degenerate gamblers. The setup is bizarre but you're basically building a slot machine symbol by symbol where every symbol is unique in terms of how much money it pays out and its interactions with the other symbols in your machine. It's very good for making you think about how to maximise expected value

---

## 2024-01-15 20:40:56 - general channel

**Steve**

Hello :wave:  apologies I'm new to this and I'm sure you've probably seen my questions 100 times before, but I was just hoping for a little direction if possible:



1. I'm looking to parse the historic data files for American football data and preferably to analyse in a csv file.  For this I thought I might need to use betfairlightweight rather than flumine? As I'm not looking to do automatic trading atm I thought BFW was the right program for that?

2. If so, I was looking at the [https://github.com/betcode-org/betfair/blob/master/examples/examplestreaminghistorical.py|example historical stream](https://github.com/betcode-org/betfair/blob/master/examples/examplestreaminghistorical.py|example historical stream). Given the data file structure is in the format of `{month}/{day}/{marketID}/{...bz2}` I guess I need to traverse the folders and load in each file individually?

3. I've seen people talk about recording prices themselves though the [https://github.com/betcode-org/flumine/blob/master/examples/strategies/marketrecorder.py|MarketRecorder](https://github.com/betcode-org/flumine/blob/master/examples/strategies/marketrecorder.py|MarketRecorder) rather than buying historic data after the fact. Do you generally put that on an EC2 or something running 24/7?

Apologies if these are all very basic!

---

## 2024-01-14 15:31:12 - issues channel

**Derek C**

Possibly related issues: I do not see TPD data coming through Flumine from version 2.3.0 onwards. I've been upgrading from old versions so could have missed some steps.



> pip3 install flumine==2.2.7

I see output from "process_sports_data"



> pip3 install flumine==2.3  # or 2.5.4, 2.5.6

no output from following example:



```

class ExampleStrategy(BaseStrategy):

    def process_sports_data(self, market, sports_data) -> None:

        # called on each update from sports-data-stream

        print('***',market, sports_data)



client = clients.BetfairClient(trading)



framework = Flumine(client)



strategy = ExampleStrategy(

    market_filter=streaming_market_filter(

        event_type_ids=["7"], market_types=["WIN"],

            country_codes=['GB' ],

    ),

    sports_data_filter=['raceSubscription'],  "raceSubscription"

)

framework.add_strategy(strategy)



framework.run()```



---

## 2024-01-14 15:10:05 - issues channel

**Derek C**

2.19.1

But the way I created the test was to just pip install flumine. I didn't specifically install the dependencies

---

## 2024-01-02 15:50:09 - general channel

**Ricky**

Hi everyone! I'm fairly new to the automated betting world and would like to start by getting my hands on some of the historical data that betfair supplies at [https://historicdata.betfair.com/#/home](https://historicdata.betfair.com/#/home). Problem is that I live in Sweden and this service is not accessible for us swedes... Does anyone know an alternate way to get access to historical data? Thanks in advance! :raised_hands:

---

## 2023-12-19 11:12:56 - general channel

**Peter**

Flumine will only see its own orders. But you could use betfairlightweight in a work or middleware to inject those that you place directly on the Betfair website. There's [https://github.com/betcode-org/flumine/blob/master/examples/middleware/orders.py|a middleware example that does this](https://github.com/betcode-org/flumine/blob/master/examples/middleware/orders.py|a middleware example that does this) to repair the setup when Flumine is re-started that could be adapted to infill your manually-placed bets.

---

## 2023-12-12 09:17:59 - general channel

**Justice**

[@UUE6E1LA1](@UUE6E1LA1) Yes, you can get access to the Proform DB. If I remember, it installs an old version of SQL Server locally on your machine. You can view the raw database with something like SSMS or DataGrip, export it elsewhere and get it into the format you want

---

## 2023-12-10 16:03:10 - issues channel

**Pietro Perrone**

Hello all! I am new to the channel, and I want to first thank all of you for putting up such a great collaborative community.

I am looking to download historical data odds using the historical data methods provided by betfairlightweight.

2 questions on this:

• I need to retrieve all the odds for tennis matches from 2015. Do you think it is better to use `get_my_data` or `create_historical_stream` ?

• I really need to differentiate between pre-match and in-play odds. Is there an easy way of doing so?

Thanks in advance!

---

## 2023-12-05 16:06:05 - issues channel

**ChrisM**

ah ok, the live key is the one you pay the £299 fee for? which is not a problem i was just hoping to get setup in testing first

---

## 2023-11-20 13:56:54 - random channel

**Ralegh**

To be honest if you’ve got flat files working with your setup there’s basically no reason to change. Also storing ML models in a database seems kinda pointless to me, how would you use it any different to on disk?

---

## 2023-11-17 13:10:08 - general channel

**Unknown**

Hi I'm new to the `betfairlightweight` Python library. I'm aiming to get a data stream of prices over time for live matches that's reflective of the viz that the Betfair UI shows you (below). Is there a method that will do this for live events, or do I need to use the `Streaming API` throughout the event and subsequently store the results manually?

---

## 2023-11-16 07:30:40 - general channel

**Chandana Tennakoon**

Hello, I am exploring the betfairlightweight library and am very new to this. I cannot find from the in-built documentation complete information about methods and members of the classes in the library. Although I have managed to hazard some guesses from going through sample code what some of these are, is there a place where there is a proper documentation? (e.g. where is market_book.market_definition.market_type or runner.ex.available_to_back is documented)

---

## 2023-11-12 23:03:22 - random channel

**JL**

yes, basically in your created directory:

```python3 -m venv .venv

source .venv/bin/activate

pip install flumine```

---

## 2023-11-11 06:57:07 - random channel

**Adrian**

What is the benefit of keeping it all in a database as opposed to just the original format on the hard drive? I think about learning SQL all the time but the simplicity of using files straight off the disk keeps me from getting started. I imagine it's good if you want to run queries on a bazillion rows at once but so far pandas + flumine + disk has been adequate.

---

## 2023-10-27 14:14:31 - issues channel

**George**

Actually, I think it is a race condition. Seems like the `flumine.markets` get added after the worker gets called the first time.

---

## 2023-10-27 14:10:08 - issues channel

**Derek C**

I'm not a flumine expert, but I think to get quality assistance with this you would need to provide more concrete information about what you are doing - market filter, worker setup etc. It's quite hypothetical at the moment and you are asking people to guess what might be wrong with some code they can't see.

---

## 2023-10-22 19:01:55 - general channel

**Trex44**

Hey Guys. So the TLDR is the fix worked. Thanks very much.



A few more details. I set up another instance and ran the patch on that one. I ran the same strategies at the same stakes on the patched instance as the for the unpatched instance. I couldn't get the install to work using the CLI even though everything seemed to download/install ok so I manually overwrote the workers file using the updated workers file Lee created. It might not have worked via the CLI because I am inexperienced using GitHub so did something wrong.



All the printed results in the the patched instance had the 'profit' column in the csv filled in correctly. The unpatched instance displayed the same error as before with zeros in sometimes present in the profit column.



• I have noticed that sometimes the same line or set of lines will be written twice. This occurs on both instances but not necessarily for the same results on each instance. My guess is its a different bug to the one that has just been fixed. It doesn't bother me as I only upload each unique bet id once to my results database. See below for an example from the patched instance. The same strategy executes on two markets but the results from the first market print again after the second.

`325529200273,strat_x,1.219940406,6846739,e75cea8e-7019-11ee-b135-17589b09afd9,2023-10-21 13:58:25.603658,3.65,3.7,1,1,-1.0,BACK,0.034584,Execution complete,"3.65,3.7,3.7",,"{'runner_id': 6846739}"`



`325538377913,strat_x,1.219940554,15914199,ca20765c-701e-11ee-b135-17589b09afd9,2023-10-21 14:33:24.004443,3.4,3.4,1,1,-1.0,BACK,0.021638,Execution complete,"3.4,3.45,3.45",,"{'runner_id': 15914199}"`



`325529200273,strat_x,1.219940406,6846739,e75cea8e-7019-11ee-b135-17589b09afd9,2023-10-21 13:58:25.603658,3.65,3.7,1,1,-1.0,BACK,0.034584,Execution complete,"3.65,3.7,3.7",,"{'runner_id': 6846739}"`





• A strategy that was active on both instances and fired on both instances over the two day test period fired on one extra market on the patched instance than on the un patched instance. Uncertain why this happened, possible could be strategy related so will need to look into the code to see. 

I will leave the two instances running the next few days to see what is generated. The unpatches instance is one I use at low stakes for my test strategies. I will be upgrading my main instance to the new patch of the back of these results.

---

## 2023-10-22 13:07:53 - strategies channel

**Adam**

Apology in advance if this is the incorrect channel to ask this question. If so, please let me know where to go, thank you :slightly_smiling_face:



Hey all, I’m new to flumine and I’m following through this amazing guide: [https://betfair-datascientists.github.io/tutorials/How_to_Automate_1/](https://betfair-datascientists.github.io/tutorials/How_to_Automate_1/). When it comes to streaming horse markets, I was wondering if there is a way to continually add markets to an strategy (that is already streaming events) as the markets become live?

The reason being is I want to set up the strategy at the beginning of the day, and as races become live, I want to add that race to the strategy for processing, and remove it as the race becomes closed or suspended. I can see there’s a `remove_market` method in the `BaseStrategy` but I can’t see an equivalent `add_market`. This suggests that the way it’s supposed to work is that we create the strategy filtering on all the australian horse markets at the beginning of the day and remove them when they’re suspended? There’s also a method called `process_new_market` but is this called when a market becomes live or does this suggest it can be used for what I’m asking?

---

## 2023-10-19 15:00:05 - general channel

**liam**

[@U03N4QBJ0TV](@U03N4QBJ0TV) can you try using Lee's [https://github.com/betcode-org/flumine/pull/712|fix](https://github.com/betcode-org/flumine/pull/712|fix) and report back?



```pip install git+[https://github.com/lunswor/flumine.git@handle-clearing-orders-only-once-settled](https://github.com/lunswor/flumine.git@handle-clearing-orders-only-once-settled)```

---

## 2023-10-13 13:09:05 - general channel

**andres gonzalez**

Hello, very new to using the betfair API, at the moment I'm simply trying to create a bot that tracks prices of specific markets I want to and want to to notify me when available back or lay liquidity is what I'm looking for. going through the betfairlightweight GitHub to try and do this step by step. Currently trying to find in the documentation all the use cases of trading.betting on python.

---

## 2023-10-11 00:00:52 - general channel

**foxwood**

Good stuff and a nice solution to managing the data warehouse - which I keep meaning to do ! Had a quick look and a couple of gotchas from my setup that may also apply to others you might like to consider at some point in the future

1. Rightly or wrongly all my market catalogues are gzipped - I thought that was the standard for the default flumine market recorder used here. The implementation seems to require these to be in unzipped form.

2. It's effectively tied to sqlite. Since my need is sql server via sqlalchemy it would be useful if the sql specific bits (possibly statements as well since there are differing sql dialects) were subsumed into a class on their own. That would allow users to implement / contribute their own flavour of sql.

Is this an open project for others to provide contributions or just one you control ? Don't know enough about how github works to answer that - i still use a 30 year old legacy GUI VCS lol.

---

## 2023-10-06 10:42:45 - general channel

**Trex44**

```import csv

import logging

from flumine.controls.loggingcontrols import LoggingControl

from flumine.order.ordertype import OrderTypes

import datetime



logger = logging.getLogger(__name__)

today_date = datetime.datetime.now().strftime("%d-%m-%Y--%H:%M")



FIELDNAMES = [

    "bet_id",

    "strategy_name",

    "market_id",

    "selection_id",

    "trade_id",

    "date_time_placed",

    "price",

    "price_matched",

    "size",

    "size_matched",

    "profit",

    "side",

    "elapsed_seconds_executable",

    "order_status",

    "market_note",

    "trade_notes",

    "order_notes",

]





class StandardLoggingControl(LoggingControl):

    NAME = "Standard_Logging_Control"



    def __init__(self, *args, **kwargs):

        super(StandardLoggingControl, self).__init__(*args, **kwargs)

        self._setup()



    def _setup(self):

        with open(f"orders_{today_date}.txt", "w") as m:

            csv_writer = csv.DictWriter(m, delimiter=",", fieldnames=FIELDNAMES)

            csv_writer.writeheader()



    def _process_cleared_orders_meta(self, event):

        orders = event.event

        with open(f"orders_{today_date}.txt", "a") as m:

            for order in orders:

                if order.order_type.ORDER_TYPE == OrderTypes.LIMIT:

                    size = order.order_type.size

                else:

                    size = order.order_type.liability

                if order.order_type.ORDER_TYPE == OrderTypes.MARKET_ON_CLOSE:

                    price = None

                else:

                    price = order.order_type.price

                try:

                    order_data = {

                        "bet_id": order.bet_id,

                        "strategy_name": order.trade.strategy,

                        "market_id": order.market_id,

                        "selection_id": order.selection_id,

                        "trade_id": order.trade.id,

                        "date_time_placed": order.responses.date_time_placed,

                        "price": price,

                        "price_matched": order.average_price_matched,

                        "size": size,

                        "size_matched": order.size_matched,

                        "profit": order.profit,

                        "side": order.side,

                        "elapsed_seconds_executable": order.elapsed_seconds_executable,

                        "order_status": order.status.value,

                        "market_note": order.trade.market_notes,

                        "trade_notes": order.trade.notes_str,

                        "order_notes": order.notes_str,

                    }

                    csv_writer = csv.DictWriter(m, delimiter=",", fieldnames=FIELDNAMES)

                    csv_writer.writerow(order_data)

                except Exception as e:

                    logger.error(

                        "_process_cleared_orders_meta: %s" % e,

                        extra={"order": order, "error": e},

                    )



        [http://logger.info|logger.info](http://logger.info|logger.info)("Orders updated", extra={"order_count": len(orders)})



    def _process_cleared_markets(self, event):

        cleared_markets = event.event

        for cleared_market in cleared_markets.orders:

            [http://logger.info|logger.info](http://logger.info|logger.info)(

                "Cleared market",

                extra={

                    "market_id": cleared_market.market_id,

                    "bet_count": cleared_market.bet_count,

                    "profit": cleared_market.profit,

                    "commission": cleared_market.commission,

                },

            )```

---

## 2023-10-03 21:25:48 - issues channel

**foxwood**

Log full of 503 errors on the streams from 6ish until it came back at about 08:05 then automatically sorted itself out and carried on as normal. Any fancy middleware ? My setup is just basic flumine and inheriting from BaseStrategy.

---

## 2023-10-03 05:59:36 - general channel

**Troy Edwards**

Hey guys are there any JSON gurus out there?  I am scraping [http://TheGreyHoundRecorder.com.au|TheGreyHoundRecorder.com.au](http://TheGreyHoundRecorder.com.au|TheGreyHoundRecorder.com.au) for its results to store in my database ie [https://www.thegreyhoundrecorder.com.au/results/ballarat/223151/1](https://www.thegreyhoundrecorder.com.au/results/ballarat/223151/1).  I was scraping this successfully for about a year now but the website has changed it webcoding.   Now using [http://VB.NET|VB.NET](http://VB.NET|VB.NET) and the DOM (ie  functions like HtmlElement and HtmlElementCollections) I can get scrape the data but it takes me 10 individual request to get the 10 races from Ballarat AUS whereas all of the data for the 10 races is also shown in the webpage source as a JSON response.  There is also additional data in this JSON response that I might like to investigate - such as general commentary like this "MAN OF MAGIC (4) was narrowly defeated in a tougher maiden race last start and looks primed to break his maiden status".





If you view the source you can find the following JSON data such as  .....   "3.25","8.42","Q/11",29.3,[1917],{"code":1840,"__typename":1841},{"id":1919,"name":1920,"colour":1876,"sex":1877,"sire":1921,"dam":1922,"__typename":1880},"3846228","Man Of Magic","My Redeemer","Darley Park" which aligns with Starting Price, Split, Position in Run, Sire and Dam etc





It looks as if the website source might contain the original JSON request as well as the JSON response OR maybe I am just confused :slightly_smiling_face:  What I would like to do is setup some classes and then decode this webbrowser JSON string into the class in one go.





Otherwise are there any good JSON tools from the MS store OR even online tools that could help determine the start and end of the JSON strings.

---

## 2023-09-20 21:05:43 - general channel

**Mona**

sorry, I am a bit new to this, do you mean you still think the problem is the processing of the data? I will change it to use marketrecorder eventually as you suggested, but still can't understand, is it because the DELAY_APP_KEY we receive much less market books hence the time difference eventually build up is not that significant?

---

## 2023-09-16 08:39:54 - random channel

**Mo**

There's the [https://betcode-org.github.io/faq/|FAQ](https://betcode-org.github.io/faq/|FAQ) but personally I think some kind of getting started in your "career" document is missing from the betcode resources. Not just how do you get started running a strategy in flumine but how do you get started setting up all of the processes you will need. Feel free to get started on this as you continue to make mistakes :wink:

---

## 2023-09-14 18:14:49 - issues channel

**Riccardo Fresi**

for sure is something related to my connection or my firewall, i upload everything on ec3 aws (user, psw, app key, cert)

seems everything working properly



i don't know ho modify my local setup

---

## 2023-09-14 10:39:02 - issues channel

**liam**

Can you share the logs from this:



```# setup logging

logging.basicConfig(level=logging.DEBUG)  # change to DEBUG to see log all updates



# create trading instance (app key must be activated for streaming)

trading = betfairlightweight.APIClient("/")



# login

trading.login_interactive()



# create stream

stream = trading.streaming.create_stream()



stream._connect()

stream.authenticate()```



---

## 2023-09-13 14:46:07 - general channel

**rob smith**

This is a basic question but I'm a self-taught beginner and can't work it out. I moved my scripts to a vps and they worked as normal for the first few days before returning a "ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host" error at login. Betfair's support have asked me for the json request and the response. This is where I'm stuck. I'm using trading.login_interactive() to login. How do I get the json request/response? Thanks

---

## 2023-09-12 16:55:28 - general channel

**Kishore Kumar**

Hi I am new to Betfair APIs and flumine. I am trying to get list of events for today and using below. From response I am not getting total available liquidity for that event. Is there any parameter I need to pass to get that , or I need to get list_market_catalogue and sum all?

`trading.betting.list_events({"eventTypeIds":[2]})`

---

## 2023-09-08 09:30:11 - issues channel

**Riccardo Fresi**

copy from example, but the while at the end

```# setup logging

logging.basicConfig(level=[http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))  # change to DEBUG to see log all updates



# create trading instance (app key must be activated for streaming)

trading = betfairlightweight.APIClient(BETFAIR_USER, 

                                       BETFAIR_PASSWORD, 

                                       app_key=BETFAIR_APPKEY, 

                                       certs=CERT_PATH, 

                                       locale='italy')



# login

trading.login()



# create queue

output_queue = queue.Queue()



# create stream listener

listener = betfairlightweight.StreamListener(output_queue=output_queue)



# create stream

stream = trading.streaming.create_stream(listener=listener)



# create filters (GB WIN racing)

market_filter = streaming_market_filter(

    event_type_ids=["7"], country_codes=["GB"], market_types=["WIN"]

)

market_data_filter = streaming_market_data_filter(

    fields=["EX_BEST_OFFERS", "EX_MARKET_DEF"], ladder_levels=3

)



# subscribe

streaming_unique_id = stream.subscribe_to_markets(

    market_filter=market_filter,

    market_data_filter=market_data_filter,

    conflate_ms=1000,  # send update every 1000ms

)



# start stream in a new thread (in production would need err handling)

t = threading.Thread(target=stream.start, daemon=True)

t.start()```

same error



```INFO:betfairlightweight.streaming.listener:[Register: 1]: marketSubscription

INFO:betfairlightweight.streaming.stream:[MarketStream: 1]: "MarketStream" created

Exception in thread Thread-5 (start):

Traceback (most recent call last):

  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1520.0_x64__qbz5n2kfra8p0\Lib\threading.py", line 1038, in _bootstrap_inner

    self.run()

  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1520.0_x64__qbz5n2kfra8p0\Lib\threading.py", line 975, in run

    self._target(*self._args, **self._kwargs)

  File "C:\Users\riccardo.fresi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\betfairlightweight\streaming\betfairstream.py", line 67, in start

    self._read_loop()

  File "C:\Users\riccardo.fresi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\betfairlightweight\streaming\betfairstream.py", line 226, in _read_loop

    received_data_raw = self._receive_all()

                        ^^^^^^^^^^^^^^^^^^^

  File "C:\Users\riccardo.fresi\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\betfairlightweight\streaming\betfairstream.py", line 256, in _receive_all

    raise SocketError(

betfairlightweight.exceptions.SocketError: [Connect: 2]: Connection closed by server```



---

## 2023-09-03 10:19:44 - strategies channel

**Unknown**

I was just looking at my code..

I dont know if this helps Andy (or hinders :grinning:) but these are the building blocks I used:



```# Load your dataset



# Histogram and Density Plot for 'X'



# Correlation Matrix considering only numeric columns



# Take a 100% random sample of the dataframe (Or reduced value to save time etc)



# Selecting features and target



# Handling any NaN values



# Splitting the data



# Training Random Forest model



# Making predictions



# Calculating Random Forest Accuracy



# Test set predictions and accuracy



# Feature Importance



# Confusion Matrix



# Initialize profit/loss tracking for all three strategies



# Lists to store profit/loss over bets



# Simple, SimpleSP and ML strategies



    # Simple Strategy



    # SimpleX Strategy



    # ML Strategy



# Plotting the Profit/Loss graph```

Re the matching rate as Liam mentioned, I know from real bets that I have a matching rate of 52% so i factored that in

Hope that helps? (Conscious Im new to this sort of thing, I hope Im not sending you down the wrong path, so Joe is worth listening to rather than me)

(PS I found the Correlation matrix worth looking at, its starts to get the old grey matter moving :grinning:)

---

## 2023-09-03 10:16:22 - betconnect channel

**Mo**

Obviously I'm only just getting started with the platform but this seems to be a high incidence so I was wondering if this is a known problem

---

## 2023-08-28 11:54:40 - random channel

**Andrew**

Before moving to Flumine I was using C#. Click-Once deployment works, or even use XCOPY or RSync over SSH to your host. .NET doesn’t need installing. Copying package files works fine.

---

## 2023-08-22 19:53:01 - random channel

**PeterLe**

OK Rishab I understand that now. This maybe useful to prevent adding many features that does little to improve the results. The first thing I noticed when starting off down this road was how much longer it takes when you are adding more and more.

I need to read more about them tools as they are new to me.



Just a general question to you or anyone. have you found ML useful in in-play markets? I can see how this would work in pre off markets but lesser so inplay? Thakns

---

## 2023-08-22 15:01:49 - random channel

**PeterLe**

In a similar post to the above, I was recently inspired by Joe at the meet up who talked a little about ML.

Im only just getting to grips with Python but thought Id have a stroll down the ML path to see what I could find. if you dont look you dont find :grinning:

These are the steps Ive taken so far but would welcome any thoughts as to my approach and whether Im going off course...(remember this is all new to me)

Steps :

Capture recorded data with Flumine.

Then use the PriceRecorder to extract certain features to a CSV (for about a month of racing UK /IRE)

Using this ;-



`import pandas as pd`

`import numpy as np`

`from sklearn.model_selection import train_test_split`

`from sklearn.ensemble import RandomForestClassifier`

`from sklearn.metrics import accuracy_score`



Then Loaded the data into a df...

Clean the data to remove NaN

Train a random forest classifier making predictions.

(I also wanted to plot  the partial dependence but having problems with the code for now...)



Then setup some features Im interested in ...(winner as a target)



`features = ['last_price_traded', 'back', 'lay', 'back_book', 'lay_book', 'ltp_book', 'Spread', 'cross_matching']`

`X = df[features].copy()`

`X['cross_matching'] = X['cross_matching'].astype(int)`

`X = X.fillna(X.median())`

`y = df['winner']`

`X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)`



`back_book_values = np.arange(1.19, 1.21, 0.01) # Just used a ouple here as a test..`



1.Then setup a simple system...

2.Then setup a system using an ML strategy...



...and determine the 'Feature importance' like so:

`feature_importance = random_forest_model.feature_importances_`

`feature_importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importance})`

`feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)`

`print(feature_importance_df)`



After running for a while I got the output like so:



# Random Forest Accuracy: 0.9120607771513096

# Total Profit/Loss using Simple strategy: £-193834.88816246387

# Total Profit/Loss using ML strategy for X 1.19: £17935.374273080262

# Random Forest Accuracy: 0.9120607771513096

# Total Profit/Loss using Simple strategy: £-193834.88816246387

# Total Profit/Loss using ML strategy for X 1.2: £17327.057237254136

# Random Forest Accuracy: 0.9120607771513096

# Total Profit/Loss using Simple strategy: £-193834.88816246387

# Total Profit/Loss using ML strategy for X 1.21: £16570.917359458937

# Best back_book value: 1.19, Profit: £17935.374273080262

#    Feature  Importance

# 3  back_book    0.209721

# 4   lay_book    0.203197

# 5   ltp_book    0.197272

# 2   lay    0.126964

# 0   last_price_traded    0.111824

# 1     back    0.082254

# 6     Spread    0.065538

# 7     cross_matching    0.003230



I can see that the ML strategy beats the simple strategy...and the back_book is the feature with the most importance...



So my question is: How do you uncover what makes the ML model significantly better?

Is it by looking at (and trying to understand the individual decision trees (a subset off)

Other things that seem relevant are a Partial Dependence Plot or form of Correlation Analysis?

What would the pro's suggest as a next step from the feature importance? Thanks in advance

---

## 2023-08-20 14:03:53 - general channel

**Y B**

Hi everyone, just getting started with flumine. Wondering how can I feed the market data from bz2 files downloaded from betfair into it?

```strategy = ExampleStrategy(

    market_filter={"markets": ["/tmp/marketdata/1.170212754"]}

)```

What exactly does the `markets` override accept?



is flumine capable of reading raw data as is or do I need to pre-process it by using e.g. [https://github.com/mberk/betfairutil](https://github.com/mberk/betfairutil)?

---

## 2023-08-17 16:29:19 - random channel

**foxwood**

Had to install rust from [https://rustup.rs/](https://rustup.rs/) which was new to me. Numbers matched exactly - several thousand calls - shin output used in other calcs - identical down to 14 decimal places ! It was using `_optimise_rust` when I stepped it but no idea of speed difference since just used the new one as was for an existing strategy that uses the current release - not time critical for me.

---

## 2023-08-14 12:52:15 - strategies channel

**PeterLe**

Question Please: As a relative beginner to Python, Im learning pandas (dataframes etc) and how to model data. I've used the price recorder to create some data in the form a of a CSV file..from my recorded markets..

Then I'm using sklearn, LinerRegression, seaborn etc...

When I compare the relationship between Profit and a particular variable, when that variable is below x, I get :

Test 1

Coefficient: [-0.00026511]

Intercept: 0.8063449241964358

(Sloping downwards left to right) - Not good,but expected



Whereas when I run it when the variable is above x I get :

Test 2

Coefficient: [0.06673513]

Intercept: 0.10630060921962795

(Sloping left to right upwards) - Good and proven in real world bets



(It should be noted that this is a very small data set, Ill be running on bigger dataset when i have found my feet..)

Now I know that from real world bets placed this variable above x definitely increases profits, but in test 2, the coefficient is very small?



So questions please:

Is linear regression a useful tool? Do the pro's on here use it in a similar way?

Given that you only need a slight edge, should I be confident in the signal with such a low coefficient?

Other than ML (Which is way above my head for now :grinning:) and linear regression, what other python tools do you use to model your data?

Thanks in advance

---

## 2023-08-14 12:11:07 - general channel

**mzaja**

Hi, has anybody had similar experience to this? I have been placing FILL_OR_KILL orders through Flumine and noticed that the order stream update for setting the order status to "Execution complete" is sometimes severely delayed. A FILL_OR_KILL order is either matched instantaneously or rejected, so it should go straight from "Executable" to "Execution complete". Normally, it looks like this, and one can see that the delta between the last two updates is 52 ms:

```Time                       Selection ID  Bet ID        Order status        Side      Matched    Remaining  Trade status

-----------------------  --------------  ------------  ------------------  ------  ---------  -----------  --------------

2023-08-13 10:35:25,142        55258054  None          Pending             BACK         0            2     Live

2023-08-13 10:35:25,340        55258054  316818562580  Executable          BACK         2            0     Pending

2023-08-13 10:35:25,392        55258054  316818562580  Execution complete  BACK         2            0     Live```

However, for a sizeable proportion of the time, the "Execution complete" status update is received several minutes later, when the market gets resulted. Note that the bet is already fully matched when it reaches the status of "Executable", but it takes almost 9 minutes for the "Exection complete" update to arrive.

```Time                       Selection ID  Bet ID        Order status        Side      Matched    Remaining  Trade status

-----------------------  --------------  ------------  ------------------  ------  ---------  -----------  --------------

2023-08-13 10:11:58,988        58973557  None          Pending             BACK            0            2  Live

2023-08-13 10:11:59,296        58973557  316815184967  Executable          BACK            2            0  Pending

2023-08-13 10:20:39,839        58973557  316815184967  Execution complete  BACK            2            0  Live```

Any thougts on this? I am trying to figure out whether this is

1. A problem on Betfair's side.

2. A problem with Flumine.

3. A problem with my setup.

---

## 2023-08-13 16:12:43 - random channel

**D C**

I've been chatting here with some people and I'm considering starting to use flumine in order to get around some issues I am having with the HTTPS client component that I currently use in my own setup. I've a question about the use of thread pools really. At times I will need to place bets across many distinct strategies in a way that they are all fired within as little as 1 millisecond of eachother. This causes the component I use a few problems the result being that my requests are queued in an opaque manner and I suffer placement latency.



When using a thread pool I'm trying to find out what the lay of the land is. Alternatively, if I write my own thread pool trying to find a best practice implementation based around the betfair API:



1. Does each thread in the pool maintain a HTTPS connection to the server (in the keep-alive sense) at all times so that when called up it is ready to immediately transmit the request, or does it sit idle and go through the whole SSL handshake process every time?

2. Are threads created at the start of the program and persist until it terminates? I am guessing this is the case due to overheads in firing up new threads in an on-demand manner?

3. Within each thread, is a "global" session token shared across the entire application, or does each thread make a separate login and manage its own connection? If the latter, is that frowned upon by betfair (do they have a limit on the number of active sessions each user account can make)?

I am a bit of a dunce with how HTTPS works under the surface and I am trying to get some support for the components I am using but the CS reps are all but accusing me of trying to create something that causes a DOS on a target so I'm getting nowhere (other than getting pissed off with them). When mentioning that I might want to fire off several requests to a server within a single figure millisecond time interval I am being told that my use case is "very unusual" and they are proving to be very unhelpful.

---

## 2023-08-08 14:46:15 - general channel

**joe taylor**

I think it’ll be helpful for beginners if someone can share an implementation/Anaylsis notebook of a basic strategy using flumine. I read the documentation but not much clear from there.  

---

## 2023-08-08 14:03:29 - strategies channel

**Joe**

[@UUE6E1LA1](@UUE6E1LA1) I don't have any papers I'd recommend.

If you are doing NN classification with back propagation then you are just using the chain rule of derivatives to calculate the changes to the network weights to minimise total network error, the derivatives being those of the activation functions in your nodes and the learning rate basically how far down the slope you want to step. Typically you would choose the activation functions only.

If you are doing decision trees (boosted and/or ensemble / RF) then you splitting based on the most effective split point in the most effective dimension, usually assuming a linear gradient wrt that dimension.

If you are doing metaheuristic search then these are usually based on a pseudo biological explanation, like genetic crossing and mutation in populations, or the swarming nature of insects around some energy source, but all really boil down to guided brute force, these algos don't bear any resemblance to anything mathematical in the underlying system being optimised.



I think the problem you are having getting started is that every single non-paper based method of optimising anything has fallen under the umbrella term of ML, mainly because it enables the fading coding/developer tech industry to pivot to a post-coding 'data science' industry, this makes is really difficult to discuss in general terms.



If I was getting started today I would start with simple NN classifier, read up on it and code a network solver.

If you wanted to look at something more unsupervised then someone has decided to name a fairly general method 'Q-Learning', look this up.

---

## 2023-08-08 10:11:38 - strategies channel

**foxwood**

I've used Google's tensorflow with python -  flexible for building / managing features - works well and now the docs appear sorted should be easier getting started. Any learning you do will transfer easily to other packages. If you are familiar with MS Visual Studio then their [http://ML.NET|ML.NET](http://ML.NET|ML.NET) add on is worth looking at - give it a csv then select fields to use and decide if feature or category is all you do - it then tries lots of different models to offer the best one. Seriously lacks ability to fine tune easily as in TF or SK but quick way to assess possibilities of datasets / models.

---

## 2023-08-07 13:05:50 - strategies channel

**Unknown**

So I have a rough pipeline setup to allow model -&gt; flumine simulation, it works and I have results which point to some potential.



Stats: £30.0 profit per market, 14.0% roi, £59.4 matched per selection



A huge increase in matched amount which is not viable but the increase in ROI is most welcome, going to play around with some features and try and reduce the amount matched (probably a ML term for this when it comes to the model)

---

## 2023-08-04 17:54:45 - random channel

**Adam**

You could also try using Miniconda or some Anaconda variant ([https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html))



Some Python libraries are still problematic with Apple silicone and letting conda manage packages/installs for you can save a lot of time/headaches.

---

## 2023-08-04 13:11:21 - random channel

**D C**

Can anyone recommend a path-of-least-resitance method of installing python on macbook? I recently bought one purely for music production but I would quite like to do a little scripting with it too just to enable me to get a bit more use out of it. I know there will be a multitude of search engine results but I've more faith in a recommendation from here tbh.

---

## 2023-08-04 09:39:09 - issues channel

**Mo**

It's not a problem with the certificate you generated using XCA which works fine otherwise you would not be able to log in



Either you have some weird software installed or there is something about your network setup that means someone is man in the middle attacking you. Perhaps it's your ISP

---

## 2023-08-03 03:06:54 - general channel

**Unknown**

Hi [@U4H19D1D2](@U4H19D1D2), Thanks for the advice! I made the git clone. But the problem persisted. After a while, I realized that the betfairlightweight library had been installed and imported from there.

This behavior didn't let me debug the things happening inside the library, just limited to the file where I was running the example.

To solve this, I put the libraries as in the image, added the _`__init__`_ necessary files, changed the route for importing, and voila! It worked! and now I can debug throughout both libraries! :raised_hands::tada:

---

## 2023-07-27 08:20:36 - general channel

**liam**

EC2.nano, setup and forget, much easier than managing it yourself

---

## 2023-07-21 10:03:54 - general channel

**anh**

hello everyone, I'm new to Python and coding in general and am in the process of moving from BA/Excel to BFLW (whilst learning on the job).  I'm very much a newbie so if betcode isn't the place for this question please let me know... I have implemented a few strategies so far but my next one requires me to check open orders (matched and unmatched) on different horse racing win markets. To do this I am trying to use list_current_orders - which I think is the right one - as follows: `open_bets = trading.betting.list_current_orders(market_ids=[market_id])`. This seems to return a list of objects but is where I'm stuck. How do I get the bet details from these objects?

---

## 2023-07-11 18:08:45 - general channel

**George**

```22 def run():

23   start_time_seconds = 43000

 24   stop_time_seconds = 1800

 25   setup_logger(logging.DEBUG)

 26   trading = login_with_bflw()

 27   client = clients.BetfairClient(trading)

 28   framework = Flumine(client=client)

 29   strategy = get_strategy(start_time_seconds, stop_time_seconds)

 30   pred_worker = get_prediction_worker(framework, start_time_seconds)

 31   logging_control = MarketOrderControl()

 32   framework.add_strategy(strategy)

 33   framework.add_worker(pred_worker)

 34   framework.add_logging_control(logging_control)

 35   with patch.object(config, 'raise_errors', True):

 36     framework.run()

 37   return framework```

---

## 2023-07-07 06:08:02 - general channel

**Mo**

I believe the error is related to how frequently you are connecting to the database so if you have reduced that frequency then that is a workaround



Another workaround I was going to suggest would be to use the IP address of the database server, assuming it is fixed, to avoid having to resolve the name



In my case, although I recall I had to mess around with the default name resolver setup in Ubuntu, that doesn't seem to be reflected in my current configuration so I assume it was fixed at some point. I am running 22.04. Upgrading should be a permanent solution

---

## 2023-07-06 18:17:00 - strategies channel

**Charaka A**

I'm new to using flumine and was wondering if anyone has an idea how to go about maintaining the state of the ladder as part of the strategy. I'd like to later visualise the ladder but initially would like to maintain my own ladder for each runner which would be updated based on the mc packets received

---

## 2023-07-04 09:41:33 - issues channel

**Mo**

Is this a fresh install of flumine? Looks like some kind of version conflict

---

## 2023-06-19 14:05:50 - strategies channel

**James**

Hey, everyone I’m new to Flumine,

I’ve been using an JS based closed source framework for a while doing mostly in play trading.

The framework I have been using  handles a few things flumine doesn’t seem to (Flumine handles a LOT that the js framework doesn’t).

I’m wondering if theres an easy way to get your current matched win/lose positions on a runner?

Also does any one have any nice util functions for hedging/ledging that they’d be willing to share?

---

## 2023-06-16 15:19:10 - random channel

**liam**

this is mine



```FROM python:3.11.3



RUN apt-get -y update



# build flumine

ADD . /flumine-prod

WORKDIR /flumine-prod



# install py libraries

RUN pip install -r requirements.txt



CMD python main.py $ENV $INSTANCE```

---

## 2023-06-16 06:42:07 - issues channel

**Aaron Smith**

hey guys! Yesterday i had my first bot going rogue. Looking at my terribly lazy workflow and messy code at times, its actually a miracle that this has been the first time in all these years. I know very well how to prevent this in the future, as i know what caused it (lazy workflow a la "why paper trade - cool kids go live" :smile: ). Knowing myself however, i could still be dumb enough to let it happen again, even after this incident.

Anyways, as i watched my rogue bot throw out 100% of my bankroll in a fraction of a second, i was wondering: how to best deal with this? I didnt want to just kill it, as then i d be left with thousands of bets (idk how many it was, it hit transaction limit, so whatever that limit is) all over betfair that are completely unattended and i d have to manually cancel them all via the betfair_webUI. As it was supposed to only be a test run, i had it set to only run for 1 hour, so i decided to just let it do its thing, as this way, while it may have broken any exposure limits imaginable, it still babysat my bets in a somewhat "smart" way.



However, after 1 hour, the bot did in fact stop, but not as gracefully as hoped. It just left all the bets up so i still had to manually go through the markets and cancel them.



This leaves me with 2 questions:

1. Is there a way to gracefully kill a rogue bot?

2. What went wrong when my bot was supposed to cancel all bets before stopping as planned?

regarding 2, here is the relevant code that terminated the bot and was supposed to cancel all bets left:

```def terminate(context: dict, framework) -&gt; None:

    for market in framework.markets:

        for order in market.blotter:

            if order.status == OrderStatus.EXECUTABLE:

                market.cancel_order(order)

    framework.handler_queue.put(TerminationEvent)





terminator = flumine.worker.BackgroundWorker(flumine=framework, function=helpers.terminate, interval=100, start_delay=60 * self.run_time_in_mins)  # termiante after run_time_in_mins



framework.add_worker(terminator)```



Also, i know you guys would ve loved for me to throw some cash at you, but luckily i didnt get punished as i should ve been. The bot actually made 10 pounds (minus what the other bots could ve made in that hour maybe, if they had any bankroll left to play with), enough to get me a well deserved pint after a productive day at "work".  But no worries, i m sure i ll unleash one of these bad boys again some time.

---

## 2023-06-10 16:53:23 - random channel

**Jonjonjon**

How do people manage their data/backtesting order?



My data is in zip files. 1 zip per day, containing one archive per market.



At present I use the multiprocessing module with a custom process pool which handles one market/archive per Flumine backtest run. I allow each worker process to run 8 backtests before it respawns.



I'm using a 3950x CPU (16c/32t) with Evo 970 plus nvme.



To prevent concurrent file access (which I am assuming will be slower than serial access), I use a multiprocessing.Lock to only allow one archive to be read at a time.



With this setup, my CPU usage tends to vary from 80-90%. So there should be scope to use it more. I am assuming that it is less than 100% due to the multiprocess lock.



However, after a few minutes, my NVME temp mazes out at 70c, which is at the higher end of its operating range. So I believe it's maxing out.



What do other people here do?

---

## 2023-06-05 23:16:51 - issues channel

**foxwood**

In `process_closed_market()` I walk the blotter and log all the bets marked as `EXECUTION_COMPLETE` For the first time today I found there were lots of unmatched lapsed bets that were not logged. From the live strategy log it seems that the market was closed and removed before `"Order status update: Execution complete"` was received for these bets ! Is this normal everyday stuff that I've not noticed before or was it just BF having a bad day ?



Edit: All the bets were `MARKET_ON_CLOSE` and less than £10 liability so guessing that's maybe what happens if not enough to make the SP draw. Wonder what the `OrderStatus` would be in that case ?

---

## 2023-05-27 23:39:10 - betconnect channel

**Alejandro Pablos Sánchez**

I'm a beginner in this world so I'm trying to setup a software infrastructure that allows me to automatically place bets on the exchange. Did anyone encounter this problem before? I'd really appreciate if someone could help me. Thanks in advance !

---

## 2023-05-25 11:34:17 - random channel

**Herugrim**

Yeah and because you pay commission per market per account you would generally end up paying more commission, especially if your accounts ran competing strategies. It’s painful to setup and even more painful to manage. 



IMO the only reason to need one is if you were deploying bots that have to potential to go rogue and drain your balance, but that comes back to improving your coding and best practices. It’s easier just to use strategy refs

---

## 2023-05-19 21:10:58 - general channel

**Jonjonjon**

I finally installed it.

My personal suite of tests takes 55 seconds on Python 3.8. 49 seconds on Python 3.11. So about 11% faster

---

## 2023-05-19 14:36:02 - general channel

**Unknown**

Good morning, everyone. Yesterday, while using _*betfairlightweight*_, I noticed that all soccer matches, once they appear as _*InPlay*_ on the Betfair website, take approximately 1 minute to show up for the first time in the API when you select to display `in_play_only=True` events. Additionally, it takes 2 minutes or more for them to stabilize and continuously appear without interruption.



```market_filter = betfairlightweight.filters.market_filter(

        event_type_ids=['1'],in_play_only=True

    )

    return trading.betting.list_events(filter=market_filter)```

Is this a normal occurrence when using the API with calls like the one above or similar to the test video I made using [https://docs.developer.betfair.com/visualisers/api-ng-sports-operations/](https://docs.developer.betfair.com/visualisers/api-ng-sports-operations/)?



Im asking because, for example, in _*Geeks Toy Software*_, once it shows as _*InPlay*_, it stays that way, and the same goes for the Betfair website. However, when using the API, this oscillating occurs.

---

## 2023-05-04 07:44:48 - issues channel

**Nick**

Hi All, I'm hoping you can help me. I'm new to flumine and I'm having trouble achieving what I'm trying to achieve for a backtest simulation.



I'm trying to run a simulation on soccer MATCH_ODDS market with the following conditions:



1. Record the odds of the favourite at 60secs before kick off

2. Place a BACK bet on the pre match favourite whilst match is in play and the odds of the favourite have increased by 20%

I'm not sure where it is going wrong or whether I am using the market.context correctly.



Code as per this:

def check_market_book(self, market, market_book):

        if (market_book.status == "OPEN") and market.seconds_to_start &lt; 60:

            # store favourite's starting price

            runners = sorted(

                market_book.runners, key=lambda r: r.ex.available_to_back[0]['price']

            )

            if runners:

                fav = runners[0]

                market.context["fav_starting_price"] = fav.ex.available_to_back[0]['price']

                market.context["market_start_time"] = market_book.market_definition.market_time

                return True



    def process_market_book(self, market, market_book):



        if "fav_starting_price" in market.context:

            # get favourite

            runners = sorted(

                market_book.runners, key=lambda r: r.ex.available_to_back[0]['price']

            )

            if runners:



                fav = runners[0]

                # calculate favourite's odds



                if market.seconds_to_start &lt; 60 and market.seconds_to_start &gt; 50:

                    fav_starting_price = fav.ex.available_to_back[0]['price']

                    fav_starting_price = market.context["fav_starting_price"]







                elif market_book.inplay == True:

                    if fav.ex.available_to_back[0]['price'] &gt; market.context["fav_starting_price"] * 1.2:

                        # place BACK bet on the favourite

                        runner_context = self.get_runner_context(

                            market.market_id, fav.selection_id, fav.handicap

                        )

                        if runner_context.live_trade_count == 0:

                            trade = Trade(

                                market.market_id, fav.selection_id, fav.handicap, self

                            )

                            order = trade.create_order(

                                side="BACK",

                                order_type=LimitOrder(

                                    get_price(fav.ex.available_to_back, 0),

                                    size=5,

                                ),

                            )

                            market.place_order(order)

---

## 2023-05-02 15:32:44 - general channel

**Adam Momen**

[@U4H19D1D2](@U4H19D1D2) Have you considered writing rust version of _flumine_ for speed gains_?_



I’m running backtesting across thousands of markets everyday, the processing time slow down as the data increased, following all the performance guidelines and tips in the [https://github.com/betcode-org/flumine/blob/master/docs/performance.md|doc](https://github.com/betcode-org/flumine/blob/master/docs/performance.md|doc) and installing flumine with c &amp; rust liberaries (`flumine[speed]` ) helped but it was still relatively slow.



I wanted faster processing speed, so I’ve run a simple benchmark [https://www.notion.so/Flumine-Backtesting-Benchmark-c3b20cd40fd4487388fd2d73ed23f72f?pvs=4|experiment](https://www.notion.so/Flumine-Backtesting-Benchmark-c3b20cd40fd4487388fd2d73ed23f72f?pvs=4|experiment) to compare file reading speeds from disk in Python3.11 and Rust, why I chose rust?  It’s safe and fast, and the learning curve not that steep.



*Rust was 35x faster.*



&gt; Note: I ran the benchmark on my M1 Air, I admit that it’s the not the best way of recording the result, but it was good rough estimation.

---

## 2023-04-16 10:42:19 - issues channel

**alan fisher**

Hi there. I'm a newbie trying to use Betfairlightweight python examples for the first time. I've  succeeded  in getting passed the trading.login which generates a session token but then anything I then try with the Trading object results in this error



Error: {'code': -32099, 'message': 'ANGX-0007', 'data': {'APINGException': {'requestUUID': 'ie2-ang08a-prd-03211101-003751a790', 'errorCode': 'INVALID_APP_KEY', 'errorDetails': ''}, 'exceptionname': 'APINGException'}}

Full Response: {'jsonrpc': '2.0', 'error': {'code': -32099, 'message': 'ANGX-0007', 'data': {'APINGException': {'requestUUID': 'ie2-ang08a-prd-03211101-003751a790', 'errorCode': 'INVALID_APP_KEY', 'errorDetails': ''}, 'exceptionname': 'APINGException'}}, 'id': 1}



Can anyone give me any pointers?

---

## 2023-03-30 19:31:56 - general channel

**Jesus Perdomo**

Hey guys, random question (relatively new to python).



Went through the betfairlightweight source to try and see if there was any implementation to use proxies with the API connection - I don't think this is the case.

Reason I am asking is because my development VPS is located in the US but I'm in the UK. All API calls unfortunately route through US IP address which betfair doesn't allow.



I was hoping I could implement a proxy to all the requests calls, but seems like I'd have to edit the original source code for this (and therefore miss out on future updates to the package etc...)



Has anyone come accross this issue? - Probably controversial as it could be used to circumvent Betfair rules of access I suppose?

---

## 2023-03-28 13:01:25 - general channel

**RDr**

Hi Liam,

I've started to search for older msg on the channel and downloaded a copy of the older slack but it will take me some time to go through all the resources available and examples to find what's relevant for me now. So I need you guidance again please.



1. Are the examples that could help with my question in the folder [https://github.com/betcode-org/flumine/tree/master/examples](https://github.com/betcode-org/flumine/tree/master/examples) ?

2. Should the files in sub-folder [https://github.com/betcode-org/flumine/tree/master/examples/strategies](https://github.com/betcode-org/flumine/tree/master/examples/strategies) be manually copied (I saw the following for setup [https://github.com/betcode-org/flumine/blob/master/setup.py](https://github.com/betcode-org/flumine/blob/master/setup.py))?

---

## 2023-03-28 00:25:19 - general channel

**RDr**

Hi, I am only getting started and found some codes to get stream racing data using befairlightweight.

It sounds like Flumine could facilitate the process and run different market_ids streams in parallel/concurrently and sequentially.

Could someone assist and let me know what the Flumine codes would be to run and get/save different streaming data in parallel (different venues) and also in sequence (same venue for different races once the previous race market closes) ?

Thanks!



#===================================================

# Sample section of codes for betfairlightweight version (only 1 stream worked for me, not sure how to adapt the codes or use existing Flumine functions to record multiple markets in  parallel or sequentially)



# create queue

output_queue = queue.Queue()



# create stream listener

listener = betfairlightweight.StreamListener(output_queue=output_queue)



# create stream

stream = trading.streaming.create_stream(listener=listener)



# create filters (AU WIN racing)

# market_filter = streaming_market_filter(

#    event_type_ids=["7"], country_codes=["AU"], market_types=["WIN"],

# )

my_market_ids = [..., ...., ...]

market_filter = filters.market_filter(market_ids=my_market_ids)



market_data_filter = streaming_market_data_filter(

    fields=["EX_MARKET_DEF", "EX_LTP", "EX_BEST_OFFERS", "EX_TRADED", "EX_TRADED_VOL", "SP_TRADED", "SP_PROJECTED"], ladder_levels=3

)



# subscribe

streaming_unique_id = stream.subscribe_to_markets(

    market_filter=market_filter,

    market_data_filter=market_data_filter,

    conflate_ms=1000,  # send update every 1000ms

)



# start stream in a new thread (in production would need err handling)

t = threading.Thread(target=stream.start, daemon=True)

t.start()



# Open a file for the market stream data

filename = f"{market_id}.txt"

filepath = os.path.join("data", filename)

with open(filepath, "w") as f:



    # check for updates in output queue

    while True:

        market_books = output_queue.get()

        print(market_books)



        for market_book in market_books:

            # print(

            #     market_book,

            #     market_book.streaming_unique_id,  # unique id of stream (returned from subscribe request)

            #     market_book.streaming_update,  # json update received

            #     market_book.market_definition,  # streaming definition, similar to catalogue request

            #     market_book.publish_time,  # betfair publish time of update

            # )



            # write data to file

            f.write(str(market_book.streaming_unique_id) + '\n')

            f.write(str(market_book.streaming_update) + '\n')

            f.write(str(market_book.market_definition) + '\n')

            f.write(str(market_book.publish_time) + '\n')

---

## 2023-03-27 17:50:27 - general channel

**Peter**

When you setup a strategy to subscribe to a market, you can set the streaming_timeout (seconds) parameter. That will force the a snapshot to be taken and evaluated at that frequency if no market updates have been received. [https://betcode-org.github.io/flumine/strategies/#parameters](https://betcode-org.github.io/flumine/strategies/#parameters)

---

## 2023-03-17 14:09:53 - issues channel

**liam**

why do you want to handle it? setup and forgot [https://github.com/betcode-org/betfair/blob/master/examples/examplestreamingerrhandling.py|example](https://github.com/betcode-org/betfair/blob/master/examples/examplestreamingerrhandling.py|example)

---

## 2023-03-13 20:10:03 - general channel

**birchy**

[@U027P3N2WMQ](@U027P3N2WMQ) I'm using the S3MarketRecorder example which uses boto3 to push to S3. The only extra setup from your end is to create a `.aws` folder in your home directory for your credentials. 

[https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html|https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html|https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

---

## 2023-03-13 11:52:02 - general channel

**Lucas Torres**

Hi guys, I'm new to the developer application of the bf, but I'm likeing to discover this. I just want the data from US horse racing and I just want the BSP of the runners. Could someone help me?

---

## 2023-03-13 09:33:10 - general channel

**Andy Bason**

It'll be my beginner knowledge level. Thanks for the help

---

## 2023-03-12 13:41:24 - general channel

**birchy**

Regarding Lightsail, I use these instances as they're far easier to setup than EC2. You can add extra storage (see screenshot), however I just run the marketrecorder on a low cost instance and push to S3.

---

## 2023-03-12 11:53:34 - issues channel

**Sunken**

Hey, fairly new to working with betfairlightweight/flumine so this might be a dumb question, but I was looking at the difference in total_volume for each race calculated via totalling the price ladders you get from the runnerEX classes, vs just parsing the json files directly, and noticed they were pretty sizeable.



Looking closer, I realised part of the reason was that even if the market update stated that there was an amount traded, and both the runnerEX class and my dictionary parser would pick up on it, afterwards for certain updates the runnerEX class would drop those values. In other cases, it would pick up trades that were not there. Is there a reason for this? Dived into the source code for a few hours but not really any closer to a solution.

---

## 2023-03-10 10:06:35 - general channel

**liam**

Here is a hopefully an easier to understand script and considerably faster, few caveats:



• Half time isn't possible without some assumptions and/or other data

• All odds movements would be a massive list, is that what you actually want?

```import logging

import csv

import smart_open

from unittest.mock import patch as mock_patch

import betfairlightweight



COLUMNS = [

    "market_id",

    "event_date",

    "event_name",

    "country",

    "market_name",

    "selection_id",

    "selection_name",

    "result",

    "actual_sp",

    "pp_min",

    "pp_max",

    "pp_wap",

    "pp_ltp",

    "pp_volume",

    "ip_min",

    "ip_max",

    "ip_wap",

    "ip_ltp",

    "ip_volume"

]



file_path = "/Users/liampauling/Documents/tmp/marketdata/1.177242007.gz"



# setup logging

logging.basicConfig(level=[http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))



# create trading instance (don't need username/password)

trading = betfairlightweight.APIClient("username", "password", "appKey")



# create listener

listener = betfairlightweight.StreamListener(

    max_latency=None,  # ignore latency errors

    output_queue=None,  # use generator rather than a queue (faster)

    lightweight=True,  # lightweight mode is faster

    update_clk=False,  # do not update clk on updates (not required when backtesting)

    cumulative_runner_tv=True,

    calculate_market_tv=True,

)



with mock_patch("builtins.open", smart_open.open):

    # create generator

    stream = trading.streaming.create_historical_generator_stream(

        file_path=file_path,

        listener=listener,

    )

    market_data = {}  # store all data



    # loop all markets

    for i in stream.get_generator()():

        for market_book in i:

            market_id = market_book["marketId"]

            if market_id not in market_data:

                market_data[market_id] = {

                    "market_definition": market_book["marketDefinition"],

                    "selections": {

                        i["id"]: {

                            "id": i["id"],

                            "name": i.get("name"),

                            "pp_min": None,

                            "pp_max": None,

                            "pp_ltp": None,

                            "pp_volume": None,

                            "ip_min": None,

                            "ip_max": None,

                            "ip_ltp": None,

                            "ip_volume": None,

                        } for i in market_book["marketDefinition"]["runners"]

                    },

                    "inplay": False,

                    "final_market_book": None,

                }

            market = market_data[market_id]



            # update selection values when prePlay

            if market_book["status"] == "OPEN" and not market_book["inplay"]:

                for selection in market_book["runners"]:

                    selection_data = market["selections"][selection["selectionId"]]

                    if selection_data["pp_min"] is None:

                        selection_data["pp_min"] = selection["lastPriceTraded"]

                        selection_data["pp_max"] = selection["lastPriceTraded"]

                        selection_data["pp_ltp"] = selection["lastPriceTraded"]

                        selection_data["pp_volume"] = selection["totalMatched"]

                    else:

                        selection_data["pp_min"] = min(selection_data["pp_min"], selection["lastPriceTraded"])

                        selection_data["pp_max"] = max(selection_data["pp_max"], selection["lastPriceTraded"])

                        selection_data["pp_ltp"] = selection["lastPriceTraded"]

                        selection_data["pp_volume"] = selection["totalMatched"]



            # update selection values when inPlay

            if market_book["status"] == "OPEN" and market_book["inplay"]:

                for selection in market_book["runners"]:

                    selection_data = market["selections"][selection["selectionId"]]

                    if selection_data["ip_min"] is None:

                        selection_data["ip_min"] = selection["lastPriceTraded"]

                        selection_data["ip_max"] = selection["lastPriceTraded"]

                        selection_data["ip_ltp"] = selection["lastPriceTraded"]

                        selection_data["ip_volume"] = selection["totalMatched"]

                    else:

                        selection_data["ip_min"] = min(selection_data["ip_min"], selection["lastPriceTraded"])

                        selection_data["ip_max"] = max(selection_data["ip_max"], selection["lastPriceTraded"])

                        selection_data["ip_ltp"] = selection["lastPriceTraded"]

                        selection_data["ip_volume"] = selection["totalMatched"]

                        selection_data["actual_sp"] = selection["sp"]["actualSP"]



            # final book

            market["final_market_book"] = market_book



# write data to csv

with open("output_bflw_new.csv", "w") as f:

    writer = csv.DictWriter(f, fieldnames=COLUMNS)

    writer.writeheader()

    for market_id, market in market_data.items():

        market_definition = market["market_definition"]

        selection_lookup = {i["selectionId"]: i for i in market["final_market_book"]["runners"]}

        for selection in market["selections"].values():

            writer.writerow(

                {

                    # market level data

                    'market_id': market_id,

                    'event_date': market_definition["marketTime"],

                    'event_name': market_definition.get("eventName"),

                    'country': market_definition["countryCode"],

                    'market_name': market_definition.get("name"),

                    # selection level data

                    'selection_id': selection["id"],

                    'selection_name': selection["name"],

                    'result': selection_lookup[selection["id"]]["status"],

                    'actual_sp': selection["actual_sp"],

                    "pp_min": selection["pp_min"],

                    "pp_max": selection["pp_max"],

                    # "pp_wap",

                    "pp_ltp": selection["pp_ltp"],

                    "pp_volume": selection["pp_volume"],

                    "ip_min": selection["ip_min"],

                    "ip_max": selection["ip_max"],

                    # "ip_wap",

                    "ip_ltp": selection["ip_ltp"],

                    "ip_volume": selection["ip_volume"],

                }

            )```

---

## 2023-03-09 20:12:37 - general channel

**Richard Cornish**

Thank you so much Liam for taking the time. The tutorial is interesting for someone brand new to the module and Python, but I’m sure it could be much more elegant. I found out today how to inspect the betfairlightweight module which has been another enlightening step! 

---

## 2023-03-08 08:56:27 - general channel

**Unknown**

Hi everyone, apologies for a complete beginner question but I am brand new to Python and betfairlightweight. I have cannibalised some code online to extract the following data from the Betfair Historical Data BASIC soccer files. It has the last pre-play odds and the ltp which is more than I ever expected to get! However, what I would really like is to adjust the code so it produces a similar Excel file but with the last pre-play odds (already got), the half-time odds (if the market is not closed at half-time), the highest price traded and the lowest price traded. If at all possible as a cherry on the top, if all of the recorded odd movements could be put into the columns to the right from the market going in-play until it closes that would be great. Apologies for such a basic question, finding my feet with coding!

---

## 2023-03-06 15:29:51 - random channel

**Luke Stevens-Cox**

Hi guys, new to this slack and sports modelling has anyone done any golf modelling and have any resources they'd be willing to share around where they started or anything they found useful? Thanks

---

## 2023-02-20 21:11:58 - random channel

**Newbie99**

I'm completely new to Mac OS and google is very limited on the subject of network drive mapping issues, so hopefully someone here has faced similar.



I have a (linux based) NAS where I store all my market recorded data, I have the drive mapped on a windows PC and can access files easily without any major lag, however when I mount the drive via terminal in Mac OS the performance is really poor, for example the same folder (containing approx 12k recorded market files) takes &gt; 30 seconds to return results from the command line (compared to virtually instantaneous on the windows machine).



The other confusing thing is that via SSH performance is fine from both the windows machine and the mac.



Obviously the solution seems to be, SSH rather than try to map the drive, but does anyone have any ideas why this could be happening (all machines are on the same WIFI network and physically in the same room)?

---

## 2023-02-12 16:49:41 - betfair-news channel

**Chantelle**

Hey guys, new here.  I've been using a bot program to execute all my bets the last year, so no coding required. I run about 8 profitable systems atm since March (39000 bets placed).   Would like to learn bit more on the API side from a purely beginners level.  I have had some exposure to Python language in the past, is Python useful or should I look more into a different language?  Are there any free resources to learn about developing and executing your strategies using the betfair API? Thanks!

---

## 2023-02-09 12:27:03 - random channel

**Unknown**

Apologies, I am rather new to Python. My load_markets functionality uses betfair lightweight, though this module is imported via betfair_data.

---

## 2023-02-08 17:56:57 - strategies channel

**Peter**

Oops [@UQL0QDEKA](@UQL0QDEKA). Just spotted that you have the parameters in the wrong place. They're parameters for the strategy rather than the market_filter, so your code should be:



```strategy = Sub6(

    name="WIN",

    market_filter=betfairlightweight.filters.streaming_market_filter(

        event_type_ids=["7"], # was 7 for horses, 4339 for greyhounds, 15 = todays card greyhounds

        country_codes=["GB","IE"],

        market_types=["WIN"],

    ),

    max_order_exposure=5,

    max_selection_exposure=20,

    max_trade_count=5,

    max_live_trade_count=1

)```

Apologies for not picking this up first time around.

---

## 2023-02-01 18:24:49 - random channel

**birchy**

I've used Linux on all of my work machines for about 20 years and recently gained access to a MacBook air M1 a few months ago. Although similar to Linux (Ubuntu, Mint, Debian, etc), I did/do find the keyboard shortcut mappings take a while to get used to. Overall it's a been positive experience. Once you have the thing setup (Pycharm, etc) the experience is not much different to any other OS. My main advice would be to ensure you research the installation process for any software you need as there's usually a specific Apple Silicon version. The default Intel versions _will_ install OK but I've had "wrong architecture" issues in the past, particularly with python/numpy/pandas while running in Pycharm. That's usually related to the python interpreter used by Pycharm and you have to point it at the full path rather than the/bin/python3.11 it suggests is available.

---

## 2023-01-31 13:52:39 - general channel

**QuickLearner8888**

Hi All.



I am new to this channel, and to Flumine in general.



Are there any tutorials out there, to explain how to use the marketrecorder?



I am interested in getting a market-stream, of a specific market_id. As an example, a live soccer-match, I would like to have only best_back_offered and best_lay_offered, and offered volumes at any given time, for every runners in the over/under market.



Any help or pointers in right direction would be a huge help.



 Thanks

---

## 2023-01-22 15:03:09 - general channel

**Peter**

A bit puzzled as to why this is a question. What's the architecture of your setup that makes this a potential concern?



I also doubt that anybody here will have an answer to this since if the keep_alive method is being used, implicitly or explicitly, to maintain active sessions it's not something we're likely to come up against. So probably one to ask Betfair.

---

## 2023-01-21 14:48:21 - general channel

**Aaron Smith**

as someone who also started using flumine early on in his coding career, i want to add that while its all technically "easy", as a beginner you are likely to get stuck on the most dumb things (at least i did), so with this i d like to relativize the word "easy" as to not make you feel dumb, which may happen anyway :D

---

## 2023-01-21 14:36:09 - general channel

**Aaron Smith**

[https://betcode-org.github.io/flumine/](https://betcode-org.github.io/flumine/) has good info for getting started. In the flumine repo under examples, you ll find the S3Recorder, which can be used to safe streaming data in a s3-bucket. The s3 recorder can be set up just like any strategy (so you can follow the steps from the link)

---

## 2023-01-18 13:55:25 - issues channel

**dont**

How did you get the code ? If you just pip installed flumine and tried to run the code, it won’t work as the examples are not part of the python package:



[https://github.com/betcode-org/flumine/blob/master/setup.py#L22](https://github.com/betcode-org/flumine/blob/master/setup.py#L22)



You can fork/pull and get the code locally after which you’ll be able to run it.

---

## 2023-01-18 10:59:12 - strategies channel

**Newbie99**

There are a few academic papers that have been posted on here in the past and in all honesty this Slack is probably the best place to learn. If you have any specific questions (e.g. terminology and/or how to get started with Flumine etc. ask away and people are generally very helpful).



If you're completely new to this then be wary of some of the youtube content, a lot of it uses questionable logic (to put it politely) and is somewhat misleading with regards to the concept of 'value' and how it can be achieved (for example, videos might say bet early in a football match to maximise the chance of a goal being scored...whilst its true to say the probability of a goal being scored is greater over a longer timeframe in any given match, without data its impossible to know whether the odds correctly reflect the probability of a goal being scored, just because they are longer in match a than in match b, it does not guarantee value is on offer).

---

## 2023-01-18 10:24:53 - issues channel

**James**

Making my first venture into flumine using the marketrecorder ([https://github.com/betcode-org/flumine/blob/master/examples/marketrecorder.py|https://github.com/betcode-org/flumine/blob/master/examples/marketrecorder.py](https://github.com/betcode-org/flumine/blob/master/examples/marketrecorder.py|https://github.com/betcode-org/flumine/blob/master/examples/marketrecorder.py)). I get a “no module named strategies” error even though I’ve installed all the dependencies. What am I doing wrong?

---

## 2023-01-13 14:52:00 - general channel

**river_shah**

```Going big...

Do you expect more than 2^32 ~4,2 billion rows? Compile polars with the bigidx feature flag.



Or for python users install pip install polars-u64-idx.```

---

## 2023-01-11 12:36:09 - issues channel

**JFP**

Just noticed a significant discrepancy when backtesting with different versions of Flumine.

Original backtesting completed back in Dec 2021 with Flumine 1.19.14 showed consistent profit for a strategy that places a lot of passive bets.

Have been running this strat live with success.

Just reran the same data with latest version of Flumine 2.3.1 which gave approx. break even. Ran backtest against periods when it was running live and it gave negative results when my live results were positive.

Reinstalled 1.19.14 and rerun Backtest, got original positive results and also got positive results that roughly match my actual results for live trading periods.

Installed Flumine 1.21.0 (when smart matching was implemented) and get the same negative results as per 2.3.1.

The docs for smart matching says, for backtesting, it removes double counting of size for passive orders. Just after some more clarification on this, is this to remove double counting when running multiple strategies (ie: simulated middleware with live strat)?

---

## 2023-01-10 12:36:21 - issues channel

**D C**

Its a steep learning curve if you are new to these things but there are no shortcuts really. Just the existence of BFLW is the biggest shortcut you could possibly get

---

## 2023-01-05 17:44:46 - general channel

**Mo**

I'm into low latency stuff so Docker isn't really compatible with that approach - I don't have anything against it though



We use ansible to manage all of our infrastructure - in addition to what Python virtual environments should be set up with what packages installed we also use it to declare what OS packages should be installed, what cron jobs should be created, what services should be running, what directories should exist, which OS users should exist, etc. etc. I certainly wouldn't recommend it if the only thing you need to solve is how to manage your Python virtual environments. But if you wanted a tool that let you manage them on top of everything else I mentioned then it is very powerful

---

## 2023-01-05 13:35:42 - general channel

**dont**

It shouldn't be very hard to install a new version. You can also just use one image that comes with python 3.11 preinstalled.

---

## 2023-01-05 13:30:55 - general channel

**birchy**

Thanks [@U4H19D1D2](@U4H19D1D2). Having read a handful of articles, I was swaying towards Ansible but now I'm not so sure, particularly given that AWS Lightsail (my preferred VPS as it's a simplified EC2 setup) has capability to add containers by simply supplying a docker file. I know you use EC2, but is your preference to run lots of small instances, or to have a larger one with multiple containers? With Docker, are there any issues with running different versions of python on a Linux (Ubuntu) VPS? For example, if my Ubuntu version comes with python 3.9, how easy is it to install 3.11 inside a container? I've had issues in the past with installing newer versions as it can get a bit messy, particularly if we have to resort to using PPA's.

---

## 2023-01-05 09:57:08 - general channel

**birchy**

Thanks all, I need to get my R&amp;D cap on and see which of your suggestions are best suited to my operation. My main requirements are to be able to easily deploy multiple Flumine instances in a way that allows for future expansion. Not sure if I need a full container setup, but will investigate and ask questions later... :grinning:

---

## 2023-01-04 23:23:20 - general channel

**Oliver**

Docker/containers have merits, and can be another layer to go with virtualenvs if you want, or you can cut out the virtualenv entirely because you are installing packages straight inside the container instead of a containerised virtualenv. I don't know your deployment experience/environment, but you may find docker is OTT.



I'd say docker/containers (as there are other alternative container runtimes) is an additional isolation/encapsulation layer which can be pretty cool but does have management overhead. You could go in other directions for similar effect, like using packer to produce virtual machine images to then deploy to machines (e.g. EC2/GCP/... instances), and in that or outside of that you could use things like ansible/chef/puppet (ansible probably is best for this kind of smaller scenario thing so can see why Mo mentioned it), and also a layer like terrafrorm (for extra info: terragrunt is also a good layer for it but I doubt so for the scale required in this case) above that to manage the provisioning of your infrastructure (e.g. from the point of spinning up cloud resources if you've gone that way).



I'd still put emphasis on the likes of Pipenv as your first stop as it isn't conceptually (or in operations) much more than the virtualenvs you are using, but has things that are significant for long term management and reproducibility (i.e. exact package version pinning using the lockfile, a bit like using `pip freeze &gt; requirements.txt` but without being a such a mess to untangle when you want to upgrade something). Another good thing is pipenv/virtualenvs will continue to work nicely with editors and you can fire them up easily and without extra permissions on machines (although the permissions is likely not an issue for you).



Just for more info: a thing from before the likes of Pipenv was [https://pypi.org/project/pip-tools/|pip-tools](https://pypi.org/project/pip-tools/|pip-tools) which isn't far removed from the niceness of Pipenv. That will do the dependency locking side of things, but you'd still want to make the environments you install into (fresh VMs, constainers, virtualenvs, or bare metal).



If I blogged or was in consultancy, I'd be inclined to draw out graphs (or a graph) showing the potential dependencies of provisioning with spiel about the different parts...

---

## 2023-01-04 23:16:37 - general channel

**Fab**

My suggested approach is also Docker. Here's a simple blueprint to get you started...



Assuming you have two Python programs (`run-oldstrategies.py`, `run-newstrategies.py`), we are on your dev machine (Linux Debian) in the directory that contains those two programs.



*Step 1 - Create separate environment requirement files*

Activate the environment containing libraries for the old strategies then do `pip freeze &gt; requirements-oldstrategies.txt`. Do the same for the new strategies environment to generate `requirements-newstrategies.txt`.



*Step 2 - Create separate Dockerfile(s)*

Create two empty text files: `Dockerfile-oldstrategies`, `Dockerfile-newstrategies`. As an example, here's what you could put inside Dockerfile-oldstrategies (you can easily figure out the other):

```FROM python:3.9-slim-bullseye

RUN apt update -y

WORKDIR /opt/myproject

COPY ./requirements-oldstrategies.txt .

RUN cat requirements-oldstrategies.txt | grep -v '==0.0.0' &gt; requirements-oldstrategies.sanitised.txt

RUN pip install --no-cache-dir --upgrade -r requirements-oldstrategies.sanitised.txt

COPY . .

ENTRYPOINT ["python", "run-oldstrategies.py"]```

*Step 3 - Install Docker*

[https://docs.docker.com/engine/install/debian/](https://docs.docker.com/engine/install/debian/)



*Step 4 - Build separate Docker images for the two programs*

```docker build -t run-oldstrategies -f ./Dockerfile-oldstrategies .

docker build -t run-newstrategies -f ./Dockerfile-newstrategies .```

*Step 5 - Install Docker on your production machin*e

Same as Step 3



*Step 6 - Transfer Docker images from your current machine to the production machine*

```docker save run-oldstrategies | bzip2 | ssh &lt;USER&gt;@&lt;PRODUCTION_IP&gt; docker load

docker save run-newstrategies | bzip2 | ssh &lt;USER&gt;@&lt;PRODUCTION_IP&gt; docker load```

*Step 7 - Log into production machine, make sure images are there*

```docker images```

*Step 8 - Start both Docker containers*

```docker run -d run-oldstrategies

docker run -d run-newstrategies```

*Step 9 - How to check logs for a Docker container*

Run `docker ps -a` to get the hash of each container then you run the following command:

```docker logs &lt;CONTAINER_HASH&gt;```



---

## 2023-01-04 22:55:32 - general channel

**dont**

ansible - bleah. You can just `pip freeze` your venv into a `requirements.txt` which then you get to install on the production machine. Alternatively you can just work with a docker container as Liam says on both dev/prod and deploy the container.

---

## 2023-01-03 23:03:49 - general channel

**birchy**

[@U02RN7YDRQ9](@U02RN7YDRQ9) I'm fine with Pycharm on my development machine. My production stuff is on a headless Linux VPS. :+1: 

[@URMM9463X](@URMM9463X) I'm thinking more along the lines of automating the setup &amp; launch via a script. It seems like a common workflow for which management tools would already exist but Google has muddied the waters and/or I'm not using the correct terminology. My basic manual workflow would be something like:

1. login to remote server via SSH

2. create venv

3. activate venv &amp; install libraries (Flumine, etc)

4. git clone strategy code

5. launch python strategy

6. logout of SSH

---

## 2023-01-03 21:54:58 - general channel

**birchy**

Bit of a noob question, but what's the recommended beginner friendly way to manage/automate python venv's on a Linux production machine? To be more specific, I've only used venv's created by Pycharm on my development machine but now I'm getting to a point where I have old bots chugging away in production but need to run others with newer libraries . Venv is the obvious way to achieve this without fucking up the older ones running on the main system, but I'm wondering how best to automate venv installation and setup for spinning up new bot instances on a single machine?

---

## 2022-12-13 18:03:46 - issues channel

**Liam Querido**

Okay, that makes sense. But how do you install the package in editable model? Is it a similar idea to pip install?

---

## 2022-12-12 15:59:56 - random channel

**D C**

I also question the security risk being limited to account funds - as you (or anyone who hacked you and obtained user details) would be able to login to any user account that didnt have 2FA setup and see their address, phone etc. If nothing else that is a risk of identity theft. Not saying you would of course, and if you customers are happy with that risk its their business. I just cant agree that risk is isolated to current account funds.

---

## 2022-12-04 06:46:37 - general channel

**Tony**

Hi, I am very impressed with this forum and I am interested in learning more about backtesting and strategy development. I am a university student and I am unable to afford the pro data, which is quite expensive. Is there an alternative to using pro data for beginners who are just starting out? It seems that some people have run into errors when using only the free data, and while there are a few months of free, full data available, I am not sure if this would be sufficient for testing the significance of a strategy. Thanks all for your help

---

## 2022-11-19 15:31:55 - issues channel

**Mo**

Sorry I’m not a windows user so can’t really help but I take the message to mean that your version of OpenSSL installed is incapable of meeting the minimum TLS version that the Betfair login server requires 

---

## 2022-11-15 13:48:40 - random channel

**PeterLe**

Just wondered if anyone had upgraded their Python version last night and found it worthwhile?

Im going to read up tonight the best way to do this on ubuntu (on Lightsail) on AWS

is it relativley easy to upgrade? Would you remove the old version completely?

It was easy enough to setup the instance on Ubuntu to start with so maybe create a new instance from scratch ?

Any thoughts please? thanks

---

## 2022-11-02 23:48:59 - random channel

**D C**

On the stream API, when making requests you supply an "id" field to match responses to a subscription request. Docs say specifically that



`id - A unique counter you should supply on a RequestMessage and which will be supplied back on a ResponseMessage.`



I've always assumed that the "uniqueness" here is with respect to each connection, rather than accross ALL connections you may use. Essentially I am asking if it is possible that I am causing problems running say 2 streams connections but using the same ID on the market subscription requests? Clutching at straws a bit here but just wondering if people use globally unique "id" fields across their entire production setup or if uniqueness inside each connection is sufficient.

---

## 2022-11-01 06:28:49 - issues channel

**Muhammad Adeel Zahid**

Ok, when I try to run the following code

```trading = betfairlightweight.APIClient(username = my_username, password = my_password, app_key = my_app_key, certs=certs_path)

trading.login()

market_id = "1.199777126"

selection_id = 31484513

resources = trading.race_card.get_race_card(market_ids=[market_id])

print(resources)```

I get the exception

`Traceback (most recent call last):`

  `File "E:\Git\betfair\dailyracevenuedatagrabber.py", line 37, in &lt;module&gt;`

    `resources = trading.race_card.get_race_card(market_ids=[market_id])`

  `File "E:\Git\betfair\venv\lib\site-packages\betfairlightweight\endpoints\racecard.py", line 59, in get_race_card`

    `raise RaceCardError(`

`betfairlightweight.exceptions.RaceCardError: You need to login before requesting a race_card`

`APIClient.race_card.login()`

when I change `trading.login()` to `trading.race_card.login()`

I get the following exception

`Traceback (most recent call last):`

  `File "E:\Git\betfair\venv\lib\site-packages\urllib3\connectionpool.py", line 703, in urlopen`

    `httplib_response = self._make_request(`

  `File "E:\Git\betfair\venv\lib\site-packages\urllib3\connectionpool.py", line 386, in _make_request`

    `self._validate_conn(conn)`

  `File "E:\Git\betfair\venv\lib\site-packages\urllib3\connectionpool.py", line 1040, in _validate_conn`

    `conn.connect()`

  `File "E:\Git\betfair\venv\lib\site-packages\urllib3\connection.py", line 414, in connect`

    `self.sock = ssl_wrap_socket(`

  `File "E:\Git\betfair\venv\lib\site-packages\urllib3\util\ssl_.py", line 449, in ssl_wrap_socket`

    `ssl_sock = _ssl_wrap_socket_impl(`

  `File "E:\Git\betfair\venv\lib\site-packages\urllib3\util\ssl_.py", line 493, in _ssl_wrap_socket_impl`

    `return ssl_context.wrap_socket(sock, server_hostname=server_hostname)`

  `File "C:\Users\adeel\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 512, in wrap_socket`

    `return self.sslsocket_class._create(`

  `File "C:\Users\adeel\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1070, in _create`

    `self.do_handshake()`

  `File "C:\Users\adeel\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1341, in do_handshake`

    `self._sslobj.do_handshake()`

`ssl.SSLError: [SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:997)`



`During handling of the above exception, another exception occurred:`



`Traceback (most recent call last):`

  `File "E:\Git\betfair\venv\lib\site-packages\requests\adapters.py", line 440, in send`

    `resp = conn.urlopen(`

  `File "E:\Git\betfair\venv\lib\site-packages\urllib3\connectionpool.py", line 785, in urlopen`

    `retries = retries.increment(`

  `File "E:\Git\betfair\venv\lib\site-packages\urllib3\util\retry.py", line 592, in increment`

    `raise MaxRetryError(_pool, url, error or ResponseError(cause))`

`urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='[http://www.betfair.com|www.betfair.com](http://www.betfair.com|www.betfair.com)', port=443): Max retries exceeded with url: /exchange/plus/ (Caused by SSLError(SSLError(1, '[SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:997)')))`



`During handling of the above exception, another exception occurred:`



`Traceback (most recent call last):`

  `File "E:\Git\betfair\venv\lib\site-packages\betfairlightweight\endpoints\racecard.py", line 28, in login`

    `response = session.get(self.login_url)`

  `File "E:\Git\betfair\venv\lib\site-packages\requests\api.py", line 75, in get`

    `return request('get', url, params=params, **kwargs)`

  `File "E:\Git\betfair\venv\lib\site-packages\requests\api.py", line 61, in request`

    `return session.request(method=method, url=url, **kwargs)`

  `File "E:\Git\betfair\venv\lib\site-packages\requests\sessions.py", line 529, in request`

    `resp = self.send(prep, **send_kwargs)`

  `File "E:\Git\betfair\venv\lib\site-packages\requests\sessions.py", line 645, in send`

    `r = adapter.send(request, **kwargs)`

  `File "E:\Git\betfair\venv\lib\site-packages\requests\adapters.py", line 517, in send`

    `raise SSLError(e, request=request)`

`requests.exceptions.SSLError: HTTPSConnectionPool(host='[http://www.betfair.com|www.betfair.com](http://www.betfair.com|www.betfair.com)', port=443): Max retries exceeded with url: /exchange/plus/ (Caused by SSLError(SSLError(1, '[SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:997)')))`



`During handling of the above exception, another exception occurred:`



`Traceback (most recent call last):`

  `File "E:\Git\betfair\dailyracevenuedatagrabber.py", line 34, in &lt;module&gt;`

    `trading.race_card.login()`

  `File "E:\Git\betfair\venv\lib\site-packages\betfairlightweight\endpoints\racecard.py", line 30, in login`

    `raise APIError(None, self.login_url, None, e)`

`betfairlightweight.exceptions.APIError: [https://www.betfair.com/exchange/plus/](https://www.betfair.com/exchange/plus/)` 

`Params: None` 

`Exception: HTTPSConnectionPool(host='[http://www.betfair.com|www.betfair.com](http://www.betfair.com|www.betfair.com)', port=443): Max retries exceeded with url: /exchange/plus/ (Caused by SSLError(SSLError(1, '[SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:997)')))`

Please note that my certificate setup and credentials are correct as I am able to use other API methods like `trading.betting.list_market_catalogue` . What could be the reason of this exception for this particular endpoint?

---

## 2022-10-26 13:34:33 - strategies channel

**Guy Adini**

Thanks Mo - I'm working on this together with Artiom, so this is super helpful to me as well...

I understand the part about batb levels all changing when a level disappears, that's clear.

The other - about virtualization from the other side, is new to me - I didn't realize that they do that!



So if I have a two runner market, say over and under, and I have, for "over" atb [[1.9, LIQ_AMOUNT]], then what is the corresponding virtual price and amount for "under"? Is there maybe some link explaining this?

---

## 2022-10-25 20:06:03 - random channel

**river_shah**

have you even been able to install flumine / bflw with 3.11?

---

## 2022-10-22 09:44:51 - random channel

**Mo**

Also package everything and have never run in to this problem. But then I deploy by git cloning and pip install -e .

---

## 2022-10-22 09:39:28 - random channel

**river_shah**

[@UBS7QANF3](@UBS7QANF3) Is `setuptools` still the recommended way to package up a project that includes python, cython and compiled `.so`? I see that in `package_data` I can list all the non python dependencies. I also see that somehow `setuptools` infers if binary distribution and appends the appropriate abi tags such as this `aarch64.whl`

---

## 2022-10-22 09:17:03 - random channel

**river_shah**

These are the contents of `setup.py` this is the command line used to create the dist

```python setup.py sdist bdist_wheel

....

/usr/local/lib/python3.10/site-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.```



---

## 2022-10-22 08:46:57 - random channel

**river_shah**

[@U4H19D1D2](@U4H19D1D2) I shamelessly copied how you package up `flumine` for some of my projects. Not a major issue but I get deprecation warnings (`SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools`). Do you have a recommendation what the best tool set for pip installable package / wheels is?



Stackoverflow is not particularly helpful: [https://stackoverflow.com/questions/58753970/how-to-build-a-source-distribution-without-using-setup-py-file](https://stackoverflow.com/questions/58753970/how-to-build-a-source-distribution-without-using-setup-py-file)

Seems like `setup.py` is still the easiest way to package up python / shell scripts despite the deprecation warnings.

---

## 2022-10-18 12:52:57 - issues channel

**Artiom Giz**

Hello!

I have an issue with *Java* code ([https://github.com/betfair/stream-api-sample-code](https://github.com/betfair/stream-api-sample-code))

• Cloned the code :white_check_mark:

Running `mvn install` :

• *Build worked* (after adding javax.annotation to pom.xml) :white_check_mark:

• *Tests fail* (mostly "StartStop", sometimes single test, sometimes two or three) :eyes:

Q1: Somebody might be met this issue? Or say something about it (fix/remove tests/...)?

Q2: Is this code widely used and supported?

Q3: Trying to understand the best way to combine my existing Java env with BF.  I see a lot of information about Python libs: *betfairlightweight* or *flumine*. Worth using them or it's the same (from support/problems POV)?



Thanks in advance, really appreciate!

---

## 2022-10-13 09:59:57 - issues channel

**liam**

Not sure where you got that example from but in the [https://github.com/betcode-org/betfair/blob/master/examples/examplestreaming.py|examples](https://github.com/betcode-org/betfair/blob/master/examples/examplestreaming.py|examples) we have some logging setup, if you set to DEBUG it might show the issue

---

## 2022-10-13 09:23:27 - issues channel

**Liam Querido**

Forgive me, I'm knew to Python, what exactly do you mean by logs?

---

## 2022-10-11 12:47:21 - general channel

**Tom**

Roger that thanks Ivan. It won't come up for me to use and says "ModuleNotFoundError: No module named 'fasttrack'" So I thought I needed to install a package. I'll check those out.

---

## 2022-10-11 06:07:56 - general channel

**Ivan Zhou**

you can't pip install the fasttrack library. You can get it from here [https://github.com/betfair-down-under/autoHubTutorials/tree/master/FastTrack](https://github.com/betfair-down-under/autoHubTutorials/tree/master/FastTrack).



There is a tutorial on how to use fasttrack here [https://betfair-datascientists.github.io/modelling/fasttrackTutorial/](https://betfair-datascientists.github.io/modelling/fasttrackTutorial/)

---

## 2022-10-11 06:02:25 - general channel

**Tom**

Also, some of the code in the Flumine Tutorial 4 refers to fasttrack as Python package; but I'm unable to install or use it. I'm fairly new to this and it's probably some obvious problem.

---

## 2022-10-10 16:39:39 - general channel

**Pos**

Yes it logs in. Ok yes I am serious about it. I'll try get setup on the api. Question for you [@U9JHLMZB4](@U9JHLMZB4), I'm running node for my application but everyone here is using python and they say its a better choice as there's more resources here. Do you think its worth going the python route and then using sockets to communicate the information to my node app?

---

## 2022-10-09 13:32:16 - general channel

**Pos**

[@UBS7QANF3](@UBS7QANF3) Not sure, maybe because i feel like there's less of a barrier to getting started quickly. Its kind of confusing getting started on the api and it seems like everyone is using python while i'm using node js

---

## 2022-10-04 21:05:07 - issues channel

**mp2003**

Hi all, I'm a beginner to betfairlightweight, although know a bit of Python. I've got an app key and SSL cert sorted, and managed to log in OK. When running the example code for 'Streaming' in Jupiter Notebook, I can run all the code OK except the last part, which just hangs on the egg timer and does not complete - no errors, resources on my machine are fine etc.



This is when running both the 'Streaming' example code in [https://betcode-org.github.io/betfair/streaming/](https://betcode-org.github.io/betfair/streaming/) (the '# check for updates in output queue' section) and also the streaming area in [https://github.com/betcode-org/betfair](https://github.com/betcode-org/betfair) (at the line 'betfair_socket.start()')



Have restarted python/web browser - at a bit of a loss! Any help would be really appreciated, thank you.

---

## 2022-09-22 23:18:00 - betconnect channel

**Mark Wells**

Hi guys. I'm trying to log in to the api for the first time with a staging account. I'm getting an error in

```client.account.login() ```

---

## 2022-09-19 07:48:05 - general channel

**Tom**

Hi guys, I am new to coding- I've done about 120 hours of training in Python in a Udemy course, which was ok but decided to get into a project to maintaining the trajectory of interest and have a background in financial markets and thought I would test an idea I've had in Horse Racing pricing, so am building a Betfair bot.



Although I don't know enough to really understand it at depth, Liams work is pretty impressive and appreciate the sharing (and no doubt others in here contributed, it's pretty cool/impressive what some people can do with this stuff)



```Anyway, the question I had is the code below - for the part that says if runner_book.ex.available_to_back - is that returning a boolean that will progress to runner_book.ex.available_to_back[0].price (to avoid an error) and will instead give us the extreme result automatically (1.01, or 1000 for the lay options)?```

```best_back_prices = [runner_book.ex.available_to_back[0].price

    if runner_book.ex.available_to_back

    else 1.01

    for runner_book

    in runner_books]```

---

## 2022-09-06 17:27:58 - issues channel

**Mona**

Hello guys, I am new to here.

I am working on some historical data for a particular market when events are inplay and trying to get the latest traded price time series. Has anyone have any experience with the Rust library they used on the tutorial? I have got to the point where all prices return within the Market.runner object is None, I am trying to understand whether it is the package problem or whether it is my understanding of the historical data structure that I need to do some modification?

Also the package is said to work with betfairlightweight as some of the functions can return MarketBook object, but I can't access its MarketBook._data attribute.

Thanks very much for help

---

## 2022-09-03 09:22:38 - random channel

**Newbie99**

The default output as you say is 127.0.0.1:4000 (or localhost:4000). However I have an elastic IP setup on AWS, which normally I send data to via Flask as follows:



```socketio.run(app, debug=False, host='0.0.0.0', port=PORT_NO)```

I can then view the output as expected from my app.



However (obviously not running my flask app at this point) when I put in the output as 0.0.0.0 and any port from cprofilev the page doesn't exist.



So I'm assuming I'm missing something simple.

---

## 2022-08-27 10:13:57 - general channel

**birchy**

Numpy is now working in PyCharm, but not really sure what the fix was. So I'd installed python 3.10 apple silicone version and was using that for PyCharm and running my code in the terminal as it became the default for `python3`. I then removed 3.10 which left me with the default 3.8 version and now PyCharm &amp; numpy work as expected. Haven't looked into the details but I suspect the default mac version may be Intel compatible.

---

## 2022-08-26 14:54:11 - general channel

**LF**

conda/mamba are usually much painless when you want to install python scientific libraries

---

## 2022-08-26 14:42:34 - general channel

**LF**

Anyway I think if you can actually install it and use it directly on your machine from the terminal  Pycharm is just pointing to the wrong python, my suggestion would be to have a fresh python installation either conda/mamba or use virtualenv and Pycharm should work

---

## 2022-08-26 12:32:21 - general channel

**birchy**

I'm having problems with numpy in PyCharm on a MacBook. If I import numpy in a python console, it's fine, however in PyCharm it complains something about architecture being wrong. This on an M1. Does anyone have any advice on PyCharm/numpy installation? I tried uninstalling and installing via PyCharm but still no joy. Baffled TBH.

---

## 2022-08-23 13:14:37 - general channel

**birchy**

So presumably, the `[speed]` install has issues on Windows? I've always used the default Flumine install as I (wrongly) thought that `[speed]` was not compatible as it's not the default version. I prefer Linux but occasionally develop on a Windows machine as it has work related software that is not available on other OS's. Is it worth installing `[speed]` on Windows, or is not incompatible/too much hassle?

---

## 2022-08-23 10:17:38 - random channel

**PeterLe**

Well as you know I'm still learning how to use Python. From knowing nothing, it wasn't as bad as i thought to get the recorder and a few strategies running (the latter with help from others on here and your examples).

I've now started to build out from those initial strategies and 'bolt stuff' on. Its a really good way of learning by the way, by using the simulator to test code (if anyone else is a beginner)

I've also learned Numpy; Pandas, Jupyter and a bit of C# too. I know have my recorders/strategies running on Ubuntu, which was easy to implement and virtually maintenance free....phey!

However, the more I learn about Python, the more I realise there's a lot more to learn, so this takes time and is part of the process. So in answer to your question, there is no one part as such, its a combination of everything

For me though, i just think of the whole thing as another tool/mentality/approach. It wont replace my preferred method of strategy development implementation, which i mentioned in the opening post, I see it more of a tool to enhance that.

I can see that there are some very technically competent folk on here who maybe not making a profit, I think that is because of the path you get led down and how your thought processes develop/channeled if you use this as your sole MO.

Either way, I'm not in any rush and the money is still rolling in, so just enjoying the trip!

---

## 2022-08-22 18:01:06 - random channel

**PeterLe**

So a question to the pro’s please

So once you have your data (in sample and out of sample etc)..its useful to tweak existing strategies etc I’ve used this lately with some good success (even found a brand new strategy too)



Question is: What is the next step in using the recorded data, do you collect additional data via logging controls and analyse with pandas/db etc

I just wondered what steps you would take from recording the data through to going live with a new strategy (just bullet points and a few pointers would be great for someone new to this approach)

(By the way; I read an entry by [@UGV299K6H](@UGV299K6H) a week or so ago about testing a well thought out hypothesis live and seeing how it plays out. it really struck a chord with me. This tends to be my approach too. Ill still continue with this but looking at alternative approaches too)

Many thanks

---

## 2022-08-22 09:21:31 - general channel

**mandelbot**

Is this still relevant?

```Installing betfairlightweight[speed] will have a big impact on processing speed due to the inclusion of C and Rust libraries for datetime and json decoding.```

---

## 2022-08-22 08:57:55 - issues channel

**mandelbot**

I'm trying to run multiprocessing on backtests for the first time (I know right?) and i keep getting the following error:



```TypeError: don't know how to handle uri Ellipsis```



```concurrent.futures.process._RemoteTraceback: 

"""

Traceback (most recent call last):

  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/concurrent/futures/process.py", line 246, in _process_worker

    r = call_item.fn(*call_item.args, **call_item.kwargs)

  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/flumine/strategy/testmulti.py", line 41, in run_process

    framework.add_strategy(strategy)

  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/flumine/baseflumine.py", line 101, in add_strategy

    self.streams(strategy)  # create required streams

  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/flumine/streams/streams.py", line 46, in __call__

    market_type = get_file_md(market, "marketType")

  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/flumine/utils.py", line 66, in get_file_md

    with open(file_dir, "r") as f:

  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/smart_open/smart_open_lib.py", line 224, in open

    binary = _open_binary_stream(uri, binary_mode, transport_params)

  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/smart_open/smart_open_lib.py", line 396, in _open_binary_stream

    raise TypeError("don't know how to handle uri %s" % repr(uri))

TypeError: don't know how to handle uri Ellipsis

"""



The above exception was the direct cause of the following exception:



Traceback (most recent call last):

  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/flumine/strategy/testmulti.py", line 63, in &lt;module&gt;

    job.result()  # wait for result

  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/concurrent/futures/_base.py", line 439, in result

    return self.__get_result()

  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/concurrent/futures/_base.py", line 391, in __get_result

    raise self._exception

TypeError: don't know how to handle uri Ellipsis```

Can't figure it out, anyone have any ideas?

---

## 2022-08-21 19:03:34 - random channel

**birchy**

I've not used selenium but from my web scraping days, the setup was to enable cookies, simulate login request and IIRC the session token was in the headers and/or cookies? The login type was "interactive" without certs and I believe you had to load the main page first to initiate the cookies or something?

In hindsight, I think I've misunderstood the question but will leave my answer anyway. :grinning:

---

## 2022-08-21 18:55:04 - random channel

**Newbie99**

Completely off topic, but I'm a bit stuck with this...does anyone know how to either:



a) Enter credentials for a chrome extension via Selenium at run time



or



b) Start a new Selenium Chrome webdriver session with extensions already installed?



I can start a new session and load up the extension (Nord VPN in case anyone has gone down a similar route in the past), but I can't work out how to actually log into the Nord VPN chrome extension (I'm using Brave if we're being picky, but essentially that's Chrome).



Just wondering if any of you webscrapers have solved this in the past?

---

## 2022-08-20 11:09:34 - random channel

**Dave**

Hardware question: I'd like to have an external drive(s) that's continuously kept synced with my S3 bucket (say once a day is fine). I'd also like to access said drive via a relatively quick connection (presumably USB will be sufficient) - something close enough to as if it was an internal drive. Anyone have any setups/components they can recommend for this?

---

## 2022-08-18 09:06:24 - random channel

**liam**

This is one of the negatives of flumines simplicity, in a more complex trading system you would separate the different components to allow strategy/framework/execution/price code to be updated without downtime.



My understanding is that [@UBS7QANF3](@UBS7QANF3) system allows this but it obviously comes at a complication/setup cost

---

## 2022-08-17 23:34:15 - general channel

**river_shah**

There is a system python but I think it defaults to 3.7. You can just download 3.10 and it does have an M1 optimised installer (you won't need to deal with building it etc)

---

## 2022-08-17 23:23:11 - general channel

**birchy**

I'm finally going to get my hands on a MacBook M1 in the near future (daughter has one that she rarely uses and has agreed to add an account for me) but as a Linux and Android user, I'm a complete noob to all things Apple. Have just had a quick Google for "MacBook M1 python development" and it looks to be a minefield of recommendations for homebrew, emulators and native installations.

This thing will basically be used exclusively for Flumine development and simulations, so my basic requirements would be:

• Python 3.10+

• PyCharm

• Git/GitHub

• Jupyter

• SSH

Any advice or links on how to achieve this setup in an uncomplicated way, things to avoid/watch out for, recommendations, etc?

I'm assuming that once python is installed, all other dependencies and libraries can be installed using `pip` in the usual way?

---

## 2022-08-08 00:22:53 - general channel

**Unknown**

Well I got it down to 25mins for 3000 files on an 8 vcpu instance. Did it with some code edits and use of the multiprocessing package which, as I understand it, is making use of all the cores by processing each file asynchronously. Couldn't reduce the time using the threading package. All in all a good learning experience! For anyone else new to multiprocessing using python I would recommend [https://www.youtube.com/watch?v=fKl2JW_qrso&amp;t=1215s|this video](https://www.youtube.com/watch?v=fKl2JW_qrso&amp;t=1215s|this video).

---

## 2022-08-03 14:39:15 - random channel

**birchy**

This is a general programming question for the python gurus. I have a library of boilerplate stuff that I install via:



`python3 -m pip install -e [git+ssh://github/|git+ssh://github/](git+ssh://github/|git+ssh://github/)...`



Inside the `__init__.py` of that library, I have:



`import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())`



...and inside each module of my library I have:



`import logging

logger = logging.getLogger(__name__)`



As far as I understand it, that's a conventional setup for libraries and logging handlers should be setup by the end user. When I import and use the library, I setup a root logger like this:



`import logging

from time import gmtime

from pythonjsonlogger import jsonlogger

from logging.handlers import RotatingFileHandler`



`logger = logging.getLogger()

custom_format = "%(asctime) %(levelname) %(message)"

os.makedirs('logs', exist_ok=True)

log_handler = RotatingFileHandler('logs/flumine_log.txt', maxBytes=int(1e6), backupCount=10)

formatter = jsonlogger.JsonFormatter(custom_format)

formatter.converter = gmtime

log_handler.setFormatter(formatter)

logger.addHandler(log_handler)

logger.setLevel([http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))`



When running my code, none of the library logging messages are saved or outputted. I'm clearly missing something obvious. Any suggestions?

---

## 2022-08-03 09:51:58 - strategies channel

**liam**

Yes but that strategy is setup for live with the filters 

---

## 2022-08-01 10:53:00 - strategies channel

**Mo**

Some thoughts:



1. SVM is an odd choice; if you want state of the art then use XGBoost. If you want simplicity, speed, ease of implementation and a method that has stood the test of time then use Logistic Regression

2. I'm not sure about including starting odds - you mention form, speed, rating: all of these will already be incorporated into the odds. So it will come down to whether there is any marginal value in your "own inputs" over and above the odds

3. Another downside to starting odds is they are only available when the race starts. Typical setup for a pre-race strategy would be to use the starting odds (implied probabilities) as the target for your model rather than binary win/loss

4. I think you're thinking along the right lines with what I'll summarise as "truncated finishing positions" although I still think just using the implied probabilities from the starting odds would be way better

---

## 2022-07-27 13:32:56 - general channel

**Michael**

I'm quite new to coding so struggling to read the docs for Flumine. If I'm creating the strategy outside of Flumine (i.e. I have marketID and I have runnerID and amount I'd like to bet) do I need to have a strategy class or can I just use Baseorder?

---

## 2022-07-27 13:31:09 - issues channel

**PeterLe**

yea i decided to have a crack at Ubuntu as Lee mentioned it was a good way to go.

It was very easy to setup via Lightsail (I didn't know the first thing about Ubuntu Linux)

Python was vey easy to install too. (Run from the command line python3 file.py

I then moved four strategies and a couple of recorders over

I still dont know much about it, but it does what i need it to do, so 'good enough is good enough'! :grinning:

---

## 2022-07-27 13:24:33 - issues channel

**birchy**

[@UVB1RFEP5](@UVB1RFEP5) as [@UBS7QANF3](@UBS7QANF3) has said, understanding how Linux works is the biggest barrier but nowadays that's not a particularly steep learning curve. It would probably be worthwhile you playing around with Ubuntu by either installing on your machine as a dual boot or on an old pc/laptop/rasp pi. You can also boot most Linux's as a "live" image that runs off cd/dvd/usb stick without installing anything. They run as a full OS in ram but can be a bit slow as a result, however, it allows you to assess a Linux session without making any permanent changes. Alternatively, you could dive straight into an AWS Lightsail instance and learn how to administer it over SSH as that's what your end goal is. [@UQL0QDEKA](@UQL0QDEKA) has done this recently and said he found it much easier than expected and now has a handful of strategies running remotely.

---

## 2022-07-19 14:46:53 - betconnect channel

**Mick**

I've fallen at the first hurdle trying to use betconnect. I have done pip install betconnect, then if I just run this:



`import betconnect`

`from betconnect.apiclient import APIClient`



I get... ModuleNotFoundError: No module named 'betconnect.apiclient'; 'betconnect' is not a package

---

## 2022-07-13 11:49:11 - random channel

**Leo**

Yeah it's a tricky one really. I use fundamental models and my general assessment is that the chances of a horse improving significantly over a new distance or first time in handicaps etc is usually overestimated in the market in comparison to its previous form. But there are definitely exceptions 

---

## 2022-07-12 17:57:32 - general channel

**WaftyCrancker**

I actually have a Udemy subscription, it's what I took my previous python course on, it wasn't the one you have posted, it was by Giles McMullen-Klein, so I may take a look at you suggestion as well. I also have PyCharm already installed.

---

## 2022-07-12 17:23:48 - general channel

**PeterLe**

Just to add...

This is a great course for a beginner:

[https://www.udemy.com/course/the-modern-python3-bootcamp/](https://www.udemy.com/course/the-modern-python3-bootcamp/)



DONT pay more than £20 for the course, search for a coupon..

---

## 2022-07-11 14:49:18 - issues channel

**Gib**

thanks for quick response liam, yes looks like i got an error when installing logging. will try to get that working...  Great job putting these resource together, really appreciate it.

---

## 2022-07-09 11:15:31 - general channel

**D C**

I'm pretty new to AWS and I just SCP my files to a local store at the end of each day. I looked as S3 but I just saw it as extra costs. What do the people who use S3 consider to be the main upside?

---

## 2022-07-02 11:20:04 - random channel

**river_shah**

Checking if of interest to anyone in the community: I am looking for a developer to help setup some core infra / data collection / middleware / simulation systems. I am too occupied on other projects and have not done this work properly even after 18+ months of betting.



Will pay competitive day rates for the initial build phase and any ongoing support needed. Familiarity with `flumine` and `bflw` a must. Please direct message me if of interest and we can walk through more details.

---

## 2022-06-15 19:41:09 - strategies channel

**birchy**

[@U01A64T6DJQ](@U01A64T6DJQ) as suggested above, try it live with minimum flat stakes ($1 or whatever). More importantly, make sure you have setup bet logging as that will give you "real world" data that you can analyse later.

[https://github.com/betcode-org/flumine/blob/master/examples/controls/backtestloggingcontrol.py|https://github.com/betcode-org/flumine/blob/master/examples/controls/backtestloggingcontrol.py](https://github.com/betcode-org/flumine/blob/master/examples/controls/backtestloggingcontrol.py|https://github.com/betcode-org/flumine/blob/master/examples/controls/backtestloggingcontrol.py)

---

## 2022-06-10 21:09:50 - general channel

**foxwood**

The proform data is in SQL server (last time I subscribed some years ago) so if you are on Windows then no need to export - just run queries to suit. Install SSMS (free) and explore with that. Use pyodbc for real time queries if you are a Python user. You can also run SQL queries from Excel.

---

## 2022-06-05 07:09:47 - random channel

**LM**

what approaches do people take to schedule flumine jobs so if becomes as hands off as possible? currently i'm killing of old process and restarting manually daily... Is there a way that flumine can add new markets as they are made available based on the filter provided (it could be setup to do this already, I'm just using it wrong....)?

---

## 2022-06-01 17:34:19 - random channel

**Peter**

[https://github.com/betcode-org/flumine/pull/577](https://github.com/betcode-org/flumine/pull/577)



It's still a pull request, so not yet integrated into the master branch of flumine. So not appropriate for inclusion in the docs, but you could install the last commit in the PR to try it out.

---

## 2022-05-21 11:17:44 - general channel

**Jonjonjon**

My first setup was a web page. The web page was Python. The Python placed the bets. To activate it I had to visit the web page. Can you beat that?

---

## 2022-05-06 08:54:11 - issues channel

**liam**

yeah, pandas install is the only thing stopping me doing it already tbh

---

## 2022-05-06 08:53:19 - issues channel

**Oliver Varney**

cool, I guess flumine would be the place to have it as a install requirement if liam ever wanted to use parts

---

## 2022-04-29 23:12:20 - general channel

**Tom**

```from matchbook.apiclient import APIClient

from matchbook.exceptions import AuthError, PasswordError, ApiError, MBError



import logging

import os

logger = logging.getLogger(__name__)

MATCHBOOK_PW = os.environ.get('MATCHBOOK_PW')

MATCHBOOK_USR = os.environ.get('MATCHBOOK_PW')

api = APIClient(MATCHBOOK_USR, MATCHBOOK_PW)



def get_client():



    try:

        if not api.session_token or api.session_token is None:

            api.login()

            logger.warn(f'this is the {api.session_token}')

    except (AuthError,ApiError,MBError):

            api.login()

    return api



def get_orders():

    api = get_client()

    r = api.betting.get_orders(runner_ids=None, market_ids=None, offer_id=None, offset=0, per_page=500,

                    interval=None, side=Side.Default, status=Status.All, session=None)

    print(r)

    print(api.session_token)```

Hi there, I was wondering if anyone is using this repo for matchbook [https://github.com/rozzac90/](https://github.com/rozzac90/)

I cannot log in again after 6 hours to refresh the token. For some reason I can't run the except block to create a new token when ApiError occurs. Does anyone know how best to handle logging in to refresh the session? My get orders function polls indefinitely so I need to be able to handle the logging in again when the token expires. Thanks

---

## 2022-04-29 08:34:42 - general channel

**liam**

Yeah, was talking to Rob about adding a getattr to allow `market_book.market_id` and `market_book["marketId"]`



There is then the question of how its added, does it become the default? Or used when installed? Or do we drop down into bflw as the default for processing historical data?

---

## 2022-04-26 15:29:18 - issues channel

**Beginner**

Guys, hello! I have a very beginner question but maybe you with very advanced knowledge can help me.



Is there a way to send API Client login data to a separate function? For example, I have the `trading.login()` in the `main()` function and I'm trying to send this data to be able to work with a separate function::



`def matches(trading):`

    `trading = trading`

    `id_event = '12345'`



    `filter_catalog_market = betfairlightweight.filters.market_filter(`

        `event_ids=[id_event],`

        `market_type_codes = [`

            `'MATCH_ODDS'`

            `]`

        `)`



    `catalog_market = trading.betting.list_market_catalogue(`

        `filter=filter_catalog_market,`

        `max_results='100',`

        `sort='FIRST_TO_START',`

        `market_projection=['RUNNER_METADATA']`

    `)`



`def main():`

    `trading = betfairlightweight.APIClient(username, pw, app_key=app_key, cert_files=('blablabla.crt','blablabla.key'))`

    `trading.login()`

    `matches(trading)`



The error that appears is:



`TypeError: cannot pickle 'module' object`



Is there any way to send this API Client login data to a separate function?

I'm sorry for the question that I know is simple, but I'm really struggling to understand.

---

## 2022-04-26 11:12:15 - strategies channel

**PirellOne**

hi All. I am Marco, from Italy, so no possibility to register on the [http://Betfair.com|Betfair.com](http://Betfair.com|Betfair.com) Api or even open account. So my question is: there's nobody from UK could help me just to get notifications (telegram, mail or whatelse..) when a massive bet is occurring only Soccer, only last 30 minutes before match starting PREGAME,  only MATCH ODDS market.. very easy task for someone having Api and know how to use Zapier or similar...i guess.. if you are interested just write..is something that would not break any betting law or any BETFAIR law.. example of this could be: 

GET notified when 10000£ bet  is made on HOME_WIN



..i am new to Slack. If i wrote in the wrong place just let me know..

---

## 2022-04-14 11:21:34 - general channel

**DFL**

Hi all, I hope this posting this here is considered kosher!



We have a sports trading team with background in (financial) algo trading industry that is looking to add developers. We've had initial success in a few different sports and really looking to scale up.



Python Developer: Looking for someone to help us collect new data, build new tools and automate our systems.



Core Developer: Also will be primarily python, prefer someone with development within Financial, Crypto or Sportsbetting. Need to have proficiency in building low-latency network applications and experience with low-latency trading applications is a huge plus.



We may also have a role for someone with a JavaScript background.



Our team is based in Dublin, but we may be open to other locations or remote for the right candidates. Let me know if you're interested in hearing more!

---

## 2022-04-13 12:17:24 - issues channel

**foxwood**

I'm running 2 live frameworks on same server for the first time - one for "ok" strategies and another for suspect ones and debugging.



As they both place bets it ends up with cross-talk warnings in the other framework's log log saying "Strategy not available to create order" and "Order %s not present in blotter". Was a bit worrying at first sight lol.



Presume this is in part caused by both frameworks having the socket hostname as the customer order ref since this does not happen when running the two frameworks on separate machines.



Suggestions: if the common hostname is the cause then extend the hostname with python PID (poss problems with multi proc) or an instance specific framework uuid property (logging does a short uuid for example) ?

---

## 2022-04-13 09:16:32 - random channel

**Nacho Uve**

Solved.

It looks that `plotly` was not properly installed. After reinstall and restart jupyter notebook it works.

---

## 2022-04-08 13:59:47 - general channel

**liam**

Just pushed a [https://github.com/betcode-org/flumine/pull/577|branch](https://github.com/betcode-org/flumine/pull/577|branch) to flumine which integrates [@UUX1L88MC](@UUX1L88MC) awesome [https://github.com/tarb/betfair_data|betfair-data](https://github.com/tarb/betfair_data|betfair-data) library, I am seeing a rough 1.5-2x speed increase with no code changes other than the price/size change (now bflw objects)



Few things to cleanup and fairly sure it can be sped up more, going forward I want to see how this can be the default for bflw and fall back to pure python if the library isn't installed but welcome any thoughts on this.

---

## 2022-04-04 15:13:53 - issues channel

**Jon K**

Sorry, new to this and not used Python much before.

Thanks for the help

---

## 2022-03-28 19:54:35 - general channel

**VT**

[@UUX1L88MC](@UUX1L88MC) BF AUS articles are well explained, detailed, it is of great help for beginner programmers. I've added it to my study list. Thank you.

---

## 2022-03-24 13:26:05 - betconnect channel

**liam**

[@ULDAVFDRP](@ULDAVFDRP) has kindly transferred his [https://github.com/betcode-org/betconnect|betconnect API python](https://github.com/betcode-org/betconnect|betconnect API python) wrapper to betcode and can now be installed via pypi :grin:



`pip install betconnect`

---

## 2022-03-17 11:54:21 - general channel

**anomaly**

Hmm I think i've gotten myself in a tangle because of the way the modelling has been done. I'm currently using bflw to manage and then spawn a model that makes a selection. Given that selection, I want to place a bet.

Each model communicates through a queue to the main thread which I originally planned to have place the bets through bflw... but now it appears flumine is much better suited for this purpose.

In summary, the current setup is: bflw process loop (monitor market stream) -&gt; spawn models according to some trigger logic and each model makes a single prediction -&gt; send the (market_id, selection_id, order_type, stake) through the queue -&gt; bflw process reads the queue and places bet -&gt; bflw closes and cleans up the model process

Given what you said and having another look at the code it seems I need to instead encode the model spawning logic _inside_ the BaseStrategy (process_market_book, check_market_book etc). Is this correct?

---

## 2022-03-16 18:30:44 - general channel

**NOT Damien**

hello [!everyone](!everyone) i am new to betfairlightweight have been looking for documention but have had no luck online does anybody have a link or file that i can get my hands on thanks in advance

---

## 2022-03-16 09:32:38 - general channel

**anomaly**

Can do! So essentially a typical situation is this:



1. you have a strategy name. say it's called "back_strat_42". it's betting on UK horseracing.

2. you have a single market_id and a single selection_id that you want to place a bet on

3. you have the liability to stake (back or lay doesn't matter).

4. you want to place just a single bet on the selection at anytime and leave it in the market. so for simplicity say a OrderType=MARKET_ON_CLOSE with PersistenceType=MARKET_ON_CLOSE

5. you want a log/trace of the result of the bet that you placed for post-race analysis (typically with a database dump)



This is to be repeated multiple times from a few different strategies but the logic is essentially as above and the current system design is to place these bets from individual threads or processes.

A follow up question is if you have dozens of these happening in parallel will it be an issue from a betfair api perspective? I'm connecting with a live api key with bot login (certs) and it seems you're only allowed 9 connections. Would this be an issue with the above setup?

---

## 2022-03-14 14:06:18 - random channel

**D C**

OK cheers Mo. I guess I will stick with R. I've been getting a bit fed up with my setup as I have various bits and pieces in JS/C++/Python and was hoping to get a more uniform setup together. Was hoping that I would easily be able to just switch from R to Python but I guess not.

---

## 2022-03-14 14:00:38 - random channel

**D C**

I've been starting to use Python to perform logistic regression but struggling to find a way to model interaction effects. In R this is easy. I've tried sklearn and statsmodels but so far can't see an easy way to do this as both make use of the dataframe columns you provide. I am brand new to this in a python setting so may have missed something obvious but is there a simple way to do this or am I better off (from speed point of view) sticking with R ?

---

## 2022-03-05 10:23:22 - issues channel

**Ruben**

yes, what I do to look at data in a columnar way is use jupyter notebooks (is installed automatically if you install the python anaconda environment). With that you can directly read a csv with pandas, and then look at as many rows of the dataframe you want

---

## 2022-03-04 10:47:03 - strategies channel

**liam**

the flumine catalogue worker uses the marketBook updates to trigger a new request, this is dependant on how you have flumine setup but if you stop getting streaming updates like you have then you wouldn't get catalogue updates

---

## 2022-03-03 09:13:55 - general channel

**J**

That's good to know, thanks. I'm fairly new to this so I'm probably doing it wrong, but I switched to a non streaming filter to use the start date but no cigar. I'm trying to find a list of venues or something to further restrict the list (I essentially just want all 'win' type 7 (horse racing) races for Australia for today but the venue list is also hard to find. Not sure if there's a better way.

---

## 2022-02-28 20:09:14 - issues channel

**Mo**

Is your app key old? Is this your first time using streaming?

---

## 2022-02-28 20:07:46 - issues channel

**William**

```   # setup logging

    logging.basicConfig(level=[http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))  # change to DEBUG to see log all updat



    # create trading instance

    trading = betfairlightweight.APIClient(user, password, app_key=appKey, certs='/certs')



    # login

    trading.login_interactive()

    # create queue

    output_queue = queue.Queue()



    # create stream listener

    listener = betfairlightweight.StreamListener(

        output_queue=output_queue

        # lightweight=True

    )

    # create stream

    stream = trading.streaming.create_stream(

        host="race",

        listener=listener

    )

    # create filters (GB WIN racing)



    market_filter = streaming_market_filter(

        # event_type_ids=['7'],

        # country_codes=['AU'],

        # market_types=['WIN'],

        market_ids=market_id

    )

    market_data_filter = streaming_market_data_filter(

        # fields=['EX_LTP', "EX_ALL_OFFERS", 'EX_MARKET_DEF', 'EX_TRADED_VOL', 'EX_TRADED'],

        # fields=['EX_ALL_OFFERS', 'EX_MARKET_DEF'],

        # ladder_levels=9,

    )

    # subscribe

    streaming_unique_id = stream.subscribe_to_markets(

        market_filter=market_filter,

        market_data_filter=market_data_filter,

        conflate_ms=100,  # send update every 1000ms

    )

    stream.start()

    return trading, output_queue, listener```

---

## 2022-02-28 11:52:06 - general channel

**Tony**

Hi all :wave:, i am new to the channel. I am going to try create a  tennis trading bot as i already trade it daily but would like to try automate certain scenarios. I have a delayed API key but from reading around it doesn’t feel like it would allow me to get an accurate picture and also i would like to stream some data for backtest purposes but the betfair free files don’t seem to have what i would like either. What is the best place way to get the live key activated?

---

## 2022-02-23 07:41:49 - random channel

**D C**

I have a similar function in my setup so I can turn off the bet placement tap if it gets hit so I can have a max loss per market to save the bankroll

---

## 2022-02-19 10:37:41 - general channel

**Mo**

```import logging

import queue

import threading



import betfairlightweight



# setup logging

logging.basicConfig(level=[http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))  # change to DEBUG to see log all updates



# create trading instance (app key must be activated for cricket stream)

trading = betfairlightweight.APIClient("username", "password", app_key="appKey")



# login

trading.login()



# create queue

output_queue = queue.Queue()



# create stream listener

listener = betfairlightweight.StreamListener(output_queue=output_queue)



# create stream

stream = trading.streaming.create_stream(listener=listener, host="sports_data")



# start stream in a new thread (in production would need err handling)

t = threading.Thread(target=stream.start, daemon=True)

t.start()



# subscribe

streaming_unique_id = stream.subscribe_to_cricket_matches()



# check for updates in output queue

while True:

    updates = output_queue.get()

    for update in updates:

        print(update.json())```

---

## 2022-02-19 08:39:37 - general channel

**rob smith**

Does anyone know of any examples of how to get the new cricket scores? I'm new to python and am struggling. Cheers

---

## 2022-02-17 05:43:47 - general channel

**Mo**

[@UUX1L88MC](@UUX1L88MC) - rust beginner question, I am trying to build the package from source. I have cloned it and am running `maturin develop` and get this error:



```💥 maturin failed

  Caused by: Cargo metadata failed. Does your crate compile with `cargo build`?

  Caused by: `cargo metadata` exited with an error: error: failed to parse manifest at `xxx`



Caused by:

  feature `edition2021` is required



  consider adding `cargo-features = ["edition2021"]` to the manifest```

---

## 2022-02-14 12:01:06 - general channel

**Mo**

CSVs are the first step, I'm aiming to build these into an sqlite database with a Python wrapper so you could do something along the lines of



```from betfairmappings import betfair_selection_id_to_runner_name_map



betfair_selection_id_to_runner_name_map.get(42791012)```

In the ultimate solution described above, `betfairutil` will import `betfairmappings` (if it is installed, will be a big package so definitely don't want it to be a required dependency) then use it to add runner names to self recorded data completely automatically

---

## 2022-02-08 20:40:41 - general channel

**liam**

Certainly recommend streaming, much lighter on CPU and reduces the complication. 



What issues are you seeing the historical data? Thought the pro stuff was good.



flumine can do whatever you want, the selling point is the switch to backtest / paper / live with no changes to your code.  Switching wouldn’t make sense depending on how advanced your current setup is and/or you want some of the features. 

---

## 2022-02-06 10:23:31 - issues channel

**Peter**

Very basic:



```import os

import logging

import queue

import threading



import betfairlightweight



# setup logging

# logging.basicConfig(level=logging.DEBUG)  # change to DEBUG to see log all updates

logging.basicConfig(

    level=logging.DEBUG,

    filename='tpd/race-subscription.log',

    filemode="a",

    format='%(asctime)s - %(levelname)s - %(message)s',

)



# create trading instance (app key must be activated for streaming)

workspace_prefix = os.getenv("WORKSPACE_PREFIX")

trading = betfairlightweight.APIClient(os.getenv("BETFAIR_USERNAME"), os.getenv("BETFAIR_PASSWORD"), app_key=os.getenv("BETFAIR_LIVE_KEY"), certs=workspace_prefix + "certs")



# login

trading.login()



# create queue

output_queue = queue.Queue()



# create stream listener

listener = betfairlightweight.StreamListener(output_queue=output_queue)



# create stream

stream = trading.streaming.create_stream(listener=listener)



# subscribe

streaming_unique_id = stream.subscribe_to_races()



# start stream in a new thread (in production would need err handling)

t = threading.Thread(target=stream.start, daemon=True)

t.start()



# check for updates in output queue

while True:

    update = output_queue.get()

    print(update)```

---

## 2022-02-06 10:17:59 - issues channel

**Peter**

Yes first time. Is the json library determined when I install Flumine?

---

## 2022-02-03 20:43:01 - general channel

**ShaunW**

I dunno [@U8ZGPN5H9](@U8ZGPN5H9), I think if people have got a tenner to spend they'll spend it whatever the minimum is.  And for new people considering automation then £1 might be less daunting if they're new to letting things run all day.  Possibly also a small nod to the authorities too that they're trying to consider the cost/impact of gambling? Can't change it anyway and vs real problems it doesn't seem too bad.

---

## 2022-02-02 10:27:02 - random channel

**Mo**

[@U4H19D1D2](@U4H19D1D2) yeah was fixed 2 versions ago in betfairutil so must have been a stale install that was fixed when restarting his IDE

---

## 2022-02-02 09:11:34 - random channel

**Peter C**

Hi [@UBS7QANF3](@UBS7QANF3), I'm having a play with this this morning, but I'm having problems loading my self recorded data. I get the following error, please would you help me debug? I get the same error importing various files with a variety of the betfairutil functions. I installed betfairutil/viz as above



```~\anaconda3\lib\site-packages\betfairutil\__init__.py in read_prices_file(path_to_prices_file, lightweight)

    792     stream = trading.streaming.create_historical_generator_stream(

    793         file_path=path_to_prices_file,

--&gt; 794         listener=StreamListener(

    795             max_latency=None, lightweight=lightweight, debug=False, update_clk=False

    796         ),



TypeError: __init__() got an unexpected keyword argument 'debug'```

---

## 2022-02-01 13:50:42 - general channel

**liam**

Got some errors when trying to install from PyPi, expected?



```  error: could not compile `bzip2-rs` due to 5 previous errors

  warning: build failed, waiting for other jobs to finish...

  error: build failed

  💥 maturin failed

    Caused by: Failed to build a native library through cargo

    Caused by: Cargo build finished with "exit status: 101": `cargo rustc --message-format json --manifest-path Cargo.toml --release --lib -- -C link-arg=-undefined -C link-arg=dynamic_lookup -C link-args=-Wl,-install_name,@rpath/betfair_data.cpython-39-darwin.so`

  🔗 Found pyo3 bindings

  🐍 Found CPython 3.9 at /Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9

  error[E0432]: unresolved import `std::io::ReadBuf`

   --&gt; /Users/liampauling/.cargo/git/checkouts/bzip2-rs-5185c758a5d48e65/748b36f/src/decoder/parallel/reader.rs:2:5

    |

  2 | use std::io::ReadBuf;

    |     ^^^^^^^^^^^^^^^^ no `ReadBuf` in `io`





  error[E0432]: unresolved import `std::io::ReadBuf`

   --&gt; /Users/liampauling/.cargo/git/checkouts/bzip2-rs-5185c758a5d48e65/748b36f/src/decoder/reader.rs:2:5

    |

  2 | use std::io::ReadBuf;

    |     ^^^^^^^^^^^^^^^^ no `ReadBuf` in `io`





  error[E0599]: no method named `read_buf` found for type parameter `R` in the current scope

     --&gt; /Users/liampauling/.cargo/git/checkouts/bzip2-rs-5185c758a5d48e65/748b36f/src/decoder/parallel/reader.rs:110:37

      |

  110 |                         self.reader.read_buf(&amp;mut read_buf)?;

      |                                     ^^^^^^^^ method not found in `R`





  error[E0599]: no method named `read_buf` found for type parameter `R` in the current scope

    --&gt; /Users/liampauling/.cargo/git/checkouts/bzip2-rs-5185c758a5d48e65/748b36f/src/decoder/reader.rs:68:37

     |

  68 |                         self.reader.read_buf(&amp;mut read_buf)?;

     |                                     ^^^^^^^^ method not found in `R`





  error: aborting due to 4 previous errors





  Some errors have detailed explanations: E0432, E0599.



  For more information about an error, try `rustc --explain E0432`.



  Error: command ['maturin', 'pep517', 'build-wheel', '-i', '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9'] returned non-zero exit status 1

  ----------------------------------------

  ERROR: Failed building wheel for betfair-data

Failed to build betfair-data

ERROR: Could not build wheels for betfair-data which use PEP 517 and cannot be installed directly

WARNING: You are using pip version 20.3.1; however, version 22.0.2 is available.

You should consider upgrading via the '/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9 -m pip install --upgrade pip' command.```

---

## 2022-02-01 12:31:27 - random channel

**Unknown**

Hey guys, here's something I'm working on for the next release of betfairviz: defining "points of interest" to use with the dashboard



These points of interest could be market related - in this example I've defined them as any matching cycle where at least £10k was matched - or they could be exogenous like goals/cards/corners in football. They let you quickly navigate the market through time and explore the market dynamics around these points



Next step is to display these points of interest on the book percentage graph with flexible styling chosen by the user



Code for the example is:



```import pandas as pd



import betfairutil

import betfairviz



market_books = betfairutil.read_prices_file('../betfair-hackathon-2021/1.176457983.bz2')



volumes_traded = pd.Series(betfairutil.calculate_total_matched(mb) for mb in market_books).diff()



points_of_interest = [

    betfairviz.PointOfInterest(

        text=f"£{round(volumes_traded[i], 2)} matched at {betfairutil.publish_time_to_datetime(market_books[i]['publishTime'])}",

        timestamp=betfairutil.publish_time_to_datetime(market_books[i]['publishTime']))

    for i in volumes_traded.index[volumes_traded &gt; 10000]

]



betfairviz.create_dashboard(market_books, points_of_interest=points_of_interest)```

It requires the latest (0.1.1) version of betfairutil, installable from GitHub a la



```pip install git+[https://github.com/mberk/betfairutil.git@master#egg=betfairutil[files]](https://github.com/mberk/betfairutil.git@master#egg=betfairutil[files])```

and the points-of-interest branch of betfairviz:



```pip install git+[https://github.com/mberk/betfairviz.git@points-of-interest#egg=betfairviz](https://github.com/mberk/betfairviz.git@points-of-interest#egg=betfairviz)```



---

## 2022-01-31 13:00:47 - general channel

**liam**

Is this rust or python? My understanding is that to make rust bindings you need to have a pretty good knowledge of cpython? Is the code open source?



Regarding your example you would need to set `lightweight=True` and `update_clk=False` on the listener for a fairer comparison. Ideally the `[speed]` install is used as well, see [https://liampauling.github.io/betfair/advanced/#performance|here](https://liampauling.github.io/betfair/advanced/#performance|here) for the performance docs

---

## 2022-01-30 16:01:40 - random channel

**river_shah**

I really think `flumine` is a fantastic name (a play on streams and evocative of steampunk) and we already have a community around it who understand that it is an integrated quant betting system. Sorry to repeat but my strong vote would be to promote `flumine` as the org name / all other packages / repos under this umbrella.



Users can still pick and choose sub packages or install the whole of `flumine` and get all the `flumine` eco-system dependencies sorted for them.

---

## 2022-01-29 09:32:53 - random channel

**Dave**

Personally I think the name should be semantic and not try to be some flashy brand. bflw did achieve that the first time round. Wannabe sport bettors and retail traders in finance love the flashy crap like "NinjaTrader" etc. I think we are all here to take a systematic and scientific approach to capitalise on market in efficiencies, and the name should reflect that. Flumine is nice as it relates to flow of liquid(ity) and I think we all appreciate the link to markets there. PyBet IMO is too generic. Something related to quantitative/systematic/non-discretionary betting would be good. Some of the flashy "brand names" here would put me off tbh, and also cater a lot to the same audience from whom you make your money off.

---

## 2022-01-25 17:31:29 - strategies channel

**foxwood**

ok fixed that safely. strategy prints out immediate info from process_closed_market for markets still on BF but closed so getting there. Actually made some bets but I'd changed stake to £1 so not taken but no error message in log - maybe it doesn't - no probs. However, nothing in log except high latency messages for {MarketStream: 2201] with typical time of 0.84 - no flumine setup messages / bet errors / markets or anything like that - not sure what to expect lol. What section of processing / transmission is the latency referring to ?

---

## 2022-01-23 23:11:43 - strategies channel

**foxwood**

I want to shift a backtest strategy to live - my first live flumine play. The strategy is based on the DataCollectWOM strategy example at [https://github.com/liampauling/flumine-strategy-development/blob/master/main.py](https://github.com/liampauling/flumine-strategy-development/blob/master/main.py)



Obvious things I need to do is change the wrapper to use live client login, remove mock_patch and provide a bflw streaming market filter.



There are 2 possible gotchas in my strategy where I'm not sure if things exist in live ie will it crash if these references are left in:

a) market_catalogue is used to get the runner name - is this just a backtest feature and should this middleware be removed if a catalogue is constructed during live streaming ?

b) in function process_closed_market the field "order.simulated.profit" is printed and logged - will that field exist or will this crash things if the reference is left in ?



Any advice or thoughts about other things I might not think of first time more than welcome

---

## 2022-01-23 10:00:53 - random channel

**Jorge**

Thanks, I created a Disk and RAM alarms with CloudWatch following this tutorial: [https://kumargaurav1247.medium.com/aws-cloudwatch-agent-installation-for-memory-metric-integrate-with-grafana-365404154](https://kumargaurav1247.medium.com/aws-cloudwatch-agent-installation-for-memory-metric-integrate-with-grafana-365404154)

---

## 2022-01-18 19:54:32 - strategies channel

**foxwood**

I have built a strategy using "datacollectwom.py" as a template. In that example it adds a new dictionary variable named "data" to market.context the first time any new market is passed to check_market_book. I've copied that approach for a strategy that watches market movements and prices and bets when appropriate. That's testing out reasonably so far with history files but I've hit some questions / doubts ...



1) is there a special reason for using market.context for the "data" variable or could I do something safely at a higher level without interfering with bflw/flumine eg market.mydatavar = {} ?

2) is it common / naughty in Python to add a variable dynamically like that ?

3) if the "enhanced" market object is deleted then any data in that variable would be lost. In bflw or flumine is there a case of a market object being deleted and recreated from scratch ie some sort of mcm case where the approach is to discard what was held and rebuild the market object from scratch ?

4) the main.py for the datacollectwom is processing history files - would the same structure /code for a strategy (less mock_patch) work with live streaming data ie would it just be simply a change of input source for the json ?



Sorry if some of these questions seem basic but trying to fill in some of my python and flumine gaps

---

## 2022-01-12 21:47:57 - general channel

**Dario Scardina**

Hi everyone, I'm wondering to setup a python script that everyday update me (i.e. by email) about my account fund stats.

I mean something like that:

• last week: +13.20€ 

• last month: -2.13€

• ...

So I need a way to extract my account balance in a specific moment of the day (for example at 23:59:59 of seven days ago, a month ago, ...)



How I can get this info? Do you have some suggestions? I'm trying get_account_statement method but I have some issues with that (and anyway I need to parse the result eventually to find out what I want).

---

## 2022-01-09 17:25:18 - general channel

**S G**

Hi All, I have got a market recorder setup with log rotation set to 1 day. However the logs arent written until midnight, this could be due to no activity or no info logs. Can I tell fulmine to write a log message every minute? something like a heart beat?

---

## 2022-01-08 15:44:09 - issues channel

**river_shah**

Just got a call from betfair, nothing new to add except they are working on fixing for Monday. Payment options will come back automatically (i.e they have not been deleted)

---

## 2022-01-08 08:42:51 - strategies channel

**birchy**

[@U4H19D1D2](@U4H19D1D2) I'm a bit confused.... The reason I changed the customer_strategy_ref was because I have one deployment server which runs 2 independent frameworks (one per betfair account), each of which has 1+ independent strategies. Obviously they're all on the same hostname, so all of the orders had the same reference which was a PITA. So what's best practice for this kind of setup?

---

## 2022-01-05 01:05:07 - random channel

**Paul**

Indeed first time [@U4H19D1D2](@U4H19D1D2) - dropped them a note to ask for more detailed info as it's not actually obvious how that happened. Frustrating, but sometimes learning how to buy money can be expensive :shrug: 

---

## 2021-12-28 18:03:06 - general channel

**Shashi Khaya**

Thanks all for your input! I am still very new to the idea of sports trading and just have a few ideas that I thought could work - What is the reason for never greening?! And [@U4H19D1D2](@U4H19D1D2) where you say - we only take value - what do you mean by that? Sorry for all the questions but this seems like such a great thing to get involved in and I am eager to learn!

---

## 2021-12-28 15:41:06 - general channel

**VT**

I've been asking about the subject out there, some recommended changing the language to C but I discarded it, I intend to do my studies in Python, I'm a beginner.



Others have suggested Cython, Cpython or Pypy, I'm still studying about that. My application is simple, just send orders and close the matched orders and speed is the most important.

---

## 2021-12-22 19:58:06 - issues channel

**Paul**

So now i'm confused. I have a live key. I've placed bets with it using BFLW but without streaming. First time I've used streaming - is there a further activation step for streaming?

---

## 2021-12-21 14:03:35 - general channel

**Peter**

If you install [https://github.com/jupyterlab/jupyterlab-desktop|Jupyter Desktop](https://github.com/jupyterlab/jupyterlab-desktop|Jupyter Desktop) it will create a whole working environment for you, including Pandas and its dependancies.

---

## 2021-12-21 12:27:55 - general channel

**Techno**

And, is Jupyter classic notebook the best one to use? I only have Python installed.

---

## 2021-12-21 08:42:11 - issues channel

**Unknown**

Hi all, I am new to Flumine and am backtesting a strategy using betfair pro data. I have followed the examples and started running backtests but have noticed an issue with simulated profit. Removed runners are returning a simulated profit (please refer to output image below)(Note: this is a backing strategy, it seems odd that the simulation would see a removed runner as winner). Would be greatly appreciated if someone could point out what I’m doing wrong.

---

## 2021-12-17 21:24:12 - issues channel

**Bradley**

Good evening. I is new to this and am is having issue with running this most excellent code. Please could you suggest what I should do to make this function?



`Traceback (most recent call last):`

  `File "/home/xxxx/PycharmProjects/flumine_client/venv/lib/python3.8/site-packages/flumine/streams/marketstream.py", line 44, in run`

    `self._stream.start()`

  `File "/home/xxxx/PycharmProjects/flumine_client/venv/lib/python3.8/site-packages/betfairlightweight/streaming/betfairstream.py", line 60, in start`

    `self._read_loop()`

  `File "/home/xxxx/PycharmProjects/flumine_client/venv/lib/python3.8/site-packages/betfairlightweight/streaming/betfairstream.py", line 207, in _read_loop`

    `received_data_raw = self._receive_all()`

  `File "/home/xxxx/PycharmProjects/flumine_client/venv/lib/python3.8/site-packages/betfairlightweight/streaming/betfairstream.py", line 229, in _receive_all`

    `raise SocketError("[Connect: %s]: Socket %s" % (self._unique_id, e))`

`betfairlightweight.exceptions.SocketError: [Connect: 2009]: Socket The read operation timed out`

---

## 2021-12-16 08:26:10 - general channel

**Paul**

On another point last night I broke my remote code-server setup I used to write bot code on my iPad. Gave AWS Cloud9 (a cloud native IDE), a go, and was pleasantly surprised by it. Think over Christmas I can see myself getting a setup where I use sagemaker for jupyter, and cloud9 for coding. But then, I'm on the Kool Aid, so…

---

## 2021-12-15 18:13:01 - issues channel

**birchy**

Interestingly, I use `.aws/credentials` and also `.betfair/credentials`, which is something I setup when I first started using Flumine ~12 months ago. I've never used the environment variables for username, password, etc. Just wondering how you guys normally SET these values? I know it can be done from the terminal but am wondering if you're automating it or entering manually?

---

## 2021-12-15 08:58:12 - general channel

**liam**

I have experimented with a few things on AWS lambda/spot instances/fargate/ecs and they all work well but there is always the upfront time cost in getting them setup and without a sophisticated framework on top it isn't exactly simple to quickly run something.



I agree with [@UBS7QANF3](@UBS7QANF3) as since purchasing a decent laptop (M1) the amount of backtests I carry out has skyrocketed as I can just press f5 and forgot about it

---

## 2021-12-14 10:38:28 - general channel

**Oliver Varney**

I think your fine on the install as its likely that you would of got an import error. As liam mentioned it probably just ran the code and exited but as it was doing nothing, nothing happened.

---

## 2021-12-14 10:28:07 - general channel

**Techno**

Hi guys. I'm Elliot. Thanks for having me. To be honest, I'm very green when it comes to programming and I'm having trouble installing Betfairlightweight. I want to use it to parse the historical data, and have a spreadsheet or even a graph if possible of all the traded prices for horses until the start of the race. Thanks.

---

## 2021-12-12 13:42:09 - random channel

**Mo**

Thanks for sharing, this was great. First time listening to this podcast. I like the format where the host is providing commentary interleaved with the guests' answers.



My top take aways:



1. There was an interesting discussion about Betfair's price ladder and how it proved an advantage over Flutter in the early days which is highly relevant to a question I posed in the Betfair AMA ([https://betfairlightweight.slack.com/archives/C02J4CBA0H5/p1635194249356600](https://betfairlightweight.slack.com/archives/C02J4CBA0H5/p1635194249356600))

2. The host mentioned the importance of being bored for coming up with creative ideas. I tend to do my best to avoid being bored but maybe this is something to try

---

## 2021-12-12 00:42:04 - general channel

**Martin Chambers**

[@U016TGY3676](@U016TGY3676) OK, thanks for that Birchy.  Having some success, but looks like I need to have certs installed (was trying to do it without it to get rolling.  The error message is: Exception: [WinError 3] The system cannot find the path specified: '/certs/'

---

## 2021-12-11 20:36:58 - random channel

**Mo**

Recommend Ubuntu. Should come with Python, Git etc already installed. 

---

## 2021-12-11 20:00:16 - random channel

**Beeblebrox**

[@U016TGY3676](@U016TGY3676) I had something similar today, in my case it was because I was maxing out the cpu.  It had been fine for months, but I started running an extra flumine instance with a new strategy a couple of days ago and it couldn't cope.



My Lightsail instance was Windows (yes, yes I know! I just used that as I'm more used to Windows), but I'm going to try setting up some Unix EC2 instances instead.  As a novice Unix user has anyone got a guide on things like which flavour of Unix to use, which instance types to use (I'm thinking t3.micro), how to install Python, Git, etc, and any other tips?  I'm sure I can work it out myself, but any guidance would be appreciated.

---

## 2021-12-11 14:37:52 - random channel

**birchy**

Must confess that I'm not an Apple fan either (unless used for making cider, which I used to do, but that's a whole different story), but am tempted to treat myself to an M1. But at ~£1K, I can't help wondering if a Dell XPS or something else with an i7 cpu would offer better VFM. Obviously I'd be installing Linux rather than Windows.

---

## 2021-12-11 05:21:26 - general channel

**Martin Chambers**

Hi all. First post here. Just getting started and have plenty to learn. Have read the docs at betfairlightweight and flumine. Just after some guidance on a work flow here to create a simple bot/strategy to start with. Login through betfairlightweight and then create a strategy with flumine? I have the been able to log into my account, get the market list etc so far.

---

## 2021-12-07 09:28:30 - strategies channel

**C0rnyFlak3s**

haha ^^ I don’t say I am fully convinced by this idea myself, and I am well aware, that this is the most basic and beginner friendly strategy that will be praised by those ebook salesman as you call them. However I think, most of them do not really analyze the parameters around the games with it. But yeah I may try to come up with something the next days, and see how it fairs :stuck_out_tongue:

---

## 2021-12-07 07:46:25 - general channel

**river_shah**

Haha, I have recently been working with `Julia` on a project so I do have a soft spot for people new to python wanting to get “compiled” language speeds

---

## 2021-12-03 07:06:07 - general channel

**captainonionhead**

I've only recently got going and have 2 python processes (one recorder, one simple strategy to keep Betfair happy whilst I gather some data).  These are running on a VPS I already had that I've repurposed.  It's roughly equivalent to a nano and I'm nowhere near stressing it.

However, I'm expecting to move to something more like Peter's setup with many processes on different instances at least partly because it allows me to update different parts of my code/infrastructure without having to take everything down.  At the moment I have a lot of code churn as I implement new features and I expect that to continue as I develop strategies and refine ones that are already running.

---

## 2021-11-26 17:13:29 - issues channel

**birchy**

Weird, something must be different on the AWS setup. Probably something simple like a slightly different directory structure. Can you ping the API server from AWS? Or even load the website with `wget`?

---

## 2021-11-20 23:12:33 - issues channel

**John**

Hi folks, I am new to this forum. I have an issue very similary to the *[https://app.slack.com/team/U02KWHK2H89|C0rnyFlak3s](https://app.slack.com/team/U02KWHK2H89|C0rnyFlak3s)* one.  However, I use the betfairlightweight library and the code from the examples.  Here is the code snippet and the error I get:

---

## 2021-11-20 12:35:43 - general channel

**Mo**

Decent book for beginners though: [https://www.amazon.co.uk/Statistical-Sports-Models-Excel-Andrew-ebook](https://www.amazon.co.uk/Statistical-Sports-Models-Excel-Andrew-ebook)

---

## 2021-11-20 12:34:21 - general channel

**S G**

I am new to modelling and strategies and was wondering if anyone can suggest a good book to kick start creating a working sport model.Any thoughts on the below book? More focussed on stocks etc but i guess priciples can be applied to sports. 

[https://www.amazon.co.uk/Machine-Learning-Algorithmic-Trading-alternative/dp/1839217715/ref=asc_df_1839217715/?tag=googshopuk-21&amp;linkCode=df0&amp;hvadid=430825732529&amp;hvpos=&amp;hvnetw=g&amp;hvrand=15520940606181387990&amp;hvpone=&amp;hvptwo=&amp;hvqmt=&amp;hvdev=m&amp;hvdvcmdl=&amp;hvlocint=&amp;hvlocphy=9045936&amp;hvtargid=pla-1123856727832&amp;psc=1&amp;th=1&amp;psc=1&amp;tag=&amp;ref=&amp;adgrpid=101598704058&amp;hvpone=&amp;hvptwo=&amp;hvadid=430825732529&amp;hvpos=&amp;hvnetw=g&amp;hvrand=15520940606181387990&amp;hvqmt=&amp;hvdev=m&amp;hvdvcmdl=&amp;hvlocint=&amp;hvlocphy=9045936&amp;hvtargid=pla-1123856727832|https://www.amazon.co.uk/Machine-Learning-Algorithmic-Trading-alternative/dp/1839217715/ref=asc_df_1839217715/?tag=googshopuk-21&amp;linkCode=df0&amp;hvadid=430825732529&amp;hvpos=&amp;hvnetw=g&amp;hvrand=15520940606181387990&amp;hvpone=&amp;hvptwo=&amp;hvqmt=&amp;hvdev=m&amp;hvdvcmdl=&amp;hvlocint=&amp;hvlocphy=9045936&amp;hvtargid=pla-1123856727832&amp;psc=1&amp;th=1&amp;psc=1&amp;tag=&amp;ref=&amp;adgrpid=101598704058&amp;hvpone=&amp;hvptwo=&amp;hvadid=430825732529&amp;hvpos=&amp;hvnetw=g&amp;hvrand=15520940606181387990&amp;hvqmt=&amp;hvdev=m&amp;hvdvcmdl=&amp;hvlocint=&amp;hvlocphy=9045936&amp;hvtargid=pla-1123856727832](https://www.amazon.co.uk/Machine-Learning-Algorithmic-Trading-alternative/dp/1839217715/ref=asc_df_1839217715/?tag=googshopuk-21&amp;linkCode=df0&amp;hvadid=430825732529&amp;hvpos=&amp;hvnetw=g&amp;hvrand=15520940606181387990&amp;hvpone=&amp;hvptwo=&amp;hvqmt=&amp;hvdev=m&amp;hvdvcmdl=&amp;hvlocint=&amp;hvlocphy=9045936&amp;hvtargid=pla-1123856727832&amp;psc=1&amp;th=1&amp;psc=1&amp;tag=&amp;ref=&amp;adgrpid=101598704058&amp;hvpone=&amp;hvptwo=&amp;hvadid=430825732529&amp;hvpos=&amp;hvnetw=g&amp;hvrand=15520940606181387990&amp;hvqmt=&amp;hvdev=m&amp;hvdvcmdl=&amp;hvlocint=&amp;hvlocphy=9045936&amp;hvtargid=pla-1123856727832|https://www.amazon.co.uk/Machine-Learning-Algorithmic-Trading-alternative/dp/1839217715/ref=asc_df_1839217715/?tag=googshopuk-21&amp;linkCode=df0&amp;hvadid=430825732529&amp;hvpos=&amp;hvnetw=g&amp;hvrand=15520940606181387990&amp;hvpone=&amp;hvptwo=&amp;hvqmt=&amp;hvdev=m&amp;hvdvcmdl=&amp;hvlocint=&amp;hvlocphy=9045936&amp;hvtargid=pla-1123856727832&amp;psc=1&amp;th=1&amp;psc=1&amp;tag=&amp;ref=&amp;adgrpid=101598704058&amp;hvpone=&amp;hvptwo=&amp;hvadid=430825732529&amp;hvpos=&amp;hvnetw=g&amp;hvrand=15520940606181387990&amp;hvqmt=&amp;hvdev=m&amp;hvdvcmdl=&amp;hvlocint=&amp;hvlocphy=9045936&amp;hvtargid=pla-1123856727832)

---

## 2021-11-16 08:05:42 - general channel

**liam**

A tutorial start to finish is certainly on my todo list however there would be the assumption of having an intermediate knowledge of python when it comes to classes/inheritance/design patterns etc.



But because its a framework once you have things figured it can be a few lines of code to setup a variation of your strategy or quickly backtest/paper trade something new. When time is at a premium this can be extremely valuable for anyone starting out.

---

## 2021-11-16 07:00:07 - general channel

**Paul**

If you want a bit more confidence as a programmer, loads of python beginner books out there, the CS50 course gives a lot of people a solid foundation, loads of options.

---

## 2021-11-16 06:25:34 - general channel

**ThomasJ**

Oh I am a beginner Pythonista and seeing how the code is designed, constructed, executed etc has taken me to a whole different level of Python understanding.

---

## 2021-11-11 11:00:43 - issues channel

**captainonionhead**

It's a fresh install a few days ago in a newly built VPS whilst I work out how to get AWS up and running so I thought I was up-to-date with everything.

---

## 2021-11-11 10:15:00 - issues channel

**captainonionhead**

Morning, I have a market recorder based upon the flumine example.  It keeps receiving `INVALID_SESSION_INFORMATION` errors from the market-catalogue polling thread after it has been running for a while.

Is this expected - do I simply need to catch the exception and login again or is there something more fundamentally wrong with my setup?

Thanks!

---

## 2021-11-11 09:38:16 - general channel

**ThomasJ**

That's an amazing offer Liam and I thank you for it (no... I'm blown away actually)

The weight mainly consists of me storing price history, avail history,  and such and then doing calculation on them every .X of a second.



I set strategy.context to various values to control what I need and I can see exactly what hurts.



I store the accumulated stuff in market.context  whose code is called from  cache.py &gt; _def_ update_cache



I have zero secret sauce unfortunately, but many many lines of code, and countless hours. Ah the common cry of the beginner. :rolling_on_the_floor_laughing: :rolling_on_the_floor_laughing: :rolling_on_the_floor_laughing:

---

## 2021-11-10 15:39:58 - general channel

**Newbie99**

For what you're trying to do, you can either:



1. Use the REST API approach, but make multiple calls (as you are limited with the amount of data you can return per call)

2. Use streaming and setup a filter for football

However, using either approach, there is no 'in-play' filter, you still need to check:



```if market_book.status == 'OPEN':

    if market_book.inplay:

        return True```

At some point.

---

## 2021-11-01 21:45:30 - general channel

**C0rnyFlak3s**

Hello! I am new to this Slack and I really like it so far. I am not sure if this is the right sub channel to ask my question, however here it goes: Which libraries do you guys use for plotting your streaming data? Odds histories, ladder informations ect. Is there any good plotting library out there which offers this functionality?

---

## 2021-10-23 10:47:02 - strategies channel

**Alex Bella**

Hi Everyone, I'm Alex and new to all this.

I know ML, Python and APIs but am a bit lost as to where to start. Any advice or doc for someone trying to get started?

---

## 2021-10-22 10:47:30 - general channel

**Vinny Banks**

Morning guys. New to slack so cut me some if I'm barking up the wrong tree. I am trying to build an auto bet machine using Python. I have created the certs and exported them but keep getting the following error message



APIError: None

Params: None

Exception: HTTPSConnectionPool(host='[http://identitysso-cert.betfair.com|identitysso-cert.betfair.com](http://identitysso-cert.betfair.com|identitysso-cert.betfair.com)', port=443): Max retries exceeded with url: /api/certlogin (Caused by SSLError(SSLError(9, '[SSL] PEM lib (_ssl.c:3991)')))



Also, when I try to upload it to my security area on my betfair account it is saying it's invalid. Is the Cert generation out of date and I'm missing something? Any hints or tips would be appreciated

---

## 2021-10-15 10:35:50 - random channel

**Jack B**

How have people setup their network security when running on AWS? Public/Private subnets, ssh tunnels etc?

---

## 2021-10-05 11:10:05 - general channel

**Oliver Varney**

Ive always just used the flumine default /  non-virtualised filter which would of always resulted in the first if condition returning true. I just wanted to experiment with a few things, so naively its the first time ive given it any serious thought :man-facepalming: Cool yes Ill email Neil and have a go on a quiet market

---

## 2021-09-18 17:36:43 - issues channel

**Aaron Smith**

Also at the same time i tried installing betfairlightweight[speed], which failed at the ciso8601 package, so i only have the orjson one

---

## 2021-09-12 12:05:01 - general channel

**Jeff Waters**

Hi [@U013MLED3V1](@U013MLED3V1). I'm not sure I follow. Surely flumine is a framework (and Betfair Lightweight is a wrapper)? At this stage, I am purely doing back testing, and as I have a (nearly completed) setup that works, using flumine, it makes sense for me to stick with that. Plus, flumine is regularly updated and the support provided via this forum is excellent, so for me it's a no brainer.

---

## 2021-09-11 17:28:57 - random channel

**thambie1**

I got an ERROR_IN_MATCHER error for the first time, other than that, not seeing anything

---

## 2021-09-11 17:28:40 - strategies channel

**birchy**

When needing to change some hard-coded parameters for a "live" strategy, is it best to stop -&gt; change -&gt; restart, or use a more dynamic setup, i.e. have an external settings file which is polled each time a market strategy is initiated?

---

## 2021-09-09 15:24:47 - general channel

**liam**

or



```pip install betfairlightweight[speed] --upgrade```

---

## 2021-09-09 15:24:24 - general channel

**George**

yep ok agreed that this is magic. all makes sense now! so i will just pip install those two and then i don't need to worry about uninstalling bflw etc

---

## 2021-09-09 15:22:50 - general channel

**George**

ah ok. call me a noob but i'm confused at how installing extra packages help speed things up? Because, surely if the code is identical to before, then the packages aren't being imported anyway?

---

## 2021-09-09 15:17:20 - general channel

**George**

wow that's a lot!

i'm only asking because I saw this in the docs:

"By default betfairlightweight will install C and Rust based libraries if your os is either linux or darwin (Mac), due to difficulties in installation Windows users can install them separately:

```$ pip install betfairlightweight[speed]```

"

which made me think that, since I only use Linux and/or Mac, there wasn't any benefit?

---

## 2021-09-09 15:14:45 - general channel

**George**

If I was to remove the betfairlightweight and install the [speed], do you know what would speed up and roughly by how much?

---

## 2021-09-09 14:54:08 - general channel

**George**

If I'm using a Mac or Linux, do I still need to install using

```pip install betfairlightweight[speed]```

or is it enough just to do

```pip install betfairlightweight```

---

## 2021-09-08 12:51:48 - general channel

**D C**

I think someone asked this recently but I can't find it anywhere in any thread. I've just changed from stream subscription using market ID list to a coarser filter. Yesterday it silently failed on me - the silence likely a bug in my logging setup but I suspect that the number of markets in my filter changed as new markets were added (seemed to fail around 6pm UTC). Because my logging failed I am not sure how to catch it so does anyone know what actually happens when this occurs. The socket was not disconnected so I presumably kept getting heartbeats and zero data (no market data files were produced after the "failure" time). Recommended solution was to ask for a bump in the market limit per connection which I will do but just curious as to what actually happens when this occurs as I am basically just making an assumption here.

---

## 2021-09-05 13:04:14 - general channel

**Dave**

This is the kinda thing we debated a while ago...I decided I liked the idea of having one centralised consumer for market data which was broadcasted internally to whatever processes wanted to subscribe to whatever markets. If you didn't want to go the redis route you could go down zmq instead which has less setup overhead (generally found it simpler). Didn't integrate it into flumine though.

---

## 2021-09-02 09:46:39 - strategies channel

**birchy**

[@U01S1VB9X9P](@U01S1VB9X9P) In theory, yes, but match rates, market impact, etc will paint a very different picture in the real world. The MC analysis is just a very basic setup to get a rough idea of how a strategy performs by comparing luck vs skill. Don't over value it.

---

## 2021-08-28 16:31:26 - general channel

**Jono**

how often does the betfair ui refresh? im placing using flumine for the first time and i just got wondering since not all the bets placed and alterations can be observed in the ui due to the speed - at least thats what it seems like so far

---

## 2021-08-22 08:57:11 - strategies channel

**Adrian**

100% and that's something i'm slowly coming to realise as i learn form you guys how you approach it. The whole strategy and execution side of things wasn't something I considered as a beginner

---

## 2021-08-21 12:56:32 - issues channel

**Jeff Waters**

PS Just found a workaround. I've uninstalled flumine, and then reinstalled it in my Conda virtual environment. That seems to have done the trick (touch wood! :smile:).



Cheers

---

## 2021-08-21 12:49:01 - issues channel

**Jeff Waters**

Yes, I did, but the fact that there was a problem with the SSL didn't really give me much of a clue as to how to fix the problem (or indeed if I could fix it). :slightly_smiling_face:



Incidentally, I've tried re-creating the project using Conda as the virtual environment (as per [https://intellij-support.jetbrains.com/hc/en-us/community/posts/360003511399-SSL-module-not-available-unable-to-install-packages?page=1#community_comment_360001528719|https://intellij-support.jetbrains.com/hc/en-us/community/posts/360003511399-SSL-module-not-available-unable-to-install-packages?page=1#comm[…]28719](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360003511399-SSL-module-not-available-unable-to-install-packages?page=1#community_comment_360001528719|https://intellij-support.jetbrains.com/hc/en-us/community/posts/360003511399-SSL-module-not-available-unable-to-install-packages?page=1#comm[…]28719)), but now Betfair Lightweight and flumine don't appear in the list of available packages.



I'll also try your suggestion of installing the SSL package.



As I mentioned yesterday, I can run my code by going into the virtual environment via powershell, but it would be nice if I could find a way of running it directly from an IDE.



Cheers

---

## 2021-08-21 12:25:15 - issues channel

**Unknown**

Hi



I've tried installing flumine and Betfair Lightweight to my virtual directory via Pycharm, but I got error messages (see attached).



I'm using Python 3.8.



I'm just flagging this up in case it isn't a known issue.

---

## 2021-08-21 12:24:47 - strategies channel

**Jono**

whats the best way to pull scores or access the inplayservice info for a corresponding football match/market in flumine? Use a background worker and somehow fill the scores and other desired details into the blotter? Bit new to flumine but its already proving incredibly useful! Cheers for any help

---

## 2021-08-20 19:22:37 - issues channel

**PeterLe**

[@U013K4VNB6D](@U013K4VNB6D) I just read the posts above; if you're not using Pycharm, Id recommend it. Im new to python too, but it just seems easier to use, debug and visually more pleasing (its free too)

---

## 2021-08-20 11:46:01 - issues channel

**Mo**

Yes but flumine is not a requirement of flumine. You have several requirements already satisfied (installed) (requests, idna, certifi, chardet, urllib3) and then several more get installed along with flumine (tenacity, python-json-logger, betfairligthweight)



When you say



&gt; I've written a program that imports flumine. However, when I try to run it

How exactly are you running it?

---

## 2021-08-20 11:08:34 - issues channel

**Jeff Waters**

I've just deleted my previous virtual environment, and set up a new one using Conda. I then tried to install flumine in it, but it thinks that it's already been installed:



*(flum) C:\Bet-Project-Code&gt;pip install flumine*

*Collecting flumine*

  *Using cached flumine-1.19.9-py3-none-any.whl (115 kB)*

*Collecting python-json-logger==2.0.2*

  *Using cached python_json_logger-2.0.2-py3-none-any.whl (7.4 kB)*

*Requirement already satisfied: requests in c:\users\water\anaconda3\envs\flum\lib\site-packages (from flumine) (2.25.1)*

*Collecting tenacity==8.0.1*

  *Using cached tenacity-8.0.1-py3-none-any.whl (24 kB)*

*Collecting betfairlightweight==2.13.1*

  *Using cached betfairlightweight-2.13.1-py3-none-any.whl (63 kB)*

*Requirement already satisfied: idna&lt;3,&gt;=2.5 in c:\users\water\anaconda3\envs\flum\lib\site-packages (from requests-&gt;flumine) (2.10)*

*Requirement already satisfied: certifi&gt;=2017.4.17 in c:\users\water\anaconda3\envs\flum\lib\site-packages (from requests-&gt;flumine) (2021.5.30)*

*Requirement already satisfied: chardet&lt;5,&gt;=3.0.2 in c:\users\water\anaconda3\envs\flum\lib\site-packages (from requests-&gt;flumine) (4.0.0)*

*Requirement already satisfied: urllib3&lt;1.27,&gt;=1.21.1 in c:\users\water\anaconda3\envs\flum\lib\site-packages (from requests-&gt;flumine) (1.26.6)*

*Installing collected packages: tenacity, python-json-logger, betfairlightweight, flumine*

*Successfully installed betfairlightweight-2.13.1 flumine-1.19.9 python-json-logger-2.0.2 tenacity-8.0.1*



Also, I'm still getting the same error message. Any suggestions appreciated.

---

## 2021-08-20 10:38:59 - issues channel

**Jeff Waters**

Fair enough, thanks Jon.



I think I've now managed to successfully install flumine within the virtual environment. However, I'm still having the same error message as before.



I'm probably overlooking something blindingly obvious, but if anyone has any suggestions, they would be much appreciated. :slightly_smiling_face:

---

## 2021-08-20 10:10:15 - issues channel

**Jonjonjon**

Yes, that could be the problem. Unfortunately, I always fail when I try to install stuff in virtual environments. Hopefully someone else here knows the correct commands.

---

## 2021-08-20 09:45:41 - issues channel

**Jeff Waters**

Thanks Jon



That's probably it. I've set up a virtual environment in the folder where my code is located. To run the code, I just get IDLE to execute it.



Is it the case that I need to install flumine into my virtual environment?



Jeff

---

## 2021-08-20 08:36:58 - issues channel

**Jonjonjon**

How are you trying to execute your code? There's a chance that you are running a different Python installation, to the one where you installed flumine.

---

## 2021-08-20 08:10:01 - issues channel

**Unknown**

Hi



I've written a program that imports flumine. However, when I try to run it, I get an error message:



*Traceback (most recent call last):*

  *File "C:\Bet-Project-Code\backtest.py", line 9, in &lt;module&gt;*

    *from flumine import BaseStrategy*

*ModuleNotFoundError: No module named 'flumine'*



I definitely have flumine installed, as when I go 'pip install flumine' via CMD, I get told that I have (see screenshot). Also, I've checked my Python version number using the powershell, and I am on version 3.8.10 (in case that's relevant).



What do you guys suggest?



Thanks in advance.



Jeff

---

## 2021-08-18 14:29:26 - strategies channel

**thambie1**

Lots (probably most) people on this slack are. You can rent a sufficient server for between $5 and $20 per month for basic setups. Many use aws ec2

---

## 2021-08-17 15:38:01 - strategies channel

**Van**

[@UEA14GBRR](@UEA14GBRR) Sorry, I don’t quite understand what I’m missing.  I thought this is a common strategy that is/was profitable for beginners. Say I had a model that told me one of two teams are likely to score,  which would also be confirmed by inplay stats, why wouldn’t laying the draw at half-time and cashing out when a goal is scored (to lock in a profit) by a +EV bet? I guess I’m trying to reconcile gambling theory with googled material :wink:

---

## 2021-08-17 08:43:00 - strategies channel

**Jonjonjon**

Suppose someone new to fundamental modelling wanted to start on UK Horse Racing.



How much of a project would it be to:



• Get historical form data and odds, for developing a model.

• Getting up-to-date data, feeding that into a model, lining up that data with Betfair markets/selections, then placing bets?

---

## 2021-08-13 14:45:27 - general channel

**Peter**

Works for me too, at least on Colab. Local issues are likely because of the minimalistic nature of my set up rather than issues with the package. Still getting warnings about plotly when I install, which are easily solved by including listing it with betfairviz when I do the initial install, but would be useful for it to be a required package.

---

## 2021-08-13 09:51:28 - general channel

**Jan**

Okay thanks Mo for looking into this. Wasn't aware this is a colab issue exclusively. Will try on a local python setup later as well

---

## 2021-08-12 10:57:38 - general channel

**Oliver Varney**

okay so no need to set any params on the BFWL client passed into the flumine client (as per the getting started example)?

---

## 2021-08-11 14:06:26 - issues channel

**liam**

So flumine uses the machines hostname as a filter, this allows multiple flumine instances to run on the same markets without impacting each other. Tbh its not really setup for this so you better option would be some bflw code to hedge

---

## 2021-08-10 12:40:38 - random channel

**liam**

I really miss the excitement of getting something working with python for the first time :sob:

---

## 2021-08-07 10:40:56 - random channel

**Thomas JAMET**

But how to justify the cash flows if we are not legally setup?

---

## 2021-08-07 10:38:36 - random channel

**Mo**

You don't need to go through any kind of formal setup procedure. The biggest question is how are you going to distribute profits? Will you have one account doing the betting or will each member have their own account?

---

## 2021-08-06 18:48:23 - strategies channel

**Michael**

[@U016TGY3676](@U016TGY3676) As far as I'm concerned optimising execution is mostly just deciding what prices and sizes to bet at. There are a couple of little tricks that can help but price and size is most of it. Some people look for speed edges but that's a specialist thing and honestly beyond most of us - it's certainly beyond me so I choose my battles. The basics of it are totally obvious - if you lay too long you lose on the price and if you lay too short you don't get matched so it's finding the optimum. Mostly I try to do that with graphs and I use quite a bit of randomisation but it's always rather unsatisfactory. Likewise stakes. Similarly obvious dynamics and similar strategy. It's not unusual for beginners to assume that they can take a model that makes a bit of money on small bets and scale it in a linear way to make life changing returns but it should be quite obvious to a moderately smart person that that's not how it works. I don't think anyone who's ever posted on here would make such a moronic mistake and if they did I certainly wouldn't point and laugh.



The other sorts of questions you're thinking about would be whether to spread your bets over a range of prices, whether there's a back equivalent for your lays on another runner, that sort of thing. There are some tricks to do with delaying bets and there are some other sprinkles but that's most of it.

---

## 2021-08-06 10:17:09 - strategies channel

**PeterLe**

I think there are many on here in the same boat [@U01S1VB9X9P](@U01S1VB9X9P); ie not having any experience in programming (nor Python)

Going off at at tangent slightly but keeping on the topic of being new to python, Ive been lucky in that Ive had a quiet time at work, so ive been able to invest some time in learning python, which I have enjoyed doing.

What Ive found is that people are very open to helping others (thanks [@U016TGY3676](@U016TGY3676) and [@UUCD6P13J](@UUCD6P13J) in my case and [@USYQKE5HN](@USYQKE5HN) explanation of OOP using a teapot analogy :grinning:), but only when you have put some effort in yourself and put some 'spade work in'

Quite often you will see a .."how do I do this"..and the response is "what have you tried so far and have you looked at the examples". That is a very fair comment.

(Im not saying this is true in your case by the way; I'm just talking in general)

Ive finally got a working strategy going about a week ago and bolted a few new bits onto it. Its not doing as well as my main stuff but its working and making money, so to anyone who's completely new; you CAN do it, but it isnt going to happen overnight

Just one last thing; Im sure there are some super complex programs out there, but in my experience a well though out simple one can be just as effective so you dont need to be a python guru, good enough is good enough

---

## 2021-08-06 01:19:54 - strategies channel

**Unknown**

Also, I just realised that there is way more documentation than I thought. When you go to [https://liampauling.github.io/flumine/|documentation](https://liampauling.github.io/flumine/|documentation) it looks like it is limited to the menu on the right (highlighted in red below). There is another menu at the top left, which isn't obvious. I think I clicked on it once and just saw the same "getting started" stuff, but had totally glossed over the "advanced" section, which happens to be very juicy indeed. So I am only just looking at it now after nearly 2 months not even realising it was there :man-facepalming:

---

## 2021-08-06 00:56:47 - strategies channel

**Adrian**

Depending on your level of experience, the documentation and examples may or may not make much sense. As a beginner of python that was the case for me. I do not have a programming background so some of the assumed knowledge was missing, simple things like having the necessary scripts placed in a local directory, logging in and (not) logging out, and using an IDE to navigate the relationships between modules. I think a FAQ channel would be very handy.

---

## 2021-08-05 19:11:01 - strategies channel

**S G**

I m a newbie for flumine and betfairlightweight. I would like to setup a simple strategy, any ideas on where to start?

---

## 2021-08-04 12:13:21 - general channel

**liam**

Installs `ciso8601` for faster datetime [https://github.com/liampauling/betfair/blob/8ee78d0ff14a585bf49eb3712375c473e83180df/betfairlightweight/compat.py#L20|parsing](https://github.com/liampauling/betfair/blob/8ee78d0ff14a585bf49eb3712375c473e83180df/betfairlightweight/compat.py#L20|parsing) (uses c) and installs `orjson` for faster json [https://github.com/liampauling/betfair/blob/8ee78d0ff14a585bf49eb3712375c473e83180df/betfairlightweight/compat.py#L14|encoding/decoding](https://github.com/liampauling/betfair/blob/8ee78d0ff14a585bf49eb3712375c473e83180df/betfairlightweight/compat.py#L14|encoding/decoding) (uses rust)

---

## 2021-07-30 16:24:16 - issues channel

**Dirk**

Hey guys. A couple of days ago I tried to login to the API for the first time. I am using Python on windows and used XCA to make the certificates. At the moment of logging in, using the following code, I get an error:



`trading = betfairlightweight.APIClient(username=my_username,`

                                          `password=my_password,`

                                          `app_key=my_app_key,`

                                          `certs=certs_path)`

`trading.login()`



The error I get is (this is only the last part of the error code, it is way bigger than this):

`APIError: None` 

`Params: None` 

`Exception: HTTPSConnectionPool(host='[http://identitysso-cert.betfair.com|identitysso-cert.betfair.com](http://identitysso-cert.betfair.com|identitysso-cert.betfair.com)', port=443): Max retries exceeded with url: /api/certlogin (Caused by SSLError(SSLError(9, '[SSL] PEM lib (_ssl.c:4022)')))`



I've heard from others that it might have to do with the certificates, but I redid the full process like it is prescribed on the manual. Is there anyone with any tips/followup questions?

---

## 2021-07-27 18:59:31 - general channel

**Unknown**

It seems an odd setup but my knowledge of python isn't strong enough for me to be confident. 



Script 1 (the one referred to above) scrapes data to the mysql database. 



Script 2 harvests links from emails using imap_tools and when a link is scraped calls Script 3 using os.system(f'start "window title" cmd /k "python scrape.py (link) &amp;&amp; exit"').



Script 3 then uses the data in mysql to scrape part of these sites.

---

## 2021-07-27 18:54:17 - general channel

**PeterLe**

Folks, quick question please..First time I ran a live strategy (Whoop!)...but placed a bet deliberately low at 1.03..If I stop the program to edit the code and then restart it, does it somehow keep a live connection (ie am I in danger of  having too many connections if I stop and start it regularly? Thanks

---

## 2021-07-27 13:23:56 - general channel

**James**

...but then I'm relatively new to python

---

## 2021-07-22 14:29:51 - general channel

**George**

Hi all. Just getting started with streaming. May be a stupid question but - what is the best way to stop streaming? Let's say I'm logging data for a single horse race and I only want to log it until the start of the race. What is the right way to end the stream? thanks.

---

## 2021-07-22 09:51:49 - general channel

**RDr**

Hi, I am only getting started using betfairlightweight with python and looking for any existing link / shared codes about how to export all info from sample bz2 historical PRO data files into dataframes and csv files. The idea is more to get familiar with the data content (eg, visualise via excel or SQL) before deciding what transformations I need. Would anyone please give me some pointers? Thanks

---

## 2021-07-21 10:09:16 - random channel

**Adrian**

i think some kind of manual or flow chart would help for those getting started. i would like to create something visual to help me learn flumine. if anyone else is interested i might make a kind of mind map or something

---

## 2021-07-20 14:55:09 - issues channel

**Jonjonjon**

Please install flumine, and then use the get_nearest_price function mentioned above.

---

## 2021-07-20 10:56:30 - general channel

**Jono**

Just getting started with flumine and there are few things I am wondering about the process_market_book() and process_orders() functions. First of all i'd just like to clarify what causes both of these functions execute. The documentation says that process_market_book logic executes upon "True" being returned from the check_market_book function but the process_orders function is a bit more ambiguous. Will this also run upon a market_book being recieved from the stream?



Secondly is there anything that stops multiple orders being placed on a single market when the market conditions are right? For example say i want to place a "back" order of stake £10 on a given market when the best back odds are &gt;3. Currently i dont understand how it wouldnt empty my account on repeated runs by placing many £10 orders whilst the conditions i have specified for placing are true (inside the process_market_book function). I'm sure this isnt the case but any clarification would be greatly appreciated. Thank you!

---

## 2021-07-10 18:35:42 - general channel

**Michael**

I'm trying to use bfwl for the first time, whilst trying to login I get the following error "HTTPSConnectionPool(host='[http://identitysso-cert.betfair.com|identitysso-cert.betfair.com](http://identitysso-cert.betfair.com|identitysso-cert.betfair.com)', port=443): Max retries exceeded with url: /api/certlogin (Caused by SSLError(SSLError(9, '[SSL] PEM lib (_ssl.c:4024)')))". I presume this is coming from the certs being incorrect, I followed the xca certificate generation, has anything changed on this that I'm missing? [https://docs.developer.betfair.com/display/1smk3cen4v3lu3yomq5qye0ni/Certificate+Generation+With+XCA](https://docs.developer.betfair.com/display/1smk3cen4v3lu3yomq5qye0ni/Certificate+Generation+With+XCA)

---

## 2021-07-09 14:11:37 - general channel

**John**

Hi all, I have managed to collect some horse racing data (huge thanks to [@U4H19D1D2](@U4H19D1D2)’s flumine!) for the past month, and am trying to setup backtesting with flumine. I saw this backtest example [https://liampauling.github.io/flumine/quickstart#backtesting](https://liampauling.github.io/flumine/quickstart#backtesting) passing one market/file (1.170212754?) to the flumine. I was trying to find a way to pass the entire folder of recorded data to flumine, but with no luck. Please could someone give me a pointer? Many thanks.

---

## 2021-07-08 10:38:59 - general channel

**Ivan Zhou**

not sure if I am doing something wrong im running

```import logging



import betfairlightweight





# setup logging

logging.basicConfig(level=[http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))  # change to DEBUG to see log all updates



# create trading instance (don't need username/password)

trading = betfairlightweight.APIClient("username", "password")



# race card login

trading.race_card.login()

# update

market_id = "1.185112813"



# race card request (provide list / returns list)

race_cards = trading.race_card.get_race_card(market_ids=[market_id])

print(race_cards)```

---

## 2021-07-07 16:56:07 - issues channel

**Mons___das**

Hey guys! I m rather new to flumine and am trying to wrap my head around everything. Amazing stuff from what i can see, big thanks to [@U4H19D1D2](@U4H19D1D2)

I am currently trying to build up a database with that i can do backtests and filter markets (for the backtest), and down the road maybe also track the orders i have placed per strategy. First step i wanted to get an idea of the general structure of how all of this is going to look like. I see flumine comes with a market_recorder (and an s3recorder on top) and a backtest function, so basically all i need is being provided, i just have to connect the puzzles pieces :smile: The s3recorder seems to throw out some zip files (1 per market), which i am supposed to store in a s3bucket. Are these the files i am supposed to feed into the backtest machinery? Assuming thats how its done, i need to know which files i throw into the backtest for a certain strategy, so i need a way to filter these markets. I was thinking that this one be one job of a database, which for example has basic information for each market_id, like what event_type it is, time of the event, runners, etcetc. How would i go about building such db? Can the market recorder also be used for this? or would i extract this info straight from the files in the s3 bucket?

---

## 2021-07-02 16:40:42 - strategies channel

**AndyL**

I found a 1% edge from my data mining setup, created strategy in Flumine ran it over night took 4 hours on 6weeks of aus horses, returned -1%, not happy with mining on market snapshots, looks like ill have to use Flumine and 4hours per iteration...

---

## 2021-07-02 04:51:51 - general channel

**Rob (NZ)**

Justing doing pip install of Flumine and it came up with  Attempting uninstall: betfairlightweight

    Found existing installation: betfairlightweight 2.12.1

    Uninstalling betfairlightweight-2.12.1:

      Successfully uninstalled betfairlightweight-2.12.1

Successfully installed betfairlightweight-2.9.0  ,

is that all good?

---

## 2021-07-01 12:52:41 - strategies channel

**D C**

Trouble is that when you are researching something that from your personal perspective you don't know much about, how do you know when "enough is enough" ? I mean you could hammer away at a shit idea for too long if you don't know when to stop. It's not like parameter selection in a model where fitting will tell you what parameters are significant and which you can throw away. How is someone new to the game supposed to know what is too little/much time?

---

## 2021-06-29 20:33:59 - random channel

**D C**

yeah. I was getting lags of 15 seconds at times for a short period but could be a problem with my setup.

---

## 2021-06-26 15:50:27 - general channel

**Ivan Zhou**

Hey everyone. I have been working on a horse racing model and I am ready to give it a punt and automate the model. I am completly new to the betfair api and betfairlightweight. I'm asumming there is a beginner guide, if someone could point me that direction so I can have a go.

---

## 2021-06-26 08:17:01 - random channel

**Oliver Varney**

worth checking out this function. It may be abit obscure if your new to python but in plain English ignoring most of it, basically a market_book update will come through and need to be processed. To save processing time, a function was created strategy.check_market_book (it looks like in newer versions of flumine it gets called via strategy.check_market  ) to throw away any updates that are not required. If the function strategy.check_market_book return True then strategy.process_market_book will be called. If strategy.check_market_book return False it will not be called.

---

## 2021-06-24 10:43:43 - general channel

**Adrian**

is it part of a package i haven't installed or something? I've installed flumine

---

## 2021-06-23 08:20:40 - general channel

**Adrian**

[@UQL0QDEKA](@UQL0QDEKA) Yes I have 2FA set up so that it adds the code to the end of my password. This works for `trading.login()` so perhaps Flumine is setup for non-2FA?

---

## 2021-06-22 08:50:56 - strategies channel

**Michael**

Well yeah there's inevitably a degree of competition. I know enough about [@U4H19D1D2](@U4H19D1D2)'s setup to know that we don't directly compete too much but there's undoubtedly other people out there. In a way though it's not the good players that are the problem; it's the bad ones who scrape up dribbles of profits on low margins with a lot of bets. They can swamp out your good bets whilst throwing away their value on a load of bad ones. Nobody wins from that.

---

## 2021-06-15 11:18:46 - issues channel

**Scott**

Morning all, is there any obvious reason why it appears bflw isn’t passing my key over to bf? I’m on a windows machine and certs folder is at the same level as bflw file.. created the cert and key on Linux following steps and uploaded to bf okay. Just can’t seem to log in. First time creating my own OpenSSL stuff so quite probable that I have messed up along that line although I appear to have the three files req 

---

## 2021-06-12 20:07:39 - strategies channel

**AndyL**

Good point [@UGV299K6H](@UGV299K6H) the criteria for stopping... im not losing money now ive got bflw &amp; flumine setup, at some point ill need to go live with something but im going to set that stop point...

---

## 2021-06-11 05:37:27 - general channel

**VT**

Hi, I've been researching how I can get Betfair historical data to backtest, any tips on a good tutorial for beginners in Python? I would like to consult the live football game moneyline markets. I intend to consult the free Basic data, 1 minute intervals, I would like to convert the odds values ​​in each minute to a dataframe.

---

## 2021-06-08 12:01:25 - general channel

**Brian**

Hi guys, looking for a little assistance (bear with me as I'm still pretty new to this :slightly_smiling_face:)... I'm using Liam's very helpful error handling example script ([https://github.com/liampauling/betfair/blob/master/examples/examplestreamingerrhandling.py](https://github.com/liampauling/betfair/blob/master/examples/examplestreamingerrhandling.py)) but I seem to have a bit on an issue in that once the loop has gone through all of the market books and starts over, it doesn't seem to be picking up updated odds from that point, like it keeps going over the stream it initially created at that point in time. Maybe this is expected behavior and there's still something I'm missing, but if there is I'd really appreciate some help figuring out what it is. I tried to move the start of the loop higher to incorporate the creation of the stream... which does work... but creates way too many logins per hour which Betfair aren't happy about. Any assistance would be hugely appreciated!

---

## 2021-06-03 10:41:32 - issues channel

**liam**

So the connection error is on the account details endpoint, whats the setup here in terms of number of markets?

---

## 2021-05-29 23:23:25 - general channel

**John**

Thanks [@U4H19D1D2](@U4H19D1D2). Here is the init function of my strategy class



```class strategy_test(BaseStrategy):





    def __init__(self, *args, **kwargs):

       BaseStrategy.__init__(self, *args, **kwargs)



       # date time

       now = datetime.now()

       dt_string = now.strftime("%Y%m%d")



       # setup logging

       path_file_log = os.path.abspath(os.path.join(cwd, "../log/", strategy_id + f"_{dt_string}" + ".log"))

       logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %I:%M:%S | ', level=logging.DEBUG,

                           filename=path_file_log)

       [http://logging.info|logging.info](http://logging.info|logging.info)("Log file: " + path_file_log)```

Any pointer to output a log file to a local drive will be appreciated.

---

## 2021-05-29 10:48:46 - general channel

**John**

Hi I was trying to setup my own log files (by doing logging.basicConfig(file_name) ) so to understand a bit deeper into the flumine. It turns out flumine still outputs the logs to the screen only. Guess I am missing something in flumine. Please could someone give me a pointer/example how I can output the logs to a file (ideally in the same time printing the logs on the screen/console too)? Many thanks.

---

## 2021-05-26 11:50:33 - issues channel

**kieran**

Hi, Apologies I am getting the same issue. I'm a Python beginner.  I'm not fully sure what "var on the flumine client" means or what the fix is? Any guidance would be appreciated.

---

## 2021-05-24 09:58:51 - general channel

**Scott**

Good Morning All! I was pointed this way by D C, If its the same person here as Twitter.. EXTREME Newbie to automation. Thrown together some python for very small programs, only to get them to produce the results I'm after. Starting Year 2 of a Data Science degree in September through the open uni as a side to creating my own betfair models. Never worked with an API before so as a complete beginner what Programming Fundamentals would you recommend diving into before even attempting to use bflw to automate my trading?

---

## 2021-05-23 23:56:10 - random channel

**James T**

I think that’s a really good / interesting question. I’ve wondered a few times about how I can keep my strategies (essentially passive income) running for my family should I die suddenly.



I’ve had an intention to properly document all my systems, setup, theory, etc... but never get round to it. Even then no one in my family would have the computer knowledge to maintain any of it, so they’d still need help. 



For now I just hope I don’t die suddenly!



Perhaps buying life insurance for an amount roughly equal to what I think my systems are worth would be another option...

---

## 2021-05-22 09:08:09 - general channel

**PeterLe**

Thanks [@U0128E7BEHW](@U0128E7BEHW) Im new to Python (and programming in general), so I guess I would create a variable using that formula, but where in the lowestlayer code would I insert it?Thanks

---

## 2021-05-19 18:35:11 - strategies channel

**Paul**

To answer your question though, multiple people have claimed to come up with derivatives that take this into account, but the only one that looks like it had legs and spelled it out last time I looked was a PhD thesis from Imperial. That said some of those links are new to me.

---

## 2021-05-17 21:27:57 - general channel

**AndyL**

Just downloaded bflw, setup certs, ran exampleone.py, worked easy peasy :-)

---

## 2021-05-12 20:54:40 - strategies channel

**birchy**

[@U01PJ5YMFBJ](@U01PJ5YMFBJ) definitely get Flumine up and running with [@U4H19D1D2](@U4H19D1D2)'s marketrecorder example (it pretty much works straight out of the box). That will give you ALL of the market data for each race. Also setup a basic strategy to avoid account suspension for leeching. Again, [@U4H19D1D2](@U4H19D1D2)'s lowestlayer example will suffice, but I'd suggest setting the price trigger to something like 1.80. You won't lose much laying odds on runners.

You can also run backtests in Flumine once you have a month or 3 of recorded data. What I would suggest is to use this ability to parse the data files to gather statistics rather than run full backtests. From there, you may find some useful patterns, upon which you could run a few backtests to prove they work as a strategy. And then.... assuming that you've done all of the above and backtests show that your ideas are sensible, you can port the Flumine strategy to live betting, which will give you "real world" data to analyse.

---

## 2021-05-07 23:14:01 - general channel

**Alex**

Hi everyone, I have a couple of questions and was hoping someone could help me or point me in the right direction. My goal is to simply have an interactive, live representation of the orderbooks for the (live) matches in different sports markets (to begin with, only MATCH ODDS). I am using the bflw library for that as follows: I subscribe to different sports markets (tennis, football, ...) as a whole in my ‚streaming class‘, as there is a limit of how many streams are allowed to be running at a time. This class has an attribute called marketbooks, which is a dictionary (market_ids as keys) that is updated with the most recent streaming updates – therefore, older updates are simply overwritten – in an infinite while loop. I pass this dynamic marketbooks attribute to another class, which is basically dynamically starting processes that take in the marketbooks and filter it for the specific market_id assigned to the thread, thus only processing the orderbook for this specific market_id. In this sub-class I then log the changes in the orderbook in yet another while loop and potentially feed the data into a tkinter gui. While this is no problem with a single market_id and I get live data in my console, I am struggling with a concurrent implementation using asyncio that would start all processes concurrently, so that there is no delay (I tried it with threading first, but ran into issues).

My questions are: Does this implementation make sense? Is it efficient or am I overcomplicating things? How can I easily see – in my setup or in the optimal setup – if a game has ended? How would the asyncio logic look like so that I don’t wait on any of the infinite while loops to finish?

 If this is not appropriate to discuss here, I would appreciate if someone willing to help could send me a private message. Thanks!

---

## 2021-04-28 17:51:30 - general channel

**Newbie99**

If I want to access all orders coming through the order stream (i.e. that includes those not placed via Flumine so they won't necessarily form part of a strategy), where should I be looking?



I have setup a background worker and then was heading down this path:



```def get_live_orders(context: dict, flumine) -&gt; None:



    for stream in flumine.streams._streams:

        # Find the order stream and do whatever```

But is there a preferred way to go about this (i.e. something more obvious I've overlooked)?

---

## 2021-04-26 17:42:49 - random channel

**Newbie99**

Possibly a bit of a longshot, but is anyone else running Nord VPN (locally) on Windows 10?



I'm running Nord VPN on my laptop and wanted to write a script to start an EC2 instance using boto3 etc, that all works fine. However when I try to create an SSH tunnel it seems to be blocked (which is logical), but I can't work out how to bypass this.



In the Nord VPN for windows client I have SSH setup under split tunnelling, so it works fine if I just try to SSH manually.



Additionally if I turn off the Nord VPN client this script works fine.



Here is my script, is anyone aware of a smart way to get something like this working without having to manually switch off the Nord VPN client (the fetch public IP function grabs the public IP of the EC instance)?



```def ssh_tunnel():



    EC2_URL = fetch_public_ip()

    username = "ec2-user"

    pem_file = '~/betfair.pem'



    # Create the tunnel

    server = SSHTunnelForwarder(

        (EC2_URL, 22),

        ssh_username=username,

        ssh_pkey=pem_file,

        remote_bind_address=(EC2_URL, 27017),

        local_bind_address=('127.0.0.1', 27017)

    )

    # Starts the tunnel

    server.start()



    # Prints the local bind port

    print(server.local_bind_port)  

    

    # Closes the tunnel

    server.stop()```

---

## 2021-04-26 14:51:24 - general channel

**Phil Anderson**

Yes, thats exactly what I'm trying to do. I tried taking out the bet target type, but then get an error msg when I run it: 'errorCode': 'INVALID_INPUT_DATA', 'errorDetails': 'One or more inputs to the operation were invalid'



Forgive me if it's something simple, but I'm new to this and I'm still trying to get to grips with it.

---

## 2021-04-26 10:40:01 - random channel

**D C**

no longer doing the XPS unbuntu preinstalled models.

---

## 2021-04-26 10:35:05 - random channel

**D C**

Can anyone recommend (from actual experience) a model and brand of new laptop that will allow an installation of ubuntu 20.04 (or linux mint equivalent) without any issues with hardware/drivers etc? Dell have crapped out on linux completely and I don't want to run the risk of excessive customs fees on a high end model from system76 in USA. And advice appreciated.

---

## 2021-04-21 06:47:51 - general channel

**Greg**

Stoked..long time lurker..first time poster noob (forgive the dumb questions if they come). Logged in via API and certs after teaching myself some python for the last 3 months:sunglasses: .Didn't think I could do it, let alone with 50 year old chemo brain  (fell asleep at my desk a lot..like an 80 year old man :laughing:) but life is full of surprises. Not sure I will get anywhere but it has been a hoot-like having a new superpower, Thank you Liam for writing this.You are a * and I am grateful. It has given me something to challenge meself with while the family is out (and I'm not sat in an undignified fashion on the toilet) Oral chemo starts tomorrow so thought I better get me thanks in before more turpentine melts my body again :grin: All the best for green across the board folks.:money_mouth_face:

---

## 2021-04-18 07:27:41 - general channel

**Peter**

As long as you have a recent version on Python and the Flumine dependancies installed (which installation of Flumine should take care of for you) there shouldn't be any special steps needed to run on Ubuntu.

---

## 2021-04-15 16:42:18 - strategies channel

**Dave**

Sounds like the database is the bottleneck here? Call to place orders/get a response should be in millis even in your current setup (ignoring any inplay delay)

---

## 2021-04-15 15:42:44 - strategies channel

**Jono**

yes, ive yet to bear witness to the majesty of streamed data and i get a little bit too excited thinking about the possibilities. the 20 second time range is the result of other obstructions and api calls i have to make in order for the strategy to run. Ill be mending and streamlining the vast majority of the process just want o make sure im getting started on the right foot with the bf side of things

---

## 2021-04-15 15:37:49 - issues channel

**Jorge**

I installed bflw using: `pip install betfairlightweight[speed]` , which installed orjson

---

## 2021-04-12 10:43:19 - general channel

**Taking Value**

Cheers Liam. If I pull the latest version of the relevant py file from the repository is there a way to direct it to add to the races files in the same sub directory on my ec2 environment rather than have it setup a new sub directory for the new stream?



My thought process is that this way it will simply add to the race files that have already been created and contain data rather than create a new sub-directory for the new stream and record the latest data to new files that I then have to merge with the old ones.

---

## 2021-04-11 19:42:55 - general channel

**Taking Value**

Yea, thanks for those examples. As I am still relatively new to python and programming this has been a great way to understand the power of python and specifically the way to utilise classes properly.

---

## 2021-03-19 19:56:32 - random channel

**Paul**

This is a good tool for exploration if you’re completely new to it all: [https://aws.amazon.com/ec2/instance-explorer/|https://aws.amazon.com/ec2/instance-explorer/](https://aws.amazon.com/ec2/instance-explorer/|https://aws.amazon.com/ec2/instance-explorer/)

---

## 2021-03-17 08:56:24 - strategies channel

**liam**

Exactly, if on the flumine readme page it describes how you have to setup MySQL, Redis, streaming process and a event process before you can even start processing data I think the take up would be zero, instead its 10 lines of pure python with the ability to add all of the above if required

---

## 2021-03-16 12:32:04 - strategies channel

**birchy**

The AWS thing was new to me when I started, but S3 is definitely worth setting up. I run a modified marketrecorder that saves the data into it's corresponding month based on projected start date/time. It just makes it easier to pull out specific months for backtesting, i.e. summer flat racing is &gt; winter racing for one of my strategies.

---

## 2021-03-15 16:08:04 - general channel

**Unknown**

Guys (gals), following recent chats about Monte Carlo, bet analysis, etc, I threw together a Python project to quickly analyse a BetHistory.csv, which can be obtained from [https://myaccount.betfair.com/activity/bettinghistory](https://myaccount.betfair.com/activity/bettinghistory) when logged in to the betfair website. For those of us that are not statisticians or maths professors, I think it's a useful beginners tool. Would appreciate any feedback, improvements, etc.

Advance warning: I've used a tkinter gui. It's not the prettiest thing in the world, but it gets the job done and is already part of the Python standard library.

---

## 2021-03-14 08:10:15 - random channel

**IndikaE**

Thanks. It does seem like a good idea to use ips. But as a complete beginner I don’t even know how to get historic data for IPS. Is that even available? My fundamental problem is that I am relying on a data feed that doesn’t provide timestamps, but only times of events relative to the beginning of each half. And I need to sync that up with betfair market data Using ips seems very reasonable, but I don’t know how to get ips historic data for backtesting. Is that possible?

---

## 2021-03-09 19:29:23 - strategies channel

**IndikaE**

Yes - I will take your advice. I have probably been overthinking it a bit. I am really only seeking confirmation that my edge is there. I have no interest in calculating VAR or anything. But my back tests do not look random at all(either I have a pretty decent edge, or I am unwittingly leaking information from train to validation). So I guess I should just use one of the ‘naive’ approaches and get on with it. Looking forward to being able to use the “check £ in account”-approach as soon as I get this strategy deployed(first time for me).

---

## 2021-03-08 20:07:31 - general channel

**Michael**

I'd suggest you get a 'python for beginners' type book - like literally a paper one and just work your way through it. You don't need to be much of a coder to work with this stuff - take it from me I'm shit. Half the book will probably get you there.

---

## 2021-03-06 18:50:50 - issues channel

**liam**

What does the setup look like in terms of framework.add_strategy

---

## 2021-03-06 14:07:26 - strategies channel

**D C**

100% this -&gt; "_*There are many beginners reading this forum, it's confusing and damaging for them to have you repeating this error as if it's a fact.*_". Saying that a true value/0EV price does not exist is basically saying that you don't know anything about or don't believe in probability theory and statistical inference and it is dangerous to propagate that notion to people new to the game who may not have the confidence to call out this flawed thinking.

---

## 2021-03-06 13:52:54 - strategies channel

**Michael**

Saying that you don't know whether X price has positive, negative or zero value isn't the same as insisting that 0EV doesn't exist, it's just recognising that you don't know it. There are many beginners reading this forum, it's confusing and damaging for them to have you repeating this error as if it's a fact. When you say that there is _'no single "right" price for a runner'_ you're arguing that there is either no 0EV price or more than one. The former conjecture (the idea that there is no 0EV price) is impossible to reconcile with the idea of +EV and -EV as you obviously can't have both without a mid-point. The latter (more than one 0EV price) would imply that a given price can simultaneously be both -EV and +EV, in other words both the layer and the backer can make a profit on the same bet, this can't be true either on a single instance or on hypothetical repetitions.  So: Since there can't be less than one 0EV price and there can't be more than one how many 0EV prices are there for a particular bet at a particular instant? ONE

---

## 2021-03-05 09:48:27 - issues channel

**birchy**

3.8.8 on dev machine

3.6.9 on production machine

First time I've actually checked that.

---

## 2021-03-02 12:05:08 - issues channel

**Peter C**

For me there is no difference in result between 1.17.5 and 1.176b0. I installed by typing:

`pip install -Iv flumine==1.17.6b0`

---

## 2021-02-25 16:34:23 - general channel

**William Martin**

Now if there was a course on getting started with the betfair API I would buy it! struggling to wrap my head around it as I'm new to programming and all examples are horse racing whereas I am interested in football

---

## 2021-02-21 13:09:03 - general channel

**Peter C**

Thanks for the pointer. I ran into this problem for the first time today so good timing!

---

## 2021-02-20 20:45:49 - general channel

**Richard**

Hi everyone, long time lurker first time poster. How would I get a rolling 2 minute window of total volume traded for each runner every 30 seconds on the streaming data?

---

## 2021-02-19 19:10:09 - general channel

**William Martin**

thanks! very new to automated stuff, used trade football markets in college a good few years ago, with a lot of success but got to time consuming with no automation and when I finished college I didnt have the free time I did before!



I'm looking to build a prototype of an app idea I have so not 100% sure if I am in the right place but eager to learn what people are doing with the betfair API and the bot trading aspect is really interesting

---

## 2021-02-18 07:09:20 - general channel

**KG**

thanks [@UBS7QANF3](@UBS7QANF3) - I amended with the patch, still getting the same error though - any chance you can cast your eyes over my code and see if you can catch my mistake? I'm not a python native, but trying to get the library to work:



```import logging



from unittest.mock import patch

import smart_open



import betfairlightweight

from betfairlightweight import StreamListener



# setup logging

logging.basicConfig(level=[http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))



# create trading instance (don't need username/password)

trading = betfairlightweight.APIClient("username", "password")



# create listener

listener = StreamListener(max_latency=None)



# create historical stream (update file_path to your file location)

stream = trading.streaming.create_historical_generator_stream(

    file_path="../_data/2021_01_JanRacingPro.tar",

    listener=listener,

)



with patch("builtins.open", smart_open.open):   

    gen = stream.get_generator()



    for market_books in gen():

        for market_book in market_books:

            print(market_book)```

---

## 2021-02-03 20:40:15 - issues channel

**Peter C**

I'm trying to access live data for the first time - using the quickstart example from the docs. I import the example strategy, and start(self) runs, but then check_market_book doesn't appear to be called, but the program continues to run with no error. Has anyone experienced this before?

---

## 2021-01-14 16:17:01 - strategies channel

**Crofty**

Re the image that Birchy posted above and Mo kindly explained, how can a non-mathematician learn how to interpret that i.e. what courses / articles / videos would explain how to do so for a complete beginner?

---

## 2021-01-13 20:44:03 - strategies channel

**birchy**

Well just those 2 responses alone tells me that your setups are far more complicated than mine are. I'm literally taking data as it arrives from betfair, doing a few simple calculations and submitting some bets. I don't have any external frameworks or components beyond a single utilities file that contains a handful of boilerplate functions. As for "modelling", when I have an idea, I create some triggers/parameters in a Flumine strategy, press the go button and wait...modify triggers...rinse and repeat. I don't have 100's of hours available to be able to learn data science and then write a million lines of code to create an AI that tells me I need to back winners and lay losers. Yes, I'm a Luddite.

Anyone got a link to some sort of "modelling for twats" articles/books?

---

## 2021-01-13 01:06:14 - general channel

**jgnz**

When using market recorder in flumine, what is the best way to keep the zipped files? I only just realised flumine is deleting them after 3600 seconds, so all my recorded markets are gone.



Should I setup a crontab to move zipped the files out before flumine deletes them? Or is there a background worker that does this?

---

## 2021-01-12 10:33:41 - general channel

**Carsten**

i got a errand shortly, and will be away for a couple of hours. again thanks for all the help. Hope we can continue later on.  hope i can provide you all the info you need to help me. I was using chrome browser would it make a difference using other browser ?  Also if you think it would be easier if you saw the output your self, we could setup a remote view of it. If its easier and speed up the process so i dont keep you active in here for weeks :slightly_smiling_face:

---

## 2021-01-07 11:28:45 - general channel

**birchy**

Question regarding analysis of settled bets...

What setups do you have to handle this? Or more specifically, what bet data do you save? I've always been a bit slack-arsed with post-race analysis: if the P&amp;L is &gt;£0, I leave the bot alone (or maybe make some minor tweaks if I can see some _obvious_ improvements) and if P&amp;L &lt;£0, I simply change some trigger values and try again. There's no real analysis behind it other than what I _think_ the triggers should be. I'm designing something to improve this and want to keep things simple, so was thinking of creating a CSV per strategy with the following data in it:



1. triggers that activated the bet being placed

2. market conditions when triggers were satisfied

3. the actual bet info (price, stake, etc)

4. result/P&amp;L for the bet

Obviously the above is potentially a LOT of data per bet, so I'm wondering what you would consider to be essential? Or maybe there is a better approach?

---

## 2021-01-06 16:26:40 - general channel

**liam**

This is going to be so painful for me, api / strategy setup / database 

---

## 2021-01-03 11:57:02 - general channel

**steve**

hi guys new to using live odds. im trying to find the near_price and far_price bsp, but keep getting 'None'. Can get the back and lay prices ok. i'm using the following code. anyone know what im doing wrong?



price_filter = bflw.filters.price_projection(

    price_data=['SP_AVAILABLE','SP_TRADED','EX_BEST_OFFERS','EX_ALL_OFFERS','EX_TRADED']

    )

market_books = trading.betting.list_market_book(

    market_ids=[1.177514203],

    price_projection=price_filter

    )

for runner in market_books[0].runners:

    print(runner.sp.near_price)

    print(runner.sp.far_price)

---

## 2021-01-02 17:07:34 - general channel

**liam**

Free tier is micro? What’s your setup? Flumine? How many markets?

---

## 2021-01-02 12:25:52 - general channel

**Mo**

```mberk@mberk-desktop:/tmp $ /usr/bin/python3.8 -m venv ./venv-baseline                                                                                                                                       

mberk@mberk-desktop:/tmp $ ./venv-baseline/bin/pip install [git+git://github.com/liampauling/betfair](git+git://github.com/liampauling/betfair) tqdm

Collecting [git+git://github.com/liampauling/betfair](git+git://github.com/liampauling/betfair)                                                                                                                                                         

  Cloning [git://github.com/liampauling/betfair](git://github.com/liampauling/betfair) to ./pip-req-build-iboy4gb7                                                                                                                                  

  Running command git clone -q [git://github.com/liampauling/betfair](git://github.com/liampauling/betfair) /tmp/pip-req-build-iboy4gb7                                                                                                             

Collecting tqdm                                                                                                                                                                                             

  Using cached tqdm-4.55.0-py2.py3-none-any.whl (68 kB)                                                                                                                                                     

Collecting requests&lt;2.26.0                                                                                                                                                                                  

  Using cached requests-2.25.1-py2.py3-none-any.whl (61 kB)                                                                                                                                                 

Collecting urllib3&lt;1.27,&gt;=1.21.1                                                                                                                                                                            

  Using cached urllib3-1.26.2-py2.py3-none-any.whl (136 kB)                                                                                                                                                 

Collecting certifi&gt;=2017.4.17                                                                                                                                                                               

  Using cached certifi-2020.12.5-py2.py3-none-any.whl (147 kB)                                                                                                                                              

Collecting chardet&lt;5,&gt;=3.0.2                                                                                                                                                                                

  Using cached chardet-4.0.0-py2.py3-none-any.whl (178 kB)

Collecting idna&lt;3,&gt;=2.5    

  Using cached idna-2.10-py2.py3-none-any.whl (58 kB)

Using legacy setup.py install for betfairlightweight, since package 'wheel' is not installed.

Installing collected packages: tqdm, urllib3, certifi, chardet, idna, requests, betfairlightweight

    Running setup.py install for betfairlightweight ... done

Successfully installed betfairlightweight-2.11.1 certifi-2020.12.5 chardet-4.0.0 idna-2.10 requests-2.25.1 tqdm-4.55.0 urllib3-1.26.2

mberk@mberk-desktop:/tmp $ /usr/bin/python3.8 -m venv ./venv-c                                         

mberk@mberk-desktop:/tmp $ ./venv-c/bin/pip install [git+git://github.com/mberk/betfair@cache-c-extension](git+git://github.com/mberk/betfair@cache-c-extension) tqdm

Collecting [git+git://github.com/mberk/betfair@cache-c-extension](git+git://github.com/mberk/betfair@cache-c-extension)

  Cloning [git://github.com/mberk/betfair](git://github.com/mberk/betfair) (to revision cache-c-extension) to ./pip-req-build-kfss8qxh

  Running command git clone -q [git://github.com/mberk/betfair](git://github.com/mberk/betfair) /tmp/pip-req-build-kfss8qxh

  Running command git checkout -b cache-c-extension --track origin/cache-c-extension

  Switched to a new branch 'cache-c-extension'

  Branch 'cache-c-extension' set up to track remote branch 'cache-c-extension' from 'origin'.

Collecting tqdm

  Using cached tqdm-4.55.0-py2.py3-none-any.whl (68 kB)

Collecting requests&lt;2.26.0

  Using cached requests-2.25.1-py2.py3-none-any.whl (61 kB)

Collecting certifi&gt;=2017.4.17

  Using cached certifi-2020.12.5-py2.py3-none-any.whl (147 kB)

Collecting urllib3&lt;1.27,&gt;=1.21.1

  Using cached urllib3-1.26.2-py2.py3-none-any.whl (136 kB)

Collecting chardet&lt;5,&gt;=3.0.2

  Using cached chardet-4.0.0-py2.py3-none-any.whl (178 kB)

Collecting idna&lt;3,&gt;=2.5

  Using cached idna-2.10-py2.py3-none-any.whl (58 kB)

Using legacy setup.py install for betfairlightweight, since package 'wheel' is not installed.

Installing collected packages: tqdm, certifi, urllib3, chardet, idna, requests, betfairlightweight

    Running setup.py install for betfairlightweight ... done

Successfully installed betfairlightweight-2.11.1 certifi-2020.12.5 chardet-4.0.0 idna-2.10 requests-2.25.1 tqdm-4.55.0 urllib3-1.26.2

mberk@mberk-desktop:/tmp $ ./venv-baseline/bin/python benchmark.py                                     

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5791.84it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5790.26it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5777.81it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5800.95it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5790.11it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5800.39it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5774.89it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5786.89it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5787.31it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5771.91it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:37&lt;00:00,  3.79s/it]

37.88023018836975

mberk@mberk-desktop:/tmp $ ./venv-c/bin/python benchmark.py                                            

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5804.39it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5812.31it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5797.65it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5781.36it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5792.19it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5803.93it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5759.62it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5762.72it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5749.46it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 21919/21919 [00:03&lt;00:00, 5721.92it/s]

100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10/10 [00:37&lt;00:00,  3.79s/it]

37.93798065185547```

---

## 2021-01-01 11:38:07 - issues channel

**liam**

however if you have logging setup the warnings will show if you set [https://github.com/liampauling/flumine/blob/707a81990d1c51d64e964c781c5e700fe58646de/flumine/strategy/strategy.py#L45|log_validation_failures](https://github.com/liampauling/flumine/blob/707a81990d1c51d64e964c781c5e700fe58646de/flumine/strategy/strategy.py#L45|log_validation_failures) to True

---

## 2020-12-24 05:49:18 - general channel

**Sam Asin**

Hey guys, I'm new to the betfair API and having some fun messing with it.

---

## 2020-12-19 15:42:14 - general channel

**Jorge**

Aha, so right now I need to cache the CurrentOrders.streaming_update['orc']['mb'] first time I call `output_queue.get()`. And then add the upcoming streaming_updates to it, so I get the full matched backs in a market for a given selection. Would this include all orders with status == 'EXECUTION_COMPLETE'?

---

## 2020-12-18 06:34:46 - issues channel

**liam**

Huh? This doesn’t look like a bflw error to me, the setup file is valid and works on py3.6

---

## 2020-12-18 00:08:46 - issues channel

**Matthieu Labour**

Hello all.

Would it be possible to rename `_requires` into, for example, `extra_requires`

at the following location [https://github.com/liampauling/betfair/blob/master/setup.py#L10](https://github.com/liampauling/betfair/blob/master/setup.py#L10)

The reason is that I am running into an error with python 3.6.9

```Traceback (most recent call last):                                                                               

  File "/home/xxx/.local/lib/python3.6/site-packages/pkg_resources/_vendor/packaging/requirements.py", line 99, in __init__                                                                                   req = REQUIREMENT.parseString(requirement_string)                             

  File "/home/xxx/.local/lib/python3.6/site-packages/pkg_resources/_vendor/pyparsing.py", line 1654, in parseString                                                                                           raise exc                                                                                ```

Generally, what is the best way to make a request for changes, report an issue and contribute? Should I, for example, create an issue on github? Can I create a PR, add reviewers, merge?

Thank you!

---

## 2020-12-17 11:04:03 - issues channel

**ricky**

I am recording marketdata via AWS S3 (S3MarketRecorder) , I expect market_catalogue shall be stored in Json format, but i got flat file.

I am new to AWS, i am not sure if it is cause by my setting problem or the source code need change to



self.s3.put_object(

	Body=str(json.dumps(market.market_catalogue.json())),

	Bucket=self._bucket,

	Key=os.path.join(

		"marketdata",

		"marketCatalogue",

		market.market_id,

	),

)

---

## 2020-12-16 10:30:25 - strategies channel

**Kai**

Statistical tests or Monte Carlo simulations for complicated setups help, but in the end it comes down to judgement.

You can also plot your pl and see how smooth it looks

---

## 2020-12-12 12:30:07 - general channel

**Alessio**

so something like a conda environment, install bflw (and dependencies) there, zip and declare as a layer to be used in the lambda?

---

## 2020-12-12 10:00:26 - strategies channel

**Artur Gräfenstein**

I think you are both right. But that hits it pretty well: “Over fitting is simply when your model too closely matches the noise in your data!” Pretty easy to understand for a beginner!

---

## 2020-12-03 18:48:25 - strategies channel

**birchy**

Thanks fellas. I've got no issues with laying runners at any price as the £10 payout target is a decent protection that allows sub-£2 bets.

Bearing in mind that I'm fairly new to this Flumine wizardry, what's the best way to save 'real' market data? I have a MarketRecorder running but that's a strategy of it's own, taken from the Flumine examples.

---

## 2020-12-03 17:34:15 - issues channel

**Aaron Smith**

Thanks for looking into it! I didnt leave out any logs, after this the last log just repeats for a long time. I didnt fork flumine and am only importing my installed flumine version, so the flumine code is unchanged. For now, all i did was write a strategy and run the framework

---

## 2020-12-02 19:46:54 - general channel

**liam**

Happy to add another channel but it’s a bit of a hassle as I have to invite everyone. Don’t think anyone minds answering the beginners questions assuming it’s not shown in the examples or docs 

---

## 2020-12-02 19:25:10 - general channel

**Artur Gräfenstein**

I would suggest someone (who has the rights [@U4H19D1D2](@U4H19D1D2)) create a #beginners channel. And every time a question is asked that fits the rubric, I or someone who speaks native English can copy and pin it. So the initial effort is very low and it is filled up over time. Beginners can also ask their questions there and anyone who is annoyed by the beginner questions simply does not join the channel.

---

## 2020-12-02 16:47:38 - issues channel

**birchy**

The new server is only a temporary setup for testing, but longer term I guess I'll need to upgrade production server to Ubuntu 20+ anyway.

---

## 2020-12-02 16:39:37 - general channel

**Chris**

Maybe a #beginners channel with a pinned post would be good, could be used for the more simple questions too

---

## 2020-12-02 16:36:36 - issues channel

**birchy**

Obviously, you're correct _again_ [@UBS7QANF3](@UBS7QANF3) :grinning:

```$ uname -v

#30~18.04.1-Ubuntu SMP Tue Oct 20 11:09:25 UTC 2020



$ apt-cache policy openssl

openssl:

  Installed: 1.1.1-1ubuntu2.1~18.04.6

  Candidate: 1.1.1-1ubuntu2.1~18.04.6

  Version table:

 *** 1.1.1-1ubuntu2.1~18.04.6 500

        500 [http://eu-west-1.ec2.archive.ubuntu.com/ubuntu](http://eu-west-1.ec2.archive.ubuntu.com/ubuntu) bionic-updates/main amd64 Packages

        500 [http://security.ubuntu.com/ubuntu](http://security.ubuntu.com/ubuntu) bionic-security/main amd64 Packages

        100 /var/lib/dpkg/status

     1.1.0g-2ubuntu4 500

        500 [http://eu-west-1.ec2.archive.ubuntu.com/ubuntu](http://eu-west-1.ec2.archive.ubuntu.com/ubuntu) bionic/main amd64 Packages

------------------

$ uname -v

#31-Ubuntu SMP Fri Nov 13 11:40:37 UTC 2020



$ apt-cache policy openssl

openssl:

  Installed: 1.1.1f-1ubuntu2

  Candidate: 1.1.1f-1ubuntu2

  Version table:

 *** 1.1.1f-1ubuntu2 500

        500 [http://eu-west-1.ec2.archive.ubuntu.com/ubuntu](http://eu-west-1.ec2.archive.ubuntu.com/ubuntu) focal/main amd64 Packages

        100 /var/lib/dpkg/status```

OpenSSL 1.1.1f is the one that's failing

---

## 2020-12-02 15:26:13 - issues channel

**birchy**

[@U4H19D1D2](@U4H19D1D2) Just had this on a Flumine fresh install on a Lightsail instance:

```File "/home/ubuntu/.local/lib/python3.8/site-packages/betfairlightweight/endpoints/login.py", line 53, in request

    raise APIError(None, exception=e)

betfairlightweight.exceptions.APIError: None

Params: None

Exception: [('SSL routines', 'SSL_CTX_use_certificate', 'ca md too weak')]```

Seems to be OpenSSL related: [https://stackoverflow.com/questions/52218876/how-to-fix-ssl-issue-ssl-ctx-use-certificate-ca-md-too-weak-on-python-zeep|StackOverflow Link](https://stackoverflow.com/questions/52218876/how-to-fix-ssl-issue-ssl-ctx-use-certificate-ca-md-too-weak-on-python-zeep|StackOverflow Link)

OpenSSL version 1.1.1

Flumine version 1.14.12

BetfairLightWeight version 2.10.2



Working fine on my production instance which has exactly the same setup and same certs?



Only difference I can find so far is:

```Linux 5.4.0-1029-aws #30~18.04.1-Ubuntu SMP

Linux 5.4.0-1029-aws #30-Ubuntu SMP```

Ubuntu 18.04 working fine, Ubuntu 20.04 is throwing the error.

---

## 2020-12-02 11:25:32 - general channel

**Thomas JAMET**

Hello everyone, I am new to sport betting, looking into tennis events. The first step for me is to gather historical information on tennis matches to feed into a model. My objective is to gather 20 years of data. I am scraping a few web-sites but I am getting blocked by Captchas. Did anyone resolve this scenario?

I am currently considering developing a Chrome extension to help facilitate the scraping while giving human access to the Captcha page. Any suggestion welcome. Thanks!

---

## 2020-12-01 21:59:13 - general channel

**Lennart**

I appreciate all the help btw, I'm still very new to this (despite having joined the slack a long time ago)

---

## 2020-11-30 10:47:29 - general channel

**Chris**

Beginners question, probably more Python related than bflw, as things stand I generally run scripts as they are to do what I want, and any processes that I need as "daemons" are running in loops, or via cron, now I've moved over to the streaming API I'd like to understand how I can have the streams running and then access the data from external other scripts (I currently have them running via a supervisord process which is a loop that connects to the stream and writes all of the market books to MySQL) I then query the MySQL database in my other Python scripts, I'd like to miss out that step if possible and just query the stream directly from my other python scripts, anyone have any pointers?

---

## 2020-11-29 17:36:42 - issues channel

**Aaron Smith**

Thanks. I m a little hesitant with overwriting stuff in the flumine framework for now, as i want to keep it as close to the original as i can to not have to rethink everything that i tweaked whenever i m getting some error. When i feel more comfortable with the framework, that may change.

Regarind the order: It must have been an order created by flumine and it must ve been a matched order, as i was only using Fill_or_Kill orders. It is only a handful of orders that are repeaditly logged. The warnings also occured on the first time i started flumine (so before any restart), looping over 3 diffrent orders

---

## 2020-11-29 17:30:46 - random channel

**Newbie99**

I've been getting this all day and I can't figure it out, as it appears to occur when _process_close_market runs (which I haven't changed from the pip install of flumine)?



```  File "/home/ec2-user/trading/env/lib64/python3.7/site-packages/flumine/flumine.py", line 44, in run

    self._process_close_market(event)

  File "/home/ec2-user/trading/env/lib64/python3.7/site-packages/flumine/baseflumine.py", line 264, in _process_close_market

    market.blotter.process_closed_market(event.event)

  File "/home/ec2-user/trading/env/lib64/python3.7/site-packages/flumine/markets/blotter.py", line 86, in process_closed_market

    for runner in market_book.runners:

AttributeError: 'dict' object has no attribute 'runners'```

---

## 2020-11-29 16:56:38 - issues channel

**Aaron Smith**

Hello folks! I m having an error i currently cant explain, its certainly not an issue of flumine itself, but maybe one of you guys can help me out anyway :slightly_smiling_face:

I keeps getting the following warning:

```{"asctime": "2020-11-28 21:23:28,772", "levelname": "WARNING", "message": "Order 217999225444 not present in blotter", "bet_id": "217999225444", "market_id": "1.176099484", "customer_strategy_ref": "ip-xxx-xx-xxx-xx", "customer_order_ref": "stratname-138258912423034860"}```

I dont see how i managed to get orders which are not in the blotter, as with markets.place_order any order should automatically be added to the blotter?

Also on a complete diffrent topic: Sometimes i get prints and [http://logging.info|logging.info](http://logging.info|logging.info)() outputs in the console output, but mostly not. How can i choose which kind of outputs i want to get in my console?

Its is entirely possible i m overlooking the obvious, i m new to coding (corona made me do it :smile: )

Thanks to anyone taking the time to help me :slightly_smiling_face:

---

## 2020-11-25 12:47:46 - general channel

**A**

Blimey. Ok yeah I think I've connected to a market stream inherently through using Flumine. What approach would you recommend for storing the market catalogue? Is the some form of side worker? Stored in memory or a DB? Quite new to the concepts and how the system is put together (I'm an iOS dev by trade) - should be good once I get the basics

---

## 2020-11-24 22:55:38 - general channel

**A**

Hello all. Just getting started with Flumine and BFLW, really pleased to have stumbled on this project and community. Looking to see if I can swing trade the horses. First question (been bugging me for a while), what does NG stand for in API-NG?!

---

## 2020-11-21 16:07:29 - strategies channel

**Alessio**

:smile: no prob i was just trying to help but i am also very beginner

---

## 2020-11-19 12:22:45 - general channel

**Artur Gräfenstein**

[@UFTBRB3F1](@UFTBRB3F1) do you use it with UI? Im Building a Electron Application for win and mac where you need to setup your strategie. So nodejs is really helpful but it musst be very fast as well!

---

## 2020-11-19 12:19:27 - general channel

**Artur Gräfenstein**

[@UUE6E1LA1](@UUE6E1LA1) Thank you! My problem is, im experienced in nodejs, but Python is new to me! So it would take a long time to learn.

---

## 2020-11-18 13:16:07 - general channel

**birchy**

In Flumine, if you have a strategy running and at some point in the future you decide you're finished with this market, is there a way to unsubscribe before market closure? This is currently for backtesting but will also be useful when live. More specifically, if code in `check_market_book()` identifies the market is no longer required, what's the best way to skip to the next market file? I know we can use `market_filter` in the framework setup, but sometimes the market changes after subscription, i.e. we've hit our exposure limit, too many runners withdrawn, etc.

---

## 2020-11-14 19:55:03 - issues channel

**Ryan Clapham**

Hi all, very new to the betfair api. I was wondering if someone could point be in the right direction. I have looked everywhere on the betfairlightweight docs but can not see anywhere it says to display odds that are available to take. Any help is much appreciated.

---

## 2020-11-12 09:15:14 - general channel

**liam**

Here is a good start, scroll down for example in how to include a library, also see [https://liampauling.github.io/flumine/advanced/#logging|here](https://liampauling.github.io/flumine/advanced/#logging|here) to setup the jsonlogger

---

## 2020-11-09 08:30:06 - issues channel

**Jorge**

Hi guys, I am not able to pip install betfairlightweight[speed]... I get the error:

• _maturin failed_

      _Caused by: Cargo metadata failed. Do you have cargo in your PATH?_

Can anyone help me?

---

## 2020-11-07 15:27:27 - strategies channel

**birchy**

[@U4H19D1D2](@U4H19D1D2) I'm used to placing only a handful of bets per market, so thought I'd already "upgraded". :grinning: 

How many bets per market would be normal? The strategy is for inplay GB horse racing, an area that is totally new to me at present.

---

## 2020-11-05 09:02:00 - random channel

**D C**

You guys make me feel like a dinosaur. Everyone will have different approaches and that will depend on their skill set and the scale they are working at. I only do horses right now and I just use single C++ applications that run acccording to rules in config files so I can run multiple instances. It is not ideal but for the scale I am working at this is sufficient (don't get me wrong, it is not trivial stuff, but it is all self-contained). Coming from a desktop development background, hearing how others are working really makes me feel like I am working in the dark ages (WTF is django and why so many APIs ?). Would love to see a presentation one day (suitable for old-school dunces like me) from one of the larger scale guys like [@U4H19D1D2](@U4H19D1D2) or [@UBS7QANF3](@UBS7QANF3) or anyone else about their setup and WHY they work that way. Might help drag me out of my neo-luddite bubble.

---

## 2020-11-01 14:09:49 - random channel

**D C**

Has anyone had to regenerate their SSL cert and key files? I upgraded my linux install recently and my nodejs stuff no longer works unless I roll back to an old nodejs version. The issue is inside openssl I think and the error is "*ca md too weak*". Some research suggests that this is because my cert and key files were generated with too old a version of SSL and this now causes issues with later versions of openssl. Is this something that you guys have had to do from time to time? For now it is not an issue overall, but I dont want to be running old versions of node for too long just to keep things going.

---

## 2020-10-30 11:20:02 - issues channel

**Misha**

So no idea what is different, because I have logged every error in all my systems for the last 3 years, and I can confirm that October 21 is the first time I have ever seen it

---

## 2020-10-27 17:07:25 - general channel

**liam**

Originally used ujson as it is quicker than the standard library however it has become very unstable with the new maintainers. Moved to orjson as it was all the rage but that can be tricky to install and the latest release has issues with some versions of python. So it is now setup to use orjson if installed and fall back on the standard library 

---

## 2020-10-27 16:55:43 - general channel

**jhaa**

do you just do pip install betfairlightweight -U on the live system or is there anything that will break?

---

## 2020-10-26 09:38:58 - general channel

**liam**

[https://github.com/liampauling/betfair/blob/master/HISTORY.rst#291-2020-10-26|2.9.1](https://github.com/liampauling/betfair/blob/master/HISTORY.rst#291-2020-10-26|2.9.1) released, historic improvement ([@UBS7QANF3](@UBS7QANF3)) and I have moved all C/Rust libraries to a speed install

```pip install betfairlightweight[speed]```

---

## 2020-10-20 16:51:49 - issues channel

**river_shah**

I am ruing the day I upgraded python to 3.9 from 3.7. all sorts of random issues popping up with basic installs (not just bflw and flumine related)

---

## 2020-10-20 16:14:56 - issues channel

**river_shah**

stack overflow coming back with minimal suggestions. wondering if anyone has any ideas:

```➜  / pip install flumine

Collecting flumine

  Using cached flumine-1.14.0-py3-none-any.whl (95 kB)

Collecting betfairlightweight==2.9.0

  Using cached betfairlightweight-2.9.0-py3-none-any.whl (60 kB)

Collecting python-json-logger==2.0.0

  Using cached python-json-logger-2.0.0.tar.gz (8.2 kB)

Collecting tenacity==5.0.3

  Using cached tenacity-5.0.3-py2.py3-none-any.whl (38 kB)

Collecting requests

  Using cached requests-2.24.0-py2.py3-none-any.whl (61 kB)

Collecting orjson==3.4.0; sys_platform == "darwin" or sys_platform == "linux"

  Using cached orjson-3.4.0.tar.gz (655 kB)

  Installing build dependencies ... done

  Getting requirements to build wheel ... done

    Preparing wheel metadata ... error

    ERROR: Command errored out with exit status 1:

     command: /usr/local/bin/python3.9 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pip/_vendor/pep517/_in_process.py prepare_metadata_for_build_wheel /var/folders/0v/x5pftd6d6_v9ylh2rnjsn8f80000gn/T/tmp8bxpoz4e

         cwd: /private/var/folders/0v/x5pftd6d6_v9ylh2rnjsn8f80000gn/T/pip-install-kfkcy84b/orjson

    Complete output (13 lines):

    :boom: maturin failed

      Caused by: Cargo metadata failed. Do you have cargo in your PATH?

      Caused by: Error during execution of `cargo metadata`: error: failed to run `rustc` to learn about target-specific information



    Caused by:

      process didn't exit successfully: `rustc - --crate-name ___ --print=file-names -Z mutable-noalias --crate-type bin --crate-type rlib --crate-type dylib --crate-type cdylib --crate-type staticlib --crate-type proc-macro --print=sysroot --print=cfg` (exit code: 1)

      --- stderr

      error: the option `Z` is only accepted on the nightly compiler





    Checking for Rust toolchain....

    Running `maturin pep517 write-dist-info --metadata-directory /private/var/folders/0v/x5pftd6d6_v9ylh2rnjsn8f80000gn/T/pip-modern-metadata-h04wo8ou --interpreter /usr/local/bin/python3.9 --manylinux=off --strip=on`

    Error: Command '['maturin', 'pep517', 'write-dist-info', '--metadata-directory', '/private/var/folders/0v/x5pftd6d6_v9ylh2rnjsn8f80000gn/T/pip-modern-metadata-h04wo8ou', '--interpreter', '/usr/local/bin/python3.9', '--manylinux=off', '--strip=on']' returned non-zero exit status 1.

    ----------------------------------------

ERROR: Command errored out with exit status 1: /usr/local/bin/python3.9 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pip/_vendor/pep517/_in_process.py prepare_metadata_for_build_wheel /var/folders/0v/x5pftd6d6_v9ylh2rnjsn8f80000gn/T/tmp8bxpoz4e Check the logs for full command output.```



---

## 2020-10-20 10:51:44 - general channel

**D**

I have used a layer for BetfairLightweight. I didn't use docker, I created it on an EC2 instance. Using this to install locally before creating the zip file for upload: pip3 install betfairlightweight -t ./lambda --upgrade

---

## 2020-10-19 22:34:35 - general channel

**Theo Caplan**

Hi - new to this so apologies if I have stupid questions.



When I have a &lt;RunnerBook&gt; object, the `.ex` attribute doesn't seem to return anything, even though it looks like it should return an &lt;ExchangePrices&gt; object. Any idea why this might be?

---

## 2020-10-17 23:28:09 - issues channel

**AP**

I am deploying a function app (serverless) on Azure and got the following error related to orjson when deploying:



```Collecting orjson==3.4.0; sys_platform == "darwin" or sys_platform == "linux" (from betfairlightweight-&gt;-r requirements.txt (line 14))

  Downloading [https://files.pythonhosted.org/packages/ca/ab/cece004aaae000741d059dcb9b1f6f62a6a5ecb2e11b3ecca09e6180c327/orjson-3.4.0.tar.gz](https://files.pythonhosted.org/packages/ca/ab/cece004aaae000741d059dcb9b1f6f62a6a5ecb2e11b3ecca09e6180c327/orjson-3.4.0.tar.gz) (655kB)

  Installing build dependencies: started

  Installing build dependencies: finished with status 'done'

    Complete output from command python setup.py egg_info:

    Traceback (most recent call last):

      File "&lt;string&gt;", line 1, in &lt;module&gt;

      File "/opt/hostedtoolcache/Python/3.6.12/x64/lib/python3.6/tokenize.py", line 452, in open

        buffer = _builtin_open(filename, 'rb')

    FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pip-install-muey9qtb/orjson/setup.py'```

---

## 2020-10-16 16:04:49 - general channel

**Mai**

Hello all! New to betfairlightweight (and betfair) and it's great to find this community. Thanks to the developers for making it open!

---

## 2020-10-16 11:05:01 - general channel

**Rob (NZ)**

any good resources I could read up on how to run the flumine (still a python newb) is it something i can pip install like lightweight

---

## 2020-10-15 16:18:55 - general channel

**Seabass**

Hi, I'm a beginner with betfair but familar with tick trading data. I'am trying to create essentially a time and sales file using the Pro historical data. But when I merge the order book data and the time and sales file I generate, the results look a little strange. Generally, you can see the exact traded size removed from the order book. But occasionaly, there seems to be a trade that was adjusted later on (size doesn't match order book) and occasionally I see exactly half of the reported trade size being removed from the book. To calculate the trades I just take the difference from the current trd cache and the newest trd cache. What is the correct way to calculate the amount that was traded? And am I overlooking something in my calculation?

---

## 2020-10-15 13:56:14 - random channel

**D C**

So Dell customer services tell me that the XPS 13 range can be purchased with Ubuntu 20.04 pre-installed. Looks mighty thin and have no idea what this thunderbolt port 3 hardware is but I guess I will need a hub of some kind for peripherals. Nice to know that they still do linux builds though so I think I will go down this route. Thanks to all for helpful suggestions.

---

## 2020-10-15 13:29:21 - random channel

**Jonjonjon**

From Ubuntu, do I just log into steam, and then click the button to install it? Do I need to worry about security? This PC is my work machine for BFLW. I don't want to break it.

---

## 2020-10-15 09:44:14 - random channel

**Chris**

Yeah, would also agree, unless you've got some specific pieces of hardware you're looking to utilize with the laptop the last 2-3 I've purchased with Windows installed I've had no problems with installing Ubuntu/Fedora on them and no problems with any hardware working on it, bluetooth/wifi etc. assume are the biggest concerns

---

## 2020-10-15 09:33:41 - random channel

**D C**

A laptop is just a laptop yes. I assumed it would be clear but what I mean is a laptop that comes pre-installed with linux on it and in which all hardware is chosen such that it will run without issue on linux. Not many places seem to do this, hence the question.

---

## 2020-10-13 10:31:37 - issues channel

**Lee**

orjson strikes again

```       Collecting orjson==3.4.0; sys_platform == "darwin" or sys_platform == "linux" (from betfairlightweight==0.0.0b21-&gt;-r /tmp/build/requirements/base.txt (line 4))

       Downloading [https://files.pythonhosted.org/packages/ca/ab/cece004aaae000741d059dcb9b1f6f62a6a5ecb2e11b3ecca09e6180c327/orjson-3.4.0.tar.gz](https://files.pythonhosted.org/packages/ca/ab/cece004aaae000741d059dcb9b1f6f62a6a5ecb2e11b3ecca09e6180c327/orjson-3.4.0.tar.gz) (655kB)

       Complete output from command python setup.py egg_info:

       Traceback (most recent call last):

       File "&lt;string&gt;", line 1, in &lt;module&gt;

       File "/app/.heroku/python/lib/python3.7/tokenize.py", line 447, in open

       buffer = _builtin_open(filename, 'rb')

       FileNotFoundError: [Errno 2] No such file or directory: '/tmp/pip-build-29ykcrms/orjson/setup.py'

       

----------------------------------------

       Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-29ykcrms/orjson/```



---

## 2020-10-09 20:46:16 - random channel

**Jonjonjon**

When I run the flumine integration tests for the first time after starting Pycharm, I need to change the working directory from:



`/home/jon/PycharmProjects/flumine/`



to



`/home/jon/PycharmProjects/flumine/tests`



How can I top having to do this serveral times per day?

---

## 2020-10-08 19:44:38 - random channel

**river_shah**

[@UU1URJ8L8](@UU1URJ8L8) the problem setup you have would better be seen as a multivariate markowitz portfolio optimisation problem. if leverage is allowed and there is guaranteed payoffs then both multivariate kelly or markowitz would say to invest to max of allowed leverage to get the risk on. regarding doing negative ev trades, for bets or assets with known covariance matrix, it is very much permissible (infact recommended) to do negative ev trades to maximize risk reward. please notice in equations on page 4 and 5 that there is absolutely no requirement to clamp weights to 0 or negative for assets where asset return is negative ([https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote14.pdf](https://ocw.mit.edu/courses/mathematics/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/lecture-notes/MIT18_S096F13_lecnote14.pdf))

---

## 2020-10-03 00:37:41 - general channel

**Dave**

FWIW - I tried republishing market data internally over zmq pub/sub and latency impact is negligible. So if you wanted a setup where you had say, one process per market, then you can't use a dedicated streaming session per market if you plan on trading more than 10 markets concurrently (for the reason Misha mentioned above). But republishing internally is a way around that, and the added latency is dwarfed by external network latency. Decided not to opt for Redis now given zmq is sufficient

---

## 2020-09-24 21:50:49 - strategies channel

**D C**

[@UFTBRB3F1](@UFTBRB3F1) I might be sending you up the garden path here, but the full platinum subscription to proform might allow you to export the data. I have used it in the past although never tried the export so I don't even know if it is possible. Downside is I think it is only installable on windows but that may not be a problem for you. I know a lot of people rate the data very highly but it might be overkill if all you want is basic result data.

---

## 2020-09-24 09:33:41 - general channel

**liam**

Yep but flumine will work off that cancel event and may reset -&gt; place new orders dependant on how it has been setup

---

## 2020-09-17 15:48:55 - random channel

**Peter**

Similar here. Used to run build development machines for my web development agency. We wanted fast processors and lots of RAM, but didn't need high end graphics and the manufacturers didn't really offer machines like that (as well as charging premium prices for decent processors). So I'd buy cheap motherboards and small form factor cases, install high end processors and RAM and mix in Ubuntu. At the time it made for really-cost effective and powerful development machines. So fast forward to today and I still have a few around which have now been repurposed to run python scripts processing or analysing sports data (often for days at a time) served to them by a shared fast 4TB disk drive onto which data stored at S3 is periodically downloaded. Next step is to convert some of those scripts to Flumine.

---

## 2020-09-17 10:17:47 - general channel

**D C**

I have some node scripts that I use that allows me to extract profits by event type/strategy ref and pattern match by event names so I can drill down very easily. I use the event type ID one for daily P&amp;L. I don't use bflw either but its just basic API listClearedOrders operation so you should be able to code it yourself easily. I can give you my scripts if you want but its rather clunky (6 CLI args) and just dumps to console so you might be better off writing one as part of your own setup.

---

## 2020-09-17 10:13:13 - general channel

**Jonjonjon**

At the end of the day, does your actual account balance look correct? I know this is a stupid question, but my whole setup is a mess and some of my stuff isn't in bflw, so it isn't that easy working out my total profit/loss manually.

---

## 2020-09-15 08:38:40 - general channel

**D C**

[@U016TGY3676](@U016TGY3676) don't worry - even I have heard of this one so it's not a secret. I was actually going to write a tool to parse the BHA twitter account for up to date NR but that link Liam just provided. Not to do what people do with the NR to create value on another runner, but to detect last minute ones so my inplay bots ignore the pulled runner. Seems to happen a fair bit right at the last minute recently and too soon for BF to actually pull it from the market. This is one area that my prehistoric desktop setup IS a help because I can manually deselect a pulled runner just after the off. Trouble is I want to be outside doing the garden not watching the screen all afternoon.

---

## 2020-09-14 17:58:02 - issues channel

**jhaa**

ok i just uninstalled ujson so it defaults to the slow python version

---

## 2020-09-14 17:56:53 - issues channel

**liam**

or uninstall orjson if you are going to be passing in numpy types

---

## 2020-09-13 13:31:40 - general channel

**D C**

Cheers [@UBS7QANF3](@UBS7QANF3) . That is a great concise explanation. So could I effectively just use EC2 as it if were a remote linux server and install whatever I need on it and go from there?

---

## 2020-09-08 08:44:46 - issues channel

**liam**

And [https://betfairlightweight.slack.com/archives/C4HL6EZTQ/p1599033634033600|2.8.0b](https://betfairlightweight.slack.com/archives/C4HL6EZTQ/p1599033634033600|2.8.0b) or uninstall ujson

---

## 2020-09-03 10:46:28 - general channel

**Taking Value**

Thanks for the input all. Will probably spend most of the day considering what to do. The Amazon S3 option is a curve ball, didn't know anything about it before today. I had just assumed everyone would be operating an SQL or NoSQL database with a self built GUI on the front. At least I have some new topics to research, always fun.

---

## 2020-09-02 10:16:51 - general channel

**liam**

I store all streaming data in AWS s3 (object storage) and then use AWS rds for db, all managed and easy to setup with terraform

---

## 2020-09-01 09:18:53 - general channel

**Mathias Tejs**

Depending on your setup (e.g. if you're jobs are in python), celery can be a good choice. For instance, it's got flower for monitoring job status in a GUI out of the box, and it handles automatic restart on errors, storing task results and so on.

---

## 2020-08-29 19:14:34 - general channel

**birchy**

Yeah, I've never needed to make any python code installable before, but just had a quick Google and it looks like the best way would be to create a single "botting" venv for all bots and then `python setup.py install --user` for my package? Or do you use `pip` in local mode?

This? [https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs)

---

## 2020-08-29 18:52:09 - general channel

**Mo**

As for how to make it installable, I’d suggest just looking at the setup.py file in a package like bflw

---

## 2020-08-29 18:48:23 - general channel

**birchy**

The only downside I can see with making it an installable package is that I'd have to recompile every time I edit the botpkg, although that's not frequent. My `botpkg/__init__.py` file looks like this:

```import os

import botpkg.betfair.api

import botpkg.betfair.racecard_api

import botpkg.betfair.price_mod

import botpkg.logger

import botpkg.testbed

import botpkg.trading

import botpkg.compile

import botpkg.filing

import botpkg.utils

import botpkg.credentials



path = os.path.dirname(os.path.dirname(__file__))

api = botpkg.betfair.api.API()

pricemod = botpkg.betfair.price_mod

logger = botpkg.logger.Logger()

testbed = botpkg.testbed.TestBed()

trading = botpkg.trading.Trading()

racecard_api = botpkg.betfair.racecard_api.API()

compile = botpkg.compile.Compile()

filing = botpkg.filing.Filing()

utils = botpkg.utils.BotFunctions()```

The main reason I took that route is because I like minimal code and wanted to avoid having lots of imports at the top of each bot. With this method, each bot only needs `import botpkg` and everything becomes available. I know it's a bit weird, but it's also very convenient. Obviously, that is the way I do things in my own library, but now I'm looking at bflw/flumine, I'm researching the best way to implement something similar.

Regarding making the package installable, which method do you recommend?

---

## 2020-08-27 10:32:36 - random channel

**birchy**

[@U4H19D1D2](@U4H19D1D2) Excellent work! Will the updates be picked up by `pip` `install` `Flumine --upgrade`, or is it better to git pull the source?

---

## 2020-08-26 20:42:58 - random channel

**mlpanda**

Hey [@U4H19D1D2](@U4H19D1D2), I have a couple of questions on using Flumine for tennis:



1. Is there an easy way to get all country_codes to get all matches rather than me passing a wikipedia list of all I can find?

2. Is there any functionality which makes it easy to fetch scores data? I'm aware that you have implemented two scores endpoints (thanks for highlighting this [@UBS7QANF3](@UBS7QANF3)): [https://betfairlightweight.slack.com/archives/C4HL6EZTQ/p1597749400063800](https://betfairlightweight.slack.com/archives/C4HL6EZTQ/p1597749400063800) 

       My current thought on implementation is to find the `eventid` the first time a given market enters `process_market_book()` and then afterwards try both endpoints to get scores, but would of course be happy if I didn't have to reinvent this myself :wink:

  3.  Is it possible to determine whether it's a match involving men or women from the scores endpoints?

---

## 2020-08-21 18:52:02 - general channel

**john walsh**

Thank you for that.  When I run your code pandas does not automatically print out the dataframes and I have to print them.  When I do that with your code it does not produce the line "48 English Premier League 10932509" but the whole list as per yours after that entry.  I am using Python 3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)] and I have installed Pandas 1.0.5

---

## 2020-08-20 00:23:53 - issues channel

**Chris**

*Context:* New to using this package. Have a hopefully quick question regarding recording market data in a manner that is consistent with the Backtesting and Paper Trading components of Flumine.



*Narrow question*: Does anyone have the MarketRecorder data file that is referenced in the marketrecorder.py file located in the flumine examples? ([https://github.com/liampauling/flumine/blob/69d68904b4ae0c8ba3c0d60991c3a6a38066040d/examples/marketrecorder.py#L8](https://github.com/liampauling/flumine/blob/69d68904b4ae0c8ba3c0d60991c3a6a38066040d/examples/marketrecorder.py#L8))



*Broader question*: What is the standard data interface to ensure backtesting/paper trading works with Flumine?

An interface is alluded to in a few different places. One example is in the following code snippet at the following link:



...

trading = betfairlightweight.APIClient("username")

client = clients.BetfairClient(trading, paper_trade=True)

framework = Flumine(client=client)



strategy = ExampleStrategy(

    market_filter={"markets": [_*"/tmp/marketdata/1.170212754"*_]}

)

framework.add_strategy(strategy)

...



[https://liampauling.github.io/flumine/quickstart/#backtesting](https://liampauling.github.io/flumine/quickstart/#backtesting)

---

## 2020-08-18 00:33:56 - issues channel

**qwerty.nat**

Just did a pip install flumine. filled in my login details in the example market recorder application to test all is ok.

`trading = betfairlightweight.APIClient(username="user",password="pass",app_key="slkfj", certs="/path/to/cert",lightweight=True)`

It fails after running for about 30 seconds,

`Traceback (most recent call last):`

  `File "marketrecorder.py", line 36, in &lt;module&gt;`

    `framework.run()`

  `File "/home/nathan/.local/lib/python3.8/site-packages/flumine/flumine.py", line 23, in run`

    `self._process_market_catalogues(event)`

  `File "/home/nathan/.local/lib/python3.8/site-packages/flumine/baseflumine.py", line 200, in _process_market_catalogues`

    `market = self.markets.markets.get(market_catalogue.market_id)`

`AttributeError: 'dict' object has no attribute 'market_id'`

If i set lightweight to False in the APIClient it all works without any error.

---

## 2020-08-15 08:06:20 - general channel

**Mo**

Off the top of my head, with `awscli` OS package installed and configured



```aws s3 sync s3://&lt;bucket_name&gt;/&lt;path_to_directory_containing_zip_files/ /tmp/betfair/

find -type f /tmp/betfair -exec sh "unzip {} ; rm {}" \;

find -type f /tmp/betfair -exec bzip2 {} \;

aws s3 sync --delete /tmp/betfair/ s3://&lt;bucket_name&gt;/&lt;path_to_directory_containing_zip_files/```

I wouldn't run the last command - which will delete everything in the S3 directory that now doesn't exist in /tmp/betfair - without checking you're happy with what /tmp/betfair contains

---

## 2020-08-07 12:01:18 - strategies channel

**D C**

I should probably add [@UQL0QDEKA](@UQL0QDEKA) that I am most likey using the least advanced setup and least optimal execution. My stuff is currently running inside a Qt GUI application running on Linux on my home desktop with CPU time wasted on such frivolous things as a real time GPS render tool and other unecessary things. Once I make the switch to headless running on AWS or similar I would be hoping that the profitability increases as there are SO many optimisations to potentially make.

---

## 2020-08-06 12:07:10 - general channel

**Misha**

My advice is to keep it as simple as you can. You only ever learn from experience so it isn't till you actually get going that you start to get an idea of what you need. The syndicates making money have surprisingly simple setups beyond using hosted servers (none of the ones I worked for used AWS services at the time). I know because I ran a few of them. It's the model that makes the money, and the operational system can increase the profits (but can never overcome a poor model)

---

## 2020-08-06 11:17:05 - general channel

**Twatter**

Flumine setup and use sounds great - might sound basic for a lot of people but would be great for newbies like myself. So far, although you guys recommended to start plugging my strategy and stuff into flumine, i've started using trying to do it all in betfair lightweight, but still at the pre-requisite stages of simply grabbing market data and prices that I need and trying to analyse them. The way I see it is that since BFLW is so close to the Betfair API, it's giving me a great understanding of how the Betfair API itself works and how it returns data, and then I can look at how Flumine then wraps more of the trading and strategy around BFLW..

---

## 2020-08-06 11:13:25 - general channel

**Twatter**

Haha - My infrastructure so far is a laptop. With internet. And power supply. Sometimes use a mouse when at a desk. Still putting together just the very basics of grabbing market prices on horses for the strategy I need. Not even sure whether the strategy I use will translate into Betfair markets as it depends on how efficient all the pricing is inter market. It's all an interesting learning experience though so far as first time properly using Betfair APIs etc

---

## 2020-08-06 11:10:45 - general channel

**liam**

I am happy to do one on either flumine setup/use or future/roadmap if there is interest

---

## 2020-08-03 11:49:19 - general channel

**Lee**

slightly odd, 1.10.2 was on pypi 10mins ago

```$ pip install flumine==1.10.2

ERROR: Could not find a version that satisfies the requirement flumine==1.10.2 (from versions: 0.1.1, 0.1.2, 0.2.0, 0.2.2, 0.2.3, 0.3.0, 0.5.0b0, 0.5.1b0, 0.5.2b0, 0.5.3b0, 0.6.0, 0.6.1, 0.7.0, 0.8.0, 0.8.1, 0.9.0, 1.0.0b1, 1.0.0b2, 1.0.0b3, 1.0.0b4, 1.0.0b5, 1.0.0b6, 1.0.0b7, 1.0.0, 1.1.0, 1.2.0, 1.3.0, 1.4.0, 1.5.0, 1.5.1, 1.5.2, 1.5.3, 1.5.4, 1.5.5, 1.5.6, 1.5.7, 1.6.0, 1.6.1, 1.6.2, 1.6.3, 1.6.4, 1.6.5, 1.6.6, 1.6.7, 1.6.8, 1.7.0, 1.8.0, 1.8.1, 1.8.2, 1.9.0, 1.9.1, 1.9.2, 1.9.3, 1.10.0, 1.10.1)```

---

## 2020-08-03 08:40:07 - general channel

**liam**

in regards to your setup do you close anything older than 3 and create new? Do you then take the hit on the first round trip or prime it first? (in regards to latency sensitive requests such as place/cancel requests)

---

## 2020-08-02 21:41:02 - issues channel

**birchy**

Not sure if it was intentional or just overlooked, but flumine utils.py is short on function comments. Would be good to make this more friendly for beginners. Also, are there any plans to add other simple functions such as vwap, sma, wom, etc?

---

## 2020-08-02 17:26:28 - strategies channel

**PeterLe**

[@U0128E7BEHW](@U0128E7BEHW) Just to add to your point and worth consideration for anyone new to strategies; I think that as you try and work towards the optimal and efficient bet to maximise value, you eventually reach a tipping point at which the p&amp;L starts to reverse (ie similar to a diminishing returns situation). So this is something to be aware of also. I also try and think about who's taking my bet on the other side and why they would do so. Very early on in my betfair career, I had a simple system that placed a back bet on certain triggers, and it lost money. I thought at the time, ok instead of backing Ill lay at the reverse price. We all know now that if only it was this simple :grinning: The problem is that when the lay would have been successful, you dont always get matched, but when the lay wasn't successful you almost always get matched.

---

## 2020-08-01 00:17:44 - general channel

**birchy**

True to my word...

I now have GitHub setup with a private repo. As you suggested, doing minor edits in the browser is fine for those occasional quick fixes. Regarding deployment on vps, I would prefer to only get the latest source when a bot is (re)started. The VPS is purely a deployment machine, so all edits will be done externally.

So I created a SSH key and loaded it into GitHub. I then ran a git clone from the VPS to download my source code ready for deployment. Bot deployed, slippers fitted, scrumpy poured. All good so far...

Following a new commit, I decide to restart a bot. Git clone fails due to folder existing already, so I delete the folder, git clone and start the bot.

It's all working as expected, however the git clone over ssh feels a bit hacky, particularly having to delete the local folder in order to allow a clone. Also, having to start ssh-agent service and then adding the key in order to connect to GitHub feels like a workaround given that I normally create a SSH config file and simply do "ssh lightsail" to gain access to the server.



Is there a nicer way of doing this?

---

## 2020-07-28 15:46:57 - issues channel

**Aaron**

uninstall and reinstall requests on your im assuming ubuntu EC2 instance. Few threads on SO indicate this may be the fix

---

## 2020-07-28 09:24:15 - issues channel

**liam**

[@U016TGY3676](@U016TGY3676) bflw is currently setup to use env vars and up to the user to handle how its used, I guess its personal preference but there is no reason you can't override the client to use a config file. It's probably a bit late in the day to move to using a config file only like aws which means we would have the added complication of handling both but open to thoughts

---

## 2020-07-27 11:32:16 - strategies channel

**D C**

With all this talk of milliseconds and latency, has anyone done a study of this in detail? I mean you will surely get different results due to thread/process scheduling times unless you are running things such that you have a process single connection using a blocking socket connection configured such that the process runs on a specific processor? I mean I know that people have multiple processors and cores etc but everything is subject to OS scheduling. I mean yesterday I was getting over 100ms delays (close to 200ms at one point) on the GPS feed as calculated from the FEED time (not the 'pt'). I had Firefox running too and once I closed that down the delay dropped to a steady 70ms. I imagine that some of the people here making larger profits are running setups that have minimal lag. Anyone looked at this kind of thing in depth, or can point out any flaw in my thinking on this matter?

---

## 2020-07-26 23:23:47 - general channel

**birchy**

I work as a PLC programmer in my full time job and we use Dropbox for everything, so I'm familiar with using it, which is why I replicated a similar setup with my own VPC.

I totally agree that I need to update my way of thinking and start using a proper version control system as I now have a lot more projects. For my needs, a centralised system seems to be the best fit.

All I need to do now is work out the easiest way to:

a) get Pycharm to automatically sync to subversion or similar when using my main dev machine

b) do simple edits/bug fixes from an Android device with automatic syncing

c) pull the code into my VPS and launch the bot. I normally use a script for this as I compile to pyc, copy to ~/ and launch, so I could potentially use that to pull the latest version before launching

d) be able to carry out minor edits from within the VPS when logged in via SSH

Does that sound feasible, or am I still pissing in the wind?

---

## 2020-07-26 22:18:31 - general channel

**Mo**

So I have copies of my GitHub repos checked out to a Dropbox folder and any changes I make to my working copies are automatically synced with Dropbox. 



I push my commits to GitHub about once a day to make sure my collaborators have access in case I get hit by a bus etc. Or I’ll push if the changes need to be deployed to production. 



Managing infrastructure with ansible means that the setup of my servers is described in code that can similarly be version controlled. Deploying trading code to production is a case of running ansible tasks that will pull the relevant code from GitHub. 

---

## 2020-07-26 17:33:04 - general channel

**birchy**

Have just setup AWS Lightsail and S3. Just wondering what everyone else does regarding their working environment? I've been using Tagadab and basically network mount a remote folder on my local machines and put all my source code into there. This allows me to pick up the source code from multiple machines/devices. Pycharm is OK with this setup as it's effectively a local drive. Sometimes I do quick edits from my phone via SSH and Nano. Are any of you doing something similar with S3? I'm currently investigating how to mount S3 as a network drive. Are there any known issues? Will also be looking at mounting the S3 in the Ubuntu instance on Lightsail to save having to SCP source code. Will be interesting to see how others setup their environments.

---

## 2020-07-26 17:23:28 - strategies channel

**birchy**

Thanks [@UBS7QANF3](@UBS7QANF3). It's not something I obsess about, more of a "nice to have". I was only testing the water as I'm new to the AWS setup and was wondering how it compared to Tagadab.

---

## 2020-07-26 09:39:31 - strategies channel

**Michael**

The GC is not keen on MSA because it can be abused to facilitate problem gambling and money laundering so BF are not that keen to give them out. It helps if you're well known to them and UK based. Bu yeah - for most people they're not of any function and just complicate your setup with a bunch of different user names and app keys.

---

## 2020-07-25 16:09:12 - strategies channel

**Mathias Tejs**

Hi all, thanks for letting me join the group :) I want to get into betting and I'm wondering if there are any resources (e.g. books, blogs, etc.) that you guys can recommend? I'm an "expert" in algorithms, software development, machine learning and probability theory but I know very little about the world of betting (and also very little about trading) - I'm only saying that to say that I'm not too interested in general programming books and so on :)



Another related newbie question: I'm especially interested in football (soccer) betting. My guess is that my biggest chance for betting profitably there would be through live betting (I want to bet 100% programmatically). Are there any live feed sources that you can recommend? I have saved up around 30k euro that I plan to risk on getting started - is that enough, or do you need a higher volume to avoid all of your winnings going to paying monthly live feed APIs? (I can see from the slack history that some of you guys are winning considerably more than that)

---

## 2020-07-22 20:10:58 - strategies channel

**birchy**

I've not used AWS before. Setup S3 last night and that wasn't as straight forward as I was expecting due to the plethora of options available.

---

## 2020-07-20 14:16:56 - random channel

**D C**

No problems overwriting the Windows install with fresh ubuntu? SSD no issue? Its been a long time since I did a fresh install - before SSDs were commonplace

---

## 2020-07-20 14:13:57 - random channel

**D C**

Can anyone recommend a standard laptop that will have no problems installing linux onto (mint specifically)? I am talking about something that I can roll up to PC world and purchase and have linux installed within a couple of hours without worry about hardware issues etc.  I usually use older machines for this purpose but my dev box needs a serious upgrade now.

---

## 2020-07-07 19:48:03 - general channel

**birchy**

Hi all,

I'm new to bflw/flumine but not new to betfair api/python. Have been running bots since around 2004 - back then I had VB6 and a carefully crafted web scraper. Here in 2020, and after using my own library ([http://BespokeBots.com|BespokeBots.com](http://BespokeBots.com|BespokeBots.com)) for many years, I've decided it's time to get to grips with this new-fangled streaming API malarkey. Was going to code my own library but there is no good reason for me to do so when [@U4H19D1D2](@U4H19D1D2) has already created this marvellous resource. I'm on a bit of a learning curve at present because Liam has written "modern" Python code, whereas mine is very old fashioned and only uses very basic implementations. Having said that, my simple library has served me well for many years and has more than paid for itself.



Moving forward, I've run a couple of the bflw/flumine examples (copy/paste code!) and have login/etc working as expected. Planning on mining some data initially to get familiar with the syntax, pitfalls, etc. Can anyone suggest the best way to go about mining data with this library? Also of interest, what format is required for backtesting?



Regarding data mining, has anyone considered combining data as a pooled group? i.e. if "N" people were all mining data, the combined efforts would help to eliminate those "missing" sections that we encounter when we lose connection. Also, if we were mining ALL available markets at a sensibly throttled speed, the combined data would achieve a much better granularity, simulating something close to what we would get if we were concentrating on specific markets at balls-out speeds. This would require a pre-agreed structure, but is easily solved if all members use the same framework. Is this do-able, or does it contravene some clause in Betfair's T&amp;C's?

---

## 2020-07-05 14:32:02 - general channel

**Mo**

As someone who is relatively new to the feed, it was amazing how many times a new piece of documentation suddenly materialised that contained critical information

---

## 2020-06-29 10:38:12 - issues channel

**Dylan**

Hey! fairly new to the project however, I'm getting a SUBSCRIPTION_LIMIT_EXCEEDED error, would the assumption be that my filters are too broad? What controls this?

```ERROR:betfairlightweight.streaming.listener:[Subscription: 1] SUBSCRIPTION_LIMIT_EXCEEDED: trying to subscribe to 345 markets whereas max allowed number was: 200

INFO:betfairlightweight.streaming.listener:[Subscription: 1]: FAILURE (1 connections available)



#main.py

market_filter = streaming_market_filter(

    event_type_ids=["7"], country_codes=["AU"], market_types=["WIN"]

)

market_data_filter = streaming_market_data_filter(

    fields=["EX_MARKET_DEF"], ladder_levels=3

)```

---

## 2020-06-26 21:00:11 - general channel

**Pete**

Hello everyone. I'm new here.

Sorry if this is an FAQ and I've missed it.

I'm new to Python. How do I satisfy myself that the Flumine/BFlightweight code doesn't share my credentials anywhere but with Betfair?

I'm not paranoid...just careful.

---

## 2020-06-20 18:17:03 - general channel

**gprokisch**

Sorry man.. For the silly question. I'm new to this betting world. This API still confusing me a bit.

---

## 2020-06-19 18:07:45 - strategies channel

**Stefan**

It was not so couple years back when I first heard about timeform api. If you think there is some value in forecast prices then just setup simple bot strategy and run it for couple days to see some results.

---

## 2020-06-17 17:06:26 - issues channel

**liam**

the fact you have cloned the bflw repo rather than installed it and running it inside the same repo could cause issues as well

---

## 2020-06-17 16:38:09 - issues channel

**Jono**

hey [@UBS7QANF3](@UBS7QANF3) ive been trying to use the example you gave a few scrolls up that uses smart_open but im having some problems using that too. ive tried "pip install smart_open" but cant seem to use the library

---

## 2020-06-17 13:36:47 - issues channel

**EJono**

I am trying to obtain selection ids from past matches of rugby matches etc through parsing a few months of historical data, downloaded via the basic plan. I was under the impression that betfairlightweight was the perhaps the optimal way to go about investigating previous data but I am having some problems operating directly on the downloaded data.tar files from betfair. I was curious if anyone knows what I should be doing in order to create a setup (in python) for retrieving information from these downloaded files either through utilising betfairlightweight or otherwise?



Any help is greatly appreciated

---

## 2020-06-15 16:42:38 - issues channel

**Peter**

`#!/bin/bash`



`yum install -y python37 python37-pip`

`yum install -y gcc gcc-c++ python3-devel ujson ciso8601 htop`



`pip3 install numpy pandas python-dotenv tenacity typing betfairlightweight flumine boto3 htop`

---

## 2020-06-15 14:37:50 - issues channel

**Sandy Caskie**

```ERROR: Command errored out with exit status 1:

  command: /Users/Sandy/anaconda3/bin/python /Users/Sandy/anaconda3/lib/python3.6/site-packages/pip install --ignore-installed --no-user --prefix /private/var/folders/1y/7v8fvfy51_sfdx_r21tgkq5h0000gn/T/pip-build-env-r8el7tjn/overlay --no-warn-script-location --no-binary :none: --only-binary :none: -i [https://pypi.org/simple](https://pypi.org/simple) -- 'setuptools&gt;=42' wheel 'setuptools_scm[toml]&gt;=3.4'

    cwd: None

 Complete output (41 lines):

 Traceback (most recent call last):

  File "/Users/Sandy/anaconda3/lib/python3.6/runpy.py", line 193, in _run_module_as_main

   "__main__", mod_spec)

  File "/Users/Sandy/anaconda3/lib/python3.6/runpy.py", line 85, in _run_code

   exec(code, run_globals)

  File "/Users/Sandy/anaconda3/lib/python3.6/site-packages/pip/__main__.py", line 19, in &lt;module&gt;

   sys.exit(_main())

  File "/Users/Sandy/anaconda3/lib/python3.6/site-packages/pip/_internal/cli/main.py", line 73, in main

   command = create_command(cmd_name, isolated=("--isolated" in cmd_args))

  File "/Users/Sandy/anaconda3/lib/python3.6/site-packages/pip/_internal/commands/__init__.py", line 96, in create_command

   module = importlib.import_module(module_path)

  File "/Users/Sandy/anaconda3/lib/python3.6/importlib/__init__.py", line 126, in import_module

   return _bootstrap._gcd_import(name[level:], package, level)

  File "&lt;frozen importlib._bootstrap&gt;", line 994, in _gcd_import

  File "&lt;frozen importlib._bootstrap&gt;", line 971, in _find_and_load

  File "&lt;frozen importlib._bootstrap&gt;", line 955, in _find_and_load_unlocked

  File "&lt;frozen importlib._bootstrap&gt;", line 665, in _load_unlocked

  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module

  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed

  File "/Users/Sandy/anaconda3/lib/python3.6/site-packages/pip/_internal/commands/install.py", line 24, in &lt;module&gt;

   from pip._internal.cli.req_command import RequirementCommand

  File "/Users/Sandy/anaconda3/lib/python3.6/site-packages/pip/_internal/cli/req_command.py", line 21, in &lt;module&gt;

   from pip._internal.req.constructors import (

  File "/Users/Sandy/anaconda3/lib/python3.6/site-packages/pip/_internal/req/__init__.py", line 11, in &lt;module&gt;

   from .req_file import parse_requirements

  File "/Users/Sandy/anaconda3/lib/python3.6/site-packages/pip/_internal/req/req_file.py", line 25, in &lt;module&gt;

   from pip._internal.req.constructors import (

  File "/Users/Sandy/anaconda3/lib/python3.6/site-packages/pip/_internal/req/constructors.py", line 28, in &lt;module&gt;

   from pip._internal.req.req_install import InstallRequirement

  File "/Users/Sandy/anaconda3/lib/python3.6/site-packages/pip/_internal/req/req_install.py", line 30, in &lt;module&gt;

   from pip._internal.operations.install.wheel import install_wheel

  File "/Users/Sandy/anaconda3/lib/python3.6/site-packages/pip/_internal/operations/install/wheel.py", line 10, in &lt;module&gt;

   import compileall

  File "/Users/Sandy/anaconda3/lib/python3.6/compileall.py", line 20, in &lt;module&gt;

   from concurrent.futures import ProcessPoolExecutor

  File "/Users/Sandy/anaconda3/lib/python3.6/site-packages/concurrent/futures/__init__.py", line 8, in &lt;module&gt;

   from concurrent.futures._base import (FIRST_COMPLETED,

  File "/Users/Sandy/anaconda3/lib/python3.6/site-packages/concurrent/futures/_base.py", line 381

   raise exception_type, self._exception, self._traceback

             ^

 SyntaxError: invalid syntax

 ----------------------------------------

ERROR: Command errored out with exit status 1: /Users/Sandy/anaconda3/bin/python /Users/Sandy/anaconda3/lib/python3.6/site-packages/pip install --ignore-installed --no-user --prefix /private/var/folders/1y/7v8fvfy51_sfdx_r21tgkq5h0000gn/T/pip-build-env-r8el7tjn/overlay --no-warn-script-location --no-binary :none: --only-binary :none: -i [https://pypi.org/simple](https://pypi.org/simple) -- 'setuptools&gt;=42' wheel 'setuptools_scm[toml]&gt;=3.4' Check the logs for full command output.```

I then uninstalled betfairlightweight and tried re-installing but got the same error. Looking online this seems like an internal error regarding pip any idea why this could happen?

---

## 2020-06-15 14:25:11 - random channel

**Chris**

A naive question as I'm only really dipping in and out of using bflw when needed, and not really a developer, but I've got a setup where I'm basically only ever grabbing prices from BFEX, and storing/comparing them with input i am providing from scraping other sites or manually, right now I generate a list of markets, and store the current available back/lay price, I'm only ever really interested in that price, currently that runs over a series of (now fairly slow) loops for the events and markets i'm interested in, I'd like to be able to expand that list of markets/events but this then makes some of the data at the beginning of my loops quite old by the time it's gone through the rest of the markets i'm interested and stored those (in a MySQL database), I think the right answer is to use Flumine, but I just wanted to see if anyone else does similar and how they handle it, in terms of getting the data back out for "current price", as I'd always been storing it in a db that was easy but i'm not sure if it's feasible with the rate that the data comes into flumine whether to then store that in a db to be able to use with my comparisons, hope that makes sense

---

## 2020-06-15 14:19:54 - issues channel

**liam**

haha, you won't look back, i think a 'how to setup a python/bflw/flumine instance on aws for free' could be a good thing to add to the faq/docs/repo

---

## 2020-06-06 16:18:09 - random channel

**Jonatan (skyw)**

If I install bflw, and then run mypy on my code which depends on bflw I will get an error that missing stubs or something like that.

---

## 2020-06-06 10:49:55 - general channel

**Will Morrison**

Worked like a charm, now I'm using flumine for the first time! If the following is too much "teach me Python", I apologize, and please feel free to tell me to just go learn more basics: I'm trying to make my first example custom strategy object, where I would like to modify the flumine example.py class to try to place a BACK on a single player if his batb is above a certain threshhold. In betfairlightweight, I was able to get these values by looping through the market book and using lines like

market_book._data["runners"][x]["ex"]["availableToBack"][lvl]["price"], where x and lvl are loop variables

which I was able to figure out by using the variable explorer in my Spyder IDE too dig into the market_book object after running one loop of examplestreaming.py. Now in flumine I don't know how to get a similar thing to investigate. I want to take a conditional like this from the example -

if (

                runner.status == "ACTIVE"

                and runner.last_price_traded

                and runner.selection_id == 11946248



and instead of runner.last_price_traded, say something like

                and runner.ex.availableToBack[0]["price"] &gt;= 3.0



Is there an easy way for me to figure out what all the runner.[things] available are named?

---

## 2020-06-04 08:21:39 - general channel

**Mo**

I install as a Python package to a virtual environment

---

## 2020-06-01 10:26:39 - random channel

**Stefan**

VS Code is really lightweight IDE, actually it is javascript app hosted in electron, therefor you can find web version of it on cloud services, like:



[https://visualstudio.microsoft.com/services/visual-studio-codespaces/](https://visualstudio.microsoft.com/services/visual-studio-codespaces/)



and so on.



I cannot afford to buy professional version of visual studio, so I use community one, and of course VS Code which supports all kinds of languages, and I experimented with python, R, julia, my favorite F# and so on. Just open VS Code Extensions and type whatever programming language you know and you will find there some extension. Python extension has 20.6 millions of installs, so seems to be quite popular.

---

## 2020-05-31 20:01:18 - issues channel

**Unknown**

Total beginner to programming (just a couple of python courses under my belt), so sorry for what are easy questions...

Im using BFLW Exampleone and trying to build out from there. The idea at this stage is to learn rather than a fully functioning program to place bets etc

Initial thoughts are to start with one market at at time, extract EX_BEST_OFFERS for each selection and store the three back odds and three lay odds (Do you store these values in a list?)

Ill only be active in play, so I guess I can loop on the Inplay flag from the market ID?

Ill create some bet logic and just print to console for now, of what the bet would have been ie selctionID; Side, Size etc..



Does this sound logical as first steps? Also, if anyone has very basic code they can share (with secret sauce removed!) it would be appreciated



Also, When I place the operation via the Visualiser, I can see the price and size (see image) , but when I run it in BFLW I can only see "object at 0x0000018286D26108" for example. Is this a location in memory where the EX_BEST_OFFERS values are stored?

if so, how do you access those values via python?



Sorry for newbie questions, thanks in advance

regards

Peter

---

## 2020-05-29 15:37:07 - issues channel

**Unknown**

Folks, re the certificates. As a beginner myself, I had the same issues..This question comes up a lot. I recently got this working. So if it helps someone in the future this is what isued to get it working.

Follow this link:



[http://www.betfairprotrader.co.uk/2015/08/creating-digital-certificate-for-betfair.html](http://www.betfairprotrader.co.uk/2015/08/creating-digital-certificate-for-betfair.html)



and then I continued with is link:



[https://helpcenter.gsx.com/hc/en-us/articles/115015887447-Extracting-Certificate-crt-and-PrivateKey-key-from-a-Certificate-pfx-File](https://helpcenter.gsx.com/hc/en-us/articles/115015887447-Extracting-Certificate-crt-and-PrivateKey-key-from-a-Certificate-pfx-File)



I had a single folder "certs" in the top level directory C:

This is what it looked like (see image), although I may have too many files in there now :grinning:



Your Python code should resemble something like this :-



trading = betfairlightweight.APIClient("UserName", "Password", app_key="YourAppKey", certs=r"C:\certs")

# login

trading.login()



Hope the helps

regards

Peter

---

## 2020-05-29 09:09:29 - issues channel

**JS**

Hi guys -  first time post from a newbie down under. I'm trying to setup betfairlightweight to bring through race fields and test on my model but have come across an issue in regards to the Certificates.  I followed this guide from Betfair in terms of certificate generation [https://docs.developer.betfair.com/display/1smk3cen4v3lu3yomq5qye0ni/Certificate+Generation+With+XCA](https://docs.developer.betfair.com/display/1smk3cen4v3lu3yomq5qye0ni/Certificate+Generation+With+XCA) which gives me a .crt and a .pem file. I realise though that it requires a .crt and a .key file as opposed to a .pem whihc this guide gives. I dont really understand the openssl side of things so thats why ive opted to use the XCA way. Any ideas on where to from here? any help would be much appreciated. Thanks!

---

## 2020-05-27 21:42:08 - general channel

**liam**

The market recorder is setup to record the raw data so that won’t really work but you can modify the price recorder [https://github.com/liampauling/flumine/blob/master/examples/strategies/pricerecorder.py|example](https://github.com/liampauling/flumine/blob/master/examples/strategies/pricerecorder.py|example)



Just change the check_market_book



```if market.seconds_to_start &lt; 600:

    return True```

---

## 2020-05-21 12:58:03 - general channel

**fjt1973**

I'm also new to Python (6 months) and like the way you can go back and edit a previous cell in Jupyter without having to re-run the whole code again.

---

## 2020-05-21 12:39:57 - general channel

**liam**

So flumine is setup for scripting, i.e. you create a script like example.py and then run it on a server (cron/docker etc) It is not really suited for an IDE like jupyter.

However there is certainly some logic missing to end the run when all markets are closed because you have found it it just continues to run, welcome thoughts on this

---

## 2020-05-19 12:34:19 - strategies channel

**James T**

I think you have two choices re: getting started and setting your future path in terms of implementation. 



You can either learn Python and use the libraries provided by the great community here. 



Or you stick with a language you’re already experienced in and use existing code or Betfair sample applications. But then build a data collection and backtesting platform yourself. 

---

## 2020-05-18 04:53:12 - general channel

**Will Morrison**

Hi everyone! I'm new to the betfairlightweight package. I already analyzed Betfair historical data using R, parsing the files with a json package and eventually creating rows with things like runner name, batb, batl, etc. I have got the examplestreaming script to generate data for the markets that I am interested in, and if I save market_book.streaming_update as a .txt and then substitute a few things, I can parse it as a json file, but it is missing some of the higher level data that I need, like the runner ids and runner names. When I click around the market_book (object?) in my variable explorer in Spyder, I can see that it looks like all the stuff I need is probably already there. Are there some examples of parsing this data into usable tables, or is there a way that I can retrieve the data to look more like the historical bz2 files that I am used to now? Thanks a bunch for any help, it's super cool to see that there's a community around this!

---

## 2020-05-12 20:38:56 - general channel

**Lee**

you could do `pip install smart_open[aws]`

---

## 2020-05-12 20:35:30 - general channel

**Jonjonjon**

(flumine) jon@jon-VirtualBox:~/PycharmProjectsFlumine/flumine$ conda install smart_open

Collecting package metadata (repodata.json): done

Solving environment: done





==&gt; WARNING: A newer version of conda exists. &lt;==

  current version: 4.8.2

  latest version: 4.8.3



Please update conda by running



    $ conda update -n base -c defaults conda







## Package Plan ##



  environment location: /home/jon/anaconda3/envs/flumine



  added / updated specs:

    - smart_open





The following packages will be downloaded:



    package                    |            build

    ---------------------------|-----------------

    boto3-1.12.39              |             py_0          93 KB

    botocore-1.15.39           |             py_0         3.8 MB

    cachetools-3.1.1           |             py_0          14 KB

    cffi-1.14.0                |   py37he30daa8_1         226 KB

    cryptography-2.9.2         |   py37h1ba5d50_0         626 KB

    google-api-core-1.17.0     |           py37_0          89 KB

    google-auth-1.14.1         |             py_0          58 KB

    google-cloud-core-1.3.0    |             py_0          28 KB

    google-cloud-storage-1.28.0|             py_0          62 KB

    google-resumable-media-0.5.0|             py_1          34 KB

    googleapis-common-protos-1.51.0|           py37_2          69 KB

    idna-2.9                   |             py_1          56 KB

    jmespath-0.9.4             |             py_0          22 KB

    libprotobuf-3.11.4         |       hd408876_0         4.8 MB

    protobuf-3.11.4            |   py37he6710b0_0         711 KB

    pyasn1-0.4.8               |             py_0          58 KB

    pyasn1-modules-0.2.7       |             py_0          63 KB

    pycparser-2.20             |             py_0          93 KB

    requests-2.23.0            |           py37_0          91 KB

    rsa-4.0                    |             py_0          30 KB

    s3transfer-0.3.3           |           py37_0          95 KB

    smart_open-2.0.0           |             py_0          76 KB

    urllib3-1.25.8             |           py37_0         165 KB

    ------------------------------------------------------------

                                           Total:        11.3 MB



The following NEW packages will be INSTALLED:



  boto               pkgs/main/linux-64::boto-2.49.0-py37_0

  boto3              pkgs/main/noarch::boto3-1.12.39-py_0

  botocore           pkgs/main/noarch::botocore-1.15.39-py_0

  cachetools         pkgs/main/noarch::cachetools-3.1.1-py_0

  cffi               pkgs/main/linux-64::cffi-1.14.0-py37he30daa8_1

  chardet            pkgs/main/linux-64::chardet-3.0.4-py37_1003

  cryptography       pkgs/main/linux-64::cryptography-2.9.2-py37h1ba5d50_0

  docutils           pkgs/main/linux-64::docutils-0.15.2-py37_0

  google-api-core    pkgs/main/linux-64::google-api-core-1.17.0-py37_0

  google-auth        pkgs/main/noarch::google-auth-1.14.1-py_0

  google-cloud-core  pkgs/main/noarch::google-cloud-core-1.3.0-py_0

  google-cloud-stor~ pkgs/main/noarch::google-cloud-storage-1.28.0-py_0

  google-resumable-~ pkgs/main/noarch::google-resumable-media-0.5.0-py_1

  googleapis-common~ pkgs/main/linux-64::googleapis-common-protos-1.51.0-py37_2

  idna               pkgs/main/noarch::idna-2.9-py_1

  jmespath           pkgs/main/noarch::jmespath-0.9.4-py_0

  libprotobuf        pkgs/main/linux-64::libprotobuf-3.11.4-hd408876_0

  protobuf           pkgs/main/linux-64::protobuf-3.11.4-py37he6710b0_0

  pyasn1             pkgs/main/noarch::pyasn1-0.4.8-py_0

  pyasn1-modules     pkgs/main/noarch::pyasn1-modules-0.2.7-py_0

  pycparser          pkgs/main/noarch::pycparser-2.20-py_0

  pyopenssl          pkgs/main/linux-64::pyopenssl-19.1.0-py37_0

  pysocks            pkgs/main/linux-64::pysocks-1.7.1-py37_0

  requests           pkgs/main/linux-64::requests-2.23.0-py37_0

  rsa                pkgs/main/noarch::rsa-4.0-py_0

  s3transfer         pkgs/main/linux-64::s3transfer-0.3.3-py37_0

  smart_open         pkgs/main/noarch::smart_open-2.0.0-py_0

  urllib3            pkgs/main/linux-64::urllib3-1.25.8-py37_0





Proceed ([y]/n)? y

---

## 2020-05-08 09:24:34 - general channel

**Nimo22**

Yes installed running with Conda and all required libraries along with bflw installed also

---

## 2020-05-08 09:21:31 - general channel

**Mo**

How new? Do you have Python installed?

---

## 2020-05-08 09:20:18 - general channel

**Nimo22**

Hi. New to python and API but very keen to learn. I understand the coding but I struggle with how do you actually use it once written? Do I need a Betfair API tool and somehow add the python code to it? I had found a link to a wordpress tutorial from Liam to help use bflw with Betfair api which is probably what I need but sadly that website is no longer. Does someone has something to point me in the right direction on the basics? I am yet to purchase a API key but want to test and fully understand first. Last thing I want is spam this group with silly questions, if somebody is willing to help a newbee to understand the basics please give me a shout! Thank you

---

## 2020-05-06 07:07:22 - general channel

**liam**

Welcome, many (including myself) came from BA or gruss but moved after wanting to do more. For me it was the challenge (can I write this strategy in my own code) as well as the ability to collect my own data and complete flexibility that coding gives you.



However it’s worth noting that it’s a steep learning curve if you are new to programming or don’t have something already ‘working’ using off the shelf software.

---

## 2020-05-04 11:34:41 - issues channel

**Unknown**

In regards to the historical data does anyone have issues with lots of updates having `img=True` and thus the cache being replaced? My assumption is that the data can be trusted and replacing the cache with the update is safe but who knows with this data (first time I have actually used Betfairs data rather than my own)

---

## 2020-05-01 10:26:55 - random channel

**Jonjonjon**

Nice. Thanks for sharing. Are you mainly going to be doing CPU (rather than GPU) intensive stuff? I currently have dual Xeon X575 chips in my setup. So they are almost 10 years old. I'm not sure how to work out how much faster a new setup will be. Having said that, I only managed to run historical data through Flumine last night, so it's early days to tell whether or not I need a crazy setup.

---

## 2020-05-01 09:13:38 - random channel

**PeterLe**

As a beginner I currently use pycharm community. Is it worth buying the professional version? I’m wondering whether it will help me learn quicker, and assist me greater or whether it’s overkill until I have more experience. Thanks 

---

## 2020-04-30 10:17:07 - general channel

**Cagdas Yetkin**

[@UBS7QANF3](@UBS7QANF3) I am trying to learn how to setup the stream and get the live odds. I have the delayed streaming service open now.



If I want to convert this sample tutorial into Belarus soccer live odds streaming then should I change the this way? Let’s say today at 12:00 there is a game between *Smolevichi and Energetik* in Belarus League.



```

market_filter = streaming_market_filter(

    event_type_ids=["1"], country_codes=["BLR"], market_types=["MATCH_ODDS"]

)```

thanks for showing some directions

---

## 2020-04-25 19:44:32 - issues channel

**user34**

I have tried reinstalling to remove the older listener classes, but it doesn't seem to help.

---

## 2020-04-21 15:56:38 - general channel

**Lee**

Is there a way currently for me to implement the SimulatedExecution methods in flumine? I’ve installed from the dev branch, sorry for being a bit too keen

---

## 2020-04-11 21:31:12 - general channel

**Ruben**

I have recently installed the betfairlightweight package, it's looking super-promising, thanks a lot to the developer(s)

---

## 2020-04-03 15:29:29 - issues channel

**Josh**

Yes installed and unfortunately had the same error, cheers liam I will keep checking back

---

## 2020-04-03 15:20:04 - issues channel

**Josh**

Hi all, hope everyone is safe and well. 



When trying to pip install betfairlightweight I get an error reading



Failed building wheel for ciso8601

Failed building wheel for ujson



Just wondered if anyone could shed some light on this

---

## 2020-04-02 17:24:12 - general channel

**Fab**

From my experience, we all learn in different ways, so my suggestion is to simply Youtube “python course beginner”, then start looking at courses one by one. If you find it difficult to understand that teacher, move to the next one.

---

## 2020-04-02 17:08:31 - general channel

**Jeff**

Yep you're right. This is what I have achieved so far in one week. Installed Python, PyCharm and Betfairlightweight and managed to get my GitHubExample to actually connect to Betfair but that's about it so far. I don't really understand coding even the Liam's examples don't make any sense to me.

---

## 2020-04-02 10:53:26 - general channel

**Mo**

Have you installed betfairlightweight?

---

## 2020-04-02 10:44:14 - general channel

**Jeff**

I like manual trading and this project will give me something to do and learn about but unfortunately I don't know what to do first. I have Betfair historic horse racing data and Python installed with PyQt but I've hit a brick wall. I don't know where to start first?

---

## 2020-04-02 00:34:48 - general channel

**Jeff**

Hi everyone I am very interested in building applications especially for Betfair. I am a complete noob with any language but I am very interested in Python. I would like to build an app that replays Betfairs horse racing historical data with ladders setup like Gruss or Bet Angel and able to place fictional bets and trade just as if it were real. I realise it's a tall order to build a complicated app with no experiance but I have plenty of time on my hands since I am out of work and have plenty of evenings to start learning. I have downloaded some sample horse racing historical data pro and advanced, Python installed and betfairlightweight and a few other addons. I guess I'd like to know where to start and if someone could point me in the right direction I'd be very greateful. Kindest regards Jeff

---

## 2020-03-31 09:53:24 - issues channel

**mandelbot**

So im trying to run the example marketrecorder.py but I get the following error:

Traceback (most recent call last):

  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python38\Lib\site-packages\flumine\examples\marketrecorder.py", line 46, in &lt;module&gt;

    framework.add_strategy(strategy)

  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python38\lib\site-packages\flumine\baseflumine.py", line 66, in add_strategy

    self.strategies(strategy)  # store in strategies

  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python38\lib\site-packages\flumine\strategy\strategy.py", line 26, in _call_

    strategy.add()

  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python38\Lib\site-packages\flumine\examples\strategies\marketrecorder.py", line 154, in add

    super().add()

  File "C:\Users\Administrator\AppData\Local\Programs\Python\Python38\Lib\site-packages\flumine\examples\strategies\marketrecorder.py", line 37, in add

    raise OSError("File dir %s does not exist" % self.local_dir)

OSError: File dir /tmp does not exist



I tried to create the dir in question but get the same. What am I missing? Appologies for the dumb question, I'm new to python and coding and am still trying to understand how this library works.

---

## 2020-03-23 22:22:59 - issues channel

**Jason**

Ive been struggling to install Betfairlightweight for the last few days. Im using pycharm



`Collecting betfairlightweight==2.2.0`

  `Using cached betfairlightweight-2.2.0-py3-none-any.whl (60 kB)`

`Collecting ujson==2.0.1`

  `Using cached ujson-2.0.1.tar.gz (7.1 MB)`

  `Installing build dependencies: started`

  `Installing build dependencies: finished with status 'done'`

  `Getting requirements to build wheel: started`

  `Getting requirements to build wheel: finished with status 'done'`

  `Installing backend dependencies: started`

  `Installing backend dependencies: finished with status 'done'`

    `Preparing wheel metadata: started`

    `Preparing wheel metadata: finished with status 'done'`

`Collecting requests&lt;=2.23.0`

  `Using cached requests-2.23.0-py2.py3-none-any.whl (58 kB)`

`Collecting ciso8601==2.1.3`

  `Using cached ciso8601-2.1.3.tar.gz (15 kB)`

`Requirement already satisfied: certifi&gt;=2017.4.17 in c:\users\justin\anaconda3\envs\build\lib\site-packages (from requests&lt;=2.23.0-&gt;betfairlightweight==2.2.0) (2019.11.28)`

`Collecting chardet&lt;4,&gt;=3.0.2`

  `Using cached chardet-3.0.4-py2.py3-none-any.whl (133 kB)`

`Collecting urllib3!=1.25.0,!=1.25.1,&lt;1.26,&gt;=1.21.1`

  `Using cached urllib3-1.25.8-py2.py3-none-any.whl (125 kB)`

`Collecting idna&lt;3,&gt;=2.5`

  `Using cached idna-2.9-py2.py3-none-any.whl (58 kB)`

`Building wheels for collected packages: ujson, ciso8601`

  `Building wheel for ujson (PEP 517): started`

  `Building wheel for ujson (PEP 517): finished with status 'error'`

  `Building wheel for ciso8601 (setup.py): started`

  `Building wheel for ciso8601 (setup.py): finished with status 'error'`

  `Running setup.py clean for ciso8601`

`Failed to build ujson ciso8601`



  `ERROR: Command errored out with exit status 1:`

   `command: 'C:\Users\Justin\anaconda3\envs\Build\python.exe' 'C:\Users\Justin\AppData\Roaming\Python\Python37\site-packages\pip\_vendor\pep517\_in_process.py' build_wheel 'C:\Users\Justin\AppData\Local\Temp\tmpswrbz18z'`

       `cwd: C:\Users\Justin\AppData\Local\Temp\pycharm-packaging\ujson`

  `Complete output (5 lines):`

  `running bdist_wheel`

  `running build`

  `running build_ext`

  `building 'ujson' extension`

  `error: Microsoft Visual C++ 14.0 is required. Get it with "Build Tools for Visual Studio": [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)`

  `----------------------------------------`

  `ERROR: Failed building wheel for ujson`

  `ERROR: Command errored out with exit status 1:`

   `command: 'C:\Users\Justin\anaconda3\envs\Build\python.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\Justin\\AppData\\Local\\Temp\\pycharm-packaging\\ciso8601\\setup.py'"'"'; __file__='"'"'C:\\Users\\Justin\\AppData\\Local\\Temp\\pycharm-packaging\\ciso8601\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d 'C:\Users\Justin\AppData\Local\Temp\pip-wheel-_l78ovpi'`

       `cwd: C:\Users\Justin\AppData\Local\Temp\pycharm-packaging\ciso8601\`

  `Complete output (14 lines):`

  `running bdist_wheel`

  `running build`

  `running build_py`

  `package init file 'ciso8601\__init__.py' not found (or not a regular file)`

  `creating build`

  `creating build\lib.win-amd64-3.7`

  `creating build\lib.win-amd64-3.7\ciso8601`

  `copying ciso8601\__init__.pyi -&gt; build\lib.win-amd64-3.7\ciso8601`

  `copying ciso8601\py.typed -&gt; build\lib.win-amd64-3.7\ciso8601`

  `warning: build_py: byte-compiling is disabled, skipping.`

  

  `running build_ext`

  `building 'ciso8601' extension`

  `error: Microsoft Visual C++ 14.0 is required. Get it with "Build Tools for Visual Studio": [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)`

  `----------------------------------------`

  `ERROR: Failed building wheel for ciso8601`

`ERROR: Could not build wheels for ujson which use PEP 517 and cannot be installed directly`

---

## 2020-03-22 08:14:56 - general channel

**mandelbot**

Hi all, I'm new here too. Been meaning to port my process to API for a while and am taking this lockdown as an opportunity to do so. I only started coding a couple years ago (VBA) and am fairly new to Python. So apologies in advance for basic questions I may ask (I promise to google first :)). Many thanks to [@U4H19D1D2](@U4H19D1D2) and everyone who contributed over the years. Looking forward to being a part of this slack!

---

## 2020-03-21 14:02:26 - issues channel

**kense**

Tried to 'pip install --upgrade betfairlightweight' after it had installed with the 'install flumine' but got the same error.

---

## 2020-03-21 14:00:53 - issues channel

**kense**

"ERROR: Could not build wheels for ujson which use PEP 517 and cannot be installed directly"

---

## 2020-03-21 13:59:50 - issues channel

**kense**

Just for info, I tried to "pip install betfairlightweight" and found that it returned an error when attempting to build the wheel for ujson (it was collecting ujson-2.0.1). When I did a "pip install flumine" afterwards, it installed ujson without any issues, but it was version 1.35 (and also included betfairlightweight 2.1.0 rather than 2.2.0). Apologies if you're already aware...

---

## 2020-03-08 06:54:35 - general channel

**reload**

Hey All



Complete newbie to Betfair, dont know any programming I just work in construction finance.



Would anyone be open to helping our punters get up and running on Betfair? - currently we bet via bookies only.



We are trying to setup database or excel of previous results for horse racing / grey hound racing including opening prices &amp; prices at jump, summarised by jockeys / trainers etc.



Is anyone open to assisting? If so, could you please advise rates? 



Look forward to hearing from you all!



Cheers

---

## 2020-02-25 12:38:05 - issues channel

**Fab**

I’m still a Python beginner so don’t guarantee that the following works, but there seems to be a way of catching when your app is exiting or gets killed

---

## 2020-02-24 16:22:38 - strategies channel

**D C**

Oh totally agree. I am not being critical just wish I could understand why. It's very useful indeed and I have more ideas of how to use it than hours to implement them. Really just getting started out but I like to understand the data first - hence rendering the positions.

---

## 2020-02-18 01:14:08 - issues channel

**Jonatan (skyw)**

python --version

pip install -r requirements.txt

---

## 2020-02-11 18:16:24 - general channel

**Alex F**

```import logging



import betfairlightweight

from betfairlightweight import StreamListener

from betfairlightweight.streaming.stream import MarketStream



"""

Data needs to be downloaded from:

    [https://historicdata.betfair.com](https://historicdata.betfair.com)

"""



# setup logging

logging.basicConfig(level=[http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))



# create trading instance (no need to put in correct details)

trading = betfairlightweight.APIClient([mailto:'alexander@gmail.com|'alexander@gmail.com](mailto:'alexander@gmail.com|'alexander@gmail.com)','xxxxxx', app_key='xxxxxx', certs='C:/OpenSSL-Win64/bin')

trading.login()



class HistoricalStream(MarketStream):

    # create custom listener and stream



    def __init__(self, listener):

        super(HistoricalStream, self).__init__(listener)

        with open('output.txt', 'w') as output:

            output.write('Time,MarketId,Status,Inplay,SelectionId,LastPriceTraded\n')



    def on_process(self, market_books):

        with open('output.txt', 'a') as output:

            for market_book in market_books:

                for runner in market_book.runners:



                    # how to get runner details from the market definition

                    market_def = market_book.market_definition

                    runners_dict = {(runner.selection_id, runner.handicap): runner for runner in market_def.runners}

                    runner_def = runners_dict.get(

                        (runner.selection_id, runner.handicap)

                    )



                    output.write('%s,%s,%s,%s,%s,%s\n' % (

                        market_book.publish_time, market_book.market_id, market_book.status, market_book.inplay,

                        runner.selection_id, runner.last_price_traded or ''

                    ))





class HistoricalListener(StreamListener):

    def _add_stream(self, unique_id, stream_type):

        if stream_type == 'marketSubscription':

            return HistoricalStream(self)





# create listener

listener = HistoricalListener(

    max_latency=1e100

)



# create historical stream, update directory to file location

stream = trading.streaming.create_historical_generator_stream(

    directory='C:/Users/alexa/Desktop/repos/bet/betfair/examples/29637259',

    listener=listener

)



# start stream

#stream.start(async_=False)



g = stream.get_generator()



for i in g:

    print(i)

    ```

---

## 2020-02-08 12:26:56 - general channel

**JK**

Ah that's interesting, thanks for that. prob saved me a few hours in the future haha. In production how would you run your bot? Like would I just let a script run 24/7 on an ec2 instance for example? Not a dev so pretty new to all this stuff.

---

## 2020-02-07 15:14:13 - issues channel

**Jonatan (skyw)**

Maybe create a FAQ for betfairlightweight or more detailed install instructions, although the extra work for different operating systems ...

---

## 2020-02-06 18:05:28 - issues channel

**Jonatan (skyw)**

Yeah, sorry did not mean to come off as rude :slightly_smiling_face:,

Yeah there are some steps  to do documentation are pretty good though so you should be fine :slightly_smiling_face:



The comment above was meant generally when people installing betfairlightweight they tend to use environments that depends on system libraries, just a strong opinion by me on not how to do it :slightly_smiling_face:. Not really a discussion in issues. Just ask if you have any other problems! GL

---

## 2020-02-06 17:08:37 - issues channel

**Alex F**

ERROR: Command errored out with exit status 1:

     command: 'C:\Users\alexa\Anaconda3\python.exe' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\alexa\\AppData\\Local\\Temp\\pip-install-jajffrml\\version\\setup.py'"'"'; __file__='"'"'C:\\Users\\alexa\\AppData\\Local\\Temp\\pip-install-jajffrml\\version\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base 'C:\Users\alexa\AppData\Local\Temp\pip-install-jajffrml\version\pip-egg-info'

         cwd: C:\Users\alexa\AppData\Local\Temp\pip-install-jajffrml\version\

    Complete output (7 lines):

    Traceback (most recent call last):

      File "&lt;string&gt;", line 1, in &lt;module&gt;

      File "C:\Users\alexa\AppData\Local\Temp\pip-install-jajffrml\version\setup.py", line 4, in &lt;module&gt;

        from version import __version__

      File "C:\Users\alexa\AppData\Local\Temp\pip-install-jajffrml\version\version.py", line 2, in &lt;module&gt;

        from itertools import izip_longest

    ImportError: cannot import name 'izip_longest' from 'itertools' (unknown location)

    ----------------------------------------

ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.

---

## 2020-02-06 16:57:41 - issues channel

**Alex F**

hey :slightly_smiling_face: i tried installing betfairlightweight, but it fails to build ciso8601, any idea what is up ? also, all i am after is to be able to read nicely the historic data that i have downloaded, is it really worth it to debug everything (ive spent 2 hours already) or just head in a different direction?

---

## 2020-01-31 14:51:51 - issues channel

**Gustav Molander**

That would be ?

```pip3 install betfairlightweight --user```

with user being my username?

---

## 2020-01-31 14:49:29 - issues channel

**Gustav Molander**

yeah skyw, do you recommend changing default python to 3 or just do pip3 install?

---

## 2020-01-31 14:48:27 - issues channel

**Gustav Molander**

Okay nice! Getting some success now, only a single error left:

```ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: Consider using the `--user` option or check the permissions.```

---

## 2020-01-31 14:45:14 - issues channel

**Gustav Molander**

Im getting the exact same errors when using pip3. Im installing the command tools now!

---

## 2020-01-31 14:34:11 - issues channel

**Jonatan (skyw)**

Make sure you have python 3.7+, then in your project folder python -m venv venv

then pip install -r requirements.txt

---

## 2020-01-31 14:32:02 - issues channel

**Gustav Molander**

Hi guys, a nice little channel you have here. :slightly_smiling_face: I just started out with trying to install betfairlightweight. Is there anything special you have to do when using Mac OS (Catalina) regarding python/python3 (pip/pip3) when installing? Im getting a bunch of errors.

---

## 2020-01-17 17:37:18 - issues channel

**Mo**

Did you install flumine to a virtual environment or system wide?

---

## 2020-01-17 16:54:43 - issues channel

**PeterLe**

Still learning Python (programming)  so forgive me if this is simple error...and i expect it is, on my part:-)

betfairlightweight all running OK, certs loaded fine too..

Im able to run some of the examples fine.



Im keen to be able to use flumine (output to a local directory on my PC)

$ PIP install flumine completed



However when I run the code im getting this error :



 File "C:/Users/User-1/Desktop/Python/Flumine/flumine-master/flumine/flumine.py", line 7, in &lt;module&gt;

    from .listener import FlumineListener

ImportError: attempted relative import with no known parent package



line 7 in flumine is :



from .listener import FlumineListener



I get the gist of the error, but not sure how to fix it.

Any help appreciated. Thanks in advance

Peter

---

## 2020-01-05 21:46:57 - general channel

**Alex A**

At least it gave me an excuse to install and use betfairlightweight.

---

## 2020-01-05 17:00:05 - issues channel

**Unknown**

Hi guys. i keep  getting the same error. how can i deal with this error attached

my code:

```import os

import logging

import queue

from betfairlightweight import filters

import datetime

import betfairlightweight

from betfairlightweight.filters import (

    streaming_market_filter,

    streaming_market_data_filter,

)



import pandas as pd

# create trading instance

trading = betfairlightweight.APIClient('username',

                                       'password',

                                       app_key='appkey',

                                       certs='C:\\Users\\')



# login

trading.login()



# make event type request to find horse racing event type

horse_racing_event_type_id = trading.betting.list_event_types(

    filter=filters.market_filter(

        text_query='Horse Racing'

    )

)

# setup logging

logging.basicConfig(level=[http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))  # change to DEBUG to see log all updates



# create trading instance (app key must be activated for streaming)

trading.login()



t = datetime.datetime.now()+datetime.timedelta(hours=12)



while datetime.datetime.now() &lt; t:

    h_i1 =datetime.datetime.now()

    h_i2 = h_i1 + datetime.timedelta(hours=12)

    # Define a market filter

    thoroughbreds_event_filter = betfairlightweight.filters.market_filter(

        event_type_ids=['7'],

        market_start_time={

            'from': h_i1.strftime("%Y-%m-%dT%TZ"),

            'to': h_i2.strftime("%Y-%m-%dT%TZ")

        }

    )



    # Print the filter

    # thoroughbreds_event_filter



    # Get a list of all thoroughbred events as objects

    thoroughbred_events = trading.betting.list_events(

        filter=thoroughbreds_event_filter

    )



    # Get a list of all thoroughbred events as objects

    hr_thoroughbred_events = trading.betting.list_events(

        filter=thoroughbreds_event_filter

    )



    # Create a DataFrame with all the events by iterating over each event object

    hr_thoroughbred_events_next_12hours = pd.DataFrame({

        'Event Name': [event_object.event.name for event_object in hr_thoroughbred_events],

        'Event ID': [event_object.event.id for event_object in hr_thoroughbred_events],

        'Event Venue': [event_object.event.venue for event_object in hr_thoroughbred_events],

        'Country Code': [event_object.event.country_code for event_object in

                         hr_thoroughbred_events],

        'Time Zone': [event_object.event.time_zone for event_object in hr_thoroughbred_events],

        'Open Date': [event_object.event.open_date for event_object in hr_thoroughbred_events],

        'Market Count': [event_object.market_count for event_object in hr_thoroughbred_events]

    })

    # create queue

    output_queue = queue.Queue()



    # create stream listener

    listener = betfairlightweight.StreamListener(

        output_queue=output_queue,

    )



    # create stream

    stream = trading.streaming.create_stream(

        listener=listener,

    )



    # create filters (GB WIN racing)

    market_filter = streaming_market_filter(

        event_type_ids=['7'],

        event_ids=hr_thoroughbred_events_next_12hours['Event ID'],

        market_types=['WIN'],

    )

    market_data_filter = streaming_market_data_filter(

        fields=['EX_BEST_OFFERS', 'EX_MARKET_DEF'],

        ladder_levels=5,

    )



    # subscribe

    streaming_unique_id = stream.subscribe_to_markets(

        market_filter=market_filter,

        market_data_filter=market_data_filter,

        conflate_ms=1000,  # send update every 1000ms

    )



    # start stream

    stream.start(async_=True)



    # check for updates in output queue



    while datetime.datetime.now() &lt; t:

        try:

            market_books = output_queue.get()

            print(market_books)



            for market_book in market_books:

                print(

                    market_book.streaming_update, 

                    market_book.publish_time,  

                )

        except:

            output_queue = queue.Queue()



            # create stream listener

            listener = betfairlightweight.StreamListener(

                output_queue=output_queue,

            )



            # create stream

            stream = trading.streaming.create_stream(

                listener=listener,

            )



            # create filters 

            market_filter = streaming_market_filter(

                event_type_ids=['7'],

                event_ids=hr_thoroughbred_events_next_12hours['Event ID'],

                market_types=['WIN'],

            )

            market_data_filter = streaming_market_data_filter(

                fields=['EX_BEST_OFFERS', 'EX_MARKET_DEF' ],

                ladder_levels=5,

            )



            # subscribe

            streaming_unique_id = stream.subscribe_to_markets(

                market_filter=market_filter,

                market_data_filter=market_data_filter,

                conflate_ms=1000,  # send update every 1000ms

            )



            # start stream

            stream.start(async_=True)

    t = t + datetime.timedelta(hours=12)```

 but i doesn't  help. i thought if i put a while loop, then when error occurs it will sleep for 1 second and then subscribe to markets as you suggested and then  start the stream again. but still the code enter a state where the message below is displayed and nothing happens. this happens everyday once .  as you can see in Pycharm, the Run tab is still green, also the stop button(red square) is still active, it seems that my code does not capture the error , but the betfairlightweight source code capture it, then something happens and it stays there.why does my try and except  statements can't capture this error? I have to push  the stop button on the top left  and then rerun the code.  have you seen this issue before, any idea how can this be fixed.

---

## 2019-12-28 12:30:44 - general channel

**Marcel**

Hi, I am pretty new to betfairlightweight. I would like to run this script:

---

## 2019-12-21 23:56:04 - issues channel

**PeterLe**

[@U92CASP1B](@U92CASP1B) Seen this error posted before..advice was :it should be settings={“betfairlightweight”: {“username......

Set certificate_login to true if you have certs setup (you can login without using login_interactive) but don’t recommend it

---

## 2019-12-02 19:20:40 - general channel

**Mo**

My suggestion is to try to get an account manager and use them to get a master/subaccount setup. But I think they don’t really give them out any more. I think their intention is for people to separate strategies using the customerStrategyRef functionality instead. I could be wrong though. [@U4H19D1D2](@U4H19D1D2) do you have any more insight?

---

## 2019-12-01 16:09:05 - general channel

**liam**

It’s setup for one when it comes to historical data, obvs the live stream can handle multiple because multiple markets come from betfair and there is only one market per file 

---

## 2019-11-28 13:37:30 - issues channel

**liam**

Are you setup to catch errors and reconnect? 

---

## 2019-11-24 23:30:03 - general channel

**PeterLe**

Hi, for anyone new to this (such as myself), i was just viewing a channel on Youtube - Horsetrader, he only has circa 10 videos, but you may find them useful. Ive just watched his video on login and session management and although Ive been through these steps over the last few days, it would have been easier to have watched that first. All his videos are based on python, so worth a mention.

---

## 2019-08-28 09:09:22 - issues channel

**liam**

pip install betfairlightweight==1.10.2b

---

## 2019-08-16 13:00:10 - general channel

**Ian**

I think the debug in container is for large teams - making environment setup for new devs less hassle 

---

## 2019-08-15 12:16:58 - general channel

**Rob (NZ)**

Awesome so good logic would be to setup a ec2 instance and use docker to deploy on it with the python code and betfairlightweight and other python libraries...  any thoughts on then how I should have my database ... so that the selections can be picked up etc (in my current setup it's just a local mysql setup so just not sure what would be the best in the cloud )

---

## 2019-07-07 11:24:56 - random channel

**OT**

I've written for 3 betting APIs and it's the worst one. It's the second time I've written for matchbook api though, the first time the strategy was not so sensitive to this

---

## 2019-06-28 14:18:42 - general channel

**Brenton Collins**

Hello, new to this group. Has anyone had issues with the OverflowError: Maximum recursion level reached python. it is happening when placing a bet in a loop, I can manage to place a bet by punching the data for each bet but as soon as I put it in a list and set the loop going I get an overflow error!!

---

## 2019-06-14 09:13:55 - general channel

**Mo**

I don't use Windows myself but I use PyCharm*: [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/). I would definitely recommend using that to develop in and it should also be able to help you with things like package installation: [https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html)

---

## 2019-06-14 09:11:17 - general channel

**Mo**

`pip` will already be installed as part of Python

---

## 2019-06-14 08:38:59 - general channel

**Mo**

`pip` is a separate application for installing Python packages

---

## 2019-06-14 08:38:40 - general channel

**Mo**

`pip install betfairlightweight` would be run in a Command Prompt

---

## 2019-06-13 22:30:15 - general channel

**Dan**

Hey, sorry numpty question but trying to get up and running I have an app key and SSL cert added to my account, how do I install betfairlightweight?  I've downloaded it from github but don't understand the $ pip install betfairlightweight instruction...where do I use this if not in python?

---

## 2019-06-05 14:21:52 - general channel

**Leon**

Hi [@U4H19D1D2](@U4H19D1D2) it was me who posted on stackoverflow - I've been given a solution now so thanks to all who contributed. You mentioned that 'the code hurts to read' - any chance you could give us a couple of pointers on how to improve it? (I'm not arguing that the code is well written, I'm just fairly new to python so looking for some pointers). Some parts of the code were taken from the betfair website as has been mentioned above (I had assumed that would be of reasonable quality, but maybe not :face_with_raised_eyebrow:)

---

## 2019-05-22 02:08:10 - issues channel

**T**

I am using betfairlightweight 1.9.1 which I installed via pip. I am running the code in a Jupyter Notebook.

---

## 2019-05-22 02:01:45 - issues channel

**T**

Hi guys. I am pretty new to betfairlightweight so please bear with!



I am trying to place an order onto the exchange using the following code:



```limit_order = filters.limit_order(

            size=stake,

            price=price,

            persistence_type='LAPSE')



    instruction = filters.place_instruction(

        order_type='LIMIT',

        selection_id=selection_id,

        side='BACK',

        limit_order=limit_order)



    place_orders = trading.betting.place_orders(

        market_id=market_id,

        instructions=[instruction])```

---

## 2019-05-16 21:34:05 - issues channel

**Newbie99**

I'm getting a weird error, out of the blue (on another machine the script runs fine), any ideas what could have got messed up (betfairlightweight appears to be installed correctly, re-installed just now, but no joy):



```

Traceback (most recent call last):

  File "D:/Python37/webpages/betfair_python.py", line 61, in &lt;module&gt;

    market_stream.start(_async=True)

TypeError: start() got an unexpected keyword argument '_async'



```



Any pointers as to what might be causing this?



For reference, if I were to remove the _async=True then instead of an error it just hangs at:



```

INFO:betfairlightweight.streaming.stream:[Stream: 1]: "OrderStream" created

INFO:betfairlightweight.streaming.stream:[Stream: 1]: "MarketStream" created

INFO:betfairlightweight.streaming.listener:[Connect: 1]: connection_id: 006-160519203236-239625

INFO:betfairlightweight.streaming.listener:[Subscription: 2]: SUCCESS

INFO:betfairlightweight.streaming.listener:[Subscription: 1]: SUCCESS

INFO:betfairlightweight.streaming.stream:[MarketStream: 1] 1.130856098 added, 1 markets in cache

INFO:betfairlightweight.streaming.stream:[Stream: 1]: 1 mc added

```

---

## 2019-04-23 09:06:52 - issues channel

**OT**

[@U4H19D1D2](@U4H19D1D2) I've been doing a bit more research on my setup. I think some of my reasoning behind writing this code (written &gt;1 year ago!) was to not subscribe to any markets that i don't want to see. otherwise at some point I will have to check each incoming market_book and reject the ones I don't want to. for example, there's no way, as far as I can tell, a way to subscribe to horse racing, but only handicap races.. you have to subscribe to all horse racing and then just skip and non-handicap races. my way around this was to just collect market_id for all handicap races and put that into the streaming_market_filter, but you need to re-do it periodically to pick up new races/markets. does that make sense? and how does that fit with your way of managing this kind of problem?

---

## 2019-04-22 11:57:19 - general channel

**Filippo Bovo**

Hi, my name is Filippo, and I have just joined this workspace.



Yesterday, I tested out the `betfairlightweight` Python package. It is really well written.



As I am quite new to the Betfair APIs, I wonder how I can get the price ladder data for a certain selection in a market.



I tried listing the runner and selection details straight from `betfairlightweight.APIClient`, but they don't seem to have details on the price ladder. My guess is that I should use a `betfairlightweight.StreamListener` to get such data, but I cannot test this as I am using a delayed app key, which does not support the Betfair Stream API.



Could you please let me know if using a stream listener is the only way to get the price ladder data?



Thanks.

---

## 2019-04-11 15:51:25 - issues channel

**OT**

[@U4H19D1D2](@U4H19D1D2) are you saying that if you setup a streaming_market_filter using some parameters other than market_id, it will automatically subscribe to new markets?

---

## 2019-03-24 21:38:28 - general channel

**Rob (NZ)**

Hi all.. just introducing myself... Rob from New Zealand... I've been using betfair for awhile and 3rd party software (betangel) .. I'm now at the stage I want to start using the api and get some automation running without depending on others software.  I'm self learning python to do this and have a strong focus on data visualisation.  I've installed lightweight and really looking forward to using it.



Cheers Rob

---

## 2019-02-20 16:11:46 - issues channel

**Newbie99**

Ok...I think I've figured out why it hangs now...it is to do with output_queue.get() returning an empty value.



I am trying to structure the below to catch (and ignore) an empty outcome (if there are values the queue works fine, which is why it always works first time), however the below returns the error shown in the logs below (which I think confirms my logic is correct, but the way I try to catch it is incorrect):



```

@socketio.on('ping')

def handle_message(*_args, **_kwargs):

    try:

            market_books = output_queue.get(False)

    except output_queue.empty:

            pass

    else:

        for market_book in market_books:

            emit('my_response2', {'message': 'update', 'mb': market_book.streaming_update})

```



Server logs (which I believe confirm my suspicion):



```

ERROR:engineio.server:message handler error

Traceback (most recent call last):

  File "D:/Python37/webpages/betfair_flaskio.py", line 51, in handle_message

    market_books = output_queue.get(False)

  File "D:\Python37\lib\queue.py", line 167, in get

    raise Empty

_queue.Empty



During handling of the above exception, another exception occurred:



Traceback (most recent call last):

  File "D:\Python37\lib\site-packages\engineio\server.py", line 505, in _trigger_event

    return self.handlers[event](*args)

  File "D:\Python37\lib\site-packages\socketio\server.py", line 590, in _handle_eio_message

    self._handle_event(sid, pkt.namespace, pkt.id, pkt.data)

  File "D:\Python37\lib\site-packages\socketio\server.py", line 526, in _handle_event

    self._handle_event_internal(self, sid, data, namespace, id)

  File "D:\Python37\lib\site-packages\socketio\server.py", line 529, in _handle_event_internal

    r = server._trigger_event(data[0], namespace, sid, *data[1:])

  File "D:\Python37\lib\site-packages\socketio\server.py", line 558, in _trigger_event

    return self.handlers[namespace][event](*args)

  File "D:\Python37\lib\site-packages\flask_socketio\__init__.py", line 258, in _handler

    *args)

  File "D:\Python37\lib\site-packages\flask_socketio\__init__.py", line 641, in _handle_event

    ret = handler(*args)

  File "D:/Python37/webpages/betfair_flaskio.py", line 54, in handle_message

    except output_queue.empty:

TypeError: catching classes that do not inherit from BaseException is not allowed



```

---

## 2019-02-19 12:05:03 - issues channel

**Newbie99**

No luck with different ports or browsers, I even tried a fresh install on my Surface Go (which admittedly is also Windows 10, but doesn't have much on it). No joy, but I did get different errors, which may be more useful to decypher:



HTTP400: BAD REQUEST - The request could not be processed by the server due to invalid syntax.

(XHR)GET - [http://localhost:3000/socket.io/?EIO=3&amp;transport=polling&amp;t=1550577763533-16&amp;sid=a30e5471ac3446018e7290fa00eba7a5](http://localhost:3000/socket.io/?EIO=3&amp;transport=polling&amp;t=1550577763533-16&amp;sid=a30e5471ac3446018e7290fa00eba7a5)



 HTTP400: BAD REQUEST - The request could not be processed by the server due to invalid syntax.

(XHR)POST - [http://localhost:3000/socket.io/?EIO=3&amp;transport=polling&amp;t=1550577763604-17&amp;sid=a30e5471ac3446018e7290fa00eba7a5](http://localhost:3000/socket.io/?EIO=3&amp;transport=polling&amp;t=1550577763604-17&amp;sid=a30e5471ac3446018e7290fa00eba7a5)



Doesn't make a great deal of sense to me, as the message is logically the same as the previous one that worked fine, but perhaps it needs a line break or something in it?

---

## 2019-02-17 17:51:34 - issues channel

**Newbie99**

By emitting a text string and commenting out the market_books references below, I can see the PING and respective emit work correctly, therefore this issue appears to be around market_books = output_queue.get() after the first time (as it always works first time round):



```

@socketio.on('ping')

def handle_message(*_args, **_kwargs):

    market_books = output_queue.get()



    for market_book in market_books:

        emit('my_response',

             {'data': 'update', 'mb': market_book.streaming_update})

```

---

## 2019-02-17 15:36:36 - general channel

**Marcel**

[@U4H19D1D2](@U4H19D1D2) I have read the examples, although it seems to me that these are related to horse racing? I have also read the API reference guide from above. It looks pretty tough to me to set up. Since I am also new to Python I have a lot to learn. For that reason I was wondering if someone had already made a script for the soccer coupon.

---

## 2019-02-17 13:48:17 - general channel

**Marcel**

Hello, nice there is a Phyton Betfair API community! I am new to Python and the Betfair API. Currently I use a vendor application in combination with Excel VBA.



To improve speed and flexibility I would like to build a bot in Python for betting on Match Odds soccer. Does someone has a script which generates a coupon of matches for the day with betting functionality which I can use as a starting point to add my criteria to place bets on those markets? That would be great!

---

## 2019-02-16 17:39:52 - issues channel

**Newbie99**

```

import os

import logging

import queue

from threading import Thread

from flask import Flask, render_template

from flask_socketio import SocketIO, emit

import betfairlightweight

from betfairlightweight.filters import (

            streaming_market_filter,

            streaming_market_data_filter,

        )



# setup logging

logging.basicConfig(level=[http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))  # change to DEBUG to see log all updates



# create trading instance (app key must be activated for streaming)

username = os.environ.get('username')

trading = betfairlightweight.APIClient(user_name, password, appkey, certs=cert_path)

trading.login()



# create queue

output_queue = queue.Queue()



# create stream listener

listener = betfairlightweight.StreamListener(

    output_queue=output_queue,

)



# create stream

stream = trading.streaming.create_stream(

    listener=listener,

)



# create filters (GB WIN racing)

market_filter = streaming_market_filter(

        event_type_ids=['7'],

        country_codes=['US'],

        market_types=['WIN'],

)

market_data_filter = streaming_market_data_filter(

    fields=['EX_BEST_OFFERS', 'EX_MARKET_DEF'],

    ladder_levels=3,

)



# subscribe

streaming_unique_id = stream.subscribe_to_markets(

    market_filter=market_filter,

    market_data_filter=market_data_filter,

    conflate_ms=1000,  # send update every 1000ms

)



# start stream

stream.start(_async=True)



# Create a flask app

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'

# Use the flask app to create a socketio decorator

socketio = SocketIO(app)

thread = None



@app.route('/')

def index():

    global thread

    if thread is None:

        thread = Thread(target=handle_message)

        thread.start()

        socketio.sleep(2)

        return render_template('index.html')



@socketio.on('connect', namespace='/test')

def test_connect():

        global thread

        socketio.sleep(1)

        market_books = output_queue.get()

        print(market_books)

        for market_book in market_books:

             print(

             market_book,

             market_book.streaming_unique_id,  # unique id of stream (returned from subscribe request)

             market_book.streaming_update,  # json update received

             market_book.market_definition,  # streaming definition, similar to catalogue request

             market_book.publish_time  # betfair publish time of update

        )



        for market_book in market_books:

             emit('my_response', {'data': 'connect', 'mb': market_book.streaming_update, 'namespace': '/test'})

        socketio.sleep(1)

@socketio.on('ping', namespace='/test')

def handle_message(*_args, **_kwargs):

    global thread

    while True:

        socketio.sleep(2)

        emit('my_response', {'data': 'pong', 'mb': 'pong', 'namespace': '/test'})

        socketio.sleep(2)

        market_books = output_queue.get()

        print(market_books)



        for market_book in market_books:

            print(

                market_book,

                market_book.streaming_unique_id,  # unique id of stream (returned from subscribe request)

                market_book.streaming_update,  # json update received

                market_book.market_definition,  # streaming definition, similar to catalogue request

                market_book.publish_time  # betfair publish time of update

            )



        for market_book in market_books:

            emit('my_response', {'data': 'update', 'mb': market_book.streaming_update, 'namespace': '/test'})

        socketio.sleep(1)



if __name__ == '__main__':

    socketio.run(app, debug=True, host='127.0.0.1', port=5000)

stream.stop()

```

---

## 2019-02-16 17:39:36 - issues channel

**Newbie99**

hello again, I have spent a lot of time stepping through the logic in a bit more of a sensible fashion and tidied things up a bit. From a logical point of view, I'm still missing something, the code appears to make sense and doesn't throw up any errors. I've setup a ping from the client, the server then responds with a pong...but only on the first ping. In the console.log on the client after that it pings away, but the server never receives them, which seems odd. I make the assumption that the error is actually along the lines of my server code is not looking for the ping, rather than any issue on the client side. I'm guessing there is an issue with Threads that I'm not understanding, because I can't see what else it could be.

---

## 2019-02-09 23:23:57 - issues channel

**Newbie99**

yep, it didn't, that was the only time I actually had an error....which is the whole confusing thing about python (to me)!



I am trying to rush things of course....but equally, this must be something that everyone on here faces surely when using the wrapper (unless no one else has ever tried to connect to to browser), so if people with far more experience than me can't spot any obvious errors, I suspect you're right I am wasting my time a bit with Python, as a beginner course isn't going to help with websockets and I'm not going to figure this out unless I randomly stumble across a similar example.



That said I'll give PyCharm a go and see if it helps and report back if I make any progress.



Thank you for your help so far though, it has actually been very useful in understanding where the error might be, even if I haven't quite got there yet. From your advice, I can at least work out where the error probably is occurring, so that is much appreciated.

---

## 2019-02-09 20:33:02 - issues channel

**Newbie99**

appreciate you've already helped out a lot, however even with Visual Studio there are no errors thrown up by the debugger....it appears the code is functioning correctly...except of course its not. The issue is around the ping or emit, one or the other (or both) are not behaving as I would expect, but are not throwing up any errors (the debugger just shows the connections to the betfair streaming data as expected).



If I refresh the browser window (which I assume pings the server), the command line console refreshes, so somehow the emit part of the code is not firing. I'm guessing (but it is a guess), its to do with this section:



```

@socketio.on('ping')

def handle_message(_message):

    market_books = output_queue.get()

    print(market_books)

```



But as no error is thrown, I'm not really sure where to go from here!



Apologies again for the dumb questions, 'pure' scripting languages (e.g. Node.js / Python) are new to me and clearly I'm struggling with the logic a bit it would seem!

---

## 2019-02-09 17:22:40 - issues channel

**Newbie99**

Okay, sorry I'm back again and really confused!



This appears to connect, but doesn't seem to emit any messages:



```

import os

import logging

import queue



from flask import Flask, render_template

from flask_socketio import SocketIO



import betfairlightweight

from betfairlightweight.filters import (

    streaming_market_filter,

    streaming_market_data_filter,

)



app = Flask(__name__)

app.config['SECRET_KEY'] = secretkey

socketio = SocketIO(app)



@app.route('/')

def sessions():

    return render_template('index.html')



# setup logging

logging.basicConfig(level=[http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))  # change to DEBUG to see log all updates



# create trading instance (app key must be activated for streaming)

username = os.environ.get('username')

trading = betfairlightweight.APIClient(user_name,password,appkey,certs=cert_path)

trading.login()



# create queue

output_queue = queue.Queue()



# create stream listener

listener = betfairlightweight.StreamListener(

    output_queue=output_queue,

)



# create stream

stream = trading.streaming.create_stream(

    listener=listener,

)



# create filters (GB WIN racing)

market_filter = streaming_market_filter(

#    event_type_ids=['7'],

#    country_codes=['GB'],

#    market_types=['WIN'],

    market_ids=['1.130856098'],

)

market_data_filter = streaming_market_data_filter(

    fields=['EX_BEST_OFFERS', 'EX_MARKET_DEF'],

    ladder_levels=3,

)



# subscribe

streaming_unique_id = stream.subscribe_to_markets(

    market_filter=market_filter,

    market_data_filter=market_data_filter,

    conflate_ms=1000,  # send update every 1000ms

)



#start stream

stream.start(_async=True)





"""while True:

    market_books = output_queue.get()

    print(market_books)



    for market_book in market_books:

        print(

            market_book,

            market_book.streaming_unique_id,  # unique id of stream (returned from subscribe request)

            market_book.streaming_update,  # json update received

            market_book.market_definition,  # streaming definition, similar to catalogue request

            market_book.publish_time  # betfair publish time of update

        )"""



@socketio.on('ping')

def handle_message(_message):

    market_books = output_queue.get()

    print(market_books)



    for market_book in market_books:

        emit(

            'market_book',

            f'{market_book} '

            f'{market_book.streaming_unique_id} '

            f'{market_book.streaming_update}, '

            f'{market_book.market_definition}, '

            f'{market_book.publish_time} '

        )



if __name__ == '__main__':

    socketio.run(app, debug=True)

```

---

## 2019-02-07 18:38:51 - issues channel

**Newbie99**

thank you for your code snippet seaders, however maybe I'm being really dense, but it doesn't appear to be working. The client code says io isn't defined, so I tried with the sample code from the Flask page, which doesn't return an error, but still nothing happens. I feel that the problem is probably still with my server code, which is currently as follows. Python is very new to me, so this attempt at editing the streaming example, might be a bit poor, but as I don't get any errors, its a bit tricky to see where the problem is!



[code]

import os

import logging

import queue



import betfairlightweight

from betfairlightweight.filters import (

    streaming_market_filter,

    streaming_market_data_filter,

)



from flask import Flask, render_template

from flask_socketio import SocketIO



# setup logging

logging.basicConfig(level=[http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))  # change to DEBUG to see log all updates



# create trading instance (app key must be activated for streaming)

username = os.environ.get('username')





# create trading instance

trading = betfairlightweight.APIClient(user_name,password,appkey,certs=cert_path)



trading.login()



# create queue

output_queue = queue.Queue()



# create stream listener

listener = betfairlightweight.StreamListener(

    output_queue=output_queue,

)



# create stream

stream = trading.streaming.create_stream(

    listener=listener,

)



# create filters (GB WIN racing)

market_filter = streaming_market_filter(

    event_type_ids=['7'],

    country_codes=['GB'],

    market_types=['WIN'],

)

market_data_filter = streaming_market_data_filter(

    fields=['EX_BEST_OFFERS', 'EX_MARKET_DEF'],

    ladder_levels=3,

)



# subscribe

streaming_unique_id = stream.subscribe_to_markets(

    market_filter=market_filter,

    market_data_filter=market_data_filter,

    conflate_ms=1000,  # send update every 1000ms

)



# start stream

stream.start(_async=True)



"""

Data can also be accessed by using the snap function in the listener, e.g:

    market_books = listener.snap(

        market_ids=[1.12345323]

    )

Errors need to be caught at stream.start, resubscribe can then be used to

prevent full image being sent, e.g:

    streaming_unique_id = stream.subscribe_to_markets(

        market_filter=market_filter,

        market_data_filter=market_data_filter,

        conflate_ms=1000,  # send update every 1000ms

        initial_clk=listener.initial_clk,

        clk=listener.clk,

    )

The streaming unique id is returned in the market book which allows multiple

streams to be differentiated if multiple streams feed into the same queue.

"""



# check for updates in output queue

while True:

    market_books = output_queue.get()

    print(market_books)





    for market_book in market_books:

        print(

            market_book,

            market_book.streaming_unique_id,  # unique id of stream (returned from subscribe request)

            market_book.streaming_update,  # json update received

            market_book.market_definition,  # streaming definition, similar to catalogue request

            market_book.publish_time  # betfair publish time of update

        )



app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)



if __name__ == '__main__':

    socketio.run(app)



stream = None

queue = None





def get_queue():

    global queue, stream



    if not queue:

        stream, queue =  trading.streaming.create_stream(

    listener=listener,

)

    return queue



@socketio.on('ping')

def handle_message(_message):

    market_books = get_queue().get()

    print(market_books)



    for market_book in market_books:

        emit(

            'market_book',

            f'{market_book} '

            f'{market_book.streaming_unique_id} '

            f'{market_book.streaming_update}, '

            f'{market_book.market_definition}, '

            f'{market_book.publish_time} '

        )





if __name__ == '__main__':

    socketio.run(app)

    stream.stop()



[/code]

---

## 2019-01-31 18:38:25 - issues channel

**Newbie99**

Sorry...dumb question probably, this whole SSL thing is new to me...so if I create a key using Putty...which seems incredibly easy, then presumably there is no issue importing into the XCA gui and somehow signing a file there, which I can then export as a .crt file and upload to Betfair.



Just wanted to check that is the correct approach

---

## 2019-01-28 19:39:51 - issues channel

**seaders**

`pip install --upgrade betfairlightweight` should do it, shouldn't it?  1.8.2 is the latest on pypi - [https://pypi.org/project/betfairlightweight/](https://pypi.org/project/betfairlightweight/)

---

## 2019-01-28 19:38:53 - issues channel

**agberk**

yeah you've probably got an old version; `pip uninstall betfairlightweight` then `pip install betfairlightweight==1.8.2`

---

## 2019-01-28 19:34:52 - issues channel

**wsdlwizard**

I am getting 'betfairlightweight.exceptions.LoginError: API login: CERT_AUTH_REQUIRED' error after using the wrapper with no problems for months. I renewed my certificates and uploaded them to Betfair and used curl to get a successful login but it still gives me this error. I then did a pip install to see if the wrapper needed updating. Any ideas? Many thanks.

---

## 2019-01-05 16:19:37 - general channel

**Rob**

I realise this may be obvious but streaming is new to me - does `output_queue.get()` get all updates when called, or is it 1 after another?

---

## 2018-10-08 09:02:28 - general channel

**liam**

v1.8.0 released, minor bug fixes and 'LoginInteractive' endpoint added so a user can login without certs, note that this will fail if you have certs setup on your account  [https://github.com/liampauling/betfair/blob/master/HISTORY.rst](https://github.com/liampauling/betfair/blob/master/HISTORY.rst)

---

## 2018-09-11 18:19:30 - general channel

**Ian**

evening all - just a question about storage_engine - is this something I need to setup on amazon prior to running flumine?

---

## 2018-08-22 15:50:53 - general channel

**Matt P**

pretty new to this streaming business and its quite the learning curve!

---

## 2018-06-06 20:53:50 - general channel

**Mihai**

Hello guys, I'm new to Python &amp; after trying the steps mentioned here: [https://underround.wordpress.com/2017/07/05/historical-data/](https://underround.wordpress.com/2017/07/05/historical-data/) 

-&gt; I got the following error: AttributeError: 'APIClient' object has no attribute 'historical'. I've adapted both codes using the code from examplestreaminghistorical.py &amp; 



-&gt; After running the first code (updated based on xamplestreaminghistorical.py) I only get: 

INFO:betfairlightweight.streaming.stream:[Stream: None]: "MarketStream" created

INFO:betfairlightweight.streaming.stream:[MarketStream: HISTORICAL] 1.136292168 added



-&gt; After running the second code I get the below error:

Traceback (most recent call last):

  File "historic_data_2.py", line 44, in &lt;module&gt;

    listener=listener

  File "C:\Users\jdoe\AppData\Local\laragon\bin\python\python-2.7.13\lib\site-packages\betfairlightweight\endpoints\streaming.py", line 58, in create_historical_stream

    listener.register_stream('HISTORICAL', 'marketSubscription')

  File "C:\Users\jdoe\AppData\Local\laragon\bin\python\python-2.7.13\lib\site-packages\betfairlightweight\streaming\listener.py", line 25, in register_stream

    self.stream = self._add_stream(unique_id, operation)

  File "historic_data_2.py", line 33, in _add_stream

    unique_id, self.output_queue, self.max_latency, self.lightweight

  File "historic_data_2.py", line 16, in __init__

    super(HistoricalStream, self).__init__(unique_id, output_queue, max_latency, lightweight)

TypeError: __init__() takes exactly 2 arguments (5 given)



Could you please help? I'm trying to get the files in a readable format.

---

## 2018-06-02 13:37:11 - general channel

**Jonatan (skyw)**

Im going tro setup something with message queues later and spawn a thread that starts the stream in sync mode to catch those exceptions.

---

## 2018-03-27 12:48:22 - general channel

**istb**

I used pip install to install initially (which is when I got the issue):

```In [1]: import betfairlightweight



In [2]: betfairlightweight.__version__

Out[2]: '1.6.0'

```

But when making the changes I cloned from github master. Which is also 1.6.0.

Perhaps they are slightly different?

---

## 2018-03-07 18:19:35 - general channel

**Tom**

Hi, 

Do you know what credentials needs to be in the .bash_profile for logging into betfair with the api?

I have a dev key generated and I'm trying to follow the non interactive bot login documentation.



From the setup wiki this is the example for .bash_profile

export JohnSmith = "a4586nfgXY"

export usernamepassword = "password"



Should mine be?



export Tom = "zwefu45338"  # made up key

export usernamepassword = "123login" # made up password



I also have the bash profile set up in the bin folder of my virtualenv do you know is that ok for the login system to work?



Thanks,

Tom

---

## 2018-01-12 14:36:31 - issues channel

**mikey155**

I'm new to this site. I'm a python newbie, all of my existing apps written in Visual Basic. Following up the previous discussion on horses names, I'm now drilling into historical data, employing betfairlightweight. Your examplestreaminghistorical works as expected as is, but I'm finding errors (missing positional argument in RunnerBook) when I try to acquire horse names. I tried adding name to RunnerBook but get the same error. Probably a naive newbie error but I thought I'd try to get some insight here. Thanks in advance.

---

## 2018-01-12 13:38:19 - issues channel

**mikey155**

I'm new to this site. I'm a python newbie, all of my existing apps written in Visual Basic. Following up the previous discussion on horses names, I'm now drilling into historical data, employing betfairlightweight. Your examplestreaminghistorical works as expected as is, but I'm finding errors (missing positional argument in RunnerBook) when I try to acquire horse names. I tried adding name to RunnerBook but get the same error. Probably a naive newbie error but I thought I'd try to get some insight here. Thanks in advance.

---

## 2018-01-12 11:18:46 - general channel

**Ian**

Given I’m new to python mo code/debug workflow will be quite frequent lol

---

## 2018-01-12 06:51:35 - general channel

**Ian**

I’ve looked into this a bit more - taken a clean install of ubuntu and installed anaconda3, then bflw lib. same as MacOs - rec error when debugging. However,also same as MacOS, if I run outwith the VSCode IDE, it seems to run, I get what looks to be the correct output?

---

## 2018-01-11 19:00:07 - general channel

**Ian**

[@U5D4ZBEAG](@U5D4ZBEAG) thanks - I’m new to python and BF - c# dev

---

## 2018-01-01 17:26:55 - general channel

**liam**

Tom what are your trying to do? Looks like you have the working directory setup incorrectly. Regarding the other question, the variable name directory is misleading as it only does one file at a time, I think it did loop through a folder but I then changed it to make the code simpler 

---

## 2017-09-11 01:50:22 - issues channel

**gerg**

yes that is right [@U5D4ZBEAG](@U5D4ZBEAG) .. I am sorry for asking dump question, new to this so trying to understand the expected output.. I am running examplehistorical.py

---

## 2017-06-23 19:49:35 - general channel

**gerg**

Im new to this group..How can I use this to get historical data of item soccer of year 2016 ? Any help is greatly appreciated

---

## 2017-06-10 20:27:16 - general channel

**Evaldas**

oh gee, I understand now. get data from stream and put it into market/strategy object, took me a while, kinda new to this :slightly_smiling_face: thanks

---

## 2017-06-09 17:03:01 - general channel

**magiclevinho**

Traceback (most recent call last):

  File "C:\Program Files\JetBrains\PyCharm Community Edition 2017.1.3\helpers\pydev\pydevd.py", line 1585, in &lt;module&gt;

    globals = debugger.run(setup['file'], None, None, is_module)

  File "C:\Program Files\JetBrains\PyCharm Community Edition 2017.1.3\helpers\pydev\pydevd.py", line 1015, in run

    pydev_imports.execfile(file, globals, locals)  # execute the script

  File "C:/Users/john/Documents/Pythonprojects/betfair_00/main.py", line 27, in &lt;module&gt;

    in_play_only=True,

  File "C:\Python27\lib\site-packages\betfairlightweight\endpoints\betting.py", line 84, in list_events

    (response, elapsed_time) = self.request(method, params, session)

  File "C:\Python27\lib\site-packages\betfairlightweight\endpoints\baseendpoint.py", line 43, in request

    raise APIError(None, method, params, 'ConnectionError')

betfairlightweight.exceptions.APIError: SportsAPING/v1.0/listEvents 

Params: {'filter': {'eventTypeIds': [u'1'], 'inPlayOnly': True}} 

Exception: ConnectionError

---

## 2017-06-08 09:55:25 - general channel

**agberk**

Anyone have experience with python requirements.txt files? I've got three packages, A, B, C. A depends on B and B depends on C. They're all in private repos so I'm specifying the github URL in the requirements file. In A's requirements file I list B's URL, and in B's requirement's I list C's URL, however when trying to install A's requirements it goes to try and install B and complains it can't find C. Do I have to list my dependency's dependencies in the requirements file? Seems like it defeats the point...

---

## 2017-06-03 11:15:34 - general channel

**jfo**

`python setup.py test`

---

## 2017-05-27 23:34:26 - general channel

**heedfull**

Hi folks getting this error when running `python setup.py test` 

```

ImportError: Failed to import test module: test_accountresources

Traceback (most recent call last):

  File "/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6/lib/python3.6/unittest/loader.py", line 153, in loadTestsFromName

    module = __import__(module_name)

  File "/betfairlightweight/tests/test_accountresources.py", line 8, in &lt;module&gt;

    from tests.tools import create_mock_json

  File "/betfairlightweight/tests/tools.py", line 1, in &lt;module&gt;

    from mock import Mock

ModuleNotFoundError: No module named 'mock'

```

---

## 2017-05-22 16:12:04 - general channel

**liam**

I'll be honest my process changes almost weekly and is more focussed around budget, want to do a blog post on this topic soon. Are you new to AWS? Because you can run a ec2.micro for free for a year which is what I originally did. I now zip and store json in s3 as soon as a market is complete, much cheaper than db storage 

---

## 2017-05-20 12:44:21 - general channel

**liam**

so the django app (called pinhole) is setup to record order/strategy data and some market level data. When it comes to recording market book data i zip that up and send it to s3, then have lambda process which includes parsing and loading to MySQL depending on market type or simply adding a record of what it is into pinhole which I can then query to get the bucket location for back testing or processing later. But yeh if you want to record/log something else you have to create a model/migrate/build the view/add to the api so its limited in that respect. But that is what elasticsearch is good for which i use for logging as it can pretty much take anything you chuck at it

---

## 2017-05-17 14:41:58 - general channel

**liam**

docker speeds things up for me, can go from no ec2 instances available to a program running and i just have to install docker

---

## 2017-05-12 08:39:16 - general channel

**jfo**

i'm new to python so interesting stuff :slightly_smiling_face:

---

## 2017-04-17 19:30:13 - general channel

**jfo**

[@U4H19D1D2](@U4H19D1D2) got any tips for install flumine with `pip` ?

---

## 2017-04-12 20:07:43 - general channel

**jfo**

[@U4JSCQ05N](@U4JSCQ05N) this any good? [http://stackoverflow.com/questions/19042389/conda-installing-upgrading-directly-from-github](http://stackoverflow.com/questions/19042389/conda-installing-upgrading-directly-from-github)

---

