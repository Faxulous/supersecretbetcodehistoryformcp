# Feature Engineering - Community Knowledge

*531 relevant conversations from across all channels*

---

## 2025-01-22 09:36:32 - general channel

**Justice**

Interesting thread and discussion. None of my models have any idea about the market price. Adding this information to my model causes it to become highly correlated to the market and dilutes the other signals/features I'm using. I find this has a large adverse affect on my turnover and therefore profit. Perhaps I need a more sophisticated approach rather than just using it as another feature

---

## 2025-01-21 19:06:09 - general channel

**liam**

Yes, reducing reliance on the model, not sure why but it's not spoken much on here or elsewhere but I know a few pros/syndicates use the market price as a valuable source of info/feature, even if its at the final stage inbetween model/execution

---

## 2025-01-21 18:58:49 - general channel

**liam**

Doesn't have to be price action, a fundamental model can/would use the market price for features / filtering etc.

---

## 2025-01-15 15:44:55 - strategies channel

**Matt**

> When those talk about time series, do you think they are referring to some unobservable latent measure of team performance, or time series of prices on a runner?

it is more of conceptually around *metric  or feature volatility*, *not Market Volatility*. (and i look it from a more pure model building POV)

Time series, especially in NBA (or sports with a lot of matches in a season), around performance of players and teams seems to be a neglected statistic. Things like a RAPM are great for a player metric in NBA, but adding a feature of volatility, hurst, etc to that players epm also lets the model know how chaotic that players performance is or if its mean reverting (depending on what you are using for time analysis).



If you sort NBA players by their RAPM strength (lets say DEC 1) and then do it again FEB 1, people that are more consistant will be at the top both times, and people that were (or arrived) at the top have higher variance. this as an added feature will let a model understand this.



in the end, i think it can be a signal of latent states (maybe seeing some player, lineup or team that all stabilized, or went volatile. But the intention is to let the model you are building know that "this person is playing erratic for this metriuc, this person is playing consistant for this metric, this team is...)

[@UPMUFSGCR](@UPMUFSGCR)

---

## 2025-01-14 15:43:33 - strategies channel

**Justice**

For what it's worth, the first 2 things I look at are calibration (as done above but with a 95% CI) and then, I plot the distribution of probabilities from my model and BSP and compare. This quickly highlights if there's a problem discriminating short/long prices. I'd then isolate those cases and analyse what pieces of information my model is missing using domain knowledge (of which I have none for dogs). I'd then attempt to encode this information into the features for my model

---

## 2025-01-09 09:20:32 - strategies channel

**Jonjonjon**

I totally agree with that. However, when I tested adding time/date features to my model they didn't improve it:disappointed: . So while we can easily observe that volumes vary by hour and day of week, I haven't been able to use it for anything useful.:disappointed:

---

## 2025-01-07 13:29:23 - general channel

**birchy**

Inspired by [@UBS7QANF3](@UBS7QANF3)'s thread, I thought I'd better try to calculate my Sharpe Ratio, which I've never done before. Can someone please confirm if this is correct? It's in a jupyter notebook where my dataframe is populated from flumine bet logs.







`def calc_sharpe(df, period='D'):

    # Create a copy of the dataframe

    d = df.copy()`



    `# Ensure datetime index

    if not isinstance(d.index, pd.DatetimeIndex):

        d.set_index('date_time_created', inplace=True)`



    `# Calculate liability and ROI

    d['liability'] = d['size_matched'] * (d['price_matched'] - 1)`



    `# Filter for matched bets

    df_matched = d[d['liability'] &gt; 0]`



    `# Calculate period returns (weighted by liability)

    period_profits = df_matched.groupby(pd.Grouper(freq=period))['profit'].sum()

    period_liabilities = df_matched.groupby(pd.Grouper(freq=period))['liability'].sum()

    period_returns = period_profits / period_liabilities`



    `# Filter out null periods

    period_returns = period_returns[period_returns.index.notnull()]`



    `# Calculate metrics

    avg_return = period_returns.mean()

    volatility = period_returns.std()

    sharpe_ratio = np.sqrt(len(period_returns)) * (avg_return / volatility) if volatility != 0 else 0`



    `# Calculate summary statistics

    total_bets = len(df_matched)

    total_profit = round(df_matched['profit'].sum(), 2)

    total_liability = round(df_matched['liability'].sum(), 2)

    overall_roi = total_profit / total_liability if total_liability &gt; 0 else 0`



    `return {

        'sharpe_ratio': sharpe_ratio,

        'average_return': avg_return,

        'volatility': volatility,

        'periods_analyzed': len(period_returns),

        'total_matched_bets': total_bets,

        'total_profit': total_profit,

        'total_liability': total_liability,

        'overall_roi': overall_roi

    }`



`sr = calc_sharpe(df, period='D')

for k, v in sr.items():

    print(f'{k}: {v}')`



---

## 2025-01-06 16:01:12 - random channel

**Mo**

Saw this paper "Maximizing Betting Profitability Through Predictive Modeling in European Football: A Feature-Driven Approach" shared on LinkedIn: [https://drive.google.com/file/d/1XOwLye3mxIyVEbFA1KrKbYOpYd0Lcloy/view](https://drive.google.com/file/d/1XOwLye3mxIyVEbFA1KrKbYOpYd0Lcloy/view)

---

## 2025-01-05 17:26:17 - strategies channel

**D C**

[@U01PJ5YMFBJ](@U01PJ5YMFBJ) just a suggestion, but have you thought of trying some fundamental modelling instead of purely market signal type approaches. Something pretty basic just to give you a better idea of model building and regression? Your talk of just throwing shitloads of features into a NN suggests that you are hoping to just stumble across something.

---

## 2025-01-05 13:31:51 - strategies channel

**Dave**

Complexity is not necessarily a bad thing (for instance if you use a tree or NN model then likely the decisions they make are far more complex than your handcrafted ifs). However typically the relationship between features and target is observable/make practical sense, so even if your logic is mostly a black box / super complicated, a simple regression of feature Vs target would suggest "yes it makes sense to include this feature/indicator". But if you don't practice good hygiene with train/test splitting / avoiding leakage etc, or simply don't use enough data, then you will have a useless model. And ofc this isn't specific to ML models, despite the terminology. Stuff like "it only works on odds of 8 and above" is _likely_ overfitting.

---

## 2024-12-24 19:11:09 - strategies channel

**Dave**

I am just trying to provide some evidence that, contrary to everyone telling [@U01PJ5YMFBJ](@U01PJ5YMFBJ) that he has no edge, that he may in fact have an edge but a) it doesn't stand the test of time because it just isn't modelled well enough and his features may just need to be more time-invariant, or b) simply he was relying on external behaviour which is no longer present. I noticed a step change in behaviour around June too, so I suspect a change in external factors :slightly_smiling_face:

---

## 2024-12-18 19:20:16 - strategies channel

**birchy**

Brilliant! I've been using a much simpler affair and analysing in pandas afterwards:



`def process_orders(self, market, orders):

    if not orders: return

    ltps = {r.selection_id: r.last_price_traded for r in market.market_book.runners if r.last_price_traded}

    for o in orders:

        if not o.elapsed_seconds: continue

        # update ev min/max

        if (

            o.elapsed_seconds &gt; 0

            and o.elapsed_seconds &lt;= 5

        ):

            ltp = ltps.get(o.selection_id)

            if ltp:

                o.notes['ev_ltp_min'] = min(o.notes['ev_ltp_min'], ltp)

                o.notes['ev_ltp_max'] = max(o.notes['ev_ltp_max'], ltp)`

---

## 2024-12-16 20:30:32 - strategies channel

**Gooat**

Broadly speaking could a middleware solution insert the bets into a market and create the trade objects? Or should I jump to Pandas?

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

## 2024-10-31 12:08:06 - issues channel

**frank**

Hi, I'm trying to login to betfair api. but this code, gives me an ssl error. :  `# Import libraries`

`import betfairlightweight`

`from betfairlightweight import filters`

`import pandas as pd`

`import numpy as np`

`import os`

`import datetime`

`import json`



`# Change this certs path to wherever you're storing your certificates`

`certs_path = r'C:\certs'`



`with open('credentials.json') as f:`

    `cred = json.load(f)`

    `my_username = cred['username']`

    `my_password = cred['password']`

    `my_locale= cred['locale']`

    `my_app_key = cred['app_key']`



`trading = betfairlightweight.APIClient(username=my_username,`

                                       `password=my_password,`

                                       `locale=my_locale,`

                                       `app_key=my_app_key,`

                                       `certs=certs_path)`



`trading.login()`   errorse is the following: `Exception: HTTPSConnectionPool(host='[http://identitysso-cert.betfair.com|identitysso-cert.betfair.com](http://identitysso-cert.betfair.com|identitysso-cert.betfair.com)', port=443): Max retries exceeded with url: /api/certlogin (Caused by SSLError(SSLError(524297, '[SSL] PEM lib (_ssl.c:3905)')))`  any help would be very appreciated. Thanks

---

## 2024-10-17 11:32:30 - issues channel

**NT**

I have, I'm just not the greatest coder and need some time to figure out how to use it appropriately in my algorithm. Lack of coding skill is honestly probably the root cause of my keep alive issues too. Thankfully, other than the keep alive, the code is running quite well and generating profit.



It is definitely on my to do list to learn how to use flumine to get a stream reading of prices to a dataframe for use on my algorithm. It would save me having to call the BFLW API on a loop.

---

## 2024-10-14 10:33:11 - strategies channel

**liam**

Weird as it lets me search it but then the link doesn't work



&gt; 

&gt; 

&gt; *liam*  [3:24 PM]

&gt; Does anyone know how much Decimal charge for the Cricket feed?

&gt; 49 replies

&gt; 

&gt; 

&gt; 

&gt; 

&gt; 

&gt; *Robert*  [3:55 PM]

&gt; I'm on the hunt for a decent feed too!

&gt; 

&gt; 

&gt; 

&gt; *D C*  [4:02 PM]

&gt; Is it just a score feed? Is Betfair's not up to scratch?

&gt; 

&gt; 

&gt; 

&gt; *liam*  [4:05 PM]

&gt; No comment

&gt; 

&gt; 

&gt; 

&gt; *D C*  [4:06 PM]

&gt; Understood

&gt; 

&gt; 

&gt; 

&gt; *liam*  [9:10 AM]

&gt; I have sent an email, will share the price if they do however I fear it might be out of my budget

&gt; 

&gt; 

&gt; 

&gt; *Mo*  [9:56 AM]

&gt; I can give you a personal introduction if you don’t get anywhere

&gt; 

&gt; 

&gt; 

&gt; *Robert*  [11:22 AM]

&gt; I think the main issue, not just for cricket, is Betfair's inability to use the widely accepted team or players names.

&gt; 

&gt; 

&gt; 

&gt; *Robert*  [3:15 PM]

&gt; And the inability to match names strikes again :expressionless:

&gt; 

&gt; 

&gt; 

&gt; *liam*  [3:36 PM]

&gt; It's a complete fucking joke tbh, almost 3 years this has been in 'production'

&gt; 

&gt; 

&gt; 

&gt; *Robert*  [3:48 PM]

&gt; you would have thought, it being the same team causing the issue as yesterday, they might have pre-empted it .....

&gt; 

&gt; 

&gt; 

&gt; *Lee*  [3:49 PM]

&gt; what issues are you seeing [@U4H19D1D2](@U4H19D1D2)?

&gt; 

&gt; 

&gt; 

&gt; *liam*  [3:51 PM]

&gt; The usual ongoing mapping issues and there is some sort of bug with the Lancashire game which is pushing out about a million updates per second on certain connections, seems like they just don't care

&gt; 

&gt; 

&gt; 

&gt; *Mo*  [6:11 PM]

&gt; Wow, looks like this is bringing down my entire scraping infrastructure

&gt; 

&gt; 

&gt; 

&gt; *liam*  [6:19 PM]

&gt; Try restarting, doesn’t seem to be on every connection

&gt; 

&gt; 

&gt; 

&gt; *Mo*  [6:21 PM]

&gt; Better but the damage has already been done

&gt; 

&gt; 

&gt; 

&gt; *Lee*  [6:22 PM]

&gt; nice to know the cricket feed could take down all my recording

&gt; 

&gt; 

&gt; 

&gt; *Mo*  [6:23 PM]

&gt; Well your mileage may vary depending on how much disk space your box has and whether you have appropriate alerts set up

&gt; 

&gt; 

&gt; 

&gt; *D C*  [6:24 PM]

&gt; Is this a recent problem or  long term? Just wondering if it's related to my recent server reboot as I am recording the cricket score feed on said server.

&gt; 

&gt; 

&gt; 

&gt; *liam*  [7:53 PM]

&gt; Recent, started today at 11:45ish, apparently now fixed

&gt; 

&gt; 

&gt; 

&gt; *liam*  [8:21 AM]

&gt; Looks like either it was never fixed or it started happening again today at about 1am

&gt; 

&gt; [8:22 AM]

&gt; 

