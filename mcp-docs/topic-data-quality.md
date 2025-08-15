# Data Quality - Community Knowledge

*528 relevant conversations from across all channels*

---

## 2025-01-18 22:48:59 - random channel

**Leo**

[@U05N9773A23](@U05N9773A23) can you get the historical data that way ?

---

## 2024-11-25 08:19:49 - general channel

**liam**

Yeah as above, introduced when they realised they could start charging for historical data. I think its a lazy way to do it, I basically used the API to learn python and had there been a charge I probably wouldn't have even started

---

## 2024-11-23 22:12:18 - strategies channel

**Oliver**

not exactly what you asked, but I moved away from the stream JSON format in my engine. The input is of course still JSON as from the stream, but I parse it straight into a point-in-time representation (practically just an array) which is only allocated once, so avoids the creation of a whole bunch of hashes and lists that then get thrown away every update. It makes processing a whole load faster - more of a point1 thing. This applies to both back testing and real world when done like this. In theory a timeseries of the point-in-time version could be something to get fancy with in serialisation/deserialisation e.g. arrow for a more natural representation, or something smarter re. compression maybe along the lines of gorilla timeseries compression.



regarding lookups, I've been aiming to do pre-processing to extract metadata like the market definitions, to place alongside market recordings. It should works fairly nicely in the archive format you get from the historical data API i.e. tar containing files for individual markets + combined streams. At the moment the best I actually do re. lookups is just reading the first message of a market's recording to determine if it matches the market filter, but if not skip on.



Doing that with fairly speedy disk (NVMe), a memory mapped .tar of recordings, and reading in a separate thread, doesn't feel bad even with implementations that have a load to `TODO: simplify/speed up/profile` littered throughout them. It takes about ~2m to go through a day of UK WIN horse racing markets, picking them out from all UK horse racing markets for a day.

---

## 2024-11-23 20:33:14 - strategies channel

**Jhonny**

I'm new to this, but I store live esa and historical data in xtdb. previously, it was just in an binary format, which meant I had to read the whole file to query the market. xtdb time slices are pretty much instant, and allows me to play with many markets at once. drawback is it takes quite the amount of disk space

---

## 2024-11-05 06:46:19 - issues channel

**liam**

No there isn’t anything written however flumine has some code for storing them alongside recording your own historical data if that is what you are asking?

---

## 2024-10-28 10:39:50 - general channel

**James**

Thanks [@U07AK2APF2B](@U07AK2APF2B) I never realised there was a difference between the live data and the betfair historical data. Thanks.

---

## 2024-10-27 12:39:04 - general channel

**Jhonny**

Hi everyone,

How long does it take to get approval for the live API key?