&gt; This file is hidden because it was uploaded more than 90 days ago. [https://betcode-org.slack.com/plans?feature=unlimited_messages|Upgrade to a paid subscription](https://betcode-org.slack.com/plans?feature=unlimited_messages|Upgrade to a paid subscription) to view.

&gt; 

&gt; 

&gt; 

&gt; 

&gt; *Robert*  [12:10 PM]

&gt; My machine must have been smoking, I wonder what's going on... (edited)

&gt; 

&gt; 

&gt; 

&gt; *liam*  [12:29 PM]

&gt; eventide issues apparently

&gt; 

&gt; [http://docs.eventide-project.org/](http://docs.eventide-project.org/)

&gt; 

&gt; 

&gt; *[http://docs.eventide-project.org|docs.eventide-project.org](http://docs.eventide-project.org|docs.eventide-project.org)*

&gt; *[http://docs.eventide-project.org/|Eventide](http://docs.eventide-project.org/|Eventide)*

&gt; Pub/Sub, Event Sourcing, Evented Microservices

&gt; 

&gt; 

&gt; 

&gt; *Gooat*  [6:48 PM]

&gt; Any ball park price numbers come back?

&gt; 

&gt; 

&gt; 

&gt; *liam*  [7:03 PM]

&gt; Nope

&gt; 

&gt; 

&gt; 

&gt; *liam*  [11:29 AM]

&gt; For those interested

&gt; 

&gt;&gt; You are more than welcome to come direct but we do have a minimum fee for direct customers that may be prohibitive to you of £2k per month and £150 per game.

&gt; 

&gt; 

&gt; 

&gt; *D C*  [11:46 AM]

&gt; 2K a month AND £150 a game. No idea if that's cheap or expensive to be fair

&gt; 

&gt; 

&gt; 

&gt; *Mo*  [11:48 AM]

&gt; Expensive compared to other sports but there’s easily enough liquidity in a match to extract that much EV

&gt; 

&gt; 

&gt; 

&gt; *liam*  [12:18 PM]

&gt; I read that as £150 a game, minimum 2k a month.

&gt; 

&gt; Update on the betfair feed is that I have continued hounding Neil to the point they have made some changes to the 'team' lots of politics/stupid code freezes but things have improved

&gt; 

&gt; 

&gt; 

&gt; *Lee*  [12:20 PM]

&gt; I noticed last month there was a big jump in quantity of matches with the feed. Up around 100 matches.

&gt; 

&gt; [12:20 PM]

&gt; Is that seasonal or from the improvements?

&gt; 

&gt; 

&gt; 

&gt; *liam*  [12:21 PM]

&gt; Both but we are now down to missing about 15% of the matches due to mapping, there where times last year where it was around 50%

&gt; 

&gt; 

&gt; 

&gt; *Lee*  [12:22 PM]

&gt; Big improvement

&gt; 

&gt; 

&gt; 

&gt; *Lee*  [2:03 PM]

&gt; How do you work out which markets are missing the feed?

&gt; 

&gt; 

&gt; 

&gt; *liam*  [2:09 PM]

&gt; nightly script to reconcile between market/feed data

&gt; 

&gt; 

&gt; 

&gt; *Lee*  [2:12 PM]

&gt; are we expecting every cricket match to have the feed?

&gt; 

&gt; 

&gt; 

&gt; *liam*  [2:13 PM]

&gt; pretty much, expect sub ~3% to not have a feed depending on what betfair put up

&gt; 

&gt; 

&gt; 

&gt; *Gooat*  [5:38 PM]

&gt; Has anyone levelled up to big stakes from the feed?

&gt; 

&gt; 

&gt; 

&gt; *liam*  [5:58 PM]

&gt; I am up to a few k exposure per market

&gt; 

&gt; 

&gt; 

&gt; *Gooat*  [6:02 PM]

&gt; Nice. Model or mix of price and flow? I struggled to avoid averse selection when testing it.

&gt; 

&gt; 

&gt; 

&gt; *liam*  [6:08 PM]

&gt; model

&gt; 

&gt; 

&gt; 

&gt; *Gooat*  [9:28 PM]

&gt; How did that game go?

&gt; 

&gt; 

&gt; 

&gt; *Sen*  [2:32 PM]

&gt; On this note - [@U4H19D1D2](@U4H19D1D2) how do you know Decimal is the best data provider in the cricket space? Something you've been able to test? (edited)

&gt; 

&gt; 

&gt; 

&gt; *liam*  [2:36 PM]

&gt; I don't, its just the one betfair provide

&gt; 

&gt; 

&gt; 

&gt; *Mo*  [2:37 PM]

&gt; I can say that the people behind it have been involved in cricket data for at least a decade

&gt; 

&gt; 

&gt; 

&gt; *Sen*  [3:15 PM]

&gt; Another option is sportmonks - they look pretty decent too

&gt; 

&gt; 

&gt; 

&gt; *liam*  [3:15 PM]

&gt; Yeah, considerably cheaper

&gt; 

&gt; 

&gt; 

&gt; *D C*  [4:31 PM]

&gt; Has the Betfair cricket feed not improved ?

&gt; 

&gt; 

&gt; 

&gt; *liam*  [7:23 PM]

&gt; Yes it has but it’s been hard work (for myself and Neil)



---

## 2024-10-02 12:21:45 - random channel

**Leo**

Depends how you model time series. I just chuck it all In a lightgbm model and you can use lagged features of both river levels and rainfall 

---

## 2024-09-26 16:09:52 - random channel

**ShaunW**

Haven't used o1 yet but I'm finding the new 'memory' feature to be a blessing and a curse. Once it's on the wrong track it's always been stubbornly wedded to it and those errors in understanding now compound across conversations.     I'm closing some convos with 'don't commit this to memory' because of it. The memory feature also raises new privacy issues imo.

---

## 2024-09-15 01:04:49 - strategies channel

**Gooat**

I always wonder about many small models/ratings v many features and dealing with it in OMS.

---

## 2024-09-14 08:52:36 - general channel

**Justice**

[@UUE6E1LA1](@UUE6E1LA1) To sum up my current workflow: data analysis, visualization, model development, backtesting all done in Python (backtesting done directly in a polars dataframe, not with flumine). All this is just strewn around in various notebooks with no real thought. Export trained model via ONNX to C# codebase for production use

---

## 2024-09-13 20:08:05 - general channel

**Justice**

[@U012XF5CNPN](@U012XF5CNPN) Is that just your backtesting/strategy logic? Or do you literally have the entire process in a single file including data processing, cleaning, feature creation, model training etc.

---

## 2024-09-12 18:48:45 - strategies channel

**Justice**

[@U4H19D1D2](@U4H19D1D2) Yeh I just have level stake fixed liability at the moment. I used to use flumine. I have my own trading framework written in C# for production code. And I do backtesting using a custom Rust plugin for polars dataframes

---

## 2024-08-28 22:44:08 - random channel

**Rob**

a few guesses...



• if you're building lots of models because you're segmenting upfront (e.g. a separate model for close to the off vs the day before) I'd try skipping this and building a model across all segments (e.g. include time before the off as a feature), as ML models can do a good job of replicating this segmentation

• if you're building lots of models because you're trying lots of hyperparameters, there are bayesian methods that should find the optimal set faster

---

## 2024-08-21 08:26:15 - strategies channel

**Derek C**

for multi-processing with backtesting, I typically would have different markets going to each process and then a separate output file for each that is named after the process, e.g. from Python mp.current_process().name. Easy to then split/concatenate this data in Pandas as needed afterwards.

---

## 2024-08-18 12:44:45 - strategies channel

**Peter**

[@U016TGY3676](@U016TGY3676) If you're using the same paginator object, then they should be the same. But if you're creating a new paginator object because the session is interrupted, then there's no guarantee.



However, there may be a better way of handling this anyway. I use the S3 inventory feature to get a daily list of objects (or subsets with a key prefix) dumped into a bucket in parquet format (csv format also available). It gives you the same data but without the the need for iterating over a bonkers number of pages.



There are some limitations:

• The list is available no more frequently than daily (weekly or month are also available), but at a time determined by AWS, you have no control over this.

• Even when it arrives the data is typically 12 or more hours out-of-date, I suspect because they run the report against cached data.

But unless you need bang up-to-date data (which would be difficult anyway with buckets containing 1mn plus objects and the most recent at the end of the pagination), these probably aren't big issues. They haven't been for me.

---

## 2024-08-12 09:37:25 - general channel

**Sen**

Mostly because the 5 day lag doesn't have a meaningful effect on 95% of features for my fundamental model. Then I just get the data from betfair 5 days later for modelling purposes. But given my fears about my data quality... I'm now very much thinking about recording and storing

---

## 2024-08-07 07:10:03 - random channel

**Tom**

IMO Taleb rationalised his luck in the '87 crash, not just with the money he received being the result of some high minded trading strategy, but into a feature of intellectual superiority.

---

## 2024-08-07 00:47:54 - strategies channel

**Gabriel Mocan**

Have you guys heard about QuestDB? I’m using it for my greyhound strategies. It’s a very optimized database for time series and finances, with a lot of useful specialized time functions. Performance is a key feature of it.





---

## 2024-08-06 13:15:57 - strategies channel

**birchy**

With horse racing the pre play liquidity has dropped off a lot but there's a significant amount matched inplay, sometimes more than was matched at the off time. I've been hacking around with modelling recently and have had some success with a basic LR model that has about 30 features that are all market data based, but there are 3 or 4 features/signals that are particularly stronger than the others. Engineering features is a trivial exercise but finding good ones is much harder. I took the approach of using lots of features and then dropping the shit ones until I had something production ready. I'm not really a fan of the 'black box' approach but it seems to understand the market nuances better than I do. The bottom line is that it's bringing in some £'s, so I'm slowly convincing myself that it's a much easier route to take.

---

## 2024-08-06 09:52:51 - strategies channel

**AndyL**

[@UGV299K6H](@UGV299K6H) sorry I meant a simple linear feature model, so my example previous was a simple linear model using the 3 core features: volume, queued and matched 

---

## 2024-08-06 07:52:30 - strategies channel

**Michael**

_"trying to find a single linear feature model"_



Yeah - that aint gonna work.

---

## 2024-08-06 07:51:14 - strategies channel

**AndyL**

Thanks chaps, it’s a tricky one horses are definitely competitive and liquidity reducing but I feel I’ve invested a lot of effort already which I feel would be wasted moving to football. As to prerace vs inplay thats a tricky one too, im currently feeling an attraction to the high volatility of inplay at the moment.

My modeling I think is a bit too simple and trying to find a single linear feature model doesn’t possibly fit the opportunities I am trying to find…maybe!

Anyway I think ive been talking too much and not getting down to it….

Cheers all

---

## 2024-08-04 15:34:35 - general channel

**Jonjonjon**

The thing with the models above is that they often won't make much difference. Or if the model makes a difference and you have a good understanding of your features, you can transform them so that even linear regression works.

---

## 2024-08-04 10:17:32 - general channel

**John Foley**

a gradient boosting model requires very few (if any) assumptions about distributions etc. handles outliers and strange distributions well. handles complicated interactions between features and handles missing data. feature selection is somewhat "built-in." performance is comparable to deep learning algos for simple tabular data

---

## 2024-08-03 21:58:19 - general channel

**Michael**

So I'm going to admit that I don't do "proper" regression. I just plot my features, look at the plots, rub my face, think about it, make up something plausible and try it.



Every once in a while I get all anxious that I should have done it properly, so I make a big effort and do xgboost or whatever, then I test that against my "eyeball" criteria and either the eyeball wins or the difference is trivial.



My general experience is that there are huge gains to be found when I find a new feature but overly stressing on the model doesn't yield much.

---

## 2024-07-30 09:30:55 - general channel

**AndyL**

[@UPMUFSGCR](@UPMUFSGCR) ev vs bsp gives you an idea if your pre race strategy is beating BSP overall, a cum plot is a good way if visualizing it

Basically you need to stash the reconciled BSP after inplay, I actually just do it in the closed_market callback, then in your analysis/pandas simply merge it with your matched bet data in order to plot…

---

## 2024-07-29 20:20:02 - general channel

**Unknown**

[@U4H19D1D2](@U4H19D1D2) 7mins , my Pandas is improving :slightly_smiling_face:

---

## 2024-07-29 20:11:54 - general channel

**AndyL**

I have BSP, just got to join in pandas

---

## 2024-07-29 10:08:00 - general channel

**Mo**

Pandas Fu equivalent to tidyverse Fu [@UUE6E1LA1](@UUE6E1LA1)

---

## 2024-07-29 09:29:51 - general channel

**Michael**

Have you given it a go? The whole pandas, numpy and jupyter labs/notebooks is excellent for analysis.

---

## 2024-07-29 09:28:43 - general channel

**D C**

Oh python pandas. I don't use pandas. Truth be told I only use python to insert my bot logs into a DB. But yeah I am sure I can do something that requires not much effort

---

## 2024-07-29 09:27:38 - general channel

**Michael**

I just meant use pandas, groupby market etc.

---

## 2024-07-29 09:27:09 - general channel

**Michael**

Pandas + kung fu.

---

## 2024-07-29 09:26:52 - general channel

**D C**

Pandas Fu?

---

## 2024-07-29 09:26:09 - general channel

**Michael**

Surely you can just take your betting data and do some Pandas Fu?

---

## 2024-07-17 12:11:22 - random channel

**Mo**

With `pystan` and `numpy/pandas` there's really no reason to miss out on what I suspect will be excellent material just because you're dogmatic about programming languages

---

## 2024-07-17 08:03:11 - issues channel

**Herugrim**

How can I add a worker to a Flumine instance to refresh a dataframe every 60 seconds?



I've created a dataframe before starting the framework and loaded it into the framework, but I'm going to asynchronously refresh the dataframe every 60 seconds, and need the Flumine instance to update with this new dataframe

---

## 2024-07-11 20:11:26 - strategies channel

**birchy**

Don't fret [@UPMUFSGCR](@UPMUFSGCR). I run flumine simulation on a $20 AWS Lightsail instance to generate 'features' CSV's and then train models on Google Colab. My strategies are unsophisticated, so 5K markets takes an hour or so to run and model takes &lt; 10 minutes to train with ~30 features. I've set a limit of 5k markets so I can get results fairly quickly and that's working for me. I take the view that if a strategy needs &gt; 5k markets to make a profit, then it's not viable in the real world.

---

## 2024-07-07 15:16:18 - general channel

**Jonjonjon**

I'd advise against using Pandas for this as it could be too slow.



I use Numba to store the data in linked lists.

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

## 2024-07-06 10:06:57 - general channel

**birchy**

I'm in the process of tidying up my code and working on some new features. I know it's not 'best practice', but in Flumine, would adding my own object like this `market.abc = myobject()` be safe? Or should I just use `market.context`?

---

## 2024-06-16 23:56:22 - random channel

**Rob**

I tend to work in RAM, would consider:



• don't store every row if you don't need to - does every row change every tick? if not, store each unique once with a from/to datetime

•  use the smallest possible data types

• do feature engineering or get feature importance on a smaller sample, and then build your model on a much dataset of columns that amtter  - obviously YMMV, but I don't build models with the full set of traded volumes at every price

• sample - lots of the time, you're not going to get a massively different answer with a subset that does fit in RAM

• buy more RAM (it's relatively cheap compared to the time you're investing - 128Gb of DDR5 isn't crazy)

• get it working locally on a sample, then use a cloud server (e.g. EC2) to fun your full build

---

## 2024-06-16 19:45:56 - random channel

**Jonjonjon**

I store in feather using Pandas. how you store and organise the data has a big effect. Might be worth looking at how HFT's store and manage their data. It's very valuable knowledge.



Also,  it's one of the few areas where the nonsense software engineers get tested on in interviews actually might have relevance.

---

## 2024-06-16 18:58:27 - random channel

**Dave**

Outside of flumine I use the historical generator stream from bflw, replay the files and handle it tick by tick. You don't need all ticks going back to when the market was open, so you can cache the bits you need yourself as you process each next tick. The advantage here as well is that this is how you'll process market data in production, so you can run the same logic for things like feature generation for both historical and realtime data.

---

## 2024-05-25 01:55:06 - strategies channel

**Troy Edwards**

I'm hearing you :slightly_smiling_face:  I have been playing around with Lasso/Ridge and reduced my data features down to 10.  I then created different models using different data features with one meaning static as in does not rely on odds or volume for Australian Greyhounds Markets.



Train/tested well.  Then after 5 days of validation 4 of those models broke (for that day anyway) but I will continue to validate over a few weeks as to the see the overall effect.



Maybe you should just continue to validate as sometimes one/two bad days is just part of that variance

---

## 2024-05-16 11:56:19 - random channel

**Ralegh**

I think ridge+feature engineering given enough time and ideas may be sota but for stuff like HFT I have heard deep learning, (and also deep RL for execution/optimiser). There’s just so much data and you can fit to it quickly eg blackrock deploying a new execution algo could be factored in if you recalibrated every day but those transient signals might not fit into features that you’ve come up with historically unless you were literally coming up with new ideas every day. 



I think XTX is pretty big on deep learning and their whole thing is taking large positions while making markets so I assume their forecasts are good. That being said regression is like concrete or steel and probably is the final arbiter of what goes in a forecast.



Also ridge + features are a lot handier for transfer learning. If you moved to a new market with little historical data you’d feel pretty confident just copying stuff across. Would be easier to manipulate and remove features (weight = 0) without the required data in the new market than trying to break apart a web of neural network shenanigans. If I’ve learned anything from success stories the easiest way to make money is take a good strategy and apply it to an inefficient/new market.

---

## 2024-05-16 11:33:04 - random channel

**river_shah**

Yes, the thing is in his preamble he goes on precisely how the model is being constructed. So you know why not do that extra step, write some of the features out by hand (rather than lstm hidden representations) and fit ridge with GCV and show us the full multi horizon alpha term structure. I'd bet even this basic approach matches lstm illustrated performance (let alone what can be achieved by grinding harder at the problem use ridge + domain knowledge)

---

## 2024-05-16 11:22:57 - random channel

**river_shah**

The Kolm paper is good but feature engineering + ridge is still SOTA. It's too bad he does not have that as the baseline model

---

## 2024-05-11 21:04:52 - general channel

**birchy**

_"you can use heartbeat to cancel all unmatched bets"_



We're all well aware of this API feature. The question is...can PENDING bets be cancelled? To clarify, a pending bet is not yet executable.

---

## 2024-05-07 09:32:59 - issues channel

**Adrian**

Ok yep, got it to the next step. It runs the first cell but encounters KeyError: 'name' in the second cell :

`df = pd.merge(df, df_strategies, left_on="trade__strategy", right_on="name", how="left")`

There's no 'name' column in any of the dataframes

---

## 2024-05-06 14:00:51 - general channel

**Adrian**

What is pandas doing that destroys the effieciency so much

---

## 2024-05-06 13:57:54 - general channel

**liam**

Looks like some super slow pandas 

---

## 2024-05-05 09:42:11 - strategies channel

**Rob**

For pandas this is very inefficient, but I very much subscribe to worrying about things that materialise. e.g. [https://stackify.com/premature-optimization-evil/](https://stackify.com/premature-optimization-evil/)



Compute is so cheap, we often don't need to worry about optimisation.

---

## 2024-05-05 09:38:51 - strategies channel

**Justice**

Interesting. I just did some further tests and while latency doesn't seem to affect the % return very much, it does affect the number of bets I am getting matched.



If I was to use polars, it would make things far easier, but I would be appending to the dataframe very frequently. Do you think this would add much overhead?

---

## 2024-05-05 09:34:42 - strategies channel

**Rob**

If I start again from scratch, I'd use a feature store, but I don't have too big an issue with processing historic data when placing bets, mainly because the historic data appears to be far less powerful then I expected :confused:



polars seems great, I will never need to chunk &amp; parallelise pandas code ever again :wink:

---

## 2024-05-05 09:06:40 - strategies channel

**Justice**

[@UC70576CB](@UC70576CB) My strategy doesn't seem to be overly sensitive to latency from my testing. All my feature engineering is done with polars, I much prefer it over pandas

---

## 2024-05-05 09:03:50 - strategies channel

**Rob**

Do you have any performance issues to worry about? If not, reusing the feature engineering code you used to build the strategy is a much bigger benefit IMHO, as there are so many edge cases to test if you reimplement processing.



If you need a more performant dataframe, consider [https://pola.rs/](https://pola.rs/)

---

## 2024-05-05 02:05:54 - strategies channel

**John Foley**

I use a feature store ( [https://feast.dev|feast](https://feast.dev|feast)) but it’s definitely  not ideal if latency is important for you 

---

## 2024-05-04 14:42:33 - strategies channel

**Justice**

Interesting. A data frame would allow me to re-use a lot of logic from my feature engineering but maybe it's more efficient to use a nested dictionary and a deque for the rolling windows

---

## 2024-05-04 12:01:32 - strategies channel

**liam**

Do you not want to just use pandas? 

---

## 2024-05-04 10:20:34 - strategies channel

**Justice**

Does anyone on here have any insights into migrating potentially hundreds of features created on a dataframe into a live production scenario, especially within the context of a flumine strategy? E.g. rolling windows, moving averages etc.

---

## 2024-04-18 08:14:32 - general channel

**liam**

Sorry I skipped a step



&gt; raw data -&gt; flumine or bflw -&gt; flat file -&gt; pandas

The flumine part obviously takes the longest but once in a flat file its quick

---

## 2024-04-17 19:58:32 - general channel

**liam**

I keep all markets in the raw format (always do this) and then process into flat files when I want to do some analysis. It’s then a case of just using pandas, I haven’t found any advantages of putting a database in between. 

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

## 2024-04-11 11:45:48 - general channel

**JFP**

Just wondering if anyone can point me in the right direction in regards to logging total cleared profit for each strategy once market/orders are cleared.



I currently log cleared orders via _process_cleared_orders_meta() and market profit via _process_cleared_markets(), but would like to add total profit for each strategy.



I can just process the cleared orders in a dataframe and groupby sum profit based on strat name, but I am hoping there is a more Flumine way to tackle this.



Have retrieved cleared orders from betfair via "client.betting_client.betting.list_cleared_orders()" to sum based on strategy name, but strategy refs have been recorded as my device name. So it appears only Flumine knows which orders belong to each strategy.

---

## 2024-03-30 18:11:16 - random channel

**Unknown**

i'm getting there.. this is looking more like it, although in reality i'm just honing my analysis/pandas/plots skills with this, and it's quite good fun!

---

## 2024-03-30 13:24:50 - random channel

**AndyL**

I must say I find there's a knack of writing pandas stuff, for example I want to create the cumsum() of one column and write it into a new column. I know this can be done in one line, but I don't currently know what that one line is...?!

---

## 2024-03-29 21:25:27 - random channel

**AndyL**

so yeah it is slower than I was hoping!

so the obvious problem is no-one is going to tell you "Alpha"

so i'm trying to calculate various features and various "triggers", then plot various plots to see how such features &amp; triggers vary against other features, with a hope of finding "Alpha" :slightly_smiling_face:

---

## 2024-03-29 18:31:37 - random channel

**Oliver**

numba is good if your code is slowed down by the python logic gluing all the pandas bits together (assuming you can't just use pandas more efficiently), so you can use something like `@numba.jit` to compile some block of code into machine code without you having to deal with it much. Its unlikely to be of huge value to you right now if pandas and numpy are new to you though as it is usually the use of pandas that can be improved most first.



PyArrow can be used as an alternative backend/storage engine for pandas, it has some merits, in particular if you write your data to disk and read it back later. Still fairly new in pandas so could be an excuse to avoid it as well, but it can read a CSV in parallel and be a lot faster.



I'd have thought you could get a fair bit more speed out of of pandas/python if you wanted as 250 rows a second sounds fairly slow to me so I imagine there's other places you can get speed first. I'd recommend profiling a run with a subset of data using [https://github.com/P403n1x87/austin?tab=readme-ov-file#synopsis|austin](https://github.com/P403n1x87/austin?tab=readme-ov-file#synopsis|austin) and then viewing the results with [https://github.com/jlfwong/speedscope?tab=readme-ov-file#speedscope|speedscope](https://github.com/jlfwong/speedscope?tab=readme-ov-file#speedscope|speedscope). This is probably to key combination I've found for optimising this kind of code.



Then again it sounds like you/your house benifits from the processing time [https://xkcd.com/303/](https://xkcd.com/303/)

---

## 2024-03-29 16:18:08 - random channel

**AndyL**

just the standard pandas &amp; numpy, matplotlib, don't know half those others, they tend to suit specific tasks...

---

## 2024-03-29 13:01:56 - random channel

**JL**

depending on what operations you do, might be worth checking

[https://github.com/thedataincubator/data-science-blogs/blob/master/sqlite-vs-pandas.md](https://github.com/thedataincubator/data-science-blogs/blob/master/sqlite-vs-pandas.md)

---

## 2024-03-29 12:31:19 - random channel

**AndyL**

optimized my pandas vector processing, should process the 16M row input in a mere 18hours :slightly_smiling_face:

---

## 2024-03-28 09:41:13 - random channel

**AndyL**

Yeah that’s my issue, ive got a noddy bit of pandas and reckon it will take 12hours to run !

---

## 2024-03-27 22:11:03 - random channel

**AndyL**

1month of record gb racing data to Pandas csv == 16Million lines !

---

## 2024-03-27 08:40:00 - random channel

**Ralegh**

Yeah mostly before fit in research code, e.g I might have a big df with histories for some horses - if you wanted a value from 5 rows ago as a feature you could do a pandas groupby then shift, with numpy it’s a little tricky, but with numba you can have def group_shift(group_ids, values, offset) which manually  does the bounds checks and it’s still very fast (probably faster than groupby)

---

## 2024-03-26 23:28:43 - random channel

**Ralegh**

I’m enjoying using dicts of numpy arrays and numba njit to write manual transformations these days (though I used a narrow subset of pandas functionality)

---

## 2024-03-26 23:25:38 - random channel

**Gooat**

Love / hate pandas / jupyter

---

## 2024-03-26 21:50:28 - random channel

**AndyL**

pandas errors can be so cryptic, just trying to "bin" a DataFrame, what am I not understanding?

```   selection_id         BSP  winner  

0      41569073    2.129299   False  

1      61343324    2.640000   False  

2      26741931   14.107778   False  

3      61939657   55.000000    True  

4      62819706  120.000000   False  

---&gt; 29 df['bsp_bin'] = pd.cut(df['BSP'], bins=4)

TypeError: putmask: first argument must be an array```



---

## 2024-03-11 16:35:27 - issues channel

**foxwood**

I think [@U012XF5CNPN](@U012XF5CNPN) explains it well and encapsulates the reasons I have turned the "feature" off. There are a mass of issues that can cause Python to throw concrete excpetions and they are not just related to Python, flumine or flumine strategy code. They include exceptions from the operating system and bugs in any of the host of python packages used - all of which would be ignored by flumine. Imho the probability of an exception arising is real and I favour the dead bot theory rather than the faulty live one.

---

## 2024-02-28 16:55:05 - random channel

**PeterLe**

Thanks Peter. I was thinking about this last night after Lee sent his message

I did something similar when I was going down the ML path, ie I was running the backtest against recorded markets and out putting the bits i was interested into a CSV...then into Pandas. -&gt; ML etc

I wasn't quite sure i this was the way to do when running live strategies and if that was the right way of doing it etc

Thanks for the pointers

---

## 2024-02-23 23:31:57 - issues channel

**Pietro Perrone**

Yes I would like to extract the 2 teams name and then create a pandas dataframe with 3 columns representing the bet (so under or over), the volume and the price

---

## 2024-02-21 12:47:18 - general channel

**Ralegh**

Just use flumine unless you specifically need other functionality, I only use a subset of features and am using copilot a lot for the rewrite but otherwise it’s a huge time sink

---

## 2024-02-20 16:27:58 - strategies channel

**Unknown**

Here is a simple model output screen from MySportsAI if you check 3/4 way down you will see a TTDrift figure, this means the average drift across the two input features is 0.532but if I run it with just TRinrace the TTDrift is 0.522 so clearly and expectedly days since the run had the higher drift factor. Numbers closer to 0.5 mean the data distribution is more alike in the train and test sets (good in other words)

---

## 2024-02-20 15:33:57 - strategies channel

**Mark Littlewood**

Maybe of help [https://towardsdatascience.com/which-features-are-harmful-for-your-classification-model-6227859a44a6](https://towardsdatascience.com/which-features-are-harmful-for-your-classification-model-6227859a44a6)

---

## 2024-02-13 09:22:39 - strategies channel

**Unknown**

[@UPMUFSGCR](@UPMUFSGCR) as you know, i'm only a beginner at this sort of thing..but this is the output of shap when i tried it.

I thought it may help you visualise it.

(For what it is worth; this is in-play horses and the top feature was something that Id never even focused on before. It surprised me that it was even listed (but made total sense after I thought about it ). So worthwhile playing around with it

---

## 2024-02-11 18:51:17 - strategies channel

**John Foley**

hard without knowing exactly what feature A is but perhaps:



“hello AGI overlord, please can you: 

• suggest ways I can make feature A more robust 

• suggest transformations on feature A that I could add into my model

• help me figure out what statistical distribution feature A follows

• suggest other ML algorithms for me to try given that feature A is really important and follows a {answer from above} distribution”

---

## 2024-02-11 18:09:25 - strategies channel

**John Foley**

there doesn’t necessarily need to be a “next step.” I wouldn’t feel the need to start removing features unless I was looking to optimise for memory/compute/training time etc. to me it’s for insights and explainability. it’s for questions like:

• which features should I invest time/money in improving?

• why did the model come up with this strange prediction? 

• does the model rely most heavily on the features that I would use if I were making a prediction myself? 

---

## 2024-02-11 18:02:09 - strategies channel

**Jonjonjon**

Thanks. This might be dumb, but suppose I find the most useful 5 features, what would the next step be? If I fit my models on those 5 features, I will have cherry picked the best features and it becomes an in-sample result.

---

## 2024-02-11 17:39:18 - strategies channel

**John Foley**

Not a top guy by literally any definition but: 

tree based sklearn models and xgboost python library have a `.feature_importances_` attribute built in which is a handy starting point. for anything more generic or custom i’ve used also shap values which are great but can need a lot of compute 

---

## 2024-02-10 17:38:12 - strategies channel

**Jonjonjon**

How do the top guys analyse the feature importance in their ML models?

---

## 2024-02-04 09:13:46 - random channel

**Paul**

A few months back there was a release of some time series model or another, and the orange website was full of people saying "we've given up on ML approaches to time series - it's all rubbish, just do some moving averages, it's useful", which surprised me, although I've not dived in much yet into that stuff yet (but planned to)

---

## 2024-01-30 21:53:33 - general channel

**Derek C**

It's a long time since I wrote the code, but I specifically use this snippet to set the parquet schema deliberately and iirc this is to avoid the pandas/parquet combination messing up my datatypes under certain circumstances such as when a string column is all nulls.



```table = pa.Table.from_pandas(df, schema=parquet_schema,   )```

Using sagemaker, as you say, sounds like a more solid option anyway though.

---

## 2024-01-30 17:29:56 - general channel

**Trex44**

Hmm that might be the issue but I did specifically enforce data types on the columns of the pandas dataframe before converting to a parquet so I don't know why the column type would then differ from one parquet file to another.



I think I have found a workaround for now, I saved about 100 of the files as csvs then loaded them up into a data flow in SageMaker and had sagemaker convert them to parquet files. I could then crawl and load these files in a notebook just fine. I am trying it with the whole data set now.  Strangely when I tried this trick with parquet files I got garbage, the data viewer function in the data flow just showed random symbols instead of headers and the data. Yet downloading the same parquet files and converting them to csv worked just fine and showed the data was in tact and readable.  Its all quite odd. The fix will be fine for now but it means I cant just save the days races as parquets and run a crawler on them which is what I really want to do.

---

## 2024-01-07 23:35:23 - random channel

**Unknown**

Here you go [@UUE6E1LA1](@UUE6E1LA1) Even allowing for time zones I haven't ever recorded a -£2,185 in any 24hr period, I'd have noticed.  Maybe it's fixed now but the screenshot is from when I first noticed the feature was there.  The 9th was correct so I'm not interpretting it incorrectly, and the 11th is wrong too as I lost about 450 vs the -350 it shows.

---

## 2023-12-05 08:46:31 - strategies channel

**PeterLe**

Hi [@U016TGY3676](@U016TGY3676), yes it did:

```# Feature Importance

print("Calculating the feature importance....")

importances = random_forest_model.feature_importances_

sorted_indices = np.argsort(importances)[::-1]

print("Feature Importance:")

for index in sorted_indices:

    print(f"{features[index]}: {importances[index]}"```

But it doesn't tell you much detail, that's why I opted for SHAP as i thought it would provide more detailed info

By the way; its been pointed out to me that whilst my initial thoughts were to see if ML could enhance a current system, the ML strat maybe a completely different strat to what my live one is

So now i know there is a better strat that the one im running live, I just have to work out what it is :grinning: :exploding_head:

---

## 2023-12-04 20:44:37 - strategies channel

**birchy**

[@UQL0QDEKA](@UQL0QDEKA) have you looked at the feature importances? They can sometimes be useful to view good/bad features of your model

---

## 2023-12-04 17:40:26 - strategies channel

**Derek C**

As for the SHAP results, I had to look it up to refresh my memory but I think this graph is showing most useful features from top to bottom. Feature 1 predicts a winner when it has a low value, as does 2 &amp; 3 (all the red dots are clustered together). I think feature 7 isn't very predictive - both high and low values are mostly red. That is my understanding but happy to be corrected. [https://datascience.stackexchange.com/questions/65307/how-to-interpret-shapley-value-plot-for-a-model](https://datascience.stackexchange.com/questions/65307/how-to-interpret-shapley-value-plot-for-a-model)

---

## 2023-12-04 10:19:32 - strategies channel

**liam**

For us mere mortals I think your last paragraph sums it up for me. So far for me the biggest insight has been its ability to quantify / visualise relationships between pnl and variables which aren't always linear.



However I have then taken the value out and updated my models / if statements to cater for the non linear relationship. In my case I have been keeping some features static and literally plugging in values to graph the change in outcome from the model, its dirty and could probably be replicated using regression but it works. Simply using the ML model was just matching or falling short of my previous strategies but using ML to advance things is a process that works well on my current strategies.

---

## 2023-12-04 09:37:19 - strategies channel

**Unknown**

Morning All,

I thought Id take a look at one of my existing profitable long term strats to see if i could improve it with ML

These are the basic steps that the ML took ;



loading data Set into dataframe....

Creating Histogram and Density plot....

Creating Correlation Matrix considering only numeric columns....

Selecting features and target....

Split the data....

Train Random Forest....

Making Predictions....

Calculating Random Forest Accuracy....

Validation Accuracy: 0.7990462572417981

Test Set predictions accuracy....

Test Accuracy: 0.7989358028340348

Calculating the feature importance....

Calculating SHAP values for model interpretability...

Analyzing overall feature contributions...



Based on 3 months of inplay data (Circa 35m rows of CSV)



The ML model was significantly better than my simple model and I though it was a good idea to use SHAP to try and understand what the model was doing ...(Now I know next to nothing about ML so not sure if those who work in this field use SHAP or whether it is any good??)



The output of SHAP is shown in the attached illustration.

(Ive removed the descriptions of the features for now)



From Top down, Im only using features 1, 4 and 5 in my day to day strat, but it seems to suggest that these three features have a negative impact on the P/L? So that has confused me :grinning:

Should I really be focusing on features 6 and 7 that have a high positive impact?  (Incidentally use feature 6 in a separate strat successfully)



How would you ML guys delve down deeper? (I though that maybe I could use Pandas to look at each feature independently, although I realise that it wouldn't give a complete picture as it maybe dependent on the values of other features, if that makes sense)

Or maybe I could run SHAP again but on selected features?

My head thinks just use pandas (as the ML stuff takes ages to run). The more I play around with ML, the more I think the simple methods of data interpretation are much quicker and provides good enough insight/indicative ie good enough == good enough

I just thought it may be an interesting topic for discussion, thanks for any thoughts

---

## 2023-11-29 09:12:52 - strategies channel

**John Foley**

newer versions of that should definitely accept pandas and other objects without needing to convert. You using an older version maybe? 

---

## 2023-11-23 09:45:18 - strategies channel

**liam**

:rolling_on_the_floor_laughing: I think the dark arts are causing my problems as I try and do things with ML :exploding_head:



Started coming up with some mad ideas involving meta model and looking at feature importance at different stages of the game

---

## 2023-11-23 09:36:18 - strategies channel

**liam**

Its an interesting problem, its something I have been battling with since I started but there doesn't seem to be anything out there to solve it.



I find racing is simpler and tbh I have never got SP to work as a feature, ignoring it and let the market tell me has always worked well for me. Maybe including the current price can do this for other sports as well..

---

## 2023-11-23 08:38:13 - strategies channel

**Mo**

You could use a meta model (not sure if this is technically the correct term) which has the individual model outputs as features. If you use a non linear modelling technique this allows you to combine the predictions in a non linear way

---

## 2023-11-20 20:18:14 - random channel

**Adrian**

Mongo could be worse, I don't have any experience with it so... I'll try a few things, as long as they have a python interface. Pandas own write to SQL library failed to complete at all with my final dataset without it being split up into parts, even then it was problematic (creating ghost entries).

Although the flat files thing is working, it's getting messy- i've got raw, unprocessed data, then cleaned, workable data, then formatted data, then finally transformed data. Trying to keep it all linked with folders and file names seems cursed.

---

## 2023-11-20 11:00:02 - random channel

**Adrian**

I think I might be able to skip SQL altogether and go for something like MongoDB. It's looking pretty promising from what i've seen. It could possibly even store ml models and associated dataframes/transformer objects,

---

## 2023-11-20 10:35:19 - random channel

**Adrian**

So i decided to take the plunge and start learning two big things over the last week. SQL and Pycharm. Can't say i think much of the former, but the latter is and absolute game changer. Regarding SQL, it takes me eight times longer to load my database up than loading it from pickle. Even longer to save it. The only case i can see this being useful is if I kept the thing open, sending in data to it periodically. At the moment pandas/pkl is so fast i can recreate my entire dataset from file faster than SQL can load. And anything that involves conversion between the two... forget about it :sweat_smile:

---

## 2023-11-11 06:57:07 - random channel

**Adrian**

What is the benefit of keeping it all in a database as opposed to just the original format on the hard drive? I think about learning SQL all the time but the simplicity of using files straight off the disk keeps me from getting started. I imagine it's good if you want to run queries on a bazillion rows at once but so far pandas + flumine + disk has been adequate.

---

## 2023-10-05 12:57:06 - general channel

**Andy B**

Okay, that does make a bit of sense.  At the start of the script I read in the event_id, time and distance to a pandas df, and then I check the df to get the distance when it opens a new market.  At some point I have pushed that down the processing order until it got to the point where I had it checking it as it processed each runner.  If I bump it up so that it is only checking once per market, I'm certain that would make this run quicker.  Only one way to find out.

---

## 2023-10-05 12:50:10 - general channel

**liam**

what are you doing in pandas? / my understanding is that you are only placing one bet so surely you just need to do the dirty pandas stuff once per market/strategy?

---

## 2023-10-05 12:49:28 - general channel

**liam**

ok so its pandas

---

## 2023-10-03 12:10:43 - general channel

**Peter**

That works for win and place markets. For more exotic markets it may fail (or will fail for the GB &amp; IE forecast market).



For those I use a worker to pull all the catalogues for the day's races, create a Pandas data frame and the group by start time and venue.



But it could equally be done without Pandas by using list comprehension.

---

## 2023-09-24 12:52:41 - general channel

**Justice**

[@UBS7QANF3](@UBS7QANF3) I sympathise with that. I created a machine learning model that had the racing post and timeform ratings as a feature. Back testing showed huge profits. Thankfully, I thought better of it. After looking into it, turns out these ratings are revised retrospectively, causing data to leak into the model

---

## 2023-09-19 12:46:38 - general channel

**Andy B**

I haven't been able to figure this out, so looking for a bit of assistance if possible.  My existing strategy looks like:



class MyStrat (BaseStrategy):



    def start(self) -&gt; None:

        print("starting strategy")



    def check_market_book(self, market: Market, market_book: MarketBook) -&gt; bool:

        # process_market_book only executed if this returns True

        if market_book.status != "CLOSED":

            return True



    # If check_market_book returns true i.e. the market is open and not closed then we will run process_market_book once initially

    # After the first inital time process_market_book has been run, every single time the market ticks, process_market_book will run again

    def process_market_book(self, market: Market, market_book: MarketBook) -&gt; None:



        if market is not None:

            if market is not None and market.market_catalogue is not None and market.market_catalogue.market_name is not None:

                RaceNumber = market.market_catalogue.market_name.split(' ')[0].replace("R","").strip()



        if market.seconds_to_start &lt;= 5 and market_book.inplay == False:

            TrackName = market.venue.lower()

            for runner in market_book.runners:

                RunnerName = [x.runner_name for x in market.market_catalogue.runners if x.selection_id == runner.selection_id]

                RunnerName = RunnerName[0].split('. ')[1].lower()

                if runner.status == "ACTIVE" and runner.ex.available_to_back: # and runner.ex.available_to_lay[0]['price']:

                    filtered_row = pd.DataFrame()

                    if market.market_type == 'WIN':

                        filtered_row = GreysList[(GreysList['TrackName'] == TrackName) &amp;

                            (GreysList['RaceNumber'] == int(RaceNumber)) &amp;

                            (GreysList['DogName'] == RunnerName)]



                    if not filtered_row.empty or market.market_type == 'PLACE':

                        if not filtered_row.empty:

                            runner_odds = filtered_row['ODDS'].iloc[0]

                            current_price = runner.ex.available_to_back[0]['price']

                            bet_price = get_nearest_price(round((current_price),2))

                            if runner_odds &lt; current_price and runner_odds &gt; 0 and current_price &gt;=2.5 and current_price &lt;= 10 and market.market_type == 'WIN':

                                print(market.market_type)



                                if market.market_type == 'WIN':

                                    stake = round((3/current_price),2)

                                    if stake &lt; 0.1: stake = 0.1

                                    print(TrackName, RunnerName, runner_odds, current_price, stake)

                                    trade = Trade(

                                    market_id=market_book.market_id,

                                    selection_id=runner.selection_id,

                                    handicap=runner.handicap,

                                    strategy=self,

                                    )

                                    order = trade.create_order(

                                        side="BACK", order_type=MarketOnCloseOrder(liability=stake)

                                    )

                                    market.place_order(order)

									

									# At this point, I want to also make a place bet but I need to get the value of runner.ex.available_to_back[0]['price'] from the PLACE market.

									# At the start of my script, I get a list of WIN and PLACE markets and store them in a dataframe called TodaysRaces.

									# I can locate the PLACE market id by querying this dataframe, but I don't know how to utilise Market.event["PLACE"] to get the value of runner.ex.available_to_back[0]['price'], so that I can set up the trade and order to place the bet.

									# Can someone point me in the right direction please?

---

## 2023-09-19 09:13:30 - random channel

**Ralegh**

Which asset class and time frame? [@UPMUFSGCR](@UPMUFSGCR) 

Id suggest focusing on getting good forecasts/models (which needs good data) before worrying about simulation. Should be able to manage with some pandas 

---

## 2023-09-14 19:02:53 - general channel

**AndyL**

I approached this just the other week:

logging control -&gt; runner.csv

market close BSP -&gt; bsp.csv

Then merged with Pandas

---

## 2023-09-05 12:02:43 - betconnect channel

**Mo**

```settled_bets = api_client.betting.my_bets(side=betconnect.BetSide.BACK, status=betconnect.BetRequestStatus.SETTLED, limit=1000).bets

problem_bets = pd.DataFrame(

    {

        "price": bet.price.price,

        "matched_stake": bet.matched_stake,

        "profit": bet.profit,

        "correct_profit": correct_profit

    }

    for bet in settled_bets

    if bet.matched_stake &gt; 0 

    and bet.profit != (correct_profit := int((Decimal(bet.price.price) - 1) * bet.matched_stake))

)

ok_bets = pd.DataFrame(

    {

        "price": bet.price.price,

        "matched_stake": bet.matched_stake,

        "profit": bet.profit,

        "correct_profit": correct_profit

    }

    for bet in settled_bets

    if bet.matched_stake &gt; 0 

    and bet.profit == (correct_profit := int((Decimal(bet.price.price) - 1) * bet.matched_stake))

)```

problem_bets:

```  price  matched_stake  profit  correct_profit

0  2.40            500     200             700

1  5.75            500    1875            2375

2  4.30            500    1150            1650

3  2.45            500     225             725

4  4.50            500    1250            1750

5  5.33            500    1666            2165```

ok_bets:

```    price  matched_stake  profit  correct_profit

0    2.50            500     750             750

1    2.00            500     500             500

2    3.70            500    1350            1350

3    3.40            500    1200            1200

4   1.909            500     454             454

5    3.25            500    1125            1125

6    2.00            500     500             500

7    3.60            500    1300            1300

8    4.50            500    1750            1750

9    5.50            500    2250            2250

10   2.60            500     800             800

11   4.50            500    1750            1750

12   5.25            500    2125            2125

13   7.50            500    3250            3250

14   5.50            500    2250            2250

15   3.20            500    1100            1100

16   4.60            500    1800            1800

17   3.10            500    1050            1050

18   7.50            500    3250            3250

19   3.20            500    1100            1100

20   6.50            500    2750            2750

21   7.00            500    3000            3000

22  2.375            500     687             687

23   4.50            500    1750            1750

24   2.50            500     750             750```



---

## 2023-09-04 12:26:36 - strategies channel

**Paul**

Are trying to solve for a filter/classification, a prediction, or a control problem? You need to think very, very carefully about the problem you’re solving for before you choose an approach and the appropriate features

---

## 2023-09-03 11:04:54 - strategies channel

**AndyL**

Thanks [@UQL0QDEKA](@UQL0QDEKA) [@U05L8PZD2FM](@U05L8PZD2FM) [@U4H19D1D2](@U4H19D1D2)

Yes, I have merged the race winner for W/L, and thus PnL.

So I think where I want to head, is I have a rough "Idea", but don't really know what variables might help make it more profitable (assuming it is to start with!)... So I was doing an initial simple baseline to understand the process... but then not sure I could equate having many many thousands of bets how you would use that in reality or refine it.

Your step by step is useful thanks [@UQL0QDEKA](@UQL0QDEKA) i've done some of the first few...

[@U05L8PZD2FM](@U05L8PZD2FM) I think I probably want to implement the basic Flumine strategy for my "idea", even though it maybe rough and ready and probably make it not too selective, and possibly not very profitable (or -EV)! Then run that through the Flumine simulator capturing CSV data for the bets, and to refine using ML what the dependent features are that would improve it?

I don't think going down the brute force, lots of hardware route sounds right for me.

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

## 2023-09-02 22:40:26 - strategies channel

**PeterLe**

Andy (given my VERY basic knowledge of ML) I think you need to initially add some more features into the ML, ie so, back, lay and LTP book etc ( you can use pandas to create these for you very easily) then create a simple strategy ( or something you are doing currently). You can the use this to learn about ‘feature importance’ … and that led me to an area I’d not thought about before (in hind sight it makes perfect sense now)

so I used this to explore and investigate things, it’s not a back test though and won’t replace flumine

---

## 2023-09-02 22:06:25 - strategies channel

**AndyL**

[@UQL0QDEKA](@UQL0QDEKA) [@U05L8PZD2FM](@U05L8PZD2FM) Made some in-roads with basic Pandas, and a simple Lay inplay &lt; 1.5 “BaseLine”:

```Total pnl =  16640.0```

So i’ve turned my market stream data into a CSV merged with winner and a PnL column, but currently “every” market update that matches inplay Lay price&lt;1.5, bets a notional £1, hence total pnl above for just 3 days is huge, could equally be huge negative...

So I could add a random classifier, and say that refines the bet choice, but that could still be 1000s of unrealistic bets in reality, since matching is unknown? In reality it would bet maybe up to a certain liability of matched bets ... I guess at some point you need to run a real Flumine backtest?

---

## 2023-08-24 18:08:33 - strategies channel

**Riccardo Fresi**

i use this self-made function, maybe can help, or improved

```def get_statistics(in_play_only=None):

    for event_type in Calcio_event_type_id:

        # prints id, name and market count

        #print(event_type.event_type.id, event_type.event_type.name, event_type.market_count)

        calcio_id = event_type.event_type.id



        # list of events

        event_list = trading.betting.list_events(

            filter=filters.market_filter(

                event_type_ids=[calcio_id], # filter on just football

                in_play_only=in_play_only,  

                #market_countries=["IT"],  # filter on just GB countries

                # market_type_codes=["WIN"],  # filter on just WIN market types



            ), locale="IT"

        )[:10]  # Seleziona solo i primi 10 elementi della lista

        

        combined_runner_dict = {}  # Dizionario per memorizzare i dati dei runner fusi

        for event in event_list:

            #print(event.event.id, event.event.name)

            inplay = trading.in_play_service.get_event_timeline(event_id=event.event.id)

            

            market_catalogues = trading.betting.list_market_catalogue(

                filter=filters.market_filter(

                    event_type_ids=[calcio_id],  # filter on just football

                    event_ids=[event.event.id],

                    # market_countries=["GB"],  # filter on just GB countries

                    market_type_codes=["MATCH_ODDS"],  # filter on just WIN market types

                ),

                market_projection=[

                    "COMPETITION",

                    "EVENT",

                    "EVENT_TYPE",

                    "MARKET_START_TIME",

                    "MARKET_DESCRIPTION",

                    "RUNNER_DESCRIPTION",

                    "RUNNER_METADATA",

                ],  # runner description required

                max_results=10, locale="IT",

            )

            #print("%s market catalogues returned" % len(market_catalogues))

            for market_catalogue in market_catalogues:

                #print(market_catalogue.market_id,

                    #market_catalogue.market_name,

                    #market_catalogue.market_start_time,)

                

                for runner in market_catalogue.runners:

                    #print(runner.selection_id, runner.runner_name, runner.handicap)

                    if inplay.status:

                        

                        runner_data = combined_runner_dict.setdefault(f"{market_catalogue.market_id}_{runner.selection_id}_{inplay.time_elapsed}",{})

                        runner_data["event_id"] = event.event.id

                        runner_data["event_name"] = event.event.name

                        runner_data["market_id"] = market_catalogue.market_id

                        runner_data["market_start_time"] = market_catalogue.market_start_time

                        runner_data["selection_id"] = runner.selection_id

                        runner_data["runner_name"] = runner.runner_name

                        runner_data["handicap"] = runner.handicap

                        market_books = trading.betting.list_market_book(

                            market_ids=[market_catalogue.market_id],

                            price_projection=filters.price_projection(

                            price_data=filters.price_data(ex_all_offers=True)

                            ), locale="IT",

                        )

                        for market_book in market_books:

                        #print(market_book.market_id,

                            #market_book.inplay,

                            #market_book.status,

                            #market_book.total_matched,)

                            for runner in market_book.runners:

                            #print(runner.selection_id, runner.status, runner.total_matched, runner.last_price_traded)

                                runner_data = combined_runner_dict.setdefault(f"{market_catalogue.market_id}_{runner.selection_id}_{inplay.time_elapsed}", {})

                                runner_data["selection_id"] = runner.selection_id

                                runner_data["total_matched"] = runner.total_matched

                                runner_data["last_price_traded"] = runner.last_price_traded

                                runner_data["Status"] = market_book.status

                                

                                #runner_data = combined_runner_dict.setdefault(f"{market_catalogue.market_id}_{runner.selection_id}_{inplay.time_elapsed}", {})

                                runner_data["Home Score"] = inplay.score.home.score

                                runner_data["Away Score"] = inplay.score.away.score

                                runner_data["Home Corners"] = inplay.score.home.number_of_corners

                                runner_data["Away Corners"] = inplay.score.away.number_of_corners

                                runner_data["Time Elapsed"] = inplay.time_elapsed

                                runner_data["Match Status"] = inplay.in_play_match_status

                                

                                

                                available_to_back = runner.ex.available_to_back

                                available_to_lay = runner.ex.available_to_lay

                            

                            

                            

                                combined_runner_list = list(combined_runner_dict.values())

        if combined_runner_dict:

            df = pd.DataFrame(combined_runner_list)  

            #df.sort_values(by=['event_id'], inplace=True)    

        else:

            df = pd.DataFrame()  # Create an empty DataFrame

            #trading.race_card.login()

            #race_cards = trading.race_card.get_race_card(market_ids=[market_catalogue.market_id])

            #results = trading.race_card.get_race_result(market_ids=[market_catalogue.market_id])

            #print(results)

    

    return df ```

---

## 2023-08-24 13:41:58 - random channel

**Unknown**

So this is the plot [@U4H19D1D2](@U4H19D1D2) in conjunction with this info...

Validation Accuracy: 0.8703854015340546

Test Accuracy: 0.8699371399724771

Total Profit/Loss using Simple strategy: £26015.709999999857

Total Profit/Loss using ML strategy for X : £25605.64000000001

The interesting thing is when this was printed out initially, it looked like the ML model wasnt as good as the simple strat.

That's not the case though as you will see the ML beat the simple strat for the same number of bets.

I found that the partial dependence plot interesting two when I chose two random features.

I can see from that, that I'm in the right ball park area, with a bit of tweaking

My initial thoughts now are to maybe create another CSV for a different month of data to see if the feature importance is similar for both months.

Then I will delve down a bit deeper into the feature importance and partial dependence.

Then Ill explore something ML related...

NB: Early on in this, I found something that I hadn't really considered for inplay before&lt; i left it out for this discussion (for obvious reasons) but keen to look deeper.

Anyway with that; Ill stop boring you all with this. I feel confident to take this further in the background and explore

if nothing else I've enjoyed my first venture into ML (even though the wife called me a 'geek' when I excitedly shown her how the 3D plot could pivot :joy:)

Just wanted to thank those who contributed in this thread and DM's cheers

---

## 2023-08-23 17:32:16 - random channel

**PeterLe**

Yep he plus version Foxwood

Ive just recoded to include the comments by Leo, results are:

Random Forest Accuracy: 0.9062742305480078

Total Profit/Loss using Simple strategy: £26007.66999999987

Total Profit/Loss using ML strategy for X 1.19: £22294.659999999945

             Feature  Importance

0  last_price_traded    0.116026

1               back    0.093928

2                lay    0.107229

3          back_book    0.206596

4           lay_book    0.203972

5           ltp_book    0.193442

6             Spread    0.075818

7     cross_matching    0.002990

(note: I found an error in my simple strategy :grinning: that why it was such a massive negative in previous text)

What is interesting now is that the ML seems to give a worse result :thinking_face:

---

## 2023-08-23 15:53:18 - random channel

**PeterLe**

[@U030GKBMCBF](@U030GKBMCBF) Just some feedback...

I asked chatgpt to comment on your suggestion in the context of my code...this is what is said ;



_The advice your colleague provided is quite accurate. Default feature importances from Random Forest models in scikit-learn can indeed be biased, particularly when the dataset includes different types of features (e.g., categorical and numerical). This bias might lead to incorrect conclusions about the importance of the features._

_In your code, you were using the default feature importance method by calling the `feature_importances_` attribute from the Random Forest model. This approach calculates feature importance based on the average depth at which each feature appears in the trees of the forest. While it is a common approach, it can be misleading._

_A more reliable way to assess feature importance is to use permutation importance. Permutation importance works by randomly shuffling the values of a single feature and measuring the resulting decrease in the model's performance. This decrease reflects the importance of that feature._



(provided some suggestions for code)



_This method will give you a more unbiased estimate of feature importance, taking into account the potential correlation between features and the different scales and types of features._

_Remember to remove or comment out the old code that calculated feature importance using `feature_importances_`._

_So, to answer your question, considering permutation importance would be an excellent improvement to your code, and it aligns with best practices in machine learning._



So spot on, thanks again :+1:

---

## 2023-08-23 10:11:57 - random channel

**PeterLe**

Morning Joe. This was really my first attempt at looking at ML. Probably best described as a random walk.:grinning:

My initial thoughts were, how to use ML to enhance, refine existing starts and secondly; use ML to look at the recorded data I had and run it against that to see what it found. (no preconceived ideas etc)

Having read up a little, I thought that feature importance may be a good place to start.

I did learn something from the feature importance (Which is not shown above). It is something that I haven't used in my in play stuff but now that ML has made it aware to me, it makes perfect sense and Im testing that in a live environment (1 day in).

As input Joe, maybe you could tell me the basic building blocks how you might go about this (just bullet points will do please)

ie :

• Record Live update data from the API (Doing that)

• use the price recorded to capture various variables (eg back, lay, ltp, books etc ) to a large CSV (Doing that)

What generic steps would you take from this point?

Thanks Joe

(PS I need to go offline for a few hours Joe, work calls - Thanks)

---

## 2023-08-23 09:35:27 - random channel

**PeterLe**

For X, Think of something that makes sense/logical (or gut feel). then branch out and see where it takes you

By the way, I recorded he following in my CSV:





```def process_market_book(self, market, market_book):

    with open(self.file_directory, "a") as f:

        writer = csv.DictWriter(f, fieldnames=HEADERS)

        for runner in market_book.runners:

            writer.writerow(

                {

                    "market_id": market_book.market_id,

                    "publish_time": market_book.publish_time,

                    "status": market_book.status,

                    "inplay": market_book.inplay,

                    "selection_id": runner.selection_id,

                    "last_price_traded": runner.last_price_traded,

                    "back": get_price(runner.ex.available_to_back, 0),

                    "lay": get_price(runner.ex.available_to_lay, 0),

                    "sp": runner.sp.actual_sp,

                    "cross_matching": market_book.cross_matching,

                    "runner_matched": runner.total_matched,

                    "venue": market.venue,



                }

            )```

and I included SP and Runner Matched in the features of the ML. For my  Inplay strat it rated SP and Runner Matched of high importance using ML, which is what you would expect. This gave me some confidence that the model was working as intended.

PS looking at the CSV header you posted I think you need to add more stuff in there as a minimum back book, lay book, Back,lay and LTP etc

---

## 2023-08-22 21:08:42 - random channel

**PeterLe**

[@U01PJ5YMFBJ](@U01PJ5YMFBJ) I started out by learning how to create the CSV  (using the price recorder) into Pandas DF's etc. (I know you are much more accomplished than me in terms of programming by the way)

The added in a couple more columns to include winner, P/L Sum of the books etc

I then started with something simple like regression

And then a random forest (ive only got the estimators set low for the time being)

I have two strats one a simple one and one an ML. They both use the same parameters eg, if the simple strat has a condition tha says back &lt; 10 then so does the ML.

to answer your question - Kind of :grinning: (remember we all do things differently and I know next to nothing about this) You need to have a 'Target'.  In my case I chose the target as 'winner' (from that you can determine whether you bet won or lost) Set up a value in the P/L column in your CSV based on say £1. if you dont have the CSV data (Which is every update) you need to get that up and running first (Lee helped me get this running, but is simple enough). use the price recorder against your recorded data (One month is plenty)

ChatGPT is great for this sort of thing it bootstraps your learning,

For your simple model just create something simple like lay the fav (in running) when X occurs. The ML will work it out for itself. The problem I had is understanding what the ML did so that I could employ that in my live stuff. Ive got some new stuff to look at now thanks to the earlier posts.

---

## 2023-08-22 20:08:56 - random channel

**AndyL**

[@UQL0QDEKA](@UQL0QDEKA) So about a random forest classifier, am I right in thinking the key to that is the "decision trees" ? ie.you've created some secret sauce decision tree alogorithm, whose parameters you've trained to get a better prediction?

or in other words, you have a set of decision trees like say:

     DecisionTree1: Win%1 = a*Feature1 + b*Feature2 + c*Feature3

     DecisionTree2: Win%2 = d*Feature4 + e*Feature5 + f*Feature6

Prediction = MajorityVote(Win%1, Win%2)

and running the dataset through Pandas...refines to give you a,b,c,d,e,f parameters for your best optimized "sauce"?

---

## 2023-08-22 19:53:01 - random channel

**PeterLe**

OK Rishab I understand that now. This maybe useful to prevent adding many features that does little to improve the results. The first thing I noticed when starting off down this road was how much longer it takes when you are adding more and more.

I need to read more about them tools as they are new to me.



Just a general question to you or anyone. have you found ML useful in in-play markets? I can see how this would work in pre off markets but lesser so inplay? Thakns

---

## 2023-08-22 19:42:10 - random channel

**Rishab**

So R2sq is a strictly increasing function wrt no. of features. So if u just keep on increasing features ur R2 will increase but ML models suffer from something known as curse of dimensionality. So Adjusted R2 takes this into consideration &amp; tells you the ideal point where the variance is balanced wrt to no. of features. To answer your second question ML models are generally complex in nature,  just with 4-5 features you can interpret a RF using the tree but can't do the same for a large number of features. I think in general you can't find exactly what the model is doing(i.e there are more complex model that combines various trees to make stronger models), but you can get a good feel for it by understanding the general working of the model, then using tools like feature imp., R2, confusion matrix etc

---

## 2023-08-22 18:05:04 - random channel

**Rishab**

You can look at Adjusted R sq. to find out if adding another feature actually improves the model performance or not

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

## 2023-08-22 14:51:07 - random channel

**liam**

Yep, flumine is for live/simulation but when it comes to modelling/backtesting you want to get things into pandas

---

## 2023-08-22 13:10:00 - random channel

**liam**

Not a stupid question, easiest way is to create a flumine strategy which writes all the data to a csv (variables + W/L of runner etc) -&gt; load into pandas



[https://github.com/betcode-org/flumine/blob/master/examples/strategies/pricerecorder.py](https://github.com/betcode-org/flumine/blob/master/examples/strategies/pricerecorder.py)

---

## 2023-08-22 13:02:52 - random channel

**Newbie99**

A bit of a random dumb question, but I was looking at [@U4H19D1D2](@U4H19D1D2)’s thread on ML and there’s one (really basic) piece that confuses me.



Let’s assume I have a basic ‘model’ that obviously uses flumine recorded data for backtesting (which also takes place in flumine).



Let’s pretend the ‘model’ simply tries to back any runner where say VWAP * x &gt; best available back price (where x = a percentage set by me currently).



How can I ‘train’ my model, as the code is written for streaming data?



Do I have to re-write everything to look at a large Pandas/PySpark data frame with all the raw data?



I’m presuming not and I’m misunderstanding how it works, but it does confuse me as the examples I’ve seen all seem to take numpy arrays as inputs or Pandas data frames!

---

## 2023-08-15 14:25:13 - strategies channel

**liam**

Pandas will be fine, it will be your CPU/ram that becomes the problem, why so big? / do you need everything you are recording?

---

## 2023-08-15 14:23:37 - strategies channel

**PeterLe**

Quick Question Please. Using the price recorder on one month of GB and IE Horses racing produces a CSV of circa 2.65gb...

How big a CSV file can you use before pandas start to struggle with it?

thakns in advance

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

## 2023-08-11 09:36:23 - general channel

**Nacho Uve**

[@U0155J92A7Q](@U0155J92A7Q) I have not many stream files. So by now, I am happy using a simple CSV. I read it with pandas and make my filters to select markets to backtest or analyze.

---

## 2023-08-08 10:11:38 - strategies channel

**foxwood**

I've used Google's tensorflow with python -  flexible for building / managing features - works well and now the docs appear sorted should be easier getting started. Any learning you do will transfer easily to other packages. If you are familiar with MS Visual Studio then their [http://ML.NET|ML.NET](http://ML.NET|ML.NET) add on is worth looking at - give it a csv then select fields to use and decide if feature or category is all you do - it then tries lots of different models to offer the best one. Seriously lacks ability to fine tune easily as in TF or SK but quick way to assess possibilities of datasets / models.

---

## 2023-08-08 09:14:16 - strategies channel

**Derek C**

Another consideration is whether the goal is to learn ML or get a good solution. Using an Auto-ML to generate features and models for you will give a better result than most people could do themselves,

---

## 2023-08-07 13:05:50 - strategies channel

**Unknown**

So I have a rough pipeline setup to allow model -&gt; flumine simulation, it works and I have results which point to some potential.



Stats: £30.0 profit per market, 14.0% roi, £59.4 matched per selection



A huge increase in matched amount which is not viable but the increase in ROI is most welcome, going to play around with some features and try and reduce the amount matched (probably a ML term for this when it comes to the model)

---

## 2023-08-07 10:19:04 - strategies channel

**liam**

Interestingly when I look at feature importance my model is at the bottom with 0.06% importance :joy:

---

## 2023-08-07 09:54:00 - strategies channel

**liam**

Ok, I follow, I think, this sounds like level 10 vs my current status of level 0.



It is already sounding like my current process of using a model and then filtering after with other features is less than ideal. However I feel starting with this using some simple models is probably going to see some improvements / move me onto level 1.

---

## 2023-08-07 09:07:55 - strategies channel

**Joe**

Are you looking to optimise a set of thresholds in your IFs or are you looking to recombine your features in a non-linear model? i.e. are you trying to find C to optimise:

IF ( f1 &gt; c1 &amp;&amp; f2 &gt; c2 &amp;&amp; f3 &gt; c3 ) THEN placeBet()

or are you trying to learn a new function F:

IF (F(f1, f2, f3) &gt; 0) THEN placeBet()

---

## 2023-08-07 08:48:58 - strategies channel

**liam**

First step is to get all the data/features into a dataset I can process, this might be the most painful part.



I have the 'base' strategy analysed in terms of profit/roi but I am wondering if I should run typical ML analysis on my predictions, accuracy/precision/recall to then compare with future models?

---

## 2023-08-07 08:46:04 - strategies channel

**Unknown**

*Day 1*



Setting the scene, the plan is to improve a live (profitable) strategy by optimising its current parameters (features) using ML.  This is going to be a learning exercise so if you have any questions / advice / criticism please get involved :wave:



The strategy is for TPD inplay racing, low stakes and taking Lay prices, market impact can be ignored for now. To keep things simple I am going to limit to Flat racing for the past 6 months, Jan-June inclusive, which gives around 1500 markets.



One of the features is what I would call the model and gives a % chance of the horse winning/losing and is what I have used for the past 4 yrs as the most important feature in the `ifs`. However I know that with the inclusion of other features it can be improved but I have never been able to optimise manually and get results.



Stats: £6.5 profit per market, 11.6% roi, £15.8 matched per selection

---

## 2023-08-04 17:44:02 - strategies channel

**Leo**

That said, the specific model is far less important than the quality of your features 

---

## 2023-08-04 12:19:57 - general channel

**joe taylor**

Hi guys! I want to work on some strategy around inplay horse racing. Had a few queries around this: how can I get real-time race data like runner distance left in race or position of each runner in race/speed 2. historical data for each runner with different features-timeform type data &amp; inplay data(like speed in last x fraction of race left etc)

---

## 2023-08-04 11:25:40 - strategies channel

**AndyL**

Definitely interested in this, i played briefly with pandas in my early goat days  with advice from [@UBS7QANF3](@UBS7QANF3). But didn't really see it's full potential.

Wondering, are all ML straight line fits? For example could you make it fit a quadratic for ax2+bx+c ? Ie.polynomial regression?

---

## 2023-07-27 08:19:27 - general channel

**liam**

I have multiple instances of flumine running all communicating with it, sending/receiving market / order / trade / strategy / notes etc to it



I have a simple SPA running on top that allows me to view everything at a glance and update settings etc



I have a few lambda scripts that communicate on a daily basis to update / reconcile / check / record various things



Simulation scripts use it to pull in the relevant marketId's / data required (catalogues / sports data etc)



However when using juypter / pandas I communicate directly to the db with SQL as its quicker, whats your frustration? Speed?

---

## 2023-07-24 08:50:03 - issues channel

**Mo**

I think a simple response along the lines of:



&gt; If you are unable or unwilling to implement robust error handling in your code I suggest you look at flumine which is a fully featured trading framework sitting atop betfairlightweight

would go a long way

---

## 2023-07-06 09:24:27 - random channel

**Jonjonjon**

Yes but it takes 38 seconds on my pc. I'm hoping to make it instant with some clever Pandas stuff.

---

## 2023-07-05 21:21:49 - random channel

**Jonjonjon**

Does anyone have a version of this function that can be used on a Pandas Series?



```def get_nearest_price(price, cutoffs=CUTOFFS):

    if price &lt;= MIN_PRICE:

        return MIN_PRICE

    if price &gt; MAX_PRICE:

        return MAX_PRICE

    price = as_dec(price)

    for cutoff, step in cutoffs:

        if price &lt; cutoff:

            break

    step = as_dec(step)

    return float((price * step).quantize(2, ROUND_HALF_UP) / step)```

---

## 2023-06-07 11:32:42 - issues channel

**Tom**

I'm having a nightmare of a time trying to use RaceCards; I want to call them to get results, bsp, market data e.t.c. - Wouldnt mind seeing the full functionality; there is something there that even has form related data (I presume it's not available for Australian horse racing?).



I've spun myself around enough times to not really know what to try next.



```def get_race_results(race_card: RaceCard, market_ids: List[str]):

    logging.debug(f"Getting race card for market_ids: {market_ids}")

    try:

        racecards = race_card.get_race_card(market_ids, data_entries="RACE")

        race_results = race_card.get_race_result(market_ids)

        print(f"race results are {race_results}")

        logging.debug(f"Received race card data: {racecards}")

    except Exception as e:

        logging.error(f"Failed to get race card data: {e}")

        return []



    result = []

    for race in racecards:

        logging.debug(f"Processing race: {race['raceName']}")

        for runner in race['runners']:

            runner_data = {

                "Market ID": race['marketId'],

                "Race Name": race['raceName'],

                "Race Time": race['raceTime'],

                "Runners": race['numberOfRunners'],

                "Distance": race['distance'],

                "Runner Name": runner['runnerName'],

                "Runner ID": runner['selectionId'],

                "Starting Price": runner['sp'],

                "Final Position": runner['finishingPosition'],

                "In-Play High Price": runner['inPlayHighPrice'],

                "BSP": runner['bsp'],

            }

            result.append(runner_data)

            logging.debug(f"Processing runner_data: {runner_data}")



    return result



def get_results(trading):

    date_str = datetime.date.today().strftime("%d-%m-%Y")

    file_path = f'data/market_trade_data/market_trade_data_{date_str}.pkl'

    market_trade_data = pd.read_pickle(file_path)

    logging.debug(f"Market trade data: {market_trade_data}")

    market_ids = refresh_market_ids(market_trade_data)



    race_card = trading.RaceCard.login()

    try:

        trading.race_card.login()

        print("Logged in successfully.")

    except Exception as e:

        print(f"Failed to log in: {e}")



    all_results = []

    for market_id in market_ids:

        logging.debug(f"Getting race results for market_id: {market_id}")

        all_results.extend(get_race_results(race_card, [market_id]))



    df_results = pd.DataFrame(all_results)

    df_results.to_csv(f"data/race_results/race_results_{date_str}.csv", index=False)

    logging.debug(f"Saved race results to 'data/race_results/race_results_{date_str}.csv'")```

---

## 2023-06-02 14:39:29 - random channel

**Peter**

Ah. For that I'd simply generate a backup with mysqldump from your primary database and then restore it to your laptop version. Stick this in a shell script (it's only two lines) and run it as needed on your laptop.



Though I would also consider whether you need to do this at all. Most of my analysis is done locally, but the data is loaded when needed from my remote primary database, often directly into Pandas using read_sql()

---

## 2023-06-02 14:18:09 - random channel

**Peter**

You're right that there are different approaches to database replication. The [https://dev.mysql.com/doc/refman/8.0/en/replication-solutions.html|MySQL documentation explains many of them](https://dev.mysql.com/doc/refman/8.0/en/replication-solutions.html|MySQL documentation explains many of them). But it's a pretty technical area and I wouldn't try to set it up and manage it yourself unless you're an experienced DBA (i which case why ask the question?).



The right solution absolutely depends on why you need a replicated database, so how others do it is pretty irrelevant. but since you asked, it's a standard feature of most cloud database services including AWS's RDS, which is how I do it, allowing me to focus on my trading apps and not get bogged down with irrelevant database issues.

---

## 2023-06-02 10:00:12 - general channel

**Trex44**

[@U04NWADNCFR](@U04NWADNCFR) When you say you use Athena to populate the pandas DF's in Sagemaker; can you do this via Sagemaker or is it a case of running the query using Athena then manually loading the output file from the given S3 bucket into a Jupyter notebook. In other words, if I change the data filters in the Pandas script I am using (e.g. focus on events taking place on Sunday only) in a Jupyter instance on Sagemaker will it run a new query via Athena and I can then visualise the output in Sagemaker? Or is it the case I would have to vary the filters in Athena then load the new results into Sagemaker for visualisation?

---

## 2023-06-01 16:13:41 - general channel

**Derek C**

[@U03N4QBJ0TV](@U03N4QBJ0TV) I do a lot of the same thing, except that I use Athena to populate pandas DataFrames in SageMaker from my files in S3. The benefit is that I can filter the rows and the columns that will be brought into memory in the SQL logic, and also sometimes do grouping to further reduce the size of the dataset that lands in Pandas. The benefit of Athena is that you don't have to actually migrate anything into a SQL database - you just tell it where the csv files are in S3 and they 'become' the database that you can then query. The awswrangler library makes it easy to integrate Pandas and Athena/S3 if you're not already using that.

---

## 2023-06-01 10:47:17 - general channel

**Trex44**

[@U04NWADNCFR](@U04NWADNCFR) Thanks very much for the answer. I currently use csv's stored in S3 then load them into a Jupyter note book in AWS Sagemaker and use Pandas to explore them. I have considered moving everything over to an SQL database but I like the graphical output I can get from using Pandas. Loading into the notebook takes an age and the kernel dies if I try to manipulate large data sets as the instance doesn't have the memory needed.

---

## 2023-05-25 06:00:28 - general channel

**Andy B**

Thanks Liam,

    def process_market_book(self, market: Market, market_book: MarketBook) -&gt; None:



        if market.seconds_to_start &lt;= 5 and market_book.inplay == False:



            [http://logging.info|logging.info](http://logging.info|logging.info)(f"Inside the last 5 seconds for this market and race is not inplay")

            ThisMarket = TodaysRunners[TodaysRunners['MarketID'] == market_book.market_id]



            for runner in market_book.runners:

				if runner.status == "ACTIVE" and runner.ex.available_to_back:

					row_index = ThisMarket[(ThisMarket['MarketID'] == market_book.market_id) &amp; (ThisMarket['SelectionID'] == runner.selection_id)].index

					if len(row_index) &gt; 0:

						# Update the value in the BSP column for the matching row

						ThisMarket.loc[row_index, 'BSP'] = runner.ex.available_to_back[0]['price']



            RaceFull = ThisMarket[['TrackName','RaceNumber','Distance','HorseName','Num','MarketID','SelectionID']].copy()

            scaled_features = StandardScaler().fit_transform(Race.values)

            ModelName = 'HorseModel2M.h5'

            ModelName = tf.keras.models.load_model(ModelName)

            Predictions = ModelName.predict(scaled_features)

            RaceFull['Probability'] = Predictions

            RaceFull['Model'] = 'Model9'

            RaceFull = RaceFull.sort_values(by = 'Probability', ascending=False)

            RaceFull = RaceFull.fillna(0)

---

## 2023-05-25 05:25:51 - general channel

**Andy B**

I have some code for placing thoroughbred bets that I cobbled together combining my python stuff and BFLW.  30 seconds out from scheduled start time, I get some variables from by database, get the current "to back" price from BF and run them through a ML algorithm to get predictions.  This works okay, but I want to shift this into Flumine and run it closer to start time.

For back testing purposes, I am pulling the data out of my database into a dataframe and then as I process each market in flumine, I select the subset of rows for the specific market and run the ML algorithm over it.  This works okay to this point, but I am now running into an issue where it is trying to continually run the process until the race goes in-play, so I can see that the way I currently have my code designed isn't right.

I was wondering how others implement the processing of ML algorithms in Flumine, or if I am better off forcing it to not process the market again once an order is placed.  If that is the better option, how would I do that?

---

## 2023-05-09 19:06:36 - random channel

**Newbie99**

```ncalls  tottime  percall  cumtime  percall filename:lineno(function)

      113    0.002    0.000  585.570    5.182 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/concurrent/futures/_base.py:199(as_completed)

      114    0.001    0.000  585.563    5.137 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py:604(wait)

      114    0.003    0.000  585.562    5.137 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py:288(wait)

     2480  585.558    0.236  585.558    0.236 {method 'acquire' of '_thread.lock' objects}

   1998/1    0.019    0.000   10.578   10.578 {built-in method builtins.exec}

        1    0.000    0.000   10.578   10.578 backtesting.py:1(&lt;module&gt;)

        1    0.002    0.002    8.888    8.888 backtesting.py:288(start_backtest_a)

  1979/22    0.004    0.000    1.383    0.063 &lt;frozen importlib._bootstrap&gt;:1167(_find_and_load)

  1960/22    0.004    0.000    1.382    0.063 &lt;frozen importlib._bootstrap&gt;:1122(_find_and_load_unlocked)

  1874/23    0.003    0.000    1.379    0.060 &lt;frozen importlib._bootstrap&gt;:666(_load_unlocked)

  1630/23    0.002    0.000    1.379    0.060 &lt;frozen importlib._bootstrap_external&gt;:934(exec_module)

  4574/43    0.001    0.000    1.370    0.032 &lt;frozen importlib._bootstrap&gt;:233(_call_with_frames_removed)

  894/160    0.001    0.000    1.056    0.007 {built-in method builtins.__import__}

 2336/977    0.002    0.000    0.919    0.001 &lt;frozen importlib._bootstrap&gt;:1209(_handle_fromlist)

        1    0.000    0.000    0.688    0.688 /python_files/football_data.py:1(&lt;module&gt;)

4684/4545    0.045    0.000    0.350    0.000 {built-in method builtins.__build_class__}

        1    0.000    0.000    0.335    0.335 /python_files/validation_functions.py:1(&lt;module&gt;)

        1    0.000    0.000    0.334    0.334 /python_files/import_historic_horse_data.py:1(&lt;module&gt;)

     1630    0.005    0.000    0.325    0.000 &lt;frozen importlib._bootstrap_external&gt;:1007(get_code)

        1    0.000    0.000    0.309    0.309 backtesting.py:212(generate_event_groupings)

        1    0.000    0.000    0.297    0.297 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/statsmodels/tsa/holtwinters/__init__.py:1(&lt;module&gt;)

        1    0.000    0.000    0.297    0.297 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/statsmodels/tsa/holtwinters/model.py:1(&lt;module&gt;)

        1    0.000    0.000    0.249    0.249 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/matplotlib/pyplot.py:1(&lt;module&gt;)

        1    0.000    0.000    0.231    0.231 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/__init__.py:1(&lt;module&gt;)

        1    0.013    0.013    0.222    0.222 backtesting.py:270(&lt;listcomp&gt;)

    39431    0.214    0.000    0.214    0.000 {built-in method posix.stat}

     1630    0.002    0.000    0.214    0.000 &lt;frozen importlib._bootstrap_external&gt;:1127(get_data)

1874/1863    0.002    0.000    0.194    0.000 &lt;frozen importlib._bootstrap&gt;:566(module_from_spec)

        1    0.000    0.000    0.194    0.194 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/scipy/stats/__init__.py:1(&lt;module&gt;)

     1637    0.188    0.000    0.188    0.000 {method 'read' of '_io.BufferedReader' objects}

  234/229    0.000    0.000    0.173    0.001 &lt;frozen importlib._bootstrap_external&gt;:1231(create_module)

  234/229    0.170    0.001    0.172    0.001 {built-in method _imp.create_dynamic}

        1    0.000    0.000    0.172    0.172 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/scipy/stats/_stats_py.py:1(&lt;module&gt;)

      100    0.000    0.000    0.164    0.002 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/matplotlib/artist.py:159(_update_set_signature_and_docstring)

       99    0.000    0.000    0.161    0.002 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/matplotlib/artist.py:126(__init_subclass__)

       33    0.000    0.000    0.148    0.004 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/importlib/__init__.py:108(import_module)

       33    0.000    0.000    0.148    0.004 &lt;frozen importlib._bootstrap&gt;:1194(_gcd_import)

        1    0.000    0.000    0.140    0.140 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/scipy/stats/distributions.py:1(&lt;module&gt;)

        1    0.000    0.000    0.137    0.137 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/matplotlib/figure.py:1(&lt;module&gt;)

        1    0.000    0.000    0.129    0.129 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/matplotlib/projections/__init__.py:1(&lt;module&gt;)

      112    0.000    0.000    0.110    0.001 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/matplotlib/artist.py:1841(kwdoc)

     2025    0.039    0.000    0.103    0.000 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/concurrent/futures/process.py:762(submit)

        1    0.000    0.000    0.100    0.100 /python_files/misc_functions.py:1(&lt;module&gt;)

        1    0.024    0.024    0.099    0.099 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/scipy/stats/_continuous_distns.py:1(&lt;module&gt;)

  234/167    0.000    0.000    0.096    0.001 &lt;frozen importlib._bootstrap_external&gt;:1239(exec_module)

  234/167    0.017    0.000    0.096    0.001 {built-in method _imp.exec_dynamic}

        1    0.000    0.000    0.096    0.096 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/flumine/__init__.py:1(&lt;module&gt;)

        1    0.000    0.000    0.095    0.095 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/smart_open/__init__.py:1(&lt;module&gt;)

        1    0.000    0.000    0.095    0.095 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/flumine/flumine.py:1(&lt;module&gt;)

        1    0.000    0.000    0.094    0.094 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/smart_open/smart_open_lib.py:1(&lt;module&gt;)

        1    0.000    0.000    0.094    0.094 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/flumine/baseflumine.py:1(&lt;module&gt;)

      112    0.002    0.000    0.094    0.001 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/matplotlib/artist.py:1602(pprint_setters)

        1    0.000    0.000    0.093    0.093 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/smart_open/doctools.py:1(&lt;module&gt;)

        1    0.000    0.000    0.093    0.093 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/smart_open/transport.py:1(&lt;module&gt;)

        9    0.000    0.000    0.093    0.010 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/smart_open/transport.py:32(register_transport)

        1    0.000    0.000    0.093    0.093 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pandas/core/api.py:1(&lt;module&gt;)

        1    0.000    0.000    0.092    0.092 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/matplotlib/colorbar.py:1(&lt;module&gt;)

        1    0.000    0.000    0.089    0.089 /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/flumine/strategy/strategy.py:1(&lt;module&gt;)

     1937    0.008    0.000    0.088    0.000 &lt;frozen importlib._bootstrap&gt;:1056(_find_spec)

     1630    0.002    0.000    0.086    0.000 &lt;frozen importlib._bootstrap_external&gt;:727(_compile_bytecode)```

---

## 2023-05-09 14:03:40 - general channel

**Andy**

I had this problem too. The betfair blog and other places talk about fill_or_kill and fill_and_kill being exactly this - [https://apps.betfair.com/learning/fill-or-kill-dont-wait-around-for-a-price-to-be-matched/|https://apps.betfair.com/learning/fill-or-kill-dont-wait-around-for-a-price-to-be-matched/](https://apps.betfair.com/learning/fill-or-kill-dont-wait-around-for-a-price-to-be-matched/|https://apps.betfair.com/learning/fill-or-kill-dont-wait-around-for-a-price-to-be-matched/) but then the documentation only talks about a minFillSize which is the min stake amount to fill before cancelling - [https://docs.developer.betfair.com/plugins/servlet/mobile?contentId=3833942#content/view/3833942|https://docs.developer.betfair.com/plugins/servlet/mobile?contentId=3833942#content/view/3833942](https://docs.developer.betfair.com/plugins/servlet/mobile?contentId=3833942#content/view/3833942|https://docs.developer.betfair.com/plugins/servlet/mobile?contentId=3833942#content/view/3833942). No mention anywhere I can see of what parameter/filter to use to use the feature as I would have assumed would have been one of it’s primary use cases (kill after X number of seconds) 

---

## 2023-05-08 13:10:31 - general channel

**liam**

Workers suit polling / long running process where as a moving average would need every MarketBook so suits being processed in a strategy and then stores in market context 

---

## 2023-04-25 16:42:02 - general channel

**Peter**

It can indeed get complicated quickly. But Flumine has features that help keep this to a manageable level.



In case it helps, my feedback and end-of-day processes lean heavily on logging controls. I have a version that writes all orders to a database and updates those entries with the result when markets are complete. This keeps the monitoring logic completely separate from strategy execution (except arguably for the single `add_logging_control()` statement), but makes the data I need available for daily reconciliation scripts and ad hoc analyses.

---

## 2023-04-17 10:51:33 - general channel

**Jorge**

Hi guys, I'm having an issue with my flumine Strategy. I save the details of every order I place, after it goes to EXECUTION_COMPLETE status, using:

```def save_completed_bets_data(self, market, selection_id):

    """

    Saves data from bets after an order in EXECUTION_COMPLETE.

    Note that an order can be partially matched many times before going to EXECUTION_COMPLETE status.



    """

    for order in market.blotter._orders.values():

        if order.size_matched &gt; 0:

            if order.status == OrderStatus.EXECUTION_COMPLETE:

                if order.selection_id == selection_id:

                    if order.date_time_execution_complete:

                        if order.bet_id not in self.completed_bets_dict:

                            self.completed_bets_dict[order.bet_id] = {

                                'market_id': market.market_id,

                                'selection_id': selection_id,

                                'side': order.side,

                                'average_price_matched': order.average_price_matched,

                                'size_matched': order.size_matched,

                                'execution_complete_ts': order.date_time_execution_complete,

                            }



                            df = pd.DataFrame.from_dict(self.completed_bets_dict, orient="index")

                            df.to_csv(self.completed_bets_csv_path)```

My issue is that for some orders (5% of them) the size_matched does not match the stake I get quering `list_cleared_orders`. Moreover, the stake from `list_cleared_orders` is always bigger than the one I recorded. Anyone has any clue why this would happen?

---

## 2023-04-03 21:34:47 - issues channel

**Andy B**

I have had my first flumine strategy up and running for about a week and it seems to work well apart from one issue that happens inconsistently.  I'm not sure if it is relevant or not, but the strategy fires when the there is less than 5 seconds to start time and the event has not gone inplay.  I keep getting batches of the following somewhat generic error filling my log file, and I am wondering if this is a common issue that I should be handling in the code with try\catch.  I'd like to know why it happens though, rather than just ignoring it:

2023-04-03 22:02:21,329:CRITICAL:Unknown error '1.212248357' in process_market_book (1.212248357)

Traceback (most recent call last):

  File "C:\Python\lib\site-packages\pandas\core\indexes\base.py", line 3803, in get_loc

    return self._engine.get_loc(casted_key)

  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc

  File "pandas\_libs\index.pyx", line 165, in pandas._libs.index.IndexEngine.get_loc

  File "pandas\_libs\hashtable_class_helper.pxi", line 5745, in pandas._libs.hashtable.PyObjectHashTable.get_item

  File "pandas\_libs\hashtable_class_helper.pxi", line 5753, in pandas._libs.hashtable.PyObjectHashTable.get_item

KeyError: '1.212248357'



The above exception was the direct cause of the following exception:



Traceback (most recent call last):

  File "C:\Python\lib\site-packages\flumine\utils.py", line 239, in call_strategy_error_handling

    return func(market, market_book)

  File "c:\Users\elmob\OneDrive\Punting\Scripts\Betfair\FluStrat.py", line 231, in process_market_book

    ratio_price = iggy_df.loc[market_book.market_id].loc[runner.selection_id].item() / runner.ex.available_to_back[0]['price']

  File "C:\Python\lib\site-packages\pandas\core\indexing.py", line 1073, in __getitem__

    return self._getitem_axis(maybe_callable, axis=axis)

  File "C:\Python\lib\site-packages\pandas\core\indexing.py", line 1312, in _getitem_axis

    return self._get_label(key, axis=axis)

  File "C:\Python\lib\site-packages\pandas\core\indexing.py", line 1260, in _get_label

    return self.obj.xs(label, axis=axis)

  File "C:\Python\lib\site-packages\pandas\core\generic.py", line 4049, in xs

    loc, new_index = index._get_loc_level(key, level=0)

  File "C:\Python\lib\site-packages\pandas\core\indexes\multi.py", line 3160, in _get_loc_level

    indexer = self._get_level_indexer(key, level=level)

  File "C:\Python\lib\site-packages\pandas\core\indexes\multi.py", line 3263, in _get_level_indexer

    idx = self._get_loc_single_level_index(level_index, key)

  File "C:\Python\lib\site-packages\pandas\core\indexes\multi.py", line 2849, in _get_loc_single_level_index

    return level_index.get_loc(key)

  File "C:\Python\lib\site-packages\pandas\core\indexes\base.py", line 3805, in get_loc

    raise KeyError(key) from err

KeyError: '1.212248357'

---

## 2023-03-27 20:21:25 - strategies channel

**R**

Usually automl wont help all that much until there is a clear hypothesis to be tested.  E.G. "I think that features &lt;x, y, z&gt; will have effect &lt;e&gt;" and then I can go and test for that.  Otherwise it's like throwing shit at a wall to see what sticks... a method I am also familiar with XD

---

## 2023-03-27 15:54:50 - strategies channel

**R**

Per [@U9JHLMZB4](@U9JHLMZB4)’s comment above, your accuracy can be high when predicting every runner will lose.  In a 10 runner race, you'd have 90% accuracy!  So we have to take a deeper look at things.  Usually you can start at precision and recall:



Precision is related to False Positives

Recall is related to False Negatives



In this case, False Positives can lose you money while False Negatives will miss trades.  So:



low Recall = Lots of missed trades

low Precision = lots of bad trades



From your numbers, you are missing more trades than you are losing; which is better than the other way around.



Not surprised that those ID features don't work, they are not "numbers" in the sense that a logistic model can deal with them.  They are more like categorical variables.  It's like trying to numerically model a word, it can be done, but needs some preprocessing.



I'm curious: is there one trade per event you are looking for or multiple signals simultaneously?  Trying to understand if you have a class imbalance problem.



Also, use cross-validation and calibration : [https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.CalibratedClassifierCV.html)

---

## 2023-03-27 13:03:31 - strategies channel

**birchy**

I now have some quick n dirty signals as a proof of concept and running against a complete dataset generated by Flumine simulation where the strategy backs every runner for £1 at LTP on every update. Results appear to be more realistic, particularly the recall stat [@U9JHLMZB4](@U9JHLMZB4) mentioned:



`Accuracy: 0.8649507394792786

Precision: 0.6514084507042254

Recall: 0.34230002846569885

F1-score: 0.4487777570442247

MSE: 0.13504926052072141

LogLoss: 4.867668736665466`



Using irrelevant features such as market_id and selection_id give poor results as expected. Surprised that the Accuracy is still quite high though. Thoughts?

---

## 2023-03-26 21:06:45 - strategies channel

**R**

So feature scaling applies to logistic regression only when you are interested in regularizing the model somehow (i.e. L1 and L2 terms are non-zero).  In most cases we want to regularize to improve generalization (reduce overfitting).



I would try to just convert everything to implied probabilities and that will act as a scaling transform.  If there are features that you can't do this to (like volume perhaps) then standardize them or play around with some scaling methods to see what works best (e.g. normalization and minmax scaling can also work)



quick and dirty method is to minmax scale things and go from there.

---

## 2023-03-26 20:13:23 - general channel

**Thomas JAMET**

How can I compute market book analytics (like moving averages) with Flumine? Is it something that's advisable?

---

## 2023-03-26 19:34:25 - strategies channel

**ShaunW**

Your understanding is correct. The implied probability of the matched prices in your dataset is approximately 0.84, which means that, on average, the market believes there is an 84% chance of the runner winning. To beat the market, your model's accuracy should be higher than this implied probability.

In your case, the accuracy of the LogisticRegression model is 0.8346, which is close to the market's implied probability but not quite above it. This means that, although your model appears to be performing reasonably well, it is not yet outperforming the market.

To improve your model's performance, you can try several approaches:

1. Feature Engineering: Create new features or transform existing features to better capture the underlying patterns in the data.

2. Feature Selection: Remove irrelevant or noisy features to reduce overfitting and improve model generalization.

3. Hyperparameter Tuning: Optimize the hyperparameters of your Logistic Regression model, such as regularization strength (C) or using different solvers.

4. Ensemble Methods: Combine multiple models, like decision trees or other classifiers, to improve overall performance.

5. Experiment with different algorithms: Try other machine learning algorithms that might better capture the patterns in your dataset.

Remember to also take into account the Precision, Recall, and F1-score of your model, as they provide additional insights into its performance. For instance, your model's high Recall (0.9988) and lower Precision (0.8354) indicate that it is good at identifying winning bets but may also produce many false positives, which can lead to losses. Balancing these metrics can help you create a more effective betting strategy.

---

## 2023-03-26 19:17:50 - strategies channel

**birchy**

Going back to my opening post, the model I was using:



`from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_squared_error`



`# Convert the target variable to binary (0 for lose, 1 for win)

df['winner'] = df['profit'].apply(lambda x: 1 if x &gt; 0 else 0)`



`# Split data into training and test sets

features = ['sig1', 'sig2', 'sig3']`

`X_train, X_test, y_train, y_test = train_test_split(df[features], df['winner'], test_size=0.2)`



`# Instantiate a logistic regression model

model = LogisticRegression()`



`# Fit the model to the training data

model.fit(X_train, y_train)`



`# Use the model to make predictions on the test data

y_pred = model.predict(X_test)`



`# Evaluate the model's performance using appropriate metrics

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

print(f"Accuracy: {accuracy}")

print(f"Precision: {precision}")

print(f"Recall: {recall}")

print(f"F1-score: {f1}")

print(f"MSE: {mse}")`



Bearing in mind that the dataset is a bet history (BACK bets only) where all unmatched bets have been removed and 'profit' is a real-world number, would this not achieve the same result as calculating EV for training? My gut feeling is that the model is shyte, or at least the data I'm using is too optimised due to being pre-filtered by the strategy that generated it. Thoughts?

---

## 2023-03-26 17:46:52 - strategies channel

**birchy**

Just for fun, chat GPT came up with this:

`import pandas as pd

from hmmlearn import hmm



# Load data into pandas dataframe

df = pd.read_csv("market_data.csv")



# Define the state space

states = ["increase", "decrease", "same"]



# Define the observation space

observations = df[["bid_price", "ask_price"]].values



# Define the transition probabilities

trans_mat = [[0.7, 0.2, 0.1],

             [0.3, 0.5, 0.2],

             [0.2, 0.3, 0.5]]



# Define the emission probabilities

emissionprob_mat = [[0.2, 0.4, 0.4],

                    [0.4, 0.3, 0.3],

                    [0.3, 0.3, 0.4],

                    [0.4, 0.4, 0.2]]



# Create the HMM model

model = hmm.MultinomialHMM(n_components=3)

model.startprob_ = [0.3, 0.4, 0.3]

model.transmat_ = trans_mat

model.emissionprob_ = emissionprob_mat



# Fit the model to the data

model.fit(observations)



# Make predictions

prediction = model.predict(df[["bid_price", "ask_price"]].values)

predicted_states = [states[state] for state in prediction]

df["predicted_states"] = predicted_states



# Print the predictions

print(df["predicted_states"])`



---

## 2023-03-26 16:09:23 - strategies channel

**birchy**

Thanks [@U04AD6RAGGH](@U04AD6RAGGH). So my features are signals generated from changes in price, volume, etc. The strategy is inplay horses, so my main concern is that it may be identifying that 1.01=winner, even though that's not always the case...

Will look at SGD. I also have plans to use a similar model for predicting price movement, i.e. the binary target being `price_now &lt; price_previously`. Any advice on that?

---

## 2023-03-22 02:52:17 - general channel

**Tom**

What's the best way to familiarise oneself with all the different functionalities and options? I'm looking on GitHub and the docs but I'm running myself in circles - I'm sure that a lot of what I want to do are the classic problems that have been overcome in the libraries - but where do you find and understand all the functionality?



getting market_percentage for example, I'm trying to use betfairutil (and I'm sure this is straightforward), but I'm having trouble going from the dataframe I've created to what's needed



```market_books = betfairutil.read_prices_file(path_to_prices_file)```

are prices_files standardised outputs from betfair?



I thought market_books themselves were betfair objects?



I seem to be confusing myself chasing different ideas of how it works without really sitting down and trying to understand the libraries first - I have a clear idea of the strategy e.t.c. but in terms of structuring software it's tricky because I can't conceptualise the end result (which parts to make modular, how to structure the different working bits and pieces etc)

---

## 2023-03-18 11:41:13 - random channel

**river_shah**

```As a trading system, I have many decision rules and thresholds. How should I optimize and combine the thresholds and rules?



Optimizing and combining decision rules and thresholds in a trading system involves selecting the best set of rules and parameter values that maximize your trading strategy's performance, given your objectives and constraints. Here's a step-by-step guide to help you:

Define objectives and constraints: Clearly state your objectives, such as maximizing returns, minimizing risk, or achieving a specific risk-return profile. Also, consider constraints like trading costs, capital requirements, and any regulatory restrictions.

Pre-process data: Clean, preprocess, and organize historical market data to use in your analysis. This data will be used to backtest and optimize your trading strategy.

Create a set of candidate rules: Develop a diverse set of trading rules based on technical indicators, fundamental analysis, or other signals. Make sure these rules are modular and can be combined or adjusted easily.

Split data into training, validation, and testing sets: Divide your historical data into separate sets to prevent overfitting and to ensure that your strategy performs well on unseen data.

Develop a performance metric: Choose an appropriate performance metric (e.g., Sharpe ratio, Sortino ratio, or information ratio) to evaluate your trading strategy. This metric should align with your objectives and constraints.

Optimize decision rules and thresholds: Using the training data, perform optimization to find the best combination of rules and thresholds. There are various optimization methods, such as:

Grid search: Systematically test various combinations of rules and thresholds within a predefined range.

Random search: Test random combinations of rules and thresholds within a predefined range.

Genetic algorithms: Apply evolutionary algorithms to find the optimal combination of rules and thresholds.

Bayesian optimization: Use probabilistic models to optimize the selection of rules and thresholds.

Validate the optimized strategy: Apply the optimized strategy to the validation dataset to assess its performance. If it does not meet your objectives, consider refining the rules, thresholds, or optimization method and repeat the process.

Backtest on out-of-sample data: Once you have validated your optimized strategy, backtest it on the testing dataset to evaluate its performance on unseen data. This step helps ensure the robustness of your strategy.

Monitor and update: Regularly monitor your trading strategy's performance and update the rules and thresholds as needed. Markets evolve over time, and your strategy may need to adapt to changing conditions.

Remember, optimizing and combining trading rules and thresholds is an iterative process that requires continuous monitoring and adjustments. A successful trading system should balance the need for robustness, simplicity, and adaptability to market conditions.```

A more concrete code example useful for trading:



```What is mean variance optimization? Implement MVO using numpy, ensure positivity constraint, shrink covariance matrix to make sparse portfolios. use L-BFGS-B as optimizer





Mean Variance Optimization (MVO) is a portfolio optimization technique developed by Harry Markowitz in his Modern Portfolio Theory. The goal of MVO is to find the optimal allocation of assets in a portfolio that maximizes the expected return while minimizing portfolio risk, as measured by portfolio variance.

Here's an example of MVO implementation in Python using NumPy, SciPy, and a shrinkage method to obtain a sparse portfolio with positivity constraints:

python```



```import numpy as np

import pandas as pd

from scipy.optimize import minimize



def mean_variance_optimization(returns, cov_matrix, target_return, shrinkage_factor=0.5):

    num_assets = len(returns)

    

    # Objective function: Portfolio variance

    def portfolio_variance(weights, cov_matrix):

        return weights.T @ cov_matrix @ weights

    

    # Shrink covariance matrix

    avg_variance = np.mean(np.diag(cov_matrix))

    shrunk_cov_matrix = (1 - shrinkage_factor) * cov_matrix + shrinkage_factor * avg_variance * np.identity(num_assets)

    

    # Constraints

    constraints = (

        {"type": "eq", "fun": lambda w: np.sum(w) - 1},  # Sum of weights equal to 1

        {"type": "eq", "fun": lambda w: np.dot(returns, w) - target_return},  # Target return

    )

    

    # Bounds: positivity constraint

    bounds = [(0, 1) for _ in range(num_assets)]

    

    # Initial weights

    initial_weights = np.ones(num_assets) / num_assets

    

    # Minimization using L-BFGS-B

    result = minimize(portfolio_variance, initial_weights, args=(shrunk_cov_matrix), method="L-BFGS-B", bounds=bounds, constraints=constraints)

    

    return result.x



# Example usage

if __name__ == "__main__":

    asset_returns = np.array([0.05, 0.1, 0.12])

    covariance_matrix = np.array([

        [0.1, 0.05, 0.01],

        [0.05, 0.2, 0.02],

        [0.01, 0.02, 0.3],

    ])

    

    target_return = 0.1

    shrinkage_factor = 0.5

    

    optimal_weights = mean_variance_optimization(asset_returns, covariance_matrix, target_return, shrinkage_factor)

    print("Optimal Weights:", optimal_weights)```

---

## 2023-03-13 11:21:21 - general channel

**Alex**

You can then turn the dictionary into a pandas Series with `pd.Series(ltp_dict)` (assuming ltp_dict) holds the prices.

---

## 2023-03-13 09:19:47 - general channel

**Andy Bason**

Hi guys, say I want to compare the LTPs of all runners in a horse race at time a and time b. What is the most efficient way to store/compare the data? My first attempt uses Pandas but it's clear now it's not up to the job. (btw I'm using betfairlightweight) Cheers

---

## 2023-03-06 14:33:53 - random channel

**PeterLe**

Sorry for the basic question....

If I wanted to run the back test and capture infomation as it was running for analysis using pandas/jupyter...

Would I use juypterloggingcontrol.py

or

backtestloggingcontrol.py



Am i correct in thinking that  juypterloggingcontrol.py is used AFTER running the back test

whereas backtestloggingcontrol.py is used DURING backtesting



Could someone please explain the difference (in very basic terms) please?

(Still on 100 days of code, maybe i should finish that first! :grinning:)

Thanks in advance

---

## 2023-03-05 09:34:28 - general channel

**Jonjonjon**

The conversion to Pandas could be a big bottleneck.

---

## 2023-03-05 09:27:59 - general channel

**Will**

Building a list with ltp and seconds to start then converting to a pandas data frame. 

---

## 2023-03-05 09:19:19 - general channel

**Jonjonjon**

Are you doing it on live data with Pandas? If so, Pandas is too slow if you are updating it with every price update. More primitive types should be fastwr

---

## 2023-03-05 08:21:25 - general channel

**Will**

hey legends - what is the best way to store/gather past last traded price on a runner. for example, currently i load a dataframe with the  ltp from about 10mins out every time it changes, then perform my predictions. if i load too many markets, i end up with latency issues.

---

## 2023-02-20 20:38:48 - general channel

**Unknown**

*Data collected using Flumine*

Hey there, I'm using Flumine's data recorder to collect streaming data. During my exploratory data analysis, I noticed some potential inconsistencies in the data and would appreciate any thoughts or insights.



To analyze the data, I've organized it into a sorted timestamp dataframe that includes both trades and the orderbook. To account for double-counting, I've divided the size of the trades by two, which has resulted in some interesting observations.



For example, in the screenshot, just before a trade occurred, the best available price to lay at level 0 was 3.55, and the size was 11.9$. At the time of the trade, the trade price was 3.55$  with a size of  5.995 * 2 = 11.99$ (in my table, I display this as 5.995$ after dividing by two, as previously mentioned). The entire level 0 was consumed by this trade, as indicated by the fact that the level with a price of 3.55 no longer existed in the timestamp just after the trade. Based on this, I believe that the actual traded amount was $11.9, and not 0.5 * $11.9 as I initially thought.



However, I've also noticed that in the majority of cases, the volume consumed from the orderbook is only half of the traded amount, which suggests that dividing by two is necessary.





This leads to the strange behavior that sometimes I need to divide the traded size by two, while other times I do not. Do you have any ideas to explain this?

---

## 2023-02-01 18:24:49 - random channel

**birchy**

I've used Linux on all of my work machines for about 20 years and recently gained access to a MacBook air M1 a few months ago. Although similar to Linux (Ubuntu, Mint, Debian, etc), I did/do find the keyboard shortcut mappings take a while to get used to. Overall it's a been positive experience. Once you have the thing setup (Pycharm, etc) the experience is not much different to any other OS. My main advice would be to ensure you research the installation process for any software you need as there's usually a specific Apple Silicon version. The default Intel versions _will_ install OK but I've had "wrong architecture" issues in the past, particularly with python/numpy/pandas while running in Pycharm. That's usually related to the python interpreter used by Pycharm and you have to point it at the full path rather than the/bin/python3.11 it suggests is available.

---

## 2023-01-31 19:13:42 - general channel

**Peter**

Broadly what [@UFTBRB3F1](@UFTBRB3F1) said, but with a couple of tweaks.



A minor point on football markets: handicaps will be non-zero for most runners in the Asian Handicap market type, and zero for other markets.



I recommend against trying to filter data from the market recorder as you stream it. Better is to collect it raw (i.e. not just the best prices), compress it and save it, all of which the marketrecorder does by just setting the parameters. Then process the files offline to extract the data you want. The reason for this process is that as you gain more experience in this field, you will probably find that you need more extensive data from which to extract the features that you will use to derive your trading triggers. And while it's easy to filter out the data you're not yet interested in, it's impossible (or at least very expensive if you buy it from Betfair) to infill later the data you wished you'd collected.

---

## 2023-01-19 13:53:00 - general channel

**liam**

When I meet people this seems to be question number 1, from profitable through to newbies. I always give the same answer which is that there is no way I would be where I am now without having worked with and spoken to those that I have met through open sourcing bflw/betcode.



You make the assumption that anyone who uses betcode libraries will make money, they are just tools. Open sourcing flumine was always a risk as its far more powerful than it lets on however it has pushed me (and others) to improve it, add features, fix bugs and is now 100x quicker than its predecessor.



The biggest change I have seen in the 'landscape' since this slack is the acceptance that you need to get value to make money. Its a secret world and think this slack is the closest you can see it in public other than the meetups :wink:

---

## 2023-01-16 12:02:43 - random channel

**Ralegh**

I process betfairs data into parquet files then load them in and do most of the proof of concept and idea testing in pandas where it takes hardly any time, with flumine as the last step

---

## 2023-01-13 23:18:20 - general channel

**Gooat**

Appreciate the input, don't get distracted by the Rust...stick with pandas and some tweaks until you a hit wall.

---

## 2023-01-13 15:01:38 - general channel

**Peter**

Looked at it a couple of times, but each time felt that the overhead of adjusting to it outweighed the performance benefits. For context my dataframes can run to several million rows, but I'm a long way short of the billions that polar seems designed to handle.



Worth adding that the real cost of the switch is very difficult to evaluate. It's fairly easy to understand "faster" and to see from the docs what can be done using Polars. But the real pain point would come in the edge cases when I hit an "oh shit" moment as I realise that this thing I do in Pandas may not exist in Polars and I've got to code it up myself or keep using Pandas anyway.

---

## 2023-01-13 14:52:00 - general channel

**river_shah**

```Going big...

Do you expect more than 2^32 ~4,2 billion rows? Compile polars with the bigidx feature flag.



Or for python users install pip install polars-u64-idx.```

---

## 2023-01-13 14:31:33 - general channel

**Gooat**

Any of the power pandas users swapping out for Polars?

---

## 2023-01-13 08:13:27 - random channel

**Mo**

Obviously in the absence of feature requests, what I add to betfairutil is whatever I'm currently working on. I've been finding recently that it really helps not to be lazy about just reading everything into memory as this allows me to saturate my CPU with workers



```  * get_market_books_from_prices_file

  * get_minimum_book_percentage_market_books_from_prices_file```

Are two other examples. Previously I would probably just have read the entire set of market books into memory then use bisect functions to find the ones I care about

---

## 2023-01-09 09:35:37 - general channel

**Andrew**

What’s the best way, with flumine, to handle this when both the price and size are to change? Clearly it’s cancel and then place. But if I’m updating too quickly (a feature of my strategy) how do I best avoid a “race” where the order to be cancelled isn’t yet executable (ie. cancellable)?

---

## 2023-01-04 01:48:00 - general channel

**Unknown**

I'd suggest [https://pipenv.pypa.io/en/latest/|Pipenv](https://pipenv.pypa.io/en/latest/|Pipenv) for managing the spec for a virtualenv, it can create (by default IIR) a virtualenv under `.venv` (you don't want to commit that), and uses a `Pipfile` and `Pipfile.lock` to manage what goes into the venvs it manages.



The useful thing is that you specify the package constraints in your `Pipfile` (e.g. `pandas ~= 1.1.0`),  then you can tell it to update the lockfile with the latest versions that satisfy the constraints, and you can sync your environments using `pipenv` - perfect for developing services with virtualenvs.

---

## 2022-11-20 14:14:27 - general channel

**liam**

I just read/write to a big file then process through pandas

---

## 2022-11-20 13:29:31 - general channel

**Jonjonjon**

Yes that is what I do too. Though there can be annoying difficulties with concatenating too much as Pandas is not good at it..someone here probably has a good way to do it.

---

## 2022-11-19 13:29:47 - strategies channel

**Liam Querido**

What is the best way to mitigate execution risk? I have an arbitrage trading strategy that places three bets anytime an arbitrage opportunity exists. The problem comes when one of the bets cannot be matched, but the other two can be.



I have considered using the MatchMe feature and setting a liquidity filter to ensure that all my bets are matched, but is there a better method?

---

## 2022-11-09 17:56:06 - general channel

**foxwood**

Got autogluton going fairly quickly so will explore the models on that to start with. Not sure about the trend to try everything then just pick simple best accuracy - the quality of the ones it gets right is more important. I got better results with tf by sticking to one model at a time and playing with the data in terms of changing the feature set, nodes, depth etc. ONNX looks interesting and MS give it some support for Windows so will have a look at that as well. Thanks for suggestions.

---

## 2022-11-09 12:57:35 - general channel

**FT**

Hi guys, I've got a flumine specific question. I don't know if I misunderstand something in the way the blotter works. I'm simulating a simple strategy with historical data. In this particular case, at the end all the orders in the markets blotter show up as PENDING, which is very unlikely since there are a lot of them and I take very bad prices just to see if they ever get the status EXECUTION_COMPLETE.

I collect some of the orders information into a dataframe. This is one example row. Why do I have a `avg_price_matched` and `size_matched` and `profit`, when the order is still PENDING? By the way the placed_at and completed_at are seconds to start time.

```selection_id  placed_at  completed_at  status                price  side  avg_price_matched  size_matched  profit

28396755      -348.287   -348.287      OrderStatus.PENDING   1.81   BACK  1.91               2.0           1.82```

---

## 2022-11-09 12:33:07 - general channel

**James**

Hi all, I'm trying to build a simple dataframe containing basic details for the day's races. For some reason I can't get the off times for each race. This line `'Start Time': [market_cat_object.market_start_time for market_cat_object in market_catalogues]` just returns None. Can anyone see what the issue is? Thanks



```# Create event filter

event_filter = betfairlightweight.filters.market_filter(

    event_type_ids=[7],

    market_type_codes=["WIN"],

    market_countries=["GB", "IE"], 

    market_start_time={

        'to': (datetime.utcnow() + timedelta(hours=time_window)).strftime("%Y-%m-%dT%TZ")

    }

)



todays_races = trading.betting.list_events(

    filter=event_filter

)



races_today = pd.DataFrame({

    'Event Name': [event_object.event.name for event_object in todays_races],

    'Event ID': [event_object.event.id for event_object in todays_races],

})



print(races_today)



races_list = races_today['Event ID'].to_list()

print(races_list)



market_catalogue_filter = betfairlightweight.filters.market_filter(event_ids=races_list, market_type_codes=["WIN"])



market_catalogues = trading.betting.list_market_catalogue(

    filter=market_catalogue_filter,

    max_results='100',

    sort='FIRST_TO_START',

)



# Create a DataFrame for each market catalogue

races_df = pd.DataFrame({

    'Start Time': [market_cat_object.market_start_time for market_cat_object in market_catalogues],

    'Market Name': [market_cat_object.market_name for market_cat_object in market_catalogues],

    'Market ID': [market_cat_object.market_id for market_cat_object in market_catalogues],

    'Total Matched': [market_cat_object.total_matched for market_cat_object in market_catalogues],

})```



---

## 2022-11-07 13:16:34 - random channel

**Mo**

betfairutil version 0.4.0 released: [https://github.com/mberk/betfairutil](https://github.com/mberk/betfairutil)



```### Added



* get_event_id_from_string function

* get_pre_event_volume_traded_from_prices_file

* get_win_market_id_from_race_card function



### Changed



* pandas is now an optional dependency

* Added should_restrict_to_inplay argument to prices_file_to_data_frame

* Made get_runner_book_from_market_book more defensive

* Added LAST_PRICE_TRADED data frame format

* Optionally output runner statuses when converting market books to data frames

* Various README improvements:

    * More hype!

    * Badges

    * Examples```

&gt; ```pandas is now an optional dependency```

[@U4H19D1D2](@U4H19D1D2) this one is for you :point_up:

---

## 2022-11-01 08:12:43 - issues channel

**Liam Querido**

Okay cool, thanks Mo. I have the following code, which calls the MarketRecorder class. When I execute the code, the data is stored in a single file of type '.205772753'.



I have two questions from here. First of all, I'm not quite sure what this file type is - could you please help me understand what it is, and how I can convert to .csv (I'm assuming you're going to suggest calling market_book_to_dataframe and then saving to .csv).



Second question, is my code actually streaming? Even though the code keeps running, no new data seems to be recorded. If I leave the code running for 10 mins, I am left with the same file that was exported when I initially executed the code 10 mins ago.



Please let me know if logs would be any of use in solving this issue. Thanks again Mo

---

## 2022-11-01 07:19:31 - issues channel

**Liam Querido**

Is the MarketRecorder under Flumine the best way to stream? I have seen lots of different modules and many different approaches to streaming - some use MarketRecorder, others don't. What do you suggest (and is there a specific streaming example you could refer me to)?



So far, I am able to obtain the market data I want, but not via streaming (just PIT query). Below is my code. What is the best way to adapt this for streaming?



Thanks in advance! This forum has already been extremely helpful!





def GetEventIDs():

    event_types = trading.betting.list_event_types()

    Result = pd.DataFrame({

        'Sport': [event_type_object.event_type.name for event_type_object in event_types],

        'ID': [event_type_object.event_type.id for event_type_object in event_types]

    }).set_index('Sport').sort_index()

    return Result



GetEventIDs()





def FilterMarkets(EventTypeID,MarketCountry,DaysUntilMarketStart):

    sport_event_filter = betfairlightweight.filters.market_filter(

        event_type_ids    =[EventTypeID],

        market_countries  =[MarketCountry],

        market_start_time ={

            'to': (datetime.datetime.utcnow() + datetime.timedelta(days=DaysUntilMarketStart)).strftime("%Y-%m-%dT%TZ")

        }

    )

    country_sport_events = trading.betting.list_events(

        filter=sport_event_filter

    )

    Result = pd.DataFrame({

        'Event Name': [event_object.event.name for event_object in country_sport_events],

        'Event ID': [event_object.event.id for event_object in country_sport_events],

        'Event Venue': [event_object.event.venue for event_object in country_sport_events],

        'Country Code': [event_object.event.country_code for event_object in country_sport_events],

        'Time Zone': [event_object.event.time_zone for event_object in country_sport_events],

        'Open Date': [event_object.event.open_date for event_object in country_sport_events],

        'Market Count': [event_object.market_count for event_object in country_sport_events]

    })

    return Result





def process_runner_books(runner_books,market_catalogues):

    '''

    This function processes the runner books and returns a DataFrame with the best back/lay prices + vol for each runner

    :param runner_books:

    :return:

    '''

    best_back_prices = [runner_book.ex.available_to_back[0]['price']

        if runner_book.ex.available_to_back

        else np.nan

        for runner_book

        in runner_books]

    best_back_sizes = [runner_book.ex.available_to_back[0]['size']

        if runner_book.ex.available_to_back

        else np.nan

        for runner_book

        in runner_books]



    best_lay_prices = [runner_book.ex.available_to_lay[0]['price']

        if runner_book.ex.available_to_lay

        else np.nan

        for runner_book

        in runner_books]

    best_lay_sizes = [runner_book.ex.available_to_lay[0]['size']

        if runner_book.ex.available_to_lay

        else np.nan

        for runner_book

        in runner_books]



    selection_ids = [runner_book.selection_id for runner_book in runner_books]

    statuses      = [runner_book.status for runner_book in runner_books]

    runners       = [market_catalogue.runner_name for market_catalogue in market_catalogues.runners]



    df = pd.DataFrame({

        'Runners': runners,

        'Selection ID': selection_ids,

        'Best Back Price': best_back_prices,

        'Best Back Size': best_back_sizes,

        'Best Lay Price': best_lay_prices,

        'Best Lay Size': best_lay_sizes,

        'Status': statuses,

    })

    return df





def GetMarketBook(MarketID,MarketCatalogue):

    price_filter = betfairlightweight.filters.price_projection(price_data=['EX_BEST_OFFERS'])

    # Request market books

    market_books = trading.betting.list_market_book(

    market_ids=[MarketID],

    price_projection=price_filter

    )

    # Grab the first market book from the returned list

    market_book = market_books[0]

    Result = process_runner_books(market_book.runners, MarketCatalogue)

    return Result

---

## 2022-10-25 13:21:24 - random channel

**birchy**

Question for the pandas gurus: I have a dataframe where column 0 is a datetime and column 1 is populated with booleans. I'm trying to calculate the timedelta between multiple rows where the start time is when col1 = True (rising edge) and the end time is when col1 = False (falling edge). The number of rows between start &amp; end time is variable and can be anything from 1 to 10+. Most of the examples I've found online only deal with diff() on consecutive rows and I'm struggling with the logic to sum the conditional delta from row x to row z. Any suggestions?

---

## 2022-10-11 09:20:07 - general channel

**Peter**

[@U03TJKFLE8K](@U03TJKFLE8K) My path was comparable to yours. I wrote the (still) most widely used PHP package for consuming the Betfair API. But it became clear that PHP was a severely limiting factor. All the best tooling for analysis, testing and trading in this space is in Python (i.e. Betfairlightweight, Flumine, Pandas and Jupyter Notebooks).



So I went all in, learnt the language and now work almost exclusively in it (with a bit of Rust thrown in when I need compiled execution speeds). So my recommendation would be the familiarise with the tools that best fit the job rather than trying to bend your process to fit what you currently know. Though that is said without knowing what your processes are, e.g. if you are placing your bets manually at the bookmakers from data summarised via web pages you’ve constructed with Node, there may be a case for not re-inventing the wheel, just the engine :slightly_smiling_face:

---

## 2022-09-29 22:07:11 - random channel

**Paul**

Avoiding over-fitting is covered by lots of good resources - big +1 to advice above. 20 features feels like a big space for some types of regression. Tools like AutoGluon (disclaimer: produced by another team at my employer), might help you as it can tell you about feature importance and does a lot of heavy lifting for you. I was taught it because I work for The Firm, but actually, it helps you with a shed ton of this stuff

---

## 2022-09-28 22:56:09 - random channel

**foxwood**

I think [@UBS7QANF3](@UBS7QANF3) is the resident wizard on this stuff - he posted a link recently to a free pdf of a textbook well worth reading - worth searching for. Think whether all the features are useful - if they are not really relevant to the prediction then leave them out since it can mislead the training. Categories can help things along if they represent very different things eg NH racing versus flat. Beware of including any data that would be unknown to your program at the time of running it live eg don't include BSP if it is a pre-race model. Maybe try a binary classification model if you just want yes/no. Worst thing I ever did was leave the result in the data set - training was superb at over 95% :rolling_on_the_floor_laughing:. Correlation matrix might throw some light on meaningful relationships in the data. No easy fixes that I know of unfortunately - just have to  keep at it refining and thinking - rinse and repeat.

---

## 2022-09-28 19:31:17 - random channel

**Jonjonjon**

I am fitting a logistic regression.



It has 20 features that have been standardised to be roughly normal.



Sample size is 20k.



60% of target values are false. 40% are true.



The score (from sklearn) is 0.5.



What should I do to test whether or not my model has been over fitted?

---

## 2022-09-27 20:54:22 - random channel

**Dave**

Fun fact: pandas started off as a project at a systematic fund

---

## 2022-09-27 20:06:57 - random channel

**Jonjonjon**

`dd.read_parquet` in [https://pandas.pydata.org/docs/user_guide/scale.html|here](https://pandas.pydata.org/docs/user_guide/scale.html|here) looks like it might do what I need too.

---

## 2022-09-27 19:55:08 - random channel

**Jonjonjon**

Thanks [@U0174A50YKS](@U0174A50YKS) I will try that tomorrow. I'm wondering if the problem would go away if I change all my Dataframes to have non-object types i.e. floats.

---

## 2022-09-27 19:16:03 - random channel

**CL**

Try some of the pyarrow functionality - eg pa.concat_tables, and then convert the resulting table to pandas if needed. I've found the arrow libraries to be generally more memory efficient.

---

## 2022-09-20 02:22:51 - general channel

**Tom**

```market_types_filter = [betfairlightweight.filters.market_filter(event_ids=[event_ids]) for event_ids in aus_thoroughbred_events_today['Event ID']]

market_types = [trading.betting.list_market_types(filter=market_types_filter) for market_types_filter in market_types_filter]

aus_thoroughbred_events_today['Market Types'] = market_types```

I've got another one there - a lot of this code is just copied from the intro tutorial - I am going to run other peoples codes (with some adjustments) that perform similar functions to what I eventually need to build to just get things working and getting used to stepping outside of that structured learning environment I have been in without going all the way to the deep end.



I have a DataFrame called aus_thoroughbred_events_today, and I wanted to add market_types to that DataFrame (but not market_types objects, the actual information of which market types are available) I've only managed to attach the objects to the aus_thoroughbred_events_today DataFrame.



Besides this, I need to test whether the market-types I am calling match up with the existing sequence of events (that they actually represent the event they are supposed to) - and I will do the same thing with market_catalogues (I think the actual code should be similar enough).



I think that a lot of this is learning how to think about the problem rather than solving the specific problem and I'll be in learning phase for some time, but I am planning on doing 4+ hours a day on this 5 days a week and hope to have a very basic first iteration of a functional bot by 2023 - happy to take any advice on any of this process!

---

## 2022-09-14 09:46:51 - random channel

**Jorge**

Ah ok I get it, you read the csv with python and avoid pandas

---

## 2022-09-14 09:41:34 - random channel

**Mo**

Very easy to get a database table into pandas as well

---

## 2022-09-14 09:41:14 - random channel

**liam**

pandas is crap for trading live

---

## 2022-09-14 09:37:10 - random channel

**Jorge**

1. Yes, I read them on startup but I have multiple factors and each factor has 600 files so I would like it to be as fast as possible.

2. I save them as separate real-time files.

3. It would be very convenient, the rest of my infra supports Pandas

---

## 2022-09-14 09:30:25 - random channel

**Mo**

A few questions:



1. Why does it need to be fast? Can't you read them all on startup and be done with it?

2. Do they need to be separate files? Reading one file will probably be quicker

3. Do you actually need the end result to be a DataFrame? As you say, pandas performance is sometimes not the best 

---

## 2022-09-14 09:27:14 - random channel

**Jorge**

Reading the file with `fastparquet.ParquetFile()` is very fast but I cannot find a way of concatenating the files without converting to Pandas (which is slow...)

---

## 2022-09-14 09:26:07 - random channel

**Jorge**

Hi, I'm facing this problem: I need to load 600 files in live-trading, each of them contains a row of a DF, and concat them into a Pandas DataFrame for analysis. Anyone knows what would be a fast file format to do this? I've tried with .parquet which takes 0.03 secs/file but I need something faster...

---

## 2022-09-06 18:10:55 - issues channel

**Mona**

is there a fast way to read and parse a .tar file and put them data into pandas DataFrame using betfairlightweight?

---

## 2022-09-01 11:34:28 - issues channel

**AP**

Hi! I created an example strategy just to test some features of flumine but I'm struggling with a problem

```class ExampleStrategy(BaseStrategy):

    def start(self) -&gt; None:

        print("starting strategy 'ExampleStrategy'")



    def check_market_book(self, market: Market, market_book: MarketBook) -&gt; bool:

        return (market_book.status == "OPEN") and (not market_book.inplay)



    def process_market_book(self, market: Market, market_book: MarketBook) -&gt; None:

        for i in range(len(market_book.runners)):

            runner = market_book.runners[i]



            LPT = runner.last_price_traded



            if runner.status == "ACTIVE" and (LPT is not None):

                if LPT &lt; 2:

                    trade = Trade(

                        market_id=market_book.market_id,

                        selection_id=runner.selection_id,

                        handicap=runner.handicap,

                        strategy=self

                    )

                    order = trade.create_order(

                        side="BACK",

                        order_type=LimitOrder(price=LPT, size=2.00)

                    )



                    res = market.place_order(order)



                    if res:

                        print("Order placed: ", market_book.market_id, runner.selection_id, LPT)



    def process_orders(self, market: Market, orders: list) -&gt; None:

        if not((market.market_book.status == "OPEN") and (not market.market_book.inplay)):

            return



        for order in orders:

            if order.status == OrderStatus.EXECUTABLE:

                if order.size_remaining == 2.00:

                    market.cancel_order(order, 0.02)  # reduce size to 1.98



                if order.order_type.persistence_type == "LAPSE":

                    market.update_order(order, "PERSIST")



                if order.size_remaining &gt; 0:

                    market.replace_order(order, new_price=1.02)```

I had run this strategy on a specific market, but then the following error was raised:

```Traceback (most recent call last):

  File "/home/alessandro/venv/lib/python3.8/site-packages/flumine/simulation/simulation.py", line 97, in run

    self._process_market_books(

  File "/home/alessandro/venv/lib/python3.8/site-packages/flumine/simulation/simulation.py", line 117, in _process_market_books

    self._check_pending_packages(market_id)

  File "/home/alessandro/venv/lib/python3.8/site-packages/flumine/simulation/simulation.py", line 189, in _check_pending_packages

    order_package.client.execution.handler(order_package)

  File "/home/alessandro/venv/lib/python3.8/site-packages/flumine/execution/simulatedexecution.py", line 31, in handler

    func(order_package, http_session=None)

  File "/home/alessandro/venv/lib/python3.8/site-packages/flumine/execution/simulatedexecution.py", line 142, in execute_replace

    place_instruction_report = replacement_order.simulated.place(

  File "/home/alessandro/venv/lib/python3.8/site-packages/flumine/simulation/simulatedorder.py", line 70, in place

    return self._create_place_response(

  File "/home/alessandro/venv/lib/python3.8/site-packages/flumine/simulation/simulatedorder.py", line 181, in _create_place_response

    if self.size_remaining == 0:

  File "/home/alessandro/venv/lib/python3.8/site-packages/flumine/simulation/simulatedorder.py", line 395, in size_remaining

    size

TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'```

It seems that the execution is broken while the framework is trying to replace an order: first it tries to cancel the order, but then it discovers that the market.status is not OPEN and raise the error with

```return SimulatedCancelResponse(

                status="FAILURE",

                error_code="ERROR_IN_ORDER",

            )```

in flumine/simulation/simulatedorder.py, line 194. I don't understand why it is happening, because the check_market_book functions should already have checked that the market is OPEN. Also, in this specific case, the market is SUSPENDED before the race, Idk if it is an useful information. Can somebody help me with it?

---

## 2022-08-30 18:39:17 - general channel

**Trex44**

Almost certainly am overcomplicating it. The files are currently CSV files that are the results from a load of computation done on different races. I am concatenating them into a single pandas data frame then I am basically just using the GUI to filter the results and display various Seaborn graphs.  I am not looking to keep the results permanently though so haven't considered Amazon RDS or anything like that. The CSV's are deleted eventually.



Just wanted the filtering to be done server side then a dictionary to be sent back to the client. Trying to teach my self how apps are built/function whilst doing this. That's half the fun.

---

## 2022-08-30 09:43:33 - general channel

**Unknown**

Thought Id check a current strategy (although stakes a bit higher)..Shows the importance of matching rates.

I never really concentrated on matching rates much before the Slack group, but it has my attention now (red line profit) :grinning:

Thanks for pointing this feature out by the way, got me thinking...

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

## 2022-08-23 08:16:45 - random channel

**liam**

My general approach for new strategy development:



• Record raw data (s3)

• Process data to create signals etc. into csv's as and when, I use Strategy classes rather than loggingcontrols (quicker / more data available) through slimmed down flumine simulation (multiprocessing / [speed])

• Load into jupyter using pandas

• Join / process / create more signals if required

• Analyse / model / backtest theoretical pnl / lots of graphs

• Create real strategy / simulate / optimise stake / triggers for market capacity

• Go live

Start to finish is normally a few hours before I get bored :joy:

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

## 2022-08-21 07:20:39 - strategies channel

**Mo**

[@U01C12ZEADQ](@U01C12ZEADQ) I'm not sure what question you're referring to as "very stupid" :sweat_smile: my current line of investigation is indeed that the model needs one or more additional features and/or a structural change

---

## 2022-08-18 10:24:12 - strategies channel

**Alessio**

Very stupid question, now that i think about it. Let me assume for a second that you lay because the model underpredicts w.r.t. odds. Is it possible it underpredicts because you have a missing feature? This would not affect 'backs' too much because without the faeature it would not be able to overpredict w.r.t. odds.

---

## 2022-08-17 23:31:54 - general channel

**river_shah**

The typical numpy, pandas, sklearn stack works flawlessly 

---

## 2022-08-13 10:21:43 - betfair-news channel

**Mo**

The second package you linked to for example says



&gt; Note: Current version does not support refreshing authentication tokens. This will need to be handled manually.

This is pretty basic functionality



It seems clear there is not a big community of javascript Betfair API users but there is a big community of Python users (you're in it)



We're not dogmatic about what language you code in - there are people on here that use C/C++, C# and other languages - but there is a huge amount of value to leverage in the off the shelf Python packages:



1. [https://github.com/betcode-org/betfair|betfairlightweight](https://github.com/betcode-org/betfair|betfairlightweight), the most cutting edge Betfair API implementation across all languages

2. [https://github.com/betcode-org/flumine|flumine](https://github.com/betcode-org/flumine|flumine), a fully featured trading platform built on top of betfairlightweight

and the community expertise you have access to if you're using something everyone is familiar with

---

## 2022-08-11 10:17:49 - general channel

**James**

I am trying to create a dataframe containing Teams/Event Names, Event IDs, Competition Names and Competition IDs. I've managed to create one dataframe containing Teams/Event Names and Event IDs and another containing Competition Names and Competition IDs. How can I match up Competition Names/IDs with the Event IDs? Any help would be appreciated!

Here's the code:

```    # Create competition filter

    competition_filter = betfairlightweight.filters.market_filter(

        event_type_ids=[1],

        market_start_time={

            'to': (datetime.utcnow() + timedelta(days=7)).strftime("%Y-%m-%dT%TZ")

        })



    # Get a list of competitions

    competitions = trading.betting.list_competitions(

        filter=competition_filter

    )



    # Create competition dataframe

    competition_df = pd.DataFrame({

        'Competition': [competition_object.competition.name for competition_object in competitions],

        'ID': [competition_object.competition.id for competition_object in competitions]

    })

    print(competition_df)



    comp_id_list = competition_df['ID'].tolist()

    print(comp_id_list)



    # Create event filter

    event_filter = betfairlightweight.filters.market_filter(

        event_type_ids=[1],

        competition_ids=comp_id_list,

        market_start_time={

            'to': (datetime.utcnow() + timedelta(days=7)).strftime("%Y-%m-%dT%TZ")

        }

    )



    upcoming_events = trading.betting.list_events(

        filter=event_filter

    )



    # Create event dataframe

    events_df = pd.DataFrame({

        'Teams': [event_object.event.name for event_object in upcoming_events],

        'Event ID': [event_object.event.id for event_object in upcoming_events],

    })

    print(events_df)```

---

## 2022-08-08 12:12:56 - general channel

**Mo**

Very happy to help - any feedback/requests for new features appreciated

---

## 2022-08-01 11:05:04 - strategies channel

**Alessio**

In general if i may add, the edge of a complex modelling technology like SVM or NNs pays off only with (1) a lot of data (like millions of examples) and/or (2) a loss function that is specialized for your task. XGBoost for non-linearity and classic regression will probably squeeze 90% of it. What is much more important is defining the objective, engineer feature and clean data like no tomorrow.

---

## 2022-07-20 10:19:33 - issues channel

**liam**

This is probably my fault;



*paper trading* is just forward testing, ie. testing on live markets but no real orders being placed



*backtesting* I see as applying a strategy on historical data



*simulation* is accurate play back of historical data as is if it was live using exactly the same code/integration



I changed the name in flumine as I found backtesting to be a bit vague as the simulation in flumine is far more powerful however I accept many will argue backtesting/simulation are the same. I will regularly 'backtest' outside of flumine using csv/pandas/jupyter before coding up properly and simulating in flumine. This allows quicker iterations without the heavy processing 'simulating' requires

---

## 2022-07-16 20:02:47 - issues channel

**D**

Using pandas to create lots of small parquet files may not be performant. Have you tried plain csv or json instead? 

---

## 2022-07-16 09:14:25 - issues channel

**Rudeger Jamison**

I have a feeling it's because I write every log directly to s3 as a parquet file, using pandas. Not very fast. Perhaps I need to collect multiple orders and write them in bulk as they're collected or a time period threshold is met?

---

## 2022-07-14 17:35:50 - issues channel

**Mick**

I'm having a bash at using betfairutil... there doesn't seem to be any documentation for it (did I miss something?). But I think I am supposed to call betfairutil.prices_file_to_csv_file(filename_including_path_of_source,filename_including_path_of_destination_csv). However, I get KeyError: 'selection_id' - this is happening within pandas. The (randomly selected) input file I'm trying to process is "BASIC-1.117880714". Any ideas?

---

## 2022-07-01 16:00:04 - strategies channel

**Unknown**

Suppose the following dataframe, filtered by horses who model predicted odds was between `8 &lt;&gt; 8.02`. `winOdd` is the model projected odds for the horse.



From the universe of *1127* horses, *128* horses finished in 1st (~10.5%).



In the second example filtered by horses who model predicted odds was between `4 &lt;&gt; 4.02`



From the universe of *889* horses, *213* horses finished in 1st (~24%).



It's a valid approach to confirm that the model has an edge?

---

## 2022-06-20 13:31:30 - strategies channel

**LF**

I think there was just some misunderstanding, so when you say you want to use E[X^2] - E[X]^2 the assumption is that you are solving this analytically and not numerically, but from my understanding, you are already computing the mean numerically using the sample mean 1/n * sum(X_i), so for the variance I would go again with the sample variance, if you are a python user you can do it using pandas/numpy

---

## 2022-06-20 10:17:32 - strategies channel

**LF**

By the way, most libraries(pandas/numpy) already give you back sample variance by default

---

## 2022-05-25 20:26:21 - issues channel

**Jonjonjon**

Are you using the `sep` feature to tag your orders?



[https://github.com/betcode-org/flumine/blob/5f78864738c32eb0e59f9d8d8c498900b51a81a3/flumine/order/order.py#L66](https://github.com/betcode-org/flumine/blob/5f78864738c32eb0e59f9d8d8c498900b51a81a3/flumine/order/order.py#L66)

---

## 2022-05-12 16:40:34 - issues channel

**foxwood**

Not worth changing imho even though it is a dirty fix - presumably been there a long time and not been a problem generally it seems. Use functions like I listed above if you need true local/event time - eg I used dateAsVenueTimezone() to get the correct hour after the UK clocks changed to avoid events at certain times. That worked without change on both backtest and live when checking "market.market_start_datetime". I think when I checked my recorded files they contained "naive" utc dates (not sure about official BF files ?). Changing may risk breaking too much proven code that people already working with ? My 2p for what it's worth  - you can always hide behind the Microsoft get-out of "feature - by design" :)

---

## 2022-05-09 19:19:51 - issues channel

**Peter**

Sorry one more. You use a lambda function to filter missing values in your exported list - much quicker to do that using Pandas drop function before exporting as that takes advantage of the indexes you've already created avoiding the need for more (implicit) iteration.



I hope these observations help. You are looking to work with a lot of data, but you also have a number of opportunities for doing so more efficiently.

---

## 2022-05-09 19:17:31 - issues channel

**Peter**

Looking at your code, it's not easy to follow but you appear to be requesting data for 13 market types for every soccer match that Betfair has coming up in the next 24 hours. That part of the code seems to me to run fairly quickly.



You then prepare and load all that data into a Pandas dataframe, which doesn't look inefficient but it's a lot of data.



You then seem to be filtering out all the markets except the Match Odds and Over Under 2.5 markets, so I suspect that there's a saving to be had by not requesting data for the other .



Then you iterate over the dataframe, which is an inherently inefficient action and request market data for each market individually. You may want to consider pulling the market IDs column out as a series and requesting the data for multiple markets at the same time. (you may need to divide this into chunks, but it would still be much more efficient than making lots of individual requests)



When you make those requests, you ask for the three best offers on both side, but only seem interested in the best price.



Finally my suspicion as to what's really blowing up your processing time is that you iterate over your Matches_BetExchange dataframe (again an inherently inefficient action) to add each row to a list. Matches_BetExchange.values.tolist() would be hugely better. You then use a lambda function to sort the list (another CPU-intensive action) - much faster would be to sort the list in Pandas, taking advantage of it's built in indexing, before extracting the data.

---

## 2022-05-06 08:54:11 - issues channel

**liam**

yeah, pandas install is the only thing stopping me doing it already tbh

---

## 2022-04-30 09:29:48 - random channel

**Dave**

Turnover for me is much higher, lower margin though as I kicked out some volatile strategies in favour of higher-sharpe. Finding it hard to make fundamental improvements to models though, a handful of new features which looked decent on paper but not sure it has changed pnl trajectory much.

---

## 2022-04-29 11:31:18 - random channel

**liam**

In addition to improving (speed/features/abstractions) flumine the only thing I would do is to abstract the way its used further with a quantopian style web frontend for simulating strategies

---

## 2022-04-29 11:27:26 - random channel

**Alessio**

I guess the next step is to build a company that sells "features" for the models that people want to do this stuff ... that way you are an intermediary, no matter their performance.

---

## 2022-04-25 12:14:36 - random channel

**Newbie99**

```53265807 function calls (53250311 primitive calls) in 151.446 seconds



   Ordered by: cumulative time



   ncalls  tottime  percall  cumtime  percall filename:lineno(function)

     5682    0.076    0.000  124.859    0.022 D:\Python37\webpages\place_order_functions.py:192(place_or_cancel)

      738    0.068    0.000  124.829    0.169 D:\Python37\webpages\market_making.py:19(place_passive_order)

      341    0.007    0.000  116.552    0.342 D:\Python38\lib\site-packages\flumine\baseflumine.py:254(_process_current_orders)

      681    0.001    0.000  115.210    0.169 D:\Python38\lib\site-packages\flumine\utils.py:259(call_process_orders_error_handling)

      681    0.003    0.000  115.209    0.169 D:\Python37\webpages\betting_strategy.py:32(process_orders)

     5697   21.047    0.004   80.373    0.014 D:\Python37\webpages\risk_functions.py:18(get_runner_exposure)

     4997    0.022    0.000   43.979    0.009 D:\Python37\webpages\place_order_functions.py:188(cancel_orders_by_price)

     4997    0.014    0.000   42.767    0.009 D:\Python37\webpages\place_order_functions.py:180(get_orders)

     4997    0.541    0.000   42.754    0.009 D:\Python37\webpages\place_order_functions.py:185(&lt;listcomp&gt;)

    77775    0.790    0.000   42.540    0.001 D:\Python37\webpages\place_order_functions.py:132(construct_price)

    73587    0.095    0.000   39.810    0.001 D:\Python37\webpages\place_order_functions.py:489(adjust_price_for_self_matching)

    73587    0.390    0.000   39.715    0.001 D:\Python37\webpages\validation_functions.py:425(validate_order_self_matching)

   147174    0.484    0.000   39.253    0.000 D:\Python37\webpages\validation_functions.py:465(get_order_list)

   147174   37.736    0.000   37.736    0.000 D:\Python37\webpages\validation_functions.py:474(&lt;listcomp&gt;)

  1056788   23.509    0.000   23.509    0.000 D:\Python37\webpages\risk_functions.py:33(&lt;listcomp&gt;)

      108    0.001    0.000   21.532    0.199 D:\Python38\lib\threading.py:270(wait)

      997   21.530    0.022   21.530    0.022 {method 'acquire' of '_thread.lock' objects}

      464    0.004    0.000   21.454    0.046 D:\Python38\lib\queue.py:153(get)

     5697    0.030    0.000   19.673    0.003 D:\Python37\webpages\risk_functions.py:78(check_combined_strategy)

     5697    3.140    0.001   19.598    0.003 D:\Python37\webpages\risk_functions.py:86(&lt;listcomp&gt;)

       50    0.002    0.000    9.686    0.194 D:\Python38\lib\site-packages\flumine\baseflumine.py:134(_process_market_books)

      625    0.001    0.000    9.638    0.015 D:\Python38\lib\site-packages\flumine\utils.py:222(call_strategy_error_handling)

       57    0.000    0.000    9.624    0.169 D:\Python37\webpages\betting_strategy.py:22(process_market_book)

  2113432    4.618    0.000    9.271    0.000 D:\Python38\lib\site-packages\flumine\utils.py:80(create_cheap_hash)

  8518043    4.560    0.000    8.305    0.000 D:\Python38\lib\site-packages\flumine\order\order.py:426(size_matched)

  2113059    2.288    0.000    7.743    0.000 D:\Python37\webpages\risk_functions.py:11(get_order_matched_exposure)

  4291494    2.451    0.000    7.361    0.000 D:\Python37\webpages\risk_functions.py:4(get_order_matched_stake)

  2113821    3.039    0.000    5.130    0.000 D:\Python38\lib\site-packages\flumine\order\order.py:259(customer_order_ref)

 10643310    4.577    0.000    4.577    0.000 D:\Python38\lib\site-packages\flumine\order\order.py:188(current_order)

     5696    0.775    0.000    4.467    0.001 D:\Python37\webpages\risk_functions.py:39(&lt;listcomp&gt;)

   1391/2    0.018    0.000    3.269    1.635 {built-in method builtins.exec}

        1    0.000    0.000    3.269    3.269 startup.py:1(&lt;module&gt;)

  1045/16    0.014    0.000    3.082    0.193 &lt;frozen importlib._bootstrap&gt;:986(_find_and_load)

  1044/16    0.007    0.000    3.081    0.193 &lt;frozen importlib._bootstrap&gt;:956(_find_and_load_unlocked)

  1002/16    0.007    0.000    3.066    0.192 &lt;frozen importlib._bootstrap&gt;:650(_load_unlocked)

   890/16    0.005    0.000    3.065    0.192 &lt;frozen importlib._bootstrap_external&gt;:777(exec_module)

  1348/16    0.002    0.000    3.053    0.191 &lt;frozen importlib._bootstrap&gt;:211(_call_with_frames_removed)

  2113432    2.341    0.000    2.341    0.000 {method 'hexdigest' of '_hashlib.HASH' objects}

  2113469    1.233    0.000    2.061    0.000 D:\Python38\lib\site-packages\flumine\order\order.py:419(average_price_matched)

      341    0.013    0.000    1.827    0.005 D:\Python38\lib\site-packages\flumine\order\process.py:33(process_current_orders)

  563/115    0.003    0.000    1.797    0.016 {built-in method builtins.__import__}

       46    0.001    0.000    1.721    0.037 D:\Python38\lib\site-packages\flumine\order\process.py:93(create_order_from_current)

        7    0.000    0.000    1.603    0.229 D:\Python38\lib\site-packages\flumine\baseflumine.py:197(_add_market)

        7    0.008    0.001    1.596    0.228 D:\Python37\webpages\middleware_example.py:24(add_market)

2117384/2117380    1.525    0.000    1.525    0.000 {method 'format' of 'str' objects}

 1227/677    0.003    0.000    1.475    0.002 &lt;frozen importlib._bootstrap&gt;:1017(_handle_fromlist)

     1586    0.005    0.000    1.400    0.001 D:\Python38\lib\logging\__init__.py:1553(_log)

        1    0.000    0.000    1.335    1.335 D:\Python37\webpages\orders_worker.py:1(&lt;module&gt;)

        1    0.000    0.000    1.332    1.332 D:\Python37\webpages\racing_functions.py:1(&lt;module&gt;)

  2113432    1.331    0.000    1.331    0.000 {built-in method _hashlib.openssl_sha1}

        1    0.000    0.000    1.325    1.325 D:\Python37\webpages\import_historic_horse_data.py:1(&lt;module&gt;)

     1586    0.002    0.000    1.308    0.001 D:\Python38\lib\logging\__init__.py:1579(handle)

     1586    0.012    0.000    1.305    0.001 D:\Python38\lib\logging\__init__.py:1633(callHandlers)

     4758    0.011    0.000    1.293    0.000 D:\Python38\lib\logging\__init__.py:937(handle)

    77775    0.183    0.000    1.271    0.000 D:\Python37\webpages\place_order_functions.py:222(get_base_price_source)

     4758    0.019    0.000    1.265    0.000 D:\Python38\lib\logging\__init__.py:1069(emit)

     1505    0.007    0.000    1.249    0.001 D:\Python38\lib\logging\__init__.py:1424(info)

        6    0.000    0.000    1.222    0.204 D:\Python38\lib\site-packages\requests\api.py:16(request)

        6    0.000    0.000    1.199    0.200 D:\Python38\lib\site-packages\requests\sessions.py:470(request)

     4997    0.018    0.000    1.189    0.000 D:\Python37\webpages\cancel_and_replace.py:33(cancel_orders)

        6    0.000    0.000    1.111    0.185 D:\Python38\lib\site-packages\requests\sessions.py:626(send)

        6    0.000    0.000    1.105    0.184 D:\Python38\lib\site-packages\requests\adapters.py:394(send)

   153222    1.010    0.000    1.078    0.000 D:\Python38\lib\site-packages\flumine\markets\blotter.py:268(__iter__)

        6    0.000    0.000    1.062    0.177 D:\Python38\lib\site-packages\urllib3\connectionpool.py:518(urlopen)

        6    0.000    0.000    1.058    0.176 D:\Python38\lib\site-packages\urllib3\connectionpool.py:357(_make_request)

        5    0.000    0.000    1.056    0.211 D:\Python38\lib\site-packages\requests\api.py:107(post)

        1    0.000    0.000    1.056    1.056 D:\Python38\lib\site-packages\pandas\__init__.py:3(&lt;module&gt;)```

---

## 2022-04-13 14:36:52 - random channel

**Mo**

Yes, something like this:



```import pandas as pd



import betfairutil

import betfairviz



market_books = betfairutil.read_prices_file('../betfair-hackathon-2021/1.176457983.bz2')



volumes_traded = pd.Series(betfairutil.calculate_total_matched(mb) for mb in market_books).diff()



points_of_interest = [

    betfairviz.PointOfInterest(

        text='Market suspension at ' + betfairutil.publish_time_to_datetime(mb['publishTime']).strftime('%Y-%m-%d %H:%M:%S.%f'),

        timestamp=betfairutil.publish_time_to_datetime(mb['publishTime'])

    )

    for prev_mb, mb in zip(market_books, market_books[1:]) if mb['status'] == 'SUSPENDED' and prev_mb['status'] != 'SUSPENDED'

]



betfairviz.create_dashboard(market_books, points_of_interest=points_of_interest)```

---

## 2022-03-17 20:50:08 - general channel

**Jonjonjon**

Is transferring the results from AWS to local machine a pain? I usually use a loggingcontrol to write my backtest orders to disk. And then use Jupyter or Spyder to load them into a dataframe for analysis

---

## 2022-03-14 18:02:40 - random channel

**Peter**

My starting point is to use a categorical variable in statsmodel and look at the coefficients and the p-test results to see whether the feature on which I might split has the variability and significance to justify a split.

---

## 2022-03-14 15:49:52 - random channel

**D C**

I basically just want to be able to model using GLMs in a similar manner to that of R so that I can do model validation, residual checks and all the other stuff. This PolynomialFeatures looks to be more useful for pure approximation problems rather than inference. I am clearly going to have to get used to changes in terminology over the last 20 years. What seems now to be called a "feature" we used to call an explanatory or dependent variable. Similarly design matrix (or observation matrix) now seems to be called feature matrix. I guess this is ML based terminology superceding the stats/approximation theory lingo now. I'll stick with R for now as I don't want to be creating extra columns myself to try to model interaction effects.

---

## 2022-03-14 15:34:23 - random channel

**Alex Alex**

Did you have a look at `sklearn.preprocessing.PolynomialFeatures` ([https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)) I’m not sure how the R implementation differs from the PolynomialFeatures. Generally I occasionally use sklearn for this purpose and never found it too bad. You can neatly package this into a pipeline with whatever model you want to run afterwards.

---

## 2022-03-14 14:00:38 - random channel

**D C**

I've been starting to use Python to perform logistic regression but struggling to find a way to model interaction effects. In R this is easy. I've tried sklearn and statsmodels but so far can't see an easy way to do this as both make use of the dataframe columns you provide. I am brand new to this in a python setting so may have missed something obvious but is there a simple way to do this or am I better off (from speed point of view) sticking with R ?

---

## 2022-03-12 19:13:36 - random channel

**Mo**

Have production and test servers both running live trading code. New features get live tested before going into production

---

## 2022-03-12 15:25:33 - general channel

**Peter**

I do similar but in parallel. I chunk the markets by day and then use multithreading to run each day in a separate thread. Each day's results are persisted to a csv file and it's then trivial to load all available days into Pandas and summarise the results. It's also easy to spot any days that fail and either restart from there or just hit any holes.

---

## 2022-03-11 12:53:33 - general channel

**jhaa**

I am looking for examples on how to convert what the flumine marketrecorder saves to a pandas dataframe or a dict for betfairviz.  Any suggestions?

---

## 2022-03-05 10:23:22 - issues channel

**Ruben**

yes, what I do to look at data in a columnar way is use jupyter notebooks (is installed automatically if you install the python anaconda environment). With that you can directly read a csv with pandas, and then look at as many rows of the dataframe you want

---

## 2022-03-05 10:03:50 - issues channel

**ThomasJ**

[@U011VL3CA2Y](@U011VL3CA2Y) Yes Excel does 'things' to data and it's a damn nuisance and I trip over it all the time.



So whilst on the subject of looking at data visually...

I program in Python for Betfair stuff (relatively newish) and of course use Pandas DataFrames extensively.

I often dump the DataFrame to disk as '.csv'.

To look at this '.csv' file in a 'raw' (unaltered way) I use Notepad++, but of course it's hard to see things columnar wise.

Is there any way I can look at data in columns with headings in it's raw state?

---

## 2022-02-17 09:12:08 - issues channel

**Stefan**

[@U02QDJCK3NW](@U02QDJCK3NW) Betfair rest api offers CompetitionIds, UEFA Champions League has 228 CompetitionId. I do not know why betfair did not implemented the same filter to streaming api. In the streaming api we have got Venues filter, but that works only for horse racing.



 [@UUUAJQZ5J](@UUUAJQZ5J) you work for betfair, please put to your list of suggestions implementing all features of rest api filter to streaming api, or at least extending functionality of venues to all events, in this case venue would be competition name, like UEFA Champions League.



Here is my test code. My code implementation uses Subscribe function that can take streaming filter, or markets, so it this case, I have queried markets by:



let filter = [ CompetitionIds [| 228 |]; MarketTypeCodes [| "MATCH_ODDS" |] ]



and then subscribed to streaming api, lines from 74 to 78:



[https://github.com/StefanBelo/Bfexplorer-BOT-SDK/blob/master/TestStreamingAPI/Program.fs](https://github.com/StefanBelo/Bfexplorer-BOT-SDK/blob/master/TestStreamingAPI/Program.fs)



As my code implements 2 Subscribe function, I can call first Subscribe to:



let filter = [ BetEventFilterParameter.BetEventTypeIds [| 1 |]; BetEventFilterParameter.Countries [| "GB" |]; BetEventFilterParameter.MarketTypeCodes [| "MATCH_ODDS" |] ]



and the next call to Subscribe by using markets, re-subcribers all already open markets plus new ones.



If you are .net developer you can use my bot sdk, if not you can reengineer my solution to your code.



Here is short video from my test:



[https://youtu.be/EGsYN0RXtNw](https://youtu.be/EGsYN0RXtNw)

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

## 2022-02-16 12:32:21 - random channel

**Chris H**

sure- my question was more that it seems like betfair providing this clk/ reconnect feature is pointless as you can just reconnect and received fresh image which will return your book to the correct state.



From the user perspective I'm not sure what using clk/initialclk adds other than some minor complication

---

## 2022-02-13 18:04:12 - issues channel

**Brøndby IF**

```import datetime

import pandas as pd

import betfairlightweight

import time



username = 'AAAAAAAAAAAAAAAAAAAAAA'

pw = 'BBBBBBBBBBBBBBBBBB'

app_key = 'CCCCCCCCCCCCCC'



trading = betfairlightweight.APIClient(username, pw, app_key=app_key, cert_files=('./certs/myAppBetfair1.crt','./certs/client-2048.key'))

trading.login()



df_final = pd.DataFrame()

for i in range(0,1):

    order_filter = betfairlightweight.filters.ex_best_offers_overrides(

        best_prices_depth=3

    )



    price_filter = betfairlightweight.filters.price_projection(

        price_data=['EX_BEST_OFFERS'],

        ex_best_offers_overrides=order_filter

    )



    # Obtendo odds para o mercado

    market_books = trading.betting.list_market_book(

        market_ids=['1.190674822'],

        price_projection=price_filter

    )



    #Lista de runners

    runners = market_books[0].runners



    back = []

    for i in range(0,3):

        try:

            back.append([runner_book.ex.available_to_back[i].price

                                    if runner_book.ex.available_to_back

                                    else 1.01

                                    for runner_book

                                    in runners])

        except:

            back.append([1.01,1.01])



    df_back = pd.DataFrame(back,columns=['Casa','Visitante','Empate'])

    df_back['data'] = datetime.datetime.now()

    df_final = df_final.append(df_back)

    time.sleep(2)```

To collect the odds offered in back I use this code, could someone help me and show me how the code would look if I wanted to collect the lastPriceTraded instead of the offered odds?



The person who helps me with codes is on vacation and I really need help to do this, unfortunately I can't do it alone.

---

## 2022-02-08 20:40:41 - general channel

**liam**

Certainly recommend streaming, much lighter on CPU and reduces the complication. 



What issues are you seeing the historical data? Thought the pro stuff was good.



flumine can do whatever you want, the selling point is the switch to backtest / paper / live with no changes to your code.  Switching wouldn’t make sense depending on how advanced your current setup is and/or you want some of the features. 

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

## 2022-01-30 14:04:07 - issues channel

**Jonjonjon**

How many strategies are attached to each Flumine instance? I'm at about 60 strategies on one of my instances and it's using a lot more CPU, but I have a feeling my moving average implementation might be non-optimal.

---

## 2022-01-26 08:16:56 - issues channel

**Jorge**

Just my 2 cents, I finally understood what is consuming my RAM memory. Just by the packages I import in my bot, it consumes 68MB. `import pandas` alone consumes 36 MB. This is a bit of a problem when I run 100x bots :smile:

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

## 2022-01-13 11:14:21 - general channel

**rob smith**

`import betfairlightweight`

`import datetime`

`import pandas as pd`

`from betfairlightweight import filters`

`from time import sleep`

`from datetime import datetime`

`from datetime import timedelta`



`username = ""`

`password = ""`

`api_key = ""`

`pd.set_option('display.max_rows', 1000)`



`def current_time(message):`

    `current_time = datetime.now()`

    `current_time = current_time.strftime('%H:%M:%S:%f')`

    `print(f'{current_time}: {message}')`



`def get_todays_games():`



    `trading = betfairlightweight.APIClient(`

            `username, password, app_key=api_key`

        `)`

    `trading.login_interactive()`

    `print("Logged in")`



    `trading.keep_alive()`



    `t20_filter = betfairlightweight.filters.market_filter(`

        `event_type_ids=[4],`

        `market_type_codes=["MATCH_ODDS"],`

        `market_start_time={`

            `'to': (datetime.utcnow() + timedelta(days=1)).strftime("%Y-%m-%dT%TZ")`

        `}`

    `)`

    `t20_events = trading.betting.list_events(`

        `filter=t20_filter`

    `)`



    `t20_events_today = pd.DataFrame({`

        `'Event Name': [event_object.event.name for event_object in t20_events],`

        `'Event ID': [event_object.event.id for event_object in t20_events],`

    `})`



    `print(t20_events_today)`



    `print()`

    `event_id = input("Input Event ID:  ")`

    `print()`



    `market_catalogue_filter = betfairlightweight.filters.market_filter(event_ids=[event_id])`



    `market_catalogues = trading.betting.list_market_catalogue(`

        `filter=market_catalogue_filter,`

        `max_results='100',`

        `sort='FIRST_TO_START'`

    `)`



    `market_types_mooney_valley = pd.DataFrame({`

        `'Market Name': [market_cat_object.market_name for market_cat_object in market_catalogues],`

        `'Market ID': [market_cat_object.market_id for market_cat_object in market_catalogues],`

        `'Total Matched': [market_cat_object.total_matched for market_cat_object in market_catalogues],`

    `})`

    `print(market_types_mooney_valley)`



    `print()`

    `market_id = input("Input Market ID:  ")`

    `print()`



    `market_books = trading.betting.list_market_book(`

            `market_ids=[market_id],`

            `price_projection=filters.price_projection(`

                `price_data=filters.price_data(ex_all_offers=True)`

            `),`

        `)`



    `while True:`

        `for market_book in market_books:`

            `print(` 

                `market_book.market_id,`

                `market_book.inplay,`

                `market_book.status,`

                `market_book.total_matched,`

            `)`

        `sleep(1)`



        `if market_book.inplay == True:`



            `while True:`

                `for runner in market_book.runners:`

                    `print(`  

                        `runner.selection_id,`

                        `runner.status,`

                        `runner.last_price_traded,`

                        `runner.total_matched,`

                    `)`

                `sleep(1)`



`get_todays_games()`

---

## 2022-01-07 08:51:57 - strategies channel

**Peter**

[@U0160E9HS2G](@U0160E9HS2G) In the scenario you posited, you would still suffer from adverse selection. Your offer is taken or you're able to take that price, because on balance the market (which is slightly better informed than your model) recognises a -EV opportunity. Ignoring commission helps, but in markets with very small spreads it becomes disproportionately important, so ignoring it helps with your hypothesis, but will adversely affect your bank.



To recast slightly what I was saying earlier, I believe that there's a consensus here that the market is pretty darned good, but not perfect. So most of the time it's pretty much accurate, but sometimes it's a bit off. Classic financial theory holds that efficient markets incorporate all the publicly available information and reflect it in their prices. By contrast your model incorporates only the information that it can infer from the features that you have given it. So most of the time the market performs better than your model 'cos it knows more, but sometimes your model may perform better than the market 'cos what it does know is more important in specific circumstances.



So if you use your model all of the time, you'll sometimes win, but mostly lose. The trick is to identify those (I'll use [@UBS7QANF3](@UBS7QANF3)'s word here) scenarios where your model outperforms the market and then focus all your attention there.



I agree with [@UBS7QANF3](@UBS7QANF3) too that the times when your model deviates the most from the market are probably the times when your model is the least performant.

---

## 2021-12-22 01:46:23 - issues channel

**JFP**

Found the issue, it is not a Flumine one, it is my error in assembly of dataframe. It occurs when adding runner status and bsp from spList.



The spList is created for all runners in def process_closed_market. I have added status and bsp to df based on selection_id match:

```for L in spList:

    df.loc[df['selection_id'] == L[0], 'bsp'] = L[2]

    df.loc[df['selection_id'] == L[0], 'selection_status'] = L[1]```

---

## 2021-12-22 01:41:28 - issues channel

**JFP**

Found the issue, it is error in assembly of dataframe. It occurs when adding runner status and bsp from spList.



The spList is created for all runners in def process_closed_market. I have added status and bsp to df based on selection_id match:

```for L in spList:

    df.loc[df['selection_id'] == L[0], 'bsp'] = L[2]

    df.loc[df['selection_id'] == L[0], 'selection_status'] = L[1]```

---

## 2021-12-21 14:03:35 - general channel

**Peter**

If you install [https://github.com/jupyterlab/jupyterlab-desktop|Jupyter Desktop](https://github.com/jupyterlab/jupyterlab-desktop|Jupyter Desktop) it will create a whole working environment for you, including Pandas and its dependancies.

---

## 2021-12-21 12:53:30 - general channel

**Aaron Smith**

pandas is a library in python, jupyter is a devloping enviroment (like an IDE) in which you write your python code. Its not a decision between pandas or jupyter, best would be to use the two in combination. I dont have a tutorial at hand, but i m certain there are thousands out there if you search for it :slightly_smiling_face:

---

## 2021-12-21 12:37:02 - general channel

**Techno**

OK. Thanks Aaron. Pandas sounds like the best one. Is there a good tutorial for it somewhere on the net please?

---

## 2021-12-21 12:34:53 - general channel

**Aaron Smith**

[@U02QK8FE1K7](@U02QK8FE1K7) yes, you can read csv files with pandas. Jupyter uses python and its better to use in this case than just a common IDE, as it allows you to run sections of your code seperatly so you dont have to run time intensive operations multiple times only to adjust a minor thing in the analysis

---

## 2021-12-21 12:24:32 - general channel

**liam**

Juypter / pandas 

---

## 2021-12-21 08:46:19 - issues channel

**JFP**

Here is my backtest code



```client = clients.BacktestClient()



framework = FlumineBacktest(client=client)



root_folder = 'C:/BF_PRO_DATA/Nov/'

folders = os.listdir(root_folder) #list of folders

markets = []



for folder in folders:

    folder = os.path.join(root_folder, folder) #dir to open folder in list of folders

    _markets = os.listdir(folder) # list of files inside folder inside list of folders

    _markets = [x for x in _markets if x.endswith('.bz2')] #adds file names to list

    _markets = [os.path.join(folder, x) for x in _markets] #adds file names to a dir string

    markets.extend(_markets) #adds exact dir for each file to market list





spList=[]



class Test1(BaseStrategy):





    def check_market_book(self, market, market_book):

        if (market.seconds_to_start &lt;= 360) and (market_book.status != "CLOSED") and not market_book.inplay and market.market_type == "WIN":

            return True



    def process_market_book(self, market, market_book):

        

        if (ABC):



            for runner in market_book.runners:

                

                runner_context = self.get_runner_context(market.market_id, runner.selection_id, runner.handicap)

                

                back1 = get_price(runner.ex.available_to_back, 0)

                back2 = get_price(runner.ex.available_to_lay, 0)

                

                #exit current selection itteration if back1 = None

                if back1 == None or back2 == None:

                    continue



                

                if (XYZ):

                        

                    trade = Trade(

                        market_id=market_book.market_id, 

                        selection_id=runner.selection_id,

                        handicap=runner.handicap,

                        strategy=self

                    )

                    

                    order = trade.create_order(

                        side= Side, 

                        order_type=LimitOrder(price=back1, size= sizeB1),

                        notes=OrderedDict(market_vol=round(totalVol, 4), sel_volume = selTradedVol, event_details = market_book.market_definition.name, order_num = 1)

                    )

                    

                    market.place_order(order)

                        

    def process_closed_market(self, market, market_book) -&gt; None:



        for runner in market_book.runners:

            spList.append([runner.selection_id, runner.status, runner.sp.actual_sp])





with mock_patch("builtins.open", smart_open.open):

    strategy = Test1(

        market_filter={"markets": markets,"listener_kwargs": {"seconds_to_start": 360}, "market_types":["WIN"]},

        max_trade_count = 4,

        max_live_trade_count = 4,

        max_order_exposure = 10000,

        max_selection_exposure = 20000

    )

    framework.add_strategy(strategy)

    framework.run()



dfList=[]



for market in framework.markets:



    for order in market.blotter:

        dfList.append(

        [

            market.venue,

            market.country_code,

            market.event_name,

            market.market_start_datetime,

            order.market_id,

            order.selection_id,

            order.notes['event_details'],

            order.notes['market_vol'],

            order.notes['sel_volume'],

            order.notes['order_num'],

            order.responses.date_time_placed,

            order.status,

            order.order_type.price,

            order.average_price_matched,

            order.size_matched,

            order.simulated.profit,

        ]

        )



df = pd.DataFrame(dfList, columns = ['market_venue', 'country_code', 'event_name', 'market_start_datetime', 'market_id', 'selection_id', 'event_details', 'market_vol', 'sel_volume', 'order_num', 'time_placed', 'status', 'price', 'average_price_matched', 'size_matched', 'simulated_profit'])

df['weekday'] = df['time_placed'].dt.dayofweek

df['month'] = df['time_placed'].dt.month



#add bsp

df['bsp']=df['selection_id']

df['selection_status'] = df['selection_id']



for L in spList:

    df.loc[df['selection_id'] == L[0], 'bsp'] = L[2]

    df.loc[df['selection_id'] == L[0], 'selection_status'] = L[1]```

---

## 2021-12-19 07:11:24 - general channel

**Peter**

Depends. That's an option. Most of the time though it's just a connection string that includes the host address. E,g,



```import pymysql

import pandas as pd

from sqlalchemy import create_engine



engine = create_engine("mysql+pymysql://{user}:{password}@{host}/{database}".format(

    user=os.getenv("DB_USERNAME"),

    password=os.getenv("DB_PASSWORD"),

    host=os.getenv("DB_HOST"),

    database=os.getenv("DB_DATABASE")

))```

then



```sql = "some sql in here"

df = pd.read_sql(sql, engine)```



---

## 2021-12-18 08:09:04 - general channel

**D**

Just to add another viewpoint to all the good advice above: I used RDS (postgres) for quite a while but it started to seem expensive, especially for historical data I was hardly ever querying. My current approach is to upload csv, parquet and json data to S3 locations and use Athena to query them into pandas dataframes. Don't have any issues so far; performance is good and I can add new data to my json files without breaking existing queries.

---

## 2021-12-18 07:25:52 - general channel

**Peter**

First reason would be that while it is easy to dump objects into into mongo as documents, it's often way more difficult to get them back out again. The keys that you want to use for retrieval may be several layers down in the documents and absent from some of them. Setting up the indices for efficient retrieval can be complicated too unless all your documents are the same shape, which as you venture into more sports they won't be.



Another reason is that I do most of my analysis in Pandas which, like RDS, works with a column and row paradigm, so I can import data directly from RDS into Pandas with a single line of code. Or if like [@U016TGY3676](@U016TGY3676) you like CSVs, you can export directly to there too :wink:.

---

## 2021-12-15 09:45:27 - random channel

**Oliver Varney**

Anyone know of better options office options on linux then libreoffice (calc) to tinker with formulas (other then python stuff like pandas)? Man it crashes constantly ..

---

## 2021-12-08 23:44:22 - general channel

**Paul**

So I think knowing a lot about successful strategies can help close the avenues down, and then with a few hundred hours of building the gym and feature engineering you might get somewhere. I'm on that path myself, albeit slowly.

---

## 2021-12-07 07:49:59 - general channel

**river_shah**

Traversing the abstract syntax tree and dumping out llvm is probably the cleanest way to go full compiled speeds with python. I hope this kind of feature and  complete GIL removal makes it into python 3.11+

---

## 2021-12-06 11:38:49 - general channel

**ThomasJ**

Ah right...so do yourself a favour and get into Matplotlib for graphs.

Took me quite a while to come to grips with it but it's power is all you will ever need for the rest of your life. Big statement I know.

So csv to be read by Pandas and then Pandas to Matplotlib.

import pandas as pd

var1 = pd.read_csv("your_csv_file")

var1 is now a pandas dataframe and off you go.

---

## 2021-12-06 10:35:08 - general channel

**Javier Martín Pérez**

Hi [@U01U24AG35W](@U01U24AG35W), I do all my programming on Python but when it comes to check bets P/L graphs etc I normally use Excel because I am used to it. Probably the best is to use Pandas but never used it to display data so will need to get my head around it for a while.

---

## 2021-12-06 10:18:13 - general channel

**ThomasJ**

Hi [@U026WRD7SHE](@U026WRD7SHE) You mentioned Excel and Tableau which are "high level wrappers" for handling data. But what most people do not realize is it that their "target market" is business users so only Bill Gates needs to concern himself with '$16+ digit numbers' :slightly_smiling_face:

In this space of Betfair data analysis, programming in Python is your best bet, and Pandas with it's gazillion features (methods) is unsurpassed due to the many many more code examples on the internet.

---

## 2021-12-06 08:33:01 - general channel

**liam**

jupyter / pandas

---

## 2021-12-06 08:32:31 - general channel

**Javier Martín Pérez**

I have been using csv files to store data like bets placed, etc but I have had several problems with Excel when I have to edit them. Apparently most of the most annoying features of Excel (like the rounding up of 16+ digit numbers) are unavoidable and I was wondering if there is a better software that you are usually using. The notepad works relatively well but is generally difficult to work with. I remember that when I used Tableau in the past it was very slow, is it better nowadays?

---

## 2021-12-03 07:06:07 - general channel

**captainonionhead**

I've only recently got going and have 2 python processes (one recorder, one simple strategy to keep Betfair happy whilst I gather some data).  These are running on a VPS I already had that I've repurposed.  It's roughly equivalent to a nano and I'm nowhere near stressing it.

However, I'm expecting to move to something more like Peter's setup with many processes on different instances at least partly because it allows me to update different parts of my code/infrastructure without having to take everything down.  At the moment I have a lot of code churn as I implement new features and I expect that to continue as I develop strategies and refine ones that are already running.

---

## 2021-12-02 11:35:07 - strategies channel

**Peter**

But you are absolutely right that he's not giving too much away. As [@UBS7QANF3](@UBS7QANF3) hinted earlier, the key to success is often coming up with a feature or features that other people aren't using to give you a small edge. He's not giving us anything from his personal secret sauce. Indeed he's showing in his predictions calibration section that there's still rather a lot of work needed to make that model usable.

---

## 2021-12-01 22:35:30 - strategies channel

**AndyL**

[@U4H19D1D2](@U4H19D1D2) correct i am doing a simple approach. Basically ive been watching loads of races and corresponding odds and looking at recent form, and ive created my own price formula from the standard features, recent finish positions, recent normalised speed avg and max, recent normalised sectional timings...

I actually quite like the prices it produces, i watch races and compare mine v market, and quite often think mine are more true. For example i quite often see a dog go up a grade and the market immediately gives it a very short fav price say 2.0,but my model has it say more at 3.5+, and to me the market has it so wrong the dog typically finishes near last...

This is where i think my model falls down it's trying to cover all prices and all dogs. Taking what [@UNQGKT0CR](@UNQGKT0CR) i think said isolate more specific variables, eg.short priced upgrade...

---

## 2021-12-01 20:31:21 - strategies channel

**Peter**

A lot of skill when using ML is determining the appropriate type of model to use. Choose a model that takes a set of features and gives you a simplistic answer, and that's what you'll get. But there are other model types, e.g. logistic regression, that do assign probabilities for each possible outcome.

---

## 2021-11-30 21:32:18 - issues channel

**Tom**

Thanks Liam. Turns out that `get_order_from_bet_id` bottleneck was *a* bottleneck but not *the* bottleneck that was causing my issues. I managed to get my `process_market_book` step down to an average of 1-5ms from 10-40ms by removing some pandas objects and using blotter exposures rather than calculating the matched exposures from the orders myself. Seems to have done the trick runs only like 10% CPU utilisation on a 2vCpu 4 Gb ram machine now and none of these accumulating latency issues

---

## 2021-11-16 13:41:55 - general channel

**birchy**

[@U013ZS16QJZ](@U013ZS16QJZ) I have been "botting" for 15+ years but am not a developer or programmer. Up until about 12 months ago, I was using a self-created Betfair API polling library ([http://www.bespokebots.com|bespokebots.com](http://www.bespokebots.com|bespokebots.com)) but decided I needed to upgrade to the streaming API. It didn't make sense for me to code it myself when [@U4H19D1D2](@U4H19D1D2) had already developed a tried and tested library. Despite "knowing" python, I struggled to get to grips with Flumine and am still discovering new features and functions. As stated above start off with using the examples and get one of them working. I'd recommend getting the marketrecorder running as that should work "out of the box", so you only need to fathom out the login procedure. Then look at strategies, preferably via the lowestlayer example and backtesting feature. For that, you'll need data, which the marketrecorder will provide.

---

## 2021-11-05 10:28:02 - strategies channel

**liam**

python

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

---

## 2021-11-05 09:58:55 - strategies channel

**liam**

Have you tried to analyse the strategy described by Dallas? For example:



• Get some pre race data

• Push through bflw and record WOM% / price / odds / … / result into a csv

• Pull into pandas see if there is any relationship between WOM/price/result and thus value 

• The above can be done with graphs/regression/ml etc.

My assumption would be that the above is a half day job and would probably lead you down another route. Also note that we are ignoring matching etc but it would give you a good idea if the idea has any value.

---

## 2021-11-01 13:47:10 - random channel

**Oliver Varney**

A performance on a given day probably cant be boiled down to one attribute. Youve got weight carried, going + actual going, jockeys, weight allowances, interference all sorts really. I think you will end up creating a feature that is way too specific and wont generalise. Furthermore if a horse cant place the jockey will walk the horse over the line and distances then can be misleading. What I will say is in-play odds can be used to determine how well a horse has run, even if it hasnt won.

---

## 2021-10-28 10:38:22 - issues channel

**JC**

Running that gives AttributeError: 'NoneType' object has no attribute 'utcnow'. It did fix it by adding the context manager in source but this may mess up other things? Seems ok for just generating dataframes but not sure about simulated orders etc.

---

## 2021-10-20 12:19:16 - general channel

**ThomasJ**

[@U01UN2R5LM8](@U01UN2R5LM8) You said "But if doing so does not speed up the backtesting, i guess that is pointless." ... well it might speed things up if you summarize data...but what to summarize? You'll find that over even a short time of backtesting you'll want to look at data in many different ways and you'll keep on producing different summaries. So the production of the summaries and then testing on them will probably be way longer than just reading from the raw data, putting it into memory via, as liam mentioned a Pandas DataFrame (I presume it's Pandas), and then you can look at the data in an infinite number of ways directly, and super fast.

---

## 2021-10-17 08:49:50 - random channel

**Oliver Varney**

Morning, im looking for some advice on hosting platforms, mainly AWS vs the rest. I am just about to start re-writing some of my services and was just wondering what peoples thoughts are on the best way to go. From what I understand if I go with AWS (rather then something like linode) im getting a large product/ feature set but in return paying higher costs and potentially slightly slower performance (from what ive read thus far). Is there any specific things around AWS and Betfair/betting that are also advantages of using it. From my understanding betfair are hosted on AWS? im pritty clueless when it comes to this stuff so would be interested in the techy guys thoughts.

---

## 2021-10-10 20:31:17 - random channel

**Jonjonjon**

In essence,  have a dataframe of 3 columns:



• forecasted return

• actual return

• market variable (e.g. time, volume, volatiliy etc...)

My strategy enters a trade if the forecasted return is greater than some threshold.



That threshold is a function of the market variable.



I'm trying to fit a piecewise linear function to the threshold.



So the dimensions are the knots on the piecewise linear function.

---

## 2021-09-29 14:49:48 - general channel

**Peter**

Recommended method is to persist live market streams, including price data, to files and then re-stream from there as many times as you need to test different placing strategies, at which time you could use logging control to write to a database - though I suspect many will write to a csv file or similar for ingestion into a Pandas dataframe.

---

## 2021-09-08 11:25:19 - general channel

**Jono**

so it loops though the markets appending them to generate the full dataframe does

`[http://logging.info|logging.info](http://logging.info|logging.info)("Generating bet dataframe from all markets")`

`for market in flumine.markets:`

    `bet_df = bet_df.append(market.context['bet_df'], ignore_index=True)`



then makes the api call.

Finally my plan would be to loop through them again and clear them, ie something like





`[http://logging.info|logging.info](http://logging.info|logging.info)("Clearing bet dataframe for all markets")`

`for market in flumine.markets:`

    `bet_df = pd.DataFrame(columns=['placed_at', 'external_event_id', 'external_bet_id'])`



The reason i did it this way is i wasnt sureif there was a "strategy.context" of sorts that you can access from all markets and append to the same dataframe. Thus each market has a df that is joined together in the worker

---

## 2021-09-08 10:35:05 - general channel

**Jono**

im currently using market.context to store a pandas df, 3 timetamps and a handful of lists. These are updated every 10 seconds or so but can increase in frequency occasionally being accessed and updated every market book. The process_market_book, process_orders, and a worker all access these variables and make changes to them as well as base decisions on their values. I was wondering best practices to avoid problems accessing or trying to update the same value at once? For example the dataframe is populated during process_market_book, the worker sends then sends said dataframe (market.context['pd_dataframe']) to an api and then attempts to clear the df. Would clearing the df in the worker cause conflicts if it at the same time the market.context is being accessed/updated at the same time in process_market_book? Sorry if this is a skewed understanding of the framework im still getting to grips with the package and threading. Thanks

---

## 2021-09-08 08:34:25 - general channel

**Jonjonjon**

[@U013K4VNB6D](@U013K4VNB6D) It depends on what you are doing. If you are planning on using Flumine with backtesting and multiprocessing, I would recommend a minimum of 1GB RAM per CPU thread.



So I have 32 CPU threads and 32GB RAM. I will occasionally run out of RAM when backtesting on 31 threads. That could be due to my bad coding, or maybe there's a memory leak (I have a feeling it might be a Pandas memory leak rather than BFLW/Flumine memory leak), but if I'd bought 64GB my life would be easier.

---

## 2021-09-06 08:18:53 - general channel

**Jono**

yes ive seen previously on here that you have to mindful of requests as to not interfere with the actual flumine event loop. Assuming the blocking I/O request works as intended the last thing to clarify before pushing forward with this idea is: Is a pandas df an appropriate object to set up add rows to inside market.context eg market.context['bet_df'] ? I know you arent a flumine user so may not be able to give me a definite answer on this one so its no problem if i have to go trial this one myself

---

## 2021-09-06 07:53:43 - general channel

**Jono**

Hey everyone, before using flumine in an older strategy i used to send a pandas dataframe of orders placed along with the ladder information at the time the bet was placed to a database api for cataloging. I would quite like to do this again specifically in a given flumine strategy iteration when a market order is placed make a note of the runner info (available to back/lay etc) for that given market_book and then send it back to my database api every 30 seconds or so. I was wondering the best way to go about this without using messy global variables. After reading up in the flumine docs my current plan is to store a pandas df in the market.context and access it in a background worker, then loop through "for market in flumine.markets:" appending each of the dfs to get all the orders and runner information in one large frame before sending it off to the db. Not had much experience with utilising the market[context] to store information between iterations so wondering if this sound like a plausible way of using it or is there a better way of going about storing odds at time of placing before sending this info off to an external api? Thanks

---

## 2021-09-02 11:29:03 - general channel

**Ke**

To be precise, i'm looking for the matched price and matched size in last 5 seconds. As we are streaming data from betfair, we must have a timestamp for each matched order. I'd like to filter out the matched order based on the timestamp to calculate the moving average of the matched price.

---

## 2021-09-01 23:24:57 - general channel

**Michael**

Quick question on displaying data, in flumine for backtesting you use the market filter and pass in your files. How can I display that data say in a dataframe, given its in .bz2 format, can I use flumine or some other library?

---

## 2021-08-31 12:10:15 - general channel

**Steve Roach**

Yeah, converting to a dataframe should be quite easy once I've got the basics in place - my problem is understanding the basics. I think my best be is to just plough through the github/Flumine documentation and see what I can understand. After that, I need to get dirty with the code, and probably ask a lot of dump questions on slack.



But, thanks for you advice here - it helps a lot.

---

## 2021-08-31 07:08:03 - general channel

**Mo**

You seem to be missing something here. The market book is the fundamental collection of data that any strategy works off so of course flumine gives you access to that. I'm not a flumine user but a quick look at the examples shows that to write a strategy you overload functions like `check_market_book` and `process_market_book`. Everything revolves around it. The only reason you might want to convert it to a data frame is if you want to perform operations on it that are easier to do in pandas or more generally with the data in a tabular format

---

## 2021-08-31 01:00:15 - general channel

**Steve Roach**

Like this from Bet Angel. Not sure it would be practical to feed this in its entirety into a strategy every second or so, but certainly an extract of features from something like this.

---

## 2021-08-30 21:22:14 - strategies channel

**Michael**

Yeah - profit in one column signal values in the other.



My pandas skills are not great so I'm sure this could be done more elegantly but the overall is that you make a new dataframe by grouping the one you have, something like this:

```lower_bound = 0

upper_bound = 1

interval = 0.1

ys = ['profit', 'fm_profit']

feature = signal



groups = np.arange(lower_bound, upper_bound + interval, interval) 

labels = groups[:-1]



df_1 = df.loc[:, ys].groupby(pd.cut(df[feature], groups, labels=labels)).mean().reset_index()```

Then just plot the new dataframe however you want to:

```df_1.profit.plot.bar()

df_1.fm_profit.plot()```

I find myself always needing the same types of plots so I keep a set of pre-made plotting functions in a separate file to the notebook and just pull them in with something like:

```%run ./analysis_tools.ipynb```

---

## 2021-08-25 07:44:12 - random channel

**Peter**

Also, it's unlikely that there's "a modeller" who has access to the whole process. I suspect that there will be a team who manage a significant data pipeilne covering a wide spectrum of data, with all the standardisation and cleansing that goes with it. So the modeller may have insight into the features being used, but not how the data arrives to him (or her). Moreover, if there's deep neural network at the core of this, it may be a black box anyway (though in the ad earlier in this thread, there was clearly a need for solid domain knowledge).

---

## 2021-08-24 22:43:07 - strategies channel

**Steve Roach**

If the amount of time into a season is a feature, should it be incorporated into the ML model?

---

## 2021-08-23 09:52:45 - general channel

**Steve**

All good. It's just pulling the attributes of the order objects in the blotter into a dict, so pandas can convert it into a df.

---

## 2021-08-16 17:28:59 - strategies channel

**Mo**

Just personal stash. I find it helps to become very familiar with the really important papers, like Dixon and Coles, then you can more easily find stuff by looking up what references it (a feature of Google Scholar)

---

## 2021-08-09 19:37:13 - issues channel

**liam**

Have you uncompressed the file or are you using something smart_open to read? But like Aaron has said the basic data is useless and you won’t be able to use all of flumines features 

---

## 2021-08-09 16:21:52 - general channel

**Peter**

[@U02ABPZRT2N](@U02ABPZRT2N) I took the opposite approach. My PHP package is the goto in that community with more checkouts from github more than all the other PHP equivalents put together, but 2 years ago I concluded that it was worth learning Python just for betfairlightweight and Pandas. And then Flumine came along to confirm that I'd made the choice (at least for me).

---

## 2021-08-08 11:49:36 - strategies channel

**Dave**

&gt;  would be great to see the results if you created two models, your normal one, then one including these and just set the stakes to minimum.

hmm yeah, or even a model including friendlies _only_ if I can source some more historical data as there are very few samples currently, or bring in some league-invariant features from other leagues and let it loose on small stakes.

---

## 2021-08-08 11:08:23 - strategies channel

**Dave**

[@UBS7QANF3](@UBS7QANF3) - yup. I guess similar principles apply in tennis - I currently do not have much intuition on the usefullness of data from friendly matches, but they do seem to have some adverse effect on my models (at least given my current feature set).

---

## 2021-08-06 13:45:27 - strategies channel

**Dave**

It's difficult to generalise this I think. For example, in football you have new leagues starting every few weeks in all sorts of regions....I spend a fair bit of time maintaining models for so many leagues, investigating if a model is ready to be deployed for a recently started league etc. Per-league effort is probably quite small but it adds up, and then you need time for execution optimization, and r&amp;d into new features. Maybe racing markets are more stable in this regard (idk). This is coming from a truly fundamental approach.

---

## 2021-07-28 08:38:13 - general channel

**bb**

[@U01J98RDHRN](@U01J98RDHRN) Another good way of getting a bit of insight into what is going on in "black box" models calculating/looking at the SHAP values. It gives a bit more of a detailed view than looking at the feature importances.



This library is a pretty good start for getting up and running



[https://github.com/slundberg/shap](https://github.com/slundberg/shap)

---

## 2021-07-28 07:09:45 - general channel

**Adrian**

[@U01J98RDHRN](@U01J98RDHRN) i'm in a similar camp. i think the hardest part about any ML is figuring out what it's trying to tell you. Building the models, feature engineering and all that is the easy part

---

## 2021-07-27 22:26:56 - general channel

**Dave**

The "right" thing to do is to interpret your models of course and disect them, but unfortunately XGBoost doesn't make it easy. If you are keen on interpretable tree models, maybe look at Random Forest? Generally given the same set of features, a RF model and a XGB model will have similar predictive ability. It is quite easy to plot trees from RF though and visualize them with graphviz. Maybe it could be a good first step before moving onto xgb

---

## 2021-07-27 22:10:58 - general channel

**Dave**

I have generally accepted that if you have, say, more than 10 features then you might as well consider your XGBoost model a black box and it becomes quite difficult to interpret. I'd lump it in with neural nets with multiple hidden layers etc. Idk if anyone else here spends time interpreting their trees but IMO if it does well out of sample and you've been clean with your modelling approach then you are probably good to go. With that being said, the sklearn api for XGBoost exposes "feature importances" - I'd definitely analyse these and ensure they somewhat make sense.

---

## 2021-07-27 13:26:39 - general channel

**Oliver Varney**

Can pandas do this? or do you need it accessible by other processes?

---

## 2021-07-22 09:51:49 - general channel

**RDr**

Hi, I am only getting started using betfairlightweight with python and looking for any existing link / shared codes about how to export all info from sample bz2 historical PRO data files into dataframes and csv files. The idea is more to get familiar with the data content (eg, visualise via excel or SQL) before deciding what transformations I need. Would anyone please give me some pointers? Thanks

---

## 2021-07-22 08:34:24 - strategies channel

**Oliver Varney**

yes train/test performance diverges fairly quickly in my experience, but thats most likely due to features not being predictive enough. That will apply to pritty much all optimisations though I would of thought.

---

## 2021-07-11 14:02:50 - strategies channel

**Unknown**

For this kind of thing where you have interactions between features that don't necessarily have a totally linear relationship, you may also want tree-based models such as Random Forests (ancient) or XGBoost (the usually better replacement).

---

## 2021-07-01 18:34:58 - random channel

**river_shah**

nice things like:

```$ poetry show --tree

requests-toolbelt 0.8.0 A utility belt for advanced users...

└── requests &lt;3.0.0,&gt;=2.0.1

    ├── certifi &gt;=2017.4.17

    ├── chardet &gt;=3.0.2,&lt;3.1.0

    ├── idna &gt;=2.5,&lt;2.7

    └── urllib3 &lt;1.23,&gt;=1.21.1



$ poetry show --latest

pendulum 2.0.4   1.4.5 Python datetimes made easy.

django   1.11.11 2.0.3 A high-level Python Web framework ...

requests 2.18.4  2.18.4 Python HTTP for Humans.```

My stack nearly got into some operational trouble due to dependency confusion..poetry just helps tighten the package supply side of things. it is not much of a cognitive overload if you just want to replicate pip behaviour and wait for more advanced feature usage

---

## 2021-06-28 10:36:25 - strategies channel

**Andrew**

With respect, you are then unlikely to find anything. My approach is to start with a theory. You then test that theory. Others may follow similar approach. For example: “Faster dogs win races. I believe there would be a weight to box relationship, and heavier dogs have an advantage if mid starters”. [I’m not suggesting this is a valid theory, but you see I now would have something to test]. Next step, ask what data you need to collect - timeframe, tracks, starter numbers, sample size. Go and collect a rich dataset then test you theory. And along the way you’ll use pandas :wink:

---

## 2021-06-27 22:31:01 - strategies channel

**AndyL**

Im not giving up on pandas, just putting in tool box til i know what to feed it...

---

## 2021-06-27 22:14:08 - strategies channel

**D C**

I don't understand you [@U01PJ5YMFBJ](@U01PJ5YMFBJ) - it does not matter whether you use python, pandas, R etc - linear regression is linear regression. You've invested the time learning to use pandas what possible benefit is there switching now? Regression results will be shit if your explanatory variables are not right. Not everything has a linear relationship and not all response variables are well suited to linear regression.

---

## 2021-06-27 21:51:59 - strategies channel

**AndyL**

Not convinced pandas is going to help me at the moment, sorry [@UBS7QANF3](@UBS7QANF3) im going to flit back again!

---

## 2021-06-27 21:46:03 - strategies channel

**AndyL**

Just done an interesting pandas regression, i added BSP as the Y, and a load of variables, a straight linear regression had an accuracy of 0 ! Hence no correlation at any time with my input variables ?!?

---

## 2021-06-27 19:51:00 - strategies channel

**Mo**

Absolutely nothing wrong with learning pandas, it's a great move that has applications far beyond sports betting

---

## 2021-06-27 19:49:57 - strategies channel

**AndyL**

No [@UBS7QANF3](@UBS7QANF3) i deserved it, i dont always realise when I say the wrong things, or go on too much.. Typical IT guy slightly on spectrum thing..

Thing is i dont realise i am flitting... pandas is just progression to me

---

## 2021-06-27 16:15:28 - strategies channel

**AndyL**

Anyway worked out pandas, so that's progress...

---

## 2021-06-26 22:15:15 - strategies channel

**AndyL**

Anyone using pandas, did you have to build Python3 from source to resolve pandas dependency on _bz2 ?

---

## 2021-06-26 11:47:40 - general channel

**birchy**

Question for the stats guys here...

So I want to build a preplay model in order to create my own prices/book using historical data for each runner. Let's say I have calculated a handful of feature probabilities for each runner and have also manually given those features a weighting. For example, one of the features may be the bookie price, to which I might give a weighting of 0.20.

I'm assuming that all of the features for each runner would somehow need to be combined to create a single probability, then the probability for each runner would need to be normalised to create a 100% book.

So my question is... in layman's terms, what's the best way to combine all of this independent data to create a final probability for each runner?

---

## 2021-06-26 03:02:27 - strategies channel

**Andrew**

And stop this “pandas model” talk. Pandas is just data structure. It’s Pythons implementation of a dataframe.  But I may be wrong that as I don’t use Python

---

## 2021-06-25 19:13:29 - strategies channel

**AndyL**

Say you come up with a pandas model that predicts a fair value at time 'now' based on a set of historical values. Which way would people play it...if the actual price now is "out" say 5% higher then that value so back.. or would you set an offer target say 8% out from now fair value with fillnkill say 10seconds...? The assumption being in 10seconds fair value won't change too much, so 8% will most likely be +EV

---

## 2021-06-25 18:55:40 - strategies channel

**AndyL**

Im now trying to muster some energy to do some pandas, just not convinced i understand how to find value in a market to really make use of it

I keep hearing snippets of you guys throwing 100s of offers at a market, and that's what my 10s fill or kill was sort of doing, didn't seem to work for the dogs!

---

## 2021-06-25 11:18:57 - strategies channel

**Peter**

[@U0155J92A7Q](@U0155J92A7Q) You can't strictly make the assumption that they're independent, since the act of placing the first bet impacts the market for the 2nd. And backtesting won't have taken this into account. That said, unless your bets are big relative to the market, I'd do it any way. A number of people here run Monte Carlo simulations to understand the range of potential outcomes, even wen they're clearly +EV. I load the data into a Pandas dataframe and draw tens of thousands of samples and although that is computationally intensive, it really doesn't take very long to run (a minute or two).

---

## 2021-06-22 12:03:37 - strategies channel

**Peter**

[@U01MPC0GUK1](@U01MPC0GUK1) No need for a new id, just use the timestamp. Shouldn't need to get all the runners on one line either, just group by timestamp and then run the analysis for that point in time against each group. This is one of the ways that Pandas scores over a spreadsheet.

---

## 2021-06-22 10:11:53 - strategies channel

**Beeblebrox**

I suppose you could do it in pandas if each line at a certain timestamp was tagged with an id and then you could group by those ids to get all runners in one line.  I'm no expert in pandas though - need to read up more about it.

---

## 2021-06-22 10:02:35 - strategies channel

**Michael**

I need to qualify the above by saying that it's only part of the process, ultimately I do re-price the whole market and I don't think you can do that with line data in Pandas. I use Pandas for what you might call 'signal discovery' as well as for analysing my actual betting. For the former I do a line for each runner at each interval with a 0 or 1 for the win and then pretend that they're all independent for the purposes of the exercise. Obviously that's wrong but it's adequate for the job I need to do. I then take that learning and look for a way to incorporate it into my pricing model.

---

## 2021-06-22 08:44:16 - strategies channel

**AndyL**

It does make me think if there's a few 100 of you on here running pandas models, i wonder how similar each is..? Do we end up fighting thresholds, you put orders in at +6.4%, Liam at +5.8%, Peter at +4.8% gets in first.....! (Just made those up!) ?

---

## 2021-06-21 22:07:23 - strategies channel

**AndyL**

So ive done sone reading about pandas, linear regression and stuff, and now what youre saying [@U9JHLMZB4](@U9JHLMZB4) [@U4H19D1D2](@U4H19D1D2) [@UGV299K6H](@UGV299K6H) makes great sense, a bit of an eye opener actually!

So it all sounds too simple though in an odd sort of way, dump a selection of market files with what you see as useful derived values into a csv, load into pandas, LinearRegression using sklearn, hey presto you have an equation to predicate an outcome say "fair value" from market values. Obviously a lot of variables there, choice of derived variables, timeframes,.....potentially a huge number, needing a decent computer to crunch! But I didn't think it could come down to just computing an equation...?

Sounds great though, i will make some baby steps maybe with 1 variable just to understand the framework...

Cheers

---

## 2021-06-21 11:47:10 - strategies channel

**Michael**

In terms of workflow I also do all analysis in jupyter notebook using Pandas. What I actually do is process every market file into an equivalent compressed csv which includes all derived variables. Then I extract the subset of data points that I'm interested in from each market file into another CSV and load that up into my notebook.  So maybe I want 1/5th of all instances where 1.5 &lt; best available back price &lt; 2 or whatever. That way I don't have to re-process all my markets every time I want a different data set, just relatively quickly extract what I need. I do both the initial processing and the extraction using multiprocessing and when I get frustrated by slowness I buy a new computer.

---

## 2021-06-21 11:28:14 - strategies channel

**Peter**

1) Pandas is very good at handling huge amounts of data. But a single market file also contains a huge amount of data, so if I'm developing a strategy with a year's worth of GB greyhound data, that's 40,000 x huge = overwhelming. So I work initially in Pandas with data from representative points in time from the start, just to make the process manageable.

---

## 2021-06-20 22:25:10 - strategies channel

**AndyL**

[@U9JHLMZB4](@U9JHLMZB4) thank you for the very concise answer, makes sense except for one query, you indicate at the end backtesting  ... and running against a large  number of market files... This sort of implies by the way you say that a pandas db does not have a large amount of data. Im was sort of thinking create a strategy to pump the market data files all into DB/panda, but thinking you're implying something more subtle?

Thanks

---

## 2021-06-20 21:43:32 - strategies channel

**Peter**

[@U01PJ5YMFBJ](@U01PJ5YMFBJ) Completely agree with [@U4H19D1D2](@U4H19D1D2) re: Pandas. It's like a cross between a spreadsheet on steroids and a database without all the overhead, but with the added benefit of transparently supporting parallel processing across however many CPU (or GPU) cores are available to it. If you've not used it before, investing some time there would dramatically speed up your analyses, making it easy to load and analyse data and then keep tweaking your parameters as you home in on finding value. Backtesting general revolves around a strategy about which you already have some confidence and running it against a large number of market files - a much slower process.

---

## 2021-06-20 20:31:19 - strategies channel

**liam**

The proper way, take your pick on tools but pandas is the go to when it comes to data analysis / ML. Backtesting is more valuable when it comes to confirming your analysis whilst getting a rough idea on matching / real pnl 

---

## 2021-06-19 09:07:05 - strategies channel

**Jonjonjon**

You could start by plotting your profit Vs book. Do that for a few features. And then ML will be useful for combing a few of those features together. If you understand the individual relationships first, it can help you fit the model more successfully.

---

## 2021-06-19 08:20:07 - strategies channel

**birchy**

I really must get my ass into gear and look at this ML malarkey. While my `if book &gt; x and ltp &lt; y...`  type triggers do generate some profits, it's not really a "model" per se. My notepad is rammed with ideas for potential features similar to the kind of thing [@U9JHLMZB4](@U9JHLMZB4) mentions above. So my question is...where would a layman start with ML, given that they are familiar with Python but a complete luddite regarding statistics, ML, NN, etc? I've looked at some tutorials online, but they all seem to assume that the reader already uses sklearn/pandas/etc...which I don't. YET.

---

## 2021-06-19 07:00:38 - strategies channel

**Peter**

[@U01PJ5YMFBJ](@U01PJ5YMFBJ) As an example, ML can be useful for detecting systemic bias in the crowd. So if the question being asked was "are soccer teams with large followings overbet?" you might use ML to build a model with fundamental features such as differences in home attendance, ground size, number of twitter followers, size of supporters club, shirt sales between two opponents. Or if you were wondering whether favourites or longshots are overbet / underbet in certain types of race, you could build a model using technical price data from the type of markets that you suspect could be prone to this.

---

## 2021-06-18 20:33:50 - strategies channel

**Dave**

Nah, football. For my forecasting target and features, anything over 4-6 months has never added additional predictability. 4 months gives me 20-30,000 samples too which is sufficient to obtain good OOS performance. I put it down to change in dynamics as a competition progresses through its stages tbh. Im sure there are people for whom 10 years of data in football is useful tho, but their features must be way diff to mine 

---

## 2021-06-16 19:06:09 - strategies channel

**Dave**

Individual team performance has rather high variance, probably better to cluster teams first maybe and then use those clusters as features

---

## 2021-06-16 17:01:38 - strategies channel

**Unknown**

basically you can predefine the models you want to try. mlp, xgboost, and most of sci kit learns one. in the preprocessing you can try various ways to make it less sparse. group features etc. but as it often uses one hot encoding it is not very good if you have &gt;1000 teams...

---

## 2021-06-16 16:54:24 - strategies channel

**Frankz**

Next question. How would create an embedding of the teams players? I have worked with creating embedding of text features quite often. there we have word2vec and doc2vec but in this case the order of the players doesn't matter too much.... but here I'm not to sure, I have looked at the paper playerank

---

## 2021-06-11 10:40:44 - general channel

**Mo**

Generating a data frame from the prices files is simple though:



```from typing import Union



import betfairlightweight

import pandas as pd

import seaborn as sns

import smart_open

from betfairlightweight.resources.bettingresources import MarketBook

from betfairlightweight.streaming import StreamListener

from unittest.mock import patch





def market_book_to_data_frame(market_book: Union[MarketBook, dict]) -&gt; pd.DataFrame:

    if type(market_book) is MarketBook:

        market_book = market_book._data



    return pd.DataFrame(

        {

            'market_id': market_book['marketId'],

            'inplay': market_book['inplay'],

            'selection_id': runner['selectionId'],

            'side': side,

            'depth': depth,

            'price': price_size['price'],

            'size': price_size['size'],

            **({'publish_time': market_book['publishTime']} if 'publishTime' in market_book else {})

        }

        for runner in market_book['runners']

        for side in ['Back', 'Lay']

        for depth, price_size in enumerate(runner.get('ex', {}).get(f'availableTo{side}', []))

    )





def file_to_data_frame(path_to_betfair_price_file: str) -&gt; pd.DataFrame:

    trading = betfairlightweight.APIClient(username='', password='', app_key='')

    stream = trading.streaming.create_historical_generator_stream(

        directory=path_to_betfair_price_file,

        listener=StreamListener(max_latency=None, lightweight=True)

    )



    with patch("builtins.open", smart_open.open):

        g = stream.get_generator()

        return pd.concat(market_book_to_data_frame(mbs[0]) for mbs in g())```

---

## 2021-06-11 05:37:27 - general channel

**VT**

Hi, I've been researching how I can get Betfair historical data to backtest, any tips on a good tutorial for beginners in Python? I would like to consult the live football game moneyline markets. I intend to consult the free Basic data, 1 minute intervals, I would like to convert the odds values ​​in each minute to a dataframe.

---

## 2021-06-04 08:46:19 - general channel

**John**

Hi [@UBS7QANF3](@UBS7QANF3), just found this useful function converting market_book to a dataframe. The Union type is quite beyond my Python level, and googling "Python Union type" doesn't help me really. I wonder if you can please give me a pointer how to make it work? Do I need to import a library for this Union type?

---

## 2021-05-14 17:47:53 - strategies channel

**Oliver Varney**

I do find the questions on what features are good in a group of nearly 1000 people who are your competitors a tad strange :face_with_raised_eyebrow:

---

## 2021-05-14 15:08:26 - general channel

**MacrcoPolo**

Yeah, still that fits happily in memory and will load in a few secs into pandas

---

## 2021-05-14 10:33:02 - strategies channel

**PeterLe**

Yes thats what has threw me to be fair. Ive tried to smooth the data out by using moving averages etc it helped but slowed things down too much

If I could strip out the outliers that would make sense.

---

## 2021-05-11 09:29:26 - strategies channel

**Peter C**

Really enjoyed a lot of the recent conversation - it kind of inspired me to have a go at modelling pre-off horse racing using market info. My model is trash, but it's been a good learning experience so far. I've been reading back through this slack and wanted to ask about using price data to fit a market.



I'm not quite sure what my thinking is - I have a few thoughts but I'm not sure. I have thought that maybe the win market is largely efficient - and therefore I could use price data to model a projected sp that I could then take to eg the place market.

I've also thought that perhaps I could use features that aren't derived from the current market price to fit my model - eg the sp far price, and then 'return' to the market (the current price) to amalgamate information a la Will Benter.

I've also thought that maybe I should include features that are derived from the current runner price to fit my model, with the intent of coming up with a projected sp interval that I could use to place bets when I see an edge - but I'm not sure how feasible this is given my assumption that the pre-off win market is largely efficient - I'm also not sure it makes sense to take the current price and +/- a bit to come up with an sp.



Not necessarily looking for specific answers to my questions but I would be interested in people's ethos surrounding this or perhaps someone is able to point me to some resources where I can learn more? I feel like I am missing a huge chunk of understanding on this topic. (I'm reluctant to go straight to google with 'price action' because I suspect there's a lot of bullshit out there; I've read the majority 'efficiency of horse track betting markets').

 [@UBS7QANF3](@UBS7QANF3) the other day you used the example of using bsp to come up with an implied distribution of runner's speeds for inplay betting. I understand this example but am not sure how this would be achieved within a single market - I need to think about it further, maybe this is the understanding I'm missing

---

## 2021-05-11 02:25:35 - issues channel

**Greg**

Hi all. Having a go (be gentle -have only been studying Python for 3 months-so here come the very dumb questions:laughing:) at logging in with the delayed key/Flumine. Managed to login  run the example strategy (using AU markets-[https://liampauling.github.io/flumine/](https://liampauling.github.io/flumine/)) I have set paper trading to True but that, changing the price entry (see LimitOrder below) point, changing _runner.last_price_traded &lt; 10_ and setting the filter to AU instead of GB are about the only changes I have made. Unfortunately I get not output at all-or errors. 'Couple of questions to kick off with : *1*.I have seen references on this channel to the delayed key (despite mine being created after April 8th 2020 so should have access to streaming )being utterly useless and I wondered if this is the problem? i.e.: is the delayed key pointless and does it effectively prevent anything from working? *2*. Does Flumine (being a fully featured/ backtesting platform) effectively supersede BFLW (I know BFLW is a dependency for Flumine) ? *3*. The example strategy has an (LAY) order parameter of _order_type=LimitOrder(price=1.01,size=2.00)_ I tried to change the price to &lt;10 for example but get an error. How do you set a price range for multiple runners in Flumine using limit orders? Thanks in advance.Apologies for the basic questions and I'll try limit them as I go. Cheers

---

## 2021-05-08 16:17:03 - general channel

**Mo**

In January, Betfair ran a survey which included a question on preferred potential API features. One of these was a bet queue indicator: [https://www.surveymonkey.co.uk/r/YW3RFGJ](https://www.surveymonkey.co.uk/r/YW3RFGJ)

---

## 2021-05-03 05:41:35 - general channel

**onthepunt**

What is the best way to not display horses in the 'runners_df' dataframe whose 'status' = 'REMOVED' using the code from [212] and [213] on [https://betfair-datascientists.github.io/api/apiPythontutorial/](https://betfair-datascientists.github.io/api/apiPythontutorial/)?

---

## 2021-05-01 12:43:07 - general channel

**liam**

[@UBS7QANF3](@UBS7QANF3) shared something in pandas recently 

---

## 2021-04-15 15:48:53 - strategies channel

**James T**

If your strategy is based on stats or analytics on data of a fixed period, like calculating a moving average or something, then that does require a little rethinking since streaming data arrives at irregular intervals. 

---

## 2021-04-07 12:03:18 - general channel

**Newbie99**

[@U4H19D1D2](@U4H19D1D2), I was just trying to play around with that new linked events feature, but am being a bit dense, how do I format for live streaming?



Lets say this is the streaming filter, its not a dict, so where does the event processing key go?



```market_filter=streaming_market_filter(

                event_type_ids=[7'],

                country_codes=['GB'],

                market_types=['WIN','PLACE', 'EACH_WAY']

            )```



---

## 2021-04-05 09:33:32 - general channel

**RicHep**

amateur question here, once I start streaming the raw data from betfair, is there an easy way to get it into a dataframe including the usual fields you'd expect, market_book.market_id,

        market_book.inplay,

        market_book.status,

        market_book.total_matched,

        runner.selection_id,

        runner.status,

        runner.last_price_traded,

        runner.total_matched,

        runner.ex.available_to_back[0].price,

        runner.ex.available_to_back[0].size,using flumine?

---

## 2021-04-01 18:47:49 - general channel

**Oliver Varney**

[@UQL0QDEKA](@UQL0QDEKA) its just that I use AI models, when features are empty / havent been seen im unsure whether the outcome will be great or not

---

## 2021-03-31 08:51:48 - random channel

**Dave**

My models just 0 out signals when features are detected to be rubbish or market volume is too low for when the data for features was collected

---

## 2021-03-31 08:41:13 - random channel

**Oliver Varney**

Just out of interest, anyone using models,  when the exchange is down for an extended period and some features are impacted as a result, do people continue as normal or sit on the bench

---

## 2021-03-19 12:30:12 - random channel

**Dave**

Used plotly for maps before. Pandas has decent styling options for rendering tables using HTML (and am sure the output can easily be converted to PDF/PNG etc)

---

## 2021-03-17 08:06:33 - strategies channel

**Jorge**

Is it possible to run flumine just as a "market recorder", with all the other features turned off? (for ex. turning off OrderStreaming)

---

## 2021-03-16 12:11:46 - strategies channel

**birchy**

So BFLW was [@U4H19D1D2](@U4H19D1D2)'s first generous offering and is the lower level implementation of the betfair API. Flumine takes bflw and adds lots of features (including backtesting capability) for "real world" applications. If you're just starting out, Flumine is definitely the way to go.

---

## 2021-03-15 09:10:52 - general channel

**Mo**

BFLW is a lower level implementation of the Betfair API in Python. Flumine sits on top of this and aims to be a fully featured trading platform

---

## 2021-03-02 10:02:44 - strategies channel

**Unknown**

Morning all, just to outline the details. Have a system that looks to suggest Ranks to either Back or Lay. Rank is the order of favouritism as determined by BSP. My monetary results are based up correct Rank being selected and a £25 Back bet or £25 Lay bet achieved at BSP. £25 was chosen when I set up my database as a figure that should be able to be matched around the off time. In reality this may not always be the case but this way I have a consistent approach. I am not at the implementation stage yet. Other caveats, I do not consider the odds when Laying. In reality I would not be placing £25 on 1000 BSP even though this might show up as a win in the results however having some visibility on the impact when a high odds Lay goes on to win I`m hoping will give some pointers on frequency and risk reward at the implementation stage. I have shown visibility on Ranks 11 &amp; 12 although they do not feature in the daily total so I can compare the rate of progress to other systems on test. This is what I believe to be the results for Mon assuming my sums/data is correct. To clarify, getting matched on the correct Rank is more important than any odds changes to the BSP value when getting matched. As a measure of success or failure I count the No of suggestions then the No that have a value &gt;£0.00. New system so thus far Count = 79, CountIF &gt;£0 = 60. I`m hoping that posting here will turn into a bit of a peer review.

---

## 2021-02-23 09:45:01 - general channel

**river_shah**

do you have any example how I can grab a pandas df or csv out of this please?

---

## 2021-02-22 08:59:10 - general channel

**Michael**

[@U016TGY3676](@U016TGY3676) is right except that it's probably easier in the short run too. I'd suggest you learn a bit of python and read up on Pandas. You can do a lot of analysis really easily with Pandas in Jupyter notebook and there's tonnes of tutorials available.

---

## 2021-02-04 13:46:17 - general channel

**Mo**

```def market_book_to_data_frame(market_book: Union[MarketBook, dict]) -&gt; pd.DataFrame:

    if type(market_book) is MarketBook:

        market_book = market_book._data



    return pd.DataFrame(

        {

            'market_id': market_book['marketId'],

            'inplay': market_book['inplay'],

            'selection_id': runner['selectionId'],

            'side': side,

            'depth': depth,

            'price': price_size['price'],

            'size': price_size['size'],

            **({'publish_time': market_book['publishTime']} if 'publishTime' in market_book else {})

        }

        for runner in market_book['runners']

        for side in ['Back', 'Lay']

        for depth, price_size in enumerate(runner.get('ex', {}).get(f'availableTo{side}', []))

    )





def file_to_data_frame(path_to_betfair_price_file: str) -&gt; pd.DataFrame:

    trading = betfairlightweight.APIClient(username='', password='', app_key='')

    stream = trading.streaming.create_historical_generator_stream(

        directory=path_to_betfair_price_file,

        listener=StreamListener(max_latency=None, lightweight=True)

    )



    with patch("builtins.open", smart_open.open):

        g = stream.get_generator()

        return pd.concat(market_book_to_data_frame(mbs[0]) for mbs in g())```

---

## 2021-01-28 17:01:41 - strategies channel

**Oliver Varney**

can you not just load to python /pandas and call sample/shuffle ?

---

## 2021-01-24 16:50:23 - general channel

**river_shah**

bflw handles all the critical features for market and order streams and all other helper functions to communicate with betfair servers for market catalogues, runner meta data. flumine, builds on top of this core to provide a feature rich strategy design, backtesting and productionizing framework.

---

## 2021-01-15 12:11:58 - general channel

**Mo**

pandas resampling can help

---

## 2021-01-10 20:19:47 - strategies channel

**Michael**

[@U4H19D1D2](@U4H19D1D2) In this case maybe but you're still just kicking the can down the road. What are you going to do when you find another feature? Start a model C and run that too? Just in the general case I don't like to approach. You can make it better by having some structure like a perpetual AvB with a 'winner stays on' structure or something like that but you can see the potential for muddying the waters if you don't. I suppose it is a question of style and how you manage your development though.

---

## 2021-01-10 19:34:46 - strategies channel

**Michael**

Personally I'm not keen on [@U4H19D1D2](@U4H19D1D2)'s approach to this problem for a few reasons, one of which is that you can easily end up with a proliferation of poorly optimised models that might be interacting in all kinds of ways that you'll never know about. I prefer to try to understand the features I'm using as deeply as possible and integrate them into a single unified model wherever possible.

---

## 2021-01-10 18:56:36 - strategies channel

**Dave**

Yeah the fact that the model is simpler is what makes it quite attractive over the other. I should stop being lazy and do some tests on the features themselves like you say!

---

## 2021-01-10 18:48:39 - strategies channel

**Michael**

Would opting for the model with fewer features allow you to analyse the remaining features against the bets? If I were struggling to make up my mind I'd generally plump for the simpler model. 3000 markets with bets in them backing at &lt; 2 seems like quite a lot to me.

---

## 2021-01-10 16:04:25 - strategies channel

**Dave**

Modelling question: I have a model, A, that by standard statistical tests performs better than model B (higher ROC, better precision/recall etc). However, on backtest, model B results in higher Sharpe and more total pnl. How would one choose which model to use? My theory is that model A is just better at forecasting situations that are already easy for the market to forecast too, and therefore unlikely to find opportunities where the market gets this wrong (hence an opportunity to take a position in the market). Note: Model B is just fit on a subset of features.

---

## 2021-01-06 08:17:27 - random channel

**bb**

[@U01J98RDHRN](@U01J98RDHRN) This is a great talk about how pandas works behind the scenes which should help to explain the indexing issue you were facing and get better understanding of it all



[https://www.youtube.com/watch?v=CowlcrtSyME](https://www.youtube.com/watch?v=CowlcrtSyME)

---

## 2021-01-05 22:28:04 - random channel

**Sam Asin**

[https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas](https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas)

---

## 2021-01-05 22:23:34 - random channel

**Sam Asin**

hoooooooooooooooolllllllllllllllllllllllllyyyyyyyyyy crap. I realize this isn't the place for python tech support, but since there are a lot of python/pandas/data people  here

---

## 2021-01-02 15:43:06 - strategies channel

**Mo**

It's not a documented feature but you can pretty easily work out how to use the website endpoint

---

## 2021-01-01 17:45:20 - random channel

**Sam Asin**

and anyways, we're all using pandas with thsi package so it's sort of moot.

---

## 2021-01-01 10:36:21 - random channel

**Alessio**

And as we always say, as long as the tools are comparable in power, whether you use pandas or R it's more your problem and the community you cater to.

---

## 2021-01-01 08:45:54 - random channel

**Mo**

Like you say, it's what you're used to, but I prefer the pipeline syntax of pandas to remembering what operations go in which position inside the square brackets

---

## 2020-12-31 23:53:35 - random channel

**Sam Asin**

[@U01C12ZEADQ](@U01C12ZEADQ) sorry i passed out it was like 4:30 am my time and I stayed up too late playing FTL. Yeah, data.table is pretty much it's own thing so it's borderline unrelated. That said, i had done some base R before, and hadn't had any problems with gotchas or anything. There are often more examples online for pandas, though.



For data.table, at least, I feel like its less verbose but that hasn't come with gotchas to me. Sometimes I just have to learn weird little tricks that are in there to help do what I want, but ultimately it's always doing what it seems like it should. I will def stan for it and think it's genius, but I'm no real programmer.



The basic gist is, compared to pandas, it generally assumes you're working inside the scope of the data.frame you're dealing with, and is really into powerful group bys with whatever statement. Everything is always df[subset stuff, stuff to do, group by stuff] and you can accomplish a ton with it.



So now, in pandas, I find myself writing:



newdf= df_name[['colname_tosum']].groupby(df_name['colname1'], df_name['colname2']).loc[df_name['colname3'] &gt; 4].sum()



or something like that, where in data.table in R it would be.



newdf = df_name[colname3 &gt; 4 , sum(colname_tosum), groupby = list(colname1, colname2)]



or just (the groupby is optional):



newdf = df_name[colname3 &gt; 4 , sum(colname_tosum),  list(colname1, colname2)]



or could just calculate that new column in the same data.frame:



df_name[colname3 &gt; 4 , newcol := sum(colname_tosum), list(colname1, colname2)]



it's probably a bit of what you're used to, and in this case the pandas line isn't that long, but it takes me forever to read that pandas line and figure out what's going on. On the other hand, I think if you are practiced in pandas, you don't default to group by etc. so much to solve your problems the way I do. Also, you might use way shorter df_names, i'm in the habit of writing long descriptive names because i usually in data.table write 'em just once per line. Anyhoo, that's my shpeal.

---

## 2020-12-31 17:44:20 - general channel

**Graham**

I've got the following code for unpacking the historic price history (Basic) and exporting to csv. I'm really hitting a blank trying to pair the "id" with horse "name" if someone wanted to give me a nudge.

```import pandas as pd

import json

from bz2 import BZ2File



file_name = "30095040.bz2"



with BZ2File(file_name, "r") as f:

    lines = f.readlines()



price_changes = []



for line in lines:

    content = json.loads(line)

    market_changes = content.get("mc", [])

    for market_change in market_changes:

        market_id = market_change.get("id")

        market_definition = market_change.get("marketDefinition")



        runner_changes = market_change.get("rc")

        if runner_changes:

            for runner_change in runner_changes:

                print(runner_change)

                price_changes.append([content.get("pt"), runner_change.get("id"), runner_change.get("ltp")])



df = pd.DataFrame(price_changes, columns=["timestamp", "selection_id", "price"])

df.to_csv("prices.csv", index=False)```

---

## 2020-12-31 14:25:20 - issues channel

**MacrcoPolo**

What I love about folk who want to do datascience is that they're generally obsessed with complex models and hitting the .fit() method on tensor flow, when actually spending time making sure your data is clean and working on sensible features is 95%+ of the job...

---

## 2020-12-31 10:19:44 - random channel

**Alessio**

Pandas is more verbose, but indeed the verboseness gives you a better understanding of what to expect.

---

## 2020-12-31 10:14:46 - random channel

**Sam Asin**

I think pandas is a lot more verbose [@U01C12ZEADQ](@U01C12ZEADQ), but also i'm used to thinking in R ways.

---

## 2020-12-31 08:03:46 - random channel

**Oliver Varney**

Cant remember exactly what the standard version has vs it but it has stuff like viewing pandas data frames , coverage for testing, threading debugging and performance stuff. Maybe not worth it for a developer of my skill but yes, the debugging tools are much better. Im surprised you dont have it. I think its only a few quid a month. They have monthly rolling options so id recommend trying it for a month and then binning it if you dont think its worth it

---

## 2020-12-30 12:22:20 - random channel

**Oliver Varney**

nope, only if, but in this case (and thinking generally) the combination of the strength of all my separate models (operating on slightly different features + times), plus the doubling of price, raises the question of how to evaluate these situations. All typical metrics suggest that pre off it was a bad bet. Probably just falls under the category of not worth the time looking into.

---

## 2020-12-29 09:58:14 - strategies channel

**Oliver Varney**

[@UBS7QANF3](@UBS7QANF3) so if you model trained on non virtual (with volume features), do you essentially have two market streams (virtual &amp; Non virtual)? If im understanding this correctly

---

## 2020-12-28 13:22:46 - general channel

**Mo**

My point is that building a model (classifier) by weighting different features has nothing to do with Bayes

---

## 2020-12-28 13:09:18 - general channel

**Mo**

It sounds like you want to use the indicator whether a horse is the most traded horse as a feature in a model and then add more features

---

## 2020-12-27 13:10:13 - strategies channel

**AP**

Ok that’s very cool, I’ve been outputting dataframes from the flumine backtests and working on those. But this seems a lot more in depth. 

---

## 2020-12-27 13:06:23 - strategies channel

**liam**

Yeah was going to add a dataframe which contains some stats such as profit/sharpe ratio/roi/match rate per strategy etc and then a series of graphs with text on what to look for etc.

---

## 2020-12-07 16:32:20 - random channel

**Oliver Varney**

typically access tables via pandas, and upsert using procs

---

## 2020-12-07 16:30:00 - random channel

**Oliver Varney**

yes essentially I use sql server as a long term datastore, with python services that request / add data, call further internal procs that populate tables and build out further features. Just wondered if there was something similar to unittest / pytest within sql server. Or is it a case of using python to pull data out then do the test cases that way

---

## 2020-12-07 13:15:17 - strategies channel

**Oliver Varney**

talking pre off [@U0160E9HS2G](@U0160E9HS2G) , if I was doing an inplay model I would likely capture a price very close to off and use it as a feature

---

## 2020-12-07 11:23:01 - general channel

**Cagdas Yetkin**

We have put together some leagues and we will be testing a few things on the go :slightly_smiling_face: Plus, we started writing a blog regarding our 30-day-betting challenge. We are already on day-9. It is going to be fun. Our friendly project is here: [http://betalertpro.com/](http://betalertpro.com/) no login required... There is a feature using the betfairlightweight but it is not active yet.



it is only in-play... So the matches will be visible today evening only.

---

## 2020-12-06 18:06:26 - strategies channel

**Oliver Varney**

yep now imagine think one of your features is the price the bookmaker produced the night before. if your model goal is to predict the winner with the most accuracy, surely it will pick the bookie odd that is the lowest ?

---

## 2020-12-06 18:03:43 - strategies channel

**Alessio**

It depends how you build the model, but you could have odds most_of_the_time and in certain cases other features could be overpowered. At least I'd expect decision-tree style models to be able to recognize that in certain situations you can refine the odds

---

## 2020-12-06 17:43:04 - strategies channel

**bb**

If the odds are far more predictive of the outcome variable than any other feature a model will weight them very heavily. At the extreme the model could just be a proxy for backing the favourite and accuracy/profitability will be in line with this

---

## 2020-12-06 17:20:06 - strategies channel

**Oliver Varney**

if you have a set of features that is prices from various sources + additional features,with each odds provider being slightly better in certain race types (or other splits), the model will learn this and should be better overall

---

## 2020-12-06 17:16:06 - strategies channel

**Oliver Varney**

i.e. if you creating a regression model to predict the value of your house, surely a good feature is the price the neighbours house sold at? Or even better the prediction from the estate agent?

---

## 2020-12-06 15:12:17 - strategies channel

**Alessio**

Random Q, did anybody try to reverse engineer some of the odds model that are around, i.e. try to figure out which are the features that mostly approximate the odds providers give you?

---

## 2020-12-06 09:13:15 - random channel

**Oliver Varney**

so I guess what I want to design or improve is a data quality / checking service. I run models that use data from many sources + I further aggregate and build out more features. also I would like to build some kind of unit test that tests the built out aggregate features in SQL Server. With a large number of sources + features it can be easy to let a inner join slip through the net instead of being a left join and it might not be fully noticeable straight away.

---

## 2020-12-04 21:52:53 - general channel

**Charlie 303**

So I have a coarse streaming filter which amounts to about 800 markets and I need runner metadata for each of these markets.  My first thought was to start with list_market_catalogue (using same coarse filter and RUNNER_METADATA projection) to build the index, then start the stream and apply updates matching the event ids.  However, I get the APING 'too much data' error on list_market_catalogue.  Applying a max_results=200 to the list_market_catalogue call seems to work, but it doesnt appear there's any pagination feature so I'm wondering how to get the remaining ~600 markets?

---

## 2020-12-03 19:43:51 - strategies channel

**birchy**

[@U4H19D1D2](@U4H19D1D2) great features, and will definitely start using them. Probably missing something here, but I presume the MarketRecorder won't pick up any bets I've got placed as it's a different strategy, so what's the recommended way to save data from a live bot?

---

## 2020-12-03 17:27:53 - strategies channel

**Dave**

It's useful for market making - if you're maintaining a spread then you can avoid getting swept where you anticipate the price to move sharply. Obvious and hypothetical example - if you have a realtime football feed you might want to cancel _fast_ whenever a player with the ball reaches a certain area of the pitch. I think it's just a feature you might want to take advantage of if your strategy suits (and use as protection), but not necessarily a source for inspiration.

---

## 2020-11-30 16:46:59 - general channel

**liam**

[https://forum.developer.betfair.com/forum/betfair-premium-newsletter/29456-premium-newsletter?p=33644#post33644|November Premium Newsletter](https://forum.developer.betfair.com/forum/betfair-premium-newsletter/29456-premium-newsletter?p=33644#post33644|November Premium Newsletter)



Looks like they stole our idea..



```Premium Webinar

Planning is underway within the Premium team to bring you a webinar in early 2021 to share exclusive insight into:

• Exchange Liquidity

• Developing Markets

• New and existing API features

• In-play feed suppliers

• Historical data sources

Further communication with date and time to be finalised. Look out for this coming soon.```

---

## 2020-11-23 21:00:29 - strategies channel

**Misha**

Introduction of a new feature, unless very carefully considered, will often make the modelling worse

---

## 2020-11-23 20:08:18 - strategies channel

**Misha**

I have seen a profitable model on Aussie Rules and Rugby League using basically one main feature. Of course, you have to identify that feature :wink:

---

## 2020-11-23 20:07:17 - strategies channel

**Misha**

For stats models, 90% of the profit comes from a few "features". Adding lots of features might fine tune a good model, and make it a great model, but if it isn't profitable just looking at a few variables, you aren't on the right track

---

## 2020-11-23 17:12:18 - strategies channel

**Dave**

But the original posts suggests that the two tasks (forecasting pricing and forecasting outcome) can be unified. But it's be unreasonable to use a model that's very good at predicting a price 5 ticks ahead that takes in order-book/trade features to forecast the outright outcome of event...

---

## 2020-11-20 21:44:01 - random channel

**Oliver Varney**

Yer might be able to devise something from there, could lead to a new feature for the model

---

## 2020-11-20 02:26:16 - general channel

**qwerty.nat**

one approach you could use is feed the raw data into bflw and modify it at X second intervals to dump each runners top Y levels of their order book (price and size ) then you can easily create an input for a machine learning system. this will nornalise the data somewhat to only information that is more relevant, then you can simply append data to this 'normalised' format with extra features you want to model on.

---

## 2020-11-17 22:22:18 - general channel

**Vincent Mele**

No, I'm trying to serialize historic streaming data at checkpoints (like 30 seconds to start time) and then store that snapshot in Postgres (as jsonb) for feature building and examination in the future at a lower resolution than streaming ticks.

---

## 2020-11-17 09:42:35 - strategies channel

**D C**

[@UBS7QANF3](@UBS7QANF3) is C++ an option for you? People who need very high performance code seem to have a huge hard-on for the newer features like move semantics ? Or does C++ not play well with Python?

---

## 2020-11-16 13:29:11 - issues channel

**liam**

what version of flumine? working fine on 1.14.8 (feature was added in 1.14.2)

---

## 2020-11-12 19:54:52 - strategies channel

**Josh**

Cython backs a lot of scientific/numerical python code (e.g. scikit-learn, pandas, etc) and is pretty easy if you're familiar with a bit of C/C++. You typically don't get a big boost unless you go through and tell the compiler the equivalent C type of variables; It's type inference is pretty weak. But for certain algorithms using the proper data structures, you can get orders of magnitude speed-up and if you're not dealing with actual python objects, you can explicitly release the GIL to get scalable cpu-bound multithreading. Numba is JIT compiles python to efficient machine code, but is primarily for numerical work, so not general purpose, for things like json parsing. As with anything, profile, profile, profile using any combination of cProfile, line_profiler, py-spy, austin, vmprof, etc to find out where the actual hot spots are in the code.

---

## 2020-11-11 17:16:31 - general channel

**Mo**

`pantab` package is great for building these extremely quickly from `pandas` DataFrames

---

## 2020-10-16 11:58:41 - random channel

**river_shah**

This is a very interesting feature / dependence. [https://betgps.com/betting-library/Gibson-etal-The-Best-Probability-Model-for-Exacta.pdf](https://betgps.com/betting-library/Gibson-etal-The-Best-Probability-Model-for-Exacta.pdf) must break pricing hard if one naively projected win probs to place

---

## 2020-10-16 09:35:38 - general channel

**Rob (NZ)**

```#Look at all NZ and Aussie Markets for the next day and bring back Market Descriptions

market_catalogue_filter = betfairlightweight.filters.market_filter(market_countries=['NZ','AU'],event_type_ids=['7'],market_start_time={ 'to': (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%dT%TZ") },market_type_codes = ['WIN'])



market_catalogues = trading.betting.list_market_catalogue( filter=market_catalogue_filter, max_results='100', market_projection = ['MARKET_DESCRIPTION','RUNNER_METADATA','MARKET_START_TIME'], sort='FIRST_TO_START' )



#Create a DataFrame for each market catalogue

market_types_markets = pd.DataFrame({ 'Market Name': [market_cat_object.market_name for market_cat_object in market_catalogues], 'Market ID': [market_cat_object.market_id for market_cat_object in market_catalogues], 'Start Time': [market_cat_object.market_start_time for market_cat_object in market_catalogues], })



market_types_markets```

outputs 100 rows but im just wondering if there is a way to get the total days racing

---

## 2020-10-15 13:26:53 - random channel

**agberk**

I put together a new desktop a few months ago; there was no way I was moving to Win10 so it was time to make the switch to Linux only for me. I came across Entroware and made an enquiry with them since I wanted a bit of customisation from the desktops they offered.



On their About Us page they literally say "No challenge is too big." I asked to use a different case and they wouldn't accommodate. They also didn't list the exact motherboard model (was considering doing some horrible GPU passthru for a Windows VM for gaming and mobos need supporting virtualisation features) and they wouldn't tell me what it was because I might mess around with it and void the warranty? I appreciate getting a laptop is slightly different but it still completely put me off them.



As an aside, gaming on Linux has been surprisingly painless. Lots of games run natively and most that don't run in Steam's Linux runtime or Proton (just an option to select in Steam). The only remaining annoyance is that most anti-cheat software doesn't run on Linux so you can't play certain online games without getting banned. I haven't tried it yet but my plan for those types of games (and anything which isn't compatible) is to go for one of these cloud gaming services like GeForce NOW.

---

## 2020-10-15 00:03:39 - general channel

**Charlie 303**

BF API n00b here; Getting thing started, I applied and received live app key. Then discovered searching through BF forums that you can increase market subscription limit (200-&gt;1000) by simply asking BF support, which is free of charge.  Didnt see any official documentation on that, but that indeed worked.  Curious if there are other features/limits that can be requested/applied for, either free or premium?

---

## 2020-10-14 12:49:19 - general channel

**river_shah**

is there much desire to integrate this into flumine? seems like a good safety feature with not much overhead.

---

## 2020-10-08 11:16:34 - issues channel

**Jorge**

Hi guys, do you know of any tool to monitor RAM usage by a Python process? I am wondering if it's the API calls what is using most of my RAM memory, or maybe it is that I am saving a row to pandas DataFrame every 10 secs with the state of the bot and I keep this dataframe in memory...

---

## 2020-10-07 21:32:23 - random channel

**Michael**

I'm going to expand on why 'closing' bets are inherently loss making because it illustrates a fundamental feature of profitable betting that is terribly important but isn't generally well understood and it might help some people.

---

## 2020-10-07 15:59:16 - random channel

**Michael**

I don't have a dog in the Flumine fight because I don't use it, but I can see why Liam doesn't want to institute a feature that is guaranteed to lose money and I just have a little demon in me that won't stand by when people say you can win without getting value.

---

## 2020-10-07 15:12:38 - random channel

**Dave**

I wrote a long thread on it on the betangel forums a while ago...that "auto offset bet" feature has probably helped make everyone money but the user :sweat_smile:

---

## 2020-10-06 20:36:47 - random channel

**liam**

[@UU1URJ8L8](@UU1URJ8L8) it’s great if you are using it for your own software but as soon as you make something open source you are very limited by the oldest version, it will be years until we can clear up type hints / use the new features in bflw :sob:

---

## 2020-09-27 19:48:28 - random channel

**Oliver Varney**

I thinks its secondary, you have a requirement first then if you need a feature that is suited to an in memory database /key-value store you use it.

---

## 2020-09-17 10:19:56 - general channel

**Jonjonjon**

Thanks for the offer, but I'm not a node guy. I will just knock something up myself using bflw and pandas. It won't take long.

---

## 2020-09-09 16:32:39 - general channel

**Jonjonjon**

At a later point I can download my orders, and use pandas to aggregate the results by customer_strategy_ref and market.

---

## 2020-09-06 12:47:28 - general channel

**Mo**

You’re going to have to share your code, it’s something to do with how you’re transforming the data using pandas, nothing to do with bflw itself

---

## 2020-09-06 12:46:05 - general channel

**ricky**

The error happened after steaming udpate, i read each items from process_runner_books(runner_book).

Log shows "pandas/core/series.py. line 871, __getitem result = self.index.get_value(self, key)"

Key Error:2

---

## 2020-08-21 18:52:02 - general channel

**john walsh**

Thank you for that.  When I run your code pandas does not automatically print out the dataframes and I have to print them.  When I do that with your code it does not produce the line "48 English Premier League 10932509" but the whole list as per yours after that entry.  I am using Python 3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)] and I have installed Pandas 1.0.5

---

## 2020-08-21 17:33:32 - general channel

**Lee**

```&gt;&gt;&gt; competition_filter = betfairlightweight.filters.market_filter(event_type_ids=[1], market_start_time={'to': datetime_in_a_week})

&gt;&gt;&gt; competition_filter

{'eventTypeIds': [1], 'marketStartTime': {'to': '2020-08-28T16:31:02Z'}}

&gt;&gt;&gt; competitions = trading.betting.list_competitions(filter=competition_filter)

&gt;&gt;&gt; import pandas as pd

&gt;&gt;&gt; soccer_competitions = pd.DataFrame({

...     'Competition': [competition_object.competition.name for competition_object in competitions],

...     'ID': [competition_object.competition.id for competition_object in competitions]

... })

&gt;&gt;&gt; 

&gt;&gt;&gt; soccer_competitions[soccer_competitions.Competition.str.contains('English Premier')]

               Competition        ID

48  English Premier League  10932509

&gt;&gt;&gt; soccer_competitions

                 Competition        ID

0        Swedish Allsvenskan       129

1       Spanish Copa del Rey     12801

2                   Specials   2608550

3     Danish Women's Matches  12016693

4               Czech 3 Liga    892425

..                       ...       ...

82           French National   1081960

83    Irish Premier Division  12203971

84  Belgian First Division A     89979

85            UEFA Euro 2020  11997260

86         Icelandic 1 Deild  12010570



[87 rows x 2 columns]```

---

## 2020-08-21 13:22:40 - general channel

**D C**

I've used it for close to 20 years now and I would say that you can advertise it as type safe but any language with an operation labelled reinterpret_cast (never mind having to support the C style cast) just can't be. Maybe in the hands of the perfect programmer who knows every line of the ever changing language standards AND never makes an error you could consider it type safe, but in practical terms it is not. For sure it is an improvement on C though I agree there but the fact that is has to support C leads to issues. You can access private members directly from a pointer to object - and this is directly attributable to having to support C language features. I guess we won't end up agreeing on this - it's just my opinion on writing my own bad code and reviewing other people's bad code over the years.

---

## 2020-08-06 06:54:15 - general channel

**Mo**

My trading platform is made up of multiple components each of which is a separate Python process. For example, a Betfair price feed, a market catalogue feed, and each event traded is its own process. Communication between them is done primarily using Redis pubsub but other features are useful - e.g. storing the market catalogues for easy lookup by the different components. For your use case a Redis Set would be perfect for keeping track of which markets you're trading

---

## 2020-08-01 09:13:10 - random channel

**Mo**

Need some help from any PyCharm professional owners...



I have a problem with the documentation popup window feature when typing in the Python console. I start typing a function and the documentation appears. Great. Now I open brackets to start specifying arguments and the documentation disappears - the documentation window says "No documentation found.". At exactly the time when I want to see it so I know what the arguments are and what they do. There are various settings involved such as the delay before the popup appears, whether to show the documentation on mouse move, whether to auto-update from source etc.



Does anyone have any idea what I'm talking about and how to fix it?!

---

## 2020-07-24 15:29:23 - issues channel

**Jon**

thank you so much everyone, now just to work out how to merge the dataframes :slightly_smiling_face:

---

## 2020-07-24 15:29:07 - issues channel

**Jon**

this seems to work:

`market_catalogue_filter = betfairlightweight.filters.market_filter(market_ids=[id])`



`market_catalogues = trading.betting.list_market_catalogue(`

    `filter=market_catalogue_filter,`

    `market_projection=[`

        `"RUNNER_DESCRIPTION"`

        `],`    

`)`



`# Create a DataFrame containing runners for the market catalogue`

`golf_runners_df = pd.DataFrame({`

    `'Selection ID': [runner.selection_id for runner in market_catalogues[0].runners],`

    `'Runner Name': [runner.runner_name for runner in market_catalogues[0].runners],`

`})`

---

## 2020-07-24 14:47:51 - issues channel

**Jon**

i get

```---------------------------------------------------------------------------

KeyError                                  Traceback (most recent call last)

&lt;ipython-input-252-bb440a3eeded&gt; in &lt;module&gt;

     10 )

     11 

---&gt; 12 market_book_to_data_frame(market_books[0])



&lt;ipython-input-235-a1a850e150a8&gt; in market_book_to_data_frame(market_book)

     15             'size': price_size['size']

     16         }

---&gt; 17         for runner in market_book['runners']

     18         for side in ['Back', 'Lay']

     19         for depth, price_size in enumerate(runner.get('ex', {}).get(f'availableTo{side}', []))



C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\frame.py in __init__(self, data, index, columns, dtype, copy)

    467         elif isinstance(data, abc.Iterable) and not isinstance(data, (str, bytes)):

    468             if not isinstance(data, (abc.Sequence, ExtensionArray)):

--&gt; 469                 data = list(data)

    470             if len(data) &gt; 0:

    471                 if is_list_like(data[0]) and getattr(data[0], "ndim", 1) == 1:



&lt;ipython-input-235-a1a850e150a8&gt; in &lt;genexpr&gt;(.0)

     17         for runner in market_book['runners']

     18         for side in ['Back', 'Lay']

---&gt; 19         for depth, price_size in enumerate(runner.get('ex', {}).get(f'availableTo{side}', []))

     20     )



KeyError: 'publishTime'```



---

## 2020-06-17 19:03:37 - issues channel

**jaderson felipe**

I downloaded the file and unzipped it ... but when I try to open it using PANDAS I always get an error ... could someone help me?

---

## 2020-06-15 16:42:38 - issues channel

**Peter**

`#!/bin/bash`



`yum install -y python37 python37-pip`

`yum install -y gcc gcc-c++ python3-devel ujson ciso8601 htop`



`pip3 install numpy pandas python-dotenv tenacity typing betfairlightweight flumine boto3 htop`

---

## 2020-06-14 09:48:57 - issues channel

**Peter**

`from unittest.mock import patch`

`from concurrent import futures`

`import os`

`import time`

`import logging`

`import multiprocessing`



`from pythonjsonlogger import jsonlogger`



`import pandas as pd`

`import smart_open`



`from flumine import FlumineBacktest, clients`

`from strategies.lowestlayer import LowestLayer`





`logger = logging.getLogger()`



`custom_format = "%(asctime) %(levelname) %(message)"`

`log_handler = logging.StreamHandler()`

`formatter = jsonlogger.JsonFormatter(custom_format)`

`formatter.converter = time.gmtime`

`log_handler.setFormatter(formatter)`

`logger.addHandler(log_handler)`

`logger.setLevel([http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))`





`def run_backtest(market):`



    `client = clients.BacktestClient()`

    `framework = FlumineBacktest(client=client)`



    `strategy = LowestLayer(`

        `market_filter={"markets": [market]},`

        `max_order_exposure=1000,`

        `max_selection_exposure=10,`

        `context={"stake": 2},`

    `)`

    `framework.add_strategy(strategy)`



    `with patch("builtins.open", smart_open.open):`

        `framework.run()`



    `market = next(iter(framework.markets))`



    `data = []`

    `for order in market.blotter:`

        `datum = [`

            `order.market_id,`

            `order.selection_id,`

            `order.responses.date_time_placed,`

            `order.status,`

            `order.order_type.price,`

            `order.average_price_matched,`

            `order.size_matched,`

            `order.simulated.profit,`

        `]`

        `data.append(datum)`



    `return pd.DataFrame(`

        `data,`

        `columns = ['market_id', 'selection_id', 'time_placed', 'status', 'price', 'average_price_matched', 'size_matched', 'simulated_profit']`

    `)`



`data_folder = os.path.expanduser('~/data/betfair/test')`

`markets = []`

`_markets = os.listdir(data_folder)`

`_markets = [x for x in _markets if x.endswith('.zip')]`

`_markets = [os.path.join(data_folder, x) for x in _markets]`

`markets.extend(_markets)`



`multiprocessing.set_start_method('fork')`



`print('Running strategy across %i markets' % len(markets))`

`with futures.ProcessPoolExecutor(max_workers=24) as pool:`

    `all_futures = [`

        `pool.submit(`

            `run_backtest,`

            `market=market`

        `)`

        `for market in markets`

    `]`



`all_dfs = []`

`for i, future in enumerate([http://futures.as|futures.as](http://futures.as|futures.as)_completed(all_futures)):`

    `print('Future %i of %i completed' % (i+1, len(all_futures)))`

    `# all_dfs.append(future.result())`

    `all_dfs.append(future.result())`



`df = pd.concat(all_dfs)`

`print(df)`



`print(df.groupby('market_id')['simulated_profit'].sum().sum())`

---

## 2020-06-12 19:56:46 - random channel

**Mo**

Thanks for the input guys. I agree, I don’t think there’s much to like about HDF5 aside from the fact pandas seems to output it incredibly quickly. I’ll check out parquet although probably I will just stick to compressed CSV

---

## 2020-06-12 19:25:28 - random channel

**MacrcoPolo**

I've moved from hdf5 to parquet in other parts of my life as it's more modern and implicitly reads files using multiple cores, so the reads are nice and quick in an age where loading data is often cpu bound on the decompression +conversion to pandas obj end

---

## 2020-06-12 17:44:26 - random channel

**D**

Have you considered parquet format? I went from zipped csv to parquet - compressed but can be saved loaded directly from Pandas.

---

## 2020-06-12 16:58:43 - random channel

**Mo**

I've been working with some larger data frames that are approximately ~5 GB when written to CSV. Pandas takes ages to write them to CSV but seconds to write them to h5 format. But then you lose the ease of readabiltiy e.g. being about to use `head`, `less`, `cat` and other UNIX command line tools. Was wondering if anyone else has experience of dealing with this

---

## 2020-06-12 11:13:42 - strategies channel

**Dave**

[@UUCD6P13J](@UUCD6P13J) - correct, my logic is as follows: take current state of the event (could be football match, race) -&gt; encode to machine understandable values (aka features) -&gt; get the model to forecast an outcome -&gt; convert the forecast probability to a price -&gt; take in the market if there is value. And no I never green up, greening up doesn't make sense in 99% of situations IMO.

---

## 2020-06-06 11:40:26 - random channel

**Sandy Caskie**

When placing a starting price bet I place my order by specifying the liability, this as done as such:

``` string = '{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/placeOrders", "params": {"marketId":"' + marketId + '","instructions":[{"selectionId":"' + j + '","handicap":"0","side":"'+ z + '","orderType":"MARKET_ON_CLOSE","marketOnCloseOrder":{"liability":"' + i + '","persistenceType":"LAPSE"}}],"customerRef":"' + ref + '"},"id": 1}'



               ```

Using pandas in python j, z and ref are stored separately and are passed to the above code. Is it possible to specify the size instead of the liability? I checked the documentation and it only shows examples where liability is specified. I would just place an order myself but I have removed all my funds from my account as testing some stuff therefore if any of you could help without me having to potentially throw money away that would be great. Cheers.

---

## 2020-06-01 07:59:31 - random channel

**Lee**

i never really realise what extra features you get until you try to help someone using community edition

---

## 2020-05-24 19:34:51 - strategies channel

**Unknown**

I have difficulty correlating data with the target (bet market). When I put everything on a dataframe (3 seasons) the number of goals scored, the recent performance, and other data like shots in the goal, corners etc ... has almost insignificant correlation, many goals seem just random.



I am doing a combination of all this and also with the SofaScore chart and there is improved a little, nothing very safe but enough to invest and try to profit.

---

## 2020-05-19 09:36:36 - general channel

**brightcake**

but having something relating a dataframe to the streaming files shouldn't take up too much extra time right?

---

## 2020-05-19 09:11:31 - general channel

**brightcake**

that's fair enough, I can always just create something that relates the dataframe to the relevant market streaming files

---

## 2020-05-19 09:09:49 - general channel

**liam**

would never make pandas a dependency

---

## 2020-05-18 21:35:16 - random channel

**PeterLe**

Evening Folks,

I mentioned on this channel a few weeks ago that a new book was due out called Flash Crash by Liam Vaughan. It tells the story of Navinder Singh Sarao, a UK based day trader who traded the stock market from a standing start (from his bedroom) to amass a fortune of ~£70m!..and then supposedly loose it...

Enjoyed reading it, although a large proportion of the book is centred on the regulatory side of things.

Some soundbites I took: 



- Nav was sell taught

- His strategy was a simple scalping technique, by placing orders out of the money (on what we class as the back side), to skew the weight of money to give the appearance that sellers were in the market. Ie to push the price down. Tactics that are used on Betfair every day (probably by a few of us on here :-)

- He ended up using a standard platform “Trading Technologies” (TT) and had some additional features programmed in by a software engineer at TT. He subsequently had a guy from Edge Technologies to further enhance those features and add a couple more (to take on the HFT’s)

- He wasn’t 100% on auto. Rather, he traded manually with these extra “weapons” as he describes it

- He didn’t write any of his own code

- At his peak he was making upto £900K/Day

- He never spent anything! (Think he treated himself to a new bike and the odd McDonalds:-)

- He attributed his success to his pattern recognition and fast reactions, the numbers dont lie, so can you doubt it?



If anything I think the book tried to paint a picture of his character, that I didn’t quite like. A bit of a dis service to him IMO. He is obviously a clever guy and its not always possible to determine intelligence or judge someone on how they come across that is perhaps different to the norm.

I dont think this will lend itself to a film/movie (Unlike The Big Short), However, it does make a good story and especially to us on here as a glimpse of the art of the possible!!

---

## 2020-05-12 21:31:09 - general channel

**Unknown**

[@U4H19D1D2](@U4H19D1D2) I'm not sure whether or not you'll want the smart_open and pandas dependencies in there, but this runs on my computer. Takes about 35 seconds on running on 12 cores.

---

## 2020-05-08 16:01:08 - random channel

**Mo**

I think for a lot of newbies it is secret sauce. Most people seem to want to start by either building a machine learning model to predict horses and end using features everyone else is already incorporating or some kind of generic time series analysis model to predict price movements as if that’s not driven by fundamental factors. 

---

## 2020-04-29 09:47:19 - general channel

**Cagdas Yetkin**

Yes I did the totorial once. I could place some bets using that. It was all in `pandas` . I am only reading and writing json files so i will try to avoid `pandas` for the time being. And thanks for the link, I am going there now.

---

## 2020-03-15 06:16:49 - strategies channel

**Peter**

[@UUCD6P13J](@UUCD6P13J), I suspect you’re not getting much of a response because the question is way bigger than it looks. But I’ll bite … though I’m not sure you’ll find the answer very helpful!



I can only answer for myself, but I doubt I’m unusual, in saying that it’s both of the above and with way more nuance.



Pre-match predictions, basic or otherwise, aka fundamental analysis, can be useful for spotting where the market is getting it wrong. Most markets will start off a bit away from “fair odds” and work their way towards them as the market comes together - though as Liam has pointed out elsewhere, even then they’re not perfect then and money can still be made at starting prices.



Oftentimes the aim is not to use fundamental analysis to guess the event’s outcome, but simply to anticipate how the market is likely to move and then exit before the event starts, e.g. can you spot a set of circumstances where the favourite is habitually overbet.



Other strategies may ignore the fundamentals and simply look at what’s happening in the market, aka technical analysis or charting. So for example from the history of matched prices I might look for upper and lower bounds, aka resistance and support prices and trade pre-event between these extremes.



Yet another class of strategies uses the prices in one market, often WIN or MATCH_ODDS, to make inferences about related markets and trade on inconsistencies.



Other strategies will use fundamental and technical analysis, for example in-play soccer strategies will take note of how the market is moving with time decay and balance that against the probability of certain events (primarily goals) occurring based on information from matches with similar features.



So overall, it’s a big it depends and is one of the factors that makes this goal so interesting and creates so much space for wildly different approaches.



Given that, in the search for your first profitable strategy, I’d recommend that you dig where you feel most comfortable. Whichever of those two high level approaches calls loudest to you, there’s a profitable strategy waiting for you to discover it.

---

## 2020-03-09 12:26:29 - general channel

**D C**

I am assuming that most people here are Python devs so maybe a waste of time asking the question here but I will try anyway. I have been a C++ dev on and off for 15+ years but since C++11 and later standards have come out I feel the language is not only dying but is overly complicated now and fast disappearing up its own arse. The C++ space seems to now be filled with pseudo-smartarses who enjoy talking about the language in abstract terms and waxing lyrical about new features, rather than rolling up their sleeves and writing something useful. As a consequence, I am looking to get into another language (not discounting pure C either). In terms of long term career demand, does anyone have any suggestions (everything but C# and Java will be seriously considered)??

---

## 2020-03-06 15:35:48 - general channel

**Mo**

Unless you have best execution turned off



```In normal circumstances the placeOrders is an atomic operation.  PLEASE NOTE: if the 'Best Execution' features is switched off, placeOrders can return 'PROCESSED_WITH_ERRORS' meaning that some bets can be rejected and other placed when submitted in the same PlaceInstruction ```



---

## 2020-03-05 21:59:21 - general channel

**Jonjonjon**

Hi Liam, I notice that on the Flumine page, it says that a backtesting feature is in development. Do you have any details on how it will simulate fills?

---

## 2020-02-25 16:46:35 - issues channel

**Peter**

Also, I find the following handy, inside that loop. when I'm processing the data into a pandas dataframe in order to display it updating in a cell in a real-time:

```        display.display(your_dataframe)

        display.clear_output(wait=True)```

---

## 2020-02-22 21:02:31 - strategies channel

**Jonjonjon**

The Pandas package can be used to do analysis and can calculate standard indicators.

---

## 2020-02-11 18:27:08 - general channel

**Alex F**

then to be able to analyze it with pandas probs

---

## 2020-02-11 00:41:19 - issues channel

**Jack Kaminski**

Is there any subscribe to market feature for historical streaming. So I can isolate one event id with a filter out of many market IDs within one input file

---

## 2020-01-10 14:23:57 - issues channel

**oliver**

Hi Mo. I fancy that is the route I just can't get it right! The code I tried (along with other slight tweaks) was:     `def finding_the_amount_of_money_match_on_each_market2():`

    `global betfair_win_race_id`

    `datetime_in_a_week = (datetime.datetime.utcnow() + datetime.timedelta(minutes=1100)).strftime("%Y-%m-%dT%TZ")`

    `market_catalogue_filter = betfairlightweight.filters.market_filter(market_ids=[1.167181875], market_start_time={'to': datetime_in_a_week})`

    `market_catalogues = trading.betting.list_market_catalogue(filter=market_catalogue_filter,`

        `market_projection=["RUNNER_DESCRIPTION","EVENT_TYPE","EVENT","COMPETITION","RUNNER_METADATA","MARKET_START_TIME"],`

        `max_results='100',`

        `sort='FIRST_TO_START')`

    `market_types_mooney_valley = pd.DataFrame({`

        `'name': [market_cat_object.runners for market_cat_object in market_catalogues],})`

    `print(market_types_mooney_valley)`      but the ouput was just the selection_ids for the horses

---

## 2020-01-10 13:44:17 - issues channel

**oliver**

Hi.

I am using a slightly different structure to the examples on the site ([https://github.com/liampauling/betfair](https://github.com/liampauling/betfair)) as I have been following the guide ([https://betfair-datascientists.github.io/api/apiPythontutorial/](https://betfair-datascientists.github.io/api/apiPythontutorial/)).

I am looking for the horses names. I don't mind how I get the names (either when I list the runners in a race, or just finding the specific name that matches with a specific selection_id using a separate bit of code).

I find the list of the runners in a race via the following code:

```def process_runner_books(runner_books):

    best_back_prices = [runner_book.ex.available_to_back[0].price

                        if runner_book.ex.available_to_back

                        else 100

                        for runner_book

                        in runner_books]

    best_lay_prices = [runner_book.ex.available_to_lay[0].price

                       if runner_book.ex.available_to_lay

                       else 1000.0

                       for runner_book

                       in runner_books]

    selection_ids = [runner_book.selection_id for runner_book in runner_books]

    last_prices_traded = [runner_book.last_price_traded for runner_book in runner_books]

    df = pd.DataFrame({

        'Last Price Traded': last_prices_traded,

        'Best Back Price': best_back_prices,

        'Selection ID': selection_ids,

        'Best Lay Price': best_lay_prices,

    }).set_index('Last Price Traded').sort_index()

    return df



def getting_market_info_for_all_the_horses_in_a_race():

    global runners_df

    price_filter = betfairlightweight.filters.price_projection(price_data=['EX_BEST_OFFERS'])

    market_books = trading.betting.list_market_book(market_ids=[betfair_win_race_id],price_projection=price_filter,)

    market_book = market_books[0]

    runners_df = process_runner_books(market_book.runners)```

If anyone could help me get the horses names I would be most grateful.

Cheers

---

## 2020-01-08 20:28:20 - issues channel

**DonJ80**

thanks Liam, i appreciate it. i will test it and let you know. "_*its a simplification of what I use"  what other/new features it includes without giving details and without sharing code, i am and i think others will be very interested to know general information about production level features that professionals like you use or implement and learn from you*_?

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

## 2019-11-14 21:13:15 - general channel

**bogdan**

market_catalogue_filter = `betfairlightweight`.filters.market_filter(event_ids=['28971066'])



market_catalogues = trading.betting.list_market_catalogue(

    filter=market_catalogue_filter,

    max_results='100',

    sort='FIRST_TO_START'

)



# Create a DataFrame for each market catalogue

market_types_mooney_valley = pd.DataFrame({

    'Market Name': [market_cat_object.market_name for market_cat_object in market_catalogues],

    'Market ID': [market_cat_object.market_id for market_cat_object in market_catalogues],

    'Total Matched': [market_cat_object.total_matched for market_cat_object in market_catalogues],

})



market_types_mooney_valley

---

## 2019-11-06 14:43:13 - general channel

**Evaldas**

So I pretty much use same tools, but it's such a mess with bokeh, pandas, matplotlib, excel, looking for one sexy solution, some kind of SQL dashboard.. 

Tableau looks nice, but there is much hate for it everywhere :D

Metabase looks interesting, have you tried it?

---

## 2019-11-06 13:22:41 - general channel

**Mo**

Tableau although I hate it with a passion. Otherwise jupyter/pandas/seaborn

---

## 2019-09-10 09:56:22 - issues channel

**Rob (NZ)**

days_ago = (datetime.datetime.utcnow() - datetime.timedelta(days=1)).strftime("%Y-%m-%dT%TZ")

acct_statement_date_filter = betfairlightweight.filters.time_range(from_=days_ago)



more_available = True

from_record = 0

data = []

while more_available:

    account_statement_result = trading.account.get_account_statement(item_date_range=acct_statement_date_filter, from_record=from_record)

    more_available = account_statement_result.more_available

    from_record += len(account_statement_result.account_statement)

    data.extend(account_statement_result._data['accountStatement'])



recent_transactions = pd.DataFrame(data)

recent_transactions



class_df = pd.DataFrame(json.loads(i['unknownStatementItem']) for i in recent_transactions.itemClassData)

class_df

---

## 2019-06-20 11:57:02 - general channel

**Mo**

```

days_ago = (datetime.datetime.utcnow() - datetime.timedelta(days=14)).strftime("%Y-%m-%dT%TZ")

acct_statement_date_filter = betfairlightweight.filters.time_range(from_=days_ago)



more_available = True

from_record = 0

data = []

while more_available:

    account_statement_result = trading.account.get_account_statement(item_date_range=acct_statement_date_filter, from_record=from_record)

    more_available = account_statement_result.more_available

    from_record += len(account_statement_result.account_statement)

    data.extend(account_statement_result._data['accountStatement'])



recent_transactions = pd.DataFrame(data)

recent_transactions

```

---

## 2019-06-16 09:30:41 - general channel

**Nghia Nguyen**

runners_df is a pandas with these columns: 'Selection ID': selection_ids,

        'Best Back Price': best_back_prices,

        'Best Back Size': best_back_sizes,

        'Best Lay Price': best_lay_prices,

        'Best Lay Size': best_lay_sizes,

        'Last Price Traded': last_prices_traded,

        'Total Matched': total_matched,

        'Status': statuses,

        'Removal Date': scratching_datetimes,

        'Adjustment Factor': adjustment_factors

---

## 2019-06-16 09:29:15 - general channel

**Mo**

And you want to bet on the first runner? I can't remember pandas syntax off the top of my head but you probably want `first_runner_selection_id = runners_df.loc[0, 'Selection ID']`

---

## 2019-06-10 11:59:04 - general channel

**Mo**

(Having done `import pandas as pd`)

---

## 2019-06-10 11:06:20 - general channel

**Rob (NZ)**

Can anyone tell me if my logic is ok, Im able to output say 5 races based on my criteria, based on getting that output should it be able to put the output into pandas for the horses  with say expect start time  (similar to what I think Conr is asking up above

---

## 2019-06-02 21:14:03 - general channel

**Chris**

Trying to display data from a market using Pandas as per the example on the Betfair site (I think I remember seeing these weren't created by anyone here and weren't great, but nonetheless seems the best place to ask), basically have the same problem as this stackoverflow post (but this isn't me), any advice greatly appreciated... [https://stackoverflow.com/questions/55420596/index-error-when-using-betfairlightweight](https://stackoverflow.com/questions/55420596/index-error-when-using-betfairlightweight)

---

## 2019-05-26 10:16:34 - general channel

**Rob (NZ)**

cheers Liam,   I have been using the example code from the betfair website ...   would i just remove the event_id as I imagine thats filtering to just that single event and then put the code you provided down under the list_market_catalogue section?



market_catalogue_filter = `betfairlightweight`.filters.market_filter(event_ids=['28971066'])



market_catalogues = trading.betting.list_market_catalogue(

    filter=market_catalogue_filter,

    max_results='100',

    sort='FIRST_TO_START'

)



# Create a DataFrame for each market catalogue

market_types_mooney_valley = pd.DataFrame({

    'Market Name': [market_cat_object.market_name for market_cat_object in market_catalogues],

    'Market ID': [market_cat_object.market_id for market_cat_object in market_catalogues],

    'Total Matched': [market_cat_object.total_matched for market_cat_object in market_catalogues],

})



market_types_mooney_valley

---

## 2019-04-25 11:31:15 - general channel

**Filippo Bovo**

I am a data scientist and have been using Pandas for about three years. Pandas was built with speed in mind using C (and Numpy), and it is good to manipulating static data. However, I have never tried dealing with live data with Pandas DataFrames. The main bottleneck I see in this case is appending and dropping data to an existing DataFrame. If I will test this in the future, I will let you know.

---

## 2019-02-20 16:33:09 - general channel

**ross o reilly**

Hi there! I am interested in scraping golf market data. For a given golf market, how to i call listMarketCatalogue in python to return a dataframe where the first column is the selection id and the second column is the players name? I'm really struggling to find the correct way to to this. thanks

---

## 2019-02-10 14:14:50 - general channel

**jgnz**

ive been very infrequently trying to scrape bet365 for years, but often use all of this as a way to find things to learn.  sqlalchemy, pandas, modules etc  ive only recently come back to bet365 and betfair with a little more knowledge

---

## 2018-02-26 07:11:27 - general channel

**liam**

Hi,

 

Following the recent developer survey we’d like to provide some feedback on some of the points raised by customers both generally and in terms of additional feature requests.

 

We’ve grouped these into distinct categories:

 

Market Data &amp; Feeds

 

We are constantly exploring ways of incorporating new data feeds into the API.    Unfortunately, there are restrictions relating to the onward supply of specific data via the API (specifically football related data) but we are investigating the incorporation of other data feeds at the moment, including improved feeds for horse racing.

 

The inclusion of raceType is on the current API roadmap and we are looking to integrate this data as soon as possible but don’t have a specific ETA.

 

We are working to make improvements to the consistency of market names &amp; abbreviations across the platform. 

 

We don’t have any plans to add specific results data into the API.  Customer who require results data following market settlement can use the historical data service (via [https://historicdata.betfair.com/#/home](https://historicdata.betfair.com/#/home)).  This data includes the result for each runner by name within the free BASIC data files.

 

We don’t have any plans to remove the time delay associated with in-play betting.  This is in place to protect customers when betting in-play and watching transmission described as “live” that may be actually delayed.

 

Stream API

 

We have an existing backlog item to add additional filters to the Stream API (including competitionId) but no plans to make any changes to the existing filter name.

 

We don’t have any plans to change the way we conflate data via the Stream API but historical data is available via [https://historicdata.betfair.com/#/home](https://historicdata.betfair.com/#/home) in the same format as provided via the Stream API if required for testing &amp; analysis purposes.

 

Pricing &amp; Charges

 

We don’t have any current plans to increase/reduce the £299 fee for Live Application Keys.

 

We received some requests to include an indicator within the API relation to transaction charging.   For transaction charging, we recommend that customers count unique the number of betId’s created in a single hour (0000-0059, 0100-0159, 0200-0259).  Any transaction fees are offset by the following (Commission + Implied Commission) ÷ 2

where Implied Commission = market losses x 3% which is calculated on a daily basis. Full details can be found via [http://www.betfair.com/aboutUs/Betfair.Charges/](http://www.betfair.com/aboutUs/Betfair.Charges/) &gt; Transaction Charges.

 

If there any specific questions/queries you’d like us to follow up with you directly please get in touch via Developer Support ([https://developer.betfair.com/support/](https://developer.betfair.com/support/))

 

Kind Regards

 

Neil

Betfair Developer Program

---

## 2017-12-11 13:44:57 - general channel

**Tom**

Hi Liam, Thanks for posting your betfair code on github.  I'm currently scraping data that I'll use for machine learning. I'm currently after highest price and lowest price matched data to establish ranges that I can use for machine learning on tennis data from 2016. I've downloaded a tar file which I planned to use with a python script and OS walk path. When I open the file there's thousands of subfolders and zipped files and I'm having issues trying to normalize the data to CSV.  I’ve seen your 

[https://github.com/liampauling/betfair/blob/master/examples/examplehistoricdata.py](https://github.com/liampauling/betfair/blob/master/examples/examplehistoricdata.py) file and I’m wondering since you have experience with betfair historical data if you could point me in the right direction? All I want to do really is build a list or dictionary in either json or csv to show Player names tournament name and highest lowest price matched inplay. Would you know if this data is available on the basic plan through betfair api?

Whats the best way to get betfair data into a pandas dataframe?

Your advice would be greatly appreciated! Many Thanks, Tom

---

## 2017-04-19 17:33:52 - general channel

**favetelinguis**

yes pandas is nice as long as your data fits in memory

---

## 2017-04-19 17:33:30 - general channel

**liam**

Used pandas a bit, nice and quick 

---

## 2017-04-19 17:32:12 - general channel

**favetelinguis**

try pandas and scikit-learn

---