I bought historical data for this month, hoping to use it in conjunction with the api (since it's not allowed to simply listen to markets without betting); However, I haven't gotten any update about my live api key; Not even an acknowledgement of my request. The month is as good as gone

---

## 2024-10-26 16:33:35 - general channel

**Trex44**

Any football traders out there have a good recommendation for a live and historical data provider? Preferably one with UTC time stamps for events?

---

## 2024-10-18 19:20:11 - general channel

**Jonas JN**

We started collecting data at a frequency of minute per minute to obtain the movement of statistics and odds, we found an unofficial API called BetsAPI, they have Betfair events mapped with their events, so it is possible to obtain statistics from their events and join betfair odds easily. However, it is an unofficial API and the data is often messed up.



So we are looking for a more consistent solution, and for the past data that we have not collected, we are trying to use Betfair's historical data, but we would need more than just the odds...

---

## 2024-10-18 15:14:41 - general channel

**Jonas JN**

Hi guys, I'm using betfairlightweight to stream historical data, do you know if it's possible to get the event score for each odd movement?



I would really like to obtain this information along with the movement of the odds, I am trying to link the data with another API to obtain statistics and other information. Could you also tell me if there is a fixed id for teams, besides the selectionId?



Thanks!

---

## 2024-10-14 15:52:18 - general channel

**Gabriel Mocan**

[@U05C31YKZ1C](@U05C31YKZ1C) the free historical data will have this information.

---

## 2024-10-14 08:50:28 - general channel

**Phydeaux**

Free historical data on Betfair will have the full market name I think. Failing that, Timeform API?

---

## 2024-09-21 13:04:23 - general channel

**TT**

How do people typically go about logging/monitoring latency? In particular the latency between betfair's publish time and the clock time when the update is received?



I can think of a couple of ways of doing it:

1. In the market recorder you could log it on each update [https://github.com/betcode-org/flumine/blob/master/examples/strategies/marketrecorder.py#L69|here](https://github.com/betcode-org/flumine/blob/master/examples/strategies/marketrecorder.py#L69|here). (Might be a bit overkill for each update but it would be complete.)

2. Have a background worker log the latency metric to Cloudwatch Metrics/Prometheus etc every x seconds.

Its not something I've been recording but if you want to optimise it (by moving aws region/vps etc) then its important to start tracking it.

---

## 2024-09-15 09:32:26 - general channel

**Johnnb**

I recently separated my market recorder and strategy code and this has caused the market recorder to start generating enormous logs full of warnings like these :



```{"asctime": "2024-09-14 18:04:50,227", "levelname": "WARNING", "message": "Order 361076840419 not present in blotter", "bet_id": "361076840419", "market_id": "1.232946144", "customer_strategy_ref": "ip-172-26-2-232", "customer_order_ref": "fbcd952b00c57-139456298400765211", "client_username": "xxxxxxx"}

{"asctime": "2024-09-14 18:04:50,227", "levelname": "WARNING", "message": "Strategy not available to create order 139456298400765211", "bet_id": "361076840419", "market_id": "1.232946144", "customer_strategy_ref": "ip-172-26-2-232", "customer_order_ref": "fbcd952b00c57-139456298400765211", "strategy_name_hash": "fbcd952b00c57"}```

Can I safely suppress these with a logging filter or do they indicate that I'm doing something wrong? All the recorder's connections are specified as DataStream which I thought meant that they wouldn't receive any order info?



```racing_recorder = S3MarketRecorder(

    name="RACING_RECORDER",

    market_filter=betfairlightweight.filters.streaming_market_filter(

        event_type_ids=["7"],

        country_codes=["GB","IE","FR"],

        market_types=["WIN"],

    ),

    stream_class=DataStream,

    context={

        "local_dir": local_dir,

        "force_update": False,

        "remove_file": True,

        "remove_gz_file": True,

        "recorder_id": recorder_id,

        "bucket":"xxxxxx",

    },

)```

---

## 2024-09-02 15:14:54 - general channel

**tone**

This is the code: strategyMR = MarketRecorder(

            name="Market Recorder TPD",

            market_filter=betfairlightweight.filters.streaming_market_filter(

                market_ids=tpd_market_ids,

            ),

            stream_class=RaceDataStream,

            context={

                "local_dir": utils.configs.marketDataPathToday,

                "force_update": True,

                "remove_file": False,

                "remove_gz_file": False,

                "load_market_catalogue": True,

                "recorder_id": "",

            },

        )

        framework.add_strategy(strategyMR)

---

## 2024-08-23 12:28:33 - issues channel

**James**

I got it from Betfair Pro Historical data, AUS Greyhounds July 2024

---

## 2024-08-12 09:37:25 - general channel

**Sen**

Mostly because the 5 day lag doesn't have a meaningful effect on 95% of features for my fundamental model. Then I just get the data from betfair 5 days later for modelling purposes. But given my fears about my data quality... I'm now very much thinking about recording and storing

---

## 2024-08-11 10:44:17 - general channel

**Sen**

I'm using advanced data - and yes it's got its flaws. Is the pro data actually just higher granularity but the same data quality? or is it higher granularity + higher quality data?

---

## 2024-08-06 21:58:03 - strategies channel

**birchy**

While we're mentioning S3... I'm at a point where I've got millions of markets saved via flumine market recorder and am wondering how others are filtering the files? e.g. say I want all GB horse races that turn inplay, what's the nicest way to find them? I've currently got a somewhat convoluted boto3 setup that paginates the market catalogues and then returns a list of market IDs that match my filters. I then download the files to local storage. I've played around with creating a local index file but it gets very big very quickly. I'm also pondering streaming direct from S3 -&gt; flumine rather than downloading them all as, similarly to [@U4H19D1D2](@U4H19D1D2), I'm processing through flumine to format data for model training.

---

## 2024-08-06 20:09:21 - strategies channel

**liam**

I could use a flat file to store the historical data and move the prediction creation / execution into one as it isn’t time sensitive.



Maybe I have been brainwashed by the microservice way of doing things, I just like the separation of tasks/code

---

## 2024-08-06 19:47:47 - strategies channel

**liam**

I need to build a process that processes historical data and creates predictions on a daily basis (every am) Does anyone have a decent design / system for this? I am currently thinking:



-&gt; machine or lambda to process the historical data to then store in a db 



-&gt; another to create the predictions using the db



-&gt; store predictions in s3 



-&gt; flumine strategy that handles the execution

---

## 2024-08-06 13:51:05 - general channel

**K H**

[https://betcode-org.github.io/flumine/quickstart/](https://betcode-org.github.io/flumine/quickstart/)

[https://betcode-org.github.io/betfair/](https://betcode-org.github.io/betfair/)

[https://github.com/betcode-org/flumine/blob/master/examples/marketrecorder.py](https://github.com/betcode-org/flumine/blob/master/examples/marketrecorder.py)



The second link is an example market recorder flumine provides. But in general you should be able to accomplish what you're trying to do using flumine/betfair-lightweight as a basis (the first two links are to their documentation)

---

## 2024-07-30 08:25:25 - general channel

**liam**

So it looks like you have a good setup for simulating strategies however you need to be careful not to use this for signal creation i.e overfitting on historical data



[@UGV299K6H](@UGV299K6H) I would agree when it comes to inplay and/or strategies with a high edge but with pre race I have always found you need a lot of data.



With TPD I built something off the test data betfair had from Monday and went live on Tuesday thinking the edge would last a few weeks at best :joy: 

---

## 2024-07-29 10:55:54 - general channel

**A**

I am yes. Haven’t got the data yet, and general impatience :joy: 



Thought I’d learn the ropes a bit first before jumping in “properly”.



Currently adding in a market recorder like the one in the examples.

---

## 2024-07-23 10:21:05 - general channel

**Adrian**

[@UQL0QDEKA](@UQL0QDEKA) no I don’t think so. One account, I had had 4 instances of flumine running on two machines at home (gave up on the VPS). One strategy for market recorder, two for live strategies and one for temp/testing. No warnings from the API about connection limits or anything. I don’t my betting patterns were anything weird, one of strategies was placing back and lay bets before the off, the other was placing them after the off.

Why I’m sure it was to do with the political discord is, it was the only place I’ve been posting for the last couple of days, and I was removed instantly from the discord server the second my account was closed. 

---

## 2024-07-10 11:50:54 - general channel

**liam**

IMHO paper trading is for testing your code against live data, no advantage over just simulating using historical data

---

## 2024-07-04 14:02:54 - general channel

**D C**

I really don't know. Given you tend to buy historical data  per month, I'd probably just use the monthly average for the data you've purchased. But probably not a good idea to listen to me - I am not very thorough when it comes to back testing and simulation.

---

## 2024-07-04 12:51:35 - general channel

**Gabriel Mocan**

[@U9JHLMZB4](@U9JHLMZB4) I agree, but let me tell you the whole story.



I’m collecting live data since Aug/23. My system is pretty much validated as far as Monte Carlo allows me to validate, and I’m already live trading for about 45 days in that strategy.



Still, I would like to add more data to the backtest to make it more robust. So I’ve purchased a couple months prior to Aug/23. The thing is, my data is collected in BRL, and the strategy parameters were also designed in BRL (most important being the market volume). To make the backtest cohesive, I would need to convert the historical data to BRL before uploading it to my database.

---

## 2024-07-04 01:43:00 - general channel

**Gabriel Mocan**

Hey there folks,



Quick question: I’ve purchased some historical data from Betfair, but I’m not sure how to handle the currency. My local currency is BRL, and apparently the currency from historical data comes in pounds. What’s the best approach to convert these values as close as they would be at the time of the event?

---

## 2024-06-16 20:27:39 - random channel

**Ralegh**

Flat file is generally the best, you don’t stream to parquet so you either stream to (eg) CSV or betfairs json format then batch convert to parquet, or batch convert historical data to parquet. [https://signalsandthreads.com/state-machine-replication-and-why-you-should-care/|https://signalsandthreads.com/state-machine-replication-and-why-you-should-care/](https://signalsandthreads.com/state-machine-replication-and-why-you-should-care/|https://signalsandthreads.com/state-machine-replication-and-why-you-should-care/) - good reading, generally advice is to have writing be single threaded (ie don’t need a dbms) which reduces complexity. If JS can handle their shittons of data in a single thread (and most financial exchanges) then almost anyone can. My betting stuff is set up roughly similar, all data gets logged to disk and the trading is full deterministic so I can fully replicate a days data in the right order and see exactly why everything happened. Each day gets zipped as one file and put in S3, about 100MB each

---

## 2024-06-14 13:11:50 - issues channel

**Unknown**

Attached is a zip folder containing a simple flumine script, a historical data file and the log file. To avoid problems, open the folder as a whole in the IDE and run the files from there. Hope this helps and please let me know if you need me to explain! Thanks!

---

## 2024-06-10 08:10:04 - general channel

**Ben Coleman**

Hi Guys,

I have been testing a new strategy using historical data simulation on Flumine and I have noticed that quite often some of my simulated bets aren't getting matched. I am only ever trying to trade at the best available price, and I am just wondering what kind of algorithm the Flumine simulation uses to decipher whether you would have been matched or how much you would of been matched. My logic on any given update takes at most 4-5ms.

---

## 2024-05-30 12:21:31 - random channel

**liam**

Hmm, I assume it would also need historical data as well?



Yeah too good, very depressing being back

---

## 2024-05-16 11:56:19 - random channel

**Ralegh**

I think ridge+feature engineering given enough time and ideas may be sota but for stuff like HFT I have heard deep learning, (and also deep RL for execution/optimiser). There’s just so much data and you can fit to it quickly eg blackrock deploying a new execution algo could be factored in if you recalibrated every day but those transient signals might not fit into features that you’ve come up with historically unless you were literally coming up with new ideas every day. 



I think XTX is pretty big on deep learning and their whole thing is taking large positions while making markets so I assume their forecasts are good. That being said regression is like concrete or steel and probably is the final arbiter of what goes in a forecast.



Also ridge + features are a lot handier for transfer learning. If you moved to a new market with little historical data you’d feel pretty confident just copying stuff across. Would be easier to manipulate and remove features (weight = 0) without the required data in the new market than trying to break apart a web of neural network shenanigans. If I’ve learned anything from success stories the easiest way to make money is take a good strategy and apply it to an inefficient/new market.

---

## 2024-05-06 09:15:37 - general channel

**liam**

The market recorder is designed for this, recording the live data and market catalogue for loading during simulation

---

## 2024-05-06 06:28:12 - general channel

**Adrian**

[@UBS7QANF3](@UBS7QANF3) i use MC to get runner ids, names, rugs/boxes and the race number from the market name. it's not a major issue as i can recreate what i need from other betfair data sources, but would be nice just to have it all in one spot so i could treat my historical data the same way I would a live market

---

## 2024-05-02 10:35:21 - random channel

**JL**

are there any way to set `self.client.account_funds.available_to_bet_balance`  accessed through `process_market_book` when simulating on historical data?

---

## 2024-04-26 09:06:55 - issues channel

**Derek C**

This problem isn't affecting me and I run Flumine market recorder 24/7. What do you think decides who is affected by this?

---

## 2024-04-25 21:18:05 - issues channel

**Ammar**

It looks to me like there’s an unexpected response type (as `None`) which is coming thru from the call stack — which looks entirely plausible as I read thru the code all the way back to `betfairlightweight`



to be clear, this isn’t impacting the data stream; but it does look like very unhappy noise in the logs, which is never nice :)



steps to replicate:

• leave the market recorder going on one machine — this is _all_ I’m using flumine for, it’s a single process which I kick off each day.  (currently on a laptop, behind expressVPN, which may be a noteworthy point) 

• use betfair to manually execute and check markets via the mobile app, and other computers

• over the course of 8-10 hours the error will start to present



the fix could be very light in the keepalive (similar to how it’s handling a failure already)





```def keep_alive(context: dict, flumine) -&gt; None:

    """Attempt keep alive if required or

    login if keep alive failed

    """

    for client in flumine.clients:

        if client.EXCHANGE == ExchangeType.BETFAIR:

            if client.betting_client.session_token:

                resp = client.keep_alive()



                # start change

                if resp is None:  # this is the unexpected response type I'm seeing

                    client.login()

                # end chage



                if resp is True or resp.status == "SUCCESS":

                    continue

        elif client.EXCHANGE == ExchangeType.BETCONNECT:

            resp = client.keep_alive()

            if resp:

                continue

        # keep-alive failed lets try a login

        client.login()```

---

## 2024-04-25 10:36:24 - general channel

**alter_life**

I am a bit confused, because betfair historical data also does not contains score, and there are not so many providers who has this data with timestamps (usually it is quite expensive) that makes it almost impossible to backtest the things..

---

## 2024-04-08 19:11:21 - general channel

**Trex44**

Will also look to disable the order stream on the market recorder instance. Not certain how to do this, but that should at least free up one connection.

---

## 2024-04-08 18:58:38 - general channel

**Trex44**

Hmm, that's really odd. I have absolutely no idea how I have reached 10 then. Have to dig about and see if I have left an old EC2 instance running by mistake or something.



I could combine the filters for the market recorders perhaps. They are different filters for each sport at the moment because I wanted to record different countries for some sports and because I use the context on each class instance/sport to direct the files to be saved in different S3 buckets.

---

## 2024-04-01 20:23:04 - general channel

**The Marco**

I have recorded a few markets using the marketrecorder.py script included in the examples. If I understand correctly, the .json file is sort of metadata about the event recorded, the actual data being in the file named after the market_id. The structure seems consistent with the historical Data Feed Spacification here [https://historicdata.betfair.com/Betfair-Historical-Data-Feed-Specification.pdf](https://historicdata.betfair.com/Betfair-Historical-Data-Feed-Specification.pdf)



I would like to start with something very trivial like plotting matched prices for runners over time, backtesting much later. Is there an existing jupyter notebook / python script that I could refer to as an example?

---

## 2024-03-28 09:19:16 - general channel

**liam**

Yes, the example market recorder will do it, which I assume you are already using?

---

## 2024-03-19 10:02:55 - general channel

**James**

Am i able to get market catalogues from anywhere once the market has closed?

The API doesn’t return them, and the Betfair historical data also doesn’t seem to include them.

---

## 2024-02-28 11:23:47 - strategies channel

**Andrey Luiz Malheiros**

Hey guys, I'm running a strategy in live paper trade mode and recording the markets with a market recorder. When I run a simulation for the same strategy over the same period using recorded files, I'm noticing a significant difference in results. So, I have two questions:

• Is there a big difference in results between the simulation and live paper trade mode?

• If not, can someone tell me the possible reasons why I'm seeing such a significant difference? (I'm observing a 320% difference in net profit)



---

## 2024-02-19 23:16:50 - general channel

**Jonjonjon**

The `ERROR_CODE` was `MARKET_SUSPENDED`.

Looking at my historical data file, the market did not get suspended at time of placement.

---

## 2024-02-16 08:58:12 - issues channel

**Al**

I am not being given historical data from betfair, but data recorded as a result of the stream. maybe I don't quite understand the question... this is basic data using best_of_book

---

## 2024-02-15 19:32:23 - general channel

**PeterLe**

Quick Question please on the market recorder

I have the TPD Subscription on one key (via betfair)

I have the code to create a file that contains just the TPD data and I have code that creates a file that contains just the normal data



For those of you that have the TPD on your account; When you record, do you create a single file for each race that contains BOTH the normal data and the TPD data that you can back test against?

Thanks in advance

---

## 2024-02-05 09:46:11 - random channel

**D C**

I'd be surprised if this doesn't breach T&amp;C to be honest. For example, I've been logging horses and dogs for years. But tomorrow I might fancy analysing football and the only way I could do that is to buy historical data. If this were setup, I could just piggyback other users historical data. Surely it's no different to data sharing?

---

## 2024-02-05 09:41:02 - random channel

**James**

Would anyone be open to contributing/helping fund a shared data pool for the sake of backtesting?

Something formatted specifically for flumine, market catalogues, historical data etc?



I feel like we’re likely all recording the same data, and going through the same pain of pulling/zipping/managing/paying to store the data in s3 and alike, and the pulling and unzipping and backtesting. Surely there is some demand here for a simpler way to do it where you can just point and shoot, a paid flumine plugin/addon to cover the data charges and storage costs.



I haven’t at all looked into the ts&cs on this stuff so probably couldn’t even if there is demand but surely this (like flumine) seems something to build once and share.

---

## 2024-02-02 19:14:11 - general channel

**JL**

my bad for being unclear. It's about obtaining historical data from a Swedish account. I understand, I'll contact support and see what they say

---

## 2024-02-02 16:43:37 - general channel

**Peter**

[@U065R0MLLBB](@U065R0MLLBB) It's not clear to which question you're looking for a solution: obtaining historical data in Sweden, or filtering streams on a time range.



If it's the Swedish thing, we've seen other questions about Betfair-related things happening differently in Sweden, so there are likely to be legal, regulatory or licensing issues that preclude an easy answer.



If it's streaming with a time range - that's not how Betfair streams work. The accepted solution is the one alluded to by [@U04NWADNCFR](@U04NWADNCFR), namely record all the data, persist to a file and then stream the through Flumine setting the [https://betcode-org.github.io/flumine/quickstart/#listener-kwargs|listener kwargs](https://betcode-org.github.io/flumine/quickstart/#listener-kwargs|listener kwargs) to do the filtering for you.

---

## 2024-01-24 20:42:20 - issues channel

**Creepto**

Hello, 



I am trying to stream historical data using the python client betfairlightweight, with create_historical_generator_stream(), as in the examples. But I got the error: 'charmap' codec can't decide byte 0x88 in position xy: character maps to &lt;undefined&gt;.

However, when I just open the file with bz2 lib I can read the file. What am I missing?

---

## 2024-01-16 17:41:03 - general channel

**Unknown**

the pitchforks may get pointed at me for this but - just an opposing view on betfair basic data. because it gets a very bad rap in here and needs some friends



• it is definitely useless if you’re trying to do anything low-latency/inplay/high frequency/purely market data-driven

• if your work (like mine) does not fall into this category, its a totally fine place to start. i found it extremely useful when starting out

• a runner’s last traded price accurate to within 1 minute (available in basic data) is far from useless. could be the thing that makes your purely fundamentals model into something profitable

---

## 2024-01-16 12:29:16 - general channel

**Tony**

hello all i am going to start using the market recorder and have an aws account does any one know if i can get away with a micro ec2 instance or does it need more juice?

---

## 2024-01-11 12:17:42 - general channel

**Peter**

By default a Flumine instance uses one connection to subscribe to market updates and one to subscribe to order updates. However you can choose not to subscribe to order updates if you don't need them, e.g. when using the market recorder.

---

## 2024-01-03 10:28:46 - strategies channel

**Unknown**

Sorry for the delay, Liam. I'll send the code in a file just to try to make it easier. But basically, instead of generating a file and saving it, I'm storing all the updates in a string and, in the end, uploading it to a database. I use Django, so the StrategyManagementMarketRecorder is the model responsible for inserting into the database. The structure is based on your market recorder code.

---

## 2024-01-02 15:50:09 - general channel

**Ricky**

Hi everyone! I'm fairly new to the automated betting world and would like to start by getting my hands on some of the historical data that betfair supplies at [https://historicdata.betfair.com/#/home](https://historicdata.betfair.com/#/home). Problem is that I live in Sweden and this service is not accessible for us swedes... Does anyone know an alternate way to get access to historical data? Thanks in advance! :raised_hands:

---

## 2023-12-31 02:42:14 - strategies channel

**Andrey Luiz Malheiros**

I changed the reference code of the market recorder, but I kept the same logic. I believe the issue might not be with the changes I made because some files are being saved correctly, starting with 'marketDefinition.' I suspect that somehow, when the code is attempting to retrieve the market_id through 'MARKET_ID_LOOKUP', it might not be obtaining it initially, causing the market_id to remain 'None'.

---

## 2023-12-29 08:53:57 - random channel

**Adrian**

[@UQL0QDEKA](@UQL0QDEKA) i have used the backtester in limited capacity only since I only have free historical data to work with. That can only give me a rough indication of whether or not I am beating SP, but not how my execution if performing. I have created a simulation using last traded prices of that data and at this point can only make an estimated guess as to how well I would get matched because there is no volume data and the intervals are unusable. This has been one of the major hurdles of production.. actually having quality data to work with. Unfortunately betfair requires you to put money down in order to get data one way or another. So there is that barrier to entry to contend with

---

## 2023-12-13 09:52:13 - strategies channel

**Adam**

long story short - they’re slightly different strategies that I want to test on live data rather than on historical data and if they’re sequential, the latter will be effected by the delay to processing

---

## 2023-12-12 08:40:33 - general channel

**Justice**

Depends what you're doing. RacingPost has fairly accurate data that is very easy to scrape. You can get BSP and in-play high and low from Timeform with a free account, although scraping is very slow- they rate limit you. They have an API but it is seriously expensive. TPD is more for in-running, although I have heard from some in this community that their historical data is doctored to more accurately reflect the position of the horse, and does not reflect the data you receive in real-time- therefore it's useless for modelling

---

## 2023-12-12 07:41:14 - general channel

**Sen**

Hi All- quick question on best sources of data for UK horse racing. Is there any preferences in this community - I'm looking at the more fundamental side.



Betfair historical data + odds

Timeform 

Tpd (total performance data) 

Any other sources that people think are essential? 



Thanks!

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

## 2023-11-23 08:31:10 - strategies channel

**liam**

Is weighted average the only answer when combining probabilities? For context I am trying to form a more accurate price by including the starting price with my own predictions when inplay, theoretical example:



Starting price: 4.0

*Half Time*

Prediction A: 2.0

Prediction B: 3.0

Current price: 3.2

```Combined Probability = (ω1 * 4.0) + (ω2 * 2.0) + (ω3 * 3.0)```

Using a default weight I get:

```Combined Probability = (0.33 * (1/4)) + (0.33 * (1/2)) + (0.33 * (1/3)) ≈ 2.80```

However the starting price is obviously having a large impact in this calculation where I imagine it decays. The predictions themselves are based on historical data with no current knowledge of the starting price.

---

## 2023-11-15 11:02:51 - general channel

**Ralegh**

Are the market catalogues output by market recorder included in historical data? I've been using historical data fine with just market definitions so I'm assuming I can just use the streamed market data files and ignore catalogues?

---

## 2023-10-25 20:26:26 - general channel

**Mikkel**

Does anyone know how non-runner reductions rate are handled in the Betfair historical data?

---

## 2023-10-13 14:46:25 - general channel

**John Foley**

really nice tool, thanks! with historical data downloaded from betfair (not self recorded), you dont get the market catalogue files. i guess that means this package will only work if you recorded the data yourself?

---

## 2023-10-12 11:37:02 - issues channel

**Riccardo Fresi**

don't know, can i use keep alive in the market recorder?

---

## 2023-10-11 00:00:52 - general channel

**foxwood**

Good stuff and a nice solution to managing the data warehouse - which I keep meaning to do ! Had a quick look and a couple of gotchas from my setup that may also apply to others you might like to consider at some point in the future

1. Rightly or wrongly all my market catalogues are gzipped - I thought that was the standard for the default flumine market recorder used here. The implementation seems to require these to be in unzipped form.

2. It's effectively tied to sqlite. Since my need is sql server via sqlalchemy it would be useful if the sql specific bits (possibly statements as well since there are differing sql dialects) were subsumed into a class on their own. That would allow users to implement / contribute their own flavour of sql.

Is this an open project for others to provide contributions or just one you control ? Don't know enough about how github works to answer that - i still use a 30 year old legacy GUI VCS lol.

---

## 2023-10-10 11:25:40 - general channel

**Peter**

Firstly welcome.



All the data you currently want, and more, is available in the files generated by the market recorder, but it needs a slight shift in how you think about them.



The way we approach this here is to save those files as raw data. Then run them through Flumine in simulation mode to extract the specifics that we want for the analysis being done at the time and save it in a format conducive to that analysis.



Later we may return, stream the same raw data but extract different parts of it, e.g. trading volumes, or SP estimates, or some metric that we derive from the raw data. We don't assume that what we want now is what we will want in the future, Hence keeping the data in it's raw form allowing for maximum flexibility.

---

## 2023-10-05 20:17:05 - issues channel

**liam**

The market recorder is for recording *live* data, what are you trying to do?

---

## 2023-10-05 18:10:08 - issues channel

**Andrey Luiz Malheiros**

Hi guys. I'm trying to use the market recorder from the examples on flumine, but it seems like the process_raw_data isn't being executed when I run the simulation. Do I need to adjust any settings to run the process_raw_data?

---

## 2023-09-29 07:24:23 - general channel

**Good Job**

Anyone ran in to missing historical data for certain events? Finding that even English premier league seems to have around a 100 games quite literally nowhere to be found on basic and where I can test, even on other tiers. Any ideas?

---

## 2023-09-25 09:37:09 - issues channel

**Mo**

flumine's market recorder will save both the price stream and the market catalogues

---

## 2023-09-25 08:54:27 - issues channel

**Mo**

I assume from your code that you are:



1. Using the REST API

2. Serially scraping the set of races

So it's not surprising that you are experiencing delayed data when you have a lot of races to loop through



There is a lot else wrong with your code - mainly that you are saving only a small subset of the data



Best practice is to use the market recorder in flumine: [https://github.com/betcode-org/flumine/blob/master/examples/strategies/marketrecorder.py](https://github.com/betcode-org/flumine/blob/master/examples/strategies/marketrecorder.py) to save the raw price stream then you can analyse it after the fact any which way

---

## 2023-09-20 20:40:47 - general channel

**Mona**

I wanted to record this "structured data" in a file that is easy for me to debug. I am not using market recorder, can it be used to record processed data&gt;?

---

## 2023-09-20 20:37:27 - general channel

**liam**

Well it sounds like that is all very slow.



If you are recording data best practice is to record the raw streaming data for simulation after, are you not using the market recorder?

---

## 2023-09-20 10:40:54 - random channel

**Jonjonjon**

[@U01B8031PM1](@U01B8031PM1) have you found the free historical data from Binance useful?

---

## 2023-09-18 13:34:26 - general channel

**Peter**

The market recorder provides the changes to the market only in a raw format. To see the actual state of the market you would run this through Flumine which creates and maintains an internal record of the state of the market as it would be after each update and makes it available to your trading strategies.



No the sample for the live event doesn't save the data to a local file. But once you have the data and have decided in which data and in what format, writing it out to a file is the easy bit. One tip for doing that would be to ensure that you record the time that the data is received, so that you can match that with the market data later.



It's easier to run separate scripts to collect event and market data. especially as the market recorder is already written for you. But there will come a point at which you want to be able to collect both together in order to make trading decisions and place bets. So it's worth working out how to do that early. If you're looking at external sources of data, you'll want to look at how Flumine supports works and middleware. These can be very useful for polling external data sources and merging event data with market data (via the market.context attribute) and feeding it to your trading strategies. There's not an easy way to answer the "how?" part of this as it depends a lot on how your accessing event data and how you plan to use it in your trading strategies.

---

## 2023-09-17 17:07:58 - general channel

**Peter**

It's done very commonly, but there's not a neat example of it as it depends on how the live stats are being consumed. However, you have the [https://github.com/betcode-org/flumine/blob/master/examples/marketrecorder.py|market recorder example](https://github.com/betcode-org/flumine/blob/master/examples/marketrecorder.py|market recorder example) for prices and for live event data the [https://github.com/betcode-org/flumine/blob/master/examples/tennisexample.py|tennis example](https://github.com/betcode-org/flumine/blob/master/examples/tennisexample.py|tennis example) shows how you can poll an external API, while the [https://github.com/betcode-org/flumine/blob/master/examples/example-sportsdata.py|sportsdata example](https://github.com/betcode-org/flumine/blob/master/examples/example-sportsdata.py|sportsdata example) shows how to handle streamed event data if you have access to that.

---

## 2023-09-11 09:30:22 - general channel

**D C**

Yeah charging for the API was something I couldn't believe when I first heard about it. Feels like pure greed - same with charging for historical data. I can't understand creating obstacles to automation like that - I remember when I first started dabbling with automation years ago I would lose hundreds of quid on a new strategy while ironing out the bugs. Probably says more about my slapdash approach to things back then but I can't be the only one who has lost more than £299 learning the hard way along the way.

---

## 2023-09-10 13:31:51 - general channel

**Dave**

Yep, fully agree with your final point - making it free certainly drops the barrier somewhat and may even encourage someone who otherwise may not take the leap due to  lack of representative data. Oh..and making the historical data portal more robust and responsive..

---

## 2023-09-02 10:06:15 - general channel

**Mo**

But you might never have picked up the change depending on when you created your personal market recorder

---

## 2023-09-01 17:54:14 - general channel

**liam**

 Bflw in lightweight mode or the rust betfair library, don’t use basic data 

---

## 2023-09-01 17:46:10 - general channel

**George**

What is the best/fastest way to grab a snapshot of a market book at X minutes before the market start time?

Of course I could load the market in flumine and loop through the updates until I get to the desired timestamp, but that seems to be a relatively slow process.

Would it be a terrible idea just to use the BASIC data instead?

---

## 2023-08-25 10:53:41 - general channel

**Unknown**

hi guys, need some help



i implemented a kelly method function

```def kelly_method(odds):

    b = odds - 1

    p = 0.94 #0.9851668726823238  # precision value for prediction model or historical win rate

    f = ((odds * p) - 1) / b

    return odds, b, p, f```

i have some doubt: p should be the % winning probability of the bet, i'm not sure to use the precision of model or the ex-post % based on actual historical results



in the first case i have a very bad performance

in the second case, not so bad;



by the way also the function give me negative results if the odds has more implicit probability respect the p variable (it makes sense to you?) so i use a 0.5 fixed for negative value (it also make sense to you?)



Other thing: the one i've loss, i suspect that i collect very bad the live odds for this single event, may i ask you if you can send me the historical data for that since seems in italy we cannot retrieve historical data? of course if is not a problem

---

## 2023-08-23 10:50:55 - general channel

**Trex44**

Hey all. Is there a way to use Multiprocessing with [https://github.com/betcode-org/betfair/blob/master/examples/examplestreaminghistorical.py|this example script](https://github.com/betcode-org/betfair/blob/master/examples/examplestreaminghistorical.py|this example script) for recording market data from recorded markets/historical data? My attempts to implement it so far aren't working.

---

## 2023-08-20 15:27:59 - general channel

**Y B**

*Context:* I'm trying to run a very simple strategy (always back the first runner at a certain level) on *basic* data (i.e. just last_price_traded without having access to order book depth). And my orders don't seem to ever get filled.

*Questions:*

• Is there anything that needs to be done to make orders get filled when backtesting on "basic" data?

• Is it even possible to get backtesting work on basic data? I'm fine with either assuming infinite depth at a certain level and/or some const value

• In basic data mode, if I place an order (back)  with "limit=X" 

    ◦ and currently the market (i.e. last traded price) is at A (A &lt; X)

    ◦ the next mkt data tick provides last traded price is at B (A &lt; X &lt; B) -- *will my order get filled?* 

---

## 2023-08-16 06:00:10 - general channel

**liam**

How are you writing to the db? Within a strategy?



Common process is to store raw data using the market recorder and then process to db/csv etc 

---

## 2023-08-13 19:53:38 - issues channel

**Michael**

This might be basic but in Flumine, how do I restrict the market recorder to particular leagues with competition ids? Streaming_market_filter doesn’t seem to have competitons_id argumnt

---

## 2023-08-12 20:32:31 - general channel

**Rishab**

I have been trying to  arrange my files created from market recorder but struggling a bit rn. Let's say I want to create a folder wrt event_Id_type. I tried changing the process_raw_data function : directory = os.path.join(self.local_dir,str(data.get('marketDefinition').get('eventTypeId')),market_id). So this line ensures that my data is saved in the correct location. But the location is created in the add function first and there's no 'data' argument passed to it so I can't find eventTypeId there. What solution are you guys using here?

---

## 2023-08-12 16:34:56 - strategies channel

**Jonjonjon**

It's a broad area. But in general it's predicting future moves using historical data.

---

## 2023-08-05 23:20:18 - general channel

**Trex44**

All brokers provide live data. interactive brokers have menagerie to pick from depending on what markets you want to trade [https://www.interactivebrokers.com/en/pricing/research-news-marketdata.php](https://www.interactivebrokers.com/en/pricing/research-news-marketdata.php). You can also pay for for market depth etc. I think they lower or wave fees once you trade over a certain volume. You can get historical data from them and other sources too e.g. Kinetic. Its the historical stuff that I was surprised how cheap it is relative to BF historic data.

---

## 2023-08-04 12:19:57 - general channel

**joe taylor**

Hi guys! I want to work on some strategy around inplay horse racing. Had a few queries around this: how can I get real-time race data like runner distance left in race or position of each runner in race/speed 2. historical data for each runner with different features-timeform type data &amp; inplay data(like speed in last x fraction of race left etc)

---

## 2023-08-04 10:38:47 - general channel

**AI Trader**

[@U01DVUAE2G1](@U01DVUAE2G1), did you ever compare historical data of raw vs virtual prices ? Did you also find instances such as the one I am sharing? I have many others, so I am not sure I am parsing the data incorrectly (even though I have double checked the raw data)

---

## 2023-08-02 14:32:23 - general channel

**rob smith**

Hello, is it possible to get the VWAP using bflw? Not for historical data but when trading live. Cheers

---

## 2023-08-01 19:35:18 - issues channel

**foxwood**

Market objects have a `__call()` method which flags a catalogue update needed when the `market_book.version` changes. That changes a few times when the reserve substitution takes place. Debugging the market recorder the `market_book` field for every event is set to `None` - is this the gotcha - no book when recording ?

---

## 2023-08-01 10:01:48 - issues channel

**foxwood**

I'm guessing it's something like that having slept on it - pretty sure the latest should work - BF manage to get the name plus "Res" suffix into their price data. Just used the flumine market recorder out of the box I think but will have a look and see if I managed to break it ! Assume this is not normal otherwise others would have fallen over it before ?

---

## 2023-07-23 09:31:51 - general channel

**Jonjonjon**

Using the market recorder example in the Flumine codebase. Then run it on AWS or a similar service

---

## 2023-07-21 20:40:35 - general channel

**Joe Bloggs**

hi, does anyone have any 50ms historical data they are willing to share

---

## 2023-07-07 07:56:27 - general channel

**liam**

Is this self recorded or betfair historical data?

---

## 2023-07-06 10:05:19 - issues channel

**John Foley**

the historical data has a 5 day delay, so never been a big deal if I miss a day or two because of connection errors 

---

## 2023-07-03 16:38:41 - issues channel

**Andrey Luiz Malheiros**

Thanks for help. I wanted a systematic way to retrieve historical data, on a daily basis or so. I guess the best approach will be to try several times a day.

---

## 2023-07-01 17:39:49 - general channel

**Michael**

This is an extremely basic question but I’m having a lot of trouble implementing it. For those using market recorder, I’m trying to write the metadata to a SQL database. I’m calling a function in the process_closed_market function which takes the market definiton, connects to the sql database and then writes it, but nothing is being written (or showing up on logs). When I implement this, I get the following error:

```2023-06-17 22:27:22,654 - ERROR - _get_cleared_market error

Traceback (most recent call last):

  File "/home/ubuntu/.local/lib/python3.8/site-packages/urllib3/connection.py", line 174, in _new_conn

    conn = connection.create_connection(

  File "/home/ubuntu/.local/lib/python3.8/site-packages/urllib3/util/connection.py", line 72, in create_connection

    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):

  File "/usr/lib/python3.8/socket.py", line 918, in getaddrinfo

    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):

socket.gaierror: [Errno -3] Temporary failure in name resolution



During handling of the above exception, another exception occurred:```

It feels like the market is never closing and then I am stuck with a full /tmp file and hence the above error occurs. How does everyone else implement this?

---

## 2023-06-24 08:25:03 - strategies channel

**thambie1**

Anyone have success handling football VAR events in backtests? Is there any way to identify such events in the historical data provided by Betfair, or in recorded data?

---

## 2023-06-16 16:53:32 - issues channel

**Michael**

I keep getting _getclearedmarket error in Market recorder because of read time outs. Is Flumine handling these or is this an error on my part somewhere?

---

## 2023-06-13 23:21:22 - strategies channel

**Michael**

On my market recorder I’m trying to collect IRE and GB racing across several markets. I keep running into the max subscribers of 200, so I’ve split GB and IRE into separate strategies, seems to be working currently but am I going to run into issues with this approach / how do others approach this?

---

## 2023-06-09 16:16:29 - strategies channel

**JazzMan**

How old is your historical data?

---

## 2023-05-27 15:13:26 - issues channel

**Jeff Waters**

Thanks Derek. Does that delay even apply with simulated trading, using historical data?

---

## 2023-05-22 09:07:47 - issues channel

**Jorge**

Hi, I keep getting this error after my flumine trader is running for ~ 1 day. I never get the error in the flumine market recorder script but I do in the trader. The error is gone after restarting the script.

INVALID_SESSION_INFORMATION: UnrecognisedCredentials. This is the full log:



```{"asctime": "2023-05-22 08:01:42,808", "levelname": "ERROR", "message": "[MarketStream: 6393]: INVALID_SESSION_INFORMATION: UnrecognisedCredentials"}

{"asctime": "2023-05-22 08:01:42,808", "levelname": "ERROR", "message": "MarketStream 6392 run error", "exc_info": "Traceback (most recent call last):\n  File \"/root/environments/flumine/lib/python3.8/site-packages/flumine/streams/marketstream.py\", line 44, in run\n    self._stream.start()\n  File \"/root/environments/flumine/lib/python3.8/site-packages/betfairlightweight/streaming/betfairstream.py\", line 67, in start\n    self._read_loop()\n  File \"/root/environments/flumine/lib/python3.8/site-packages/betfairlightweight/streaming/betfairstream.py\", line 233, in _read_loop\n    self._data(received_data)\n  File \"/root/environments/flumine/lib/python3.8/site-packages/betfairlightweight/streaming/betfairstream.py\", line 274, in _data\n    raise ListenerError(self.listener.connection_id, received_data)\nbetfairlightweight.exceptions.ListenerError: connection_id: 101-220523080142-760501, data: {\"op\":\"status\",\"id\":6393,\"statusCode\":\"FAILURE\",\"errorCode\":\"INVALID_SESSION_INFORMATION\",\"errorMessage\":\"UnrecognisedCredentials\",\"connectionClosed\":true,\"connectionId\":\"101-220523080142-760501\"}"}```

---

## 2023-05-17 20:14:08 - general channel

**vtaco**

so if i'm running a market recorder, safe to say theres no reason to run pricerecorder (other than the convenience of all price updates dumped to csv)?

---

## 2023-05-17 06:45:10 - general channel

**liam**

`pricerecorder` is writing some basic data to a csv whereas `marketrecorder` is storing all streaming updates to allow market playback through the simulation and/or bflw

---

## 2023-04-29 05:35:21 - general channel

**RDr**

As MitchM mentioned, the Polling API total matched would be for the sum of back and lay. After some tests backing a few runners and checking the data from flumine market recorder (Streaming API) and  the matched bets from the Polling API, I saw about 5% being systematically added to my back bets and recorded as traded (at least kind of explain why Polling Matched &lt; 2 * Streaming/tv in the snapshot). Would these 5% be for commission or something and included only for Betfair streaming API data?

---

## 2023-04-18 06:52:33 - general channel

**Adrian**

i think i actually wrote some code a couple years back to make the historical data work with flumine but can't remember. i know there was an issue with the cumulative volume being calculated differently

---

## 2023-04-18 06:24:03 - general channel

**Adrian**

thank you Mo. I will try to implement some code that Liam created but it looks like there might be problems with the historical data

---

## 2023-03-18 13:09:53 - random channel

**PeterLe**

In response to the question : summarise the key points from the book - efficiency of racetrack betting markets by william T Ziemba and which is the most optimal strategy:



"Efficiency of Racetrack Betting Markets" is a book by William T. Ziemba and Donald B. Hausch that provides a comprehensive analysis of the betting markets in horse racing. The book examines the efficiency of these markets and explores various strategies for betting on horse races. Here are the key points from the book:

1. Market efficiency: The authors argue that racetrack betting markets are relatively efficient, meaning that odds generally reflect the true probability of outcomes. However, they also point out that there are inefficiencies that can be exploited by astute bettors.

2. The favorite-longshot bias: The book discusses the well-known favorite-longshot bias, which is the tendency for bettors to overbet longshots and underbet favorites. This bias can lead to consistent losses for bettors who consistently back longshots.

3. The importance of data: The authors emphasize the importance of using data to make informed betting decisions. This includes historical data on horse performances, track conditions, and other relevant factors.

4. Handicapping: Ziemba and Hausch provide a detailed overview of various handicapping methods, such as speed ratings, pace analysis, and form analysis. They argue that successful handicapping is essential for consistently identifying value bets.

5. Optimal betting strategies: The book examines several betting strategies and their potential profitability, such as the Kelly Criterion, proportional betting, and fixed fractional betting.

6. Market efficiency and arbitrage opportunities: The authors explore the existence of arbitrage opportunities in racetrack betting markets, where bettors can lock in a profit regardless of race outcomes.

7. Risk management: The book emphasizes the importance of managing risk in betting, highlighting that the optimal betting strategy should take into account the bettor's risk tolerance and bankroll size.

The most optimal strategy, according to the authors, is using the Kelly Criterion. This betting strategy involves adjusting bet sizes based on the perceived edge and the bettor's bankroll. The Kelly Criterion is known for maximizing long-term growth while also managing risk. However, it's important to note that the success of this strategy depends on the bettor's ability to accurately estimate the true probabilities of race outcomes and identify value bets.

---

## 2023-03-18 11:45:55 - random channel

**river_shah**

If I know favourites are over bet in signifiant horse races, what should I do?





If you believe that favorites are overbet in significant horse races, it means that the public is putting too much money on the favorite horses, causing their odds to be lower than their true probabilities of winning. In this case, you can consider the following strategies to potentially take advantage of this market inefficiency:

1. Bet on non-favorites: Focus on betting on non-favorite horses that may have higher odds than their true probabilities of winning. These horses may be undervalued due to the overbetting on the favorites, which can create potential value bets.

2. Look for value in exotic bets: Exotic bets, such as exactas, trifectas, or superfectas, involve predicting the order of finish for multiple horses in a race. Since most bettors tend to focus on favorites, there may be value in including non-favorite horses in your exotic bets.

3. Bet on races with less public attention: Large races tend to attract more casual bettors who tend to overbet favorites. By focusing on races with less public attention, you may find more accurately priced odds, allowing you to identify value bets more easily.

4. Utilize a data-driven approach: Collect and analyze historical data on horses, jockeys, trainers, and race conditions to build a predictive model. This can help you identify undervalued horses and make more informed betting decisions.

5. Implement a disciplined bankroll management strategy: To minimize your risk, use a disciplined bankroll management strategy, such as betting a fixed percentage of your bankroll on each race. This can help protect your bankroll from significant losses due to unexpected race outcomes.

6. Monitor the odds movement: Keep an eye on the odds as they change leading up to the race. You may find value bets if you can identify and capitalize on any discrepancies between the odds and your assessment of each horse's true probability of winning.

Remember, betting on horse races always involves a level of risk. While you may be able to identify value bets by exploiting the overbetting on favorites, it's essential to have a disciplined approach to bankroll management and be prepared for potential losses.

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

## 2023-03-13 19:29:26 - general channel

**Michael**

Birchy are you writing to a server on the lightsail instance or doing it another way? I’m currently writing data to mysql on lightsail but its for scraping so not sure how it will react when I’m writing data every second for a market recorder

---

## 2023-03-08 08:56:27 - general channel

**Unknown**

Hi everyone, apologies for a complete beginner question but I am brand new to Python and betfairlightweight. I have cannibalised some code online to extract the following data from the Betfair Historical Data BASIC soccer files. It has the last pre-play odds and the ltp which is more than I ever expected to get! However, what I would really like is to adjust the code so it produces a similar Excel file but with the last pre-play odds (already got), the half-time odds (if the market is not closed at half-time), the highest price traded and the lowest price traded. If at all possible as a cherry on the top, if all of the recorded odd movements could be put into the columns to the right from the market going in-play until it closes that would be great. Apologies for such a basic question, finding my feet with coding!

---

## 2023-02-09 10:47:12 - random channel

**liam**

*[https://promos.betfair.com/promotion?promoCode=CHELTHISTDATA|Cheltenham Festival - Free Exchange Historical Data](https://promos.betfair.com/promotion?promoCode=CHELTHISTDATA|Cheltenham Festival - Free Exchange Historical Data)*



_The Betfair Historical Data service provides time-stamped Betfair Exchange data for purchase &amp; download to registered Betfair customers_

_To mark the up and coming Cheltenham Festival (14th-17th March) we are offering the following free data packages (worth £1097) covering the Cheltenham Festival period over the last 4 years._



_• Horse Racing - ADVANCED data – March 2019-2022_

_• Horse Racing - PRO data - March 2019-2022_

---

## 2023-02-02 11:14:54 - betfair-news channel

**Yosef Mentzer**

Hi, is the Historical Data API down? I am getting error 500 when I make requests and the web API does not show plans, "My Data", etc.

---

## 2023-01-31 19:13:42 - general channel

**Peter**

Broadly what [@UFTBRB3F1](@UFTBRB3F1) said, but with a couple of tweaks.



A minor point on football markets: handicaps will be non-zero for most runners in the Asian Handicap market type, and zero for other markets.



I recommend against trying to filter data from the market recorder as you stream it. Better is to collect it raw (i.e. not just the best prices), compress it and save it, all of which the marketrecorder does by just setting the parameters. Then process the files offline to extract the data you want. The reason for this process is that as you gain more experience in this field, you will probably find that you need more extensive data from which to extract the features that you will use to derive your trading triggers. And while it's easy to filter out the data you're not yet interested in, it's impossible (or at least very expensive if you buy it from Betfair) to infill later the data you wished you'd collected.

---

## 2023-01-24 06:34:53 - general channel

**Andrew**

Are you using the stream? Prices are on the RunnerBook. And keep historical data in the runner context.

---

## 2023-01-16 21:02:21 - general channel

**Trex44**

Think I have just copied that over from the Market Recorder start, didn't realise it was a different class of stream for recording data.

---

## 2023-01-11 14:15:15 - issues channel

**JFP**

Prob should clarify. I have a strategy that places bets live. Have been running this with profit. When I simulate this strat with historical data, I get negative results

---

## 2023-01-09 17:34:55 - general channel

**Ralegh**

Is there a good way to download historical data straight to AWS? Rather than scp, would be a lot faster, I tried using the link from the website but didn’t work

---

## 2022-12-30 10:41:13 - general channel

**Ralegh**

Extra Q; would using the market recorder be a better choice than buying 50ms data? Or is 50ms intervals enough?

---

## 2022-12-28 19:52:19 - general channel

**Mark Zheng**

Hi all, I'm currently learning how to backtest with Flumine by following this tutorial:

[https://betfair-datascientists.github.io/api/How_to_Automate_5/](https://betfair-datascientists.github.io/api/How_to_Automate_5/)



I am running into an issue where several values such as 'profit' and 'size_matched' are all 0, meaning I can't create any meaningful insight. I've tried using the exact "Back the favourite" code, including using a similar dataset but the issue still persists. As far as I can tell, the only things that I have different is that I have the basic data. Has anyone ran into this issue before or has an idea on what might be causing it?

---

## 2022-12-23 15:29:34 - strategies channel

**Peter**

Use the [https://github.com/betcode-org/flumine/blob/master/examples/strategies/marketrecorder.py|market recorder](https://github.com/betcode-org/flumine/blob/master/examples/strategies/marketrecorder.py|market recorder) to record and save the raw stream data.

---

## 2022-12-21 13:19:00 - general channel

**R**

Yep, issue with scrapers is if the site layout / schema changes then you need to rewrite.  I avoid them for this reason.



as far as comparison to paid data services, I can't say but I would reason that the services are paid because they are more valuable than what is available on public websites.



on 4) check out the lowestlayer here : [https://github.com/betcode-org/flumine/tree/master/examples/strategies](https://github.com/betcode-org/flumine/tree/master/examples/strategies) and you can pair this with a market recorder

---

## 2022-12-21 08:51:13 - general channel

**R**

As far as I know:



1. TimeForm ($$$)

2. Proform ($$)

3. Webscrapers ($ / time)

4. Flumine / Market recorder to gather data from the exchange (but you might not call this fundamental data)

For written guides, I guess check out the betcode repos



[https://github.com/betcode-org/betfair](https://github.com/betcode-org/betfair)

[https://github.com/betcode-org/flumine](https://github.com/betcode-org/flumine)



or the betfair developer site itself, which has some docs too (can't get a link right now, good ole VPN issues)

---

## 2022-12-01 14:51:12 - general channel

**rob smith**

When parsing historical data with [https://github.com/betcode-org/betfair/blob/master/examples/examplestreaminghistorical.py](https://github.com/betcode-org/betfair/blob/master/examples/examplestreaminghistorical.py) how do you get the market name? Eg 5f Hcap

---

## 2022-11-22 19:21:48 - strategies channel

**Dave**

Question for those running strategies with high passive top-of-book presence. Do you make any effort to remove your orders in historical data? Seems highly non-trivial but also highly important if you want to then launch your backtest on a period over which you ran in prod....

---

## 2022-11-09 12:57:35 - general channel

**FT**

Hi guys, I've got a flumine specific question. I don't know if I misunderstand something in the way the blotter works. I'm simulating a simple strategy with historical data. In this particular case, at the end all the orders in the markets blotter show up as PENDING, which is very unlikely since there are a lot of them and I take very bad prices just to see if they ever get the status EXECUTION_COMPLETE.

I collect some of the orders information into a dataframe. This is one example row. Why do I have a `avg_price_matched` and `size_matched` and `profit`, when the order is still PENDING? By the way the placed_at and completed_at are seconds to start time.

```selection_id  placed_at  completed_at  status                price  side  avg_price_matched  size_matched  profit

28396755      -348.287   -348.287      OrderStatus.PENDING   1.81   BACK  1.91               2.0           1.82```

---

## 2022-11-05 01:56:45 - general channel

**Unknown**

You can get this historical data from [http://betsapi.com|betsapi.com](http://betsapi.com|betsapi.com) a cheap (and slow) API.

---

## 2022-11-01 08:20:30 - issues channel

**Mo**

1. It's technically a JSONL or line delimited JSON file. It's the same format as what you get if you purchase the official Betfair historic data - one streaming API message per line

2. There is a prices_file_to_csv_file function in betfairutil

3. Probably. It depends on a couple of things: 1. is the market active? If there are no price changes in those 10 minutes then don't expect there to be any changes to the file 2. are you looking at the prices file or the market catalogue? The market recorder should be saving both. You wouldn't expect the market catalogue to change (much)

---

## 2022-10-23 14:55:43 - general channel

**Unknown**

Hello all,



Please, does anyone suggest a way to get a historical database for the Corner`s event in a timeline view (minute of the event) ? Thanks!

---

## 2022-10-14 12:10:25 - general channel

**FT**

Hi, I just found bflightweight a few minutes ago. I got the following question:

I purchased historical data in 50ms resolution and I wanted to recreate the stream of orders (place as well as cancel) that went into the markets. I'm not yet sure if this is something where bflightweight can help. I found the _create_historical_generator_stream_ function. Can I subscribe to the order stream generated by it?

I thought I'd just ask before wasting a lot of time exploring.

Thanks in advance

---

## 2022-10-10 12:24:36 - betfair-news channel

**Michael McGarry**

does anyone know how to tell which sport a market book refers to when working with data from 'Other Sports'? I'm trying to find historical data for darts matches differentiated by competition and can't see any field for 'sport' and when querying for historical data the sport field will only take 'other sports' as an input.

---

## 2022-10-05 22:46:57 - betconnect channel

**Mr West**

As far as betfair historical data is concerned I wouldn’t go back more than a couple of years.  If you’re strategies are looking at the amount of money being matched then old data behaves differently.

---

## 2022-10-05 11:22:47 - issues channel

**Michael McGarry**

Hi, I'm trying to parse historical data with betfairlightweight and I'm encountering an issue with get_file_list that I can't seem to solve. I get an error every time stating:



```InvalidResponse: Invalid response received: 

[!DOCTYPE html](!DOCTYPE html)

&lt;html&gt;

&lt;head&gt;

&lt;meta name="viewport" content="width=device-width" /&gt;

&lt;title&gt;ngErrorRedirect&lt;/title&gt;

&lt;/head&gt;

&lt;body&gt;

&lt;div&gt;

Error

&lt;/div&gt;

&lt;script defer src="[https://static.cloudflareinsights.com/beacon.min.js/v652eace1692a40cfa3763df669d7439c1639079717194](https://static.cloudflareinsights.com/beacon.min.js/v652eace1692a40cfa3763df669d7439c1639079717194)" integrity="sha512-Gi7xpJR8tSkrpF7aordPZQlW2DLtzUlZcumS8dMQjwDHEnw9I7ZLyiOj/6tZStRBGtGgN6ceN6cMH8z7etPGlw==" data-cf-beacon='{"rayId":"75556616acc7dc25","token":"d048f65d27954a24aa6b1d7d2ddcb256","version":"2022.8.1","si":100}' crossorigin="anonymous"&gt;&lt;/script&gt;

&lt;/body&gt;```

This happens even when trying to search for just a couple of days of data, so it isn't an issue of querying too much data. The files definitely exist as the get_collection_options and get_data_size are returning what I'd expect for the same parameters.

---

## 2022-09-24 16:40:16 - issues channel

**Newbie99**

I'm sure this will be something incredibly dumb, but why would the market recorder not always produce a .gz file when the market closes?



Here is my code:



```import time

import logging

import betfairlightweight

from pythonjsonlogger import jsonlogger

import account_info as ai

from flumine import Flumine, clients

from flumine.streams.datastream import DataStream

from marketrecorder import MarketRecorder

from flumine.worker import BackgroundWorker

from recorded_files_worker import sort_recorded_files

from flumine.streams.datastream import RaceDataStream



logger = logging.getLogger()



custom_format = "%(asctime) %(levelname) %(message)"

log_handler = logging.StreamHandler()

formatter = jsonlogger.JsonFormatter(custom_format)

formatter.converter = time.gmtime

log_handler.setFormatter(formatter)

logger.addHandler(log_handler)

logger.setLevel([http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))



trading = betfairlightweight.APIClient(ai.accname, ai.accpass, ai.acckey, certs=ai.path)

client = clients.BetfairClient(trading, interactive_login=False)



framework = Flumine(client=client)



strategy = MarketRecorder(

    name="horse_racing",

    market_filter=betfairlightweight.filters.streaming_market_filter(

        event_type_ids=["7"],

        country_codes=["GB", "IE", "US", "AU", "FR"],

        market_types=["WIN", "PLACE", "EACH_WAY", "OTHER_PLACE"],

    ),

    stream_class=DataStream,

    context={

        "local_dir": ai.market_recorder_path,

        "force_update": False,

        "remove_file": True,

        "remove_gz_file": False,

    },

)



framework.add_strategy(strategy)



strategy = MarketRecorder(

    name="football",

    market_filter=betfairlightweight.filters.streaming_market_filter(

        event_type_ids=["1"],

        market_types=["OVER_UNDER_05", "OVER_UNDER_15", "OVER_UNDER_25", "OVER_UNDER_35", "OVER_UNDER_45", "CLEAN_SHEET", "MATCH_ODDS", "MATCH_ODDS_AND_BTTS", "BOTH_TEAMS_TO_SCORE", "HALF_TIME",

                      "HALF_TIME_SCORE", "FIRST_HALF_GOALS_05", "FIRST_HALF_GOALS_15", "FIRST_HALF_GOALS_25", "CORRECT_SCORE", "DOUBLE_CHANCE", "DRAW_NO_BET"]

    ),

    stream_class=DataStream,

    context={

        "local_dir": ai.market_recorder_path,

        "force_update": False,

        "remove_file": True,

        "remove_gz_file": False,

    },

)



framework.add_strategy(strategy)

framework.run()```

The strange thing is, for horse racing, it creates a .gz file, but for football it just leaves the file unzipped (it records it correctly, just leaves it as the market name in the folder), why would this be?



Even more weirdly, it appears to correctly create the .gz files for the first x markets after startup, then stops...again just for football, which makes zero sense to me!

---

## 2022-09-14 21:08:11 - general channel

**Alessio**

40k means you have some historical data for both right? Then I would use something that is not names, like which days the played and against whom. That way you kinda get a graph, and you can do a first batch.

---

## 2022-09-06 20:05:33 - general channel

**Trex44**

Guys, can anyone who is familiar with the [https://historicdata.betfair.com/Betfair-Historical-Data-Feed-Specification.pdf|betfair historical data-feed-specs](https://historicdata.betfair.com/Betfair-Historical-Data-Feed-Specification.pdf|betfair historical data-feed-specs) explain to me what _*0 vol is remove*_ means. For `trd` for instance you would never reduce the trd value or remove it as I understand it as this number represents the value traded at a given price so should only ever increase.

---

## 2022-09-06 17:27:58 - issues channel

**Mona**

Hello guys, I am new to here.

I am working on some historical data for a particular market when events are inplay and trying to get the latest traded price time series. Has anyone have any experience with the Rust library they used on the tutorial? I have got to the point where all prices return within the Market.runner object is None, I am trying to understand whether it is the package problem or whether it is my understanding of the historical data structure that I need to do some modification?

Also the package is said to work with betfairlightweight as some of the functions can return MarketBook object, but I can't access its MarketBook._data attribute.

Thanks very much for help

---

## 2022-09-05 07:01:27 - general channel

**Mick**

From an earlier Q&amp;A I learned that the "BASIC" betfair historical data ([https://historicdata.betfair.com/#/home](https://historicdata.betfair.com/#/home)) could not be used to reconstruct the state of the back/lay ladders but you can do it with the "PRO" data. I was just wondering if you can reconstruct the ladder state with the "ADVANCED" data (albeit less frequently than with the pro).

---

## 2022-08-28 12:50:31 - issues channel

**Alan Patterson**

I'm testing streaming historical data using betfairlightweight. I can't get smart_open to work to open the bz2 files.

If I unzip the files it works fine.

I am importing in my python script before doing anything, so I think the imported open should override the built in, but it is not working.

Any help on using smart_open when reading the historical bz2 files?



```from smart_open import open



import betfairlightweight

from betfairlightweight import StreamListener



...```

---

## 2022-08-18 11:07:32 - random channel

**birchy**

Given that most of us are running market recorders and collecting the same data sets, it would make sense if we amalgamated the data from a handful of instances but as [@UBS7QANF3](@UBS7QANF3) states, it's a grey area regarding Betfair licencing &amp; selling. Probably better to just team up with a couple of trustworthy colleagues and share data privately.

---

## 2022-08-18 09:18:36 - random channel

**Mo**

Easier to update individual components yeah but I still use the market recorder to scrape the price stream so I face this problem too



I agree with [@U016TGY3676](@U016TGY3676) if it was essential you had no gaps then I think the only solution is you run 2 instances and stagger the deployment of updates



I sort of follow the policy of buying the historic data for the sports I trade so the scraped data acts as something available for immediate analysis while the historic data is - I hope - a cleaner and more comprehensive data set when that is needed. However, as I'm sure you can guess or know the historic data is far from perfect



Given that there's huge overlap in what we're all scraping I think the ideal would be some kind of data sharing but that's a very gray area

---

## 2022-08-17 12:32:09 - random channel

**river_shah**

Let’s say one refactors market recorder and need to update containers, what is the best way to terminate old instances and bring up new ones without causing any blips in data recording?

this is typically very stable code but still curious how 100% uptime can be achieved

---

## 2022-08-17 11:57:16 - random channel

**river_shah**

For long running tasks such as market recorders, do you guys ever experience outages or does AWS /cloud platform of choice handle live migration gracefully and flumine keeps running?

---

## 2022-07-24 23:22:06 - general channel

**InvestInHorses**

Question for `CORRECT_SCORE` markets on football, specifically Premier League:



The "runner" in the correct score market has `SelectionId` and `runnerName`:



`{RunnerDescription : SelectionId=1 : runnerName=0 - 0 : Handicap=0 : SortPriority=1 : Metadata=}`



Does anyone know if the `SelectionId` and `runnerName` always remain constant? i.e. if I know the selection the `SelectionId=1` will that always be `0 - 0` for every Premier League game?



This seems like a reasonable assumption to make, but I haven't parsed through the Historical Data, but if someone could confirm this for me would save me a bit of time. Or would you recommend parsing the `runnerName`? Also, does this data ever have  deviations e.g. instead of `0 - 0`  we can have `0 - 0.` i.e. notice the period, for example

---

## 2022-07-24 12:48:47 - random channel

**PeterLe**

[@U010GM77S4W](@U010GM77S4W) recently explained how to add more than one strategy to a single instance (thanks madelbot) using this :

import logging

import betfairlightweight

from pythonjsonlogger import jsonlogger



from flumine import Flumine, clients

from flumine.streams.datastream import DataStream

from Strategy1 import Strategy1

from Strategy2 import Strategy2





logger = logging.getLogger()



custom_format = "%(asctime) %(levelname) %(message)"

log_handler = logging.StreamHandler()

formatter = jsonlogger.JsonFormatter(custom_format)

formatter.converter = time.gmtime

log_handler.setFormatter(formatter)

logger.addHandler(log_handler)

logger.setLevel([http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))



trading = betfairlightweight.APIClient('username', 'password', app_key='app_key',

					certs='/path/to/certs')

trading.login()



client = clients.BetfairClient(trading)



framework = Flumine(client=client)



markets1 = betfairlightweight.filters.streaming_market_filter(

           event_type_ids=["7"],

           country_codes=["GB", "IE"],

           market_types=["WIN"]

)



markets2 = betfairlightweight.filters.streaming_market_filter(

           event_type_ids=["4339"],

           country_codes=["GB"],

           market_types=["WIN"]

)





strategy1 = Strategy1(

    name="Strategy1",

    market_filter=markets1,

    max_order_exposure=50000000,

    max_selection_exposure=6000000,

    max_trade_count=200,

    max_live_trade_count=1,

    context={"stake": 2},

)



strategy2 = Strategy2(

    name="Strategy2",

    market_filter=markets2,

    max_order_exposure=50000000,

    max_selection_exposure=6000000,

    max_trade_count=2000,

    max_live_trade_count=2,

    context={"stake": 2},

)



framework.add_strategy(strategy)

framework.add_strategy(strategy2)



framework.run()



I assume you can use the same principle using the market recorder to record more than one sport/category?

If so, Ill probably just add one more sport category for now, but is it good practice to add multiple sports. Does it start to slow the system down too much if you add multiple? Would it be reasonable to assume it could handle 3 or 4 categories easily? (Im using ubuntu on AWS 4gb ram, 2 CPU's)

(Can someone remind me of the subscription limit too please?) Thanks in advance

---

## 2022-07-20 10:19:33 - issues channel

**liam**

This is probably my fault;



*paper trading* is just forward testing, ie. testing on live markets but no real orders being placed



*backtesting* I see as applying a strategy on historical data



*simulation* is accurate play back of historical data as is if it was live using exactly the same code/integration



I changed the name in flumine as I found backtesting to be a bit vague as the simulation in flumine is far more powerful however I accept many will argue backtesting/simulation are the same. I will regularly 'backtest' outside of flumine using csv/pandas/jupyter before coding up properly and simulating in flumine. This allows quicker iterations without the heavy processing 'simulating' requires

---

## 2022-07-18 15:14:31 - random channel

**PeterLe**

Good Afternoon, Wow its cracking the flags in Manchester today! :hot_face:



Although I have the market recorder running fine in windows, Im trying to get it running in Ubuntu and I can see it is failing due to the certs reference below.



import time

import logging

import betfairlightweight

from pythonjsonlogger import jsonlogger



from flumine import Flumine, clients

from flumine.streams.datastream import DataStream

from marketrecorder import MarketRecorder

# from flumine import MarketRecorder



logger = logging.getLogger()



custom_format = "%(asctime) %(levelname) %(message)"

log_handler = logging.StreamHandler()

formatter = jsonlogger.JsonFormatter(custom_format)

formatter.converter = time.gmtime

log_handler.setFormatter(formatter)

logger.addHandler(log_handler)

logger.setLevel([http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))



myacc = str(input("please enter account name: "))

app_key = str(input("Please enter key: "))

mypass = str(input("Please enter Password and 2FA: "))

trading = betfairlightweight.APIClient(myacc,mypass, app_key, certs=r"C:\certs")



# client = clients.BetfairClient(trading) //Changed 21st July

client = clients.BetfairClient(trading, order_stream=False)



framework = Flumine(client=client)



strategy = MarketRecorder(

    name="WIN",

    market_filter=betfairlightweight.filters.streaming_market_filter(

        event_type_ids=["7"],

        country_codes=["GB", "IE"],

        market_types=["WIN"],

    ),

    stream_class=DataStream,

    context={

        "local_dir": "/home/ubuntu/flumine",

        "force_update": False,

        "remove_file": True,

    },

)



framework.add_strategy(strategy)



framework.run()



Question Please: Can i copy over the certs I have in my windows systems and then reference them something like : -

trading = betfairlightweight.APIClient(myacc,mypass, app_key, certs=r"/home/ubuntu/certs") I assume they are just a digital file and not specific to an OS?

Or, more likely, am I going about this the wrong way. Thanks in advance

(PS I will set the environment settings soon :grinning:)

---

## 2022-07-17 10:56:58 - random channel

**birchy**

Personally, I use a $10 instance for a small handful of strategies and a market recorder. CPU runs around 10%, so plenty more capacity.

 A $5 would probably suffice for my stuff.

---

## 2022-07-13 16:39:28 - random channel

**Unknown**

I'm not actually much of a betcode user so forgive my ignorance...



I want to extract some data from the free (one minute interval) betfair historical data and write it out as csv so I can process it with my C code. The data I want is something like a snapshot of everything contained in the image below (for all races in a date range) at a certain time of day – or perhaps a certain number of minutes before the start of a race. So my question is, what would be the least painful way to do this? Does betcode (or flumine?) have this kind of functionality built in already? Or has someone made some other kind of utility to do this?

---

## 2022-07-13 11:22:00 - issues channel

**liam**

Ah, no the market recorder will use a different stream, I have a fix [https://github.com/betcode-org/flumine/pull/594/commits/9895e827ea15aa51db74bd36ed957358c235c983|here](https://github.com/betcode-org/flumine/pull/594/commits/9895e827ea15aa51db74bd36ed957358c235c983|here) that I will push out today

---

## 2022-07-06 15:55:50 - random channel

**EJono**

Thank you for the insight and use case. Its good to know what youve been able to get out of the service. The documentation is slightly unclear what endpoint should be used for live football scores, for instance the "Events API" has an inplay endpoint but its not clear if this data is made available after the match is terminated ie is historical data at that point. Which ebdpoint do you utilise for inplay live scores on football?

---

## 2022-07-03 09:15:05 - general channel

**Trex44**

Hey all. Is there anywhere where I can get historical data on Runners that would link to Betfair id's.  I have a lot of race data recorded from Betfair but didn't record the runners actual names or finishing positions at the same time.

---

## 2022-07-01 20:10:01 - strategies channel

**nthypes**

it uses historical data

---

## 2022-06-27 10:16:50 - random channel

**Newbie99**

Is there a neater way of removing latency warnings when using the market recorder than changing the MAX_LATENCY value in the basestream.py file (for Flumine)?

---

## 2022-05-31 21:02:40 - general channel

**Michael**

For historical data in the form 1.xxxx.bz2. Does the xxx mean anything i.e. date or market?

---

## 2022-05-27 05:41:46 - betfair-news channel

**Wilcox**

Hey guys, I am new here. What is the best way to convert historical data to a csv file? The data is from BASIC tier 

---

## 2022-05-21 18:18:00 - issues channel

**Peter**

You can collect it from the historical data (or your streamed data). It can be found near or at the end of each market in the market close update.

---

## 2022-05-21 17:34:23 - issues channel

**Brøndby IF**

Hello guys, happy Saturday everyone!



When the market is finished it gives `WINNER` or `LOSER` _status_, but after some time if try to pull that market it no longer exists.



Is there a standard time that the market remains available with this _status_ before it is possible to collect only from Historical Data?

---

## 2022-05-09 18:59:36 - general channel

**John Foley**

Does anyone know of any APIs that have xG in their historical data offering? (aside from statsbomb or the likes targeting the big fish)

---

## 2022-05-09 16:30:17 - issues channel

**Aaron Smith**

if i see this correct you only need the streaming data? so basically what the flumine market recorder does?

---

## 2022-05-06 13:24:27 - general channel

**Peter**

I use them. Data quality is pretty good and they're super-responsive to corrections in their historic data.



I don't know what the delay is, but I would expect it to be somewhat variable depending on the speed of the feed the data analysts receive, how far ahead of the "live" broadcast they are receiving it, how much of the encoding is automated and how quickly specific analyst is able to encode the non-automated events. Overall however, I would expect it to be dwarfed by the impact of polling for new data.



I'm not aware of a mapping between Betfair team names and Sporting Monks. I've done that myself but found a fair number of inconsistencies in team names on the Betfair making, even in major competitions, rendering a mapping a bit problematic. My preference instead is to use fuzzy logic on the team names to find best matches. I've found that more reliable (i.e. less brittle).

---

## 2022-05-02 13:14:23 - issues channel

**John Foley**

So I’ve just twigged that “last traded price” in the historical data (basic files) is not what I thought it was…

1. If I want to see what the best available prices were available at a given timestamp, then I actually need the “Best Available to Back/Lay” fields, is that correct?

2. Seeing now that these are only available in Advanced/Pro files. I was wondering if anyone could share any thoughts on reliability of the advanced files for backtesting? If I’m looking to see what prices were available at a given timestamp (to the nearest minute is fine), is the advanced data good enough? Just interested to hear about others experiences before I go making any bulk purchases

3. I’ve found the basic files can sometimes be missing random events. E.g. a race meeting with 7 races but the basic data seems to only have the win market for 4 of them, stuff like that. Is this a known trait of the basic data? Are the gaps filled in for advanced/pro?



---

## 2022-05-01 23:11:24 - random channel

**LM**

Does anyone know if data from the racecard endpoint is only provided for a limited period. I'm trying to get historical data for Jan this year and I'm not getting anything returned?

---

## 2022-04-29 08:34:42 - general channel

**liam**

Yeah, was talking to Rob about adding a getattr to allow `market_book.market_id` and `market_book["marketId"]`



There is then the question of how its added, does it become the default? Or used when installed? Or do we drop down into bflw as the default for processing historical data?

---

## 2022-04-19 08:11:41 - strategies channel

**liam**

Betfair event file is from the historical data, it is basically all markets for an event in a single file. You can replicate this by appending all the markets you want to process into a single file (order doesn't matter) flumine will then process chronologically with markets available as per the code above assuming `event_processing` is True



[https://betcode-org.github.io/flumine/quickstart/#event-processing](https://betcode-org.github.io/flumine/quickstart/#event-processing)

---

## 2022-03-30 16:37:47 - betfair-news channel

**Neil T (Betfair)**

Yes, its off the roadmap, the main priorities are further feed integrations, passive bets work.  There's too much cross over with historical data sales and again, hard to determine real benefits

---

## 2022-03-30 16:32:39 - betfair-news channel

**liam**

I assume it's now completely off the roadmap? I imagine it has an overlap with the historical data sales.



I have been thinking about adding the private graphs endpoint to bflw, will that cause any 'issues'?

---

## 2022-03-30 16:26:59 - betfair-news channel

**Neil T (Betfair)**

Hi [@U4H19D1D2](@U4H19D1D2) - this was on the roadmap several years ago and we got fairly close to doing it before it was de-prioritized in favor of other projects.  There was also subsequent conflict between offering this as a service and a separate historical data service post settlement.

---

## 2022-03-30 12:35:34 - issues channel

**Javier Martín Pérez**

I guess than in a similar fashion to your mapping I could get the data from the historical data but that will take a while :disappointed: . Thanks for the help!

---

## 2022-03-29 17:37:23 - betfair-news channel

**Alessio**

From my point of view, and I believe i'm not the only one, I think the most useful historical data stretches up to 2-3 years in the past., not more

---

## 2022-03-29 16:44:58 - betfair-news channel

**Neil T (Betfair)**

When we initially launched the service back in 2017 data for all Exchanges (.com, .it and .es) was recorded and packaged as part of each monthly file on [https://historicdata.betfair.com/](https://historicdata.betfair.com/). However, due to time constraints, a dedicated historical data site for Spain and Italy was out of scope. The .es and .it data was subsequently purged from the existing published files to reduce complexity and the overall size of the stored files.

---

## 2022-03-29 13:44:43 - betfair-news channel

**Alessio**

Is there any chance we'll get to enable buying historical data on regional exchanges like the Italian one?

---

## 2022-03-29 12:09:41 - betfair-news channel

**Neil T (Betfair)**

Hi [@UBS7QANF3](@UBS7QANF3),  yes, we can get something added to the historical data dev backlog for this.

---

## 2022-03-11 14:20:15 - issues channel

**Paul**

Possibly stupid question: is it possible to use the DataStream and `process_raw_data` with data recorded with the market recorder? I tried to throw it in there to debug something around what I'm doing in `process_market_book` and it didn't seem to fire.

---

## 2022-03-07 19:31:31 - issues channel

**Ruben**

where are you seeing these files? I don't think my market recorder creates them

---

## 2022-02-17 22:24:33 - issues channel

**Aaron Smith**

Lately my market_recorder is throwing some of those bois below over the day. Often times the market_recorder fails to put the market files into the s3 bucket (at any step, all i know for now is they are not in the bucket at the end of the day). For a single day/run cycle of the market recorder, either all or none of markets that have orders in them makes it into the bucket. Anyone having an idea whats going on here?

```{"asctime": "2022-02-16 19:08:14,104", "levelname": "ERROR", "message": "_get_cleared_market error", "exc_info": "Traceback (most recent call last):

  File \"/path/prod_market_recorder/venv/lib/python3.10/site-packages/flumine/worker.py\", line 230, in _get_cleared_market

    cleared_markets = betting_client.betting.list_cleared_orders(

  File \"/path/prod_market_recorder/venv/lib/python3.10/site-packages/betfairlightweight/endpoints/betting.py\", line 434, in list_cleared_orders

    (response, response_json, elapsed_time) = self.request(method, params, session)

  File \"/path/prod_market_recorder/venv/lib/python3.10/site-packages/betfairlightweight/endpoints/baseendpoint.py\", line 55, in request

    self._error_handler(response_json, method, params)

  File \"/path/prod_market_recorder/venv/lib/python3.10/site-packages/betfairlightweight/endpoints/baseendpoint.py\", line 81, in _error_handler

    raise self._error(response, method, params)

betfairlightweight.exceptions.APIError: SportsAPING/v1.0/listClearedOrders \nParams: {'betStatus': 'SETTLED', 'marketIds': ['1.194823061'], 'customerStrategyRefs': ['ip-xxx-xx-xx-x'], 'settledDateRange': {'from': None, 'to': None}, 'groupBy': 'MARKET'} 

Exception: None 

Error: {'code': -32099, 'message': 'ANGX-0006', 'data': {'APINGException': {'requestUUID': 'ie2-ang30b-prd-02011018-001f0d3c34', 'errorCode': 'UNEXPECTED_ERROR', 'errorDetails': ''}, 'exceptionname': 'APINGException'}} 

Full Response: {'jsonrpc': '2.0', 'error': {'code': -32099, 'message': 'ANGX-0006', 'data': {'APINGException': {'requestUUID': 'ie2-ang30b-prd-02011018-001f0d3c34', 'errorCode': 'UNEXPECTED_ERROR', 'errorDetails': ''}, 'exceptionname': 'APINGException'}}, 'id': 1}", "trading_function": "list_cleared_orders", "response": "SportsAPING/v1.0/listClearedOrders 

Params: {'betStatus': 'SETTLED', 'marketIds': ['1.194823061'], 'customerStrategyRefs': ['ip-xxx-xx-xx-x'], 'settledDateRange': {'from': None, 'to': None}, 'groupBy': 'MARKET'} 

Exception: None 

Error: {'code': -32099, 'message': 'ANGX-0006', 'data': {'APINGException': {'requestUUID': 'ie2-ang30b-prd-02011018-001f0d3c34', 'errorCode': 'UNEXPECTED_ERROR', 'errorDetails': ''}, 'exceptionname': 'APINGException'}} 

Full Response: {'jsonrpc': '2.0', 'error': {'code': -32099, 'message': 'ANGX-0006', 'data': {'APINGException': {'requestUUID': 'ie2-ang30b-prd-02011018-001f0d3c34', 'errorCode': 'UNEXPECTED_ERROR', 'errorDetails': ''}, 'exceptionname': 'APINGException'}}, 'id': 1}"}```

---

## 2022-02-15 11:07:59 - random channel

**Oliver Varney**

Is the structure of the market book identical in this library? I have to run a full batch of files through a process and grab some basic data, so im just looking to cut down time where possible. Im along way off 6 markets a second with bflw even with traded volume recalced turned off. Although im using betfairutils package directly

---

## 2022-02-11 10:09:57 - random channel

**Oliver Varney**

With the market recorder do people recorder all horse racing with one process? what do poeple market_filter look like? is it too heavy to do it all in one or not really anything to worry about?

---

## 2022-02-09 08:41:04 - general channel

**liam**

Bflw will output historical data as per a normal marketBook request / stream

---

## 2022-02-08 20:40:41 - general channel

**liam**

Certainly recommend streaming, much lighter on CPU and reduces the complication. 



What issues are you seeing the historical data? Thought the pro stuff was good.



flumine can do whatever you want, the selling point is the switch to backtest / paper / live with no changes to your code.  Switching wouldn’t make sense depending on how advanced your current setup is and/or you want some of the features. 

---

## 2022-02-08 20:17:35 - general channel

**Dan Q**

Hey, just wanted to share my process and do a quick sanity check since I'm not super familliar with BFLW/Flumine. This is my process right now:

• Container on AWS ECS recording Betfair odds data every 5 seconds - using the API via BFLW - for the markets I'm interested in (NBA) and writing to a DB

• Model trained on historical data from Betfair pro files (lots of cleaning/processing as there are very weird behaviors in the historicals that don't reflect the live environment)

    ◦ All historical reading and treatment done with code I wrote myself, no BFLW here

• External data read from other sources and also fed into a DB. Historicals are used along with BF historicals to train the model.

• Live, constantly running betting bot reads the most recent data from the DB for live games joined with external data, manipulates it to the format the model expects, and makes a decision based on model output and strategy parameters

    ◦ Again a custom class/process, BFLW used only to connect to the API to collect bankroll info and place orders

• If bet decision is made, sends a fill or kill limit order through BFLW client

• Strategy parameters are determined through intensive backtesting/bootstrapping on the live data collected so far

    ◦ Also a custom backtesting suite I wrote to calculate expected profitability and other stats over n games in the season based on resampling previous games

This is working well and is thankfully profitable so far, but I feel like I may have reinvented the wheel at least five times during the whole thing considering BFLW/Flumine exists. I've seen a lot of mention of backtesting on Flumine, would it also allow more complex operations like I described with using external data and output from a model? What is the benefit of doing so vs. the solution I've described? One thing I'm not doing which I know I could be is streaming and recording the data instead of the 5-second snapshots I'm using right now, but so far it's served me well and I haven't seen a reason to switch.

---

## 2022-02-08 11:02:40 - general channel

**Nacho Uve**

How can I filter a historical data stream by a specific marketType?

---

## 2022-02-04 16:45:04 - general channel

**Nacho Uve**

Hello,



I am starting with bf exchange bots for soccer. At this initial point with a very limited budget, I have to work with BF BASIC PLAN and streams that I have recorded (a ridiculous amount, :/  ).



So, I would like to do backtesting with historical data of the BASIC PLAN, but it does not include "atb/atl", just "ltp".

I think it could be a good idea to transform "ltp" of each runner into a some kind of "atb" and "atl" (like it was the best price). I think it can match the needs of my simple test strategies.



Do you think it makes any sense? What would be the best approach to do it(a middleware, a custom FlumineBacktest class, a custom FlumineMarketStream?

---

## 2022-02-04 10:42:47 - general channel

**Chris H**

Question, does anyone have any data for betfair which contains mappings of football event id's to competition ids for past events they would be willing to share?



I have historical data since Dec 2019 and there does not seem to be a way to get the competition id from the api, and trying to join everything up via the event/runner names sounds... not fun :sweat_smile:

---

## 2022-01-30 23:00:33 - general channel

**Techno**

So, how do you all handle price reductions in horse races when a horse is a non-runner? Those aren't prices people have taken, they're prices reduced by Betfair. I am looking at the historical data and it seems like a lot of the races have price reductions.

---

## 2022-01-25 08:42:07 - general channel

**Nacho Uve**

Hello,



I can not download any historical data from [http://historicdata.betfair.com|historicdata.betfair.com](http://historicdata.betfair.com|historicdata.betfair.com). Unfortunately this service is not available to customers in some countries.

I'm interesting in historical soccer data to start to try flumine strategies.



Could someone who already has these files share them?

Are there any alternative link with historical files to download?



Thank you very much!

---

## 2022-01-24 22:36:47 - general channel

**Techno**

Hi guys. I have noticed on the historical data, there are prices (odds) taken that aren't on the betfair exchange, Like 3.47 and 4.68 etc.  How are these figures calculated? Are they average odds or something? Thanks.

---

## 2022-01-19 17:31:14 - strategies channel

**Lee**

i think the market recorder takes the last cached catalogue at the time of market save/upload

---

## 2022-01-16 18:16:05 - general channel

**NC**

```UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 581: character maps to &lt;undefined&gt;```

I'm encountering this error when trying to stream the historical data from a file on disk. I've copied the code from examplestreaminghistorical.py and changed the file_path for the historical stream, to that of my .bz2 file (also tried for .tar with similar result). I guess I've misunderstood something. Any ideas?

---

## 2022-01-16 14:17:26 - general channel

**NC**

Can someone help or direct me to some python code that will read the .bz2 or .tar files from the betfair historical data and put it into a nice tabular format, ready for a simple csv? I have all the bz2/tar files on my hard drive aleady. thanks in advance

---

## 2022-01-16 05:45:03 - general channel

**Colin**

Does anyone have any experience with developing their own bot and using it with a stake that is below the default minimum amount in your region/country for a prolonged period of time and for betting types that were not classed as closing out? If so, did you receive a warning from Betfair quite swiftly?

I note the 4th bullet point here, [https://developer.betfair.com/en/exchange-api/faq/](https://developer.betfair.com/en/exchange-api/faq/)

I'm keen to production-ise my bot soon, but I also want to start slow given it is not feasible for me to use Betfair's historical data to back test the algorithm I am using.

---

## 2022-01-15 11:52:28 - random channel

**liam**

Market recorders actually use different stream types so no benefit when sharing an instance, hence recommendation to use separate 

---

## 2022-01-15 09:30:23 - random channel

**Newbie99**

Apologies as this is a bit open ended, but I'm not understanding what went wrong here, last night around 1 am, out of (seemingly) no-where it looks like I suddenly got latency warnings and then eventually the process killed:



```{"asctime": "2022-01-15 01:00:05,664", "levelname": "INFO", "message": "Placing new LAY order for runner ('Jaime Jamel', 35971913, 0), runner exposure is: {'selection_id': 35971913, 'handicap': 0, 'if_win': 0.539, 'runner_matched_stake': 0.0, 'runner_matched_exposure': 0.0, 'min_market_exposure': -18.509999999999998} and limit is: 0.3."}

{"asctime": "2022-01-15 01:00:05,664", "levelname": "INFO", "message": "Order status update: Pending", "market_id": "1.193372878", "selection_id": 35971913, "handicap": 0, "id": "138615012056645370", "customer_order_ref": "7c44d7544ce40O138615012056645370", "bet_id": null, "date_time_created": "2022-01-15 01:00:05.664573", "publish_time": "2022-01-15 01:00:05.647000", "market_version": null, "async": false, "trade": {"id": "7a2c3bee-759e-11ec-b096-02054918c7c6", "strategy": "betting_market_lay", "place_reset_seconds": 0.0, "reset_seconds": 0.0, "orders": ["138615012056645370"], "offset_orders": [], "notes": "R3 5f Allw,2022-01-15 01:02:00,WIN,Flat,US,Charles Town,False,False,None,False,Jaime Jamel,2.64,2479.75,8,1,False,None,0,Charles Town (US) 14th Jan,31175177,7,{'strategy_name': 'betting_market_lay', 'selection_id': 35971913, 'handicap': 0, 'price_percentage': 0.768, 'min_valid_external_value': 0.8, 'current_back_price': 48, 'current_mid_price': 56.5, 'current_lay_price': 65, 'previous_back_price': 50, 'previous_mid_price': 62.5, 'previous_lay_price': 75},1", "market_notes": null, "status": "Live", "status_log": ""}, "order_type": {"order_type": "Limit", "price": 50.0, "size": 0.31, "persistence_type": "LAPSE", "time_in_force": null, "min_fill_size": null, "bet_target_type": null, "bet_target_size": null}, "info": {"side": "LAY", "size_matched": 0.0, "size_remaining": 0.31, "size_cancelled": 0.0, "size_lapsed": 0.0, "size_voided": 0.0, "average_price_matched": 0.0}, "responses": {"date_time_placed": null, "elapsed_seconds_executable": null}, "runner_status": null, "status": "Pending", "status_log": "Pending", "violation_msg": null, "simulated": {"profit": 0.0, "piq": 0.0, "matched": []}, "notes": "R3 5f Allw,2022-01-15 01:02:00,WIN,Flat,US,Charles Town,False,False,None,False,Jaime Jamel,2.64,2479.75,8,1,False,None,0,Charles Town (US) 14th Jan,31175177,7,{'strategy_name': 'betting_market_lay', 'selection_id': 35971913, 'handicap': 0, 'price_percentage': 0.768, 'min_valid_external_value': 0.8, 'current_back_price': 48, 'current_mid_price': 56.5, 'current_lay_price': 65, 'previous_back_price': 50, 'previous_mid_price': 62.5, 'previous_lay_price': 75},1", "market_notes": null}

{"asctime": "2022-01-15 01:00:30,284", "levelname": "INFO", "message": "1.193373059: 0 cleared orders found, more available: False"}

{"asctime": "2022-01-15 01:01:13,244", "levelname": "WARNING", "message": "[FlumineStream: 4002]: Latency high: 0.9758524894714355"}

{"asctime": "2022-01-15 01:01:13,245", "levelname": "WARNING", "message": "[MarketStream: 3001]: Latency high: 0.9100987911224365"}

{"asctime": "2022-01-15 01:01:13,245", "levelname": "WARNING", "message": "[MarketStream: 2001]: Latency high: 0.8022336959838867"}

{"asctime": "2022-01-15 01:12:41,802", "levelname": "INFO", "message": "Deleting requests.Session", "sessions_created": 36, "session": "&lt;requests.sessions.Session object at 0x7f2c6a5195d0&gt;", "session_time_created": 1642208309.3769233, "session_time_returned": 1642208405.607362, "live_sessions_count": 1, "err": true}

{"asctime": "2022-01-15 01:12:41,813", "levelname": "WARNING", "message": "[MarketStream: 3001]: Latency high: 689.2287058830261"}

{"asctime": "2022-01-15 01:12:41,814", "levelname": "WARNING", "message": "[FlumineStream: 4002]: Latency high: 689.5181279182434"}

{"asctime": "2022-01-15 01:12:41,814", "levelname": "WARNING", "message": "[MarketStream: 2001]: Latency high: 689.121832370758"}```

The only change I've made (and so at this stage I'm assuming is the culprit) is to run the market recorder on my live instance, as opposed to my local test instance (previously I recorded locally and kept my live stuff separate), so I added this just before framework.run() on my live code in AWS:



```recorder = MarketRecorder(

            name="MR_horse_greyhounds",

            market_filter=streaming_market_filter(

                    event_type_ids=[7],

                    country_codes=['GB','IE','US','FR', 'AU'],

                    market_types=['WIN', 'PLACE', 'EACH_WAY'],

                ),

            stream_class=DataStream,

            context={

                "local_dir": ai.unprocessed_data,

                "bucket": "fluminetest",

                "force_update": False,

                "remove_file": True,

            },

        )



        framework.add_strategy(recorder)```

Am I potentially trying to record too much in one go and/or from the error am I somehow creating too many sessions (and if so how might I stop this)?



Again apologies for the open ended nature, I'm clearly not understanding something about sessions I feel!

---

## 2022-01-12 16:42:34 - general channel

**Stefan**

Of course if you work with historical data from different sources, you could have problems, but your question was about live data, right?

---

## 2022-01-09 18:28:57 - general channel

**S G**

I can see logs getting generated. However there are gaps. For ex: log rotation happens on 00:00AM. But the last log line is an hour earlier or something like that. I just want to make sure that recorder is ok. May be i could add a log line in the market recorder to log every 1 min.

---

## 2022-01-09 17:25:18 - general channel

**S G**

Hi All, I have got a market recorder setup with log rotation set to 1 day. However the logs arent written until midnight, this could be due to no activity or no info logs. Can I tell fulmine to write a log message every minute? something like a heart beat?

---

## 2021-12-22 19:42:41 - issues channel

**Paul**

Dumb question. Am I safe to assume if I'm seeing this when trying to use the market recorder example, I'm using a key for which streaming hasn't been enabled?

```ListenerError(self.listener.connection_id, received_data)\nbetfairlightweight.exceptions.ListenerError: connection_id: 206-221221193700-982041, data: {\"op\":\"status\",\"id\":1004,\"statusCode\":\"FAILURE\",\"errorCode\":\"NOT_AUTHORIZED\",\"errorMessage\":\"AppKey is not configured for service\",\"connectionClosed\":true,\"connectionId\":\"206-221221193700-982041\"}"}```



---

## 2021-12-22 17:19:04 - issues channel

**foxwood**

Ok - my bad - hadn't considered that it has to match the historical data files BF provide. Will just use a script to wrap files I want to view. Didn't know there was a lines-only standard - thanks for that :slightly_smiling_face:

---

## 2021-12-22 09:33:55 - general channel

**Techno**

Sorry, I mean what is trd named in the program. I can see trd in the data I have downloaded from Betfair. It is advanced data. For example ltp in Betfair historical data is named "runner.last_price_traded" in the examplestreaminghistorical.py file. What is trd named in the software please?

---

## 2021-12-22 06:57:26 - general channel

**Peter**

Are you using the free data? If so TRD data isn't included. Betfair's [https://historicdata.betfair.com/Betfair-Historical-Data-Feed-Specification.pdf|Betfair's historical data specification](https://historicdata.betfair.com/Betfair-Historical-Data-Feed-Specification.pdf|Betfair's historical data specification) shows what's included in each package. Page 4 is especially helpful for its table showing the differences.

---

## 2021-12-22 01:58:26 - general channel

**Techno**

I'm  editing the examplestreaminghistorical.py file in BFLW to output a little more data but I can't find the last traded value. The last_price_traded for each runner is already there, but where do I find the actual amount traded? I think it corresponds to the TRD value in the BF historical data file.

---

## 2021-12-21 16:22:26 - general channel

**Techno**

Hi Guys. I would like to download historical data only for Hcap races - but not novice or maiden handicaps. Is there a way to do that? Thanks.

---

## 2021-12-18 08:09:04 - general channel

**D**

Just to add another viewpoint to all the good advice above: I used RDS (postgres) for quite a while but it started to seem expensive, especially for historical data I was hardly ever querying. My current approach is to upload csv, parquet and json data to S3 locations and use Athena to query them into pandas dataframes. Don't have any issues so far; performance is good and I can add new data to my json files without breaking existing queries.

---

## 2021-12-14 10:36:46 - general channel

**Oliver Varney**

think there is also an example for the historical data which sounds like what your looking for also

---

## 2021-12-14 10:28:07 - general channel

**Techno**

Hi guys. I'm Elliot. Thanks for having me. To be honest, I'm very green when it comes to programming and I'm having trouble installing Betfairlightweight. I want to use it to parse the historical data, and have a spreadsheet or even a graph if possible of all the traded prices for horses until the start of the race. Thanks.

---

## 2021-12-09 01:34:32 - general channel

**NC**

Yes, completely agree. My expectations are quite low tbh, especially for the model based upon historical data, but I do think RL has a huge role to play to learn new ways to make money. From what I hear it's being used in the financial markets very successfully, and I would imagine something similar could be done on the sports exchange. Also the work that was done on chess, just shows how powerful it can be, outperforming all known engines to date. Anyway, needless to say it's a huge undertaking, but I hope either me or someone else here can make some big steps (if not already)

---

## 2021-12-09 01:05:36 - general channel

**Mr West**

Hey [@U02PKHL5W4F](@U02PKHL5W4F) your not the first and you won't be the last to think you can use ML &amp; historical data to make your fortune :moneybag: Good luck :crossed_fingers:

---

## 2021-12-08 23:51:22 - general channel

**NC**

My main avenue at the moment is building a successful ML model on historical data, and using RL to develop a profitable long term strategy to place bets. I'm confident this will be profitable but at a fairly low %. My secondary avenue will be to create a bot to use RL and make money through trades. My hunch is this will be much more complex but potentially much more lucrative. I get the point about narrowing down some potential strategies though.

---

## 2021-12-04 17:13:37 - general channel

**liam**

If it’s purchased data I think they are in the market_definition, if not record the catalogue (as per the market recorder example) and load them in with this [https://github.com/liampauling/flumine/blob/master/examples/middleware/marketcatalogue.py|middleware](https://github.com/liampauling/flumine/blob/master/examples/middleware/marketcatalogue.py|middleware) 

---

## 2021-12-03 06:25:03 - general channel

**Peter**

I'm a keep it simple kind of a guy, so even though the market recorder is very lightweight, I run it on it's own ec2 instance to remove any risk of interference. Or more accurately I run them (as I run five of them collect all the markets that interest me).

---

## 2021-12-02 21:20:18 - general channel

**TT**

How do people deploy the market recorder alongside strategies? My initial thoughts are to try and keep them separate but I can see a few options:

 - Deploy two separate ec2 instances (one for the market recorder and one for running strategies)

 - Use one ec2 instance but run 2 separate python processes

 - Use one instance and just add both the market recorder strategy to the framework alongside the other strategies



 How do other people approach this? And are there any other things to consider i.e latency/connection limit issues etc?

---

## 2021-11-24 16:38:27 - general channel

**Peter**

Easy to get confused about this. The market recorder used to store the data in zip archives, but fairly recently [@U4H19D1D2](@U4H19D1D2) converted it to save the data in gzips instead - a significant improvement in usability.

---

## 2021-11-16 22:11:51 - strategies channel

**Unknown**

Any ideas on how to extract goal scored information from the betfair historical data? I was wondering what your approaches are. Obv one could monitore the correct score market but are there any other more efficient approaches? What I try to achieve is deduct from the over 1.5 market the point a goal was scored. As you can see in the linked image it is obvious that the goal was scored after around 67min. However in the end you can also see some weird behavior where the odds drop and then return to a higher point. So what would be the best way to distinguish between those two scenarios in a less perfect odd plot.

---

## 2021-11-16 06:55:48 - general channel

**Paul**

Can I ask [@U013ZS16QJZ](@U013ZS16QJZ) - if you have something that works with bflw, what your objective in moving to flumine is? Is that you want to make use of paper trading, historical data stuff, etc.? If so, make that your end goal, don't worry about all the functionality and having a complete picture and just chip away towards your goal

---

## 2021-11-15 21:17:39 - issues channel

**C0rnyFlak3s**

I have a problem with the Historical API downloading my historical data. I am communicating via the requests lib in python and commands like ‘GetMyData’ or ‘GetCollectionOptions’ work fine, however once I try to run ‘DownloadListOfFiles’ with my filter as input the API returns with an error which is not specified. I am currently using the Delay Application Key and try to download free historical Data which I already “purchased” (in reality it was a free data set). Any ideas?

---

## 2021-11-11 10:15:00 - issues channel

**captainonionhead**

Morning, I have a market recorder based upon the flumine example.  It keeps receiving `INVALID_SESSION_INFORMATION` errors from the market-catalogue polling thread after it has been running for a while.

Is this expected - do I simply need to catch the exception and login again or is there something more fundamentally wrong with my setup?

Thanks!

---

## 2021-11-05 10:32:58 - strategies channel

**Adrian**

that would be awesome! i was just about to ask how you extract the data from the stream/historical data

---

## 2021-11-05 09:14:30 - strategies channel

**Adrian**

What's the best way to analyse market data? Is there a separate program or something? How would one even start to analyse the historical data?

---

## 2021-11-04 17:13:38 - general channel

**C0rnyFlak3s**

So according to [@U01NJ85MP7F](@U01NJ85MP7F) there may be issues if I only fetch streaming data without trading in the markets for a longer period of time? What will happen in the case I stream data for multiple days to create my own historical data? Is this unwanted behavior by the betting exchange, and what will happen if I do so? Answers are greatly appreciated before I finally start my data stream :slightly_smiling_face:

---

## 2021-11-01 12:43:06 - random channel

**Mick**

Roughly you could say that most horse races are run at a comfortable pace with all the horses clustered together, then when they reach the last couple of furlongs they will sprint for the line and only then do the gaps between horses open up. Occasionally however, races are run where one or two horses will apply pressure much earlier on and the race will become strung out and the final gaps between horses will end up much larger than would normally be the case. What I want to do is be able to determine how strung out a race was early on, from historical data. I dare say it may be revealed by sectional times but they are only available for a few racecourses. So is there some other clue in data I could download/scrape/purchase? Perhaps in-running odds at the half way point?

---

## 2021-10-24 18:35:27 - strategies channel

**Amit Patel**

its one of the free horse racings files from betfairs historical data site, 29717254 from 1st May 2020

---

## 2021-10-23 10:01:00 - strategies channel

**Adrian**

Thanks Oliver. I don't really know how to approach historical data analysis. My only skill right now is backtesting, then iterating the backtest for better performance. THere must be a way to make it work

---

## 2021-10-21 23:32:51 - strategies channel

**Adrian**

I should have been more specific - do you analyse historical data separately from backtesting? I know how to backtest. I just dont really know how to approach the historical data.

I guess I'm just looking for a more reliable approach to what I've been doing, which is identify a strategy (from observed market behaviour), backtest, adjust parameters, validate.

So far the validations have fallen down. So I have a more fundamental issue.

Liam said start with a known strategy and adjust to make it work. So how does historical data analysis work with that? It's not just adjusting the backtest, right?

---

## 2021-10-19 13:05:08 - general channel

**Alessio**

ah yes, i guess they also cost non trivial amount of money. in this case it's enough for me because it's a lot of historical data and my algorithm is not too sensitive around there (getting goals is basically 'state change', and that's it).

---

## 2021-10-16 08:05:40 - random channel

**Paul**

For example, you might start with “identify a profitable trading strategy for horse racing markets 2 minutes before official start time” (which is tough enough already). To do that you will need to:

• Download historical data

• Understand it, perhaps do some cleaning and so on

• Get it into a format that you can use for your strategy building

• Run some tests

• Visualise the test results

…

---

## 2021-09-28 13:17:32 - general channel

**JC**

Hi everyone, I've been running an old version of the S3 Market Recorder and am trying to convert all of my old recorded zip files to gzip on S3. EC2 bash script seems like potentially the best option, but will need a larger instance as inflating and zipping takes ages. Anyone had any experience with this or got an easy/serverless way to do it? Cheers, Joe

---

## 2021-09-19 09:21:58 - issues channel

**Mo**

[@U016TGY3676](@U016TGY3676) have you make any modifications to the market recorder example?

---

## 2021-09-08 13:33:16 - issues channel

**Mons___das**

As i am testing a lot of stuff (and surely not always following best practice :grimacing: ), the market recorder has been terminated rather frequently. Could this lead to files being left there ?

---

## 2021-09-08 13:09:35 - issues channel

**Peter**

That's the where the market recorder keeps the data, executes the compression and from where it will upload the files when finished. There are two parameters that you can pass into the market recorder: "remove_file" and "remove_gz_file" which by default are set to False. To stop these /tmp subfolders from growing until you run out of disk, you're going to want to set them to True when you start the recorder. For example:



`strategy = S3MarketRecorder(`

    `name="Golf Market Recorder",`

    `market_filter=betfairlightweight.filters.streaming_market_filter(`

        `event_type_ids=["3"],`

    `),`

    `stream_class=DataStream,`

    `context={`

        `"local_dir": "/tmp",`

        `"bucket": "*************",`

        `"force_update": True,`

        `"remove_file": True,`

        `"remove_gz_file": True,`

    `},`

`)`

---

## 2021-09-05 22:35:15 - general channel

**Jeff Waters**

I've tried to add filters to only include British races and win races (based on filters used in the the example code at [https://github.com/liampauling/flumine](https://github.com/liampauling/flumine)):



```strategy = TestStrategy(

    market_filter={"markets": marketsToProcess},

    country_codes=["GB"],

    market_types=["WIN"],

    max_order_exposure=1000,

    max_selection_exposure=105,

)```

However, I got an error message:



*TypeError: __init__() got an unexpected keyword argument 'country_codes'*



Presumably, that was because I wasn't using market_filter=streaming_market_filter, as in the example (as I was using historical data rather than live data).



Is there any way of filtering out particular types of races when using historical data, other than putting something like

```if market.country_code != "GB":

    continue```

in the process_market_book method?



Thanks



Jeff

---

## 2021-09-05 15:52:47 - general channel

**Jeff Waters**

I've just purchased some historical data from Betfair containing thousands of JSON files. What I've done previously is to manually extract some of the files to a folder called 'Data', and then go:



*from os import listdir*

*from os.path import isfile, join*



*markets = [f for f in listdir('Data') if isfile(join('Data', f))]*

*for i in range(len(markets)):*

    *markets[i] = "Data/" + markets[i]*



*strategy = TestStrategy(*

    *market_filter={"markets": markets},*

*)*

*framework.add_strategy(strategy)*

*framework.run()*



However, that approach isn't viable when there are thousands of files in different folders in a WINRAR file. I've been told I can use match.patch:



*with mock.patch("builtins.open", smart_open.open):*

    *framework.add_strategy(strat)*

    *framework.run()*



However, where do I put the name and path of the tar file? Alternatively, is there a program that extracts all the JSON files to a single folder?



Thanks



Jeff

---

## 2021-09-01 06:58:25 - general channel

**Adrian**

Thanks Peter. It's quite interesting how that works. I don't fully understand it but that makes sense not to pass them in in the first place. My problem is I started the market recorder a couple months back without sorting the market types into separate folders, so I'll have to create some kind of script that creates a list of the needed markets. Or that sorts them into correct folders them

---

## 2021-08-25 18:53:28 - general channel

**azevedo**

As with regards to if it's giving a specific problem, it isn't really. I was just curious about these warnings I'm getting and if that could somehow have any data quality implications down the line.

---

## 2021-08-24 19:22:08 - general channel

**azevedo**

hey guys. testing the flumine market recorder on greyhounds. getting quite a few messages come through after more than an hour after market initially closed. seems to be mostly on FORECAST markets. I've investigated a few manually. Examples messages for one market below. If you have some editor like VS code to compare the two messages, you'll see that the only difference is the "pt" timestamp and that the latter message has "img": true attached to it. Everything else is the same. Any idea why this might be happing? there is of course the "force_update" field for this sort of thing, but seems that too many of these update are just the same initial closure. (no issue on the Flumine side, rather why Betfair might be doing this? and how are people setting the "force_update" and "market_expiration" parameters to tackle these sort of things?



```Initial closure message

{"op": "mcm", "clk": null, "pt": 1629820207534, "mc": [{"id": "1.186741004", "marketDefinition": {"bspMarket": false, "turnInPlayEnabled": false, "persistenceEnabled": false, "marketBaseRate": 5, "eventId": "30826229", "eventTypeId": "4339", "numberOfWinners": 1, "bettingType": "ODDS", "marketType": "FORECAST", "marketTime": "2021-08-24T15:48:00.000Z", "suspendTime": "2021-08-24T15:48:00.000Z", "bspReconciled": false, "complete": true, "inPlay": false, "crossMatching": false, "runnersVoidable": false, "numberOfActiveRunners": 0, "betDelay": 0, "status": "CLOSED", "settledTime": "2021-08-24T15:50:02.000Z", "runners": [{"status": "LOSER", "sortPriority": 1, "id": 38255840}, {"status": "LOSER", "sortPriority": 2, "id": 38255841}, {"status": "LOSER", "sortPriority": 3, "id": 38255842}, {"status": "LOSER", "sortPriority": 4, "id": 38255843}, {"status": "LOSER", "sortPriority": 5, "id": 38255844}, {"status": "LOSER", "sortPriority": 6, "id": 38255846}, {"status": "LOSER", "sortPriority": 7, "id": 38255847}, {"status": "LOSER", "sortPriority": 8, "id": 38255848}, {"status": "LOSER", "sortPriority": 9, "id": 38255849}, {"status": "LOSER", "sortPriority": 10, "id": 38255850}, {"status": "LOSER", "sortPriority": 11, "id": 38255852}, {"status": "LOSER", "sortPriority": 12, "id": 38255853}, {"status": "LOSER", "sortPriority": 13, "id": 38255854}, {"status": "LOSER", "sortPriority": 14, "id": 38255855}, {"status": "LOSER", "sortPriority": 15, "id": 38255856}, {"status": "LOSER", "sortPriority": 16, "id": 38255858}, {"status": "LOSER", "sortPriority": 17, "id": 38255859}, {"status": "LOSER", "sortPriority": 18, "id": 38255860}, {"status": "LOSER", "sortPriority": 19, "id": 38255861}, {"status": "LOSER", "sortPriority": 20, "id": 38255862}, {"status": "LOSER", "sortPriority": 21, "id": 38255864}, {"status": "LOSER", "sortPriority": 22, "id": 38255865}, {"status": "LOSER", "sortPriority": 23, "id": 38255866}, {"status": "WINNER", "sortPriority": 24, "id": 38255867}, {"status": "LOSER", "sortPriority": 25, "id": 38255868}, {"status": "LOSER", "sortPriority": 26, "id": 38255870}, {"status": "LOSER", "sortPriority": 27, "id": 38255871}, {"status": "LOSER", "sortPriority": 28, "id": 38255872}, {"status": "LOSER", "sortPriority": 29, "id": 38255873}, {"status": "LOSER", "sortPriority": 30, "id": 38255874}], "regulators": ["MR_INT"], "venue": "Hove", "countryCode": "GB", "discountAllowed": true, "timezone": "Europe/London", "openDate": "2021-08-24T12:57:00.000Z", "version": 3988988530, "priceLadderDefinition": {"type": "CLASSIC"}}, "_stream_id": 2001}]}



Another message after more than an hour after closure

{"op": "mcm", "clk": null, "pt": 1629825468969, "mc": [{"id": "1.186741004", "marketDefinition": {"bspMarket": false, "turnInPlayEnabled": false, "persistenceEnabled": false, "marketBaseRate": 5, "eventId": "30826229", "eventTypeId": "4339", "numberOfWinners": 1, "bettingType": "ODDS", "marketType": "FORECAST", "marketTime": "2021-08-24T15:48:00.000Z", "suspendTime": "2021-08-24T15:48:00.000Z", "bspReconciled": false, "complete": true, "inPlay": false, "crossMatching": false, "runnersVoidable": false, "numberOfActiveRunners": 0, "betDelay": 0, "status": "CLOSED", "settledTime": "2021-08-24T15:50:02.000Z", "runners": [{"status": "LOSER", "sortPriority": 1, "id": 38255840}, {"status": "LOSER", "sortPriority": 2, "id": 38255841}, {"status": "LOSER", "sortPriority": 3, "id": 38255842}, {"status": "LOSER", "sortPriority": 4, "id": 38255843}, {"status": "LOSER", "sortPriority": 5, "id": 38255844}, {"status": "LOSER", "sortPriority": 6, "id": 38255846}, {"status": "LOSER", "sortPriority": 7, "id": 38255847}, {"status": "LOSER", "sortPriority": 8, "id": 38255848}, {"status": "LOSER", "sortPriority": 9, "id": 38255849}, {"status": "LOSER", "sortPriority": 10, "id": 38255850}, {"status": "LOSER", "sortPriority": 11, "id": 38255852}, {"status": "LOSER", "sortPriority": 12, "id": 38255853}, {"status": "LOSER", "sortPriority": 13, "id": 38255854}, {"status": "LOSER", "sortPriority": 14, "id": 38255855}, {"status": "LOSER", "sortPriority": 15, "id": 38255856}, {"status": "LOSER", "sortPriority": 16, "id": 38255858}, {"status": "LOSER", "sortPriority": 17, "id": 38255859}, {"status": "LOSER", "sortPriority": 18, "id": 38255860}, {"status": "LOSER", "sortPriority": 19, "id": 38255861}, {"status": "LOSER", "sortPriority": 20, "id": 38255862}, {"status": "LOSER", "sortPriority": 21, "id": 38255864}, {"status": "LOSER", "sortPriority": 22, "id": 38255865}, {"status": "LOSER", "sortPriority": 23, "id": 38255866}, {"status": "WINNER", "sortPriority": 24, "id": 38255867}, {"status": "LOSER", "sortPriority": 25, "id": 38255868}, {"status": "LOSER", "sortPriority": 26, "id": 38255870}, {"status": "LOSER", "sortPriority": 27, "id": 38255871}, {"status": "LOSER", "sortPriority": 28, "id": 38255872}, {"status": "LOSER", "sortPriority": 29, "id": 38255873}, {"status": "LOSER", "sortPriority": 30, "id": 38255874}], "regulators": ["MR_INT"], "venue": "Hove", "countryCode": "GB", "discountAllowed": true, "timezone": "Europe/London", "openDate": "2021-08-24T12:57:00.000Z", "version": 3988988530, "priceLadderDefinition": {"type": "CLASSIC"}}, "img": true, "_stream_id": 2001}]}```

---

## 2021-08-21 20:02:32 - issues channel

**Jeff Waters**

I've created a backtest script for historical data: [https://github.com/JeffW12345/betfair-backtester](https://github.com/JeffW12345/betfair-backtester).



My file returned zero profit for every single market, so to test if it was working I've added 'print(len(market.blotter))' to line 43 of runbacktests.py. It gives a blotter list length of zero for every market, suggesting that nothing is being added to the blotter.



Could someone take a look and tell me where I'm going wrong, please?

---

## 2021-08-21 15:13:04 - strategies channel

**S G**

since I started market recorder more events turned in-play, but market recorder didnt automatically subscribe to new events

---

## 2021-08-21 15:12:44 - strategies channel

**S G**

I have started market recorder for tennis, but this is only getting updates on 3 markets

---

## 2021-08-19 18:56:09 - general channel

**Peter**

I achieve this by limiting both country and market types e.g.



```MAJOR = [

    "GB", # Great Britain

    'DE', # Germany

    'ES', # Spain

    'FR', # France

    'IT', # Italy

   ]



MINOR = [

    'BE', # Belgium

    'CH', # Switzerland

    'DK', # Denmark

    'FI', # Finland

    'GR', # Greece

    'IR', # Ireland

    'NL', # Netherlands

    'NO', # Norway

    'PL', # Poland

    'PT', # Portugal

    'RO', # Romania

    'RU', # Russia

    'SE', # Sweden

    'TR', # Turkey

    'AR', # Argentina

    'BR', # Brazil

    'MX', # Mexico

    'US', # United States

    'AU', # Australia

    'CN', # China

    'JP', # Japan

]



MARKET_TYPES =  ['MATCH_ODDS', 'HALF_TIME', 'CORRECT_SCORE', 'HALF_TIME_SCORE', 'BOTH_TEAMS_TO_SCORE', 'OVER_UNDER_15', 'OVER_UNDER_25', 'OVER_UNDER_35']



strategy = S3MarketRecorder(

    name="Minor Soccer Market Recorder",

    market_filter=betfairlightweight.filters.streaming_market_filter(

        event_type_ids=["1"],

        country_codes=MINOR,

        market_types=MARKET_TYPES,

    ),

    stream_class=DataStream,

    context={

        "local_dir": "/tmp",

        "bucket": "betfair-flumine",

        "force_update": False,

        "remove_file": True,

    },

)```



---

## 2021-08-18 02:29:47 - strategies channel

**Van**

[@U01S1VB9X9P](@U01S1VB9X9P) I am actually a CS nerd in general :wink: What I’m missing is statistical modelling and gambling theory - i.e how to go about converting historical data into a probability.

---

## 2021-08-16 13:17:41 - general channel

**Peter**

The market recorder does stream the data in order to record it. But I'd recommend streaming it again to process it into the form that works for your analysis, ad then again for your backtesting, and you'll almost certainly find yourself doing it over and over as you become more sophisticated and think of new approaches for the same markets, so it's really helpful to have a clean versio of the original data to keep going back to. Good luck.

---

## 2021-08-16 11:26:41 - strategies channel

**Mo**

However the flumine market recorder does it [https://betfairlightweight.slack.com/archives/C4HL6EZTQ/p1629066953248900](https://betfairlightweight.slack.com/archives/C4HL6EZTQ/p1629066953248900)

---

## 2021-08-16 07:05:55 - strategies channel

**S G**

Guys anyone has historical data in github or in a shared location? betfair seems to charge a fortune for a months worth of data with ms ticks

---

## 2021-08-15 11:57:25 - issues channel

**liam**

This problem is due to the historical data only so certainly wouldn’t remove the field, just needs to be handled correctly, likely to add a flag to the listener `shitty_betfair_data=False`

---

## 2021-08-15 07:28:20 - issues channel

**liam**

Can you create a GitHub issue? Needs to be handled although why they decided to do this for historical data is infuriating 

---

## 2021-08-15 04:55:41 - issues channel

**ThomasJ**

(I am running Flumine over Historical Data.)



Is the runner traded volume for live streaming different to historical data? I ask because this code `runner.total_matched = new_data["tv"]` in BFLW  `Class MarketBookCache &gt; def update_cache` seems to store only the traded volume at a single price (sometimes for more than 1 price) and not the accumulated volume for all price points.



In "Betfair Developer Program  Exchange API  Historical Data FAQ's - How is traded volume represented within the PRO Historical Data files?" ([https://support.developer.betfair.com/hc/en-us/articles/360002401937-How-is-traded-volume-represented-within-the-PRO-Historical-Data-files-|link](https://support.developer.betfair.com/hc/en-us/articles/360002401937-How-is-traded-volume-represented-within-the-PRO-Historical-Data-files-|link)) it explains that "The runner tv (“tv”) represents the cumulative traded amount at the last price traded (ltp) or cumulative amount of all ‘trd’ amounts in the update if multiple prices are included."



Anyway, regardless of the details of the calculation of `runner.total_matched`, at any point in time should not its value be equal to the sum of all volumes at all prices?



I am digging into this because in Flumine's `class RunnerAnalytics &gt; def _calculate_matched`, the code `return round(total_matched - prev_total_matched, 2)` seems to assume that `total_matched` is always increasing in value when it's not. Numerous times the returned value is a negative (and by large amounts as I recorded them) which is not possible in real life.

---

## 2021-08-12 10:28:01 - general channel

**ThomasJ**

I've been doing the Flumingo Tango and the Middleware step has my head in a complete spin. My dance partner is Ms Historical Data from the Backtest Lowestlayer school. :smile:



PART A

So a Trade/Order Package is created and placed in the backtest handler queue.

After the appropriate delay the code winds it's way down to `class Simulated &gt; def place &gt; elif available_to_lay &lt;= price` which is where the matched/not-matched decision is made.

If a match occurs then that order is not looked at again from a matching perspective. All good.



PART B

But if a match does not occur then that order has a size_remaining != 0 and Middleware takes an interest.

For every marketbook update, Middleware calculates RunnerAnalytics, and I will focus on 'traded'.

In `class RunnerAnalytics &gt; def _calculate_traded` the traded values are calculated as deltas compared to prior marketbook update (or empty {} if runner is not included in latest marketbook update).

After RunnerAnalytics, because `order.status == OrderStatus.EXECUTABLE` and `size_remaining != 0`, the code ends up in `class Simulated &gt; def _calculate_process_traded`, which is where I get totally bamboozled.



`_traded_size_ = _traded_size_ / 2`

        `if _self_._piq - _traded_size_ &lt; 0:`

            `size = _traded_size_ - _self_._piq`

            `size = round(min(_self_.size_remaining, size), 2)`

            `if size:`

`                _self_._update_matched(`

                    `[`

`                        _publish_time_,`

`                        _self_.order.order_type.price,`

                        `size,`

                    `]  # todo takes the worst price, i.e what was asked`

                `)`

`            _self_._piq = 0`

        `else:`

`            _self_._piq -= _traded_size_`

            `logger.debug(`

                `"Simulated order {0} PIQ: {1}".format(_self_.order.id, _self_._piq)`

            `)`



1. Why are unmatched orders not just left in the backtest handler queue to wait for a match, or of course killed after 2 secs?

2. No doubt there is a good answer for Q1 so can someone please explain how the trade deltas matching works in middleware.

---

## 2021-08-09 19:37:13 - issues channel

**liam**

Have you uncompressed the file or are you using something smart_open to read? But like Aaron has said the basic data is useless and you won’t be able to use all of flumines features 

---

## 2021-08-09 18:57:04 - issues channel

**Aaron Smith**

If i recall correctly, basic data doesnt have volume information, which would be needed for a backtest, so that would surely thorw some errors

---

## 2021-08-09 16:48:24 - general channel

**admiral**

Where does flumine get its historical data for backtests from? I thought it costs money

---

## 2021-08-08 11:49:36 - strategies channel

**Dave**

&gt;  would be great to see the results if you created two models, your normal one, then one including these and just set the stakes to minimum.

hmm yeah, or even a model including friendlies _only_ if I can source some more historical data as there are very few samples currently, or bring in some league-invariant features from other leagues and let it loose on small stakes.

---

## 2021-08-02 18:20:43 - general channel

**thambie1**

I don't use flumine myself, but this is the example market recorder: [https://github.com/liampauling/flumine/blob/master/examples/marketrecorder.py](https://github.com/liampauling/flumine/blob/master/examples/marketrecorder.py)

---

## 2021-07-23 07:20:18 - general channel

**Mo**

I'm also really confused by the reference to market recorder and real time but note that there is a `streaming_update` field on the MarketBook: [https://github.com/liampauling/betfair/blob/6991a6a51363bae5fe5940f647b5cf7a4e7113cb/betfairlightweight/resources/bettingresources.py#L566](https://github.com/liampauling/betfair/blob/6991a6a51363bae5fe5940f647b5cf7a4e7113cb/betfairlightweight/resources/bettingresources.py#L566). This contains the raw message

---

## 2021-07-23 06:18:31 - general channel

**Adrian**

does the market recorder cache the json messages and then bulk update the save file? Or does it update the save file every time? Reason I'm asking is if it's possible to use the raw json messages from betfair in real time or should we always be using runner_book/market_book?

---

## 2021-07-22 06:03:48 - issues channel

**Adrian**

ok got everythin down to just 2 flumine instances. one for market recorder one for strategies. alas, i am somehow ending up with 13 active connections and cannot reconnect. unless there is some way i can kill those old connections, there's literally nothing else I can do except get hosting in the UK

---

## 2021-07-21 09:13:52 - issues channel

**Adrian**

yes thanks, i've done that for the market recorders. i might just have to work at reducing everything down to 2 flumines and/or get uk server as suggested

---

## 2021-07-21 08:59:24 - issues channel

**Adrian**

One each for market recorder - horses and greyhounds. One each for the strategies ofthose markets

---

## 2021-07-18 11:51:13 - general channel

**Juha Kiili**

I'm trying to implement a custom "market recorder" in Flumine that also records the relevant `inplayservice` events (or status) and is back-testable for a strategy that also uses the `inplayservice` data?



How would you approach this on a high-level?



I apologize for the vague question, but I'm not quite in-depth with the codebase and need a push to the right direction.

---

## 2021-07-15 09:58:00 - strategies channel

**Adrian**

i could bring it up on the betfair website/api if it's available otherwise i have the market recorder going where it's captured

---

## 2021-07-07 17:24:41 - issues channel

**Peter**

The market recorder script provides you with two files per market. A stream file which shows how offered prices, traded prices and matched volumes evolved over the life of the market and a market catalogue which has the meta information that you'd need to decide which markets to feed into your back testing.

---

## 2021-07-07 16:56:07 - issues channel

**Mons___das**

Hey guys! I m rather new to flumine and am trying to wrap my head around everything. Amazing stuff from what i can see, big thanks to [@U4H19D1D2](@U4H19D1D2)

I am currently trying to build up a database with that i can do backtests and filter markets (for the backtest), and down the road maybe also track the orders i have placed per strategy. First step i wanted to get an idea of the general structure of how all of this is going to look like. I see flumine comes with a market_recorder (and an s3recorder on top) and a backtest function, so basically all i need is being provided, i just have to connect the puzzles pieces :smile: The s3recorder seems to throw out some zip files (1 per market), which i am supposed to store in a s3bucket. Are these the files i am supposed to feed into the backtest machinery? Assuming thats how its done, i need to know which files i throw into the backtest for a certain strategy, so i need a way to filter these markets. I was thinking that this one be one job of a database, which for example has basic information for each market_id, like what event_type it is, time of the event, runners, etcetc. How would i go about building such db? Can the market recorder also be used for this? or would i extract this info straight from the files in the s3 bucket?

---

## 2021-07-06 11:32:11 - general channel

**ThomasJ**

[@U4H19D1D2](@U4H19D1D2) No problem. I'm going over some [https://betfair-datascientists.github.io/historicData/jsonToCsvTutorial/#complete-code|code](https://betfair-datascientists.github.io/historicData/jsonToCsvTutorial/#complete-code|code) provided by Betfair in Oz that uses parts of BFLW to read historical data and new code to process it and write CSV. There is a section in the new code that seems to use 'spb' and 'spl' to calculate "calculating SP traded vol as smaller of back_stake_taken or (lay_liability_taken / (BSP - 1))" which I cannot fathom.

This is performed using Final market. The code was written by a BF employee so I guess it must have some significance.



For info the specific code in question is...



`# returning smaller of two numbers where min not 0`

`_def_ min_gr0(_a_: float, _b_: float) -&gt; float:`

    `if _a_ &lt;= 0:`

        `return _b_`

    `if _b_ &lt;= 0:`

        `return _a_`



    `return min(_a_, _b_)`



`postplay_traded = [ (`

            `r.last_price_traded,`

            `r.ex.traded_volume,`

            `# calculating SP traded vol as smaller of back_stake_taken or (lay_liability_taken / (BSP - 1))`        

            `min_gr0(`

                `next((pv.size for pv in r.sp.back_stake_taken if pv.size &gt; 0), 0),`

                `next((pv.size for pv in r.sp.lay_liability_taken if pv.size &gt; 0), 0)  / ((r.sp.actual_sp if type(r.sp.actual_sp) is float else 0) - 1)`

            `)`

        `) for r in postplay_market.runners ]`

---

## 2021-07-05 09:11:05 - general channel

**Adrian**

[@U4H19D1D2](@U4H19D1D2) I have investigated and it looks like your market recorder uses cumulative traded volume. Whereas the historical (pro) data from Betfair does not use cumulative values.

---

## 2021-07-05 08:50:14 - general channel

**Peter C**

I wasn't aware of this, what is the reason for not showing the virtual prices by default? I've been using the basic market recorder example from the flumine docs, is there any way to set virtualise=true to request the virtual prices for the recorder? Do I put this in streaming_market_data_filter?

---

## 2021-06-30 20:38:18 - random channel

**Dave**

Don't care about the historical data. Just want the merch. I am in.

---

## 2021-06-30 20:05:29 - random channel

**birchy**

Yeah, you've probably already got something in mind? Correct me if I'm wrong, but weren't you working on some sort of market re-player using historical data?

---

## 2021-06-26 11:47:40 - general channel

**birchy**

Question for the stats guys here...

So I want to build a preplay model in order to create my own prices/book using historical data for each runner. Let's say I have calculated a handful of feature probabilities for each runner and have also manually given those features a weighting. For example, one of the features may be the bookie price, to which I might give a weighting of 0.20.

I'm assuming that all of the features for each runner would somehow need to be combined to create a single probability, then the probability for each runner would need to be normalised to create a 100% book.

So my question is... in layman's terms, what's the best way to combine all of this independent data to create a final probability for each runner?

---

## 2021-06-24 11:12:24 - general channel

**Adrian**

ok got it! Thank you! I had to create a new py file in the same directory as my script and pasted the market recorder strategy code in there. phew! I am now seeing a stream of data coming through

---

## 2021-06-24 09:46:41 - general channel

**Adrian**

The market recorder is easy to understand. Thank you!

---

## 2021-06-24 09:41:23 - general channel

**Mo**

Both the Betfair historic prices files and those files recorded by the market recorder are in the same format: a sequence of messages in an identical format to what you receive when connected to the streaming API

---

## 2021-06-24 09:40:19 - general channel

**Mo**

Have you looked at the market recorder example? [https://github.com/liampauling/flumine/blob/master/examples/marketrecorder.py|https://github.com/liampauling/flumine/blob/master/examples/marketrecorder.py](https://github.com/liampauling/flumine/blob/master/examples/marketrecorder.py|https://github.com/liampauling/flumine/blob/master/examples/marketrecorder.py)

---

## 2021-06-24 09:20:28 - general channel

**Adrian**

Yes I've done that, using historical data. It was tricky, since the time intervals are not steady. But now i need live data

---

## 2021-06-24 09:18:57 - general channel

**liam**

So you would create your own strategy for that although recommend having some historical data for testing / prototyping 

---

## 2021-06-24 03:22:23 - general channel

**Adrian**

Hi it's me again. Just looking for some direction now that I can login. I've been working with historical data the last few months so if I can get the data in roughly the same format I'm golden. Wondering how does MarketRecorder output data and in what format? Also, what command should I use to call it? I'm thinking `framework.add_strategy(strategy)`  then point strategy at MarketRecorder? That way the parameters (country, event and type) are set via the strategy variable? TIA!

---

## 2021-06-11 07:19:59 - general channel

**VT**

Thanks but I know how the functionalities to consult markets and place bets work through the API, what I'm looking for now is to be able to manipulate the historical data of Betfair.

---

## 2021-06-11 05:37:27 - general channel

**VT**

Hi, I've been researching how I can get Betfair historical data to backtest, any tips on a good tutorial for beginners in Python? I would like to consult the live football game moneyline markets. I intend to consult the free Basic data, 1 minute intervals, I would like to convert the odds values ​​in each minute to a dataframe.

---

## 2021-06-04 10:58:45 - issues channel

**James McKenzie**

I removed the strategy that pushes to redis and just ran a market recorder. I got the following when scraping GB races:





```{"asctime": "2021-06-04 05:02:46,633", "levelname": "WARNING", "message": "_get_cleared_market StatusCodeError", "exc_info": "Traceback (most recent call last):\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages/flumine/worker.py\", line 228, in _get_cleared_market\n    cleared_markets = betting_client.betting.list_cleared_orders(\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages/betfairlightweight/endpoints/betting.py\", line 432, in list_cleared_orders\n    (response, response_json, elapsed_time) = self.request(method, params, session)\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages/betfairlightweight/endpoints/baseendpoint.py\", line 48, in request\n    check_status_code(response)\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages/betfairlightweight/utils.py\", line 34, in check_status_code\n    raise StatusCodeError(response.status_code)\nbetfairlightweight.exceptions.StatusCodeError: Status code error: 503", "trading_function": "list_cleared_orders", "response": "Status code error: 503"}

{"asctime": "2021-06-04 05:03:01,545", "levelname": "ERROR", "message": "get_account_details error", "exc_info": "Traceback (most recent call last):\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages/flumine/clients/betfairclient.py\", line 50, in _get_account_details\n    return self.betting_client.account.get_account_details()\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages/betfairlightweight/endpoints/account.py\", line 54, in get_account_details\n    (response, response_json, elapsed_time) = self.request(method, params, session)\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages/betfairlightweight/endpoints/baseendpoint.py\", line 48, in request\n    check_status_code(response)\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages/betfairlightweight/utils.py\", line 34, in check_status_code\n    raise StatusCodeError(response.status_code)\nbetfairlightweight.exceptions.StatusCodeError: Status code error: 503", "error": "Status code error: 503"}

{"asctime": "2021-06-04 05:03:02,638", "levelname": "ERROR", "message": "get_account_funds error", "exc_info": "Traceback (most recent call last):\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages/flumine/clients/betfairclient.py\", line 56, in _get_account_funds\n    return self.betting_client.account.get_account_funds()\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages/betfairlightweight/endpoints/account.py\", line 35, in get_account_funds\n    (response, response_json, elapsed_time) = self.request(method, params, session)\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages/betfairlightweight/endpoints/baseendpoint.py\", line 48, in request\n    check_status_code(response)\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages/betfairlightweight/utils.py\", line 34, in check_status_code\n    raise StatusCodeError(response.status_code)\nbetfairlightweight.exceptions.StatusCodeError: Status code error: 503", "error": "Status code error: 503"}```

the process is currently hanging

---

## 2021-05-25 12:25:52 - random channel

**Oliver Varney**

isnt it just a sad fact of gambling (edit: and anything where large sums of money are involved)? our model are build on historical data where it most likely occurred in a handful of matches and is already built in to our expected return? not that legitimises it at all

---

## 2021-05-22 15:05:34 - general channel

**PeterLe**

apologies for the very basic question again; If I wanted to set the market recorder to only record the inplay (horseracing win) data, is that easy to do?

I can see that this is already in the code:

strategy = MarketRecorder(

    name="WIN",

    market_filter=betfairlightweight.filters.streaming_market_filter(

        event_type_ids=["7"],

        country_codes=["GB", "IE"],

        market_types=["WIN"],

    ),

So that is OK.

I thought it may be by changing the in_play_only: bool value in filters.market_filter?

Or am i completely looking in the wrong place! (more lIkely)

Thanks

---

## 2021-05-22 09:16:57 - general channel

**PeterLe**

Thanks [@U0128E7BEHW](@U0128E7BEHW) No all my stuff is written in C#, i have a programmer, but I has some time over the next few months to start learning Python myself.  I managed to get the market recorder working yesterday, so that was an achievement :grinning:

---

## 2021-05-21 23:16:22 - strategies channel

**Paul**

This paper describes a betting exchange simulator that simulates a large number of events and agents to help train ML. The theory has a long track record in fiscal markets but it still feels… odd… maybe useful to train and then use actual historical data for testing &amp; validation? [https://arxiv.org/pdf/2105.08310.pdf|https://arxiv.org/pdf/2105.08310.pdf](https://arxiv.org/pdf/2105.08310.pdf|https://arxiv.org/pdf/2105.08310.pdf)

---

## 2021-05-21 20:42:54 - issues channel

**Newbie99**

```import time

from datetime import timedelta, timezone, datetime

import logging

import betfairlightweight

import argparse

from betfairlightweight.filters import streaming_market_filter

from pythonjsonlogger import jsonlogger

import racing_functions as rf

import non_streaming_functions as nsf

from flumine import Flumine, clients, BaseStrategy, markets

import account_info as ai

from simple_book import simple_book

from flumine.worker import BackgroundWorker

from marketrecorder import MarketRecorder

from flumine.streams.datastream import DataStream

# from race_card import get_racecard

from price_comparison import get_price_comparison

from terminate import terminate

from cross_market import get_markets

from orders_worker import get_live_orders

from flumine.controls.loggingcontrols import LoggingControl

global snapshot



logger = logging.getLogger()



custom_format = "%(asctime) %(levelname) %(message)"

log_handler = [logging.StreamHandler(), logging.FileHandler(ai.log_folder_path + '/' + datetime.now().strftime("%m-%d-%Y_%H_%M_%S") + '.log')]

formatter = jsonlogger.JsonFormatter(custom_format)

formatter.converter = time.gmtime



for l in log_handler:

    l.setFormatter(formatter)

    logger.addHandler(l)

# logger.addHandler(log_handler)

logger.setLevel([http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))



rc = rf.open_json(ai.racing_config)



parser = argparse.ArgumentParser()

parser.add_argument("--c", default=None, type=int, help="Conflate messages in ms")

parser.add_argument("--s", "--strategy-list", nargs='+', default=[])

parser.add_argument("--p", default=False, type=bool, help="Paper or real world trading")



args = parser.parse_args()



paper = args.p

# paper = True

if paper == True:

    print('Paper Trading Enabled')

else:

    print('Live Trading Enabled')



market_recorder = False

if market_recorder is True:

    print('Market Recorder Enabled')



strategy_names = args.s

strategy_names = ['politics_test']

conflate = args.c



start_time = datetime.now(timezone.utc)



settings = [setting for setting in rc if setting['on'] == 'True' and setting['strategy_name'] in strategy_names]



trading = betfairlightweight.APIClient(ai.accname, ai.accpass, ai.acckey, certs=ai.path)

# min bet validation temporarily added to stop the min size replace issue

client = clients.BetfairClient(trading, paper_trade=paper) #,  min_bet_validation=False)



framework = Flumine(client=client)



for s in settings:

    country_codes = s['country_codes'] if nsf.true_or_false(s['country_codes']) != False else None

    market_types = s['market_types'] if nsf.true_or_false(s['market_types']) != False else None

    race_types = s['race_types'] if nsf.true_or_false(s['race_types']) != False else None

    venues_to_include = s['venues_to_include'] if nsf.true_or_false(s['venues_to_include']) != False else None

    print({'strategy_name': s['strategy_name'], 'strategy_type': s['strategy_type'], 'event_type_ids': s['event_type_ids'],

           'country_codes': country_codes, 'market_types': market_types, 'race_types': race_types, 'venues': venues_to_include})

    if s['strategy_type'] == 'simple':

        strategy = simple_book(start_time=start_time, settings=s,

            market_filter=streaming_market_filter(

                event_type_ids=s['event_type_ids'],

                country_codes=country_codes,

                market_types=market_types,

                # market_types=['WIN', 'OTHER_PLACE'],

                # country_codes=['AU'],

                # market_types=['WIN','PLACE', 'EACH_WAY'],

                race_types=race_types,

                venues=venues_to_include



            ),

            streaming_timeout=2,

            max_selection_exposure=s['max_selection_exposure'],

            max_order_exposure=s['max_order_exposure'],

            conflate_ms=conflate,

            name=s['strategy_name'],



        )



        framework.add_strategy(strategy)



worker_settings_list = [

    {'function_name': 'get_markets', 'function': get_markets, 'func_kwargs': {"stake": 2, "margin": 0, "exposure_limit": 60}, 'interval': 0.25, 'start_delay': 30},

    {'function_name': 'terminate', 'function': terminate, 'func_kwargs': {"today_only": True, "seconds_closed": 600}, 'interval': 60, 'start_delay': 60},

    {'function_name': 'get_price_comparison', 'function': get_price_comparison, 'func_kwargs': None, 'interval': 60 - rf.randomiser(15), 'start_delay': 30},

    # {'function_name': 'get_live_orders', 'function': get_live_orders, 'func_kwargs': {'snapshot':snapshot}, 'interval': 5, 'start_delay': 30},

    # {'function_name': 'get_racecard', 'function_name': get_racecard,'func_kwargs': {"event_type_ids": 7, 'market_types': 'WIN', 'source': 'Racecard'}, 'interval': 30, 'start_delay': 30}

]



for f in rf.get_worker_functions(settings):

    function_setting = [ws for ws in worker_settings_list if str(ws['function_name']) == f['function_name']]

    if len(function_setting) &gt; 0:

        function_setting = function_setting[0]

        print(f, function_setting)

        framework.add_worker(

            BackgroundWorker(

                framework,

                function_setting['function'],

                func_kwargs=function_setting['func_kwargs'],

                interval=function_setting['interval'],

                start_delay=function_setting['start_delay']

            ))



if market_recorder is True:

    recorder = MarketRecorder(

        name="WIN",

        market_filter=streaming_market_filter(

                event_type_ids=[7],

                country_codes=['GB','IE','US','CA'],

                market_types=['WIN','PLACE'],

            ),

        stream_class=DataStream,

        context={

            "local_dir": ai.unprocessed_data,

            "bucket": "fluminetest",

            "force_update": False,

            "remove_file": True,

        },

    )



    framework.add_strategy(recorder)



framework.run()```



---

## 2021-05-20 05:54:13 - general channel

**liam**

[@U01TXCYTCSF](@U01TXCYTCSF) that is historical data only [https://github.com/liampauling/betfair/blob/ee4488ddb4f4bee775450f7497c08ea0fb470e9b/betfairlightweight/resources/streamingresources.py#L171|https://github.com/liampauling/betfair/blob/ee4488ddb4f4bee775450f7497c08ea0fb470e9b/betfairlightweight/resources/streamingresources.py#L171](https://github.com/liampauling/betfair/blob/ee4488ddb4f4bee775450f7497c08ea0fb470e9b/betfairlightweight/resources/streamingresources.py#L171|https://github.com/liampauling/betfair/blob/ee4488ddb4f4bee775450f7497c08ea0fb470e9b/betfairlightweight/resources/streamingresources.py#L171)

---

## 2021-05-19 11:45:57 - general channel

**azevedo**

another qn on market recorder. if you set force_update to True, what’s the expected behaviour vs it being False?

---

## 2021-05-01 05:41:58 - strategies channel

**Oliver Varney**

Just a couple of things on coming up with a model, be careful your not over fitting or data mining whereby you apply filters till you hit a profit, yet are left with such a small sample size that it isnt really significant.  if you have historical data, split it into two sections (80-20% split is generally okay with a smaller sample which you have by the sounds), train / come up with the model on the 80% and test it out applying the logic on the 20%. The performance should only be measured against the 20% and any performance on the 80% should be disregarded.

---

## 2021-05-01 00:21:21 - random channel

**John A**

Never purchased Historical data, do my own recording of streaming data. 

---

## 2021-04-28 18:09:08 - general channel

**Lee**

you might need to go the raw stream route but similar to the market recorder but changing up the stream from MarketStream to OrderStream

---

## 2021-04-22 12:14:51 - general channel

**Jorge**

The tutorial is really good, they use the "PRO" historical data but that can be replaced by the recorded streaming files from flumine

---

## 2021-04-20 22:00:44 - general channel

**azevedo**

I’ve just started playing with the market recorder.py example in flumine, looks awesome! 

does it store the account’s Order stream updates somewhere along with market data updates? 

and what about market_catalogues?

---

## 2021-04-20 15:32:35 - issues channel

**Robert**

anyone know an easy way to check betfair who won and placed for a race? I am assuming this is not possible for historical data without using their historical API. How about with the live API

---

## 2021-04-11 09:27:54 - general channel

**John**

Hi I have been following [@U4H19D1D2](@U4H19D1D2)’s great library/page ([https://betfair-datascientists.github.io/historicData/jsonToCsvTutorial/](https://betfair-datascientists.github.io/historicData/jsonToCsvTutorial/)) parsing the advance data to a summary table. As the next step I am very curious to see how to parse the pro/advance historical data to time series. Tried google it and search here but can't find anything. Just in case I miss something, please could somebody give me a pointer? Many thanks!

---

## 2021-04-09 20:04:00 - general channel

**Taking Value**

Ohh I have misunderstood. I thought Flumine was for backtesting and bflw was for recording. Been reading the flumine docs. Just found the market recorder strategy on the Flumine GitHub. I will read it over, thanks very much.



Did you build the BF lightweight library first then Flumine later? Just wondering - Seems Flumine does everything BFL does and then some.

---

## 2021-04-09 19:57:25 - general channel

**liam**

No, tbh just use flumine and/or read the source code on how it does it with the market recorder strategy, reasonably straight forward 

---

## 2021-04-08 16:38:50 - general channel

**William Martin**

So I've abandoned trying to get data via the api to build the mvp of the new betting product I want to create.



Im trying to get the historical data for soccer for April but when I try and unzip its saying there are errors with the files. do I need something special to unzip a .tar?

---

## 2021-04-08 08:37:50 - random channel

**Crofty**

There are some weather radar apps and if it was possible to download historical data ie at  x time on y date, the weather at Lords was cloudy you could factor that in. But then there is other factors like the standard of the bowler versus the standard of the batsman; a strong batsman facing a weaker bowler would have more impact on the prices.

---

## 2021-04-04 11:00:34 - strategies channel

**Oliver Varney**

[@U01PQ9SR9MJ](@U01PQ9SR9MJ) I still think you are data mining, i.e. applying filters to historical data till you get a profit

---

## 2021-03-26 10:54:07 - general channel

**Misha**

[@U0160E9HS2G](@U0160E9HS2G) - OnCourt is a historical database, not a live one

---

## 2021-03-22 19:06:34 - strategies channel

**mandelbot**

I'll work on doing a Monte Carlo, never done one before. I do have a few profitable live strategies though I have to say my approach is pretty basic compared to many on here. I've only just moved to working with python and bflw in the last few months having come from automating strategies on betangel. Still learning the ropes as it were.



You're right 3k does seem a bit thin, unfortunately that's the extent of my historical database for now. I am also betting on bigger odds but &lt;100 so probably that makes 3k seem even thinner. I figured though since I was beating BSP then I might be doing something right.

---

## 2021-03-17 08:06:33 - strategies channel

**Jorge**

Is it possible to run flumine just as a "market recorder", with all the other features turned off? (for ex. turning off OrderStreaming)

---

## 2021-03-15 14:19:16 - random channel

**D C**

I agree if we are talking about some shithouser like "The Badger" who "trades" allsorts but focuses on teaching IP horse racing traders how to "race read" using video streams delayed by who-knows-how-many-seconds. Now as an inplay botter I recognise that I benefit greatly from scum like him duping newbies with some pisspot e-book and making them think they can make money manually trading inplay against video lag/drones/GPS/tracksiders, but it does not sit comfortably with me at all from a moral perspective.



But now compare the other side of the "courses" coin. Imagine someone teaching a course on multinomial logistic regression to an audience who want to model probabilities of horses in a race using historical data/form etc. Or basic poisson regression so you could implement dixon-coles or some ML technique - specifics don't really matter provided it is an actual subject that the tutor has expertise in. The application area (making money from sports betting) is the selling point but paying to learn the methodology from a quality teacher is by no means "dodgy" even if afterwards the technique does not yield profit. After all you can have the right tools but they might not be good enough unless you have the right data (be that bespoke data or fast stream stuff etc). I think I know the types you are referring to though [@U016TGY3676](@U016TGY3676) and I agree with you for the most part. Nobody with an edge is going to sell it on unless they at stage 3 in your list - and after that point that edge will likely evaporate quickly the more people start to utilise it.

---

## 2021-03-15 09:35:49 - general channel

**Steve Roach**

Hi Guys,



I would like to build a database of historic horse racing data with which to analyse at my leisure. I have run the bflw example; examplehistoricdata.py and it is returning some data. I notice right away that is is going to my account on Betfair's Exchange Historical Data and first lists all of the files that I have so far purchased. Right now there are 2 off the Basic plan, and 1 off the Advanced. I see no reason that, given the right amount of effort, I could pull the data into the form that I want. However, at the moment, I'm trying to keep costs down, so I'm just getting the free stuff.



However, I also have access to Betfair's Data Portal (beta) page. Amongst others, there is a set of files "Horse Racing - Files - Month_by_Month_Pro". These are fairly large (some up to 10Gb) and they look like a zipped up set of market files, each covering a month, dated from May 2015 to Feb 2021.



A few questions about this...



• Can bflw access the Data Portal files? Is this even a useful thing to do?

• Can these files be usefully used to create a history?

Thanks in advance.

---

## 2021-03-08 20:59:48 - general channel

**Dave**

[@U01NU8PTC5Q](@U01NU8PTC5Q) may I ask how you intend to consume this historical data? Do you want to, say, convert it to a CSV and then browse it in Excel?

---

## 2021-03-08 19:19:48 - general channel

**Pierino S**

I did download some historical data, think I got December 2020 and unzipped it so i can see its in json format. Can I put that through flumine ?

---

## 2021-03-08 18:32:26 - general channel

**Dave**

alternatively, some of the usually-paid historical data is free (specifically the data from april/march 2020 i think) if you want to get a feel for it.

---

## 2021-03-08 18:22:09 - general channel

**Pierino S**

How do I access historical data on Flumine ?

---

## 2021-03-02 19:59:58 - general channel

**klozovin**

historical data has market and selection names (in the "mcm" message) and the live streaming data does not? right? there's no way to get the names from the stream as well...

---

## 2021-03-02 12:26:01 - strategies channel

**Unknown**

[@U01PQ9SR9MJ](@U01PQ9SR9MJ) the point is that your conclusion of "what is the likely outcome going forward" is unlikely to be useful unless you evaluate this conclusion on data you have not incorporated when doing your data mining. To put it simply, you can't say that your observation of some pattern is a useful observation unless you find that this observation is profitable on data you have kept seperate from where you identified this pattern in the first place. indeed you are attempting to do something like this with your "forward testing", but you can very easily learn the results of your forward testing by just holding out some of your historical data. (This is of course not to disqualify the usefulness of actually taking your strategy to the market with small stakes).



also to add - if you are relying on real trading to do this "validation" for you, your whole process is going to be slow. By holding out some historical data you can instantly check if the patterns you've identified have some profitability (and  therefore meaning you have not just overfit your historical data set).

---

## 2021-03-02 12:24:04 - strategies channel

**James T**

I think like you suggested at the very start you need to change your overall thinking / mentality when coming up with strategy ideas. 



Very first thing is have an idea of where there might be value and possibly why. Imagine a specific point in time and you see odds at 2.1, is backing at that price cheap? Is 2.15 cheap? Is 2.2 cheap? How can you determine if any particular bet is cheap? For me, that’s what a strategy is - a method of determining a fair price so that I can either back or lay with a margin on top of the fair price. 



If you base things on ordering, why would the 3rd favourite necessarily be cheap or expensive based on history? For me the 3rd favourite has just as much probability of being either, so any trend you find in historical data will turn out to be you fitting to the data. 



So I recommend going back to the basics and write down 10 ideas of how you can measure whether a price is cheap or expensive to back or lay. Then test those ideas to see if they are actually a good measure. 

---

## 2021-03-02 12:11:09 - strategies channel

**Atho55**

I am looking at historical data to try to determine what the likely outcome might be going forward based upon what happened in the past. No rocket science behind it unfortunately.

---

## 2021-03-02 12:05:22 - strategies channel

**Oliver Varney**

This is the typical learning approach from machine learning. Take your all the historical data you have and randomly shuffle it. Once shuffled take 20% of you data and put it aside, forget about it for now, almost like it doesn't exist.  With the remaining 80% you will use this data to come up with your model / script / decision maker. Apply the process of learning to this data solely making sure it never sees any of the 20% hidden away. A typical learning approach could be linear regression (gradient descent) but it can be as simple as using excel to filter records although this is sub optimal. Once you think you have constructed your model / script / decision maker, return to that 20% of data and apply the rules / model to it and evaluate performance.

---

## 2021-03-02 11:12:38 - strategies channel

**Oliver Varney**

Id suggest downloading the daily BSP files, splitting your model data into 80% and 20% roughly. Build your script/ decision maker off of the 80% of the historical data, do not let it see the  other 20%. Once you have fully come up with the script / decision maker rules, return to the 20% and see if it makes profit.

---

## 2021-03-01 21:13:56 - strategies channel

**Atho55**

From historical data, hardly going to go into detail

---

## 2021-03-01 20:34:59 - strategies channel

**Atho55**

It`s not betting on a specific horse, but betting on the BSP Rank favourite for every race (UK) for that day regardless of price and obv assumes bets matched at BSP. Have used historical data to give a pointer to what might be a reasonable combination on the day.

---

## 2021-03-01 20:25:35 - strategies channel

**Oliver Varney**

using previous historical data to predict whether you should bet on a horse at a certain price is fairly common if you mean that

---

## 2021-02-24 21:50:39 - general channel

**Pierino S**

Yes, I'd not seen that video, but he has a similar one on his Twitter, with lots of big greens. I have seen him refer a lot to scalping, so do think that's a big part of his philosophy. I've never seen what bank he has, I think you could figure it out, as he definitely shows individual market big greens, so with the Betfair historical data, you could guess-timate what he was up to.........Are there any other Top Drawer traders out there ?

---

## 2021-02-24 11:18:04 - general channel

**Ian**

Hi all, does anyone know if there is a resource that can provide market meta data for historical market ids? Specifically racing - looking to add certain points such as distance, race code, class and if possible going to my flumine collected streams. The BF basic historical data does not seem to contain this.

---

## 2021-02-20 09:27:53 - general channel

**Mick**

I wish I'd never mentioned the tie breaking idea... but do you dispute my more general point, namely "if you have multiple imperfect forecasters of something then employing a weighted sum of their estimates will yield greater accuracy than simply choosing the best of them. You can tune the weights from historical data."

---

## 2021-02-19 16:35:01 - general channel

**Mick**

In general if you have multiple imperfect forecasters of something then employing a weighted sum of their estimates will yield greater accuracy than simply choosing the best of them. You can tune the weights from historical data.

---

## 2021-02-19 08:45:34 - general channel

**Aaron Smith**

[@U01NJ85MP7F](@U01NJ85MP7F) basic / advanced historical data is pretty much useless and pro data is costly. I d rather subscribe to a market and put the money in bets instead of buying the pro-data with it. Having a strategy running will probs give you a better feel for the market and even if your "strategy" sucks, as long as your placing bets on a runner with low price spread, you wont lose a lot. Even if you place low stake bets at random, you ll win some and lose some and it would take some time until you actually reach what you would ve paid for the pro data set

---

## 2021-02-19 06:24:26 - general channel

**KG**

hey guys, I've been playing with using bwlw to parse the historical data sets. am I right in my understanding that, although the historic data files include runner and market name, because the stream API doesn't include the names bflw doesn't support pulling the names out of the historic files? very happy to be corrected if my understanding is wrong here, otherwise keen to hear if anyone has a work around or if there are plans to support it in the package in the future?

---

## 2021-02-18 10:45:48 - general channel

**Alessio**

no, everybody has their own, and that's why you need to make sure your live data and historical data are from the same provider :stuck_out_tongue:

---

## 2021-02-18 06:38:35 - general channel

**KG**

hey guys. has anyone used bflw to read in the PRO historical data sets from their TAR form? I'm following the [https://github.com/liampauling/betfair/blob/master/examples/examplestreaminghistorical.py|sample code](https://github.com/liampauling/betfair/blob/master/examples/examplestreaminghistorical.py|sample code) and getting the following error, which I assume is due to the TAR format?



```UnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in position 569: character maps to &lt;undefined&gt;```

---

## 2021-02-17 10:55:02 - general channel

**Robert**

For anyone interested in why the historical data for runner total_matched is not correct whereas the live API is, here is my response from betfair:

```The total cumulative traded volume per runner (at all prices) isn't included in the PRO data set, unlike in the live Stream API.



For a single price point, 'tv' is cumulative, so each "trd" update contains the price and cumulative traded volume traded so far at that price.  The final sum of the 'tv' at each price point for each selection will be equal to the market traded volume.



"op":"mcm","clk":"9702272675","pt":1563905629308,"mc":[{"id":"1.160659053","rc":[{"trd":[[4.1,11.11]],"ltp":4.1,"tv":11.11,"id":9938916},{"atb":[[4.1,9.93]],"id":9938916}],"con":true,"img":false}]}

{"op":"mcm","clk":"9702305064","pt":1563905813250,"mc":[{"id":"1.160659053","rc":[{"trd":[[4.1,31.31]],"ltp":4.1,"tv":31.31,"id":9938916},{"atb":[[4.1,0]],"id":9938916},{"atl":[[4.1,4.9]],"id":9938916}],"con":true,"img":false}]}

{"op":"mcm","clk":"9703398965","pt":1563917405197,"mc":[{"id":"1.160659053","rc":[{"trd":[[4.1,37.64]],"ltp":4.1,"tv":37.64,"id":9938916},{"atl":[[4.1,1.74]],"id":9938916},{"spn":6.6,"spf":1.0,"id":11110173}],"con":true,"img":false}]}

The runner tv ("tv") represents the cumulative traded amount at the last price traded (ltp) or cumulative amount of all 'trd' amounts in the update if multiple prices are included.```

---

## 2021-02-14 19:51:22 - issues channel

**thambie1**

[@UQL0QDEKA](@UQL0QDEKA) I've considered creating a new account to switch currencies at some point. How difficult and time consuming was the process to move over api access, historical data purchases, money, etc to the new account?

---

## 2021-02-05 08:28:15 - general channel

**Robert**

Hi, anyone know if it is possible to purchase subset of betfair historical data? If just wanted runner book total_matched from 2018 to 2020 say and was not interested in purchasing other columns?

---

## 2021-01-28 15:18:48 - general channel

**Robert**

looking at the betfair historical data I downloaded from the betfair website + using the streaming api for parsing this -- I notice that total_matched in market book is missing most of the time -- is this expected?

---

## 2021-01-27 16:17:52 - issues channel

**Peter C**

What is the easiest way to pull out which runner won when streaming historical data using flumine? I'm currently calculating it from last traded price, but it feels like there's a more explicit route which I'm missing

---

## 2021-01-16 07:36:25 - general channel

**jgnz**

ok thanks liam. i've just added a crontab for now as i dont want to restart the market recorder that i have running. still a bit gutted i lost the data from the India vs Australia match, but its my own fault for copying and pasting too much.

---

## 2021-01-15 10:03:23 - general channel

**Jono**

so did i, apologies for not sending in a code snippet to clarify exactly whta is happening. Im clearing my directory and downloading the BASIC data again to try and rule out the chance its iterating over advanced and pro data i have stored. Will shoot another message in a few hours if im still having probs with it. Like you and the documentation suggests there really shouldnt be values for the atb and atl info

---

## 2021-01-13 01:06:14 - general channel

**jgnz**

When using market recorder in flumine, what is the best way to keep the zipped files? I only just realised flumine is deleting them after 3600 seconds, so all my recorded markets are gone.



Should I setup a crontab to move zipped the files out before flumine deletes them? Or is there a background worker that does this?

---

## 2021-01-07 14:42:34 - general channel

**Robert**

happy new year.  The betfair historical data goes back to ~2016  for uk horse racing.  I was wondering if anyone knows where can get some (at least partial) historical betfair data which goes back for 2014 and 2015?

---

## 2021-01-03 17:51:41 - strategies channel

**JC**

Yeah I would agree, maybe there is a problem with my market recorder

---

## 2021-01-02 08:26:27 - general channel

**Newbie99**

(note though you seem to have to prefix a '1' on that historical data 'event_id' for it to equal a standard 'market_id', so in MySQL, something like this:



```a.market_id = concat('1.',b.event_id)```

---

## 2021-01-02 06:17:39 - general channel

**Charlie 303**

Trying to collate BSP csv data (from [https://promo.betfair.com/betfairsp/prices](https://promo.betfair.com/betfairsp/prices)) and bf historical for the same market -- BSP data gives only the 'event_id', so I figured I could get the corresponding historical data by using the eventId filter, but neither trading.historic.get_file_list(... event_id) in betfairlightweight, nor the crappy download form at [http://historicdata.betfair.com/$/mydata|historicdata.betfair.com/$/mydata](http://historicdata.betfair.com/$/mydata|historicdata.betfair.com/$/mydata) works. Has anyone used eventId filter successfully or otherwise have any hints to get the corresponding historical market id(s) associated with a target event from a BSP file? I suppose I could just download all markets on a given day and grep through the entire collection for the eventId

---

## 2020-12-31 14:51:55 - general channel

**Graham**

please feel free to tell me to f-off but would someone have a historical dataset of intraday horse racing BF price changes that I could tap into please?

---

## 2020-12-29 23:30:28 - general channel

**Tianyao Wu**

Hi guys, is it true that basic historical data has a lot of missing soccer matches?

---

## 2020-12-29 09:54:32 - strategies channel

**Misha**

So does the historical data (provided by Betfair) use the non-virtual prices, or the virtual prices?

---

## 2020-12-28 12:41:08 - general channel

**nthypes**

I agree with you. So the frequentist approach is kind of useless right? The number return from this calculation looking at the historical data, it's a generalization, so kinda of useless when looking at specific race, right?

---

## 2020-12-27 19:52:59 - general channel

**nthypes**

Or what I really get looking the historical data is _P(MT | WIN)_?

---

## 2020-12-27 19:50:01 - general channel

**nthypes**

Question: Imagine that i'm using Bayes Theorem to infer what the probability of a Horse Win in a 7 horses race given that the horse in question is the most traded horse based on volume. I imagine that what I would like to infer is the _P(WIN | MOST TRADED)._



I can get this probability using frequency data analysis. Is Bayesian approach here useless, since I can get this info from looking at the average win from most traded horses historical data?

---

## 2020-12-26 20:49:37 - random channel

**Alessio**

For now, i am looking at two things: low liqudity markets where betfair goes out of sync with reality and historical data prediction to see when a "sure bet" will generate during certain markets

---

## 2020-12-26 11:12:06 - general channel

**Alessio**

Also, if you keep the structure they use for historical data you can just sync subdirectories of it, instead of the whole bucket

---

## 2020-12-23 09:08:51 - issues channel

**Michael**

So back to your original question - I'd say the basic data LTP is a totally reasonable way to estimate your ability to do that and analyse its effect on your returns and I wouldn't apply any transformation to is as you're potentially just introducing and unnecessary error.

---

## 2020-12-16 00:47:23 - random channel

**Charlie 303**

+1 for using Postgres if SQL is involved for holding historical data. As Mo mentioned, the JSON handling is convenient and somewhat easy to optimize.  Using PG for historical + NeDB (in-mem mongo basically) essentially as a cache

---

## 2020-12-15 04:29:24 - general channel

**nthypes**

Folks, any way to get historical data with a discount or cheaper price?

---

## 2020-12-13 14:46:48 - general channel

**Matthieu Labour**

Do you run the in-play service endpoint continuously such that you build a historical database overtime?

---

## 2020-12-13 14:34:09 - general channel

**Matthieu Labour**

Hi all. Question on Backtesting. When backtesting using flumine and betfair, how does one get event updates during in-play such as goals scored, points won, game stats such as first service being lost in tennis. It would be great to learn what folks have been exploring to join betfair historical data with in-play event updates. Thank you!

---

## 2020-12-06 09:13:15 - random channel

**Oliver Varney**

so I guess what I want to design or improve is a data quality / checking service. I run models that use data from many sources + I further aggregate and build out more features. also I would like to build some kind of unit test that tests the built out aggregate features in SQL Server. With a large number of sources + features it can be easy to let a inner join slip through the net instead of being a left join and it might not be fully noticeable straight away.

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

## 2020-11-21 15:32:58 - strategies channel

**Oliver Varney**

watch the markets, understand the fundamentals, come up with a hypothesis, test vs historical data

---

## 2020-11-20 00:28:57 - general channel

**Ben**

Apologies if this has been asked already, but Slack is pretty bad for viewing historic questions: any pointers on parsing the historical data files to look for strategies? I've got a few years of the professional historic data for horse racing but am struggling to get it in a useful format to analyse.



I've got the stream generator working in bflw with no issues but I can't seem to figure my way through turning that output into data that I can analyse.

---

## 2020-11-15 18:22:33 - general channel

**Alessio**

which is an annoying risk of screw up when training on historical data of course

---

## 2020-11-13 21:04:43 - issues channel

**Ruben**

but how else can I build up a repository to backtest? I can't buy historical data since I'm on a non-UK market, so it wouldn't be at all representative

---

## 2020-11-11 13:52:11 - general channel

**thambie1**

Hey folks. Question for those who are running backtests in the cloud, how much is it costing you? For comparison my infra is costing me about $0.50 per 1 year of backtest over pro soccer historical data. Some days I do a ton of backtests, which can add up.  I'm curious how that compares to others.

---

## 2020-11-08 02:53:55 - random channel

**stephencornelius**

Ive played around with the Betfair API for sometime, since their previous REST API. Im now looking into developing a full app with strategies etc. using the streaming API and I'm conscious ill need market data in order to backtest / validate them. I recall reading about the REST API that if you requested price data but were not placing bets that you would be disconnected.



With the streaming API is it possible to subscribe to price data without any repercussions? E.g. The first thing I was planning to create was an automated method of subscribing to all prices for all markets for a given event from each market creation until market closure with a result in order to build as much data as quickly as possible while I develop the rest of my app.



Firstly, is this allowed? If so can you use the Live API key or is only the delayed key allowed?

If not allowed can anyone advise the best way to get as much data as possible for backtesting (Would rather not use the historical data as I dont think its either live or complete / rich enough for me). Feel free to point me to answers if this has already been asked but I was unable to locate.



Thanks in advance

---

## 2020-11-05 20:53:41 - general channel

**Jonjonjon**

If I start running a market recorder to watch all WIN, PLACE and OTHER_PLACE Horse and Dog markets, is there anything I need to be aware of beforehand? I've read a few prior posts about limits, but am not sure what they refered to

---

## 2020-11-05 15:03:29 - general channel

**Jono**

hey [@UBS7QANF3](@UBS7QANF3) ive noticed that in basic historical data market_book.runners contains the last traded price but the market_book.market_definition.runners contains the handicap values . The former doesnt have as many many entries so there isnt a one to one relation between the list of last traded prices and handicaps. I was wondering if there was a way to correctly index through the all the runners ensuring that the ltp and handicap match up correctly. I believe a way to get the lst from the market_definition runners would be a solution to my problem but i havent managed to find a way to do this. Any help is massively appreciated cheers

---

## 2020-11-05 08:13:48 - random channel

**Misha**

Obviously vastly different approaches depending on your starting point. I'm testing a single model/strategy/idea that if works will next be updated in 2022 (tennis probabilities based on historical data). Also looking at a more specific model that would need a fair bit more fine-tuning than that, but that's in development. I think the different approaches reflect the different target markets

---

## 2020-10-28 10:22:39 - general channel

**Jonjonjon**

What is the difference between E and M file types when downloading historical data from betfair?

---

## 2020-10-19 10:41:44 - issues channel

**George Whewell**

hi, any issues with historical data api? i've tried increasing timeout to 10mins and still getting timeout with this:

```for line in client.historic.get_file_list(

    "Soccer",

    "Basic Plan",

    from_day=1,

    from_month=9,

    from_year=2020,

    to_day=2,

    to_month=9,

    to_year=2020,

    market_types_collection=["MATCH_ODDS"],

    countries_collection=["GB"],

    file_type_collection=["E"],

):```

---

## 2020-10-15 16:18:55 - general channel

**Seabass**

Hi, I'm a beginner with betfair but familar with tick trading data. I'am trying to create essentially a time and sales file using the Pro historical data. But when I merge the order book data and the time and sales file I generate, the results look a little strange. Generally, you can see the exact traded size removed from the order book. But occasionaly, there seems to be a trade that was adjusted later on (size doesn't match order book) and occasionally I see exactly half of the reported trade size being removed from the book. To calculate the trades I just take the difference from the current trd cache and the newest trd cache. What is the correct way to calculate the amount that was traded? And am I overlooking something in my calculation?

---

## 2020-10-09 21:50:32 - issues channel

**Misha**

The historical data is supplied by Betfair, and it is of indeterminate quality

---

## 2020-10-09 21:47:26 - issues channel

**Misha**

It should only happen for historical data - not live data

---

## 2020-10-06 08:36:48 - general channel

**Alessio**

i was looking into the historical data..(the free PRO and ADVANCED ones) maybe somebody did it as well.. i was trying to see how the market moves while in play for some soccer or horse racing market.. but it seems there's only a few seconds between the market gets defined as 'in play' and it gets closed.. is it me reading the data wrong or is it actually like this? (i'm using bflw histostream of course)

---

## 2020-10-05 13:34:06 - general channel

**Lee**

I'll answer based on how i use Flumine

1. For recording I use the S3 market recorder from the examples and use the same recorder to record all sports. So for football i'd run it using something like below. This will record all GB football matches to individual files and upload to S3. I personally wouldn't restrict by date as the streaming will subscribe to new markets to the recorder as and when they become available.

```framework.add_strategy(

    S3MarketRecorder(

        market_filter=streaming_market_filter(

            event_type_ids=[1],

            market_types=[

                "MATCH_ODDS",

                "OVER_UNDER_25",

            ],

            country_codes=["GB"],

        )

        stream_class=datastream.DataStream,

        context={//add config here}

    )

)```

2. There's no limit (afaik) in Flumine so just depends on what your strategies are doing and how long they take to process each update.

3. There's also no limit on how many instances of Flumine you can run, you're only limited by betfair streaming connections which is 10.

---

## 2020-10-02 21:20:26 - issues channel

**Jonjonjon**

If I record my own data, using the market recorder, and then use it for backtesting, there is a problem with in the market cache, as it expects some runners variables to be populated before it starts doing stuff with market books. Has anyone else encountered this?

---

## 2020-09-25 16:17:13 - general channel

**Jono**

is there anyway of differentiating if last traded price from Basic historical data was on a BACK or LAY selection?

---

## 2020-09-24 15:57:20 - general channel

**Jono**

hey all quick one this time, ive got some purchased historical data and looking for the exchange odds values and volumes but struggling to locate where they are. Should i be able to see them in the market_definition or runner objects or somewhere entirely different? help is greatly appreciated

---

## 2020-09-23 09:08:26 - general channel

**Jono**

Currently having some success getting to grips with parsing historical data from bf but was wondering if an events associated competition id is available in the data from the basic plan. Ive had a look at the official documentation and the info parsed from a such a file and cant seem to find an events comp id. Is this id available in some resource i am not looking at? or in the market_definition returned? Thanks

---

## 2020-09-17 09:12:40 - general channel

**Jono**

I am receiving an error  at the "for market books in gen()" line regarding a unicode error: 'charmap' codec can't decode byte 0x8f in position 159: character maps to &lt;undefined&gt;. So i was wondering if any processing has to be performed on the downloaded files prior to executing this script and/or parsing historical data?

---

## 2020-09-16 20:56:33 - general channel

**Dave**

evening all - looking to set up some higher-freq strategies in the coming months so have deployed the classic flumine market recorder. Qq about restarting on failure - is there any issue with writing the MD to the same file it was writing to prior to any crash/failure? I noticed the example flumine market recorder creates a new directory each time it starts up, so could be a pain when it comes to stitching MD from a previous run with MD recorded from the subsequent run of the recorder (for the same given market of course). I imagine there'll just be extra market definition entries, but other than that no issue?

---

## 2020-09-05 23:08:17 - issues channel

**Ruben**

there's something that is keeping me a bit worried....I run my market recorder on a very modest server (1 GB RAM), and yesterday the python process suddenly stopped, without any errors/warnings in the log, nor in stdout. I have no clue what could have caused this, any ideas?

---

## 2020-08-27 21:25:13 - general channel

**birchy**

I have a noob question regarding the python logging module... I pretty much copy &amp; pasted [https://github.com/liampauling/flumine/blob/master/examples/marketrecorder.py|market recorder.py](https://github.com/liampauling/flumine/blob/master/examples/marketrecorder.py|market recorder.py) to an AWS Lightsail instance a month ago and launched as a detached process. I've just discovered that despite the process still running, no data has been saved for over a week. I've not previously used the logging module, so where is the logging info going? I assume there's a file somewhere, otherwise it's not actually "logging" anything?!

---

## 2020-08-27 04:57:01 - general channel

**InvestInHorses**

hi, I joined this Slack channel as I've purchased Betfair historical data and want to build a price cache for back testing my own strategies and creating my own tools for research

---

## 2020-08-26 18:34:32 - general channel

**birchy**

Refreshing to see that [@U4H19D1D2](@U4H19D1D2) is having success with simple "if this condition" type strategies as that's exactly what I do. I basically have a set of functions that check various market conditions and then combine the return values to make a decision. In the early days I would create a strategy based on my understanding of the markets and then go straight to live testing at minimum stakes. I still do that occasionally but mostly gain some confidence first by backtesting against historical data. The one thing you really have to understand is the power of big numbers... i.e. 1000 bets or markets is a reasonable starting point but even that can sometimes be showing a loss for a strategy that is actually profitable over a much larger sample. Variance is both our enemy and our best friend.



There was a time when I would write off bots if they lost £100 at £2 stakes (which was day one in some cases!), but learnt quite a few years ago that you realistically need a bank of at least 1000 bets just to cover the variance.

---

## 2020-08-25 23:48:25 - random channel

**birchy**

It's peaked my interest...is there any timestamped historical data available, i.e. where I could compare gps feed vs exchange prices?

---

## 2020-08-24 22:35:12 - issues channel

**birchy**

Any ideas why smart_open() can't open files saved with marketrecorder.py? I recently had issues getting backtesting running with self-recorded data but have had success using `.bz2` historical data acquired from Betfair. Turned out that there was nothing wrong with my original backtest code, but my recording code is shyte. :man-facepalming:



`def _zip_file(self, file_dir: str,`

    `market_id: str) -&gt; str:

    """zips txt file into filename.bz2"""

    zip_file_directory = os.path.join(

        self.local_dir,

        self.recorder_id,

        "%s.bz2" % market_id

    )

    with zipfile.ZipFile(

        zip_file_directory,

        mode="w"

    ) as zf:

        zf.write(

            file_dir,

            os.path.basename(file_dir),

            compress_type=zipfile.ZIP_BZIP2

        )

    return zip_file_directory`

---

## 2020-08-23 11:57:49 - general channel

**Misha**

For historical data. The number of updates live is limited by how many there are at the time :wink:

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

## 2020-08-14 18:37:42 - general channel

**birchy**

Bummer, I would normally use bz2 inline with the historical data but the Flumine example uses zip, so I left it alone... assuming it was a suitable format for backtesting.

---

## 2020-08-10 20:09:53 - general channel

**liam**

Have you seen the [https://github.com/liampauling/betfair/tree/master/examples|examples](https://github.com/liampauling/betfair/tree/master/examples|examples)? It might be that you want to process historical data first to get a feel however I recommend making some requests as per the [https://liampauling.github.io/betfair/quickstart/|QuickStart](https://liampauling.github.io/betfair/quickstart/|QuickStart) to get a better understanding of the API and responses 

---

## 2020-07-30 22:27:12 - issues channel

**mlpanda**

Hey, has anyone had the issue of receiving an empty list when using the historical data example in betfair lightweight: [https://github.com/liampauling/betfair/blob/master/examples/examplehistoricdata.py](https://github.com/liampauling/betfair/blob/master/examples/examplehistoricdata.py)



In `my_data` I have the following data purchased:

`{'sport': 'Horse Racing', 'plan': 'Advanced Plan', 'forDate': '2020-05-01T00:00:00', 'purchaseItemId': 48406}`



But when I use the following function:

```# get file list

file_list = trading.historic.get_file_list(

    "Horse Racing",

    "Advanced Plan",

    from_day=1,

    from_month=5,

    from_year=2020,

    to_day=31,

    to_month=5,

    to_year=2020,

    market_types_collection=["WIN", "PLACE"],

    countries_collection=["GB", "IE"],

    file_type_collection=["M"],

)

print(file_list)```

I get an empty list in `file_list`. If I try to expand the dates to e.g. `to_month=6` I get an error (probably because I haven't purchased data for June), but I'm puzzled why I get an empty list for the above example.

---

## 2020-07-25 10:49:14 - issues channel

**Mark**

Happy weekend chaps!

I've been using the examplestreaminghistorical.py from BFLW to run through some of the historical data files offered by Betfair recently. It's been working great.. except when I run through a Greyhound file where a reserve runner replaces the original. This seems to happen at least once per meeting and the whole thing chokes.



I haven't touched anything except the location of each data file (obviously!) According to the Traceback, it's tripping up over a number of processes and I haven't a clue where to start.



I've updated BFLW to 2.6.0 and I'm using the out-of-the-box examplestreaminghistorical.py without modification.



Has anyone else come across the same thing and can point me in the right direction? Cheers!



```Traceback (most recent call last):

  File "G:/python/scratchpad/examplestreaminghistorical.py", line 34, in &lt;module&gt;

    for market_books in gen():

  File "C:\Users\Mark\AppData\Local\Programs\Python\Python38-32\lib\site-packages\betfairlightweight\streaming\betfairstream.py", line 326, in _read_loop

    if self.listener.on_data(update) is False:

  File "C:\Users\Mark\AppData\Local\Programs\Python\Python38-32\lib\site-packages\betfairlightweight\streaming\listener.py", line 127, in on_data

    self._on_change_message(data, unique_id)

  File "C:\Users\Mark\AppData\Local\Programs\Python\Python38-32\lib\site-packages\betfairlightweight\streaming\listener.py", line 167, in _on_change_message

    self.stream.on_update(data)

  File "C:\Users\Mark\AppData\Local\Programs\Python\Python38-32\lib\site-packages\betfairlightweight\streaming\stream.py", line 59, in on_update

    self._process(data[self._lookup], publish_time)

  File "C:\Users\Mark\AppData\Local\Programs\Python\Python38-32\lib\site-packages\betfairlightweight\streaming\stream.py", line 152, in _process

    market_book_cache.create_resource(

  File "C:\Users\Mark\AppData\Local\Programs\Python\Python38-32\lib\site-packages\betfairlightweight\streaming\cache.py", line 218, in create_resource

    data = self.serialise

  File "C:\Users\Mark\AppData\Local\Programs\Python\Python38-32\lib\site-packages\betfairlightweight\streaming\cache.py", line 267, in serialise

    "runners": [

  File "C:\Users\Mark\AppData\Local\Programs\Python\Python38-32\lib\site-packages\betfairlightweight\streaming\cache.py", line 269, in &lt;listcomp&gt;

    self.market_definition_runner_dict[

KeyError: (27395886, 0)



Process finished with exit code 1```

---

## 2020-07-24 23:27:42 - general channel

**birchy**

Actually, now that I've written that down, I'm questioning my own ability. I've not watched a betfair market for at least 5 years, so as such I'm developing strategies blindly, using nothing but educated guesses. I do test them on historical data before going live, but in reality everything is based on assumptions that I've accumulated over the last 30 years, mixed with a handful of new ideas I've read on various forums and betting blogs.

---

## 2020-07-16 12:52:08 - general channel

**JC**

Hi guys, pretty new here and really enjoying getting to learn the ropes of working with the API. Thanks to the brilliant libraries of bflw and flumine and previous queries in this chat I have managed so far to implement an S3 market recorder running on an EC2 instance. I am now looking to capture as much other available data about the market and runners as possible i.e. metadata available via `list_market_catalogue` , as well as some summary data such as total amount traded at start and end, so that I can query and filter the files on S3 using this. I would also like to record a stream for in-play scores data for tennis. Seems like I should set up a simple script for the former on a time loop which can update and feed my database. For the scores streaming, is there a way to do this in flumine? Any advice would be very welcome on either of these. Thanks again for these libraries and for the active community here :grinning:

---

## 2020-07-08 18:33:05 - general channel

**birchy**

[@U4H19D1D2](@U4H19D1D2) you mentioned the free historical data last night...now I've added everything available to my "purchases" but am having a ball-ache downloading it. Seems like they're throttling the upload and my calcs suggest it's going to take about a week to download it all through Chrome browser. Is there a quicker way to download and/or save/resume?

---

## 2020-07-05 12:01:01 - strategies channel

**Sandy Caskie**

So I have streamed horse racing data saved this and used this to build a predictive price model. My streamed data is not of a super high latency though. I will have to look in more detail the reason for this though it seems pretty accurate on a first glance. My question relates to historical data. I also built a predictive model using the free package but this was pretty useless with a frequency of per minute. For anyone else who has done something similar was the pro data particularly useful for building a predictive model?

---

## 2020-07-05 10:01:38 - general channel

**SrFabio**

You can have a look at betfair exchange historical data ([https://historicdata.betfair.com/#/home](https://historicdata.betfair.com/#/home)). If you are looking for inplay stats then you'd have to use a third-party like opta (I've not used any myself so can't really recommend)

---

## 2020-07-01 14:34:55 - general channel

**Mark**

I'm currently editing the examplestreaminghistorical.py file in BFLW to output a little more data. I've figured out most of what I need, but can't for the life of me find the last traded value. Of course the last_price_traded for each runner is already there, but where do I find the actual amount traded? I think it corresponds to the TRD value in the BF historical data file.



```runner_def = runners_dict.get(

                    (runner.selection_id, runner.handicap))

                output.write(

                    "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"

                    % (

                        market_book.market_id,

                        market_book.publish_time,

                        market_book.status,

                        market_book.inplay,

                        market_book.total_matched,

                        runner.selection_id,

                        runner.ex.available_to_back[0].price,

                        runner.ex.available_to_back[0].size,

                        runner.ex.available_to_lay[0].price,

                        runner.ex.available_to_lay[0].size,

                        runner.total_matched,

                        runner.last_price_traded or "",

                    )

                )```



---

## 2020-06-19 09:40:44 - general channel

**brightcake**

so what would normally be runners in historical data are treated as seperate markets in stream?

---

## 2020-06-18 18:49:54 - strategies channel

**Julio**

do you know if we can get some historical data from timeform?

---

## 2020-06-17 13:52:24 - issues channel

**EJono**

Accessing the directory of the downloaded files seems to be the high level problem I'm having. The BASIC file in the below photo is just the extracted entry of the initially downloaded data.tar file that I downloaded from bf historical data page yesterday

---

## 2020-06-17 13:36:47 - issues channel

**EJono**

I am trying to obtain selection ids from past matches of rugby matches etc through parsing a few months of historical data, downloaded via the basic plan. I was under the impression that betfairlightweight was the perhaps the optimal way to go about investigating previous data but I am having some problems operating directly on the downloaded data.tar files from betfair. I was curious if anyone knows what I should be doing in order to create a setup (in python) for retrieving information from these downloaded files either through utilising betfairlightweight or otherwise?



Any help is greatly appreciated

---

## 2020-06-17 13:34:45 - issues channel

**EJono**

Hey everyone, I had a question regarding bf historical data and was pointed towards this group on the developer forums. don't want to flood the wrong message board. Is this the right place to post my concerns?

---

## 2020-06-15 13:59:23 - issues channel

**mandelbot**

The code is just the same as the market recorder example

---

## 2020-06-15 13:38:31 - issues channel

**mandelbot**

BTW when I said instances I meant instances of the market recorder

---

## 2020-06-15 13:13:30 - issues channel

**Sandy Caskie**

I am trying to get the price historical data for back and lay for horse racing events prior to the race start. I have been able to download the historical data using the GitHub repository [https://github.com/liampauling/betfair/blob/master/examples/examplehistoricdata.py](https://github.com/liampauling/betfair/blob/master/examples/examplehistoricdata.py). I have then tried to view this data using the code from this repository [https://github.com/liampauling/betfair/blob/master/examples/examplestreaminghistorical.py](https://github.com/liampauling/betfair/blob/master/examples/examplestreaminghistorical.py). Though when I do this I receive the following error:



```AttributeError: 'Streaming' object has no attribute 'create_historical_generator_stream'```

When I look at the downloaded historical data file and read it as .txt file I can see it has the last traded price per runner. Therefore it appears that the downloaded file does have the data I am looking for. Though I cannot see a date-time stamp or if it is back or lay price for the traded price. Therefore I have two questions:



1. Is this the correct method to get back and lay price data up until the race starts?

2. Has this attribute name been changed or something? That is why I am getting this error.

---

## 2020-06-12 18:02:19 - issues channel

**Mark**

[@UQL0QDEKA](@UQL0QDEKA)  [@UPMUFSGCR](@UPMUFSGCR) Yeah, I'm an absolute newbie at Python and it's been an eye-opener going from the most basic of JSON files in my "*Python Crash Course*" book to the mind boggling multiline deep-nested monstrosity that is a Betfair Historical Data File! None of the Python gurus seem to cover that in their YouTube videos :astonished:

I'm currently collecting snippets I may find useful along the journey, such as the Certs tutorial and of course, the Backtest file, while the example files are a great help too. That Liam fella's a clever bloke :wink:. It took me a while to figure out that I could save snippets in my Saved Items area so the data file to database example by [@UNQGKT0CR](@UNQGKT0CR) fell off the end of the message list before I could grab it. I was originally going to suggest a Newbies section where common problems and solutions could be stored but I guess the Saved Items and Files links pretty much has that covered already.

---

## 2020-06-12 17:04:15 - general channel

**gprokisch**

Where I can find historical data of Greyhound race for use in backtesting?

---

## 2020-06-12 14:35:39 - issues channel

**Rich**

When I download the historical data straight from the betfair website, I get a TAR file of bzipped json files.

---

## 2020-06-12 14:34:48 - issues channel

**Rich**

```num_of_markets = 3



class HistoricalGeneratorStreamTarBz(HistoricalGeneratorStream):

    """Copy of 'Betfair Stream' for parsing historical data (no threads).

    RB: Edited for reading tarred/bzipped files

    """

    def _read_loop(self):

        tar = tarfile.open("D:/BetfairHorseMarketsDetailed.tar")

        i = 0

        self._running = True

        for member in tar.getmembers():

            bzf=tar.extractfile(member)

            f = bz2.open(bzf)

            i += 1

            if i &gt; num_of_markets: #change this to get more than 3 markets!

                self.stop()

                break

            content=f.readlines()

            for update in content:

                if self.listener.on_data(update) is False:

                    self.stop()

                    raise ListenerError("HISTORICAL", update)

                if not self._running:

                    break

                else:

                    yield self.listener.snap()

            else:

                self.stop()



stream = HistoricalGeneratorStreamTarBz('', listener)

gen = stream.get_generator()```

---

## 2020-06-12 14:19:45 - issues channel

**Rich**

Hi, I'm playing with the historical data (HistoricalGeneratorStream).  There doesn't seem to be any code here to deal with the bzip/tar file layout.  What is expected to be the content of the 'directory="/tmp/BASIC-1.132153978"' Is this a json file, several json files in one directory etc? Thanks

---

## 2020-06-12 11:40:33 - strategies channel

**Dave**

[@UUCD6P13J](@UUCD6P13J) - it takes historical data into account, I spend a lot of time gathering clean, consistent data and transforming it and getting rid of anomalies and etc.

---

## 2020-06-05 14:31:30 - general channel

**Julio**

Hello all,

For all of you who are not (yet) recording data, Betfair has an offer:

*Free Betfair Exchange Historical Data Offer!*

We are offering the following historical data free of charge:

*January 2020– May 2020 – ADVANCED data - All Sports – (normally £2615)*

*April 2020 – May 2020 – PRO data – All Sports – (normally £2180)*

---

## 2020-06-01 07:33:20 - general channel

**Will Morrison**

Mo and liam, thanks a ton for the help last week, I super appreciate the package and you guys keeping an active community here! I haven't bought an active key yet, so when I run my modified version of the streaming example, I just get an update from the while loop market_books = output_queue.get() every 180 seconds. For now, I just put some loops underneath that to grab the data that I want from the market books and save it as a csv, but this feels like it can't be the right approach once I have a live key, since I would be copying a bunch of unchanged data constantly. I'm guessing that the way the data stream comes in is that it only sends updates to things that have changed, like the json lines in the historical data? Is there an example that would help me see how to record the stream in a smart way? And thanks in advance for your patience, I suspect that for a more experienced programmer this might be a trivial question to figure out.

---

## 2020-05-27 21:42:08 - general channel

**liam**

The market recorder is setup to record the raw data so that won’t really work but you can modify the price recorder [https://github.com/liampauling/flumine/blob/master/examples/strategies/pricerecorder.py|example](https://github.com/liampauling/flumine/blob/master/examples/strategies/pricerecorder.py|example)



Just change the check_market_book



```if market.seconds_to_start &lt; 600:

    return True```

---

## 2020-05-18 23:09:18 - strategies channel

**SrFabio**

Thanks! I'd like to ask a question as I'm a bit confused: when building a trading model do you guys mostly seek statistical arbitrage opportunities based on historical data or is there something better to look for?

---

## 2020-05-18 07:49:52 - general channel

**Will Morrison**

I hadn't looked at the historicalstreaming example because I assumed it was basically the same as the live streaming one but on historical data. Now I see that it has some writing examples which may be exactly what I need to get started. Thanks Liam!

---

## 2020-05-18 04:53:12 - general channel

**Will Morrison**

Hi everyone! I'm new to the betfairlightweight package. I already analyzed Betfair historical data using R, parsing the files with a json package and eventually creating rows with things like runner name, batb, batl, etc. I have got the examplestreaming script to generate data for the markets that I am interested in, and if I save market_book.streaming_update as a .txt and then substitute a few things, I can parse it as a json file, but it is missing some of the higher level data that I need, like the runner ids and runner names. When I click around the market_book (object?) in my variable explorer in Spyder, I can see that it looks like all the stuff I need is probably already there. Are there some examples of parsing this data into usable tables, or is there a way that I can retrieve the data to look more like the historical bz2 files that I am used to now? Thanks a bunch for any help, it's super cool to see that there's a community around this!

---

## 2020-05-14 12:45:50 - general channel

**brightcake**

sorry i meant market recorder

---

## 2020-05-13 15:22:30 - general channel

**Mark**

Hello! Like many I came here after downloading some of the free Betfair Historical Data files and after discovering the multiline JSON format was tripping me up, discovered the bflw and flumine packages. Spent the rest of my life reading through the messages! Got to admit, it looks like a steep learning curve so I'm off now to fire up Sublime Text and progress beyond Hello World! :astonished:

---

## 2020-05-12 23:28:27 - random channel

**Jonjonjon**

What's the difference between the E and M File Types from Betfair's Historical Data?

---

## 2020-05-12 20:25:10 - general channel

**Jonjonjon**

[@UBS7QANF3](@UBS7QANF3) Why would you be against that? The historical data from betfair arrives in that format. So if we don't have it, users will need to decompress all the files anyway.

---

## 2020-05-08 17:14:47 - general channel

**Edoardo**

Hello. I'm new and I would like to download some Betfair historical data about soccer. The problem is that I'm from Italy and the operator told me that it is possible to download those data only from UK and Malta. Is there any workaround? Thanks in advance

---

## 2020-05-04 11:34:41 - issues channel

**Unknown**

In regards to the historical data does anyone have issues with lots of updates having `img=True` and thus the cache being replaced? My assumption is that the data can be trusted and replacing the cache with the update is safe but who knows with this data (first time I have actually used Betfairs data rather than my own)

---

## 2020-05-03 22:31:22 - random channel

**Jonatan (skyw)**

[@UPMUFSGCR](@UPMUFSGCR),  Yeah, of course, could you send it to me? I do not have access to historical data from Sweden.

---

## 2020-05-03 20:46:27 - random channel

**Jonjonjon**

[@U92CASP1B](@U92CASP1B) I notice that you are using a data from Dec 2019 to do your benchmarking. Are you able to share that (without getting in trouble), so that I can test against the same file? If not, could we try to use a common file from the recent free historical data that Betfair has provided? For example, I am now running it against 29639024, an AU horse racing data from 1st April 2020. The pro data is free for April.

---

## 2020-05-01 21:24:18 - general channel

**Jonjonjon**

I'm looking at 1.166947655, Jan 4th, which is a free download from Betfair's historical data service

---

## 2020-05-01 10:40:45 - random channel

**Jonjonjon**

Last night, all I did was pump some historical data through the backtest example. It probably took over a minute just to loop over all the data in the file. Once I've worked out how to use it, I can test several different parameters/markets/strategies simultaneously using different cores. But as Mike Tyson says, everyone has a plan until they get punched in the mouth, so I don't want to buy new hardware until I really need it.

---

## 2020-05-01 10:26:55 - random channel

**Jonjonjon**

Nice. Thanks for sharing. Are you mainly going to be doing CPU (rather than GPU) intensive stuff? I currently have dual Xeon X575 chips in my setup. So they are almost 10 years old. I'm not sure how to work out how much faster a new setup will be. Having said that, I only managed to run historical data through Flumine last night, so it's early days to tell whether or not I need a crazy setup.

---

## 2020-04-24 10:50:00 - random channel

**Jonatan (skyw)**

I agree that for most the basic solution is more than sufficient.  Things that I think could be there are how fast can you process historical data, the rate of messages through market cache. the delay added.

---

## 2020-04-22 23:00:56 - general channel

**user34**

I have just started working with the historical data from Betfair and want to extract the market books at a given time before the event. Does anyone know what functions I should be using for this?

---

## 2020-04-10 22:14:41 - general channel

**Lee**

Is it okay to keep the market recorder running in flumine as one of the strategies in production or keep them as two separate services?

---

## 2020-04-05 07:53:48 - issues channel

**Mo**

What historical data do you own?

---

## 2020-04-02 12:18:56 - general channel

**Jeff**

On line 66 of example do I need to point it to the historical data file? These are the errors I am getting: C:\Users\Jeff\PycharmProjects\GitHubExample\venv\Scripts\python.exe C:/Users/Jeff/PycharmProjects/GitHubExample/GitHubExample.py

INFO:betfairlightweight.streaming.listener:Register: marketSubscription 0

INFO:betfairlightweight.streaming.stream:[Stream: 0]: "HistoricalStream" created

Traceback (most recent call last):

  File "C:/Users/Jeff/PycharmProjects/GitHubExample/GitHubExample.py", line 71, in &lt;module&gt;

    stream.start()

  File "C:\Users\Jeff\PycharmProjects\GitHubExample\venv\lib\site-packages\betfairlightweight\streaming\betfairstream.py", line 295, in start

    self._read_loop()

  File "C:\Users\Jeff\PycharmProjects\GitHubExample\venv\lib\site-packages\betfairlightweight\streaming\betfairstream.py", line 301, in _read_loop

    with open(self.directory, "r") as f:

FileNotFoundError: [Errno 2] No such file or directory: '/Users/liampauling/Downloads/Sites 3/xdw/api/c0a022d4-3460-41f1-af12-a0b68b136898/BASIC-1.132153978'



Process finished with exit code 1

---

## 2020-04-02 00:34:48 - general channel

**Jeff**

Hi everyone I am very interested in building applications especially for Betfair. I am a complete noob with any language but I am very interested in Python. I would like to build an app that replays Betfairs horse racing historical data with ladders setup like Gruss or Bet Angel and able to place fictional bets and trade just as if it were real. I realise it's a tall order to build a complicated app with no experiance but I have plenty of time on my hands since I am out of work and have plenty of evenings to start learning. I have downloaded some sample horse racing historical data pro and advanced, Python installed and betfairlightweight and a few other addons. I guess I'd like to know where to start and if someone could point me in the right direction I'd be very greateful. Kindest regards Jeff

---

## 2020-03-28 15:14:40 - general channel

**brightcake**

Quick question about betfair historical data - each file that is downloaded contains the history of one market only? Or do you sometimes find data from other markets contained there?

---

## 2020-03-23 22:50:35 - general channel

**Johnny**

Hi all, been lurking for a while now and suddenly seem to have a bit more time on my hands...  I came across betfairlightweight after doing a load of work writing my own API-NG interface - haven't finished much of the streaming part yet but will probably not bother since Liam's implementation looks so comprehensive!  



Anyway my question is, what is the more common approach here, to collect your own data via recording streams or buying the pro datasets from betfair?  How do you guys browse the data since there are so many markets and events?  I've written my own historical data browser which i suppose all of you backtesters have already done.

---

## 2020-03-17 08:09:18 - issues channel

**liam**

This is basically the conclusion I came to, running any historical data in a separate thread doesn't really work as it need to be moved into the main thread. One way would be to override process_market_book and add the terminator to the queue if market_book.closed

---

## 2020-03-02 15:40:16 - general channel

**AP**

When trying to process multiple historical data files at the same time, is threading more efficient than multiprocessing?

---

## 2020-02-29 17:10:15 - issues channel

**liam**

Historical data 

---

## 2020-02-24 13:04:35 - issues channel

**Jack Kaminski**

Can anyone help me with extracting the market definition dictionary from a historical data stream object. Like retrieving the market books only return a marker definition dictionary

---

## 2020-02-23 10:13:48 - general channel

**Lee**

Does anyone buy the betfair historical data or just collect their own?

---

## 2020-02-22 12:25:37 - issues channel

**Lee**

Hi, for the historical data, I have all the files and wrote a little script to extract and merge into one file then call this:

```stream = trading.streaming.create_historical_stream(

    directory='data/merged.txt',

    listener=listener,

)```

Is this the correct way of doing it or is there a better way? Looks like doing it this way i'll need to sort by `publish_time`

---

## 2020-02-19 19:07:35 - general channel

**Fab**

I haven’t tried to play with historical data using betfairlightweight yet. But from what I recall, each line of an historical data file is a separate json object.

---

## 2020-02-13 17:49:10 - general channel

**Alex F**

so i can actually build a scraper for the future, but cannot do anything like this for historical data

---

## 2020-02-10 19:28:03 - general channel

**klozovin**

do you work with lots of historical data? is it gigabytes or terabytes? :slightly_smiling_face:

---

## 2020-02-10 15:17:00 - general channel

**Josh**

I noticed there were some questions about whether PRO level historical data is handled by the library a while back and I just wanted to point out that I think there may be issues with how the library handles traded volume given [https://support.developer.betfair.com/hc/en-us/articles/360002401937-How-is-traded-volume-represented-within-the-PRO-Historical-Data-files-](https://support.developer.betfair.com/hc/en-us/articles/360002401937-How-is-traded-volume-represented-within-the-PRO-Historical-Data-files-).

---

## 2020-01-29 09:39:00 - general channel

**JonJonJon**

It's not something I'm currently looking at. I've found that live testing on the exchange is better than doing backtesting on historical data.

---

## 2020-01-15 14:55:43 - general channel

**Robert**

Hi, I have betfair historical data and am using your API, I would like to know which horse was paid out by betfair:

I can do runner.status to get 'LOSER' or 'WINNER' but can I be sure this is actually what was paid out and that it was not changed shortly after the race finished?

---

## 2020-01-13 13:28:25 - general channel

**Nick P**

Hiya - new joiner here. Excellent site by the way.  Just have a basic query around the BF historical data - Can I  get Metadata i.e via the ListMarketcatalogue - need to get historical Jockey/weights/Ratings etc.  Not sure I can but if anyone could  comfirm - thanks !

---

## 2020-01-11 14:53:48 - general channel

**AP**

Has anyone attempted to process the historical data in parallel?

---

## 2020-01-08 17:14:44 - general channel

**AP**

Ok so for trading live the historical data is stored in memory for the most part 

---

## 2019-12-28 12:36:13 - general channel

**Marcel**

2) Can you explain the added functionality from this script compared to manually downloading historical data files? Does it extract the tar - files for example in another format and which format?

---

## 2019-12-28 12:33:09 - general channel

**Marcel**

I have two questions. 1) Do I need to have an App key from Betfair to run this script? I already have a Betfair account and I can download historical data manually.

---

## 2019-12-01 16:09:05 - general channel

**liam**

It’s setup for one when it comes to historical data, obvs the live stream can handle multiple because multiple markets come from betfair and there is only one market per file 

---

## 2019-11-27 17:26:57 - general channel

**hugo**

How soon after settling does a market become available on the historical data api?

---

## 2019-11-27 13:58:01 - general channel

**hugo**

If I'm dealing with a market that was open for a very long time (an outright market on a world cup for instance) will I find the historical data file for that market in the month that it opened?

---

## 2019-10-14 10:51:55 - issues channel

**Phil Hughes**

The historical data website seems to be up and running again now but I still can't seem to download files via the api. Anyone tried in the last few days?

---

## 2019-09-21 12:38:54 - issues channel

**Justin Fisher**

:wave: hello to the code maintainers. First off want to say :pray: for the python package, big fan.



Im having an issue pulling historical data at the moment. It seems like maybe `betfair` and their download historical data isnt working but want to be sure. I usually use the UI but its been returning `10kb` tar files that dont seem to open correctly. I am now trying to use the download approach found at `[https://github.com/liampauling/betfair/blob/master/examples/examplehistoricdata.py](https://github.com/liampauling/betfair/blob/master/examples/examplehistoricdata.py)` and added some of my own print statements:

---

## 2019-09-12 10:58:49 - general channel

**liam**

its due to the requirement of handling the shitty historical data

---

## 2019-09-06 13:12:25 - general channel

**stefan**

Overall it looks like the api for historical data download has changed, and the way to obtain the file via `DownloadFile?filePath` is obsolete?

---

## 2019-09-06 12:40:28 - general channel

**stefan**

Hi all. Does anybody know if there is a way to filter by `eventTypeId` for historical data download, when your selected sport is `Other Sports`? Thanks :thumbsup:

---

## 2019-07-28 06:37:26 - general channel

**William**

using historical data

---

## 2019-07-20 20:35:16 - general channel

**Dawid**

I have one problem - I want lot of historical data to make my own analysis, there is a lot of data I can access (I am using race cards via betfairlightweight and csv files from [https://promo.betfair.com/betfairsp/prices](https://promo.betfair.com/betfairsp/prices)), however I can't find race results with final horse place

---

## 2019-06-15 18:23:44 - general channel

**liam**

Currently rebuilding the API / migrating the data. The background was that historical data was to be accessed through the web app, when released I reverse engineered the API and added to bflw as well as highlighting a few issues to betfair. They responded by fixing and adding the documentation, they then underestimated the load from people automating the downloading thus the refactor. 

---

## 2019-06-15 17:59:28 - general channel

**Jonatan (skyw)**

Anyone know if historical data will be available for us again with bad domains  .SE

---

## 2019-06-11 21:13:36 - general channel

**Chris**

Has anyone been able to get back and lay odds from the historical data?

---

## 2019-05-26 09:02:38 - general channel

**liam**

v1.10.0 released which fixes a few bugs (vscode/stop) and a new type of historical data stream (generator) [https://github.com/liampauling/betfair/blob/master/HISTORY.rst](https://github.com/liampauling/betfair/blob/master/HISTORY.rst)

---

## 2019-04-27 11:08:05 - general channel

**jgnz**

hi all, is there anyway to get historical data for non sport events? when i browse through [https://historicdata.betfair.com/#/mydata](https://historicdata.betfair.com/#/mydata) it would appear not

---

## 2019-04-12 09:39:51 - general channel

**phil**

Really interested by this python app - I am about four months into learning Python, and I'm perhaps going to take this on as a side project. My first app was a roulette game which then tested various strategies against a virtual roulette table to see if it could win. It wasn't very sophisticated really, but it was great to try. What I hope to achieve with this app is to download historical data from betfair and test strategies against that

---

## 2019-04-02 21:08:35 - issues channel

**Paw**

Heya, I'm trying to use the streaming example on a football game (Match Odds) where I want to get data in the same format I'd as when getting  historical data from Betfair (streaming dump)

---

## 2019-03-26 05:02:57 - issues channel

**Unknown**

I mean I am looking for the betfair historical data which currently can’t be downloaded from betfair.



I just would like to see some data to play with and write some code while waiting to download the “real” ones.



So maybe someone had some files to share?

---

## 2019-03-25 19:18:59 - issues channel

**Paw**

Following up on the data question -&gt; do we have a secondary historical data market on here :wink: I'm looking for a month of premiership initially to start building my ingestion framework and ML models..

---

## 2019-01-30 13:38:20 - issues channel

**liam**

i don't know where i read this but I think Neil mentioned that they are rewriting the historical data api

---

## 2019-01-30 13:25:38 - issues channel

**Rory**

[@U5D4ZBEAG](@U5D4ZBEAG) I'll try shortly and let you know ... but I've downloaded lots of historical data for the last 3 seasons ... regularly get corrupted files like that .... best bet is to try it again ...

---

## 2019-01-12 18:16:34 - general channel

**Rory**

historical data is a bit of a mess ... times out regularly when trying to download a few months worth of data in my experience

---

## 2019-01-12 17:27:59 - general channel

**Matt P**

Hi chaps, is anyone else having trouble logging into the historical data site? I'm having issues and not sure if it's at my end or theirs...

---

## 2019-01-02 16:39:50 - general channel

**Rory**

brilliant, cheers [@U5D4ZBEAG](@U5D4ZBEAG)... I'm going back through the historical data and can see Utd as runner 48351 as far back as 2015 .... was thinking of using that as a lookup but not 100% sure I can rely on it :grin:

---

## 2018-12-28 17:59:03 - general channel

**Rory**

quick question on soccer asian handicap historical data ...

---

## 2018-12-12 07:53:48 - general channel

**ak**

Hi all! I'm looking into some historical data. May I check why in `RunnerBook` sometimes `book.last_price_traded` is different to `book.ex.traded_volume[-1].price`?

---

## 2018-10-19 17:15:12 - general channel

**rafaelmarch3**

Thanks agberk, I'll take a look. Another question, is there an interface to retrieve historical data without downloading the JSON files and creating a parser for them ?

---

## 2018-10-18 16:56:11 - general channel

**seaders**

(normally with the historical data, the question is how to unzip them, what are they, where did they go, and what does x, y and z mean!)

---

## 2018-10-18 16:51:32 - general channel

**LK**

ok. Allthough that is present in the 'advanced' data I see. But I was assuming that just meant best back/lay (like a BBO in stock-trading). That could still mean that virtual / implied prices are not in the advanced historical data.

---

## 2018-10-18 16:47:19 - general channel

**LK**

Do I understand correctly that in live-streaming data you can opt to see virtual (I would like them implied) prices? But when you buy historical data you only get the actuals back and lay priceladders. (Theoretically you could calculate the virtual prices yourself)

---

## 2018-10-18 16:10:30 - general channel

**LK**

I'll take a look and see if I can reconcile that with my historical data. Thanks for pointing me in the right direction again.

---

## 2018-09-23 15:03:43 - general channel

**cieria**

Hello! I am trying to parse some historical and output into a file, using the code in the example here [https://github.com/liampauling/betfair/blob/master/examples/examplestreaminghistorical.py](https://github.com/liampauling/betfair/blob/master/examples/examplestreaminghistorical.py). I have downloaded the historical data from betfair, an archive "data.tar". If unzipped, it yields a folder structure like C:/data/xds/historic/BASIC/ $many_folders$ /archives.bz2. In the example code, when initiating the historical stream I have tried giving the "directory" parameter as the the path to the BASIC dir, as well as the path to the actual bz2 files, but both cases fail with error "IsADirectoryError" or with "UnicodeDecodeError: 'utf-8' codec can't decode byte 0xdf in position 12: invalid continuation byte" if I give the path to a bz2 archive

---

## 2018-09-20 11:52:21 - general channel

**George**

if you agree we can safely ignore for historical data, then i guess it could be solved by checking a "historical" flag

---

## 2018-09-19 10:34:33 - general channel

**George**

do you have an example of how to parse historical data with a market-data-filter? (e.g. if I only want to parse 3 levels of the book). currently taking hours to parse the raw BF data. Thanks

---

## 2018-08-16 21:43:32 - general channel

**Rory**

yes - I've seen similar from the historical data

---

## 2018-08-16 21:35:44 - general channel

**Disco**

Does historical data contains some spain/italy exchanges data aswell?

---

## 2018-08-07 15:13:56 - issues channel

**man**

I have been trying to use the HistoricalStream to parse historical data with no success. Does any one have sample code which is up to date?

---

## 2018-07-23 16:30:59 - general channel

**liam**

yeah but my backtesting framework is now single threaded so repeatable and runs of a generator spitting out update one by one (historical data), I know there is a word for this but can't remember

---

## 2018-07-10 08:57:21 - general channel

**Ben**

hey guys i had a question, do you guys know a good database of historical data on horse racing? free/cheap?

---

## 2018-05-25 10:56:57 - general channel

**OT**

[@U9RMY3JHK](@U9RMY3JHK) I didn;t know 3rd parties sold that stuff. does it come with betfair IDs mapped? I'd love some runner metadata to go with the historical data :smile:

---

## 2018-05-16 14:49:20 - general channel

**erlend**

Any idea how to get the market catalogues for historical data? When I run list_market_catalogue() with my list of downloaded market_id's it just comes back empty.

---

## 2018-05-15 10:14:08 - general channel

**Chris**

Hi all, just joined this group and getting my head round the Betfair historical data

---

## 2018-05-05 21:04:43 - general channel

**favetelinguis**

I just tried to use betfairlightweight with historic BASIC data and found it very odd that the first message does not contain the complete market book state, it is just a bunch of delta messages. How are you using the historic data if you dont know the entire start state in the first message, you sort of need to consume enogh messages for all runners to have gotten a new delta message?

---

## 2018-04-11 10:39:24 - general channel

**OT**

betfair have fixed up the historical data api.. working great, now.

---

## 2018-04-07 08:02:51 - random channel

**liam**

Nope just the ability to process historical data through it

---

## 2018-04-05 12:27:41 - general channel

**OT**

does the historical data api have some kind of rate limiting on it? because often I just get bz2 files with no market content

---

## 2018-03-18 10:53:19 - general channel

**erlend**

Noob question but if I want to aggregate historical data, should I use [https://github.com/liampauling/betfairdata](https://github.com/liampauling/betfairdata) or [https://github.com/liampauling/betfair](https://github.com/liampauling/betfair)?

---

## 2018-03-04 02:34:58 - general channel

**Henry**

How can i actually get information of all past matches as only event ids are included in historical data and i am looking for their corresponding matches

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

## 2018-02-05 19:20:42 - general channel

**Unknown**

Hi, Does anybody know if Betfair historical data purchases have sportsbook data from downloads off the site? The data I have has identical selection id's but different market i.d. The event name is the same. Any idea what two markets these are? I'm guessing one is match odds would the other one be match odds sportsbook?

---

## 2018-02-01 06:11:16 - general channel

**liam**

Historical data doesn’t contain Xm prices (bdatb/bdatl) 

---

## 2018-01-18 12:10:47 - general channel

**mikey155**

OT, I've been downloading historical data today successfully. I have an issue which may be related - I don't know. The only way I can get at the json data is if I open the bzip files in notepad via 7Zip - exactly the way described in the Betfair guidance on their help page. The problem is I can only do this one fille at a time. I need a way that I can get to, and open in json format, large batches of files.

---

## 2018-01-12 15:40:57 - issues channel

**mikey155**

Thanks that's a good lead. What gets me about Python is that things change so quickly e.g. I'm using Python 3.6 in PyCharm and the word async gives a syntax error. I was able to get round that for the historical data but it might be an issue when I move on to stream API for trading.

---

## 2018-01-12 14:36:31 - issues channel

**mikey155**

I'm new to this site. I'm a python newbie, all of my existing apps written in Visual Basic. Following up the previous discussion on horses names, I'm now drilling into historical data, employing betfairlightweight. Your examplestreaminghistorical works as expected as is, but I'm finding errors (missing positional argument in RunnerBook) when I try to acquire horse names. I tried adding name to RunnerBook but get the same error. Probably a naive newbie error but I thought I'd try to get some insight here. Thanks in advance.

---

## 2018-01-12 13:38:19 - issues channel

**mikey155**

I'm new to this site. I'm a python newbie, all of my existing apps written in Visual Basic. Following up the previous discussion on horses names, I'm now drilling into historical data, employing betfairlightweight. Your examplestreaminghistorical works as expected as is, but I'm finding errors (missing positional argument in RunnerBook) when I try to acquire horse names. I tried adding name to RunnerBook but get the same error. Probably a naive newbie error but I thought I'd try to get some insight here. Thanks in advance.

---

## 2018-01-09 15:03:06 - general channel

**Ian**

Afternoon gents - apologies for the basic request but is there any docs referring to extracting historical data and is [http://www.betfairpromo.com/betfairsp/prices/](http://www.betfairpromo.com/betfairsp/prices/) the best place to obtain data? I presume volume etc must be recorded by oneself and a historical record built that way? I’ve looked at places such as [http://www.juststarthere.com/historical-horse-racing-price-movement-data.html](http://www.juststarthere.com/historical-horse-racing-price-movement-data.html) but not sure how ligitimate that data is as I thought BF held the copyright on it?

---

## 2017-12-31 09:48:53 - general channel

**OT**

Does anybody else have problems downloading historical data from the API? sometimes the content of the market file is just "Error" .. Is this betfair rate-limiting me or something?

---

## 2017-12-24 15:03:39 - general channel

**OT**

thanks, so in historical data it's just correlated to the favourites

---

## 2017-12-16 20:10:41 - general channel

**swt**

Hi, I would like to modify the examplehistorical.py to upload historical data to SQL. Can You help me how to print Event, Market and Selection data. I found Market name is "name", Event name is "eventName", Selection name is the "name" of runners but I could not figure out how to print them. Many thanks

---

## 2017-12-14 02:28:54 - general channel

**seaders**

you're receiving batches of json, 1 per line, in the historical data files you get from BF

---

## 2017-12-11 13:44:57 - general channel

**Tom**

Hi Liam, Thanks for posting your betfair code on github.  I'm currently scraping data that I'll use for machine learning. I'm currently after highest price and lowest price matched data to establish ranges that I can use for machine learning on tennis data from 2016. I've downloaded a tar file which I planned to use with a python script and OS walk path. When I open the file there's thousands of subfolders and zipped files and I'm having issues trying to normalize the data to CSV.  I’ve seen your 

[https://github.com/liampauling/betfair/blob/master/examples/examplehistoricdata.py](https://github.com/liampauling/betfair/blob/master/examples/examplehistoricdata.py) file and I’m wondering since you have experience with betfair historical data if you could point me in the right direction? All I want to do really is build a list or dictionary in either json or csv to show Player names tournament name and highest lowest price matched inplay. Would you know if this data is available on the basic plan through betfair api?

Whats the best way to get betfair data into a pandas dataframe?

Your advice would be greatly appreciated! Many Thanks, Tom

---

## 2017-12-09 11:30:35 - random channel

**OT**

Anybody seen this error when dealing with the historical data?

---

## 2017-12-02 12:10:37 - general channel

**POR**

[@U4H19D1D2](@U4H19D1D2) Hi Liam, just found your stuff for extracting the Betfair Historical data to .csv format. I used the examplestreaminghistorical.py you have it github. I'm just wondering what I need to edit to extract all the data fields to a file, not just the specific ones like "Time,MarketId,Status,Inplay,SelectionId,LastPriceTraded". I'm not great at getting my head around monogramming.

---

## 2017-11-02 18:47:05 - general channel

**seaders**

I don't use the historical data too much as we record basically everything we use in our strats

---

## 2017-11-02 18:42:41 - general channel

**liam**

i started but got really bored so just focussed on parsing the historical data, much much quicker

---

## 2017-10-26 21:07:47 - issues channel

**liam**

Yeh performance is an issue, I have moved to golang for parsing historical data 

---

## 2017-10-26 20:45:08 - issues channel

**OT**

take the historical stream example and set the listener to lightweight=True.. actually now that I mention this, maybe it's to do with the historical data.. :confused:

---

## 2017-09-11 02:30:41 - issues channel

**gerg**

Why I am not seeing these fields in the historical data... Sorry to bother you, but can you provide me with links to some docs to understand more on calculating ODDS?

---

## 2017-09-09 21:52:34 - issues channel

**liam**

You need to add the file name of the market you have downloaded and unzipped from the historical data website to the end of that directory 

---

## 2017-09-09 04:44:28 - general channel

**gerg**

I downloaded the historical data from the website and I could clearly see "OODS" column in it, Following are the column fields in historical data 

"SPORTS_ID","EVENT_ID","SETTLED_DATE","FULL_DESCRIPTION","SCHEDULED_OFF","EVENT","DT ACTUAL_OFF","SELECTION_ID","SELECTION","ODDS","NUMBER_BETS","VOLUME_MATCHED","LATEST_TAKEN","FIRST_TAKEN","WIN_FLAG","IN_PLAY"

---

## 2017-06-23 20:29:16 - general channel

**gerg**

[@U4H19D1D2](@U4H19D1D2) Thanks for answering my query.. Where can I get these historical data for free (I am not using it for commercial purpose)?

---

## 2017-06-23 19:49:35 - general channel

**gerg**

Im new to this group..How can I use this to get historical data of item soccer of year 2016 ? Any help is greatly appreciated

---

## 2017-05-31 16:34:25 - general channel

**liam**

Historical data has been released:

---

