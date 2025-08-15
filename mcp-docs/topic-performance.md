# Performance - Community Knowledge

*1579 relevant conversations from across all channels*

---

## 2025-01-26 08:28:15 - strategies channel

**Unknown**

Big week this week and it all came out of the meetup on Tuesday



I had an idea for a new strategy while chatting to [@U01PJ5YMFBJ](@U01PJ5YMFBJ) and while it took a few days to go from idea to implementation (both o1 and DeepSeek made a complete hash of it), the backtest looks great - see first attached plot. I've live tested it on a couple of races and am looking to deploy it more widely today. This is now `Strategy3`



Also at the meetup, [@U05SRUKGYCC](@U05SRUKGYCC) made some comments that gave me some perspective on `Strategy2`. It helped cement my feeling that it's not contrarian enough and I need to revert to the original vision of the strategy. I've started work on a third iteration of it with promising signs. I had really hoped I was going to be able to report today that I'd gone live with _both_ `Strategy2` and `Strategy3` this week but sadly not quite there yet



Existing strategies got absolutely crushed this week and that unfortunately coincided with it being my turn to run them. My already considerable shortfall is now even larger. Although they've been running for years, variance like this is still stressful when you're personally making the losses even if it all gets accounted for. However, these emotional factors are easier to handle being part of a group that can provide perspective and shared experience



New strategies flat on the week so far after a bad day yesterday (my naturally pessimistic disposition thinks there's still plenty of time for them to get further in the hole for the week) but the losses seem in line with variance and I'm not at all concerned (yet). I did increase stakes on `Strategy0` on Monday and it's probably past time I increased stakes on `Strategy1` as well



Plan for the coming week is to get `Strategy3` as widely deployed as possible - I'll need to check backtest performance on US/rest of world horses, and see what I can do about testing it on greyhounds as well. I have a feeling the strategy should work well inplay but backtests look awful. I'm actually specifically interested in getting it working for inplay football but that probably needs a fair bit more work than just tuning some parameters



Development-wise the main focus will be trying to finally get `Strategy2` over the line

---

## 2025-01-25 14:25:54 - issues channel

**R**

Has anyone ever noticed memory leaks when using flumine to collect data?  We've restarted an old collector system and find its crashing.



Of course, we've double checked it's not something on our side RE post processing and storage.  I'm sure it's something benign that we've missed, but it seems like flumine is holding on to market data even after close.



Anyone found something similar?

---

## 2025-01-24 19:59:10 - random channel

**Gooat**

[@U01B8031PM1](@U01B8031PM1) are you using it instead of something from openai or anthropic? Similar performance?

---

## 2025-01-22 09:43:52 - general channel

**D C**

Yeah I've found that for inplay too [@U05N9773A23](@U05N9773A23) when combining price and GPS into a model - the price just dominates. I think using market price makes more sense for pre-off as pre-off prices are only reflective of current market sentiment, whereas inplay prices are more reflective of the true probability (excluding things like high volatility periods and information latency etc.)

---

## 2025-01-19 12:59:23 - strategies channel

**Unknown**

It's been a frustrating week trying to get `Strategy2` to the point where I'd be comfortable redeploying it



On Monday I started by increasing the exposure limit on `Strategy1` for in play horses to bring it in line with what I've used for backtesting. I haven't spent much time using backtests to gauge how much I can scale everything up but that's perhaps something to start thinking about



I wasn't planning on doing this but I decided on Monday to also compare `Strategy0`'s live bets to the backtest and discovered some big problems with my execution which meant I'd missed out on - very roughly - about 15,000 bets over the past three months. This was largely down to handling the start of races and using the `marketStartTime`. I've completely overhauled the logic and it appears to have fixed things. I made a separate tweak that should also help reduce the number of missing bets but, checking that now, it's been somewhat less successful



Right, back to `Strategy2`. I've definitely made significant improvements to the model over the past week but none of the changes have translated into a meaningful shift in backtest performance. Intuitively, where the model is strongest it must just be agreeing with the market. However, I did have a small breakthrough last night with the filters I'm applying to try to avoid adverse selection and I think the strategy is just about at the stage where I'm happy to start live testing it again today. I don't think the backtest performance is quite good enough but the thing that convinced me it's worth live testing is that I can run it against many more markets than I have scraped prices for - i.e. all of the `OTHER_PLACE` markets. As in my last update, I can use BSP to quickly assess whether it's actually finding value on those markets. The breakthrough I'm referring to should apply to pretty much any taker strategy so I'm excited to apply it to other strategies



So the plan for the rest of the day is to manually run the strategy against today's UK racing and I also still owe my syndicates another couple of hours work for the week. Looking to next week, I should fit `Strategy2`'s model to Australian racing and backtest it again to see how that's looking. I do have one other big model improvement on my to-do list that I'll action and a couple of suggestions from o1 that I think are worth exploring but I haven't thought about what's next beyond that. I'll review my list of strategy ideas and have another chat with o1



A couple of general findings from this week:



1. It really helps to step away from the computer. All of my big breakthroughs in thinking came from taking a shower or cooking dinner or walking the dog

2. o1 continues to be indispensable. It's at least as good as if I had a junior quant working for me

Update on performance:



1. Got rotated back into syndicate strategies yesterday. We've been undertaking a large reconciliation exercise, the end result of which is that I'm quite a bit behind of my share so I imagine I'll be in rotation for a bit now

2. New strategies had a bad couple of days midweek and have been absolutely crushing it since then

New strategies net profit up to 2.3% of existing strategies net profit!

---

## 2025-01-17 09:39:10 - general channel

**Ralegh**

Any idea what the overhead for betfair vs tpd direct is? Would be surprised if it’s taking more than 50ms to go through their system plus latency across open internet 

---

## 2025-01-17 09:28:42 - general channel

**D C**

You must have been filling your boots nicely then when the BF feed went to shit at the end of last year!!! I'd say you are getting a decent latency advantage over us on the BF feed if you are getting it pushed directly over UDP from TPD direct. And massive advantage to the OTS ladder trader boys what with all the overheads that a graphical desktop app will have. I think that feed that TPD provide is limited to 200ms refresh rate too when last I looked although admittedly it comes with some nice extras like course par times.

---

## 2025-01-17 09:23:14 - general channel

**Justice**

[@UUE6E1LA1](@UUE6E1LA1) I'm just muddying the signal :joy::joy: Though I do maintain that the inaccuracy is hugely frustrating. Whenever my model is wrong and I get picked off, I'd say 95% of the time it's due to an inaccuracy in the data. I'm curious as to whether the data from the other courses will be using the same technology and whether it will be any more accurate. I can imagine there is a very small latency advantage but I don't know if this is significant. I also found I can subscribe to duplicate feeds for redundancy so dropouts are very minimal

---

## 2025-01-17 09:16:17 - general channel

**D C**

i find this really interesting - it doesn't seem that long ago (although it probably was) that you were saying that GPS was rubbish and was too error prone to yield any edge! Now you are paying TPD for a direct sub - so you are going to have a latency advantage over any of us getting it from Betfair and a presumably massive latency advantage over Gruss/BA/Betmover integrated GPS users. And yet you are worried about alpha decay ???? I share your view on the need for diversification though.

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

## 2025-01-11 11:44:21 - strategies channel

**Jonjonjon**

Yes we could. Is there a reason your stakes aren't double what they are? For me, it's because my performance declines.

---

## 2025-01-11 09:23:12 - strategies channel

**Jonjonjon**

[@UBS7QANF3](@UBS7QANF3) do you know how your syndicate's overall performance would be affected, if on a particular day two of you traded, instead of just one?

---

## 2025-01-10 11:24:01 - strategies channel

**Unknown**

I haven't really settled on a definitive schedule for publishing these but I figured I'd probably be too busy this weekend so I'm getting this week's update in early



It's been a hard and frustrating week grinding away on `Strategy2`



First up, as mentioned in my [https://betcode-org.slack.com/archives/CTPL3R3FU/p1736081164005719|last post](https://betcode-org.slack.com/archives/CTPL3R3FU/p1736081164005719|last post), I increased stakes on `Strategy0` and `Strategy1` on Monday (2025-01-06). My plan is for these to increase in line with the notional bankroll I have set aside for this collection of personal strategies, and for this bankroll to grow organically. If I find a strategy that I'm extremely bullish on and think it could benefit from an injection of capital then I will obviously do so but that's not (yet?) the case for `Strategy0` or `Strategy1`.



So, `Strategy2`. I've been alternating between thinking I've cracked it and thinking all I have is a horribly overfit hot mess. I started off very quickly making progress in overhauling the model and staking which:



1. Permitted trading on all runners, not just the favourite

2. Widened the number of markets that could potentially be traded

3. Takes current position into account, hopefully resulting in smoother returns

The progress was such that on Wednesday (2025-01-08), I switched off "V1" and deployed "V2". I observed the bets for V2 in a few races and noticed it wasn't doing a great job of beating BSP. Small sample size obviously but I decided to switch it off and dig into the backtests a bit more



First up I confirmed in the backtest that bets which beat BSP do great and bets which don't beat BSP are bad. So it's not like my model is so good that it can identify times BSP is wrong (at least in aggregate)



This strategy and, to a lesser extent, `Strategy1`, has a variety of filters applied to the trading signals. Things like requiring a minimum expected ROI (EROI) to bet, but also not exceeding a maximum EROI. Also some traded volume and other market "quality" indicators like overround/spread in an attempt to restrict to situations where confidence in the model predictions is likely to be highest



Initially I had optimised these filters using backtest realised returns but based on my increased understanding of the importance of beating BSP for this strategy, I went back and included expected value calculations in the optimisation process. This suggested that I'd overfit many of these filters and so I went back and re-optimised them using expected value with the result that several of the filters were discarded in their entirety. The backtest performance although arguably now more likely to reflect future returns looked significantly less impressive by the end of this process



For both backtesting and the live trading that's been done with the strategy, such that it is, I've been focusing on UK horse racing. However, I'm very keen to get it working in other jurisdictions and also on greyhounds. For obvious reasons:



1. The more markets it can trade, the quicker live feedback can be had

2. More markets traded = smoother returns

3. If it can widely scaled then the per bet performance doesn't need to be amazing

I do have some problems with lack of data, however:



1. I haven't been scraping greyhound markets for very long

2. I only realised this week I haven't been scraping horse racing `OTHER_PLACE` markets (now corrected)

3. No doubt there are other market types I'm still not scraping that I am ultimately interested in (e.g. Each Way, AvB, Without favourite, all exactas/quinellas/forecasts/reverse forecasts/perfectas/superfectas/trifectas/etc. and all aliases thereof)

This lack of market data to backtest against is one reason why I'm so keen to nail down the model building process and to rely less heavily on the market based filters. If I can be confident that I'm building a market beating model in cases where I do have the market data, then I am more inclined to cautiously deploy the model to other markets and rely on live results for feedback



I mentioned in my last update that as part of this strategy I wanted to look at extending both Shin's method and Kelly staking to handle markets with multiple winners. I've had some generic insights into these that I think people may find useful:



1. The R package [https://cran.r-project.org/web/packages/implied/index.html|implied](https://cran.r-project.org/web/packages/implied/index.html|implied) already implements Shin's method for multiple winners. However, it simply finds a value of `z` numerically using the existing formula. I don't believe this is correct as the starting assumptions under which Shin derived his model are not applicable for multiple winners. Nevertheless, this approach may be practically useful if not conceptually sound

2. A recently developed alternative to Shin is [https://github.com/gotoConversion/goto_conversion|GOTO (Gambling Odds To Outcome) Conversion](https://github.com/gotoConversion/goto_conversion|GOTO (Gambling Odds To Outcome) Conversion). This method apparently has serious chops, having been used in several gold medal winning solutions on Kaggle. It appears to be able to handle cases with multiple winners trivially. However, I observed some issues using the method in practice. Firstly, the code does not seem to be very well written, requiring me to fork the repo and make some changes. Secondly, the method produced negative probabilities for the BSP on a completely unremarkable horse racing WIN market. Also worth noting that most if not all of the motivating analysis supporting the method focuses on markets with few winners like football and therefore there's much weaker evidence that it would outperform Shin in horse racing. The repo is not configured for me to create a GitHub issue to discuss these concerns with the author so I have reached out to him on LinkedIn but have yet to receive a response

3. ChatGPT, o1 specifically, has been extremely useful for strategic discussions about developing `Strategy2`. In my opinion, a product like it is becoming increasingly essential if you work by yourself

4. I'm no longer planning on extending Kelly staking to handle market with multiple winners but while looking at it I noticed that the way I've always done fractional Kelly staking is wrong. This has implications for my existing strategies and it's gratifying that looking at new markets in new ways can lead to widely applicable fresh insights in this way

Update on performance with reference to the attached plots:



1. I got rotated back into the syndicate strategies for a day, made a load of money and got rotated out

2. New strategies took a few days to dig themselves out of the hole but they've done it

3. Looks like `Strategy1` in play is really carrying water

New strategies net profit up to 0.77% (from 0.4%) of net profit of existing strategies so everything is moving in the right direction!



Plan for the coming week is to continue to grind away on `Strategy2`, mainly focusing on the model, and hopefully getting it to the point where it can be redeployed to UK racing. Next step after that will be getting it deployed to Australian racing then US racing then perhaps rest of world if it seems worthwhile, followed by greyhounds. I haven't thought about what's next after `Strategy2` but last count I have ideas for 11 other strategies on my list. Other syndicate members will be back to work on Monday so I'll be back to working on existing strategies next week as well

---

## 2025-01-07 11:22:30 - strategies channel

**Jonjonjon**

Interesting.... Have you had much luck incorporating stuff like that into your price action models?



I tried adding stuff like hour of day, day of week, recent performance Vs other runners,  but didn't really get anything worthwhile from it.

---

## 2025-01-07 00:39:17 - general channel

**Alex A**

I’ve asked on here before and some people have said they can happen on the initial snapshot, but I still haven’t seen it, and processing the snapshot faster is very unlikely to noticeably improve my betting performance.

---

## 2025-01-06 22:42:48 - strategies channel

**Jonjonjon**

When those talk about time series, do you think they are referring to some unobservable latent measure of team performance, or time series of prices on a runner?

---

## 2025-01-04 14:50:48 - strategies channel

**D C**

Interesting. I've just done a very basic DB profit analysis looking at averaged profit in bands of days 1-10,11-20,21-30 (ignored 31st for simplicity) and I see the opposite of what you are - best performance in the FINAL third of the month (on average) by quite some margin.

---

## 2025-01-03 22:58:39 - general channel

**Jonjonjon**

I trade the greyhounds from the UK. My matched volumes and performance haven't changed that much since Dec 30th.

---

## 2024-12-24 09:58:52 - strategies channel

**foxwood**

Quite dramatic. Since you're offering I'd look for things that might have changed suddenly that could impact your signal(s). Latency, timing, server upgrade, software upgrade - faster/slower performance, cross matching are a few. Left field thought is that whoever you were feeding from pre-off went wholly inplay 6 months ago and affected you on both counts.

---

## 2024-11-30 13:41:19 - strategies channel

**Jonjonjon**

Didn't someone post some analysis about benchmarking performance Vs prices at some point in the future? Have you tried that?

---

## 2024-11-30 10:48:07 - strategies channel

**Mo**

Second related question: what is your workflow for going from idea to live trading strategy? Mine is usually:



1. Get told about an idea ([@U012XF5CNPN](@U012XF5CNPN) leaking alpha) or reading about one (in a book that [@UPMUFSGCR](@UPMUFSGCR) has dismissed out of hand)

2. Validate idea by doing some basic analysis on summary data eg BSP data

3. Confirm idea looks good in a backtest, mainly looking at the equity curve (is it up and to the right, how do the drawdowns and other variance characteristics look)

4. Validate backtest by live trading small stakes and comparing live trading results to backtests on the same events

5. Scale up stakes in line with live trading performance



---

## 2024-11-30 10:30:02 - strategies channel

**tone**

Well, that depends on how you define "fail". You have an expectation of performance prior to OOS, and, invariably, performance is poorer than expectation in OOS, but you might be prepared to optimise if performance is still tolerable.

---

## 2024-11-27 10:46:33 - issues channel

**foxwood**

That one latency message comes from _process_market_books() - if there were true latency on the stream I'd expect to see loads of standard bflw messages of the form "levelname": "WARNING", "message": "[MarketStream: 2001]: Latency high: 0.60121750831604". Possible application loops not getting back to process_market_book in time ? Try profiling or putting more traces in.

---

## 2024-11-27 09:53:33 - issues channel

**liam**

and i can already see a latency warning, what is `OrdersMiddleware`?

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

## 2024-11-27 08:33:29 - issues channel

**liam**

this sounds like your code, and you are 100% not getting any latency warnings?

---

## 2024-11-27 08:31:20 - issues channel

**liam**

whats a server/API rule? The logs will tell you if your code is the problem re the latency warnings

---

## 2024-11-25 11:15:00 - strategies channel

**Joe**

[@UBS7QANF3](@UBS7QANF3) To answer 1-5 I have an IO front end with a little dsl that can extract data from the compressed json stream files, fast enough like [2min per year of global racing, but this is largely because there is minimal impedance mismatch between IO and compute and memory in my implementation, it is using very fast local storage and lots of cores for parallel decompression, this is the same point that <@US2RWCWKY](2min per year of global racing, but this is largely because there is minimal impedance mismatch between IO and compute and memory in my implementation, it is using very fast local storage and lots of cores for parallel decompression, this is the same point that <@US2RWCWKY) was making.



To back test / train / ML that same IO front end is used but to fill memory structures whose contents are 'implied' by the strategy being trained and shape/order optimised for the hardware (e.g. gpu structures will be totally different shape to cpu). In other words it only keeps the answers to the questions it is likely to need during training and puts them in the memory location that will guarantee the lowest latency during training given the expected order those questions will be asked in. This is the data equivalent to dead code removal during compilation followed by compile time optimisation. The training process then only iterates over these memory structures at high frequency. To do this and ensure that the 'logic' being trained will behave identically when run in production on live streams requires everything be written against interfaces that are implemented multiple times. This is similar to what [@U012XF5CNPN](@U012XF5CNPN) alluded to in point 3. It could also be thought of as a very application specific cache.



This would be quite a departure from how Flumine works where there is no real change between live and back testing other than inserting the simulated matcher.

---

## 2024-11-24 15:11:00 - strategies channel

**Jhonny**

[@UBS7QANF3](@UBS7QANF3) I don't see why #6 isn't possible. I mentioned I don't do it simply because my stack is in clojure, not python. But, yh, I do have backtest speed and flexibility (I'm still working on this part tho). Maybe even have 2 storage formats optimized for different needs if needed.

---

## 2024-11-24 15:05:13 - strategies channel

**Oliver**

a potentially cheap experiment would be to add a caching layer that takes your back testing input (recording JSON) and then pickles it. e.g.

```USE_PICKLE_CACHE = bool(os.evnrion.get('USE_PICKLE_CACHE'))



def my_pickle_cache(inner_function):

    """Use a cache if enabled with a non-empty USE_PICKLE_CACHE value in the environment."""



    if not USE_PICKLE_CACHE:

        return inner_function

    @functools.wraps(inner_function)

    def cacher(filename):

        cache_path = f'{filename}.pkl'

        with open(cache_path, 'rb') as f:

            return pickle.load(f)

        result = inner_function(filename)

        with open(cache_path, 'wb') as f:

            pickle.dump(result, f, pickle.HIGHEST_PROTOCOL)

        return result

     return cacher



@my_pickle_cache

def read_normal_json_input(filename) -> list[dict]:

    ...```

then you cache once. If IO rate is the issue (probably a natural follow on to test), you could replace the `with open(...)` stuff with `with gzip.open(...)` and use something like level 4 compression, which I suspect is around the sweet spot for maximising throughput.



The pickle version is a variable that can have a bit of impact on its performance, so something to experiment with, just like compression level.

---

## 2024-11-24 14:22:50 - strategies channel

**Mo**

Some use cases I have:



1. Get the market books for all markets just before they turned in play

2. Get the market books corresponding to the times that my bets got filled

3. Extract the winner(s) of every market

4. Calculate the total volume traded for every market

5. Get the market books before and after X minutes before the market start time

6. Speed up flumine backtests

---

## 2024-11-24 13:10:38 - strategies channel

**liam**

Do you think this would solve the problems you are trying to solve vs just improving the speed of processing the raw stream? ie. get the Rust wrapper up to a level it can be used

---

## 2024-11-23 22:12:18 - strategies channel

**Oliver**

not exactly what you asked, but I moved away from the stream JSON format in my engine. The input is of course still JSON as from the stream, but I parse it straight into a point-in-time representation (practically just an array) which is only allocated once, so avoids the creation of a whole bunch of hashes and lists that then get thrown away every update. It makes processing a whole load faster - more of a point1 thing. This applies to both back testing and real world when done like this. In theory a timeseries of the point-in-time version could be something to get fancy with in serialisation/deserialisation e.g. arrow for a more natural representation, or something smarter re. compression maybe along the lines of gorilla timeseries compression.



regarding lookups, I've been aiming to do pre-processing to extract metadata like the market definitions, to place alongside market recordings. It should works fairly nicely in the archive format you get from the historical data API i.e. tar containing files for individual markets + combined streams. At the moment the best I actually do re. lookups is just reading the first message of a market's recording to determine if it matches the market filter, but if not skip on.



Doing that with fairly speedy disk (NVMe), a memory mapped .tar of recordings, and reading in a separate thread, doesn't feel bad even with implementations that have a load to `TODO: simplify/speed up/profile` littered throughout them. It takes about ~2m to go through a day of UK WIN horse racing markets, picking them out from all UK horse racing markets for a day.

---

## 2024-11-18 08:59:53 - general channel

**Gooat**

That is peak performance Paul

---

## 2024-11-17 21:43:28 - random channel

**Clive**

The new mini is nice, but you don’t get much memory without forking out for it. The m4 in it is very very good - especially for single core performance. 

---

## 2024-11-17 19:04:42 - random channel

**Derek C**

I just got an M4 macbook pro and the performance is phenomenal.

---

## 2024-11-17 18:10:00 - random channel

**Jonjonjon**

Omg. I had thought apple stuff gave poor performance/$. I guess I was wrong.

---

## 2024-11-17 17:38:33 - random channel

**Paul**

Under the hood, macOS is one of the best OSes out there. Open source package management via homebrew is better than anything else I've used elsewhere, everything "just works" due to vertical integration - no driver hacking - it's a solid stack. And while people say Apple is expensive, weirdly, for the new Apple Silicon stuff it's actually remarkably cheap for that performance level...

---

## 2024-11-17 17:29:30 - random channel

**Paul**

Just checked, the stats I saw were adjusting for power consumption as well. Raw performance you might be better off with Xeon or Ryzen, but your power consumption will be much higher and I think the SKU price will be higher (the Mac tested here is a $600 complete system, including RAM, storage, PSU, etc): [https://www.phoronix.com/review/apple-m4-intel-amd-linux/5|https://www.phoronix.com/review/apple-m4-intel-amd-linux/5](https://www.phoronix.com/review/apple-m4-intel-amd-linux/5|https://www.phoronix.com/review/apple-m4-intel-amd-linux/5)

---

## 2024-11-17 17:19:20 - random channel

**Paul**

macOS is a BSD unix under the hood, which I would contend, on many points is > Linux. Performance/$ the M4 is in a different class to anything you can run Linux (or Windows) on, and even if the Mach microkernel scheduler was crap and BSD sockets were in your way a bit, you’re probably going to end up still ahead than you would on a similarly priced PC, if you’re CPU bound. GPU bound, things get different.

---

## 2024-11-17 13:53:52 - random channel

**Dave**

Thinking of updating my local box (which I use for backtesting), which may mean moving from the older to newer CPU in this comparison. [https://cpu.userbenchmark.com/Compare/Intel-Core-i7-4700MQ-vs-Intel-Core-i7-13650HX/2727vsm2049566](https://cpu.userbenchmark.com/Compare/Intel-Core-i7-4700MQ-vs-Intel-Core-i7-13650HX/2727vsm2049566) Any ideas how I can guage how much of a performance bump I can expect? The latter CPU is just one I've pulled from an arbitrary top of line performance laptop. I believe most of my backtesting is cpu-bound and not io-bound.

---

## 2024-11-16 23:56:42 - random channel

**James**

Caveat here though is a lot of my stuff is pre play or not massively latency sensitive so I haven’t had to push it too much.

---

## 2024-11-14 10:17:19 - strategies channel

**liam**

btw `100ms of code latency` is absurd, i aim for sub 1ms

---

## 2024-11-14 10:09:11 - strategies channel

**liam**

So you have these available



[https://github.com/betcode-org/flumine/blob/a9cd71befc6062b52ce65ca695b50a56a2e81344/flumine/config.py#L26](https://github.com/betcode-org/flumine/blob/a9cd71befc6062b52ce65ca695b50a56a2e81344/flumine/config.py#L26)



You can be clever and set them to negative values up to the betDelay



```from flumine import config

config.place_latency = -0.5```

---

## 2024-11-14 10:06:19 - strategies channel

**tone**

I'm trying to determine the potential value in shaving milliseconds from latency but I figure it might be possible to get a rough idea by shortening the betDelay. Say my orders take about 1200 ms to hit the market. 1000 betDelay and 200 code + wire latency. I figure if I could alter betDelay to, say, 900ms that would give me a steer on what shaving 100ms of code latency would bring!

---

## 2024-11-14 10:03:13 - strategies channel

**liam**

ie the betfair betDelay or the latency bet delay? Also what is the context?

---

## 2024-11-06 07:21:00 - random channel

**Michael**

Ok I'll start then shall I? I think laying Trump was the right bet based on the information we had, but I think there are words to be eaten about the performance of the market, and I did say that the confidence being expressed was not well founded.

---

## 2024-11-04 14:18:28 - general channel

**Daniel**

Ah fair - creation of their objects upon reading the serialised data could be a decent impact on latency

---

## 2024-11-04 10:07:34 - general channel

**liam**

Np with the first, I have speed/latency concerns with the second, Enums are slow, would need to test/profile 

---

## 2024-11-01 03:32:12 - general channel

**Phydeaux**

I have a "home lab" for other reasons, with NAS and a decent amount of compute so I've not deployed to the cloud. I am rural so have a good amount of solar and batteries, so even the electricity is free. The capex was relatively chunky, but built for other reasons, so the marginal cost to use it for betting / analysis was basically zero apart from my time.



Network latency isn't a concern for my strategy, but if it was I'd do a little testing to find which GCP/AWS/other zone is "closest".

---

## 2024-10-31 10:28:25 - general channel

**James**

Following on from Paul’s recommendation, I work with AWS in my day job extensively but don’t have the same limitations he does. Lightsail and Fargate serverless containers, and s3 for storage. Along with using a neon Postgres or digital ocean Postgres (for no cold start) is what I use for my market catalogues and betting records. Most of your record keeping can happen in background threads and can afford to be a little slower. 



Lightsail and neon are a bit more batteries included and a good place to start, and less knobs go turn. Fargate and a dedicated DB can let you squeeze some more out as you get deeper into it. 



This setup means my costs are low. I run my sims on my own hardware, even if slow it doesn’t cost me anything except electricity :relaxed: 

---

## 2024-10-31 07:50:50 - general channel

**James**

AWS Ireland tends to be best for latency from what I’ve seen. 

---

## 2024-10-23 11:20:23 - random channel

**D C**

[https://www.totalperformancedata.com/triplesdata-and-total-performance-data-merger-talks-end/](https://www.totalperformancedata.com/triplesdata-and-total-performance-data-merger-talks-end/)



I'm a bit confused by this - I thought they had already merged? Leaves me wondering how this affects any future access to GPS tracking for AUS racing.

---

## 2024-10-10 12:52:24 - general channel

**Brøndby IF**

Hi [@U4H19D1D2](@U4H19D1D2) I don't know if I really pushed it too far, because the test I did was with 6 simultaneous charts, but I'm analyzing whether it could be the fault of some kind of escape, since there is a script trigger for each of them, with the intention of being asynchronous. I managed to solve the memory accumulation, by the way.



I'm also thinking about generating the requests with Python and sending the JSON data to be processed by HTML instead of using JS for this, perhaps it will provide more security and stability.



But if I do notice that there is such a limitation, I will use the graph api to learn and reproduce it using the official API.

---

## 2024-10-06 14:16:06 - random channel

**D C**

This is nothing new. Race reading and horse body language courses have been around for a long time. Hunt for profit, everyone's favourite "polymath" Tony Hargraves. All the drone does is reduce your video latency. It's the same old shit, just pushing the drone angle to those who don't even realise what kind of video feed latencies are involved and how far down the food chain they actually are. Drone pics are an edge for those who know what they are looking at with horses and jockeys (not me I hasten to add) and have the patience to sit in front of a ladder and a video screen all day.

---

## 2024-10-03 21:19:57 - strategies channel

**JL**

oh it's wrong? I did it similar to: [https://www.quantstart.com/articles/Sharpe-Ratio-for-Algorithmic-Trading-Performance-Measurement/](https://www.quantstart.com/articles/Sharpe-Ratio-for-Algorithmic-Trading-Performance-Measurement/)

---

## 2024-09-26 16:09:52 - random channel

**ShaunW**

Haven't used o1 yet but I'm finding the new 'memory' feature to be a blessing and a curse. Once it's on the wrong track it's always been stubbornly wedded to it and those errors in understanding now compound across conversations.     I'm closing some convos with 'don't commit this to memory' because of it. The memory feature also raises new privacy issues imo.

---

## 2024-09-25 00:23:11 - random channel

**Jonjonjon**

What sort of performance boost when backtesting with Flumine, did people get when upgrading to python 3.11?

---

## 2024-09-21 13:04:23 - general channel

**TT**

How do people typically go about logging/monitoring latency? In particular the latency between betfair's publish time and the clock time when the update is received?



I can think of a couple of ways of doing it:

1. In the market recorder you could log it on each update [https://github.com/betcode-org/flumine/blob/master/examples/strategies/marketrecorder.py#L69|here](https://github.com/betcode-org/flumine/blob/master/examples/strategies/marketrecorder.py#L69|here). (Might be a bit overkill for each update but it would be complete.)

2. Have a background worker log the latency metric to Cloudwatch Metrics/Prometheus etc every x seconds.

Its not something I've been recording but if you want to optimise it (by moving aws region/vps etc) then its important to start tracking it.

---

## 2024-09-05 19:39:20 - general channel

**Rob**

Obviously what I want to avoid!



I can't see any way that flumine is using >1 core, so if that's the case, and my code is too slow, I  guess I can offload the data processing/model scoring to a locally hosted API which can use all the cores, and have the flumine `process_market_book` code call that.



Anyone else do that, or anything similar?

---

## 2024-09-05 19:04:15 - general channel

**Rob**

I'm just about ready to use flumine for live betting for the first time (rather than simulation).



Based on what I've read here, I know I'm doing more heavy computation that others. I'm happy with the speed of simulation but that's using 10 cores, and I'm not clear if flumine can use >1 core when running live? If a `process_market_book` call is still running when the next update arrives, what happens?



I'll try it tomorrow night so I guess I can also find out that way :slightly_smiling_face:

---

## 2024-09-04 19:33:20 - general channel

**Sam G**

Hi [!here](!here) i have been a relatively quiet watcher on this slack workspace - and want to dive in more and learn about the ins and outs of sports betting coding. I have been a python programmer for over 12 years, and some C++ and Java before that ( was in high frequency trading in finance sector). I have a property tech startup that I am winding down (due to business profitablity slowing down) and I want to go back to my love of quant + programming in sports betting, an area that I have slowly picked up some interest in. I also learnt Rust for last 1.5 years, used it on my own startup (which really didnt need Rust but used it to learn) and want to see if I can use Rust knowledge in bet-code



I also helped start a crypto trading firm (so have some relatively newer experience in programming for excahnge trading - around 2018-2020 - was working part time with them)



I learnt a bit of the betfair api - but not much,and want to dive in.



*questions:*

1. What are the best resources to learn production level (or near production level) sports betting. Are there good videos or paid training material that explains a lot of things in one place? 

2. Is someone looking for a partner to do it with - perhaps someone who knows more about the sports betting side of things, and some programming experience - and I can help them with my knowledge in programming ?

Will be good to help others and learn in the process



Thanks again

---

## 2024-08-29 15:33:23 - issues channel

**casper**

[@U4H19D1D2](@U4H19D1D2) I’m using poetry and when going from 2.20.1 to the latest 2.20.2 version it uninstalls ciso8601 module. I have the following line:

```betfairlightweight = { version = "2.20.2", extras = ["speed"], source = "pypi-store" }```

So simply bumping the version here uninstalls ciso8601 for me (one of the “speed” requirements). Going back to 2.20.1 installs ciso8601 again. Any ideas what might be happening?

---

## 2024-08-28 22:25:53 - random channel

**Rob**

The 9950 benchmarks somewhere towards double the 3950x, so I'd expect you're right about the speed up you'd get. After that you're pretty much in threadripper territory, if you don't want to cloud.



Obviously don't know what you're doing, but I tend to just do as much as I can in a reasonable amount of time. Most ML stuff has diminishing returns (e.g. you can build a model that's 98% as good in 1/100th of the time), but sometimes you need the extra performance.

---

## 2024-08-28 06:54:00 - strategies channel

**liam**

[https://betcode-org.github.io/flumine/performance/|https://betcode-org.github.io/flumine/performance/](https://betcode-org.github.io/flumine/performance/|https://betcode-org.github.io/flumine/performance/)

---

## 2024-08-26 14:27:51 - random channel

**Unknown**

Racehorse Success Secret: Gut Bacteria in Foals Could Predict Future Champions!



A recent Nature article examines how the gut microbiome of young racehorses influences their future health and athletic performance. Researchers found that foals with higher gut bacterial diversity at one month old were less likely to develop respiratory diseases and performed better in races up to three years old. Conversely, antibiotic exposure in the first month reduced microbial diversity, increased disease risk, and negatively impacted racing success. These findings highlight the importance of early gut health in determining long-term outcomes.



For more details, you can read the full article here: [https://www.nature.com/articles/s41598-024-64657-6](https://www.nature.com/articles/s41598-024-64657-6)

---

## 2024-08-24 14:54:24 - random channel

**Jonjonjon**

What's the recommended way to work out the best optimisation route for calibrating tabular models such as xgboost, catboost, random forest etc ..?



My models are taking around 100seconds to fit on my cpu. I fit hundreds of models.



I use a 16 core Ryzen 3950x cpu



I have found that it's best to do this using 16 processes, allowing each model fit to use 2 CPUs.

To improve performance, I guess I have the options to

• upgrade CPU to 9950x

• get a GPU

• try a cloud machine

I'm not keen on just buying a machine with a 9950x to see how much better it will be due to the cost, and my suspicions that it might only give me 50-100% improvement.

From reading on GPUs I might only get 2-5x improvement, but those articles were with different cpus and older GPUs.

I'm not an expert on the cloud, and am worried about potential costs and complexity.

What is a good workflow to identify to best way forward for me?

---

## 2024-08-22 14:14:04 - strategies channel

**liam**

Yes but it will only be rejected if the best available moves between your placement and when it reaches the matching engine, ie. latency + betDelay

---

## 2024-08-11 23:49:15 - general channel

**Paul**

Things that spring to mind others didn’t mention 



1. If you’re making rather than taking, and your prices are more than 1-2 pips away from each other (back/lay spread on US racing can be very broad), someone new could be doing the same strategy “inside” your prices. Can you go back and check what volume was matched at a price other than your own?

2. Your hosting setup has changed. Data centres get new links, retire old ones, your VPS could now have a noisy neighbour sucking bandwidth, and so on, and so on. Doesn’t take much to add 10ms latency onto a box. Even worse if you’re running from home (residential broadband especially over OpenReach makes no guarantees about anything, ever)

3. You were betting against another bot, you’ve taken their money, they’re gone.

4. Variance. Law of large numbers says you’ll have bad runs now and again and sounds like this has been running for a long time. I know you asked how to check it’s not chance alone, but one easy check is to wait another few days where the odds become smaller and smaller

---

## 2024-08-11 17:08:06 - general channel

**D C**

If you are talking about pure API-NG (as opposed to flumine/bflw wrapper) from memory, I think you'll need listMarketBook and add "SP_PROJECTION" (or maybe "SP_TRADED") to your PriceProjection field. Take a look at the BF API documentation pages for listMarketBook operation though - that will put you right if what I've said above is wrong.

---

## 2024-08-11 11:59:55 - general channel

**Mo**

[@UGV299K6H](@UGV299K6H), I have a somewhat similar situation at the moment where I have a suspicion a code change has adversely affected performance. I’m using a Kolmogorov-Smirnov test to compare the distribution of market returns pre- and post-change. It’s definitely not the only way to do this but it’s one way to do it

---

## 2024-08-11 11:40:48 - issues channel

**liam**

Sorry, it’s lazily patched but it’s worth the performance as it’s super slow creating all the PriceSize objects 

---

## 2024-08-10 18:23:37 - general channel

**Dave**

Backtests are good - if your backtest for May + June look similar and look good, while your real performance for May matches backtest but June doesn't then likely you've broken something (i.e. you got a bug). If your backtest for June shows similar degradation then it suggests your alpha has degraded (either because some participants have scaled down, someone competitive has entereed etc). It might be a matter of recalibrating some params, or it might be a matter of resting the strategy and backtesting again in a few weeks to see if the breakage was transient or not.

---

## 2024-08-10 16:11:38 - general channel

**ShaunW**

Tricky one, backtesting variations (like asking for less margin)  is unreliable in markets you were present in. But it's impractical to step away for long enough to get a big enough clean sample without you in it..  I end up lowering the latency just enough for test 'me'  to beat what live me did but then that's at best only an indicative bodge.  What happened is knowable, what you should have done instead and into the future might not be.

---

## 2024-08-10 14:10:00 - general channel

**liam**

I wouldn't call this 'normal', based on your previous issues how confident are you that you haven't changed anything? Latency on your tick to trade? etc.

---

## 2024-08-07 09:58:29 - strategies channel

**Derek C**

I have several pets, slowly creating more cattle ... but in the proposed workflow above, if the output is predictions on S3 I would just use Athena as my database like I do for most stuff. My scheduling is EventBridge invoking lambda/Step functions.

---

## 2024-08-07 00:47:54 - strategies channel

**Gabriel Mocan**

Have you guys heard about QuestDB? I’m using it for my greyhound strategies. It’s a very optimized database for time series and finances, with a lot of useful specialized time functions. Performance is a key feature of it.





---

## 2024-08-06 22:10:07 - strategies channel

**birchy**

I'm a complete luddite to databases and have always used flat files for simplicity. But there's a point when even flat files become cumbersome. The issue I have is that I run 99% of my code on a Lightsail instance (which is plenty fast enough for my needs and allows access from multiple devices) but the local storage is limited. Traditionally, I've just downloaded the markets I'm concentrating on and then delete &amp; download when I move onto the next set. How bad is flumine performance when reading direct from S3 using smart_open() and boto3?

---

## 2024-08-06 13:15:57 - strategies channel

**birchy**

With horse racing the pre play liquidity has dropped off a lot but there's a significant amount matched inplay, sometimes more than was matched at the off time. I've been hacking around with modelling recently and have had some success with a basic LR model that has about 30 features that are all market data based, but there are 3 or 4 features/signals that are particularly stronger than the others. Engineering features is a trivial exercise but finding good ones is much harder. I took the approach of using lots of features and then dropping the shit ones until I had something production ready. I'm not really a fan of the 'black box' approach but it seems to understand the market nuances better than I do. The bottom line is that it's bringing in some £'s, so I'm slowly convincing myself that it's a much easier route to take.

---

## 2024-08-06 10:52:55 - strategies channel

**D C**

[@U01PJ5YMFBJ](@U01PJ5YMFBJ) IF you stick to pre-race you've got the added bonus in that you can use BSP as a measure to assess your success. Inplay that is not so easy to do. Inplay, you've got delays  - bet placement and internet latency (the latter being variable to some extent) so this makes back testing and simulating stuff more error prone. Then you've got things like offering prices versus taking (the former again harder to simulate and back test - impossible to PRECISELY assess the impact of your offers on the market). Your time is your own to spend of course but how much time have you invested in pre-off horses? Are you looking to move because you think increased volatility inplay is more attractive or because you feel you've hit a brick wall on the pre-race side? Or have you just become downbeat and demotivated because you haven't "cracket it" yet?

You've got to consider that you might never get there - I'm not trying to demotivate you at all but its an event with a non-zero probability. And if you flit around too much from sport to sport or mixing market phases you might do more harm than good.

I don't know your background but have you got the maths/stats chops to considered using some fundamental data instead/in addition your market based variables?

---

## 2024-08-06 06:59:07 - strategies channel

**liam**

Agree with above however racing has the advantage of a lot of opportunities, you can spend an afternoon testing / debugging on live markets. This is invaluable when starting out, sports like cricket really slow your progression down due to the smaller number of markets. 

---

## 2024-08-04 18:33:10 - strategies channel

**liam**

When simulating the code runs in a single process so you wont get any latency logs as it doesn’t impact anything.



Just profile your code, cprofilev 

---

## 2024-08-04 17:57:44 - strategies channel

**Rob**

>  Takes my machine around 3 seconds to process a single market

Same here, until I add my processing.



When using `flumine`, how do I know when my processing is too slow, e.g. if `process_market_book` is still running when the next update arrives? I tried randomly waiting for 2s in my simulation, but I don't see anything in the logs.



I'm currently approximating how much "time" I have per market based on the # markets in my strategy and the amount of time they're active for e.g. there are 6 race meetings per day, with 7 races, that I'm active in for an average of 6 hours before the off, then if each market takes 2 minutes to simulate, there should be plenty of time

---

## 2024-08-04 10:59:32 - strategies channel

**AndyL**

oh! well that may explain things...!

The thing is i'm trying to find a way of "analysing" inplay prices and EV, and you have the issue of "signal", then 1second delay +latency.....

hence I tried to virtually simulate the behaviour

the problem with purely backtesting is the biggest effect is execution method

---

## 2024-08-04 10:50:05 - strategies channel

**AndyL**

Latency ah yeah 

---

## 2024-08-04 10:49:13 - strategies channel

**liam**

you need to add network latency as well so it will be more than 1s

---

## 2024-08-04 10:17:32 - general channel

**John Foley**

a gradient boosting model requires very few (if any) assumptions about distributions etc. handles outliers and strange distributions well. handles complicated interactions between features and handles missing data. feature selection is somewhat "built-in." performance is comparable to deep learning algos for simple tabular data

---

## 2024-08-04 09:34:02 - general channel

**John Foley**

interested to hear what people have done to tackle latency with model inference (ML or otherwise). struggle with this myself, usually end up just making fewer .predict calls than i would like to

---

## 2024-08-04 07:08:15 - issues channel

**Unknown**

Hi guys; I've noticed lately that my marketbooks are not being updated - I'm not sure what the problem is exactly, but in the log file the price is 11.5 where the actual price is 15.5.  It's the whole book, and it happened the other day as well. On a reboot of the program it's done the same thing again. Log files are showing old prices, with the book just not being updated.  What do I need to check to analyse the problem / what should I be on the lookout for?



I am running a beta version of my script to add untested strategy on the same ec2 instance, so there are multiple scripts pulling the data with the same address or whatever. I don't think there are any memory problems because it's happened again after I've checked that.



The prices on the other script running look fine - different strategy names if it helps.

---

## 2024-08-03 20:57:22 - general channel

**D C**

You can get a performance bump there if you just do total_vol/vol #freealpha :grin:

---

## 2024-08-03 14:03:04 - general channel

**Jonjonjon**

Thanks for posting here [@U9UJH4P1P](@U9UJH4P1P). Out of interest

• do you trade your own account?

• Is Betfair actively trying to improve the exchange performance?

---

## 2024-07-30 18:13:30 - strategies channel

**liam**

Fastest way to speed up python is to not run it, do you need to execute every tick?

---

## 2024-07-30 17:38:10 - strategies channel

**A**

Fairly new to Python.



After profiling and openeing in snakeviz, it looks as though most of the work is slowed down by things in `functools`  module - guess it’s the `@cachedproperty`  decorators I used.



Will have a play with that.



Thanks for the pointers :pray:

---

## 2024-07-30 17:18:25 - strategies channel

**liam**

[https://betcode-org.github.io/flumine/performance/|https://betcode-org.github.io/flumine/performance/](https://betcode-org.github.io/flumine/performance/|https://betcode-org.github.io/flumine/performance/)

---

## 2024-07-30 00:00:48 - general channel

**Unknown**

So some good points learner by me tonight:

1. You can run Flumine sumulation from compressed data, I can now simulate a whole year at once, nice one [@U4H19D1D2](@U4H19D1D2) 

2. EV_vs_BSP is great to visualize actual startegy performance

3. You need a decent size dataset to evaluate a strategy, ie.1 year! as you can see below this "fitted" strategy can perform seemingly well for a few months in a row, but in the end of the day although +ve, it is highly likely just random!!

 1 year backtest from compressed .gz data:

---

## 2024-07-29 21:03:30 - general channel

**liam**

Yes it can, I store compressed and take the performance hit

---

## 2024-07-29 10:47:32 - general channel

**A**

Great thread. I’m currently following a similar path to you Andy - brute forcing things until I find something consistently profitable. I’m playing in the greyhounds market at the moment. Current strategy seems to be breaking even to slightly profitable (based on 2-3 weeks). Need to bite the bullet and implement simulation and backtesting as my feedback loop is so slow in my current workflow (essentially AB testing the same strategy with different thresholds running live)

---

## 2024-07-27 23:17:26 - general channel

**Misha**

We are working on a proper ML model, but progress has been a lot slower than I would like. But that's not my job :wink:

---

## 2024-07-27 21:16:06 - general channel

**AndyL**

current performance rubbish! i'm going to try and swap round a couple of the params, do others do that? ie.your convinced a certain param indicates a lower price, but maybe it means higher.......?

---

## 2024-07-25 18:05:26 - strategies channel

**liam**

I ignore exposure and bet based on a state change, so for TPD it’s an update (with a delay as I don’t want to be every update) and cricket it’s a new ball. 



Basic premise is to reduce risk and try not to have a large exposure on a single ‘state’ that might contain errors / latency that is out of my control 

---

## 2024-07-23 12:42:56 - random channel

**Mo**

&gt; The Department of Economics at the University of Crete welcomes you to attend a webinar on Thursday 25 July at 19.00 GREEK time.

&gt; 

&gt; Title: Predicting full retirement attainment of NBA players

&gt; 

&gt; Presenter: Giorgos Foutzopoulos, Private Company

&gt; 

&gt; Abstract: Τhe aim of this analysis is to predict whether an National Basketball Association (NBA) player will be active in the league for at least 10 years so as to be qualified for NBA's full retirement scheme which allows for the maximum benefit payable by law. We collected per game statistics for players during their second year, drafted during the years 1999 up to 2006, for which, information on their career longetivity is known. By feeding these statistics of the sophomore players into statistical and machine learning algorithms we select the important statistics and manage to accomplish a satisfactory predictability performance. Further, we visualize the effect of each of the selected statistics on the estimated probability of staying in the league for more than 10 years.

&gt; 

&gt; Zoom link: [https://uoc-gr.zoom.us/j/88659969718?pwd=g6bjYPDCuUQo1bzVxjjbgQL4xFN1f3.1|https://uoc-gr.zoom.us/j/88659969718?pwd=g6bjYPDCuUQo1bzVxjjbgQL4xFN1f3.1](https://uoc-gr.zoom.us/j/88659969718?pwd=g6bjYPDCuUQo1bzVxjjbgQL4xFN1f3.1|https://uoc-gr.zoom.us/j/88659969718?pwd=g6bjYPDCuUQo1bzVxjjbgQL4xFN1f3.1)

---

## 2024-07-22 21:47:10 - general channel

**birchy**

I do mine at strategy level in process_market_book but it would be nicer in middleware. I usually just save the complete market_book and then do stuff like get time series based on the publish_time_epoch, etc. From memory, middleware __call__() gets called on every update. [@U4H19D1D2](@U4H19D1D2)?

---

## 2024-07-17 12:05:51 - random channel

**Paul**

The R code is definitely understandable and could be ported. I was reading through some of the first chapter on MCMC this morning and nothing looked too hard to port to python, although I’m not familiar with differences between RStan and PyStan (yet). Tempted to write Python versions of each of his code listings and whack them up on GitHub. The theory sections are pretty in-depth, and for some of it I’m definitely lost (so I’m going to have to go back through sections like conjugate priors, for example, slowly, and with a google machine at my side), but the code looks like something I can pick up and use and play with.

---

## 2024-07-17 10:01:36 - general channel

**liam**

InPlay Greyhounds please Betfair



[https://totalperformancedata2-my.sharepoint.com/personal/tayla_buck_totalperformancedata_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Ftayla%5Fbuck%5Ftotalperformancedata%5Fcom%2FDocuments%2FAttachments%2FTPD%20Q2%20Review%2Epdf&amp;parent=%2Fpersonal%2Ftayla%5Fbuck%5Ftotalperformancedata%5Fcom%2FDocuments%2FAttachments&amp;ga=1|TPD 2024 Q2](https://totalperformancedata2-my.sharepoint.com/personal/tayla_buck_totalperformancedata_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Ftayla%5Fbuck%5Ftotalperformancedata%5Fcom%2FDocuments%2FAttachments%2FTPD%20Q2%20Review%2Epdf&amp;parent=%2Fpersonal%2Ftayla%5Fbuck%5Ftotalperformancedata%5Fcom%2FDocuments%2FAttachments&amp;ga=1|TPD 2024 Q2)

---

## 2024-07-16 11:36:02 - issues channel

**liam**

threads in python share memory so flumine only requires a single login

---

## 2024-07-15 19:40:04 - issues channel

**liam**

It should always improve your latency as you will use less threads thus less sessions active 

---

## 2024-07-11 13:03:42 - strategies channel

**AndyL**

PERFORMANCE

• Single-Precision: 35.58 TFLOPS

• Transistor Count: 28.3 billion



---

## 2024-07-11 10:50:33 - strategies channel

**AndyL**

I just estimated my recent Flumine backtest speed, I think it's about *10* markets per second :joy:

---

## 2024-07-11 00:08:30 - strategies channel

**thambie1**

If I were buying a machine for backtests, I'd build a desktop with the most powerful retail CPU on the market. And then in my case, model training is also memory heavy so I'd want minimum 128GB on that. Everything else wouldn't matter as much

---

## 2024-07-11 00:04:27 - strategies channel

**thambie1**

@James I have done cost experiments for zipped vs unzipped. I found unzipped to be cheaper in my use case. You should have cpu profiling working and be able to do such experiments yourself if you want to make optimizations of this kind. That being said, the financial choice is clear to just buy a better dev machine if that can fix your problem, unless your really not valuing your time to go the cloud route. It really is a time sink, trust me.

---

## 2024-07-09 16:42:46 - random channel

**Simon Chan**

Maybe a weird question:

I recalled that someone here posted a photo of some paragraph from a book a while ago. I don't remember what it said exactly but what I can paraphrase from memory is: it talks about  the author (or someone else)  learning /using advanced technical concepts (mathematics, computer science) in order to help trading, but is not interested 

 in these concepts on their own at all, as these are just useful tools to make money.  There was also discussion on this sentiment and I think most folks here disagreed/ were not warmed to it.



I can't find the post now because it is way past the 90 days history limit by Slack.  It is probably a wild guess, but does anyone know the book, or know who posted it and/or have archived the post?  I'm interested in reading the book further (part of the academic research I'm doing).

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

## 2024-07-05 10:56:09 - random channel

**Tom**

I've been running a script on betfairlightweight to collect data (and order execution on flumine; but was slowly trying to get my data collection through flumine / OOP but don't want to mess up what the script is doing.



That makes it a lot easier

---

## 2024-07-05 10:15:27 - issues channel

**Unknown**

yeah, slower here but similar to the backtest latency preset

---

## 2024-07-05 09:21:45 - issues channel

**liam**

You honestly think you are getting 0.0001s latency from betfair and it's only 'possible' that your clock is wrong?

---

## 2024-07-05 09:02:33 - issues channel

**liam**

Agreed, but why do you think the UK server should have higher latency?

---

## 2024-07-05 08:58:10 - issues channel

**Adrian**

its more stable because it's higher latency. But still swings around just as much per tick

---

## 2024-07-05 08:47:47 - issues channel

**Adrian**

Yes. WHen you calculate latency by dividing market epoch by 1e3 you get 1000s of a second errors. Because the numbers are exactly the same up to the decimal point

---

## 2024-07-05 01:12:50 - issues channel

**Unknown**

[@U016TGY3676](@U016TGY3676) sorry i misread 'counterparty' as counterplay. I get what you mean now, thanks. You could be right, i'm not cancelling for many minutes though so i dont see how thats could be a factor

[@U4H19D1D2](@U4H19D1D2) That is time - mb publish time epoch. i literally took your formula straight from baseflumine.py

`latency = time.time() - (market_book.publish_time_epoch / 1e3)`

here is the full screenshot

the order shown is latency | time.time() | market_book.publish_time_epoch | market_book.publish_time_epoch / 1e3

---

## 2024-07-04 06:35:23 - issues channel

**liam**

Do you know what your latency is when receiving data ie. Publish time vs your clock / do you get any data conflated? 



Unless you are betting into a highly volatile market such as inplay racing I am not sure this would be latency tbh 

---

## 2024-07-02 13:34:00 - random channel

**Unknown**

I guess I will ping some further observations and punting log as it makes watching the tournament more interesting. I make no claims to having any alpha in this as my systematic strategies don't touch this.



Portugal actually drifted out despite winning their game. Less than stellar performance and Ronaldo seems very unconvincing. When Portugal was drifting out, someone started backing England some more. Causal? It seems like regardless of weaker or stronger teams getting kicked out of tournament, there is a wall of money backing England.



There were a couple of £1M bets during the Portugal/ Slovenia penalties (To Qualify market). Maybe [@U4H19D1D2](@U4H19D1D2) has started betting on football

---

## 2024-07-02 08:11:53 - random channel

**D C**

Just logged into one of my AWS servers to find that it must have rebooted overnight. Bots on the server have been running for about 18 months uninterrupted. How common is it for AWS stuff to just reset like that? Memory and CPU and disk usage were all very low. It's no big deal I guess, but I've never seen Linux just reboot like that for no (obvious) reason.

---

## 2024-07-01 00:15:12 - strategies channel

**James**

```# latencies used for simulation

place_latency = 0.120

cancel_latency = 0.170

update_latency = 0.150

replace_latency = 0.280```

Sim latencies are in seconds yeah?

---

## 2024-06-29 10:23:33 - issues channel

**Adrian**

[@U05L8PZD2FM](@U05L8PZD2FM) yep happened the second i moved it over.

[@UBS7QANF3](@UBS7QANF3) i haven't tried doing the backtest with lower latency. I'll give it a crack. Thanks for the idea!

It's probably my bad coding that was being cushioned with a higher latency

---

## 2024-06-29 10:04:25 - issues channel

**Mo**

I can't speak to the cancelling behaviour you've observed but:



Reduced latency is going to affect how quickly you receive the triggers as well as how quickly you send your bets to Betfair. It's not impossible that acting too quickly is deleterious. Have you tried running backtests with different simulated latencies and comparing results?

---

## 2024-06-29 09:08:22 - issues channel

**foxwood**

Given the bet cancellation is 8 minutes later could be some code running at suspension / close of market - although no idea what type of markets you are on ? If sure it is not your code doing / causing the cancel then try comparing the server/home code and package versions. Losses due to improved latency quite possible - now getting matched on bad value bets that were just too late from Aus so not being matched from home but are now.

---

## 2024-06-29 02:06:12 - issues channel

**Unknown**

here's the latency on my new server. you can see it's not high. I should add that i'm only taking bets not offering them, so the matching should be near instant, but definitely not worse than from the other side of the planet

---

## 2024-06-29 01:50:48 - issues channel

**Unknown**

Hi Guys,

Strange thing is happening. I moved my hosting from my home lab in Australia to Ireland. My latency has improved drastically, however for some strange reason my bet matching has become worse. Here are two graphs, the first one shows the total elapsed seconds of all my bets. You can see the huge jump in the last lot to the right where virtually nothing is being matched straight away. The second graph shows all bets that were matched under one second. You can see the huge spike where it doesn't even touch zero seconds elapsed whereas it was sitting on the x axis most of the time before. The decrease in performance is showing in my results.. my ev and my profit is flatlining. What the hell is happening?

---

## 2024-06-28 02:13:51 - random channel

**James**

Hey, I’ve been calling the an undocumented, but public api to provide some race info to a manual in play trader. They want to know at a quick glance, Driver/Jockey, track conditions etc and bookie sites and other racing sites are bloated and load slowly.



It was running fine for about a year, and a little while back they blocked access to their API from a massive number of cloud providers (I assume by IP ranges) from AWS/GCP right down to digital ocean and Vultr.



As a temporary solution I have a local server running on the network for this trader, and his IP can access the API without any issues. I want to host it again so it can be accessed away from his home network (without a VPN) and it has CORS settings in place meaning it needs to happen on a server rather than client side. Any ideas from this crowd? I know its more softwarey/infrastructurey than the data questions that usually end up here but thought I’d ask all the same.

---

## 2024-06-21 09:32:19 - random channel

**liam**

Being completely honest, not sure I have found a single paper that a) I find interesting and b) actually understand, they all seem just full of pointless maths and equations.



The most interesting part of sports right now is live data / tracking / ai tracking etc. something which fits more into CS as well



[https://www.totalperformancedata.com/](https://www.totalperformancedata.com/)

[https://jabbr.ai/](https://jabbr.ai/)

[https://pysport.org/](https://pysport.org/)

[https://www.statsperform.com/artificial-intelligence-in-sport/](https://www.statsperform.com/artificial-intelligence-in-sport/)

---

## 2024-06-16 19:31:05 - random channel

**Justice**

[@UEA14GBRR](@UEA14GBRR) Yes I could use SQL, with a properly normalized database. But I am going to have to de-normalize and load into memory at some point to train my model/test/visualize etc.



I could lazily iterate which would avoid memory issues as [@U0128E7BEHW](@U0128E7BEHW) suggested but it would be awfully slow and I'm impatient. Perhaps I just need more compute.

---

## 2024-06-11 05:25:55 - general channel

**liam**

Placement/cancel/replace latency is impacted by your network latency and the matching cycle but on some markets you will have a bet delay that is imposed by betfair, inplay racing / tennis / football etc.

---

## 2024-06-11 02:10:47 - general channel

**Ben Coleman**

Yeah ok interesting. Is that placement latency something that Betfair intentionally imposes on all incoming orders or is it just a reflection of the time taken for Betfair to process your order and any other requests that were ahead in the queue?

---

## 2024-06-10 16:05:34 - general channel

**George**

Hope you don't mind if I follow up on this - I noticed that the `deepcopy` is adding a lot of latency to the extent that it might not be viable to use `remove_bet_from_runner_book` in the process_market_book.

Is there a way of achieving the same result without using `deepcopy`?

---

## 2024-06-10 13:54:52 - general channel

**ShaunW**

You might respond in 4 or 5ms but physics and the matching engine at BF means that your order won't be applied until after a placement latency of approx 120-150ms (actually iro 50-200ms) A lot happens in that time and what you're aiming for is often long gone, especially bearing in mind that the api msg you're responding to is subject to an arrival delay too.

---

## 2024-06-03 12:42:51 - issues channel

**George**

It seems like order logging in flumine simulation suffers from an inherent problem with race-conditions. Essentially I believe that the simulation loop is fast, but the logging-control loop is slow, and they run in parallel.



This means, by the time the logging-control comes to log any particular order, that order might have changed its status or properties potentially multiple times.



To resolve this, potentially the easiest option would be to pass dictionaries into the logging-control, rather than Order objects. Is that something that people are already doing / aware of / interested in? Is it already possible to achieve somehow without making changes to the internals of flumine?

---

## 2024-06-03 09:11:50 - general channel

**Ralegh**

Try smarkets if you aren’t market making, matchbook if you’re not latency sensitive, and *maybe* betdaq if you’re doing slowish market making since their prices are quotes a bit wider but their api is not great. Betconnect is sort of a wild card I would do that if similar to matchbook you are getting value without needing fast order placement or maybe you’re trying to hedge something when there’s not much liquidity on betfair

---

## 2024-05-31 21:20:49 - general channel

**George**

Not sure about that... actually, in simulation, the race condition with order status happens when using the normal logging controls, it's nothing to do with what I've added here.



When I comment out the code I've added, I still see "new" orders being written to the log with size_cancelled > 0 and size_remaining == 0.



That wouldn't happen in live trading because of the real-life latency involved.

---

## 2024-05-31 14:30:05 - general channel

**George**

OK, thanks. I'm not concerned about race conditions on the status. Latency would concern me a bit but I'm happy to give it a go.



However I'm not immediately sure how I would create an order class that would naturally get its status updates passed through the `LoggingControl` .



To do that, I think an order status update would have to be a `CURRENT_ORDERS_EVENT` and I can't immediately see how to implement that...

---

## 2024-05-31 14:23:23 - general channel

**liam**

I think you might be confusing python `logging` with flumine `loggingcontrol`  however when designing flumine I decided not to make an order status update pass through loggingcontrol due to latency and race conditions.



I was worried it might slow things down but you could easily create your own order class that does do this but it does open up a few issues regarding race conditions on the status etc.

---

## 2024-05-29 19:36:31 - random channel

**Dave**

I aim for around min 5% in backtest. Once deployed, as long as it is positive and has no negative impact on my other strategies (latency, wasting streaming bandwidth etc) then that's enough to justify running it

---

## 2024-05-27 10:20:04 - general channel

**George**

Thanks guys. I was not really interested in latency - I guess my question should have been:



"Does the simulation EVER modify the runner-book to include my newly-placed order?"



My `process_orders()` doesn't do anything currently - I'll look and see whether that was the problem.



Could I ask [@UUCD6P13J](@UUCD6P13J) to clarify also? As I am now super confused!! Thank you all

---

## 2024-05-26 16:42:29 - general channel

**foxwood**

Agree with [@U01PJ5YMFBJ](@U01PJ5YMFBJ) - "will I see my order in the market book on the next loop" i think the answer is yes and no. Simulation attempts to copy real world and adds in a processing delay for orders to reflect posting to  exchange and bet confirmation. So, if the next data packet is a long time coming then the order may well be there on next `check_market_book()` but on a busy market it may take a couple of loops. There are a number of controllable latencies for simulation in the config file [https://betcode-org.github.io/flumine/advanced/#place_latency](https://betcode-org.github.io/flumine/advanced/#place_latency)

---

## 2024-05-20 06:20:40 - strategies channel

**liam**

Your example code doesn't show this? The `listener_kwargs` act at the very lowest level of the stream logic within bflw in order to speed things up so if any are different they cannot be shared

---

## 2024-05-17 22:57:30 - strategies channel

**thambie1**

[@U05N9773A23](@U05N9773A23) EX_BEST_OFFERS_DISP is the one with the latency penalty

---

## 2024-05-17 20:40:52 - strategies channel

**Dave**

How does the 150ms latency work with the 50ms matching cycle?

---

## 2024-05-17 12:05:08 - strategies channel

**Justice**

I always use EX_BEST_OFFERS. Didn't realise there was a performance penalty?

---

## 2024-05-17 10:10:24 - strategies channel

**James Scott**

Does calculating it yourself not cause some latency?

---

## 2024-05-17 00:23:11 - strategies channel

**thambie1**

I'd rather calculate it myself than pay the latency cost

---

## 2024-05-16 11:34:24 - random channel

**river_shah**

I guess then he'd have to say:

`We find that surpassing the performance of a simple linear regression in the return forecasting task is surprisingly challenging.`

---

## 2024-05-16 11:33:04 - random channel

**river_shah**

Yes, the thing is in his preamble he goes on precisely how the model is being constructed. So you know why not do that extra step, write some of the features out by hand (rather than lstm hidden representations) and fit ridge with GCV and show us the full multi horizon alpha term structure. I'd bet even this basic approach matches lstm illustrated performance (let alone what can be achieved by grinding harder at the problem use ridge + domain knowledge)

---

## 2024-05-16 11:13:05 - random channel

**river_shah**

`We find that surpassing the performance of a simple LSTM in the return forecasting task is surprisingly challenging.`



I am going to stick with ridge regression until you pry it out my cold dead hands

---

## 2024-05-14 12:01:04 - random channel

**liam**

Looks like you have latency issues and CPU issues based on both those warnings, hard to offer help without seeing a profile or the code

---

## 2024-05-14 10:12:32 - random channel

**Johnny**

Quite relevant for me, currently trying to streamline my process_market_book, as when the football markets get busy I'm getting epic latency which goes away when things quiet down

```{"asctime": "2024-05-12 04:48:03,422", "levelname": "WARNING", "message": "[MarketStream: 2016]: Latency high: 865.0007269382477"}

{"asctime": "2024-05-12 04:48:03,425", "levelname": "WARNING", "message": "High latency between current time and MarketBook publish time", "market_id": "1.228296017", "latency": 2898.2553684711456, "pt": "2024-05-12T03:59:45.170000"}```

---

## 2024-05-14 09:57:42 - random channel

**liam**

[https://markrbest.github.io/message-arrival-rates-and-latency/|Message Arrival Rates and Latency](https://markrbest.github.io/message-arrival-rates-and-latency/|Message Arrival Rates and Latency)

---

## 2024-05-10 19:25:26 - issues channel

**ShaunW**

Check your sim latency vs live? Sounds like you're getting in too far in front of your live orders. Its hard retesting something you're present in.

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

## 2024-05-07 12:49:11 - strategies channel

**Ben Coleman**

I would usually get 1 or 2 collections of these logs every day. I am tracking latency between publish time and calling process_market_book which tends to be around 4-5ms and the time from then to placing orders which is around 3-4 ms. I have detailed breakdowns of the latter one, how would you go about breaking down the former one? Also how do you access the execution logs that tracks latency? Does it just appear in the log files because its only that screenshot that I get information on latency.

---

## 2024-05-07 10:24:30 - general channel

**liam**

A few things that stand out



`seconds_to_start` you seem to be calling this a lot? Can you reduce calls?

`betfairlightweight==speed` are you using it as I can't see evidence of the C/Rust libraries

`listener_kwargs` are you using as `check_market_book` seems to be called a lot / is quite slow

`dict.___get___` lots of calls, ideally reduce if possible

`regex` seems slow, have you optimised using compile?

---

## 2024-05-07 08:54:10 - strategies channel

**liam**

Yeah, ok but do you get a lot of those logs? You need to isolate / get some visibility on where the latency is coming from

---

## 2024-05-07 07:28:29 - strategies channel

**liam**

In the execution logs flumine logs the latency, do you know what you are getting? Median/dist etc?

---

## 2024-05-07 07:24:08 - strategies channel

**Ben Coleman**

Hi all,

I'm interested in knowing a little bit more about how to go about decreasing latency on trades and getting matched more often. I have a few questions and I wouldn't mind hearing anyones insights:

- What does the force argument do within the market.place_order() function? and would setting it to True potentially make the function run faster?

- Are the streams global or individual specific? Meaning does everyone always get the same update at most every 50ms and it is published at the same instant or is the instant the update is published for individuals only specific to them and hence they might have slightly differing market books due to what happens in the interim?

- How are incoming requests managed on the exchange side? Is it every 50ms the exchange looks at all of the requests in the previous 50ms and executes them in the order that they appeared then publish the updated book every 50ms? Or is there some sort of hierarchy where certain types of requests are executed before others each increment (eg. Process all the fill or kill orders first then the standard limit orders next or all cancel order requests are executed before place order requests?)

Cheers

---

## 2024-05-06 13:57:54 - general channel

**liam**

Looks like some super slow pandas 

---

## 2024-05-06 11:59:32 - general channel

**Adrian**

Thanks for that! Didn't know there was a guide on performance. I've tried most of these but will give multiprocessing and limiting control blocked orders a go

---

## 2024-05-06 11:52:54 - general channel

**Lee**

[https://betcode-org.github.io/flumine/performance/|https://betcode-org.github.io/flumine/performance/](https://betcode-org.github.io/flumine/performance/|https://betcode-org.github.io/flumine/performance/)

---

## 2024-05-05 21:18:44 - strategies channel

**Dave**

No, book building is super fast. Like I said, outside of my logic in Flumine's post-book-building stage, it seems all my latency is network. Flumine itself doesn't add anything really, latency wise, from what I can see.

---

## 2024-05-05 21:17:36 - strategies channel

**D C**

Is the market book updating in flumine slow then?

---

## 2024-05-05 21:16:10 - strategies channel

**D C**

I'm pretty happy with what I've got I'm just intrigued by other people's perceptions of what they deem as acceptable latency. It seems reasonable to me to be waiting 13ms (average) from when Betfair push the JSON out and my having received and parsed it.

---

## 2024-05-05 21:07:03 - strategies channel

**D C**

I'd be quite happy with that to be honest. I use C++ and an event based SSL socket and my average from message publish time to message read off the buffer and parsed as JSON is about 13ms. Of course I don't know if mine and Betfair's clocks are synced but I was pretty happy with this. I suspect if I used a specific thread with a blocking socket connection I would shave a little off it but  you can' get rid of network latency completely.

---

## 2024-05-05 21:05:23 - strategies channel

**Dave**

So this basically has me wondering if keeping my median latency at 10ms is simply impossible when adding extra strategies, so I should just distribute instances across more cores, or perhaps somehow do computation out of process

---

## 2024-05-05 20:48:52 - strategies channel

**D C**

10 milliseconds from publish time to your order being placed? I often get bigger latency as the difference between the publish time and the time I've finished parsing the update, nevermind application logic. I always thought this was a reasonable network latency but looks like I need to up my game!

---

## 2024-05-05 20:22:07 - strategies channel

**liam**

If you are worried about that sort of latency then you are using the wrong language tbh 

---

## 2024-05-05 19:55:41 - strategies channel

**Dave**

I will check out bflw speed, thanks Liam. I ran profiler when backtesting which helped a lot with optimization within the callbacks, but obviously tells you about nothing network related. I'm basically seeing typically around 10millis between the update's publish time and me asking flumine to place an order. I know my logic is no more than around 1.5ms, so I'm wondering how the rest of the 8-9ms is distributed.

---

## 2024-05-05 19:50:07 - strategies channel

**liam**

Just load up a profiler and have a look.



I assume you are using bflw speed? After the network JSON decoding is slow but not much we can do about that, the streaming logic is heavily optimised (for python) but creating the python objects in bflw is the slow part however flumine does some clever stuff to try and limit/remove it. The ‘tick to trade’ code within flumine itself is very minimal and normally rounds to zero relative to what happens within a strategy. 

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

## 2024-05-04 15:05:16 - strategies channel

**Ralegh**

Usually want to preallocate a numpy array per column and fill it with values, can use it as a ring buffer if you don’t have enough memory

---

## 2024-05-04 14:23:41 - strategies channel

**liam**

Need to be careful when things start getting large as everything slows down and causes latency issues 

---

## 2024-05-03 15:11:21 - general channel

**Bruno**

Hi Liam,



I think you may have misunderstood my question a bit, perhaps I did not make myself very clear.



please consider this MWE



```filter=streaming_market_filter(

        event_type_ids=["7"],

        market_types=["WIN"],

    )



class ML_strategy(BaseStrategy):

    pass

fakestrat=ML_strategy(market_filter=filter)



class BlotterWatcher(BaseStrategy):

    def start(self):

        print('BlotterWatcher started')

    def check_market_book(self, market, market_book):

        # process_market_book only executed if this returns True

        if market_book.status != "CLOSED":

            return True

    def process_market_book(self, market, market_book):

        self_orders=market.blotter.strategy_orders(strategy=self)

        fakestrat_orders=market.blotter.strategy_orders(strategy=fakestrat)

        if self_orders:

            print('Self orders:',self_orders)

        if fakestrat_orders:

            print('Fakestrat orders:',fakestrat_orders)



strategy=BlotterWatcher(market_filter=filter)

framework.add_strategy(strategy)

framework.add_strategy(fakestrat)

framework.run()```

I have a strategy, _also called ML_strategy,_ running _in another process_.



this "blotter watch script" only prints out orders from fakestrat, not from self. contrary to what you said, I believe this is because the strategies share a class name, and the hostname is not the answer to my question. many thanks for your speedy reply and thank you for making an attempt to answer my question.



Many Thanks,



Bruno

---

## 2024-05-03 13:55:41 - general channel

**Bruno**

hi, when we create a trade I understand that we need to pass an instance of a strategy class, and then later we can access the orders unique to that strategy using blotter.strategy_orders and similar, however my question is what aspect of the class exactly determines this uniqueness - is it the memory location of the class, the name of the class, the hash of the class, or have i misunderstood the scenario? in short, I want to run multiple instances of flumine and selectively reference orders between the instances, but I'm struggling to work out how I can achieve that

---

## 2024-05-01 15:09:24 - random channel

**PeterLe**

Let me know what you think Mo when you have read it

I have Michael Lewis - Liars Poker which ive been meaning to read for a while (and permanent record - Ed Snowden..find it a bit slow TBH)

You might enjoy this too if you havent read it : [https://www.amazon.co.uk/Bitcoin-Billionaires-Genius-Betrayal-Redemption/dp/B07P75J5MW/ref=sr_1_1?crid=1DCLMGCYTZAG4&amp;dib=eyJ2IjoiMSJ9.RgdEWhLg_WhCKNfP4LIho-17nuVuZO-HTFZ_-Joey7rQUNOdo2bTIQSmuXj3fK6wgJE2wCZehwIDU8_cnnBLkokPR1TF6BUDBlhM-hQeawYTO9BZLrDt2d_y05RF9dkCJ314nKnyaEqOdmivBlW23yKx1a7FIjNokBibne2-uh4RHmzti6e7h69ZVSRYKSaZGPrIEh6uw4FPICZlS4Lag_-zw_TyfL6fwrXDypRbbcY.6EsP9U-reR_p1qmixo-_0Xi-uf7Y6_gU6R7R6f8WNCk&amp;dib_tag=se&amp;keywords=bitcoin+billionaires&amp;qid=1714572380&amp;s=books&amp;sprefix=bitcopin+billionaires%2Cstripbooks%2C71&amp;sr=1-1|https://www.amazon.co.uk/Bitcoin-Billionaires-Genius-Betrayal-Redemption/dp/B07P75J5M[…]books&amp;sprefix=bitcopin+billionaires%2Cstripbooks%2C71&amp;sr=1-1](https://www.amazon.co.uk/Bitcoin-Billionaires-Genius-Betrayal-Redemption/dp/B07P75J5MW/ref=sr_1_1?crid=1DCLMGCYTZAG4&amp;dib=eyJ2IjoiMSJ9.RgdEWhLg_WhCKNfP4LIho-17nuVuZO-HTFZ_-Joey7rQUNOdo2bTIQSmuXj3fK6wgJE2wCZehwIDU8_cnnBLkokPR1TF6BUDBlhM-hQeawYTO9BZLrDt2d_y05RF9dkCJ314nKnyaEqOdmivBlW23yKx1a7FIjNokBibne2-uh4RHmzti6e7h69ZVSRYKSaZGPrIEh6uw4FPICZlS4Lag_-zw_TyfL6fwrXDypRbbcY.6EsP9U-reR_p1qmixo-_0Xi-uf7Y6_gU6R7R6f8WNCk&amp;dib_tag=se&amp;keywords=bitcoin+billionaires&amp;qid=1714572380&amp;s=books&amp;sprefix=bitcopin+billionaires%2Cstripbooks%2C71&amp;sr=1-1|https://www.amazon.co.uk/Bitcoin-Billionaires-Genius-Betrayal-Redemption/dp/B07P75J5M[…]books&amp;sprefix=bitcopin+billionaires%2Cstripbooks%2C71&amp;sr=1-1)

---

## 2024-04-30 15:16:15 - strategies channel

**Ger Gleeson**

Ill piggy back on this thread. Also pretty new in this space. Im looking to move running my scripts from running on my local machine to run within the cloud etc. My scripts are pretty straight forward (at the moment). I just to have them hosted in IRE / UK to avoid geoblocking etc, and also run in "background". Im used to running scipts through Anaconda / jupyter lab / chrome etc but this seems vey slow (start up, general navigation etc) on a 1GB RAM setup within AWS lightsail. Anaconda documentation seems to recommend 4BG+ RAM, which looking at the lightsail pricing per month is coming out at 40 USD per month. Can anyone suggest simplier set up i can go with which requires less RAM etc would allow a cheaper rate per month

---

## 2024-04-23 13:14:15 - strategies channel

**ShaunW**

If speed is your number one priority then don't use python :wink:

---

## 2024-04-23 12:53:09 - strategies channel

**James**

Maybe I was told incorrectly, I was however definitely encouraged to host in Ireland on AWS for the best latency from a cloud point of view.

---

## 2024-04-23 12:49:42 - strategies channel

**ShaunW**

I don't think Betfair use AWS? I thought they ran their own hardware, in Dublin, near AWS. Either way the cost of the service has to be balanced with performance, no point saving a dollar to earn $1000 less.

---

## 2024-04-23 12:45:02 - strategies channel

**James**

Digital ocean apps containers are $10 per month for a 1gb 1 cpu machine. So cheap.



Betfair servers are in Ireland on AWS, so minimum latency is to host is there, ECS containers or Lightsail tend to be easiest and fast, but not as cheap as DO.

---

## 2024-04-23 10:54:22 - general channel

**Ammar**

If you partition by a market filter when opening flumine, you will get one connection per filter, so number of markets will be lower per stream / connection. 



I have not seen any posts about anyone hit a stream performance issue tho, so it may not be necessary. But my experience w the framework is still quite limited so I may be missing something



Also I believe betfair limits each api key to 10 streaming connections. 



You could try it and see … it may be a case of trial and error to get the right hardware and stream filter setup for your use case 

---

## 2024-04-23 10:46:07 - general channel

**Aiyaj Khalani**

re: Streaming is “cheap” - you get one connection established per market filter you pass into the flumine instance (plus one for orders if you want it)



we have requirement of subscribing to around 12k markets on streaming API. do you think it will be still cheaper? i meant having few market subscriptions vs this much wider subscription would result in same latency or load?

---

## 2024-04-18 01:59:54 - random channel

**Alex A**

When I first start my process up, I measure the latency (publish time vs local receive time). and restart if it’s over some threshold.

---

## 2024-04-17 20:14:32 - random channel

**liam**

So anyone do this?



&gt; Smart quant crypto traders will spin up many thousands of EC2 instances, measure latency to the exchange, and only keep the best instances, continually. This process allows them to eventually get EC2 instances to trade from probably in the same rack, or maybe on the same bare metal box, as the exchange. 

---

## 2024-04-17 16:54:42 - random channel

**D C**

Remember Liam calling them an RNG which seems about right. Sky pics slow too which won't help when comparing to market.

---

## 2024-04-16 17:11:19 - random channel

**Paul**

The bit I picked up from it is if you’re dealing with an exchange where you latency is basically normalised (and, let’s face it, we are), it means that HFT isn’t really practical. And it isn’t in BF anyway because of transaction charges that eat away at profit unless your volumes are very lumpy. It’s interesting in fiscals they kind of dream to be in this situation to level the playing field. :slightly_smiling_face:

---

## 2024-04-16 13:56:44 - random channel

**Paul**

Found this [https://blog.abctaylor.com/what-would-happen-to-low-latency-trading-if-exchanges-moved-to-the-cloud/|blog thinking through what would happen if a stock market went full cloud](https://blog.abctaylor.com/what-would-happen-to-low-latency-trading-if-exchanges-moved-to-the-cloud/|blog thinking through what would happen if a stock market went full cloud) quite interesting, but interesting parallels to BF, et al. :thinking_face:  HN discussion thread is [https://news.ycombinator.com/item?id=40050717|here](https://news.ycombinator.com/item?id=40050717|here)

---

## 2024-04-16 09:22:20 - issues channel

**Peter**

Yep. [https://betcode-org.github.io/flumine/performance/#cprofile](https://betcode-org.github.io/flumine/performance/#cprofile)

---

## 2024-04-16 06:49:00 - issues channel

**A**

If I’m receiving `[MarketStream: 2001]: Latency high: 0.516402006149292` warnings in my console, does that suggest my `process_market_book` function is inefficient? I don’t think it’s network latency. Might need to dig into python threading.

---

## 2024-04-14 19:18:26 - general channel

**liam**

Are your strategies that latency sensitive?

---

## 2024-04-14 18:54:02 - general channel

**Dave**

The context is that I want to free up some connections to launch additional markets. But I'm worried that if I "merge streams" in this way, ticks may arrive "slower", (e.g. in this case GB ticks and AU ticks will be interleaved on the same stream rather than receiving them independently on two streams), or maybe even subject to forced conflation. Obviously you're still at the mercy of the GIL + the fact that flumine is single process, but still. I am imaging a scenario where stream throughput is always the same on Betfair's side, so subscribing to GB+AU on one stream may result in suboptimal delivery of ticks vs 2 streams with GB + AU independently. (just using GB + AU for example sake btw, obviously more concerned about markets that tick heavily in paralell).

---

## 2024-04-14 18:43:16 - general channel

**ShaunW**

Most of the year they don't overlap, or by much. Schedule them to start up and shutdown seperately as required. But combining your sub into Aus and UK together probably won't make any performance difference  because when one is busy the other isn't.  You'll be checking a tick is one you want anyway regardless of subscription, as you don't assume a data source that's out of your control is as expected, as part of defensive coding good practice.

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

## 2024-04-08 09:08:00 - issues channel

**Johnnb**

This is the code that sets up the logging :

```logger = logging.getLogger()

custom_format = "%(asctime) %(levelname) %(message)"

formatter = jsonlogger.JsonFormatter(custom_format)

formatter.converter = time.gmtime

log_file_name = 'multi_recorder.log'

log_handler_file = logging.FileHandler(log_file_name)

log_handler_file.setFormatter(formatter)

log_handler_file.setLevel(logging.WARNING)

logger.addHandler(log_handler_file)```

and this is the whole contents of the log file :

```{"asctime": "2024-04-07 12:06:30,768", "levelname": "WARNING", "message": "[FlumineStream: 4001]: Latency high: 0.5309743881225586"}

{"asctime": "2024-04-07 12:22:38,592", "levelname": "WARNING", "message": "[FlumineStream: 3001]: Latency high: 0.5384097099304199"}

{"asctime": "2024-04-07 12:38:51,513", "levelname": "WARNING", "message": "[FlumineStream: 3001]: Latency high: 0.618567705154419"}

{"asctime": "2024-04-07 13:22:52,309", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.7499873638153076"}

{"asctime": "2024-04-07 13:22:52,309", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.7483816146850586"}

{"asctime": "2024-04-07 13:22:52,309", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.6966326236724854"}

{"asctime": "2024-04-07 13:22:52,309", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.5819070339202881"}

{"asctime": "2024-04-07 13:22:52,310", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.5760924816131592"}

{"asctime": "2024-04-07 13:32:00,671", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.6668083667755127"}

{"asctime": "2024-04-07 14:21:34,134", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.5454201698303223"}

{"asctime": "2024-04-07 14:21:34,135", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.5427672863006592"}

{"asctime": "2024-04-07 14:29:44,438", "levelname": "WARNING", "message": "[FlumineStream: 3001]: Latency high: 0.5154736042022705"}

{"asctime": "2024-04-07 15:04:02,227", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 1.7697350978851318"}

{"asctime": "2024-04-07 15:04:02,229", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 1.669356107711792"}

{"asctime": "2024-04-07 15:04:02,229", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 1.5565588474273682"}

{"asctime": "2024-04-07 15:04:02,229", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 1.5507323741912842"}

{"asctime": "2024-04-07 15:04:02,229", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 1.452915906906128"}

{"asctime": "2024-04-07 15:04:02,230", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 1.3592793941497803"}

{"asctime": "2024-04-07 15:04:02,230", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 1.3554434776306152"}

{"asctime": "2024-04-07 15:04:02,230", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 1.2436447143554688"}

{"asctime": "2024-04-07 15:04:02,230", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 1.1467902660369873"}

{"asctime": "2024-04-07 15:04:02,231", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 1.142089605331421"}

{"asctime": "2024-04-07 15:04:02,231", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 1.0893239974975586"}

{"asctime": "2024-04-07 15:04:02,231", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.9845194816589355"}

{"asctime": "2024-04-07 15:04:02,231", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.8789470195770264"}

{"asctime": "2024-04-07 15:04:02,232", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.8751261234283447"}

{"asctime": "2024-04-07 15:04:02,232", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.7643704414367676"}

{"asctime": "2024-04-07 15:04:02,241", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.7685585021972656"}

{"asctime": "2024-04-07 15:04:02,242", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.6691379547119141"}

{"asctime": "2024-04-07 15:04:02,242", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.574512243270874"}

{"asctime": "2024-04-07 15:06:28,467", "levelname": "ERROR", "message": "DataStream 2001 run error", "exc_info": "Traceback (most recent call last):\n  File \"/home/ubuntu/.local/lib/python3.10/site-packages/flumine/streams/datastream.py\", line 172, in run\n    self._stream.start()\n  File \"/home/ubuntu/.local/lib/python3.10/site-packages/betfairlightweight/streaming/betfairstream.py\", line 60, in start\n    self._read_loop()\n  File \"/home/ubuntu/.local/lib/python3.10/site-packages/betfairlightweight/streaming/betfairstream.py\", line 228, in _read_loop\n    received_data_raw = self._receive_all()\n  File \"/home/ubuntu/.local/lib/python3.10/site-packages/betfairlightweight/streaming/betfairstream.py\", line 258, in _receive_all\n    raise SocketError(\nbetfairlightweight.exceptions.SocketError: [Connect: 2002]: Connection closed by server"}

{"asctime": "2024-04-07 15:15:02,315", "levelname": "WARNING", "message": "[FlumineStream: 3001]: Latency high: 0.6098229885101318"}```

---

## 2024-04-08 08:25:55 - issues channel

**Johnnb**

Hi everyone, I'm new here so might be missing something obvious. I'm running an s3marketrecorder in a lightsail instance. I started it yesterday morning and it still seems to be recording ok, but yesterday afternoon it stopped removing the txt and gz files after the markets closed. I got this error at about the time it stopped :

```{"asctime": "2024-04-07 15:06:28,467", "levelname": "ERROR", "message": "DataStream 2001 run error", "exc_info": "Traceback (most recent call last):\n  File \"/home/ubuntu/.local/lib/python3.10/site-packages/flumine/streams/datastream.py\", line 172, in run\n    self._stream.start()\n  File \"/home/ubuntu/.local/lib/python3.10/site-packages/betfairlightweight/streaming/betfairstream.py\", line 60, in start\n    self._read_loop()\n  File \"/home/ubuntu/.local/lib/python3.10/site-packages/betfairlightweight/streaming/betfairstream.py\", line 228, in _read_loop\n    received_data_raw = self._receive_all()\n  File \"/home/ubuntu/.local/lib/python3.10/site-packages/betfairlightweight/streaming/betfairstream.py\", line 258, in _receive_all\n    raise SocketError(\nbetfairlightweight.exceptions.SocketError: [Connect: 2002]: Connection closed by server"}```

The gz files are still being sent to the bucket and there's nothing else in the log apart from a few latency warnings

---

## 2024-04-07 13:33:03 - general channel

**Justice**

I recall the UDP feed I got 4 or 5 years ago was straight from the course, the latency was more like what [@UUE6E1LA1](@UUE6E1LA1) is reporting

---

## 2024-04-07 13:28:25 - general channel

**Justice**

Potentially, though I would have to de-obfuscate the code and I suspect most the latency is from the extra hop to TPD from the course then to the vendor

---

## 2024-04-07 13:15:31 - general channel

**Unknown**

Yes, the difference between the feed time and the time received at my script. I am guessing it will have to route from the course, to TPD then to 3rd party vendor apps hence the poor latency

---

## 2024-04-07 12:54:18 - general channel

**liam**

What is the latency like?

---

## 2024-04-02 18:12:06 - random channel

**Jonjonjon**

I would like a historic recording. Yes thanks I have already used docker stats but I think my Mickey mouse code is slowly increasing Ram and CPU over time. A historic recording will help me check this.

---

## 2024-04-01 08:25:52 - general channel

**Paul**

Why would betfair increase latency across all their markets if you don’t have a license for a third party data product for one sport in one country?

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

## 2024-03-28 13:17:18 - random channel

**ShaunW**

Design a more efficient test? Or just use every 3rd or 4th update. ML is just analysis, a guide, so doesn't need the resolution a simulation does.    Modern hardware speeds means loading everything or just running backtests has become de regueur,   but reintroduce some of the forgotten methodology that makes analysis a distinct disciple in itself.   We had terabytes of data back in the 90s and pathetic hardware, still managed to develop strategy without waiting a month for a figure.

---

## 2024-03-25 14:08:34 - random channel

**Michael**

It's only really useful in certain circumstances, but say you need to analyse the relative performance of two groups of back bets at long odds; if you do that just by using the final result then you'll miss a lot of data because you might be missing out on a lot of bets that nearly won and seeing your results skewed by just a few that made it over the line by a nose. If you pseudo-settle all bets according to whether BATB &lt; 1.2 at any point after your bet matches  then you can capture much richer data and make a better comparison between the groups.

---

## 2024-03-11 12:24:51 - general channel

**liam**

Just check the latency yourself



```market_book.publish_time or market_book.publish_time_epoch```

But yeah fix your code :joy:

---

## 2024-03-11 11:33:59 - general channel

**Bruno**

Hi, I'm having this issue where I think I'm processing the data slower than it's coming in, which leads to a (growing) lag between my code and the market. is there a way to force flumine to discard data above a certain age, or is my only option to use conflation?

---

## 2024-03-06 09:02:00 - general channel

**Prime**

mumbai (for example) to london network latency is around 120ms. If this is a manual user thing, I dont think that's particularly relevant. It also doesnt matter where the server is, as long as its "in the path" between the user and London, as the information will still have to travel from their fingers to London at a maximum of lightspeed.

---

## 2024-03-01 19:56:52 - general channel

**Sen**

Hi Guys. So I do a ton of fundamental modelling and predictions and basically no quick in and out strategies. Basically 0 in play betting. I was thinking of trying to improve my execution using the stream API. Does this make sense? Or is it really only designed for the high frequency betting during in-play markets? 



Does anyone have any know how big the latency diff is in terms of millisecodns between the standard API and the stream API is?

---

## 2024-02-29 13:37:46 - issues channel

**Paul**

Only just saw this, but if it persists, don’t rule out your ISP messing about if it’s from a box at home. I used to work in ISPs and it was quite normal to “sin bin” customers (throttling, increasing latency, and so on) using more bandwidth than seemed reasonable based on contention needs. Normally triggered if they were torrenting, but could be an issue if you’re streaming a lot of market updates…

---

## 2024-02-28 23:27:49 - strategies channel

**AndyL**

```from flumine import config



    config.place_latency = 0.5

    config.cancel_latency = 0.5```

---

## 2024-02-28 23:03:09 - strategies channel

**Andrey Luiz Malheiros**

I'm reading about the usage of SimulatedClient, but I'm unable to find where to set the latency. Is it within the execution_cls attribute?

---

## 2024-02-28 17:48:05 - strategies channel

**AndyL**

Yes see the flumine client config to set latency in simulation 

---

## 2024-02-28 17:22:55 - strategies channel

**Andrey Luiz Malheiros**

Can I set a custom latency for simulation?

---

## 2024-02-28 14:10:01 - strategies channel

**ShaunW**

Shouldn't be any difference, it's just sourcing data from either the stream or the store and from then on presumably it's just the same code?   Live is different though as you're present in the data, live 'you' gets matches that the test instance therfore doesn't.  You've then got to fudge the latency so the test gets there before live did.

---

## 2024-02-28 12:25:45 - issues channel

**foxwood**

Thanks [@U4H19D1D2](@U4H19D1D2) - cleared itself about 12:10 - log shows BF closed order stream and new one working properly now - market stream latency disappeared at same time but connection not remade weirdly.

---

## 2024-02-28 12:00:04 - random channel

**Peter**

What [@UUCD6P13J](@UUCD6P13J) says, and yes a database. I write the orders to it when they're placed and my logging control then dips in again to update those records with the result whe the market it settled. because logging controls are threaded there's unlikely to be any impact on the performance of your strategies when making calls to  the database, even if it's remote (as mine is).

---

## 2024-02-28 11:47:43 - issues channel

**foxwood**

Anybody else seeing latency issues on market stream. I've been getting 0.5 seconds off almost continuously since I started about an hour ago. Have reset the clock so not that. BF issue, BF smacking my legs for some reason, poor connection (is HS fibre) AWS server seems ok recording - just local ?

---

## 2024-02-27 21:03:09 - random channel

**PeterLe**

Maybe someone can give me a steer on this please...

Within my strat, order object I have this code ;



```trade = Trade(

    market_book.market_id,

    runner.selection_id,

    runner.handicap,

    self,

    notes=collections.OrderedDict(

        {

            "back_odds": back,

            "lay_odds": lay,

            "last_price_traded": runner.last_price_traded,

            "publish_time": market_book.publish_time,

            "overround": back_book,

            "underround": lay_book,

            "race_type": market_book.market_definition.race_type,

        }```

I can see the information is being captured and Id like to be able to start looking at this in more detail. (maybe a database perhaps)

Q: At the the time the data is being captured, how do you save it? Is it stored in memory, a file or output to something else

I just wondered whats the best way so I can start to learn, if you could just point me in the right direction that would help..I can pick it up fom there

Thanks

---

## 2024-02-22 08:18:07 - general channel

**liam**

flumine is my third attempt at a framework in python, there will probably be a fourth. Using python comes at a cost when it comes to speed but in terms of development speed I am not sure it can be matched

---

## 2024-02-21 18:49:48 - general channel

**Si**

I’m a C# guy at heart, had to learn Java over the last year or two for the day job. Got into this space in the last month or two. Never touched Python before and discovered BF Lightweight, then subsequently this Slack. If you can code well in one language, then ChatGPT or GitHub Pilot is a game changer at picking up another. Use micro prompts, and slowly build out what your doing.  It helped immensely picking up Java and Python.

---

## 2024-02-21 17:44:01 - general channel

**Ralegh**

Pythons always my goto for research, ideally you should be able to load ML models into other languages at runtime, or use python bindings if available, or at a worst case run python in a separate process and feed targets/forecasts into the trading process. Worst case as in performance but still a very valid approach, anything that latency sensitive can probably be a simpler model anyway

---

## 2024-02-21 14:30:28 - general channel

**ShaunW**

PiQ, not taking your own money, not taking money more than once, latency etc. And still it's only part of a system. There's some sort of pre/post trading analytics to build around it too.

---

## 2024-02-16 12:25:43 - strategies channel

**foxwood**

Wow that was useful for all sorts of other stuff that vanishes as well. Betfair discussion from Oct22 Neil advised:

• For performance reasons, all bet matching takes place in a bulk betting matching cycle, each of which takes ~100 m/s.

So it follows that the 9 - 10 updates per second that I am seeing recorded is realistically best performance and not missing anything :slightly_smiling_face:. It's actually slower than I thought - was thinking 50ms for some reason.

Thanks [@U4H19D1D2](@U4H19D1D2)

---

## 2024-02-12 17:59:06 - general channel

**Tony**

hey all, i have been thinking about this more recently, how  much data is really needed to create a 'decent' model? I look at football and tennis and how valuable is the last 10 seasons with various changes in each sport e.g. tennis court speed, racquets, fitness, covid etc - I'm a big believer of its the quality of the data rather than the amount. Just interested to see what other people think.

---

## 2024-02-11 18:09:25 - strategies channel

**John Foley**

there doesn’t necessarily need to be a “next step.” I wouldn’t feel the need to start removing features unless I was looking to optimise for memory/compute/training time etc. to me it’s for insights and explainability. it’s for questions like:

• which features should I invest time/money in improving?

• why did the model come up with this strange prediction? 

• does the model rely most heavily on the features that I would use if I were making a prediction myself? 

---

## 2024-02-09 17:17:43 - random channel

**PeterLe**

Thanks [@UUE6E1LA1](@UUE6E1LA1) that interesting. I like to think my stuff is like a caterham 7, chassis and an engine no mod cons :grinning:

mind you im still getting a mini performance so we will see :grinning:

---

## 2024-02-09 15:25:32 - random channel

**D C**

I used to find strategy reference string a really useful thing but it ultimately ended up hampering my performance and in conjunction with other things, cost me a lot of money.

I don't use it at all now and just use distinct suffix per strategy on customer order reference strings to distinguish between strats. You live and learn...

---

## 2024-02-08 16:27:49 - strategies channel

**dan**

Sure sorry guys [@UBS7QANF3](@UBS7QANF3) [@U012XF5CNPN](@U012XF5CNPN). I was looking into greyhound or horse racing as I felt those would be the easiest to model, Whatever relevent variables I can find like weight, past performance etc. I come from an ML background but not got much experience in this field so no idea how to find good data!

---

## 2024-02-06 17:40:12 - general channel

**Jeff Waters**

Hi Shaun



I believe that, with back testing, you can separate your data into chunks, and allocate each chunk to a separate process, which speeds up the operation. I believe that each process is run on a separate core, and its memory is independent of the memory used by the rest of the app (though apparently there is still a possibility of race conditions if you're using shared variables, which I don't quite understand).



I would have also expected the stuff in the background to work out how to run code as quickly as possible, but that's not the case in this instance.



As you can probably tell, my knowledge of this stuff is quite vague. For a more technical explanation, see  [https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python](https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python)

---

## 2024-02-04 19:49:45 - general channel

**ShaunW**

I seperate my data collection and trading [@U013K4VNB6D](@U013K4VNB6D). If you ever need to stop your strategy then the collection is unaffected. Plus a hair of a speed advantage if the trading instance isn't also recording although that can be done asynchronously if you're short of available connections and have to trade and record at the same time. But I'm not using flumine so it could be different in terms of routing one api connection to multiple strategy instances.

---

## 2024-02-03 16:29:25 - general channel

**Dave**

ROC curve is generally quite good for evaluating classification performance, so you can compare ROC curves of your two sets of estimates.

---

## 2024-02-02 17:56:45 - general channel

**ShaunW**

Hi. Try to focus on the specfic things you're investigating. You only need the whole stream for high frequency stuff and that can't really be explored in CSVs, you'd use a backtest for that. But try using a backtest (with no actually betting strategy, just a blitz through the data)  as a means of logging if the data doesn't directly store what you need, or to extract at a lower frequncy, or just in certain conditions.  Also work on just a subset of your data warehouse and then test against the remaining data to safeguard against backfitting and to speed up your analysis.

---

## 2024-02-02 07:37:47 - general channel

**Aiyaj Khalani**

no, i am just thinking about how can we improve latency while placing a bet from my server which is based on india to betfair API

---

## 2024-02-02 05:06:31 - general channel

**Aiyaj Khalani**

Hi All,

I have deployed my server in london which is interacting with betfair API. i am calling API for placing bet hosted on my sever. for live events, it seems betfair is taking around 5.5s to place a bet. but since my user is not from the london and its from india, i see extra 1s overhead on sending request to my server. i thought of moving my server to india but then betfair APIs will not be accessible from my server. i was thinking to add VPN in my server to interact with betfair API but again it will add some extra overhead due to VPN proxy. I saw many exchanges place bets around 5.5s, is there any good way to reduce latency in my case?

---

## 2024-02-01 14:37:34 - issues channel

**PeterLe**

I use certificate's too, although it must have been pure luck getting it working :grinning:

from memory I think I used the instructions here ; [http://www.betfairprotrader.co.uk/2015/08/creating-digital-certificate-for-betfair.html](http://www.betfairprotrader.co.uk/2015/08/creating-digital-certificate-for-betfair.html)



you will need to add something like this in your code too :

```trading = betfairlightweight.APIClient(myacc, mypass, app_key, certs=r"C:\certs")```



---

## 2024-01-28 21:17:15 - strategies channel

**Ralegh**

Makes sense, and yeah shouldn’t matter either way if not latency sensitive.



I think generally I try to keep trading code stateless so the logic by default would just be to ignore failed orders and only retry if conditions are still true. Target position = (calculation)… trade while position &lt; target position. Or target position at price level = (calculation) and the same

---

## 2024-01-28 21:05:44 - strategies channel

**liam**

My initial point was regarding latency sensitive strategies and it’s something I have never really though about / ignored.



Regarding the cost I guess it’s a case of handling the retry and it’s logic, it’s just another complication and if it’s not latency sensitive surely just a retry is the simple option as it’s only been ~500-1000ms 

---

## 2024-01-28 20:40:19 - strategies channel

**Ralegh**

Does it? I’d assume if you’ve already done the round trip to hear a place order failed then super latency sensitive stuff would have gone already, otherwise unless you’re taking a lot of time to process it should be similar latency wise to just resubmitting a failed order, but you wouldn’t resubmit if the condition had changed. If you’re doing heavy calculations with latency sensitivity I’d assume you’d need to offload to another thread and cache the results anyway, and just do a quick check of e.g price &gt; X, so don’t see how it’d be different. Not sure what context you’re talking about though

---

## 2024-01-22 19:15:22 - random channel

**liam**

That is place, cancel or replace latency which has an overhead on the betfair side 

---

## 2024-01-22 16:42:08 - random channel

**Paul**

Also might be worth looking at the distribution of latencies. [@U4H19D1D2](@U4H19D1D2) posted about being non-profitable at 250ms added latency the other day. If you were running that strategy with p95 +/- 10ms, you’d be probably fine. But at p99 +/- 500ms, maybe not…

---

## 2024-01-22 16:38:09 - random channel

**Paul**

If your EV is latency dependent, possibly awful. If you’re not, it’s less thank a blink of an eye and you’re miles ahead of the betangel lot. :shrug: 

---

## 2024-01-22 16:10:00 - random channel

**foxwood**

Bored so thought I'd try that ping on my new Irish Lightsail server - it's meaningless for what I do but shows that milliseconds are too coarse for latency measurement these days

`Approximate round trip times in milli-seconds:`

    `Minimum = 0ms, Maximum = 1ms, Average = 0ms`

---

## 2024-01-22 15:33:19 - random channel

**Paul**

The brakes Betfair apply to latency sensitive strategies are called “transaction fees”. :joy: We have all paid them and moved on. :clown_face: If you’re a millisecond faster than the next guy, good for you, but just remember EV extracted through exploiting low latency is hard to keep as an advantage, as it’s the easiest capability to “just” spend money solving for. Only a matter of time before someone is consistently a nanosecond faster than you.

---

## 2024-01-21 19:46:22 - random channel

**Jonjonjon**

This is what I get from a grep on my logs. Is that latency value how long it takes to place the order?



```cat my_log_file.txt | grep execute_place | grep -o -P  '\"latency\"(.*?),'

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0003,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0043,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0045,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.026,

"latency": 0.0003,

"latency": 0.0006,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0004,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0042,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0045,

"latency": 0.0034,

"latency": 0.0001,

"latency": 0.0053,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0027,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0028,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0005,

"latency": 0.0003,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0027,

"latency": 0.0073,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0044,

"latency": 0.0001,

"latency": 0.0002,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0002,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0171,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0003,

"latency": 0.0001,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0033,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0,

"latency": 0.0002,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0003,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.005,

"latency": 0.0003,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0092,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0006,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.003,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0003,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0003,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0073,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0004,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0006,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0073,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0019,

"latency": 0.0057,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0003,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0003,

"latency": 0.0035,

"latency": 0.0003,

"latency": 0.0003,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0,

"latency": 0.0,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0003,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0043,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0055,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0003,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0002,

"latency": 0.0165,

"latency": 0.0001,

"latency": 0.0002,

"latency": 0.0001,

"latency": 0.0001,

"latency": 0.0001,```

---

## 2024-01-21 15:57:59 - general channel

**liam**

streaming_timeout on the market filter / strategy from memory 

---

## 2024-01-20 19:27:45 - random channel

**AndyL**

[@UQL0QDEKA](@UQL0QDEKA) i had a serious performance issue a couple of months back and i used cprofilev and reduced my processing time by a factor of 5, it’s really easy to use

---

## 2024-01-19 14:06:32 - strategies channel

**Mo**

In my apparently wrong opinion it should be `sum(profit) / sum(liability)` where for back bets the liability is equal to the matched stake. I also use ROI as the headline metric in comparing strategies, monitoring for degrading strategy performance, identifying areas where strategies need improvement, and evaluating the impact of said improvements

---

## 2024-01-19 12:47:29 - random channel

**PeterLe**

[@U0128E7BEHW](@U0128E7BEHW), [@UUE6E1LA1](@UUE6E1LA1), [@UEA14GBRR](@UEA14GBRR), you guys seems to know C#...do you mind if I ask a question please?

One of the applications Im running is an old version...its been chugging away for years so reluctant to change really...

However I got this feed back from ChatGpt :

Usage of HttpWebRequest: The code snippet shows the use of `HttpWebRequest`. While this is still a valid class in .NET, it's considered somewhat outdated compared to newer HTTP client libraries like `HttpClient`. If not already updated later in the code, consider using `HttpClient` for more efficient network operations and better support for asynchronous operations.

-----

in your view, would you think this a priority to change to HttpClient ?

(It may well be that the outdated version is successful because it is slower perhaps, so if I did update, maybe Id run AB tests  old v new etc)

Anyway, Id welcome your thoughts please? (Im wondering if its a no brainer to update to asynchronous?) Thanks

---

## 2024-01-18 13:48:21 - random channel

**ShaunW**

Didn't know that [@UQL0QDEKA](@UQL0QDEKA) I use 4.5 and it told me I couldn't give it a whole project? Fully compiled [@UUE6E1LA1](@UUE6E1LA1) I don't have any special setting for the compiler. With placement being anywhere from 80ms to 170ms I spend more time on improving the strategy than trying to shave off half a millisecond. I process market change messages and orders asynchronously anyway so not struggling for speed too much.

---

## 2024-01-18 13:10:18 - random channel

**Lee**

Entirely depends on your goals. If you want to optimise for speed/latency it’s essential. You need to have a baseline measurement to know where the bottlenecks and if your changes actually make any difference otherwise it’s just guesswork.

---

## 2024-01-18 13:07:21 - random channel

**Mo**

Again, I think the comments are fair. betfairutil code is primarily designed to be readable, defensive, and composable with less emphasis on performance.



My function wouldn't give you the book percentage based on the last traded price and there's probably not a trivial way to do so using other betfairutil functions so I think it's entirely reasonable to keep using your function/ChatGPT's optimised version of your function.



I'm just always on the lookout for feedback on betfairutil.

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

## 2024-01-18 12:45:22 - random channel

**Mo**

I agree with ChatGPT's comments - I'd rather explicitly check for usable data ahead of time than rely on try-except. While the latter I think is sometimes considered more "Pythonic", I still prefer the code-style of the former and there are performance considerations

---

## 2024-01-18 12:37:19 - random channel

**PeterLe**

I just fed some of my code into Chatgpt for comments on how to optimse.

it suggested that this code ;



```def calculate_book_percentage(runners):

    back_book = 0

    lay_book = 0

    ltp_book = 0



    for runner in runners:

        if runner.status == "ACTIVE":

            try:

                back = get_price(runner.ex.available_to_back, 0)

                if back:

                    back_book += 1 / back

            except AttributeError:

                return None



            try:

                lay = get_price(runner.ex.available_to_lay, 0)

                if lay:

                    lay_book += 1 / lay

            except AttributeError:

                return None



            if runner.last_price_traded:

                ltp_book += 1 / runner.last_price_traded



    return round(back_book, 4), round(lay_book, 4), round(ltp_book, 4)```

be replaced by this code

```def calculate_book_percentage(runners):

    back_book, lay_book, ltp_book = 0, 0, 0



    for runner in runners:

        if runner.status != "ACTIVE":

            continue



        back = get_price(runner.ex.available_to_back, 0)

        lay = get_price(runner.ex.available_to_lay, 0)

        ltp = runner.last_price_traded



        if back:

            back_book += 1 / back

        if lay:

            lay_book += 1 / lay

        if ltp:

            ltp_book += 1 / ltp



    return round(back_book, 4), round(lay_book, 4), round(ltp_book, 4)```

The rationale presented as ;

Key Changes:

1. Removed `try-except` Blocks:

    ◦ The original version used `try-except` blocks to catch `AttributeError` if the `available_to_back` or `available_to_lay` prices were not available. This can be inefficient in a loop.

2. Direct Checks for Price Availability:

    ◦ The optimized version directly checks if the `back` and `lay` prices are available using simple `if` statements, which is more efficient than handling exceptions.

3. Simplified Logic:

    ◦ Streamlined the logic to be more concise and straightforward, improving readability and performance.

By making these changes, the function becomes more efficient, especially in a real-time data processing context where

every millisecond counts



I've tested in back tests (all ok) and ran it live yesterday, all OK.

As I only know a very basic amount about Python, would any more experienced coders comment as to whether it is a positive change for the better? Thanks

---

## 2024-01-17 22:41:57 - random channel

**Andrey Luiz Malheiros**

Yes, I am using performance suggestions, including multiprocessing. But thank you anyway, I will profile my code and see what is happening.

---

## 2024-01-17 19:38:56 - random channel

**Jonjonjon**

If you haven't already, please read this page: [https://betcode-org.github.io/flumine/performance/](https://betcode-org.github.io/flumine/performance/)

---

## 2024-01-16 17:41:03 - general channel

**Unknown**

the pitchforks may get pointed at me for this but - just an opposing view on betfair basic data. because it gets a very bad rap in here and needs some friends



• it is definitely useless if you’re trying to do anything low-latency/inplay/high frequency/purely market data-driven

• if your work (like mine) does not fall into this category, its a totally fine place to start. i found it extremely useful when starting out

• a runner’s last traded price accurate to within 1 minute (available in basic data) is far from useless. could be the thing that makes your purely fundamentals model into something profitable

---

## 2024-01-16 15:35:15 - general channel

**PeterLe**

I was just thinking...I have two strats running on separate instances (the code/logic for the strat is slightly different on each)

When I get the latency messages I get it on both instances (never on just one or the other), so that would suggest its not the strat code then ?

Could well be the clock timing in some way as you say...

Anyway, if I dont find the problem how can I disable just the latency message Liam?

---

## 2024-01-16 15:22:45 - general channel

**PeterLe**

Well Ive had these on and off intermittently Liam since I started using Flumine (either when running locally or on AWS).

Some days its fine, last 3 or 4 days have been fine for instance..

I usually have the terminal window visible so i can keep my eye on it when doing the day job alongside...ie of any error messages etc..

When the latency message comes through it just streams down the page and I can see other messages

I know its there for a reason but its working and making profits etc

---

## 2024-01-16 15:21:38 - general channel

**ShaunW**

.... To account for less than ideal connections you could have the high latency warning threshold calculated on the fly from a recent average + allowable diff? Scope creep tho.

---

## 2024-01-16 14:59:38 - general channel

**PeterLe**

I know its a basic noddy question but how do i turn off the Market Stream - 'Latency High' messages?

Would I comment out the line that is printing it, or set the level of the messages so these (info ?) type are missed. Thanks

---

## 2024-01-10 14:00:47 - general channel

**Trex44**

[@U04NWADNCFR](@U04NWADNCFR) Hey mate, do you know why Athena seems to hate nearly all parquet files? If I use Athena on CSVs its fine but if I use it on the same data saved as parquets it can usually find a way to error and there isn't enough information in the error for me to figure out the issue. For speed and costs I was hoping to save my data as parquets but at the moment can't.

---

## 2024-01-08 19:36:18 - strategies channel

**mandelbot**

And how do you calculate your latency?

---

## 2024-01-08 18:20:04 - strategies channel

**mandelbot**

How do you record latency along with your orders?

---

## 2024-01-08 06:28:10 - strategies channel

**liam**

It’s all simulated, I do something similar to above but needs different code to go negative on the signal latency 

---

## 2024-01-07 22:53:37 - strategies channel

**foxwood**

Guessing he tweaks the latency factors in config.py ...

```# latencies used for simulation

place_latency = 0.120

cancel_latency = 0.170

update_latency = 0.150

replace_latency = 0.280```

Might be interesting to find out my live latency and mod those variables to match so backtests closer to (my) real world timings - yet another thing for the puzzles board.

---

## 2024-01-07 19:30:26 - strategies channel

**Unknown**

Spoken a lot about latency vs profit recently but not sure I have shared an example. Here is how one of my strategies performs when simulated, for example there is a 50% drop in profit with just a 0.25s delay!

---

## 2024-01-06 18:47:27 - random channel

**liam**

Yeah removing network latency and just focusing on what flumine is doing 

---

## 2024-01-06 12:43:15 - random channel

**liam**

If you record the latency per bet and plot it, you can see how sensitive you are to 0.001/0.01/0.10s per latency

---

## 2024-01-06 12:39:53 - random channel

**PeterLe**

latency is important to me.

So by example; If you wanted to run say 5 strats (on one account) that pace a high number of bets then ideally one start per instance rather than 5 starts per instance. Optimal would be to run the starts on separate instances/accounts I expect?

---

## 2024-01-06 12:35:02 - random channel

**liam**

I normally don’t go above 5, strategy dependant, they are called sequentially and in order so it depends how sensitive you are to latency. When optimising the preference would be 1 strategy per instance, I record tick to trade to monitor this 

---

## 2024-01-06 12:00:23 - random channel

**Jonjonjon**

The latency on the final one increases to about 0.15s

---

## 2023-12-15 18:15:20 - general channel

**Paul**

Do they actually differ? I’m not that into dogs but this question surprised me. If the data does not exist, I think you could either create it (lots of decent open source GIS data out there), or normalise it through dog performance at different tracks, maybe?

---

## 2023-12-12 15:09:43 - random channel

**George Swindells**

[@U05N9773A23](@U05N9773A23) Best to email the sales team ([mailto:info@totalperformancedata.com|info@totalperformancedata.com](mailto:info@totalperformancedata.com|info@totalperformancedata.com) i think) to see what they're offering these days, I don't get involved in that process much anymore unless I'm asked to prepare a sample of data for a prospective client

---

## 2023-12-12 11:03:18 - random channel

**D C**

I can see why people would find the drone feed more useful - more for the angle than the latency difference (especially in the finishing straight). Never used it myself but seen it posted that people have paid £500 a day for these pics. Could be absolute bollocks but thats quite a deficit to be making up the markets on a daily basis.

---

## 2023-12-12 09:15:56 - strategies channel

**Adam**

Hey quick question: does Flumine manage streams at the framework level or the strategy level? e.g. If I start two seperate strategies within the same framework that stream events from the *exact same markets (i.e* `framework.add_strategy(strategy1)` and `framework.add_strategy(strategy2)`), would it open one stream that both strategies ingest from, or two separate streams? If it’s the latter, would that increase latency since the network request is doubled?

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

## 2023-12-10 13:25:41 - general channel

**AndyL**

I found cprofilev great to profile my strategies, I improve my performance by a factor of about x4

---

## 2023-12-08 07:10:00 - general channel

**Mo**

Are you doing this in flumine? Have you followed all of the guidance on performance? [https://betcode-org.github.io/flumine/performance/|https://betcode-org.github.io/flumine/performance/](https://betcode-org.github.io/flumine/performance/|https://betcode-org.github.io/flumine/performance/)

---

## 2023-12-04 17:40:26 - strategies channel

**Derek C**

As for the SHAP results, I had to look it up to refresh my memory but I think this graph is showing most useful features from top to bottom. Feature 1 predicts a winner when it has a low value, as does 2 &amp; 3 (all the red dots are clustered together). I think feature 7 isn't very predictive - both high and low values are mostly red. That is my understanding but happy to be corrected. [https://datascience.stackexchange.com/questions/65307/how-to-interpret-shapley-value-plot-for-a-model](https://datascience.stackexchange.com/questions/65307/how-to-interpret-shapley-value-plot-for-a-model)

---

## 2023-12-04 10:22:05 - random channel

**Johnny**

I'm just using the example marketrecorder.py.  It seems to die (docker container restarts) on match days which means I have a load of incomplete market files - been checking the logs and get a load of "latency high" lines followed by a timeout error.  Maybe subscribing to too many markets is the issue, will try narrowing it down next



```{"asctime": "2023-12-03 13:12:51,407", "levelname": "ERROR", "message": "_get_cleared_market error", "exc_info": "Traceback (most recent call last):\n  File \"/usr/local/lib/python3.11/site-packages/flumine/worker.py\", line 235, in _get_cleared_market\n    cleared_markets = betting_client.betting.list_cleared_orders(\n                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/local/lib/python3.11/site-packages/betfairlightweight/endpoints/betting.py\", line 434, in list_cleared_orders\n    (response, response_json, elapsed_time) = self.request(method, params, session)\n                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/local/lib/python3.11/site-packages/betfairlightweight/endpoints/baseendpoint.py\", line 54, in request\n    self._error_handler(response_json, method, params)\n  File \"/usr/local/lib/python3.11/site-packages/betfairlightweight/endpoints/baseendpoint.py\", line 80, in _error_handler\n    raise self._error(response, method, params)\nbetfairlightweight.exceptions.APIError: SportsAPING/v1.0/listClearedOrders \nParams: {'betStatus': 'SETTLED', 'marketIds': ['1.221745228'], 'customerStrategyRefs': ['d69966378a3d'], 'settledDateRange': {'from': None, 'to': None}, 'groupBy': 'MARKET'} \nException: None \nError: {'code': -32099, 'message': 'ANGX-0010', 'data': {'APINGException': {'requestUUID': 'ie2-ang26b-prd-09131022-00af825869', 'errorCode': 'TIMEOUT_ERROR', 'errorDetails': ''}, 'exceptionname': 'APINGException'}} \nFull Response: {'jsonrpc': '2.0', 'error': {'code': -32099, 'message': 'ANGX-0010', 'data': {'APINGException': {'requestUUID': 'ie2-ang26b-prd-09131022-00af825869', 'errorCode': 'TIMEOUT_ERROR', 'errorDetails': ''}, 'exceptionname': 'APINGException'}}, 'id': 1}", "trading_function": "list_cleared_orders", "response": "SportsAPING/v1.0/listClearedOrders \nParams: {'betStatus': 'SETTLED', 'marketIds': ['1.221745228'], 'customerStrategyRefs': ['d69966378a3d'], 'settledDateRange': {'from': None, 'to': None}, 'groupBy': 'MARKET'} \nException: None \nError: {'code': -32099, 'message': 'ANGX-0010', 'data': {'APINGException': {'requestUUID': 'ie2-ang26b-prd-09131022-00af825869', 'errorCode': 'TIMEOUT_ERROR', 'errorDetails': ''}, 'exceptionname': 'APINGException'}} \nFull Response: {'jsonrpc': '2.0', 'error': {'code': -32099, 'message': 'ANGX-0010', 'data': {'APINGException': {'requestUUID': 'ie2-ang26b-prd-09131022-00af825869', 'errorCode': 'TIMEOUT_ERROR', 'errorDetails': ''}, 'exceptionname': 'APINGException'}}, 'id': 1}"}```

---

## 2023-11-27 16:13:06 - random channel

**Javier Martín Pérez**

Yes, in my case is latency but also the use of the CPU going above 60% which is not ideal in theory

---

## 2023-11-27 16:11:18 - random channel

**Johnny**

How does one know when more compute or memory is needed?  Is it the latency warnings?

---

## 2023-11-23 09:11:06 - strategies channel

**Mo**

It doesn't seem crazy to start with a linear decay. I think probably using backtest performance to compare different weighting schemes is a good way forward

---

## 2023-11-22 09:57:02 - random channel

**Justice**

According to the webpage, he is a data scientist at TPD: [https://www.totalperformancedata.com/about-us/](https://www.totalperformancedata.com/about-us/)

---

## 2023-11-18 11:35:11 - general channel

**Prime**

if you have a streaming json decoder then its not such a big deal. however if, like most people, you download the whole json message then decode it in one go and then handle each market in sequence, you will do much better if the snapshot is segmented because you can start doing your market handling faster, while the rest of the json downloads and decodes on another thread and feeds that process. on betfair's side, they prefer segmented messages because it reduces memory load when assembling very large messages and allows them to send you data faster as the first message will be ready more quickly. generally, most of the time, because this is all startup stuff its not very relevant. on our systems we certainly never bother with it. we talk to betfair via 1/10 Gbit links and initial decoding only happens once before any trading etc kicks in. imo it's all Joe's fault.

---

## 2023-11-17 19:22:59 - issues channel

**AndyL**

[@U4H19D1D2](@U4H19D1D2) thanks Liam, yes, I think i've worked it out, it's not a memory leak per-se. Basically since I added PLACE to the listener, I am now subscribing GB,IE and WIN,PLACE for this one strategy, and it actively trades from 3hours out from startTime. What I see is a gradual increase in CPU towards mid-day when the main afternoon races fall within that 3hour window. I roughly calculated the market processing thread will be going around 50 markets, and my strategy code is probably not as efficient as it could be... My VM CPU then hits 50% in a 2vCPU box, which then starts to limit it, the affect it had was to cause the market update processing to lag the live updates, causing a steady progression of increase in latency, eventually towards a latency of 30mins!!! My trading  logic once the latency hit around 5mins was starting to put orders in for markets that were now closed! Thus getting lots of BF errors, and what made things worse for my hedge bets I was rather stupidly immediately re-placing the failed hedge causing yet more of a race......and eventually bang!

What i've learned:

1. I need to profile my strategy code more to try and make it more efficient. I've already done a good set of fixes...

2. I'm perhaps pushing my luck adding PLACE and doubling the number of active markets in that 3hour trade window, running on a single Flumine instance....

3. Importantly I need to monitor "latency" to prevent this sort of CPU race condition

I've done a set of fixes for 1 & 3 and I'm testing them now.....

---

## 2023-11-17 14:59:38 - general channel

**Alex A**

Bit strange that they recommend enabling it for performance, as performance while processing the initial snapshot will be orders of magnitude worse than normal with or without segmentation.

---

## 2023-11-16 17:48:31 - issues channel

**AndyL**

followed eventually by Flumine instance being OOM killed !!:

```[571936.357166] oom-kill:constraint=CONSTRAINT_NONE,nodemask=(null),cpuset=/,mems_allowed=0,global_oom,task_memcg=/user.slice/user-1000.slice/session-72.scope,task=python3,pid=18874,uid=1000

[571936.357231] Out of memory: Killed process 18874 (python3) total-vm:2811936kB, anon-rss:1657564kB, file-rss:0kB, shmem-rss:0kB, UID:1000 pgtables:3488kB oom_score_adj:0

[571937.565101] loop6: detected capacity change from 0 to 8```

---

## 2023-11-16 17:45:57 - issues channel

**AndyL**

Hi [@U4H19D1D2](@U4H19D1D2) what does this mean in real terms please?

```{"asctime": "2023-11-16 11:55:48,259", "levelname": "WARNING", "message": "High latency between current time and OrderPackage creation time, it is likely that the thread pool is currently exhausted", "trading_function": "cancel", "session": "&lt;requests.sessions.Session object at 0xffff62401130&gt;", "latency": 0.29, "order_package": {"id": "14c7f3f3-8477-11ee-98e5-77b81b73792a", "client": "&lt;flumine.clients.betfairclient.BetfairClient object at 0xffffb03a1ac0&gt;", "market_id": "1.221270586", "orders": ["139194285340131329"], "order_count": 1, "package_type": "Cancel", "customer_strategy_ref": "aaaa", "bet_delay": 0, "market_version": null, "retry": true, "retry_count": 0, "async": false}, "thread_pool": {"num_threads": 18, "work_queue_size": 0}}```

followed by lots of these later on:

```{"asctime": "2023-11-16 13:28:46,316", "levelname": "WARNING", "message": "High latency between current time and MarketBook publish time", "market_id": "1.221270587", "latency": 68.93769669532776, "pt": "2023-11-16T13:27:37.379000"}```

---

## 2023-11-10 19:50:36 - issues channel

**liam**

What’s your latency like for place / cancel requests?

---

## 2023-11-10 18:06:51 - issues channel

**AndyL**

thanks [@UQL0QDEKA](@UQL0QDEKA) So i've moved to a AWS t4g, and no latency issues anymore,which is progress.

However, bot still having issues which looks like a coding bug of mine, it's interesting it's taking a while to develop given this version of the instance has been running a month, but this week my "hedging" is failing, and i'm getting loads of these exceptions:

```Order does not currently have a betId```

Which is odd, unfortunately it's in my hedging logic, I need to handle it better I think.

But [@U4H19D1D2](@U4H19D1D2) how does an Order not have a betId ?

---

## 2023-11-09 20:50:31 - issues channel

**AndyL**

happens more frequently when latency spikes

---

## 2023-11-09 19:24:32 - issues channel

**AndyL**

[@U4H19D1D2](@U4H19D1D2) had a bit of an issue with one of my Flumine processes that eventually crashed the VM, thought i'd pass it by you incase it looks familiar. My naive view it looks a bit like a run-away thread/resource issue..?

• Flumine 2.4.2 betfairlightweight 2.17.3

looking at the "logs", the issue looked to start gradually with periodic:

```High latency between current time and OrderPackage creation time, it is likely that the thread pool is currently exhausted", "trading_function": "cancel", "session": "&lt;requests.sessions.Session object at 0x7f70f376bc40&gt;", "latency": 0.381, "order_package": {"id": "xxxxx", "client": "&lt;flumine.clients.betfairclient.BetfairClient object at 0x7f7119b1b6a0&gt;", "market_id": "1.220926100", "orders": ["139188221331829894"], "order_count": 1, "package_type": "Cancel", "customer_strategy_ref": "XXXXX", "bet_delay": 0, "market_version": null, "retry": true, "retry_count": 0, "async": false}, "thread_pool": {"num_threads": 26, "work_queue_size": 3}}```

then a few mins later got:

```"High latency between current time and MarketBook publish time", "market_id": "1.220920848", "latency": 2.08534836769104, "pt": "2023-11-09T11:37:19.521000"}```

this repeated then "continuously" with latency time steadily increasing... message being issued about 50/second

```{"asctime": "2023-11-09 11:40:30,227", "levelname": "WARNING", "message": "High latency between current time and MarketBook publish time", "market_id": "1.220926100", "latency": 14.246732711791992, "pt": "2023-11-09T11:40:15.981000"}```

then about 150 warnings/second

```{"asctime": "2023-11-09 11:54:22,299", "levelname": "WARNING", "message": "High latency between current time and MarketBook publish time", "market_id": "1.220920734", "latency": 176.0338258743286, "pt": "2023-11-09T11:51:26.266000"}```

eventually the increasing CPU usage killed the AWS VM which I had to reboot via the console

---

## 2023-11-06 15:05:50 - random channel

**liam**

Latency certainly impacts EV for me

---

## 2023-11-05 18:00:13 - general channel

**liam**

[https://betcode-org.github.io/flumine/performance/|https://betcode-org.github.io/flumine/performance/](https://betcode-org.github.io/flumine/performance/|https://betcode-org.github.io/flumine/performance/)

---

## 2023-11-05 17:58:45 - general channel

**Trex44**

Hey all, is there a way to speed up the back test code [https://github.com/betcode-org/flumine/blob/master/examples/simulate-sportsdata.py|here](https://github.com/betcode-org/flumine/blob/master/examples/simulate-sportsdata.py|here) using  multiprocessing ? I want to speed it up when testing 1000's of markets.

---

## 2023-11-02 14:25:50 - strategies channel

**liam**

Have you read [https://betcode-org.github.io/flumine/performance/|this](https://betcode-org.github.io/flumine/performance/|this)?

---

## 2023-10-19 10:24:12 - general channel

**Unknown**

Hi folks,



I think I may be getting somewhere, but very slowly!

The attached code is attempting to use a MarketRecorder strategy to record a simulated market but I'm running into the attached error in marketrecorder.py.

It seems there is no "id" property in the data object. I've tried hard-coding market_id to be the actual market id but this then creates a some new problems, which I'm happy to go into if anyone thinks necessary.

---

## 2023-10-16 10:33:40 - strategies channel

**Unknown**

*ML Day 70*



Haven't given up, after exploring a few algos I found that using XGBoost seemed to be the most applicable / get the best results in terms of accuracy on the problem I was trying to solve. Using my current prediction I used the algo to predict the error (delta), from my understanding this is a common technique (does it have a name?) and proved to be far more accurate than starting 'fresh'.



Had a few issues with latency when simulating using the sklearn integration as its considerably slower compared to using the low level [https://xgboost.readthedocs.io/en/stable/python/python_api.html|library](https://xgboost.readthedocs.io/en/stable/python/python_api.html|library).



However the improvements just didn't equate to more profit, I have since worked on trying to get the algo to reveal what it was doing. I started reverse engineering / brute force by plugging in values that I believe had the highest importance and graphing the results. Without revealing too much this gave me a regression model for the variables as opposed to an 'if statement' on the min/max, not sure this is how I am supposed to be using machine learning but its working for me right now :joy:

---

## 2023-10-16 07:22:53 - general channel

**liam**

Depends, latency is a sliding scale, where are you on the scale?

---

## 2023-10-15 21:46:27 - general channel

**Rishab**

Does running all the markets for a sport(say horse racing) in just 1 flumine instance affect the strategy in any way if my strategy is latency sensitive?

---

## 2023-10-15 19:40:23 - strategies channel

**Jonjonjon**

Have you tried throwing the same data at different algorithmns? I found that for my dataset, Elastic Net CV gave better out-of-sample performance than Random Forest.

---

## 2023-10-05 15:28:07 - general channel

**river_shah**

`flumine[speed]`just ensures that `befairlightweight[speed]` is used. No other optimisations in flumine itself?

---

## 2023-10-05 09:41:44 - general channel

**Andy B**

That doesn't help with speeding up the simulation unfortunately.

---

## 2023-10-05 06:36:37 - general channel

**Andy B**

If there is a better way to do my back tests, I'm happy to learn.  I have three strategies in the one back test, and I want to be able to place no more than 1 bet on a runner in each strategy.  I was using the following to speed up market processing:

if 'processed' not in market.context:

                market.context['processed'] = True



This has the impact of preventing other strategies from processing that market and that means my test results are incorrect.  I changed that code to:



if 'processed' not in self.context:

                self.context['processed'] = True



This appears to allow each strategy to process the market, although I haven't definitively proved that yet.    If there is a better way to do this, let me know.

---

## 2023-10-03 16:51:30 - random channel

**Johnny**

Have you got a subscription?  Wonder if actual performance is anything like the video

---

## 2023-10-01 09:41:46 - general channel

**Andy B**

I had avoided that as I thought the memory overhead would be a problem, but I think you are right, it's possibly the simplest way forward.

---

## 2023-09-30 18:20:58 - random channel

**river_shah**

The `gpt-manager` gets angry and writes a lengthy negative performance review for `gpt-engineer` forever impeding promotion / compensation progress

---

## 2023-09-29 03:50:37 - general channel

**Andy B**

Hi All, I am trying to create a backtest based on the Aus PRO greyhound files from betfair.  I can see that the box\trap number is included in the bane value in the raw files, but I can't find a way to get it out in the back test.  In the live stream I would do something like:



Box = [x.runner_name for x in market.market_catalogue.runners if x.selection_id == runner.selection_id]

Box = Box[0].split('. ')[0]



As far as I can work out, there is no market_catalogue when using the PRO files to backtest, although maybe I have missed something logical.  I could provide the data I need from an alternative source, but I don't really want to do that because a:) it is very memory intensive to store large amounts of data in a multi-threaded backtest and b:) the data is in the raw files, so I should be able to access it.  I've searched through previous threads in here and I've looked at the betcode FAQ on github, and I am feeling like I may not be able to do this simply using flumine, but I am sureother people have found a way around this, so I am curious how it is being done.

---

## 2023-09-28 14:27:20 - strategies channel

**liam**

[https://robotjames.com/posts/kwant-signal-trade-offs-in-the-real-world/|kwant signal trade-offs in the real world](https://robotjames.com/posts/kwant-signal-trade-offs-in-the-real-world/|kwant signal trade-offs in the real world)



Well worth reading the other posts, he is able to articulate a lot of what I do a lot better than I have ever managed :joy:



&gt; *&lt;https://robotjames.com/posts/how-scalable-is-this-strategy/

&gt; |how scalable is this strategy?&gt;*

&gt; friend asks "how do i know how scalable this strategy is?"

&gt; one very simple thing you can do to get an idea, is to look at the decay in simulated performance when you delay acting upon your signals.

&gt; how much worse does it look if you delay your rebalance trades by 15m, 60m, 4h etc?

&gt; slow decay means you might have a chance of sizing it up.

&gt; if it falls off a cliff, you probably gotta stay small and nimble in that strategy.

&gt; we're always trading at other people's prices and can only eat what we are fed.

&gt; beep....boop

---

## 2023-09-24 11:36:55 - general channel

**TT**

I've not delved into the code too much but I saw this:

[https://github.com/TotalPerformanceData/gmaxfeed/blob/87e58cf32fcb2e2c3ea147dcdeaa15fbd4f96091/gmaxfeed/feeds/record_live.py](https://github.com/TotalPerformanceData/gmaxfeed/blob/87e58cf32fcb2e2c3ea147dcdeaa15fbd4f96091/gmaxfeed/feeds/record_live.py)

---

## 2023-09-24 11:33:39 - general channel

**Unknown**

I came across this library which may be of interest:

[https://github.com/TotalPerformanceData/gmaxfeed/](https://github.com/TotalPerformanceData/gmaxfeed/)



I haven't used it, but it appears to be what you are looking for i.e access to the raw data with a TPD licence. Has anyone else used this?

---

## 2023-09-23 15:05:24 - general channel

**Trex44**

Hey, just wondering. It it common to get Latency High warning such as the ones below.

```{"asctime": "2023-09-23 14:03:32,716", "levelname": "WARNING", "message": "[MarketStream: 2001]: Latency high: 0.9683074951171875"}

{"asctime": "2023-09-23 14:03:32,720", "levelname": "WARNING", "message": "[MarketStream: 2001]: Latency high: 0.864220142364502"}

{"asctime": "2023-09-23 14:03:32,725", "levelname": "WARNING", "message": "[MarketStream: 2001]: Latency high: 0.8646314144134521"}

{"asctime": "2023-09-23 14:03:32,741", "levelname": "WARNING", "message": "[MarketStream: 2001]: Latency high: 0.6966798305511475"}

{"asctime": "2023-09-23 14:03:32,743", "levelname": "WARNING", "message": "[MarketStream: 2001]: Latency high: 0.6270527839660645"}

{"asctime": "2023-09-23 14:03:32,748", "levelname": "WARNING", "message": "[MarketStream: 2001]: Latency high: 0.5797228813171387"}

{"asctime": "2023-09-23 14:03:32,759", "levelname": "WARNING", "message": "[MarketStream: 2001]: Latency high: 0.5898082256317139"}```

---

## 2023-09-21 15:17:59 - general channel

**Mona**

Hi thanks, I haven't profiled it yet, but did a simple profiling on `process_market_book` function after I removed the writing of the structure data into csv, the whole function takes less than tenths of a second to execute, the high latency issue still persists, is this still not efficient enough

---

## 2023-09-21 14:13:41 - issues channel

**liam**

It’s on purpose as 2.18 has a scary streaming change which I have been testing, it’s solid so will eventually upgrade flumine, lots of other PRs pending including a speed for flumine 

---

## 2023-09-21 13:04:09 - issues channel

**birchy**

[@U4H19D1D2](@U4H19D1D2) Quick question...bflw is on version 2.18.0 but flumine requires 2.17.3. Is that an oversight? I've only just noticed as I upgraded both and pip complained. Also, are there any plans to have a flumine[speed] version that uses bflw[speed] on non-windows platforms?

---

## 2023-09-20 20:37:27 - general channel

**liam**

Well it sounds like that is all very slow.



If you are recording data best practice is to record the raw streaming data for simulation after, are you not using the market recorder?

---

## 2023-09-20 18:32:23 - general channel

**Mona**

It is weird that I get high latency between current time and MarketBook publish time with my newly subscribed LIVE_APP_KEY.

---

## 2023-09-20 10:53:20 - random channel

**river_shah**

But essentially most infra is a solved problem for all but the lowest latency trades and should be delegated to vendors or open source libraries

---

## 2023-09-19 19:07:24 - random channel

**casper**

[@U4H19D1D2](@U4H19D1D2) Saw your comment on the PR (below). So this is getting scrapped? Also, any benefit in increasing the buffer size higher than 1024, have you tried different buffer sizes?



```Just did some real world testing on this, when subscribed to all racing markets and all data I see no improvement in latency comparing this branch to master with roughly only 4% of updates greater than 1024 bytes.



Interestingly when a large update comes through (&gt; 4000 bytes) master is quicker.```

---

## 2023-09-19 07:35:08 - general channel

**Mo**

[https://github.com/mberk/betfairutil/blob/18dcd187b5cab8fa4be25694fb64e8045bf3214e/betfairutil/__init__.py#L2178](https://github.com/mberk/betfairutil/blob/18dcd187b5cab8fa4be25694fb64e8045bf3214e/betfairutil/__init__.py#L2178)



&gt;  Working out the total volume traded on a market is surprisingly tricky given Betfair's shenanigans around the market

&gt;     closure. Specifically, the last few updates in the price stream result in data getting zeroed out which means if you

&gt;     were to just look at the last available market book it would look like the total volume traded was zero. In fact, it

&gt;     appears there is no consistency as to how many price stream updates are involved in this zeroing of data and so it's

&gt;     not as simple as having a rule such as "look at the second to last market book available".

&gt; 

&gt;     If memory usage is not an issue then the most robust method would be to read the entire set of market books into

&gt;     memory then iterate them in reverse order looking for the first market book that has a non-zero total volume traded.

&gt;     However, in many use cases memory usage is a significant concern. For example, if you want to process tens of

&gt;     thousands of markets and use parallel processing to speed this up then you end up needing to hold the entire set of

&gt;     market books for multiple markets in memory simultaneously and, depending on the number of cores your machine has

&gt;     and the number of parallel processes you use, it is easy to exhaust the total memory available.

&gt; 

&gt;     The solution presented here is to use a deque

&gt;     ([https://docs.python.org/3/library/collections.html#collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)). Think of this as a limited length list

&gt;     where when a new item is appended to the list, another item is removed for the start of the list. This is used when

&gt;     reading the prices file to leave us with the X last market books which can then be iterated in reverse order to find

&gt;     the last one which has a non-zero volume traded. Based on my own analysis of prices files I have settled on a

&gt;     default maximum length of the deque of 8 - i.e. at most this function will store 8 market books in memory at any one

&gt;     time. This is a trade-off between giving correct results and drastically cutting down on memory usage versus reading

&gt;     the entire set of market books into memory. If memory usage is not of concern to you then you can simply set the

&gt;     deque_len argument to None and the function will read the entire set of market books into memory ensuring

&gt;     correctness. If you observe any prices files where a deque of length 8 doesn't give correct results then please

&gt;     create a GitHub issue here: [https://github.com/mberk/betfairutil/issues](https://github.com/mberk/betfairutil/issues) so I can investigate.

---

## 2023-09-18 21:14:21 - random channel

**Ralegh**

Can’t speak from experience but I’d expect ms minimum, depending on server location, but you’re competing with people with microsecond or even nanosecond latency for higher tech exchanges 

---

## 2023-09-18 21:11:35 - random channel

**Jonjonjon**

How much latency would I expect trading via IBKR?

---

## 2023-09-18 13:11:15 - strategies channel

**liam**

You can also use it see if a drop in pnl over time is due to matching / model performance / market

---

## 2023-09-15 21:06:06 - random channel

**Pete**

what you should use for your socket receive buffer size is something that very much depends



with a low latency connection, fast processing of received messages and smallish message sizes from bf I would imagine you will quickly get diminishing returns from larger and larger buffers



this is also something you can test by recording how often the receive buffer you use is completely full

---

## 2023-09-15 14:18:39 - random channel

**liam**

[@U05PD1LRGGH](@U05PD1LRGGH) has a good point here in regards to waiting for the last two chars, thoughts?



```Increasing the buffer size will make it more likely that there's

less-than-one-full-buffers worth of data to read and increase the chance

that the last two characters read will be CRLF.



My gut feeling is that in all likelihood during real world usage the

original code will be faster on average as long as the buffer is set

appropriately, as on a low latency connection I believe a single message

will be read in totality much more often than not.



It will have the chance of spikes of latency for individual messages if

they ever get stuck in the buffer as described, but again my suspicion is

that this would actually be rare.



I think you should not merge this and revert the other commit.```

---

## 2023-09-14 17:36:56 - general channel

**birchy**

Interesting, because I've been using the same logging control for a couple of years but with separate bsp information. It's only this week that I updated flumine and then decided to update my logging control to include the bsp data. Based on what [@U4H19D1D2](@U4H19D1D2) said above, I'm planning to build 2 lookup dicts - one for my orders and one for BSP's and then amalgamate and write the CSV once I have both for each market. The only issue I can foresee is that I'll need to avoid a memory leak due to having BSP's in my lookup for markets on which I had no orders but I can probably manage that with a TTL or orders/market check.

---

## 2023-09-14 10:31:34 - random channel

**John Foley**

haha yep, fun little puzzle. i think you’re probably right as the scipy loggamma is written in cython. the speed increases may be cancelled out by trying to figure out how to fit it in though lol

---

## 2023-09-13 08:39:52 - random channel

**Unknown**

Just been playing around with [https://bloomberg.github.io/memray/index.html|memray](https://bloomberg.github.io/memray/index.html|memray) very neat for anyone who is looking for a memory profiler, good news is that bflw/flumine looks to be memory leak free still :smile:

---

## 2023-09-10 15:59:10 - random channel

**Joe**

I think it's configured to 50Hz, so 20ms, this a tradeoff between per order latency and batch sizing for efficient block (storage) persistence and packet utilization. It can certainly vary based on load, network events, storage events, etc. Betfair can also change it whenever they want to.

---

## 2023-09-09 13:28:31 - general channel

**Steve**

Memory charges on azure are also a bit steep. Will start shopping around for a better database too.

---

## 2023-09-08 21:33:43 - strategies channel

**Dave**

ahh okay, your 1045ms is total roundtrip, with 1000 being in-play delay, so 45ms includes: (book recv latency + trading logic latency + order submission latency + ack latency), so your actual reaction time to the market book tick may well be single digit ms (which is what I am measuring, i.e. how long between book publish time and triggering an order to Betfair).

---

## 2023-09-08 21:27:42 - strategies channel

**D C**

Well, I see that as just 45ms latency given 1000 for the inplay delay. I was actually pretty happy with my mean latency times which are around the 1150 mark until I saw your post. I suspect that most of this is down to the asynchronous component I use. I'm moving to a connection pool implementation so will be interesting to review things after that.

---

## 2023-09-08 20:55:40 - strategies channel

**Dave**

That's correct Liam, I am computing as (time.time()*1e3 - book.publish_time_epoch). I'll double check my clock and make sure it's not behind for some reason. I am sure I am trading on fewer events though which could explain it (and possibly simpler logic). Possible dumb question: I assume you have n flumine instances running a number of strategies each - even though your machine's CPU may not be saturated, have you looked at latency impact of just splitting one of those instances across two boxes (i.e. cheap way to truly parallelize with no GIL in the way)?

---

## 2023-09-08 09:58:32 - strategies channel

**D C**

Yeah I probably have lower latency in reality as I use an async component so I log transmission time as the time that the non-blocking write call returns - it doesn't mean that is when the write actually happened. Although I log the publish time I don't actually use that in the database but I can see that does reduce it further. Even with all that taken intou account though I am nowhere near single figure latencies.

---

## 2023-09-08 09:40:35 - strategies channel

**D C**

8-10 ms latency? Wow - I just looked at august and the lowest latency I had was 1045 milliseconds (inplay horses). However, I measure mine from time the order is created by a strategy, to the time that I receive the bet on the order stream. I place with the async flag and the lowest latency I have on the placement is 20ms. My SQL is quite basic and I am not familiar with how to extract the median.

---

## 2023-09-06 09:47:38 - general channel

**D C**

I hope you are right Michael. From memory, the white paper states a non-invasive credit check would be made on as little as a £150 loss over 24 hours or £1K across 30 days (might have those figures wrong I am going from memory).

I share your sentiment about not taking people's last penny but people with a problem (the people that these changes are supposed to protect) will still gamble. I say that as someone who was once very close to having a serious gambling problem, who even took out payday loans at times to bet, and was a cigarette paper's width from having to get an IVA due to using credit cards to gamble. Based on my own betting patterns I know for a fact that you can spot a certain type of problem gambler just from deposit + bet patterns. Bookies and casino's have known this for ages (if not they are criminally stupid) but were too greedy for too long. I still find it unbelievable that these morons at the GC think their proposed measure will do anything other than relocate the problem.

---

## 2023-09-05 21:12:23 - strategies channel

**Dave**

Does anyone measure their trading latency? If anyone is willing to share, I'm particularly interested in (order_submit_time - book_publish_time), separately for pre-play and in-play. :slightly_smiling_face:

---

## 2023-09-03 11:39:58 - strategies channel

**AndyL**

[@U05L8PZD2FM](@U05L8PZD2FM) yes, that's exactly the problem I was thinking about, trying to equate ML with a real world strategy, as you say it typically adapts to what us matched, and adverse selection is probably hard to model..?

I think I'll head down the optimization route, as i can see through my current backtesting workflow im probably not being very good at optimising 

Thanks

---

## 2023-09-01 17:46:10 - general channel

**George**

What is the best/fastest way to grab a snapshot of a market book at X minutes before the market start time?

Of course I could load the market in flumine and loop through the updates until I get to the desired timestamp, but that seems to be a relatively slow process.

Would it be a terrible idea just to use the BASIC data instead?

---

## 2023-08-31 11:07:57 - issues channel

**river_shah**

The network architecture of BF is not entirely well understood but if you queue too many packets due to your high bandwidth / low latency connection, reasonable chance packet drops occur and strange connection errors will pop up. I could be totally wrong on this, so please verify if indeed your connection matches said description.

---

## 2023-08-31 11:03:11 - issues channel

**river_shah**

George, I am just guessing but likely you are on an extremely high bandwidth, low latency connection into BF. Your last two errors seem to suggest this. I think packets are getting dropped before BF handshakes properly.

---

## 2023-08-25 14:29:53 - random channel

**D C**

Yes I can see the sense in that. It again leads to numerous questions. For foorball, the game is 90 minutes (give or take injury time). But how about a tennis match of indeterminate duration? Similarly, how about uniformity of model performance with respect to time? I guess I am not expecting any answers, but every time I try to analyse things in a statistically sound manner I am always just left scratching my head when it comes to inplay.



As you say Mo, one prediction per event makes everything more simple but in truth I don't know where to start when it comes to open ended IP stuff.

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

## 2023-08-23 21:49:00 - general channel

**Andrew**

With thanks once again to Liam, isn’t this what you’re looking for. Works for me. [https://betcode-org.github.io/flumine/performance/|https://betcode-org.github.io/flumine/performance/](https://betcode-org.github.io/flumine/performance/|https://betcode-org.github.io/flumine/performance/) I create a CSV output per market. Subsequently you can merge or leave as 1:1 for your market PRO stream files.

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

## 2023-08-22 18:05:04 - random channel

**Rishab**

You can look at Adjusted R sq. to find out if adding another feature actually improves the model performance or not

---

## 2023-08-20 15:07:00 - general channel

**Mo**

1. Give the list of files in the `market_filter` under the `markets` key

2. Yes it can read the raw data files but you probably need to patch `open` as described here: [https://betcode-org.github.io/flumine/performance/#file-location](https://betcode-org.github.io/flumine/performance/#file-location)

---

## 2023-08-18 17:57:49 - issues channel

**Derek C**

I am slowly migrating stuff over to Flumine (from BFLW-based approaches). One issue I seem to have is that even when my market_data_filter specifies ladder_levels=5, the market_book has the whole ladder.



eg when I create the strategy I pass the following:





```market_data_filter=streaming_market_data_filter(

            fields=[

                "EX_ALL_OFFERS",

                "EX_LTP",

                "EX_TRADED",

                "EX_TRADED_VOL",

                "EX_MARKET_DEF",

            ], 

            ladder_levels=5,

    ),```

Yet  in market_book.runners[0].ex.available_to_back there are over 30 entries. What am I missing?

---

## 2023-08-18 09:44:12 - issues channel

**Harry Corrigan**

Would like to avoid using list_market_book as it's slower &amp; also don't want to have to keep making requests for orders made outside of strategy

---

## 2023-08-17 16:29:19 - random channel

**foxwood**

Had to install rust from [https://rustup.rs/](https://rustup.rs/) which was new to me. Numbers matched exactly - several thousand calls - shin output used in other calcs - identical down to 14 decimal places ! It was using `_optimise_rust` when I stepped it but no idea of speed difference since just used the new one as was for an existing strategy that uses the current release - not time critical for me.

---

## 2023-08-14 16:52:33 - strategies channel

**R**

[@UBS7QANF3](@UBS7QANF3) can't say on speed, I know it leverages other libs for certain routines based in C so it's fast enough that I've never thought to profile it against scipy.



Thing for me was just more granular API on optimization problems.

---

## 2023-08-14 07:27:43 - random channel

**Mo**

I really don't think this is an area where you want to be relying on a 3rd party that doesn't understand your use case. It does seem strange to me that there isn't more out there regarding low latency HTTPS connection pools but I guess it's too niche/people are too protective of their own implementations. I have my own in C, originally built on top of libcurl but now using my own custom HTTPS client. Whether you need to do that or not depends on whether you really need what that offers you over the flumine implementation which, from a first glance at the code [@UUCD6P13J](@UUCD6P13J) shared, looks solid. Not that I would expect anything else!



I highly recommend when pushing requests to a pool like this that there is a check immediately before bet placement between the time the request was generated and the time now and discarding anything greater than a tight threshold. That would have avoided your previous problems but no doubt would not have been possible if using a 3rd party component that you have no internal access to

---

## 2023-08-13 16:52:19 - random channel

**D C**

There is no error. Just latency buildup. Writing further requests to this component just results in it queuing them until it can send

---

## 2023-08-13 16:45:11 - random channel

**D C**

Any obviously that bottleneck and latency would just get worse and worse and also apply to cancellations. That is what battered me - leaving the fruit to be picked off.

---

## 2023-08-13 16:43:02 - random channel

**D C**

17 second bet placement latency was the worst I saw. Cost me in the region of 20k I estimated

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

## 2023-08-11 23:49:00 - strategies channel

**Jonjonjon**

Numba definitely helps put money in my bank account and the 3.11 update was a huge performance boost.

---

## 2023-08-11 22:35:33 - issues channel

**Mo**

I believe this happens when the subscription message gets sent before Betfair is ready for it, which can happen if your latency to Betfair is particularly low



I do this, which is a bit of hack:



```betfair_stream._connect()

time.sleep(3)

betfair_stream.authenticate()

betfair_stream.subscribe_to_orders(order_filter=betfairlightweight.filters.streaming_order_filter(order_filter))```

---

## 2023-08-07 19:28:32 - general channel

**AI Trader**

Hi guys,

Has anyone tried different approaches to sending multiple orders to Betfair at once? I am currently doing that thorugh creating multiple threads to send all my orders. Sometimes more than 1,000 orders at the same time in the startup. I am creating these threads in python, and I have realized that the latency to spin up a thread is quite significant (could be as high as 30ms). When doing that for hundreads of orders, it becomes meaningful. How do you usually do that? Asyncio? Thanks

---

## 2023-08-07 19:02:50 - strategies channel

**foxwood**

Training per race would be slower but that is only while training - applying the model to live data would be no different. To add to the headache have a look at a regression model instead of classification - that should give you a score instead of a binary win/lose - effectively a probability.

---

## 2023-08-07 17:57:56 - strategies channel

**liam**

[@U02RN7YDRQ9](@U02RN7YDRQ9) would that not be mega slow?



I think the only thing I have achieved today is a headache, certainly fallen into the overfitting trap, thanks [@U01B8031PM1](@U01B8031PM1) for sharing `GroupTimeSeriesSplit` makes sense and works well.



I have a pipeline that is working well and likely something that I will share as its very cool to be able to create a model and then run it within a flumine simulation with a few lines.



Really starting to question the suitability of using ML at this stage, maybe its the classifiers I am using but they just want to overfit. A few could have predicted this but I am going to go back to the beginning with my model predictions and see if that can be improved using regression.

---

## 2023-08-07 09:25:56 - strategies channel

**Joe**

[@U4H19D1D2](@U4H19D1D2)ok so unlabeled unsupervised derivative free reinforcement learning with the goal of maximising profit or ROI. You need to get your data into a memory structure that can be executed at very high frequency then use a derivative free / metaheuristic search such as FF, PSO, etc. Your conditional betting logic would need to be rephrased to operate on the new memory model and you would need some type of environment that can minimally mimic the market if your logic takes actions based on its previous actions.

---

## 2023-08-05 21:56:35 - general channel

**Trex44**

What are the bariers do you think? I was looking into it recently and was surprised at how much easier and cheaper it is to get high quality data for Financial markets that for Betfair. Probably means there is less alpha from it but I was still surprised.



I have also wondered if there is a lot of stuff that gets left on the table by the big guys because it wouldn't have a meaningful impact on their overall performance. Kind of how value investing in smaller market cap companies is something (according to Joel Greenblat) that managers of smaller portfolio sizes can do well at because the bigger portfolios ignore the companies as they can't get enough money into them.

---

## 2023-08-04 19:52:28 - strategies channel

**liam**

[@U05LDB7TK8B](@U05LDB7TK8B) yeah expecting that to be a problem to solve, it’s a question that comes up a lot when it comes to latency / blocking the main queue etc. 

---

## 2023-08-04 18:33:27 - strategies channel

**Leo**

[@UPMUFSGCR](@UPMUFSGCR) it's generally faster and more memory efficient, so can iterate faster during development. Performance does vary from problem to problem, and lightgbm takes more tuning, there probably isn't much in it but lightgbm seems to come out on top more often than not and seems to be the new standard in kaggle competitions 

---

## 2023-08-04 13:40:56 - general channel

**Mo**

The data provider is [https://www.totalperformancedata.com/|https://www.totalperformancedata.com/](https://www.totalperformancedata.com/|https://www.totalperformancedata.com/)



Typically you would get access to this via Betfair



Historic data is available via an API but it is largely useless

---

## 2023-08-04 12:19:57 - general channel

**joe taylor**

Hi guys! I want to work on some strategy around inplay horse racing. Had a few queries around this: how can I get real-time race data like runner distance left in race or position of each runner in race/speed 2. historical data for each runner with different features-timeform type data &amp; inplay data(like speed in last x fraction of race left etc)

---

## 2023-08-03 15:38:57 - general channel

**liam**

So why is speed an issue? Just use a worker to disable the strategy when balance &lt; x however just fix the issue 

---

## 2023-08-03 15:18:40 - general channel

**George**

Has anyone ever coded a trading control to validate that the account has sufficient funds to place the bet?

It seems like the latency involved makes it impossible. `get_account_funds` takes a really long time to return.

Has anyone solved this problem?

---

## 2023-07-27 08:19:27 - general channel

**liam**

I have multiple instances of flumine running all communicating with it, sending/receiving market / order / trade / strategy / notes etc to it



I have a simple SPA running on top that allows me to view everything at a glance and update settings etc



I have a few lambda scripts that communicate on a daily basis to update / reconcile / check / record various things



Simulation scripts use it to pull in the relevant marketId's / data required (catalogues / sports data etc)



However when using juypter / pandas I communicate directly to the db with SQL as its quicker, whats your frustration? Speed?

---

## 2023-07-26 11:23:31 - strategies channel

**Mo**

1. What was your maximum loss prior to this?

2. Are you basing `I had a problem last night where someone had reverse engineered my strategies.` on any observations other than your realised performance?

3. What was your EV according to BSP?

---

## 2023-07-23 11:39:07 - general channel

**Guy Adini**

Do you know which datacenter offers the lowest latency when connecting to Betfair?

I'm already on AWS so London or Dublin make the most sense for me, but it would also be good to know in general - if I want the very lowest latency in the future, if there's some other recommended provider.

---

## 2023-07-15 19:55:27 - random channel

**jackofallspades**

Maybe paid "official" event data providers are behind it? I guess that there will be attempts of pitch-siding as long as affordable event data with minimum latency is not available.

---

## 2023-07-15 19:34:57 - random channel

**Alex**

My guess is: these events receive sponsorship money from (traditional) bookmakers. Bookmakers get adversely selected when people engage in courtside latency arb -&gt; bookmakers push to stop courtside betting.

---

## 2023-07-14 15:28:21 - strategies channel

**R**

I think this might also be helpful too in terms of parallelizing independent monte carlo runs



[https://betcode-org.github.io/flumine/performance/#multiprocessing](https://betcode-org.github.io/flumine/performance/#multiprocessing)

---

## 2023-07-14 11:00:36 - general channel

**Johnny**

Cool.  Guessing s3 performance is unaffected by number of objects in a bucket then... I currently have the same structure as Peter but all on HDD at home.  Are I/O charges a concern at all?

---

## 2023-07-14 07:22:52 - strategies channel

**Peter**

Stepping back, I use Monte Carlo simulation too, but (almost) always offline as part of my analysis to develop and evaluate strategies. I only have one strategy currently where it's integrated into the strategy itself. For that strategy, what's changing and warrants re-running the simulation is the state of the event itself, i.e. fundamental rather than market data. Updates to that are way slower than every 50 milliseconds. So I have a process that runs in parallel to my Flumine strategy to ingest external data about the state of the event, run the simulation and store the latest result, which can be read by my Flumine strategy as and when it needs it.



In my case it's an older home grown process (it's been around for a while). But Flumine provides [https://betcode-org.github.io/flumine/workers/|workers](https://betcode-org.github.io/flumine/workers/|workers) that are how I could do this job if I were writing this today. A worker runs in parallel to your Flumine strategy so (normally) won't slow it down (though if you have a single processor available to your Flumine instance it might). Thus you could run your simulations continuously in a worker function and, using the flumine object available to each worker, write the results back to your strategy or individual markets objects each time a simulation completes, from which your strategy can pick them up when processing market updates.

---

## 2023-07-13 17:27:56 - strategies channel

**Peter**

That's really not a surprise. It's not that Flumine is slow, it's that it's receiving and processing updates for every market to which you're subscribed as frequently as every 50 milliseconds, so there's really not enough space in there to run 10k sample monte carlo simulations as well.



If the simulations are important to you, you have three things you could do:

1. in your subscription request, ask for conflated data e.g. only receive the data every second, opening a bigger window into which to run your simulations

2. offload the simulations to a worker (to stop them blocking your main process) and write the results back to the relevant market.context for ingestion into market update processing

3. 1 and 2 above.

---

## 2023-07-12 17:43:15 - issues channel

**Peter**

Clearly something is going very wrong. the starting point would be to profile your code. See [https://betcode-org.github.io/flumine/performance/#strategy](https://betcode-org.github.io/flumine/performance/#strategy). Also are you experiencing any network issues at the location where you run your strategies?

---

## 2023-07-12 16:52:55 - issues channel

**Andrey Luiz Malheiros**

I seem to be having some latency issues. It was working fine until yesterday, but today it started consistently showing the following errors. Even if I terminate the execution of Flumine and start it again, the errors persist. I'll send the logs I'm receiving. These errors persist, and no orders are being placed, and the strategies are not being executed. Does anyone know how to resolve this or at least attempt to remedy it?

```[2023-07-12 14:20:07,894: INFO/ForkPoolWorker-2] Client update account details

[2023-07-12 14:21:07,795: INFO/ForkPoolWorker-2] Updated marketCatalogue for 1.215993597

[2023-07-12 14:21:18,819: INFO/ForkPoolWorker-2] Market 1.215993597 closed

[2023-07-12 14:21:42,401: WARNING/ForkPoolWorker-2] [MarketStream: 2001]: Latency high: 0.5233955383300781

[2023-07-12 14:53:35,502: WARNING/ForkPoolWorker-2] [MarketStream: 2001]: Latency high: 1505.3750047683716

[2023-07-12 15:30:03,086: WARNING/ForkPoolWorker-2] [MarketStream: 2001]: Latency high: 4085.18798494339```

---

## 2023-07-04 16:10:49 - strategies channel

**George**

if `process_market_book` can take up to 20ms, is that slow enough to cause 'problems'?

---

## 2023-07-04 14:09:31 - strategies channel

**R**

nice, thanks guys.  I'll dig into understanding the control classes now.  Slowly internalizing the philosophy of flumine.



much appreciated to you both!

---

## 2023-07-02 14:27:36 - issues channel

**Peter**

Problem doesn't need to be solved. This was more a test of my understanding - so many thanks for the confirmation.



My use case is a bit out there. The bottleneck is an external API call, currently called on every price update, but I can push that to a worker and keep track of the results, and only call it within the custom event to validate freshness if a potential bet is to be placed, which is rare compared to price updates.



I can also reduce the frequency with which price updates are evaluated by reducing the ladder size to ignore those that aren't relevant or by conflating changes. So I expect to be able to achieve performance gains of order of magnitude 1000s with just a few tweaks to the data structure and process flow - no need to consider messing with Flumine's simplicity.

---

## 2023-07-02 11:04:05 - issues channel

**Peter**

Probably a question(s) for [@U4H19D1D2](@U4H19D1D2), but if anybody else knows I'd love to hear from your.



I'm not hugely familiar with event handling in Python, but it looks to me as though Flumine has a single FIFO queue handled in the main thread. If so, I would speculate that this means that processing heavy custom events would be blocking and a source of latency.



Is there anything in Flumine that would allow custom events to be offloaded to a queue on a different thread, or better a different processor? Or would this basically require building a parallel event handling infrastructure in my strategy runner?

---

## 2023-06-28 17:34:15 - general channel

**George**

Now I think I understand workers and my code is working - thanks very much. But I still have an issue.

Whilst the simulation is of course much faster than "real-time", there is no equivalent way to speed up the worker code which is inherently slow (e.g. calls to an external database or API).

This means that the worker output - which writes to `market.context` - is totally misaligned (in terms of 'clock') with the market-book. Isn't this a huge issue for some users?

Now I am lucky, because my worker output does not change frequently over time. However, I do need the worker to execute its "first pass" before the first `process_market_book`  is called. I can, of course, instruct my worker to start 10 "minutes" before `check_market_book` returns True, but 10 simulation-minutes is much quicker than the time it takes for the worker output to be generated, so it solves the issue in live trading but not in simulation.

I think that I can workaround this issue by checking the `market.context` during the `check_market_book`. However, it is not ideal, because `check_market_book` will return False in the simulation, whereas, in real life it would have returned True.

Depending on how slow the worker is, most of the simulated trading window could have been missed, just waiting for the worker's first pass!

I imagine this is not a new question - what is the standard answer to dealing with this?

---

## 2023-06-26 12:09:03 - general channel

**Jorge**

I see a lot of [https://github.com/betcode-org/flumine/blob/master/flumine/baseflumine.py#L140|"High latency between current time and MarketBook publish time"](https://github.com/betcode-org/flumine/blob/master/flumine/baseflumine.py#L140|"High latency between current time and MarketBook publish time") messages but very few [https://github.com/betcode-org/betfair/blob/master/betfairlightweight/streaming/stream.py#L69|"Latency high"](https://github.com/betcode-org/betfair/blob/master/betfairlightweight/streaming/stream.py#L69|"Latency high") ones. What is the difference between the 2 of them?

---

## 2023-06-26 10:14:09 - general channel

**Jorge**

I guess my model is too slow and when there are many live games it takes too long to run process_market_book. For sure increasing the number of CPUs and optimizing the model would help me. I'd just like to add another safety check in case this ever happens again

---

## 2023-06-26 10:04:01 - general channel

**Jorge**

With high Latency I mean I see "High latency between current time and MarketBook publish time" in the logs. In these cases [https://github.com/betcode-org/flumine/blob/master/flumine/markets/blotter.py#L185|market.blotter.get_exposures(self, lookup=selection_lookup)](https://github.com/betcode-org/flumine/blob/master/flumine/markets/blotter.py#L185|market.blotter.get_exposures(self, lookup=selection_lookup)) returns a wrong exposure, my guess is that it does not consider the order because the EXECUTION_COMPLETE message does not arrive on time

---

## 2023-06-26 09:24:50 - general channel

**Jorge**

Hi, I'm trying to understand how would my flumine Strategy work in case the latency suddenly is very high. I am placing an order using [https://github.com/betcode-org/flumine/blob/master/flumine/markets/market.py#L79|place_order](https://github.com/betcode-org/flumine/blob/master/flumine/markets/market.py#L79|place_order) and then checking the selection's exposure using [https://github.com/betcode-org/flumine/blob/master/flumine/markets/blotter.py#L185|market.blotter.get_exposures(self, lookup=selection_lookup)](https://github.com/betcode-org/flumine/blob/master/flumine/markets/blotter.py#L185|market.blotter.get_exposures(self, lookup=selection_lookup)). Could it happen that the order gets matched and goes to EXECUTION_COMPLETE, but being the latency very high, the selection's exposure doesn't consider this order? In this case, my strategy would think this order never existed and place it again

---

## 2023-06-24 07:24:44 - random channel

**James**

Multiprocessing doesn’t share memory by default though.  so you should use shared memory if you don’t want to repeat work for something you need in all processes.

[https://docs.python.org/3/library/multiprocessing.shared_memory.html](https://docs.python.org/3/library/multiprocessing.shared_memory.html)

---

## 2023-06-24 03:00:33 - general channel

**Andy**

Anyone running their code in VSC getting these oom errors and VSC crashing periodically? The program doesn’t seem to be using large amounts of memory if I check task manager and the json files I’m reading and writing to aren’t more than a few mb in size. Have tried the google suggestions but hasn’t improved things - [https://stackoverflow.com/questions/71614897/vscode-crashed-reason-oom-code-536870904#:~:text=If%20you%20are%20using%20VSCode,Optimizations%22%20and%20mark%20the%20checkbox.&amp;text=It's%20easy%20than%20you%20think,will%20see%20that%20it%20works|https://stackoverflow.com/questions/71614897/vscode-crashed-reason-oom-code-536870904#:~:text=If%20you%20are%20using%20VSCode,Optimizations%22%20and%20mark%20the%20checkbox.&amp;text=It's%20easy%20than%20you%20think,will%20see%20that%20it%20works](https://stackoverflow.com/questions/71614897/vscode-crashed-reason-oom-code-536870904#:~:text=If%20you%20are%20using%20VSCode,Optimizations%22%20and%20mark%20the%20checkbox.&amp;text=It's%20easy%20than%20you%20think,will%20see%20that%20it%20works|https://stackoverflow.com/questions/71614897/vscode-crashed-reason-oom-code-536870904#:~:text=If%20you%20are%20using%20VSCode,Optimizations%22%20and%20mark%20the%20checkbox.&amp;text=It's%20easy%20than%20you%20think,will%20see%20that%20it%20works).

---

## 2023-06-23 22:41:40 - random channel

**Jonjonjon**

I just tested it. Removing the Simulation middleware improves performance by about 25%.

---

## 2023-06-23 22:16:41 - random channel

**Mo**

I think you will find you were receiving 10 updates a second as usual but that the speed was constant for 1 second’s worth of updates. When I first started using the feed I observed the speed only updated once a second. This is because the speed was not being calculated from changes in location but comes directly from the GPS chip based on the Doppler Effect. 



I don’t pay close attention to the speed field so didn’t realise it had changed to a higher frequency which you seem to be implying it did. My first question is whether it is still coming direct from the chip or whether it is now being based on changes in location

---

## 2023-06-23 20:44:44 - strategies channel

**Jonjonjon**

I prefer market_book.publish_time. the above will behave differently based on your latency

---

## 2023-06-21 21:36:50 - random channel

**AndyL**

in fact given this month's performance, I think i'm an omeaba !

---

## 2023-06-21 12:21:41 - general channel

**casper**

Hey [@U4H19D1D2](@U4H19D1D2)!



I think in the latest betfairlightweight release (2.17.2) you haven’t actually upgraded orjson to 3.8.7 as per release notes? It’s still at 3.8.5?



[https://github.com/betcode-org/betfair/blob/master/requirements-speed.txt#L2](https://github.com/betcode-org/betfair/blob/master/requirements-speed.txt#L2)

[https://github.com/betcode-org/betfair/pull/519/files](https://github.com/betcode-org/betfair/pull/519/files)



The latest orjson version is now 3.9.1, maybe worth bumping to that? They (orjson) seem to have been doing loads of minor releases recently.

---

## 2023-06-21 10:49:17 - random channel

**Jonjonjon**

If removing "framework._market_middleware", what sort of performance benefits do people see?

---

## 2023-06-21 09:13:19 - strategies channel

**Mo**

By performance you mean absolute returns?

---

## 2023-06-21 09:12:31 - strategies channel

**Jonjonjon**

Performance doesn't seem to improve if I increase the size.

---

## 2023-06-21 09:06:32 - strategies channel

**Jonjonjon**

I'm happy with the performance at £2 stakes. No need to reduce my size.

---

## 2023-06-21 08:35:14 - random channel

**Mo**

I don't use flumine but you need to patch `open` with `smart_open.open`: [https://betcode-org.github.io/flumine/performance/#file-location](https://betcode-org.github.io/flumine/performance/#file-location)

---

## 2023-06-20 21:20:21 - issues channel

**Jeff Waters**

Hi



I've been back testing a system that involves placing a lot of bets. I kept getting an 'ERROR - Transaction limit reached' message, which I presume is meant to prevent users from going over the 5000 (?) bets you can place per hour before you start paying a charge. However, it looks like it continues to apply when processing market activity that took place over an hour after the 5000 limit would have been hit.



Is there anything I can do to get around this, please, as the constant console output slows things down?

---

## 2023-06-20 12:09:52 - general channel

**George**

Is it a bad idea to put a 'slow' (maybe a few seconds) function call inside `process_market_book`?  I imagine that would cause a lot of problems when (potentially) betting on large numbers of markets?

---

## 2023-06-20 11:41:09 - general channel

**D C**

Yeah I saw that [@UQL0QDEKA](@UQL0QDEKA) although it was mostly for pennies up in the top end prices. Does anyone know if bookies apply a latency on their odds for non-logged in accounts to deter scraping? If so probably no point me watching at all.

---

## 2023-06-16 07:50:32 - issues channel

**liam**

Did you remove all the controls that flumine has in place to stop this?



And to answer point 2 I imagine the program exited due to memory leak / CPU so the termination function could never run.

---

## 2023-06-13 18:20:33 - strategies channel

**liam**

flumine deals with it as gracefully as it can, have a look at the [https://github.com/betcode-org/flumine/blob/master/flumine/streams/marketstream.py|marketstream](https://github.com/betcode-org/flumine/blob/master/flumine/streams/marketstream.py|marketstream) code to see how it retries to connect with exponential backoff. I think there has only been one occasion in the past year where I have had to restart but I think we have fixed this particular issue (memory leak)

---

## 2023-06-11 10:22:34 - random channel

**Mo**

[@U01PJ5YMFBJ](@U01PJ5YMFBJ) if you want some insight into the practicalities of TPD on course activities, this is a fun read: [https://www.totalperformancedata.com/2022-5-31-a-day-in-the-life-of-a-tpd-operator/](https://www.totalperformancedata.com/2022-5-31-a-day-in-the-life-of-a-tpd-operator/)

---

## 2023-06-11 09:56:09 - random channel

**foxwood**

That's true for traditional disk drives where lots of small files are sprinkled around the drive at random. The needed head movement and rotational latency wastes significant amounts of time. With ssds' that problem goes away. The remaining issue is that of finding the true file address which means searching directory sectors. While ssd's still have to do that, the time taken and access speed to the directory sectors is very fast. I organize my files in folders by event type and date (eg "HR230611" for today's horses) which helps minimize the search time when the strategy is given a long list of files to work through for backtest.

---

## 2023-06-10 20:00:02 - random channel

**Jonjonjon**

Thanks everyone for sharing. I use zip files as I read somewhere that having lots of small files can cause performance issues on the disk

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

## 2023-06-07 12:44:11 - strategies channel

**Aaron Smith**

[@UBS7QANF3](@UBS7QANF3) you are correct that assuming that there is no systematic bias in the bet selection of any strategy would be a questionable claim to make without any further proof given. However, i didnt claim this was true for any of my strategies. I merely constructed such a strategy for the purpose of showing an example of an EV calculation that may (for this particular strategy) be accurate in the sense that pnl/EV would eventually converge towards 1 over time, but would still be inaccurate in the sense that this could be a very slow process and there are obviously better ways to calculate an EV.

---

## 2023-06-06 14:21:37 - strategies channel

**D C**

Surely you're never going to be able to identify inaccurate prices on individual case basis. You can only really assess performance of probability estimates on a large scale (regardless of whether BSP / odds at off etc). We can get away with it on theoretical idealisation of things like fair coins/dice etc, but you can surely never know that an even money closing price favourite should really have gone off at 10/11 ??? And then you've got stuff like race/match fixing and inside info to contend with. Surely its all a lost cause trying to work out when a particilar off price is "bad" ?

---

## 2023-06-06 13:58:00 - strategies channel

**Aaron Smith**

I think we maybe need to differentiate between 2 ways an EV can be inaccurate:

1. pnl/EV converges towards 1 over time, but slowly.

2. pnl/EV does not converge towards 1

For example, if i have a strategy that is equally likely to back or lay a runner, independent on the odds, then i could calculate an EV by just comparing the odds i took to 1/n (basically using 1/n where n = number of runners instead of some kind of final price). This EV would obviously be super inaccurate, but still correct in the sense that pnl/EV would over time still converge to 1, just super slowly.



I m more interested in case 2. Suppose we take final prices (at schedueled off) to calc our EV, can you come up with any reason pnl/EV would not converge towards 1 over time? Or have you had strategies that showed amazing EV (calculated from actual bets, not simulation), but you disregarded them based on actual pnl? If so, did you find any reason on how the EV came to be inflated?

---

## 2023-06-06 13:27:42 - random channel

**Jonjonjon**

I would have thought it would take longer too, as it will need to create new processes and restart Flumine etc... I would also expect it to use  less memory, which may or may not be a concern (I was too tight and only bought 32gb ram).

---

## 2023-06-05 23:01:54 - random channel

**Jonjonjon**

At the moment I only do 1 market at a time, using the multiprocessing module to run lots in parallel.

I've noticed that my NVME (Samsung EVO 970 plus) is getting a bit hot, at 70C, and am asking the question to see if reorganising things can help to reduce the strain on the device.

This evening, I've tried running multiple backtests per worker, instead of creating a new worker per backtest. That has increased the speed of the backtests at the cost of increase my drive temp.

---

## 2023-06-02 18:06:06 - random channel

**liam**

Is it that slow? I use RDS on AWS all day

---

## 2023-06-01 16:13:41 - general channel

**Derek C**

[@U03N4QBJ0TV](@U03N4QBJ0TV) I do a lot of the same thing, except that I use Athena to populate pandas DataFrames in SageMaker from my files in S3. The benefit is that I can filter the rows and the columns that will be brought into memory in the SQL logic, and also sometimes do grouping to further reduce the size of the dataset that lands in Pandas. The benefit of Athena is that you don't have to actually migrate anything into a SQL database - you just tell it where the csv files are in S3 and they 'become' the database that you can then query. The awswrangler library makes it easy to integrate Pandas and Athena/S3 if you're not already using that.

---

## 2023-06-01 10:47:17 - general channel

**Trex44**

[@U04NWADNCFR](@U04NWADNCFR) Thanks very much for the answer. I currently use csv's stored in S3 then load them into a Jupyter note book in AWS Sagemaker and use Pandas to explore them. I have considered moving everything over to an SQL database but I like the graphical output I can get from using Pandas. Loading into the notebook takes an age and the kernel dies if I try to manipulate large data sets as the instance doesn't have the memory needed.

---

## 2023-05-30 19:55:12 - strategies channel

**AndyL**

So let me see, that's telling me the most common latency in executing a cancel is about 50ms ?

---

## 2023-05-27 16:17:01 - general channel

**Mo**

I’m curious what latency edge you’re hoping to get by asking this in a public forum rather than working it out yourself?

---

## 2023-05-26 19:12:44 - general channel

**AI Trader**

Hi guys,

What is the physical location of betfair servers? Asking because I want to run my strategies in the same location for lower latency. Is it London?

---

## 2023-05-25 09:36:58 - general channel

**Andy B**

I think I am going to have to reconsider this as I keep running into memory issues, despite having more than enough available memory.  Thanks for your help [@U4H19D1D2](@U4H19D1D2)

---

## 2023-05-25 08:24:00 - general channel

**liam**

Not sure how keras/h5 works but to start with I imagine loading the model is slow and is shared so could be done in `Strategy.add`



```def add(self):

    self.model = tf.keras.models.load_model(ModelName) ```

---

## 2023-05-25 07:57:37 - general channel

**Andy B**

I think that I am accessing the keras model to make predictions too fast when back testing against the market stream:

2023-05-25 16:21:56,369:CRITICAL:Unknown error bad allocation in process_market_book (1.212040559)

Traceback (most recent call last):

  File "C:\Python\lib\site-packages\flumine\utils.py", line 239, in call_strategy_error_handling

    return func(market, market_book)

  File "C:\Python\Scripts\flumine\FlumineSims.py", line 228, in process_market_book

    ModelName = tf.keras.models.load_model(ModelName)

  File "C:\Python\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler

    raise e.with_traceback(filtered_tb) from None

  File "C:\Python\lib\site-packages\h5py\_hl\files.py", line 533, in __init__

    fid = make_fid(name, mode, userblock_size, fapl, fcpl, swmr=swmr)

  File "C:\Python\lib\site-packages\h5py\_hl\files.py", line 226, in make_fid

    fid = h5f.open(name, flags, fapl=fapl)

  File "h5py\_objects.pyx", line 54, in h5py._objects.with_phil.wrapper

  File "h5py\_objects.pyx", line 55, in h5py._objects.with_phil.wrapper

  File "h5py\h5f.pyx", line 106, in h5py.h5f.open

  File "h5py\h5fd.pyx", line 155, in h5py.h5fd.H5FD_fileobj_get_eof

  File "h5py\h5fd.pyx", line 155, in h5py.h5fd.H5FD_fileobj_get_eof

MemoryError: bad allocation



That makes sense if it is multi-processing and trying to open it n number of times I guess, but I am not sure if there is a way to do this without slowing down the stream.  Is there a better way to do this?

---

## 2023-05-23 12:09:19 - strategies channel

**river_shah**

Sorry if this is a digression and over engineered for your use case but as you say "best", the answer is in mean variance optimization. The mathematically grounded way is that you come up with strategy expectations of returns and covariances and then blend all individual strategies into a meta strategy and trade that. The meta strategy assigns positions limits to ensure you don't blow through market capacity.

---

## 2023-05-23 08:35:36 - general channel

**Jonjonjon**

Suppose I am running 10,000 backtests.

I want to store the results.

I currently store the results as gzipped JSON, one per market. But then I end up with 10,000 files.

I've tried writing to sqlite instead, but that uses a lot of disk space.

I'm thinking of trying to write all results to a single zipped test file. But I've read that most libraries such as gzip will give poor performance if write to it incrementally. What else should I try?

---

## 2023-05-17 02:27:32 - strategies channel

**Alex**

It also depends on the number of bets placed, i.e. are you closing out bets half way through the race, then placing new bets? With 1000 datapoints your estimated strategy performance will have larger error than with 10000. Overfitting might be an issued based on how many parameters your model has (you'll likely be fine if you just have a few). You can try to bootstrap standard errors of your strategy to get an idea of how significant your results are.

---

## 2023-05-10 08:50:45 - random channel

**Newbie99**

Its funny, but I wrote these functions, probably 2, maybe 3 years ago now (albeit they have grown into very slow moving monsters over time)! Back then they seemed to make sense!!!



I think the bulk of the issue is the sheer inefficiency of these two, as they get called a lot as part of my order validation (or cancellation) process:



```def check_race_type_by_country(race_type, market_name, event_type_id, country_dict):



    race_type = return_race_type(race_type, market_name, event_type_id)



    maiden = True if 'Mdn' in market_name else False



    if country_dict != False and isinstance(country_dict, dict):

        price = False

        # If a dict is in the config, it will match by country and race type

        maiden_list = [v for k,v in country_dict.items() if race_type == k]

        if len(maiden_list) &gt; 0:

            if isinstance(maiden_list[0], list):

                for m in maiden_list[0]:

                    if 'Mdn' in m.keys() and maiden is True:

                        price = m['Mdn']

                    else:

                        if 'default' in m.keys():

                            price = m['default']

            else:

                price = maiden_list[0]



        else:

            if 'default' in country_dict.keys():

                if 'odds' not in country_dict.keys() and 'runners' not in country_dict.keys():

                    maiden_list = country_dict['default']

                    if isinstance(maiden_list, list):

                        for m in maiden_list:

                            if 'Mdn' in m.keys() and maiden is True:

                                price = m['Mdn']

                            else:

                                if 'default' in m.keys():

                                    price = m['default']

                    else:

                        price = maiden_list

                else:

                    price = country_dict

    else:

        # If a single price (rather than a dict) is in the config, then it will set this for all valid markets

        if isinstance(country_dict, float) or isinstance(country_dict, int):

            price = country_dict

        else:

            price = False

    return price



def true_or_false(setting, country_code=False, market_id=False, market_type=False):

    if not isinstance(setting, list):

        if setting == 'True':

            return True

        elif setting == 'False':

            return False

        else:

            return setting

    else:

        if country_code is False or country_code is None or country_code == 'False':

            if setting == 'True' or setting is True:

                return True

            elif setting == 'False' or setting is False:

                return False

            else:

                if market_id is False:

                    if isinstance(setting, list):

                        default = [s for s in setting if isinstance(s, dict) and 'default' in s.keys()]

                        if len(default) &gt; 0:

                            if market_type is False:

                                return default[0]['default']

                            else:

                                market_type_benchmark = [s for s in setting if isinstance(s, dict) and market_type in s.keys()]

                                if len(market_type_benchmark) &gt; 0:

                                    return market_type_benchmark[0][market_type]

                                else:

                                    return default[0]['default']

                        else:

                            return setting

                    else:

                        return setting

                else:

                    for s in setting:

                        if market_id in s.keys():

                            if s[market_id] == 'True':

                                return True

                            elif s[market_id] == 'False':

                                return False

                            else:

                                return s[market_id]

                        else:

                            default = [s for s in setting if 'default' in s.keys()]

                            if len(default) &gt; 0:

                                if market_type is False:

                                    return default[0]['default']

                                else:

                                    market_type_benchmark = [s for s in setting if

                                                             isinstance(s, dict) and market_type in s.keys()]

                                    if len(market_type_benchmark) &gt; 0:

                                        return market_type_benchmark[0][market_type]

                                    else:

                                        return default[0]['default']

                            else:

                                return False

                    else:

                        default = [s for s in setting if 'default' in s.keys()]

                        if len(default) &gt; 0:

                            if market_type is False:

                                return default[0]['default']

                            else:

                                market_type_benchmark = [s for s in setting if

                                                         isinstance(s, dict) and market_type in s.keys()]

                                if len(market_type_benchmark) &gt; 0:

                                    return market_type_benchmark[0][market_type]

                                else:

                                    return default[0]['default']

                        else:

                            return False

        else:

            for s in setting:

                if isinstance(s, dict):

                    if country_code in s.keys():

                        if s[country_code] == 'True':

                            return True

                        elif s[country_code] == 'False':

                            return False

                        else:

                            if isinstance(s[country_code], dict):

                                if market_type in s[country_code].keys():

                                    return s[country_code][market_type]

                                else:

                                    if 'default' in s[country_code].keys():

                                        return s[country_code]['default']

                                    else:

                                        return False

                            else:

                                return s[country_code]

                    else:

                        if market_id is False:

                            default = [s for s in setting if 'default' in s.keys()]

                            if len(default) &gt; 0:

                                if market_type is False:

                                    return default[0]['default']

                                else:

                                    market_type_benchmark = [s for s in setting if

                                                             isinstance(s, dict) and market_type in s.keys()]

                                    if len(market_type_benchmark) &gt; 0:

                                        return market_type_benchmark[0][market_type]

                                    else:

                                        return default[0]['default']

                            else:

                                return setting

                        else:

                            if market_id in s.keys():

                                if s[market_id] == 'True':

                                    return True

                                elif s[market_id] == 'False':

                                    return False

                                else:

                                    return s[market_id]

            else:

                default = [s for s in setting if isinstance(s, dict) and 'default' in s.keys()]

                if len(default) &gt; 0:

                    if market_type is False:

                        return default[0]['default']

                    else:

                        market_type_benchmark = [s for s in setting if

                                                 isinstance(s, dict) and market_type in s.keys()]

                        if len(market_type_benchmark) &gt; 0:

                            return market_type_benchmark[0][market_type]

                        else:

                            return default[0]['default']

                else:

                    if isinstance(setting, list):

                        return setting

                    else:

                        return False```

setting in the above refers to a dict, on startup I open a json file which contains various parameters.



An example would be something like this:



```    {

        "event_type_ids": [

            7

        ],

        "strategy_name": "strategy_xyz",

        "country_codes": false,

        "market_types": [

            "WIN"

        ],

        "execution_market_types": [

            "WIN"

        ],

        "pre_event_order_window": [

            {

                "GB": [

                    {

                        "start": 3600,

                        "duration": false

                    }

                ],

                "IE": [

                    {

                        "start": 3600,

                        "duration": false

                    }

                ],

                "US": [

                    {

                        "start": 3600,

                        "duration": false

                    }

                ],

                "FR": [

                    {

                        "start": 3600,

                        "duration": false

                    }

                ],

                "AU": [

                    {

                        "start": 3600,

                        "duration": false

                    }

                ]

            }

        ]}```



---

## 2023-05-10 07:48:20 - random channel

**liam**

The best way to speed up python is to not run python, so anything you can do to not call code if not required is your best option first

---

## 2023-05-09 13:19:49 - random channel

**Newbie99**

I've recently switched to a new MacBook pro, from an old windows machine and as I knew performance was rubbish on that, I didn't worry too much, just left things processing overnight etc. However with an M2 Max I was expecting super fast backtesting, but compared to the results people post on here I seem to be way behind (e.g. 16k pre-race horse racing markets, 1 hour before the off takes circa 3 hours).



My code is as follows:

```def start_backtest_a(chunked_markets, max_workers, profit_sum, in_play, seconds_to_start, event_processing,

                    strategy_names, match_all, middleware):



    _process_jobs = []

    with futures.ProcessPoolExecutor(max_workers=max_workers) as p:

        for m in chunked_markets:

            _process_jobs.append(

                p.submit(startup,

                         profit_sum=profit_sum,

                         in_play=in_play,

                         seconds_to_start=seconds_to_start,

                         event_processing=event_processing,

                         markets=m,

                         strategy_names=strategy_names,

                         match_all=match_all,

                         middleware=middleware

                )

            )

        for i, job in enumerate(futures.as_completed(_process_jobs)):

            try:

                mini_output_list = job.result()  # wait for result

                output_list.extend(mini_output_list)

                progress = len(m) * i+1

                time_taken_seconds = (datetime.datetime.utcnow() - sim_start_time).total_seconds()

                time_taken_minutes = time_taken_seconds / 60

                percentage = progress / total_markets

                time_taken = time_taken_minutes if time_taken_minutes &gt; 2 else time_taken_seconds

                time_remaining = (time_taken / percentage) - time_taken

                time_measure = 'minutes' if time_taken_minutes &gt; 2 else 'seconds'

                print(f'Currently on market {progress} / {percentage*100:.2f}% of {total_markets}, '

                      f'time taken so far is {time_taken:.2f} {time_measure}, estimated time remaining is {time_remaining:.2f} {time_measure}, ')

            except Exception as e:

                print(f'Exception {e}.')

        return output_list```

With startup being as follows:



```def startup(markets, profit_sum, in_play, seconds_to_start, event_processing, strategy_names, match_all, middleware=False):

    logger = logging.getLogger()



    custom_format = "%(asctime) %(levelname) %(message)"

    log_handler = logging.StreamHandler()

    formatter = jsonlogger.JsonFormatter(custom_format)

    formatter.converter = time.gmtime

    log_handler.setFormatter(formatter)

    logger.addHandler(log_handler)

    logger.setLevel(logging.CRITICAL)  # Set to logging.CRITICAL to speed up simulation



    start_time = get_utc_time()



    # Gets a list of strategy settings

    settings = [setting for setting in rc if setting['on'] is True and setting['strategy_name'] in strategy_names]



    client = clients.SimulatedClient(simulated_full_match=match_all)



    framework = FlumineSimulation(client=client)



    # with mock_patch("builtins.open", smart_open.open): # Commented out as files will be unzipped prior to running

    for s in settings:

        max_selection_exposure = s['max_selection_exposure'] if true_or_false(s['max_selection_exposure']) != False else None

        include_virtual_prices = "EX_BEST_OFFERS_DISP" if true_or_false(

            s['include_virtual_prices']) is not False else "EX_ALL_OFFERS"

        if s['strategy_type'] == 'simple':



            strategy = betting_strategy(start_time=start_time, settings=s, paper=client.paper_trade,

                                        market_filter=create_market_filter(markets, in_play, seconds_to_start, event_processing),

            market_data_filter=streaming_market_data_filter(

            fields=[

                include_virtual_prices,

                "EX_TRADED",

                "EX_TRADED_VOL",

                "EX_LTP",

                "EX_MARKET_DEF",

                "SP_TRADED",

                "SP_PROJECTED",

            ]

            ),

            streaming_timeout=2,

            max_selection_exposure=max_selection_exposure,

            max_order_exposure=s['max_order_exposure'],

            conflate_ms=s['conflate'],

            name=s['strategy_name'],



            )



            framework.add_strategy(strategy)



    ''' Add in Middleware to get Market Catalogue '''

    framework.add_market_middleware(MarketCatalogueMiddleware())



    if middleware is not False:

        framework.add_market_middleware(middleware)



    framework.add_market_middleware(RiskMiddleware(framework))



    framework.run()```

I presume that calling the middleware could be an issue and also potentially my structure is wrong (i.e. in terms of trying to multiprocess at the wrong point).



I did try to get chatGPT to re-write things and it tried to use:



_with mp.get_context('spawn').Pool(max_workers) as pool:_ 



However I couldn't get it working (i.e. it never actually ran the framework, so I couldn't work out how to proceed).



Appreciate this is a bit of a '_how long is a piece of string_' situation, but is there a fairly generic approach to using multi processing with middleware that perhaps I could use as a template?

---

## 2023-05-09 11:43:39 - general channel

**Beeblebrox**

This is it. If I could easily replicate it I'd log something, but unfortunately that's not the case.



I suspect it is something to do with latency as it only tends to happens when there are lots of markets being streamed (~5000) at the weekend. In my logs though there are only ever latency peaks of ~1 second which quickly fall away (within ~.01 seconds).



Like I say though, if I stop and restart it, it then works fine for the rest of the weekend, so no idea what's going on.

---

## 2023-05-09 10:48:11 - general channel

**liam**

Without some code to replicate not sure what is going on here, I imagine some [user] code is causing the latency to get high and then cause issues rather than what is described

---

## 2023-05-08 11:50:10 - general channel

**Jorge**

Hey guys. Using flumine my Strategy behaves strangely when Latency is high. Could it happen that my [https://github.com/betcode-org/flumine/blob/master/flumine/markets/blotter.py#L118|market.blotter.live_orders](https://github.com/betcode-org/flumine/blob/master/flumine/markets/blotter.py#L118|market.blotter.live_orders) gets updated but my [https://github.com/betcode-org/flumine/blob/master/flumine/markets/blotter.py#L74|market.blotter.strategy_selection_orders](https://github.com/betcode-org/flumine/blob/master/flumine/markets/blotter.py#L74|market.blotter.strategy_selection_orders) does not get updated? For example, in the event of an order filled, I'm thinking [https://github.com/betcode-org/flumine/blob/master/flumine/markets/blotter.py#L118|market.blotter.live_orders](https://github.com/betcode-org/flumine/blob/master/flumine/markets/blotter.py#L118|market.blotter.live_orders) could change but [https://github.com/betcode-org/flumine/blob/master/flumine/markets/blotter.py#L74|market.blotter.strategy_selection_orders](https://github.com/betcode-org/flumine/blob/master/flumine/markets/blotter.py#L74|market.blotter.strategy_selection_orders) doesn't and therefore my exposure calculation is wrong.

---

## 2023-05-07 23:15:39 - general channel

**Jeff Waters**

I've put some code in process_market_book to log the WOM when my orders are at least partially matched:



```for order in market.blotter.live_orders:

    runner = Repository().get_runner_from_order(order)

    if order.size_matched &gt; 0 and not hasattr(order, "wom"):

        order.wom = Wom().get_wom_for_runner(runner)```

When I print my results to a spreadsheet, I use:



```wom = order.wom if hasattr(order, "wom") else 0```

When I print the results, for orders that were matched, some of my entries are zero and some are the wom. I don't understand why it's sometimes the case that the order object is given a 'wom' attribute when money has been matched, and sometimes it isn't?



I wondered whether it might be due to race conditions, as I'm using multi-processing. I'm aware that, with multi-processing, each process has its own memory space, but Chat GPT assures me that race conditions can nevertheless happen (and yes, I'm aware that GPT isn't an authoritative source! :smile:). Anyway, I applied a lock to everything in process_market_book, but that didn't fix the issue.



Any suggestions would be appreciated.



Thanks



Jeff

---

## 2023-05-06 02:58:00 - general channel

**Tom**

I am no expert on this at all - but I saw this recently, which looks pretty interesting in regards to speed of Python [https://www.theregister.com/2023/05/05/modular_struts_its_mojo_a/](https://www.theregister.com/2023/05/05/modular_struts_its_mojo_a/)

---

## 2023-05-04 10:25:01 - general channel

**Jonjonjon**

Nice [@U01B8031PM1](@U01B8031PM1). I'm hoping to build it on my Dev box in the following week. Have you witnessed.any performance gains?

---

## 2023-05-02 15:55:49 - general channel

**Mo**

So basically you've got all of the memory management overhead of constructing 3840 x 2 lists which are each at least 2k elements long none of which is done in rust



I totally agree with you we should aim to speed up flumine (and betfairutil) using rust ideally by building on [https://github.com/tarb/betfair_data](https://github.com/tarb/betfair_data) but I think the current comparison is unfair

---

## 2023-05-02 15:48:41 - general channel

**Mo**

1. No one uses `ujson` any more, use `orjson`

2. From what I can tell, you do things differently in Python than rust. In Python you read the entire contents of the file into memory then start deserialising line by line. In rust you are deserialising as you read the lines. I assume the latter will be more efficient as it lets the CPU get to work on deserialisation while you are waiting on I/O

---

## 2023-05-02 15:36:08 - general channel

**Adam Momen**

Thanks for the link, I agree, python garbage collector is slowing it down.

---

## 2023-05-02 15:32:44 - general channel

**Adam Momen**

[@U4H19D1D2](@U4H19D1D2) Have you considered writing rust version of _flumine_ for speed gains_?_



I’m running backtesting across thousands of markets everyday, the processing time slow down as the data increased, following all the performance guidelines and tips in the [https://github.com/betcode-org/flumine/blob/master/docs/performance.md|doc](https://github.com/betcode-org/flumine/blob/master/docs/performance.md|doc) and installing flumine with c &amp; rust liberaries (`flumine[speed]` ) helped but it was still relatively slow.



I wanted faster processing speed, so I’ve run a simple benchmark [https://www.notion.so/Flumine-Backtesting-Benchmark-c3b20cd40fd4487388fd2d73ed23f72f?pvs=4|experiment](https://www.notion.so/Flumine-Backtesting-Benchmark-c3b20cd40fd4487388fd2d73ed23f72f?pvs=4|experiment) to compare file reading speeds from disk in Python3.11 and Rust, why I chose rust?  It’s safe and fast, and the learning curve not that steep.



*Rust was 35x faster.*



&gt; Note: I ran the benchmark on my M1 Air, I admit that it’s the not the best way of recording the result, but it was good rough estimation.

---

## 2023-04-23 11:18:30 - general channel

**Tom**

I'm interested to know how you guys are working the bet placement process with Flumine.



My lines are blurring between a linear computing process, OOP (which I'm only slowly getting the hang of), the RunnerContext object, Trade object, order itself, order-packaging and Trade execution - do I push the order execution calling functions in flumine, or create it to the objects and write general code in process_orders to process all orders? I was executing trades, until I started building an output for results comparison e.t.c. and I feel like I stepped over a layer of complexity and having trouble contextualising it all now

---

## 2023-04-20 14:01:15 - general channel

**Peter**

Flumine maintains a list of market objects that you could iterate over to find the one with the smallest seconds_to_start attribute.



But that's not how I'd do it personally. Cleaner would be to treat each market separately and within the strategy do this processing when each market's seconds_to_start &lt;= 600 (you could set a flag in market.context to ensure that it's only done once).



Even cleaner would be to put this test and associated processing into the call() method in a custom middleware class.



However, if your external site is slow to respond you may need to push this out to another process to avoid holding up stream processing.



Yet another approach would be to make the external calls in a worker function, in which case rather than trying to infer the next race from the stream, I'd recommend making a single call at the beginning of the day using betfairlightweight to load all the catalogues and save a local list of the day's start times and then work through that to trigger your calls to the external site.

---

## 2023-04-18 05:48:40 - general channel

**Mo**

Standard practice is to patch `open` with `smart_open.open` and then `flumine` can read the `bz2` files directly: [https://betcode-org.github.io/flumine/performance/#file-location](https://betcode-org.github.io/flumine/performance/#file-location)

---

## 2023-03-26 19:41:37 - strategies channel

**R**

also yes, hyperparameter optimization and cross-validate the shit out of everything.

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

## 2023-03-17 10:52:27 - issues channel

**Kosta Pana**

Thanks very much Liam - I will have a try with setting logging to debug.



Do you know if setting logging to debug has any performance cost? Otherwise what is the best way to detect if a stream breaks down?

---

## 2023-03-13 11:16:00 - issues channel

**Sunken**

Still having issues. Putting in some of the code I used to test the difference

```test_file_path=F'{start_path}PRO_2020_Apr_10_29766007_1.170279955.txt'

data_dump=open(test_file_path,"r")

json_dump=data_dump.readlines()



listener = betfairlightweight.StreamListener(max_latency=None,calculate_market_tv=True,cumulative_runner_tv=True)



stream = trading.streaming.create_historical_generator_stream(

    file_path=test_file_path,

    listener=listener,

)



gen =stream.get_generator()

market_booksList=list(gen())



total_traded=0



for i,update in enumerate(json_dump):

    if i == 0: # No price info

        continue

    betfair_dataDict=json.loads(update)

    trade_changeList=betfair_dataDict['mc'][0]['rc']



    for changeDict in trade_changeList:

            if 'trd' in changeDict:

                total_traded += changeDict['tv']

    total_traded_blw=market_booksList[i][0].total_matched

    if abs(total_traded - total_traded_blw) &gt;0.1:

         print(total_traded, "basic")

         print(total_traded_blw, "blw")

         print(i)```

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

## 2023-03-09 13:32:26 - general channel

**Richard Cornish**

Any chance to have a look at this one? I’m still trying but failing miserably with the various Python libraries :joy:  if I use gigasheet to combine and transform the files that works, but it is slow and labour intensive 

---

## 2023-03-08 19:48:42 - strategies channel

**liam**

I think it’s more important to try and understand what impacts a strategy pnl.



I find that optimising model variables / thresholds in an ideal world to be be the easy part, the problem is the market is not ideal. You can see this by comparing a model with 100% matching vs real world, the optimum will be different. 



To answer your question I think it can certainly vary per market type, racing is a nightmare as you have the slow decay mixed with the change in ‘seasons’. I don’t think I have ever had a strategy increase it’s profit/ROI without an iterative AvB type development to see where the limits are. You can’t do this purely through simulation, sometimes involves bleeding some cash. I have mentioned this before and I think there was a poll but I spend 80% of my time on execution/matching (which feeds into threshold and model optimization) 

---

## 2023-03-07 15:46:17 - betfair-news channel

**Unknown**

Hi [@U02K5EBKNBF](@U02K5EBKNBF) - please see further details regarding the root cause of Saturdays issue - _We had multiple failovers of the Exchange Bet Stream on Saturday, which caused a full snapshot to be sent out to our other downstream applications. One of these applications ran out of memory when trying to process the snapshot, causing long garbage collection, and leading to bet placement failures. To mitigate such problems, we are currently in the process of aggressively reducing &amp; tuning memory usage across both the Bet Stream and our downstream applications_

---

## 2023-03-05 15:44:38 - strategies channel

**Dave**

Question regarding strategy calibration: how often do you tend to recalibrate your strategy parameters, e.g. refresh the thresholds of your triggers etc? For my football betting I have always been able to keep my thresholds the same, but retrain my ML models periodically, for a few years now. Never really been an issue. For racing (which I've only been doing at scale since last Nov), I have no model, just reacting to observations in market data (so the model ends up being a bunch of handcrafted thresholds). I have no sense yet as to how quickly my calibrated values may become too stale. Does anyone do anything as basic as this, and if so, how do you keep your thresholds/parameters up to date? Run some periodic optimization over a grid of possible thresholds?

---

## 2023-03-05 09:19:19 - general channel

**Jonjonjon**

Are you doing it on live data with Pandas? If so, Pandas is too slow if you are updating it with every price update. More primitive types should be fastwr

---

## 2023-03-05 08:21:25 - general channel

**Will**

hey legends - what is the best way to store/gather past last traded price on a runner. for example, currently i load a dataframe with the  ltp from about 10mins out every time it changes, then perform my predictions. if i load too many markets, i end up with latency issues.

---

## 2023-02-22 09:45:55 - general channel

**jp**

Anyone got experience with live/inplay soccer data from [https://www.thesports.com/](https://www.thesports.com/)? In particular I am interested in latency, quality of data and pricing.

---

## 2023-02-21 10:44:55 - general channel

**liam**

you will be fine, streaming is incredibly lightweight on cpu/memory

---

## 2023-02-21 10:38:32 - general channel

**Ke**

If i subscribed other markets which i'm not interested in as i can't filter them out, would it slow down the streaming for the games I'm interested in? Or would the stream speed be affected by the number of the game i subscribed?

---

## 2023-02-21 09:46:59 - general channel

**liam**

Assuming you are filtering by NBA marketTypes I think you would struggle to register any latency issues, can't filter by competitionId when streaming :wink:

---

## 2023-02-21 09:41:26 - general channel

**Ke**

Oh, i didn't realize it works that way. That would be great. Regarding filter, i'm only interested in NBA. But it looks there is no way to filter only NBA games. I can ignore all other games when process market data, but would it cause any latency issue as it streams data of games I'm not interested?

---

## 2023-02-20 23:21:09 - random channel

**birchy**

Maybe something like this? [https://apple.stackexchange.com/questions/239536/slow-performance-accessing-ubuntu-samba-folders/239559#239559|https://apple.stackexchange.com/questions/239536/slow-performance-accessing-ubuntu-samba-folders/239559#239559](https://apple.stackexchange.com/questions/239536/slow-performance-accessing-ubuntu-samba-folders/239559#239559|https://apple.stackexchange.com/questions/239536/slow-performance-accessing-ubuntu-samba-folders/239559#239559)

---

## 2023-02-20 21:11:58 - random channel

**Newbie99**

I'm completely new to Mac OS and google is very limited on the subject of network drive mapping issues, so hopefully someone here has faced similar.



I have a (linux based) NAS where I store all my market recorded data, I have the drive mapped on a windows PC and can access files easily without any major lag, however when I mount the drive via terminal in Mac OS the performance is really poor, for example the same folder (containing approx 12k recorded market files) takes &gt; 30 seconds to return results from the command line (compared to virtually instantaneous on the windows machine).



The other confusing thing is that via SSH performance is fine from both the windows machine and the mac.



Obviously the solution seems to be, SSH rather than try to map the drive, but does anyone have any ideas why this could be happening (all machines are on the same WIFI network and physically in the same room)?

---

## 2023-02-13 07:21:31 - general channel

**liam**

[https://betcode-org.github.io/flumine/performance/|Yes](https://betcode-org.github.io/flumine/performance/|Yes) 

---

## 2023-02-12 22:27:37 - general channel

**Trex44**

Is there a way to add multiprocessing to the FlumineSimulation class (think this would be the correct class to add it to) to get it to speed up back tests? Idea would be to run the simulation on the markets in parallel then collect and merge the results. Mt attempts so far haven't worked.

---

## 2023-02-07 09:46:15 - issues channel

**liam**

How do you normally access the API? From memory you are blocked from automating the actual login so you would have to:



```trading = betfairlightweight.APIClient("username", "password", app_key="appKey")



trading.set_session_token("SSOID")```

---

## 2023-01-25 13:39:53 - random channel

**river_shah**

I don't know much about inplay horses so won't comment. I know for other bet sized constrained markets, multiple strategy replicates typically result in very bad performance for high stakes

---

## 2023-01-23 09:34:55 - issues channel

**liam**

I am suddenly getting a flumine instance dying at 04:55 almost every morning, from memory betfair do some currency calculations at around this time? Anyone else?

---

## 2023-01-22 15:26:23 - general channel

**Adam Momen**

What is the time unit measure of the latency? Is it in seconds?

---

## 2023-01-16 12:34:15 - random channel

**liam**

In python it’s the creation of objects that takes the large majority of time as shown by the Rust library, reading json isn’t worth the optimisation. Have you profiled your code? 



I use s3 for storing the data but have a local cache (~100gb) to remove the network latency 

---

## 2023-01-16 11:34:25 - random channel

**D C**

I know some of you here put a lot of importance in performance when it comes to simulating/backtesting etc. I don't use flumine/BFLW, but from what I read people mostly use S3 storage, decompress raw JSON stream  files and run backtests like that (please correct if wrong). Given performance considerations, I was wondering if anyone uses or has given thought to utilising an alternative file format to give processing an extra zip? I'm working on some GPS stuff at the moment and it's occurring to me that a large proportion of processing time is down to JSON parsing every time I run analysis. I was wondering if anyone has tried binary file formats or something similar? Not sure if I will eventually do this as it may be a premature optimisation but I've worked a lot with binary data files which has made me start thinking about going down this route.

---

## 2023-01-13 18:56:36 - strategies channel

**R**

Agreed, the whole "catastrophic forgetting" concept is very relevant.  Funnily I've just found that a simple static rule is on-par for performance, maybe it eeks out a small edge but it's practically irrelevant.



I'll toy with it some more for shits 'n giggles though!

---

## 2023-01-13 15:13:06 - general channel

**R**

also, billions of rows with an in-memory data structure?



I'd be more inclined to use out-of-core compute, e.g. streaming + database / indexed data

---

## 2023-01-13 15:01:38 - general channel

**Peter**

Looked at it a couple of times, but each time felt that the overhead of adjusting to it outweighed the performance benefits. For context my dataframes can run to several million rows, but I'm a long way short of the billions that polar seems designed to handle.



Worth adding that the real cost of the switch is very difficult to evaluate. It's fairly easy to understand "faster" and to see from the docs what can be done using Polars. But the real pain point would come in the edge cases when I hit an "oh shit" moment as I realise that this thing I do in Pandas may not exist in Polars and I've got to code it up myself or keep using Pandas anyway.

---

## 2023-01-13 08:13:27 - random channel

**Mo**

Obviously in the absence of feature requests, what I add to betfairutil is whatever I'm currently working on. I've been finding recently that it really helps not to be lazy about just reading everything into memory as this allows me to saturate my CPU with workers



```  * get_market_books_from_prices_file

  * get_minimum_book_percentage_market_books_from_prices_file```

Are two other examples. Previously I would probably just have read the entire set of market books into memory then use bisect functions to find the ones I care about

---

## 2023-01-11 14:06:59 - issues channel

**JFP**

Thanks Liam. The strategy giving different results does not have any simulated middleware. Is there anyway smart matching could be causing these discrepancies or do you think it could be some update in between versions 1.19.14 and 1.21.0, I noticed a couple of speed improvements for backtesting between these versions?

---

## 2023-01-09 15:12:46 - general channel

**PeterLe**

Thanks Alessio, this is just a standard drive (ie not SSD)...so if I slowing increase the setting, at some point it will be too slow and errors would occur?

---

## 2023-01-09 14:20:35 - general channel

**thambie1**

I use Java, and started with the codebase [@UUE6E1LA1](@UUE6E1LA1)  linked a few years ago. This is the best starting point for Java I'm aware of. Unless you really need a high performance language, I'd recommend going with betfairlightweight. You'll save a lot of time, particularly with getting a backtesting system out of the box.

---

## 2023-01-05 17:44:46 - general channel

**Mo**

I'm into low latency stuff so Docker isn't really compatible with that approach - I don't have anything against it though



We use ansible to manage all of our infrastructure - in addition to what Python virtual environments should be set up with what packages installed we also use it to declare what OS packages should be installed, what cron jobs should be created, what services should be running, what directories should exist, which OS users should exist, etc. etc. I certainly wouldn't recommend it if the only thing you need to solve is how to manage your Python virtual environments. But if you wanted a tool that let you manage them on top of everything else I mentioned then it is very powerful

---

## 2023-01-03 19:26:26 - issues channel

**Brøndby IF**

Good afternoon everyone!



About streaming (specifically about soccer events).



In a normal filter `betfairlightweight.filters.market_filter` I use `in_play_only=True`, but in `streaming_market_filter` there is only `turnInPlayEnabled`.



What method do you recommend to handle the need for only inplay events using streaming for lower latency in data collection?

---

## 2022-12-31 22:20:58 - general channel

**Ralegh**

Anyone used flumine with pypy? Absolutely chewing up memory

---

## 2022-12-30 12:38:49 - general channel

**Mo**

Have you read [https://betcode-org.github.io/flumine/performance/](https://betcode-org.github.io/flumine/performance/)?

---

## 2022-12-30 12:32:18 - general channel

**Ralegh**

Ah I see yeah makes sense, I’ve been using it a lot so fairly used to the interface, only annoyance is simulation speed but that’s probs a python issue, just gonna wack on a c6a with joblib and pray haha, much better to be slower and more accurate though, lifesaver

---

## 2022-12-30 11:43:22 - general channel

**PeterLe**

I run a few instances locally on my home PC and noticed the last couple of days that I had high latency (circa 0.6)...

Today when i started them, I had no latency messages.

I tend to run them anyway even when I get the messages, so not too concerned

What would you think is the main reason and does everyone get theses from time to time? Thanks

---

## 2022-12-23 09:04:50 - strategies channel

**Liam Querido**

What is an appropriate figure for bet latency?

---

## 2022-12-23 09:03:36 - strategies channel

**Mo**

Personally I think provided you are using an appropriate figure for your bet latency (and including the bet delay if appropriate) then you can assume if what you want is still on the order book then you get matched

---

## 2022-12-20 13:39:27 - general channel

**shashank bansal**

I want to create an interpreter system where people subscribe to a server and server sends the feed from BF to subscribers. There can be 1000s of connection and can burst out the system with so many odds every few ms. S3 will slow down the latency for sure. So, was thinking towards Dynamodb.

---

## 2022-12-17 19:03:40 - general channel

**Matthieu Labour**

Hi, when recording market data for 2 sports, do you recommend that I use one strategy for both sports or 2 strategies (one per sport)? In other words, would you create 2 instances of [https://github.com/betcode-org/flumine/blob/master/examples/strategies/marketrecorder.py](https://github.com/betcode-org/flumine/blob/master/examples/strategies/marketrecorder.py). One per Sport or one only. Is there performance penalty in having multiples and specializing him.

---

## 2022-12-08 11:45:49 - strategies channel

**PeterLe**

Yes what I mean by the reference to betangel was that there would be a number of uses using it that needed to get up to speed so there may have been som easier profits available initially. I have the TPD feed via betfair (using c#) and i also tested using betangel. I got different results using the same strategy criteria using my own program and betangel. Your correct about the frequency of the updates by the way.

---

## 2022-12-08 09:45:59 - strategies channel

**D C**

Pretty much all my inplay GPS based strats have been down significantly on last year performance. Still making enough to dodge returning to employment but its getting close enough that I have to keep thinking about it. I don't know how I would go about testing it but it 'feels' like the inplay market is sharpening up a bit with fewer opportunities.

---

## 2022-12-04 17:19:38 - general channel

**AI Trader**

I understand that. What I am trying to achieve here s to select a subset of say, 100 markets, out of 10,000 markets that pass through the basic filter provided by Flumine. I don't want to subscribe to every update of these 10,000 markets as this would be unnecessary and slow. Are you saying that adding and removing markets after the framework is running is impossible?

---

## 2022-11-23 11:10:44 - issues channel

**EJono**

I am currently testing out a strat using flumine on several markets, one on the Morocco v Croatia MATCH_ODDS currently in play. market_id: 1.197092678



Im noticing large periods of time between successive process_market_book() executions up to ~10-20 minutes at some points before regular millisecond frequencies resume. I was wondering if anyone else is experiencing slow streamed market_books for this game even though its a very high volume world cup game, or if there is something else i am not aware of that is causing pmb to not execute ie market_book.status == "CLOSED"  (which is a filter i have in place during check_market_book). Any help greatly appreciated.

---

## 2022-11-20 11:29:54 - general channel

**Jeff Waters**

Hi



I'd like to make is so that, when I run back tests using the multiprocessor code at [https://betcode-org.github.io/flumine/performance/](https://betcode-org.github.io/flumine/performance/), the orders in each process's blotter are written to a spreadsheet when that process has completed running.



Would that be possible, and if so where would I put the a call to the spreadsheet-generating function?



Thanks



Jeff

---

## 2022-11-18 21:40:49 - random channel

**Newbie99**

A while ago I seem to remember someone on here talking about [http://api-football.com|api-football.com](http://api-football.com|api-football.com), out of curiosity, I believe they refresh the live score once every 15 seconds, but does anyone know roughly how much latency there is in that (i.e. at the point of update, would it be 'live' or is there a noticeable delay)?



For my purposes ms don't matter, its only really if its a large number of seconds away from the other live score services that I guess it could be a problem.

---

## 2022-11-15 21:43:59 - random channel

**V**

Nope, I stand corrected. Looks like instances of user defined classes _are_ indeed hashable, and the hash defaults to the output of id. Which in CPython I believe is the memory address of the object. So assuming you pass in a reference to the exact same runner book, it _should_ give you what you want.

---

## 2022-11-15 09:13:51 - general channel

**liam**

```from flumine import config



config.place_latency += 0.1```

---

## 2022-11-15 09:11:47 - general channel

**Jorge**

[@U4H19D1D2](@U4H19D1D2) This doesn't seem to affect orders being matched or not. Shouldn't I modify this instead?

```import flumine.config

flumine.config.place_latency += 0.1```

---

## 2022-11-14 09:29:54 - random channel

**Mo**

Yeah, switched to it in production as soon as it came out. For the performance benefit

---

## 2022-11-12 16:43:45 - general channel

**liam**

Assumption are:



• you would never want to miss an update

• make sure your strategies can process quicker than a new book update 

• If you find this is a limitation then flumine isn’t for you (although I would fix the slow strategies)

• Workers are for polling type situations (

ie. external data update)

• Middleware gets called on every marketBook update (similar to django request/response cycle / middleware)

---

## 2022-11-05 20:11:31 - issues channel

**liam**

[https://betcode-org.github.io/flumine/performance/#file-location|https://betcode-org.github.io/flumine/performance/#file-location](https://betcode-org.github.io/flumine/performance/#file-location|https://betcode-org.github.io/flumine/performance/#file-location)

---

## 2022-11-05 01:56:45 - general channel

**Unknown**

You can get this historical data from [http://betsapi.com|betsapi.com](http://betsapi.com|betsapi.com) a cheap (and slow) API.

---

## 2022-11-03 03:21:01 - general channel

**Guy Incognito**

Is there anyway to run the loop at the end of [https://github.com/betcode-org/betfair/blob/master/examples/examplehistoricdata.py|https://github.com/betcode-org/betfair/blob/master/examples/examplehistoricdata.py](https://github.com/betcode-org/betfair/blob/master/examples/examplehistoricdata.py|https://github.com/betcode-org/betfair/blob/master/examples/examplehistoricdata.py) in parallel to speed up download. I tried using joblib but there isn't much difference.



The original loop looks like this:

```for file in file_list:

    print(file)

    download = trading.historic.download_file(file_path=path)

    print(download)```

---

## 2022-10-30 05:41:46 - issues channel

**thambie1**

anyone seeing stream latency in the 100+ millisecond range?

---

## 2022-10-25 17:12:14 - strategies channel

**Mo**

For those of you who do in play, how do you score your models?



Using standard scoring rules has never quite sat right with me given you may be making hundreds (or theoretically infinite numbers) of predictions repeatedly on the same outcome



Backtests is another option but realised profit is slow to converge and all the other things that go into them such as choice of staking make it hard to focus on predictive accuracy of the model

---

## 2022-10-19 12:54:14 - issues channel

**D C**

The benefit is huge [@U01FQH5FA8M](@U01FQH5FA8M). It is not just speed - it is also about lower data transmissions and packet sizes but also greater precision when dealing with things like nonrunners and reduction factors and separating IP money from PE money at the race crossover. I realise that these things may not be directly important to you. I resisted for ages because things were working fine but I definitely noticed profit improvement after switching to streaming. It also makes analysing recorded data a lot easy because listMarketBook calls means you have to calculate the deltas yourself after every call. I guess it depends on your refresh rates and needs though so I get its a personal decision.

---

## 2022-10-19 12:49:33 - issues channel

**Mick**

I know almost nothing about streaming, other than somehow things happen faster - and generally speed is not an issue for me... So I'm concerned that I will have to learn a whole load of new things for not much benefit.

---

## 2022-10-14 13:22:53 - issues channel

**Aaron Smith**

just putting this out here for closure: not calling `market.transaction()`  on each market_book actually solved the latency issues (only change i made and havent gotten a single latency warning since).

Still gotta get profiling working for the future i guess :smile:

---

## 2022-10-13 13:07:31 - issues channel

**liam**

you might be surprised, common error to pass in an incorrect var, anyway run [https://betcode-org.github.io/flumine/performance/#cprofile|this](https://betcode-org.github.io/flumine/performance/#cprofile|this) and share the output (dm if you want) and you will know the answer straight away

---

## 2022-10-13 13:03:18 - issues channel

**liam**

the log with "High latency between current time and MarketBook publish time" normally points to something bad within a strategy, profiling will tell you straight away

---

## 2022-10-13 13:00:21 - issues channel

**Aaron Smith**

Hi people

I switched from using `market.place_order(order)`  to using

```with market.transaction() as t:

    for order in orders:

        t.place_order(order)```

This was done to chunk up orders and with that make for a smoother execution.

However sadly this has had the opposite effect. Since the change i m getting flooded with all possible latency warnings and higher delay than i ve ever seen before (60seconds+), so i assume i must ve messed up somewhere.

example warnings (just imagine an army of these):

```{"asctime": "2022-10-13 11:00:58,015", "levelname": "WARNING", "message": "[OrderStream: 1001]: Latency high: 62.55000066757202"}



{"asctime": "2022-10-13 10:59:20,992", "levelname": "WARNING", "message": "High latency between current time and MarketBook publish time", "market_id": "1.204868412", "latency": 26.081366777420044, "pt": "2022-10-13T10:58:54.911000"}



{"asctime": "2022-10-13 10:59:20,987", "levelname": "WARNING", "message": "[MarketStream: 2001]: Latency high: 26.017338514328003"}```

The basic structure i use goes as follows:

All this happens within the strategy method `process_market_book` .

I create a bunch of orders for different runners using `trade.create_order` .

I collect these orders in a list. Then i call

```

    @staticmethod

    def place_orders(orders: list[BetfairOrder], market: Market):

        with market.transaction() as t:

            for order in orders:

                t.place_order(order)





    @staticmethod

    def cancel_orders(market: Market, orders: list[BetfairOrder]):

        with market.transaction() as t:

            for order in orders:

                if order.status == OrderStatus.EXECUTABLE:

                    t.cancel_order(order)```

to place and cancel orders.



Anyone having an idea whats going on here?

If no orders are collected for placing/cancelling, these 2 functions are still called with an empty list, can this cause any issues?



Thanks a lot to anyone taking the time :slightly_smiling_face:

---

## 2022-10-11 09:20:07 - general channel

**Peter**

[@U03TJKFLE8K](@U03TJKFLE8K) My path was comparable to yours. I wrote the (still) most widely used PHP package for consuming the Betfair API. But it became clear that PHP was a severely limiting factor. All the best tooling for analysis, testing and trading in this space is in Python (i.e. Betfairlightweight, Flumine, Pandas and Jupyter Notebooks).



So I went all in, learnt the language and now work almost exclusively in it (with a bit of Rust thrown in when I need compiled execution speeds). So my recommendation would be the familiarise with the tools that best fit the job rather than trying to bend your process to fit what you currently know. Though that is said without knowing what your processes are, e.g. if you are placing your bets manually at the bookmakers from data summarised via web pages you’ve constructed with Node, there may be a case for not re-inventing the wheel, just the engine :slightly_smiling_face:

---

## 2022-10-10 16:29:58 - general channel

**Peter**

Betfair updates prices 20 times per second, which is 20 times faster than the minimum refresh rate allowed for the website, and that's assuming that your scraper logs in and you have your account set to the fastest refresh rate. Then you have to add the latency and processing time that your process adds on top.



If your script doesn't log in then you're seeing delayed prices, which can often bear very little resemblance to the current prices (we get queries here about that fairly regularly).



[@UBS7QANF3](@UBS7QANF3) is right. If you're serious about this, it's way better to take the time to learn how to do it properly.

---

## 2022-10-03 13:01:33 - general channel

**Jonjonjon**

Rust is beyond my skills. Are there any areas we might be able to improve performance if we use Numba? If you aren't already familiar, it will compile and make purely numerical stuff a lot faster. But if we need to use classes, attributes and dictionaries then things will be trickier.

---

## 2022-10-02 09:56:16 - general channel

**Alessio**

If you want to speed it up i think aws batch/lambda and equivalents are a reasonable route for "pay-as-you-go"

---

## 2022-10-01 22:26:41 - general channel

**thambie1**

Apache Spark is a distributed data processing framework. If you want to run flumine backtest parallelized on many machines at once, it is useful. Other than that, it is not useful. It's not going to speed anything up on your local machine.

---

## 2022-10-01 22:16:34 - general channel

**Jeff Waters**

I was just reading an article about Pyspark, which said it can process data at vastly faster speeds than traditional Python. [https://sparkbyexamples.com/pyspark/what-is-pyspark-and-who-uses-it/|https://sparkbyexamples.com/pyspark/what-is-pyspark-and-who-uses-it/](https://sparkbyexamples.com/pyspark/what-is-pyspark-and-who-uses-it/|https://sparkbyexamples.com/pyspark/what-is-pyspark-and-who-uses-it/)



Could it be used to achieve faster back testing with Flumine?



Thanks



Jeff

---

## 2022-10-01 21:19:27 - issues channel

**Aaron Smith**

today i m getting flooded with these bois today:

```"WARNING", "message": "[MarketStream: 2001]: Latency high: 0.5774619579315186"```

I get it correctly that these have nothing to do with code execution and all to do with connection to the betfair server?

Is anyone else experiencing this or is this only on my end?

---

## 2022-09-28 20:02:33 - random channel

**foxwood**

Randomly split your data into at least 2 sets. Train the model on the first set then see what the built model achieves on the unseen second set. Great result on training and worse performance on validation is overfitting. Lots of articles out there on ways to loosen it up.

---

## 2022-09-28 19:55:00 - random channel

**Unknown**

Did you split into training/test data_sets? I m not an expert in machine learning, but it seems very logical that if performance on the training data is significantly better than the performance on the test data that you are overfitting

---

## 2022-09-28 06:44:58 - random channel

**river_shah**

See if this could work for you: [https://stackoverflow.com/questions/13780907/is-it-possible-to-np-concatenate-memory-mapped-files](https://stackoverflow.com/questions/13780907/is-it-possible-to-np-concatenate-memory-mapped-files)

---

## 2022-09-27 19:16:03 - random channel

**CL**

Try some of the pyarrow functionality - eg pa.concat_tables, and then convert the resulting table to pandas if needed. I've found the arrow libraries to be generally more memory efficient.

---

## 2022-09-27 17:33:31 - random channel

**Jonjonjon**

Suppose I am using multiprocessing with Flumine to produce data files for a few thousand markets.



At the moment these are feather files.



I want to load these feather files into memory.



I can load the feather files into memory separately. They fit.



However, I cant concatenate them as I run out of ram.



I have tried writing them all into a CSV. But that is too big.



I have tried sequentially writing them into a single parquet which is 1.5gb. but when I try to load that the ram usage explodes so I can't use it.



What would others suggest here?

---

## 2022-09-25 17:18:46 - random channel

**D C**

Any recommendations of how to deal with other than bog standard CS - currently doing this and it is painfully slow?

---

## 2022-09-25 12:10:06 - betfair-news channel

**Mick**

I got blocked once before for reading too much data whilst making too few bets and it was a painful and slow process getting unblocked so now I'm paranoid about getting blocked again. My data use/bet size ratio has improved very dramatically so that's not an issue anymore but there's a couple of things I've been doing recently that I wanted to check on. Firstly - I'm wanting to leave my trading unattended for hours and just for safety I'd like to take all but the bare minimum required cash in my account each day and put more back in the following day - we're talking a few hundred pounds. Would that cause a problem? Secondly, I've been trying a strategy of putting in a bet request above the market price and then gradually lowering it as race time approaches. But for programming simplicity it's actually easier to cancel and then make a new request (not sure if the API lets you change your requested odds anyway). So for any one horse I might make of the order of a dozen bets that get requested and cancelled before an order is accepted. The duration of any single requests is at least ten seconds. Might this cause me any trouble?

---

## 2022-09-23 10:17:31 - general channel

**PeterLe**

I was just checking my P&amp;L's this morning and noticed that one particular flumine strat on AWS Ubuntu had done well over the last 30 days or so...so i thought Id log into to check all looked ok disk space etc...

Everything looked good except I noticed that i had run that particular program via Pycharm rather than standalone...:grinning::man-facepalming:

So now im thinking, whether to just leave it running or stop it and run standalone... (I appreciate that the former is not good practice and maybe slower, but what would you do?) Thanks

---

## 2022-09-22 12:56:34 - betconnect channel

**Sam**

Hey [@U9JHLMZB4](@U9JHLMZB4), we made some changes to `bet_request_get` to improve performance + added some functionality around layside filtering.

I'm not sure what specifically has caused the break because the output for `bet_request_get` hasn't changed, nor has the input.



We've rolled the changes back and we're investigating in the meantime. Can you let us know if you're able to get bet requests through the api again?

---

## 2022-09-20 21:17:02 - issues channel

**TT**

I'm looking at the [https://betcode-org.github.io/flumine/performance/|multiprocessing code example in the docs](https://betcode-org.github.io/flumine/performance/|multiprocessing code example in the docs), which I've got working, but how do people usually assess the combined results? When running a single process you have a single framework and can [https://github.com/betcode-org/flumine/blob/master/examples/simulate.py#L34|iterate over the markets and orders](https://github.com/betcode-org/flumine/blob/master/examples/simulate.py#L34|iterate over the markets and orders), but it's less obvious how to do this when multiprocessing, (without looking at each framework in isolation.)

---

## 2022-09-18 10:36:26 - random channel

**Peter**

Bringing this back to basic principles, workers are executed on a schedule / frequency that you determine and (normally) in a different thread hopefully on a different processor so have minimal impact on your strategy's processing time. Whereas middleware will be triggered with each market update and will delay / extend your strategy's processing.



So which is appropriate is going to depend on the CPU resources needed for your processing and the criticality of having it done for every market update, and oftentimes there won't be a clear answer.



To put this into context with your examples, for a) if your processing is quick and needs updating every time the prices move, you probably want middleware (though you may also want to cache the prices and check that the update has moved the ones you're interested in before executing the bulk of your processing). For b) if you're ingesting and processing a lot of data from an API and/or dealing with its latency and/or are not allowed to make up to 20 calls to it per second, then a worker is likely to be a better solution.

---

## 2022-09-17 19:38:18 - random channel

**Newbie99**

That said I'll try and think how to re-write for middleware as I'd like to get more up to speed with how that works

---

## 2022-09-17 19:37:46 - random channel

**Newbie99**

I can probably re-write what I need in a single thread in all honesty for this one, I've got into the habit of using workers as in live otherwise I end up with a lot of latency warnings (probably not for this one as it happens, its not very CPU intensive).

---

## 2022-09-17 16:10:47 - random channel

**Newbie99**

This is following on from the earlier conversation about backtesting with multi-proc (but isn't specific to chunking and event_processing, or at least I don't think it is...that said who knows).



So, I pass a list of markets to this function called startup, which runs as expected, in this instance it calls a worker, which doesn't run as expected.



Here is the startup function (this appears to run correctly, i.e. I can see the markets are loaded, market catalogues added and profit / orders always show as 0, but at least that confirms the script is working):



```def startup(markets, snapshot={}, strategy_names=strategy_names, event_list=False):

    logger = logging.getLogger()



    custom_format = "%(asctime) %(levelname) %(message)"

    log_handler = logging.StreamHandler()

    formatter = jsonlogger.JsonFormatter(custom_format)

    formatter.converter = time.gmtime

    log_handler.setFormatter(formatter)

    logger.addHandler(log_handler)

    logger.setLevel(logging.CRITICAL)  # Set to logging.CRITICAL to speed up simulation



    start_time = get_utc_time()



    settings = [setting for setting in rc if setting['on'] is True and setting['strategy_name'] in strategy_names]



    client = clients.SimulatedClient(simulated_full_match=False)



    framework = FlumineSimulation(client=client)



    print('Start of chunk', '-' * 150)

    for market in markets:

        print(check_event_id(market))



    with mock_patch("builtins.open", smart_open.open):

        for s in settings:

            max_selection_exposure = s['max_selection_exposure'] if true_or_false(s['max_selection_exposure']) != False else None

            if s['strategy_type'] == 'simple':



                ### ---- Remember to change listener kwargs , "listener_kwargs": {"seconds_to_start": 7200, "inplay":False}



                strategy = betting_strategy(start_time=start_time, settings=s, paper=client.paper_trade,

                                            market_filter={"markets": markets, "listener_kwargs": {"seconds_to_start": 7200, "inplay":False}, "event_processing": True},

                market_data_filter=streaming_market_data_filter(

                fields=[

                    "EX_ALL_OFFERS",

                    "EX_TRADED",

                    "EX_TRADED_VOL",

                    "EX_LTP",

                    "EX_MARKET_DEF",

                    "SP_TRADED",

                    "SP_PROJECTED",

                ]

                ),

                streaming_timeout=2,

                max_selection_exposure=max_selection_exposure,

                max_order_exposure=s['max_order_exposure'],

                conflate_ms=s['conflate'],

                name=s['strategy_name'],



                )



                framework.add_strategy(strategy)





        worker_settings_list = [

            {'function_name': 'get_in_play_football_data', 'function': get_in_play_football_data, 'func_kwargs': None ,'interval': 15, 'start_delay': 0}

        ]



        for f in get_worker_functions(settings):

            function_setting = [ws for ws in worker_settings_list if str(ws['function_name']) == f['function_name']]

            if len(function_setting) &gt; 0:

                function_setting = function_setting[0]



                framework.add_worker((BackgroundWorker(

                            framework,

                            function_setting['function'],

                            func_kwargs=function_setting['func_kwargs'],

                            interval=function_setting['interval'],

                            start_delay=function_setting['start_delay']

                        )))



        ''' Always add Risk Calc worker '''

        framework.add_worker(

            BackgroundWorker(

                framework,

                calc_risk,

                func_kwargs=None,

                interval=0.5,

                start_delay=5

            ))



        ''' Add in Middleware to get Market Catalogue '''

        framework.add_market_middleware(MarketCatalogueMiddleware())



        framework.run()



    for market in framework.markets:

        print("Order Count: {0}".format(len([o for o in market.blotter])))

        print("Profit: {0:.2f}".format(sum([o.profit for o in market.blotter])))



    if strategy_names[0] == 'market_data_extract':

        return write_market_context_to_json(framework)

    else:

        return write_pl_to_json(framework,group_by_market=False)```

Now, when I noticed the worker wasn't producing anything I did a quick test as follows:



```def get_in_play_football_data(context: dict, flumine) -&gt; None:

    print('ABCD')

    s = [m for m in flumine.markets]

    print(s)```

On screen I see the following:



```1.202093022 added

ABCD

[]

Order Count: 0

Profit: 0.00```

So the worker is running as we can see the printout, but how can s be an empty list?

---

## 2022-09-17 09:07:54 - random channel

**Unknown**

Last 24hrs, tbh yours seems high but as long as you aren't getting latency warnings I don't see an issue

---

## 2022-09-14 09:42:52 - random channel

**liam**

for me anything latency sensitive is flat files loaded at runtime

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

## 2022-09-13 20:47:40 - random channel

**Jonjonjon**

Is your latency column the "mean" value?

---

## 2022-09-13 07:56:59 - random channel

**Unknown**

You got me thinking so I did some tests yesterday on an instance I have running with 6 strategies that I know are slow at processing, here is the following at order creation:



```latency = (trade.date_time_created - market_book._datetime_created).total_seconds()```

Very strategy dependant but has the potential for the order to make a big difference in pnl / matching

---

## 2022-09-12 16:32:15 - general channel

**Aaron Smith**

not sure if i understand. The way i imagine it is

total_latency = signal_from_betfair_to_me + code_runetime + signal_from_me_to_betfair.

In a backtest, the time a signal between me and betfair takes can only be assumed, so you set some fixed value. But runtime of your code would be the same. Basically, if i added a time.sleep(1) in my process_market_book, this would not effect the result of the simulation ?

---

## 2022-09-12 16:01:04 - general channel

**Aaron Smith**

when backtesting with flumine, does runtime of your code effect the (simulated) latency?

---

## 2022-09-11 23:22:24 - random channel

**Jonjonjon**

I am running almost 200 strategy instances under a single Flumine instance on a single script.



I'm concerned that it might cause performance issues, due to the multiple calls to `check_market_book`

What is the recommended way to check whether or not I am likely to be experiencing latency issues?



Looking though the logs, I have this from the trade log:



`"date_time_created": "2022-09-11 22:03:05.967328", "publish_time": "2022-09-11 22:03:05.914000"`



I believe "publish_time" is the time that comes from the streaming market book update, and "date_time_created" is the time, which is around 53 ms. But assumes that my clock is aligned with the Betfair clock.



How would other users measure this?

---

## 2022-09-08 16:43:34 - issues channel

**Aaron Smith**

checking through my latency warnings i see that 98% of them are this version:

```"WARNING", "message": "High latency between current time and OrderPackage creation time, it is likely that the thread pool is currently exhausted", "trading_function": "cancel", "session": "&lt;requests.sessions.Session object at 0x7f02236a0b20&gt;", "latency": 0.102, "order_package": {"id": "3f6818d6-2f8b-11ed-969e-257a4444e788", "client": "&lt;flumine.clients.betfairclient.BetfairClient object at 0x7f028fd7ba30&gt;", "market_id": "1.203111349", "orders": ["138819438430078669"], "order_count": 1, "package_type": "Cancel", "customer_strategy_ref": "prod_GH", "bet_delay": 0, "market_version": null, "retry": true, "retry_count": 0, "async": false}, "thread_pool": {"num_threads": 25, "work_queue_size": 2}```

I get these on cancel and place. `work_queue_size` can be higher (last one it was at 19, this time 2 was highest for this chunk of latency errors (they generally come in chunks). What i m surprised by is `"num_threads": 25` , i can not really see why i would have 25 threads running?

---

## 2022-09-08 09:08:21 - issues channel

**Mo**

If you have something logging timestamps, you could look for a jump around the time the latency errors started. For example, if you log something that is typically around 100 milliseconds between messages and then you see a much larger gap and then a return to 100 milliseconds this might be evidence for this

---

## 2022-09-07 13:51:44 - issues channel

**Mo**

What's the latency warning based on? Local clock versus publish time? If so it could be your clock drifted/got synchronised to a source different enough from Betfair to start triggering the warnings

---

## 2022-09-07 13:36:43 - issues channel

**liam**

which latency warning?

---

## 2022-09-07 13:33:49 - issues channel

**liam**

and during the latency issues where was the CPU?

---

## 2022-09-07 13:26:14 - issues channel

**Aaron Smith**

Latency issues:

My code has been running unchanged for a few months now. I do get an occasional latency warning (maybe like 1 or 2 a week), but thats it. One day to the other i suddenly get a bunch of latency warnings, (30+ a day) with unchanged code.

I know i should probably profile my code, and while that may help, it seems like something else is going on on top. Therefore i wanted to ask you guys:

• What are possible reasons for latency issues? (this would somewhat boil down to slow code or bad connection i guess, but especially for the latter i wonder if there are reasons for this to suddenly pop up.

• How to resolve them? 

---

## 2022-09-07 11:35:36 - general channel

**George**

Hi guys, I'm looking at some PRO data and I would like to get a snapshot of the market at a particular point in time. Currently my approach is to load the data into a BFLW historical generator stream, and then check the timestamp of every single market book in the generator until I reach the one I'm interested in.

This is proving to be very slow (like 2 hours to run a month of data). I'm wondering whether there is a much smarter way to achieve what I am trying to do?

---

## 2022-09-02 19:10:39 - random channel

**Newbie99**

With regards to balancing EC2 instances / Betfair connections &amp; markets, is there a consensus on the best way to split things up?



Currently I just stick everything on a single T3.micro and in the last few weeks I've been getting a lot of latency warnings, to the point where at the weekends it just stops functioning.



This co-insides with me looking at far more football markets than before and whilst of course my code will be inefficient and there will absolutely be improvements, in terms of a sensible approach to grouping, what is the optimal way?



Currently it feels as though a single instance is fine with possibly somewhere between 2-3k markets (across horse racing and football), but above this it struggles.



So obviously I need to look for bottlenecks in my code, but aside from that, should I create a separate EC2 instance or should I split the football markets up across multiple connections etc?

---

## 2022-08-30 09:57:43 - general channel

**Guy Adini**

Hi guys, and apologies if this has been asked a million times before: I'm new and don't know where to find the FAQ :slightly_smiling_face:

Could someone please tell me where are the Betfair servers physically located, and where to put a server in order to get the lowest possible latency to them?

---

## 2022-08-29 19:40:52 - general channel

**Trex44**

I am building a GUI to sit on top of a script I have built for analysing data. Getting fed up of changing the filters in the code manually each time. However there is no way an EC2 environment can display a GUI. I want to adapt the script (which sits on my EC2 instance) to accept an input sent from the GUI on my local PC (the client), do the compute on the EC2 environment then return the output data back to my local PC where the GUI can make use of it.   I used WinSCP for one off downloads but that's too slow. I want to be able to move faster.

---

## 2022-08-26 09:19:43 - issues channel

**liam**

Looks like you need to profile your code, streams run in their own thread so wouldnt cause latency issues in the main thread unless they where very heavy

---

## 2022-08-26 09:18:20 - issues channel

**Johnny Boston**

Yeah, so it looks like I have open connections then. I found latency issues when I had multiple strategies (more than 5) in the same container.



I then split them up and that went away. The latency was mainly due to custom streams that were getting model odds on short intervals.

---

## 2022-08-25 21:18:38 - general channel

**Peter**

Not really. The constraint is the size of the internal network pipe at AWS, which no external software can influence. Best package is almost certainly boto3, which I'm sure AWS will have optimised for speed in this area as it's in their interest too to keep these pipes clear.



So the only practical way to optimise the speed is to ensure that the S3 bucket and EC2 instance are in the same region.



However, I've never found the streaming speed from S3 to be a constraint. Profiling and streamlining my code is usually a much more productive use of my time.

---

## 2022-08-25 20:57:14 - general channel

**Trex44**

Is there a way to speed up/optomise the downloading of files from S3 to EC2 does anyone know? A python library perhaps or some hardware tweak.

---

## 2022-08-23 13:14:37 - general channel

**birchy**

So presumably, the `[speed]` install has issues on Windows? I've always used the default Flumine install as I (wrongly) thought that `[speed]` was not compatible as it's not the default version. I prefer Linux but occasionally develop on a Windows machine as it has work related software that is not available on other OS's. Is it worth installing `[speed]` on Windows, or is not incompatible/too much hassle?

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

## 2022-08-22 09:21:31 - general channel

**mandelbot**

Is this still relevant?

```Installing betfairlightweight[speed] will have a big impact on processing speed due to the inclusion of C and Rust libraries for datetime and json decoding.```

---

## 2022-08-21 09:39:48 - strategies channel

**Mo**

To be clear I am live trading the strategy just backing



Whether to just move on is an interesting question of how to prioritise the infinite possibilities of what to work on. And perhaps more importantly, whether trying to solve the mystery of the poor laying performance is mainly just an intellectual exercise rather than a profitable one

---

## 2022-08-19 08:58:25 - random channel

**mandelbot**

well if anyone's interested I ended up going for a [https://www.amazon.co.uk/WD_BLACK-Battlefield-Bundle-speeds-3600MB/dp/B0989X548R/ref=sr_1_3?crid=HJVDEJZY2P23&amp;keywords=wd+black+sn750&amp;qid=1660895871&amp;sprefix=wd+black+sn750%2Caps%2C76&amp;sr=8-3|WD_BLACK SN750](https://www.amazon.co.uk/WD_BLACK-Battlefield-Bundle-speeds-3600MB/dp/B0989X548R/ref=sr_1_3?crid=HJVDEJZY2P23&amp;keywords=wd+black+sn750&amp;qid=1660895871&amp;sprefix=wd+black+sn750%2Caps%2C76&amp;sr=8-3|WD_BLACK SN750) + ACASIS enclosure

---

## 2022-08-15 14:24:17 - strategies channel

**Mo**

The bets range across the entire price ladder and the performance is equally bad in all regions of it

---

## 2022-08-15 10:42:33 - strategies channel

**Mo**

&gt; So could you just have other players beating you to the lay side - all your good bets there simply aren't matching?

Could be - seems strange that would apply to one side only. I can test this by reducing my simulated bet latency and seeing how the results change

---

## 2022-08-13 19:06:49 - strategies channel

**Peter**

Flumine is designed to handle multiple strategies and if they're targeting the same markets it normally makes sense to run them on a single process.



When it won't usually make sense is when the markets are different, e.g. don't mix football and horse racing, or if you have a strategy that is very CPU intensive and may slow up the responsiveness of other strategies.



I think it's pretty normal also to keep data collection separate.

---

## 2022-08-12 09:09:10 - issues channel

**Evaldas**

So, I'm logging order placement latency with `order.responses.date_time_placed - order.date_time_created` For place orders this is as expected around 200ms, but replace orders are always less than 1ms, which is obviously not correct. What I'm doing wrong?

---

## 2022-08-11 19:03:48 - strategies channel

**birchy**

For those of you with profitable strategies, how often do you all have to carry out maintenance or "tweak" settings/signals/etc? Personally I have one particular strategy that was my first live one with Flumine that's been untouched for ~2 years now. It's nothing adventurous but has been slowly ticking along and in recent months has performed exceptionally well. No doubt there will be an equal downturn at some point....

---

## 2022-08-11 09:44:27 - strategies channel

**liam**

FYI that delay includes the inplay delay if present and network/match latency which you can adjust in the [https://github.com/betcode-org/flumine/blob/fd527626accbddd7782477f420855f57e928dae9/flumine/config.py#L25|config](https://github.com/betcode-org/flumine/blob/fd527626accbddd7782477f420855f57e928dae9/flumine/config.py#L25|config)

---

## 2022-08-08 11:32:14 - strategies channel

**thambie1**

It's much easier to to grow an already working but small scale strategy than to start a new one. It really depends on what you're existing strategy is, and whether there's room for growth. Bet sizing, latency, and modifications to the strategy can all be potential options. That being said, if you do decide to go down a completely different rabbit hole, I would pursue option #2. It's still very hard, but easier than #3, and more likely to be a stable competitive advantage compared to #1.

---

## 2022-08-08 11:20:44 - strategies channel

**Alessio**

Monday morning curiosity. I have now a few things that work-ish a bit (my understanding is that ~3% profit on average is within expectations, but they are not scaling at the moment). The ways i feel i could continue exploring are more or less three axes: (1) low latency -- try to acquire fresher data and try to be earlier than others, but do not try to get "better" odds, just get to them earlier  --,  (2) more high precision strategies that try to figure out when odds are missing a piece of information or (3) simple strategies with complex fundamentals that run frequently  -- try to get better at pricing than BF, and any time there's mis-pricing, just enter/exit the market.  I don't do scalping, is boring and not enough liquidity :)

My feeling is that on the downside (1) has intrinsic limits unless you go for expensive data at some point, but may be very fruitful;  (2) looks like the simplest to go forward, but has the risk of black swan events and (3) is probably an endless pit unless you have a team of 4 working on it or stuff like that.

Is there some common wisdom or common ways to understand what's best? Or personal experience you guys want to share (within the limits of not telling, of course) ?

---

## 2022-08-07 13:07:13 - general channel

**PeterLe**

Im using an MP600 PCIe, eitherway Im happy with the backtest speed, 6 mins to test that many is superfast , In the time I can make a brew, i can discover another losing strategy :grinning:

---

## 2022-08-07 08:49:36 - general channel

**birchy**

Also, make sure your files are local rather than on S3 as pulling from S3 will add network latency.

---

## 2022-08-07 08:45:50 - general channel

**foxwood**

There's a nice multiproc example in the flumine performance docs but if you want to get in deep then [https://docs.python.org/3/library/multiprocessing.html](https://docs.python.org/3/library/multiprocessing.html)

---

## 2022-08-04 13:44:06 - general channel

**John Foley**

Been thinking about this as well recently - a half-baked idea I had was to try using [https://github.com/mlflow/mlflow|mlflow](https://github.com/mlflow/mlflow|mlflow). It's designed for a very similar situation where you’re training hundreds or thousands of ML models, all with different parameters, and need a flexible way to attach performance metrics to each run. Definitely might be overkill though.. 

---

## 2022-08-04 07:30:36 - general channel

**Mo**

Does anyone have any tips for organising backtest results? The output of my backtests is one file per event so each backtest occupies a single directory. I'm currently distinguishing between the different parameters used in each backtest in the directory name but this is quickly becoming unwieldy as I add more parameters and it's hardly the best way to encode this information. For example:



```.../backtests/results-new-min-roi-0.0-max-roi-120.0-max-price-1000-bankroll-10000-bet-latency-100ms-cooldown-20000ms-entire-race-with-tags```

I'm thinking of having some kind of "meta file" in each backtest directory that could contain these parameters and other useful information for example:



```{

    "git_commit": "00e8402a7395de0b91d24a2fa15953a9f3271dca",

    "number_of_events": 19214,

    "event_status_breakdown": {

        "SUCCESS": 12007,

        "ERROR": 43,

        "MISSING_DATA": 7167

    },

    "parameters": {

        "min_roi": 0.0,

        "max_roi": 120.0,

        ...

    },

    "profit": -143762.12,

    ...

}```

and/or possibly have a top-level index of the backtests, either in a flat file or SQLite database and then the directories can have uninformative names like "00000043" or "cc097b8048064a3acd969de313e52f9b3fd896c7"

---

## 2022-08-03 08:50:16 - strategies channel

**liam**

from memory it's a big change in the streaming backend to make it work, must be asked for a lot though as it is very annoying...

---

## 2022-08-02 08:22:17 - strategies channel

**liam**

How quickly do you need the information? If it doesn't require any long requests you can put it in middleware instead and use the `add_market` function which is called when a market is added but this is in the main queue so would cause latency issues. If you use a worker to just set it to 60s? and check for new markets, I imagine a delay of 60s on new markets isn't a problem?

---

## 2022-08-01 10:53:00 - strategies channel

**Mo**

Some thoughts:



1. SVM is an odd choice; if you want state of the art then use XGBoost. If you want simplicity, speed, ease of implementation and a method that has stood the test of time then use Logistic Regression

2. I'm not sure about including starting odds - you mention form, speed, rating: all of these will already be incorporated into the odds. So it will come down to whether there is any marginal value in your "own inputs" over and above the odds

3. Another downside to starting odds is they are only available when the race starts. Typical setup for a pre-race strategy would be to use the starting odds (implied probabilities) as the target for your model rather than binary win/loss

4. I think you're thinking along the right lines with what I'll summarise as "truncated finishing positions" although I still think just using the implied probabilities from the starting odds would be way better

---

## 2022-07-31 23:44:21 - strategies channel

**Troy Edwards**

Hi all long time since chatting.  I have been trying some strategies with Aussie and NZ greyhound racing and still don't have an edge yet.  So back to learning and I have come across SVM - Support Vector Machine regression tool which I want to apply to greyhound data.  Some of the X inputs will be form, speed, rating, starting odds etc and some of my own inputs.  However for the Y inputs which are the results, should I enter say 1 (True) for the winner and then -1 (False) for the other 7 runners?  OR should I enter the actual finishing positions 1 thru 8?    I am wondering if training the model with positions 1-8 may introduce errors OR be too difficult?  I was also thinking I could just set positions 1-3 True and everything else False as most of my strategies are for Lay bets?   I  have started any coding yet for the model but am going to use Accord.MachineLearning.VectorMachines.Learning in the .NET library.

---

## 2022-07-29 14:23:45 - issues channel

**liam**

Out of memory, hard to debug without knowing what is running on the box or if it's the python process itself that has a leak, login at 10:20 and monitor will tell you straight away 

---

## 2022-07-29 13:24:31 - issues channel

**mandelbot**

My strategies keep getting killed around the same time (10:23. Any idea why this might be the case?

```

[Fri Jul 22 10:23:45 2022] Out of memory: Killed process 23407 (python) total-vm:1645160kB, anon-rss:545988kB, file-rss:0kB, shmem-rss:0kB, UID:1000 pgtables:1588kB oom_score_adj:0

[Sat Jul 23 10:23:59 2022] Out of memory: Killed process 3568 (python) total-vm:1614732kB, anon-rss:584060kB, file-rss:0kB, shmem-rss:0kB, UID:1000 pgtables:1660kB oom_score_adj:0

[Fri Jul 29 10:23:44 2022] Out of memory: Killed process 28699 (python) total-vm:1633308kB, anon-rss:515668kB, file-rss:0kB, shmem-rss:0kB, UID:1000 pgtables:1524kB oom_score_adj:0```

---

## 2022-07-29 10:19:28 - issues channel

**George**

When streaming market data I am getting a few messages saying "Latency high: [tel:06334546432|0.](tel:06334546432|0.)xxxx". They seem to come in a burst lasting a couple of milliseconds. Is that normal or is there something I could do to avoid it?

---

## 2022-07-28 17:23:17 - random channel

**Mick**

Not streaming - I don't think I need the high speed stuff. I'm betting hours before the off.

---

## 2022-07-27 13:24:33 - issues channel

**birchy**

[@UVB1RFEP5](@UVB1RFEP5) as [@UBS7QANF3](@UBS7QANF3) has said, understanding how Linux works is the biggest barrier but nowadays that's not a particularly steep learning curve. It would probably be worthwhile you playing around with Ubuntu by either installing on your machine as a dual boot or on an old pc/laptop/rasp pi. You can also boot most Linux's as a "live" image that runs off cd/dvd/usb stick without installing anything. They run as a full OS in ram but can be a bit slow as a result, however, it allows you to assess a Linux session without making any permanent changes. Alternatively, you could dive straight into an AWS Lightsail instance and learn how to administer it over SSH as that's what your end goal is. [@UQL0QDEKA](@UQL0QDEKA) has done this recently and said he found it much easier than expected and now has a handful of strategies running remotely.

---

## 2022-07-26 15:52:04 - issues channel

**CL**

See eg here - [https://stackoverflow.com/questions/30418886/how-and-why-does-quickedit-mode-in-command-prompt-freeze-applications](https://stackoverflow.com/questions/30418886/how-and-why-does-quickedit-mode-in-command-prompt-freeze-applications). If you disable quick edit you should be fine. From memory Mo this happens if you launch via other means as it is a cmd.exe thing - if there is a visible process window then it can hang if you click in it.

---

## 2022-07-26 11:39:27 - issues channel

**JFP**

Just wondering if someone could explain an issue I've been having with my automation over the past couple of weeks.

I turn my program on for the day via a text editor which contains my script, the python window pops up and I see all the races load up as normal. When I check in at end of day, I find that no bets have been placed, the dialog in the python window has not changed since I left it. When I hit enter, the python window dialog box is filled with a stream of high latency messages. It appears as though it somehow gets paused, has anyone experienced this?

Have been running the same program for months with no issues, but over the past 2 weeks this has happened 3 times. Am using Flumine 1.21.6.

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

## 2022-07-21 00:06:32 - general channel

**Jonjonjon**

It's hard to give exact figures as we all run different code. But when I upgraded my PC a couple of years ago, relative passmark scores (between my old and newer PC) were a reasonable indication of the relative performance for Flumine backtesting.



[https://www.cpubenchmark.net/high_end_cpus.html](https://www.cpubenchmark.net/high_end_cpus.html)

---

## 2022-07-19 08:09:41 - strategies channel

**Mo**

[https://betcode-org.github.io/flumine/performance/#file-location](https://betcode-org.github.io/flumine/performance/#file-location)

---

## 2022-07-17 20:10:21 - general channel

**thambie1**

That specific change (though in a different language) is on my todo list to speed up my backtest. Doesn't matter much in production though

---

## 2022-07-17 13:09:04 - general channel

**Dave**

Maybe not much when the bottlenecks really are in network latency/in play delay/matching cycle itself.

---

## 2022-07-17 11:18:48 - random channel

**birchy**

Plus you get much improved latency, which will likely increase increase profit/loss.

---

## 2022-07-16 21:15:09 - issues channel

**D**

The files may be larger but is the performance better or worse? I don't know but I don't think the answer is obvious. Anyway, birchy’s method sounds like a better approach.

---

## 2022-07-16 15:59:47 - issues channel

**birchy**

There's going to be latency writing direct to S3. Far better to save locally and then copy or move to S3 on a separate process.

---

## 2022-07-16 11:31:23 - issues channel

**Jonjonjon**

Afraid I've never used S3, so I can't comment on the performance of writing to it.

---

## 2022-07-16 09:15:52 - issues channel

**Rudeger Jamison**

Although each file atm seems to be one markets worth of orders.... I'm not exactly sure. Clutching at straws a bit. I have 4gb of memory and 1 vcpu.

---

## 2022-07-14 09:54:41 - random channel

**Newbie99**

I effectively just copied this:



[https://betcode-org.github.io/flumine/performance/#multiprocessing](https://betcode-org.github.io/flumine/performance/#multiprocessing)



and this:



[https://github.com/betcode-org/flumine/tree/master/examples/middleware](https://github.com/betcode-org/flumine/tree/master/examples/middleware)



In terms of approach I don't think I've changed anything (other than the odd bit of formatting etc.)

---

## 2022-07-14 09:28:52 - random channel

**Newbie99**

I use the market catalogue middleware example when backtesting and it all works fine:



[https://github.com/betcode-org/flumine/blob/master/examples/middleware/marketcatalogue.py](https://github.com/betcode-org/flumine/blob/master/examples/middleware/marketcatalogue.py)



However, when self recording, the market catalogues are saved as a .json.gz, so if I run the following in a standalone script:



```mc_path = '/1.200396929.json.gz'



with open(mc_path, "rb") as r:

    data = gzip.GzipFile(fileobj=r).read()

    catalogue_json_data = json.loads(data)

    print(catalogue_json_data)```

As expected it returns:



```{'marketId': '1.200396929', 'marketName': 'Over/Under 2.5 Goals', 'marketStartTime': '2022-06-22T16:00:00.000Z', 'description': {'persistenceEnabled': True, 'bspMarket': False, 'marketTime': '2022-06-22T16:00:00.000Z', 'suspendTime': '2022-06-22T16:00:00.000Z', 'bettingType': 'ODDS', 'turnInPlayEnabled': True, 'marketType': 'OVER_UNDER_25', 'regulator': 'GIBRALTAR REGULATOR', 'marketBaseRate': 2.0, 'discountAllowed': False, 'wallet': 'UK wallet', 'rules': '&lt;!--Football - Over/Unders --&gt;&lt;br&gt;How many goals will be scored in this match.&lt;br&gt; All bets apply to Full Time according to the match officials, plus any stoppage time. Extra-time/penalty shoot-outs are not included.&lt;br&gt;&lt;br&gt;&lt;/b&gt;For further information please see &lt;a href=[http://content.betfair.com/aboutus/content.asp?sWhichKey=Rules%20and%20Regulations#undefined.do](http://content.betfair.com/aboutus/content.asp?sWhichKey=Rules%20and%20Regulations#undefined.do) style=color:0163ad; text-decoration: underline; target=_blank&gt;Rules &amp; Regs&lt;br&gt;&lt;br&gt;\n', 'rulesHasDate': True, 'priceLadderDescription': {'type': 'CLASSIC'}}, 'totalMatched': 35.4, 'runners': [{'selectionId': 47972, 'runnerName': 'Under 2.5 Goals', 'handicap': 0.0, 'sortPriority': 1, 'metadata': {'runnerId': '47972'}}, {'selectionId': 47973, 'runnerName': 'Over 2.5 Goals', 'handicap': 0.0, 'sortPriority': 2, 'metadata': {'runnerId': '47973'}}], 'eventType': {'id': '1', 'name': 'Soccer'}, 'competition': {'id': '4051', 'name': 'Norwegian Cup'}, 'event': {'id': '31543907', 'name': 'Strindheim v Kristiansund', 'countryCode': 'NO', 'timezone': 'GMT', 'openDate': '2022-06-22T16:00:00.000Z'}}```

However, if I try to adapt the middleware code as follows:



```class MarketCatalogueMiddleware(Middleware):

    def add_market(self, market) -&gt; None:

        try:

            zipped_catalogue_file_path = str(get_mc_folder(market, zipped_folder_path))

            catalogue_file_path = os.path.join(MARKET_CATALOGUE_PATH, market.market_id + '_market_catalogue.json')

            if zipped_catalogue_file_path is not False:

                if os.path.exists(zipped_catalogue_file_path):

                    with open(zipped_catalogue_file_path, "rb") as r:

                        data = gzip.GzipFile(fileobj=r).read()

                        catalogue_json_data = json.loads(data)

                        print(catalogue_json_data)```

Then I just get the following error:



```Exception 'int' object has no attribute 'startswith' occured on market 1.200522372```

If I use a different approach, as follows:



```class MarketCatalogueMiddleware(Middleware):

    def add_market(self, market) -&gt; None:

        try:

            zipped_catalogue_file_path = str(get_mc_folder(market, zipped_folder_path))

            catalogue_file_path = os.path.join(MARKET_CATALOGUE_PATH, market.market_id + '_market_catalogue.json')

            if zipped_catalogue_file_path is not False:

                if os.path.exists(zipped_catalogue_file_path):

                    with gzip.open(zipped_catalogue_file_path, 'rb') as fin:

                        catalogue_json_data = json.loads(fin.read().decode('utf-8'))

                        market.market_catalogue = MarketCatalogue(**catalogue_json_data)```

Then I get the following error:



```Exception Not a gzipped file (b'{"') occured on market 1.199593125```

Now of course, I can get around this by unzipping the files first, but I feel I must be missing something obvious here, why can I unzip into memory from a static script, but not via middleware, I presume there is a logical reason and whilst it doesn't matter as there is an obvious alternative approach, I would like to understand why this doesn't work if possible?

---

## 2022-07-08 20:35:54 - random channel

**Jonjonjon**

[@UBS7QANF3](@UBS7QANF3) What's so great about Chat With Traders? I used to listen to it, but most of the interviewees were the delusional types who think that a positive mental attitude will make you a winning trader. I don't see how my mindset affects the performance of Python betting scripts?



The worst was a guy who thought that any strategy would win with the correct mindset. Suppose you ran the same Python script as me. Suppose you think it's great and I think it's nonsense. Would that make the script perform better for you?

---

## 2022-07-02 13:18:25 - strategies channel

**birchy**

[@U01A64T6DJQ](@U01A64T6DJQ) 

As [@USYQKE5HN](@USYQKE5HN) has said, keep it simple. Getting matched at value prices is a bigger issue than generating probabilities. First thing I would do is run a simple simulation where you assume that you had 100% of your bets matched at your generated prices Vs actual win/lose outcomes. That will tell you how your prices compare to real world results and should generate a profit/loss close to zero if your model is well calibrated.



Assuming the above generates expected results, THEN you can run backtests in Flumine:

`if betfair_available_price &gt; my_price:

    side = 'BACK'

if betfair_available_price &lt; my_price:

    side = 'LAY'`

The Flumine simulation engine will give you a good approximation of which bets will get matched, which ones won't and a simulated "real world" profit/loss which will hopefully be &gt; 0. You should also calculate the "what if I bet at BSP instead" profit/loss, where you replace the simulated matched price with BSP, keeping the matched amount the same. If the BSP performance is better, it's back to the drawing board.



FYI: The above assumes straight betting and no greening/hedging nonsense.

---

## 2022-06-30 21:28:30 - strategies channel

**Tom Cannon**

My predictions of price movement is only accurate for a short period of time. I've found I can rarely get matched on the correct side before the price moves.



I've been working with UK horse-racing and filtering by a over a certain matched to ensure fluidity.



I'd take any to be honest, it's all just data to me - as long as it's descriptive enough to predict value. I took a look at Total performance data but couldn't find any prices or many reviews if this service was worth it.

---

## 2022-06-29 13:45:00 - general channel

**Wayne**

Thank you, and I do appreciate the feedback - not that my word counts for anything on here but I promise this is real. I consult for most of the established trading firms globally. The salaries on the low latency focussed dev roles are not much different to those in finance nowadays

---

## 2022-06-29 12:54:11 - general channel

**Wayne**

Hey all, I hope this posting is best placed in the general channel.



I am helping to scale a trading syndicate, so far they have a team of 17 quants and quant devs and focus on football and horse racing - it is not all Betfair focussed. Looking to hire developers with experience and interest trading sports – that led me here.



The client uses a mix of low latency and value-based approaches, latency is quite key to some strategies they run so C++ experience is a big plus. Compensation will consist of base salary, guaranteed bonus for the first year (team profit share after) and a sign on bonus to compensate for any strategy you have running currently. As a guide, dependent on experience base salary can range from £110-200k (huge range I know this is not helpful).



Let me know if you're interested in hearing more! Or let me know if this is not the right place for this message and I will not reoffend!

---

## 2022-06-29 09:11:32 - general channel

**EJono**

is there a reliable way of determining if a football event will have score data through the inplayservice api pre kick off? Secondly is anyone aware of the reliability of the score feed? For instance does it seem like the scores have a latency of ~1-2 minutes from moment of the goal (or other score feeds), are incorrect scores to be expected every 100 or so games, are small games given less attention than those with high traded volumes? etc - just peoples general experience of how useful the score feed from the inplay service actually is or if they try and avoid it in favour of other sources

---

## 2022-06-27 10:16:50 - random channel

**Newbie99**

Is there a neater way of removing latency warnings when using the market recorder than changing the MAX_LATENCY value in the basestream.py file (for Flumine)?

---

## 2022-06-24 16:47:36 - issues channel

**Aaron Smith**

Hi ppl!

I m trying to extract bsp (and result) from historic streaming files. Here is what i do:



```def get_selection_id_to_result(trading, streaming_file: str) -&gt; dict:

    stream = trading.streaming.create_historical_generator_stream(

        file_path=streaming_file,

        listener=StreamListener(

            max_latency=None, update_clk=False,

        ),

    )

    with patch("builtins.open", smart_open.open):

        g = stream.get_generator()

        selection_id_to_result = {}

        for market_book in g():

            market_book = market_book[0]

            if market_book.status == 'OPEN':

                continue

            for rb in market_book.runners:

                if rb.selection_id not in selection_id_to_result:

                    selection_id_to_result[rb.selection_id] = {'bsp': float('nan'), 'result': ''}

                sp = get_sp(rb)

                if isinstance(sp, float):

                    if not math.isnan(sp):

                        selection_id_to_result[rb.selection_id]['bsp'] = round(sp, 3)

                selection_id_to_result[rb.selection_id]['result'] = rb.status



    return selection_id_to_result```

`get_sp`  is liams function from flumine/utils.

Mostly it works, but sometimes it doesnt get the sp even though there is one. Does anyone have an idea what could be causing this?

---

## 2022-06-22 12:39:20 - strategies channel

**nthypes**

Let's suppose that you found a model that his accuracy is equal to the BSP. What are your thoughts on the best strategy to exploit this model? Looks like that a simple BACK if odds are above the predicted value has a poor performance/high variance.

---

## 2022-06-21 22:02:44 - random channel

**liam**

Yeah I keep an eye on CPU, book processing time and place/cancel latency 

---

## 2022-06-21 22:01:30 - random channel

**Unknown**

Hmmm... I hadn't considered latency. My CPU% on a dual core machine looks like this, running 5 Flumine instances, one of which is at close to 100 strategies. I don't have much time to monitor this so am not too keen spinning up another machine if I can avoid it.

---

## 2022-06-21 21:56:40 - random channel

**birchy**

However many it takes to get to the CPU running at 99%? :grinning: 

Serious answer...depends on how much computing each strategy uses. I don't think there's a limit in flumine other than CPU limitations, particularly on AWS. I guess latency would be the key metric?

---

## 2022-06-18 17:32:29 - general channel

**Unknown**

*Update*: Looks like that is related with this [https://github.com/betcode-org/betfair/blob/e3d36f67d5291faa8e7ac85c061631b0dd722091/betfairlightweight/streaming/cache.py#L262|code-line](https://github.com/betcode-org/betfair/blob/e3d36f67d5291faa8e7ac85c061631b0dd722091/betfairlightweight/streaming/cache.py#L262|code-line). Looks like that is intended to make it faster and using `Available` class for that. Because when there is market change and we print that in [https://github.com/betcode-org/betfair/blob/e3d36f67d5291faa8e7ac85c061631b0dd722091/betfairlightweight/streaming/cache.py#L247|here](https://github.com/betcode-org/betfair/blob/e3d36f67d5291faa8e7ac85c061631b0dd722091/betfairlightweight/streaming/cache.py#L247|here), we can see all "trd" information. So that is available but for speed reason, that is disabled. Are there any way to enable full log via _streaming module_ or is it not possible? Also I can create a github issue if that is preferable.

---

## 2022-06-13 03:41:25 - general channel

**Unknown**

Anyone been getting really bad latency issues recently? Yesterday my latency was at 1 second today when I checked its hitting 4s :disappointed:

---

## 2022-06-10 14:24:48 - issues channel

**EJono**

Sorry liam this may be a dead I do not have the raw data just the timestamps of the PMB execution time and some custom teritary logs ie market_book latency, market suspended status, runner_exposure, back&amp;lay prices

---

## 2022-06-07 13:27:21 - random channel

**liam**

[https://betcode-org.github.io/flumine/performance/#multiprocessing](https://betcode-org.github.io/flumine/performance/#multiprocessing)

---

## 2022-05-31 15:52:08 - random channel

**liam**

[https://www.totalperformancedata.com/blog/2022/5/31/a-day-in-the-life-of-a-tpd-operator|A day in the life of a TPD operator](https://www.totalperformancedata.com/blog/2022/5/31/a-day-in-the-life-of-a-tpd-operator|A day in the life of a TPD operator) 

---

## 2022-05-20 11:09:03 - general channel

**mandelbot**

Can I expect a latency bump from running on a linux box vs windows? Just switched :nerd_face:

---

## 2022-05-20 10:36:08 - random channel

**Alex Alex**

I have tried it recently. I have to say it is a bit of a mixed bag. Yes, it saves a ton of time with boilerplate code and some of the stuff it writes is really amazing. But then other times it writes code that looks ok but doesn’t quite do what I intended it to do, so I end up fixing the code which tends to end up slower than just writing it correctly in the first place. It’s still super amazing to see it work and it is 1000x more useful than I first thought it was.

---

## 2022-05-20 08:23:42 - issues channel

**liam**

What is the latency? Are you placing a lot of orders? Average bet delay you are dealing with?



I bump to 64 anyway



```from flumine import config



config.max_execution_workers = 64```

---

## 2022-05-20 07:17:24 - issues channel

**Mike Breen**

Hi There - I am running two strategies on an ECS Service in Ireland with 2 vCPU and 8Gb Memory and I am getting loads of `WARNING` logs saying :



```High latency between current time and OrderPackage creation time, it is likely that the thread pool is currently exhausted - "thread_pool": {"num_threads": 26, "work_queue_size": 0}```

Is this expected - I thought this would be a minimal number of strategies to cause such an issue?

---

## 2022-05-12 11:59:35 - general channel

**Nicholas vizard**

Hey guys, bit of a left-field question here. I was wondering if anyone knew were to find aggregate stats on betfair's recent general performance, particularly relating to their importance in the betting landscape.



For example, things like what was the total traded volume through betfair in 2021? How many sports did betfair cover? How many markets were run in 2021? etc. Just looking to do a brief right up of the importance of betfair and any help would be much appreciated.



Cheers,

Nick

---

## 2022-05-11 10:04:34 - issues channel

**Jorge**

```2022-05-10 11:27:31,751 | WARNING | a | a | [MarketStream: 1002]: Latency high: 6.878550052642822

2022-05-10 11:27:31,752 | WARNING | a | a | [MarketStream: 1002]: Latency high: 6.872628688812256

2022-05-10 11:27:31,753 | WARNING | a | a | [MarketStream: 1002]: Latency high: 6.8602306842803955

2022-05-10 11:27:31,753 | WARNING | a | a | [MarketStream: 1002]: Latency high: 6.777828693389893```

---

## 2022-05-11 09:32:18 - issues channel

**liam**

Which latency messages are you getting? Can you share as there are two types

---

## 2022-05-11 09:21:23 - issues channel

**Jorge**

```def _calc_latency(publish_time: int) -&gt; float:

    return time.time() - publish_time / 1e3```

Isn't it ms?

---

## 2022-05-11 09:17:35 - issues channel

**Jorge**

It is randomly increasing in value. I see latency is measured in ms. What does a latency of 10 exactly mean? Does it just mean I get prices 10ms later than they are published?

---

## 2022-05-11 07:28:49 - issues channel

**liam**

If the latency is constant then it’s probably a clock issue, if it increases in value it’s a CPU and if it does the latter but randomly it’s probably CPU but is then recovering Ie. The load is not constant 

---

## 2022-05-11 07:17:12 - issues channel

**Jorge**

How can I know if the "Latency high" messages that are accumulating are due to not having enough CPU's in my VM?

---

## 2022-05-10 17:06:13 - issues channel

**Jorge**

Hi, has anyone experienced "Latency high" messages accumulating today?

---

## 2022-05-10 16:13:17 - random channel

**Mo**

```stream = trading.streaming.create_historical_generator_stream(

    file_path=path_to_prices_file,

    listener=StreamListener(

        max_latency=None, lightweight=lightweight, update_clk=False, **kwargs

    ),

)

with patch("builtins.open", smart_open.open):

    g = stream.get_generator()

    for market_book in g():

        pass```



---

## 2022-05-06 18:20:17 - general channel

**Kunal Maneck**

How is the latency of sportmonks feed? 

---

## 2022-05-06 13:32:14 - general channel

**Graham**

I wouldn’t be surprised to hear they are reselling official feeds with latency which renders it useless for bet placement 

---

## 2022-05-06 13:24:27 - general channel

**Peter**

I use them. Data quality is pretty good and they're super-responsive to corrections in their historic data.



I don't know what the delay is, but I would expect it to be somewhat variable depending on the speed of the feed the data analysts receive, how far ahead of the "live" broadcast they are receiving it, how much of the encoding is automated and how quickly specific analyst is able to encode the non-automated events. Overall however, I would expect it to be dwarfed by the impact of polling for new data.



I'm not aware of a mapping between Betfair team names and Sporting Monks. I've done that myself but found a fair number of inconsistencies in team names on the Betfair making, even in major competitions, rendering a mapping a bit problematic. My preference instead is to use fuzzy logic on the team names to find best matches. I've found that more reliable (i.e. less brittle).

---

## 2022-05-06 08:58:56 - issues channel

**Oliver Varney**

the Side enum implementation is quite nice tbh with all the helper attributes, not sure if that would effect performance if flumine implemented that directly as the side

---

## 2022-05-04 19:59:21 - issues channel

**foxwood**

Loads of latency issues recorded in logs on the market stream today at 2 different locations and different strategies - up to 15 seconds at times and then recovers - anybody else ?



Edit - 50 even ?!

Saw something similar the other day and thought it was just local connection issue

```{"asctime": "2022-05-04 18:04:15,828", "levelname": "WARNING", "message": "[MarketStream: 2001]: Latency high: 13.703663110733032"}

{"asctime": "2022-05-04 18:04:15,875", "levelname": "WARNING", "message": "High latency between current time and MarketBook publish time", "market_id": "1.198672766", "latency": 50.026501417160034, "pt": "2022-05-04T17:03:25.849000"}```

Edit 2 - that PC was saving it's log to a NAS over wifi - very slow. Think a race developed between trying to log latency warnings and taking so long to do so it increased the latency more ! Switched to local PC now instead which will hopefully fix things.

---

## 2022-05-04 17:11:23 - random channel

**VT**

Has anyone noticed differences in latency in the last 2 days? Here in Brazil it is high.



Latency: 2.8783345222473145

---

## 2022-05-04 08:02:29 - general channel

**Jonjonjon**

I run over 50 on a single python instance. I haven't tracked latency, but it (along with 3 other Flumine scripts) uses 30-80% CPU utilisation on a dual CPU cloud machine

---

## 2022-05-04 07:22:48 - general channel

**liam**

Very strategy dependant, if you are getting latency warnings then you have gone way too far 

---

## 2022-05-04 01:16:11 - general channel

**Rudeger Jamison**

Hey - is there a general strategy limit that is known to slow down Flumine?



eg. Is there any advice to run one instance of Flumine with say 5 strategies or is it resilient enough to  use with say 30 strategies +?



I can test this out myself, just thought you guys would have experience with this already. Cheers

---

## 2022-05-03 21:05:37 - general channel

**liam**

Lightweight mode won’t work in flumine as it’s designed to use resources however a few things are patched to improve speed (check out the patch file)

---

## 2022-05-03 16:21:30 - issues channel

**D**

What is happening in the function odds_search that's so slow it needs a separate process for each market? Sorry if that's a dumb question but I'm not getting it.

---

## 2022-05-03 16:15:33 - issues channel

**Beginner**

Hi [@URMM9463X](@URMM9463X) thanks to help. Check it out, yesterday I sent the code here without using multiprocessing, it works perfectly because I can send `trading` as an argument without any difficulties. But, it generates a slowness that when using it on a day by day, I confess to you that it ends up getting in the way of making decisions in the market. So, if I could use multiprocessing to collect the information all at once without having to wait for an analysis to finish and move on to another, it would improve a lot for me.

---

## 2022-05-03 11:08:53 - general channel

**Mo**

If you want to compete on latency you shouldn't be using Python 

---

## 2022-05-03 10:02:02 - general channel

**LM**

Is there any way to gauge the actual latency of bet placement to the exchange? Also is there significant improvement using lightweight mode in Flumine streaming to improve latency (obviously is going to be code dependent but I'm only running super simple logic)?

---

## 2022-05-02 18:32:09 - issues channel

**Unknown**

Guys, this code is to analyze if everything is ok in both markets and if it is, it responds with `'Approved to invest'`



This file is called `Betfair.py`, so in my main code I call it like this:



`import Betfair`

`print(Betfair.match_data(31410834))`



This id `31410834` is from an example game that has open markets and everything is ok.



Perfect, you guys who have advanced knowledge in Python and have been using betfairlightweight for a long time... As can see, in this place in the code:



`for _ in range(3):`

        `for _, market in markets.iterrows():`

            `odds_search(trading,market)`



I'm asking to generate a loop for 3 times in the analysis of the filtered markets, calling the `odds_search` function.



It works perfectly, but as you can see, I add the login data to the api (`trading`) when calling the function, but when I try to use basic multiprocessing or pool, I can't send `trading` as an argument, this error appears: `TypeError: cannot pickle 'module' object`.



When someone has some spare time, could help me out and show me how I could edit this code to make it work with multiprocessing so that these 3 loops are done at the same time to increase speed to colect the data?



I can create a question on stackoverflow if want. Any help will be most welcome!

---

## 2022-04-29 20:54:21 - random channel

**Jonjonjon**

It's been fairly mediocre for me this year. I've really tuned up my strategies, but the performance is probably slightly less than where I was by this time last year.

---

## 2022-04-29 11:31:18 - random channel

**liam**

In addition to improving (speed/features/abstractions) flumine the only thing I would do is to abstract the way its used further with a quantopian style web frontend for simulating strategies

---

## 2022-04-29 11:27:26 - random channel

**Alessio**

I guess the next step is to build a company that sells "features" for the models that people want to do this stuff ... that way you are an intermediary, no matter their performance.

---

## 2022-04-29 10:00:50 - random channel

**charlie_v**

[@UUE6E1LA1](@UUE6E1LA1) did some C++ last yes, talk about painful, was coding in .net and the debugger is so darn slow,. code was twice as fast as my C# but they really do not make it easy.

---

## 2022-04-26 08:28:35 - random channel

**liam**

chance its a race condition due to the latency issues

---

## 2022-04-25 11:07:25 - random channel

**Newbie99**

In terms of orders, it can be &gt;1000, however that doesn't seem to be the issue as for 1.182979902 I only have a handful and the latency warnings start almost straight away.

---

## 2022-04-24 13:46:26 - random channel

**Newbie99**

I'm sure this has been asked before, but just wanted to double check as I couldn't find it.



This message simply means the publish time is x seconds ago and that could be because its a slow market (in this case tournament outright winner, which genuinely can go for some time without updates), but doesn't indicate a problem:



```WARNING:flumine.baseflumine:High latency between current time and MarketBook publish time

{"asctime": "2022-04-24 12:41:12,737", "levelname": "WARNING", "message": "High latency between current time and MarketBook publish time", "market_id": "1.182979902", "latency": 61.23844265937805, "pt": "2022-04-24T12:40:11.499000"}```

Whereas this, suggests latency due to code / connection (or some other factor) and could indicate a problem:



```WARNING:betfairlightweight.streaming.stream:[MarketStream: 2001]: Latency high: 0.5573089122772217

{"asctime": "2022-04-24 12:41:50,796", "levelname": "WARNING", "message": "[MarketStream: 2001]: Latency high: 0.5573089122772217"}```

---

## 2022-04-20 10:02:20 - random channel

**Troy Edwards**

Hey guys - I have been storing data in a BINARY file because I had structures within structures.  Today I ran out of memory and I know its time to go to SQL.  So I added a local MDF local database to my Visual Studio, created a table and tested access but I can't get it to work ?



Dim myDataReader As SqlDataReader

Dim myConnection As SqlConnection

Dim myCommand As SqlCommand

Dim strSQL As String



myConnection = New SqlConnection("Data Source=(LocalDB)\MSSQLLocalDB; Initial Catalog=C:\CODE\BETFAIR ARB\PREVIOUS DATA\PreviousRaceData.mdf")

myConnection.Open()



strSQL = "SELECT ID FROM dbo.tblCompletedRaces"

myCommand = New SqlCommand(strSQL, myConnection)



myDataReader = myCommand.ExecuteReader()



If myDataReader.Read() Then

            Debug.Print(myDataReader.Item("Runnername"))

        Else

            MsgBox("Didn't work...")

        End If

Any ideas :disappointed:

---

## 2022-04-19 18:20:20 - general channel

**Michael**

Ok. Personally I would focus on that. You don't want to be carpet bombing the exchange if you can help it.



One thing that you've done well is played a long game and hung in there - don't let that go. Stay patient and work out where your winnings are coming from.



You might find yourself tempted to try to jack up your betting in the hope that you'll win more that way - you won't.



Take your time, build slowly and drive up the average profit of your transactions. Go for the robust long term operation, not the short term win.

---

## 2022-04-19 16:04:31 - general channel

**AndyL**

I have a separate Flumine python process for each strategy at the moment. Surprisingly cpu usage is quite low, memory good, so mainly network bound

---

## 2022-04-14 15:07:28 - general channel

**foxwood**

£2k pd remote working for this sort of stuff imho and if you really want minimum latency it needs to be C/C++ with asm as well. Oh, and a piece of the action :grin:

---

## 2022-04-14 14:34:39 - general channel

**D C**

Do people really use Python for low latency trading?

---

## 2022-04-14 14:16:18 - general channel

**ShaunW**

One missing thing [@UPCC7TU8L](@UPCC7TU8L), wages?   As a guide my brother-in-law is in low latency financial trading development and makes £750 a day.

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

## 2022-04-13 08:57:32 - issues channel

**Jorge**

It may be my crappy server provider, I also observed higher "Latency high" logs in general

---

## 2022-04-13 08:54:39 - issues channel

**liam**

What do the logs look like before it crashes? I can confidently say it won't be bflw causing this, whats the memory use of redis?

---

## 2022-04-13 08:23:15 - issues channel

**Jorge**

Hi, my streaming_market_data process is suddenly using a lot of memory RAM. For the first couple of days it is completely OK but then suddenly it starts accumulating more RAM and in a couple of days it takes all the available RAM in the Server, making the process freeze. Yesterday it took 80MB RAM (normal) and today it went up to 250MB RAM. Has anyone experienced something similar? This is basically my code for the process:



```trading = betfairlightweight.APIClient(... , lightweight=True)

trading.login()



market_filter = streaming_market_filter(event_type_ids=event_type_ids, market_types=market_type_codes, turn_in_play_enabled=True, country_codes=country_codes)

market_data_filter = streaming_market_data_filter(fields=["EX_BEST_OFFERS_DISP", 'EX_TRADED_VOL', "EX_MARKET_DEF"], ladder_levels=1)

streaming = Streaming(trading, market_filter, market_data_filter)

streaming.start()



while True:

    try:

        new_market_books = streaming.output_queue.get()

        publish_to_redis(db_0, new_market_books)

        log_debug('Total markets saved in Redis: {}'.format(len(db_0.keys())))



    except Exception as e:

        log_exception(e)```

I don't see any ERROR logs. Only some WARNINGs here and there about "Latency high", but I had those long time ago and the same process did not accumulate RAM memory...

---

## 2022-04-08 15:45:06 - general channel

**Rob**

currently no, both to the mutability, and construction. Adding mutability is actually pretty hard, if you change a ladders values, then you will break future updates that depend on that ladder, and any other change (times/strings/etc) will be ignored and replaced next time the parser spots a difference anyway. The only real way to do it would be to copy the object and mutate the copy, and once you’re paying the price of a deep copy you’re probably best just copying into a new python class that you can control.



As for constructors I’ll need to do research on the benefits. If using my ‘native’ objects is way faster, then I’ll probably add them, but I suspect it wont be any faster then just making your own python class - which would also be a lot more flexible.  I honestly dont know tho, so will need to do some benchmarking. If my objects are slower/(or just not substantially faster) and are also less flexible, then I dont know if theres really much point adding constructors.

---

## 2022-04-08 15:21:56 - general channel

**Oliver Varney**

Ive been playing around with it and the performance is very impressive. Maybe be worth noting that you cant change market_book attributes (unless rob has changed anything in the recent pushes or my settings are wrong), i.e. adjusting old market_book etc

---

## 2022-04-08 13:59:47 - general channel

**liam**

Just pushed a [https://github.com/betcode-org/flumine/pull/577|branch](https://github.com/betcode-org/flumine/pull/577|branch) to flumine which integrates [@UUX1L88MC](@UUX1L88MC) awesome [https://github.com/tarb/betfair_data|betfair-data](https://github.com/tarb/betfair_data|betfair-data) library, I am seeing a rough 1.5-2x speed increase with no code changes other than the price/size change (now bflw objects)



Few things to cleanup and fairly sure it can be sped up more, going forward I want to see how this can be the default for bflw and fall back to pure python if the library isn't installed but welcome any thoughts on this.

---

## 2022-04-04 15:03:16 - issues channel

**Jon K**

[https://githubmemory.com/repo/liampauling/flumine/issues/487](https://githubmemory.com/repo/liampauling/flumine/issues/487)

---

## 2022-04-03 11:39:20 - random channel

**liam**

Nah, chunk into 8 markets (prevents memory leaks) some code that might help



```chunk = 8

total = len(all_markets) / chunk

for markets in tqdm(chunks(all_markets, chunk), total=int(total)):

    run_process(markets)```



---

## 2022-04-01 10:08:12 - betfair-news channel

**Neil T (Betfair)**

Morning [@UUE6E1LA1](@UUE6E1LA1) - This isn’t something under consideration. The main reasons for this are lack of liquidity, the practicalities of managing it accurately and picture latency. Many greyhound races are largely determined by what happens in the first second or two after the traps open so it isn’t something which lends itself easily to Exchange in-play betting.

---

## 2022-03-29 21:50:49 - issues channel

**Jonjonjon**

I'm still trying to debug the problem of missing bets (I'm getting lots of placed bets in the backtest, but they're not being place when live). After checking my live latency is fine, and then increasing the backtest latency to 1 second (where it still has lots of placed bets) I'm totally flumoxed.:disappointed:

---

## 2022-03-28 08:17:37 - issues channel

**Mo**

You mentioned vCPUs but those are going to be largely irrelevant for a lagging GUI. Network bandwidth/latency is much more important

---

## 2022-03-28 08:14:29 - issues channel

**Unknown**

Just for your reply :grin: Yes I am using a Remote Desktop to connect to a Linux ec2 instance but it’s very slow and lags 

---

## 2022-03-28 08:09:19 - random channel

**Mo**

I doubt you will notice a difference unless you are extremely latency sensitive

---

## 2022-03-28 08:08:12 - random channel

**PeterLe**

just to add; i did some test many years ago on Virtual V Dedicated, using similar specs and the exact same strategy, and then comparing the betids, I found the dedicated to be marginally slower (and more expensive as Mo has stated)

---

## 2022-03-28 07:55:04 - issues channel

**Kunal Maneck**

Any ideas how I can address lagging issues on my Linux ec2 instance? I have a 8cpu instance but still very slow when using Microsoft Remote Desktop on my Mac 

---

## 2022-03-22 22:52:31 - random channel

**Jonjonjon**

At the moment, I don't think it simulates taking volume. By default it has 0.15 seconds of latency, but I increased it to 0.5 seconds for safety.

---

## 2022-03-22 22:37:59 - random channel

**James T**

If you're taking, you can always simulate sensitivity to latency (slippage), but you won't be able to simulate how much you might move the market. Also I don't know how flumine simulates taking volume (e.g. does it simulate removing it from the book so you can't take it twice?)

---

## 2022-03-19 10:08:06 - general channel

**birchy**

When using Flumine backtest to process market data into csv's and I only need to call `process_market_book()` once per market, is it possible to skip straight to market closure? I currently use:

`def check_market_book(self, market, market_book):

    if 'signals' in market.context: return`

...but am wondering if it's possible to speed up/skip the unwanted updates? It seems like premature optimisation at first glance, but when processing 50K+ markets, it would make a difference.

---

## 2022-03-19 00:28:16 - general channel

**anomaly**

Pretty slow but not really an issue for runtime. I'm understanding how to work with the framework better, cheers for the help. It's going to require a major rewrite to merge with flumine so i'll stick with the low level bflw ops for now and slowly rewrite the codebase into flumine.

---

## 2022-03-17 20:44:45 - general channel

**liam**

I have tried a few ways of doing it on AWS but always fallen back to backtesting locally, although slower it is worth the cost in being able to very quickly analyse the results / make changes / rerun etc 

---

## 2022-03-17 12:04:44 - general channel

**liam**

Yes ideally, how slow is the modelling process? 

---

## 2022-03-14 14:00:38 - random channel

**D C**

I've been starting to use Python to perform logistic regression but struggling to find a way to model interaction effects. In R this is easy. I've tried sklearn and statsmodels but so far can't see an easy way to do this as both make use of the dataframe columns you provide. I am brand new to this in a python setting so may have missed something obvious but is there a simple way to do this or am I better off (from speed point of view) sticking with R ?

---

## 2022-03-12 12:32:06 - random channel

**Alex Alex**

Provided that flumine is python I would be surprised if you see a huge performance boost by buying a m1 ultra over something with less cores unless you have lots of code that releases the GIL.

---

## 2022-03-12 10:41:05 - random channel

**Unknown**

It doesnt release for a few more days. But it has the same cpu cores as the m1Pro/m1Max so you can expect basically equivalent performance. (maybe a little higher if they clock it higher as theres not battery/power draw concerns)

---

## 2022-03-02 13:23:26 - random channel

**liam**

[https://www.totalperformancedata.com/news-all/2022/3/2/total-performance-data-signs-landmark-multi-year-deal-with-jockey-club-of-saudi-arabia|:eyes:](https://www.totalperformancedata.com/news-all/2022/3/2/total-performance-data-signs-landmark-multi-year-deal-with-jockey-club-of-saudi-arabia|:eyes:)

---

## 2022-02-28 20:16:52 - general channel

**liam**

From memory you have to apply and tell them what you plan on doing / turnover but once in they are keen to help, well they where for me up until I got banned from XSP

---

## 2022-02-27 12:27:57 - general channel

**Aaron Smith**

I did it like a real man, no paper-trading no backtest - just raw negative EV :smile: Anyways, i think you need to trade at least a little when streaming the data, otherwise betfair may dislike your use of their api. Shouldnt cost a lot though, with minimal stakes and only a few bets. You may aswell win some, EV and reality converge towards each other slowly

---

## 2022-02-24 10:54:53 - general channel

**Rob**

performance wise, its quite a lot slower the mutable version in the benchmark, finishing in 7:15sec for the same data (22k markets)

---

## 2022-02-21 16:07:49 - general channel

**Rob**

All the extra allocations and copying of data has taken a big hit on the performance - but im still getting a touch above 50 markets/s || 375,000 update/s which isn’t a bad place to start. I expect to be able to raise that a bit when I dig into a profiler

---

## 2022-02-18 16:05:33 - general channel

**Alex Alex**

By doing it in the strategy itself I assume you mean run the calc for each market? The calculation is not super slow, but slow enough that I’d rather run it only once for all markets.

---

## 2022-02-18 15:38:46 - general channel

**liam**

Depends how slow the calculation is, you can use a worker to update the context and do it in the strategy itself or like you describe in a worker

---

## 2022-02-18 13:18:31 - general channel

**Gooat**

How is latency versus the market looking?

---

## 2022-02-18 07:58:19 - random channel

**bb**

I assume you are running it on EC2. One thing I have found is that the default swap is a lot lower than on my laptop and any memory spike above the limit caused crashes. 

---

## 2022-02-16 14:32:24 - random channel

**Jonjonjon**

Suppose I ran a script locally and it had no problems, but running it on AWS caused memory issues. How would you try to debug it? I have checked that I am running the same version of the script.

---

## 2022-02-16 14:08:12 - random channel

**liam**

[https://docs.developer.betfair.com/display/1smk3cen4v3lu3yomq5qye0ni/Exchange+Stream+API#ExchangeStreamAPI-PerformanceConsiderations](https://docs.developer.betfair.com/display/1smk3cen4v3lu3yomq5qye0ni/Exchange+Stream+API#ExchangeStreamAPI-PerformanceConsiderations)

---

## 2022-02-16 14:07:53 - random channel

**liam**

in the docs



```Performance tips



A single market subscription &amp; a subscription to all markets have an identical latency:

Cost is identical as the two subscriptions above would evaluate in sequence and thus with the same average latency.

Initial image is more costly to send than extra updates.

Limiting data with appropriate filters reduces initial image time

Segmented data will always out perform non-segmented data:

You will be processing a buffer while another is in-flight and another is being prepared to send

Writes to your connection are directly effected by how quickly you consume data &amp; clear your socket's buffer

Consuming data slowly is effectively identical to setting conflation.

If you receive con=true flag on a market - then you are consuming data slower than the rate of delivery.```

---

## 2022-02-16 11:41:04 - issues channel

**Aaron Smith**

[@U4H19D1D2](@U4H19D1D2) mh, actually not super sure, i know i ve had the latency warning on the orderStream, but not 100% sure if it was the case in this particular case. My logs dont reach far back enough to check it.

---

## 2022-02-16 11:25:10 - issues channel

**liam**

Lots of orders? Regular? Latency constant or increasing? Can't say I have ever had this with the order stream

---

## 2022-02-16 11:24:18 - issues channel

**river_shah**

What are the reasons why this may occur?

```WARNING[betfairlightweight.streaming.stream:on_update:68] [OrderStream: 1001]: Latency high: 1.75960373878479```

Not seeing high latency warnings on `MarketStream` so strategy is definitely keeping up with market data

---

## 2022-02-16 08:04:50 - general channel

**Rob**

hmm, that could be the problem, I do use the tv value they provide for the runner.

Should I just sum the volume in the tv cache? There shouldnt be any performance worries so its just a matter of which is more accurate.

---

## 2022-02-15 11:41:25 - random channel

**Oliver Varney**

```def read_prices_file(

    path_to_prices_file: str, lightweight: bool = True, **kwargs

) -&gt; Union[List[MarketBook], List[Dict[str, Any]]]:

    import smart_open

    from unittest.mock import patch



    trading = APIClient(username="", password="", app_key="")

    stream = trading.streaming.create_historical_generator_stream(

        file_path=path_to_prices_file,

        listener=StreamListener(

            max_latency=None, lightweight=lightweight, update_clk=False, **kwargs

        ),

    )



    with patch("builtins.open", smart_open.open):

        g = stream.get_generator()

        return list(mbs[0] for mbs in g())```



---

## 2022-02-15 11:00:26 - random channel

**Oliver Varney**

as a benchmark, how long should it take to stream a pricing file using bflw, full updates with all performance settings (although with recalcs of traded_volumes)?

---

## 2022-02-12 18:17:28 - strategies channel

**AndyL**

Multi process works great, all 4 cores zooming

I also cProfiled my strategy and improved its performance by another factor of x4     :rocket:

---

## 2022-02-12 10:13:34 - strategies channel

**AndyL**

Ah yes, i think it's memory exhaustion. Just looked at performance doc, I'll do that, thanks [@U4H19D1D2](@U4H19D1D2) demsg confirms out of memory thanks [@U01D36QEBSB](@U01D36QEBSB)

---

## 2022-02-12 08:22:43 - strategies channel

**liam**

Are you batching up the markets as per the [https://liampauling.github.io/flumine/performance/#multiprocessing|performance](https://liampauling.github.io/flumine/performance/#multiprocessing|performance) docs?

---

## 2022-02-11 15:43:25 - issues channel

**foxwood**

[@U016TGY3676](@U016TGY3676) It's on a Windows server so was easier to replicate my devenv and run it that way for now rather than setting up for command line. Early days with flumine and it has helped with some needed debugging and quick fixes. PyCharm is certainly a memory hog though which with other stuff that runs is pushing the hardware.

---

## 2022-02-05 11:08:59 - strategies channel

**liam**

`listener_kwargs` will help there, and then I would look at profiling your code, something is very slow

---

## 2022-02-05 10:42:00 - strategies channel

**liam**

[https://liampauling.github.io/flumine/performance/](https://liampauling.github.io/flumine/performance/)

---

## 2022-02-05 10:41:24 - strategies channel

**rjj**

Hi everyone, is there a way of speeding up the backtesting? I'm running 10K (flumine scraped) markets across 12 CPUs but its still taking 24+ hours. I'm not sure what performance I should be expecting but wondered if maybe there was a way to serialised the market ticks as flumine objects or something, to save parsing the data files.

---

## 2022-02-03 16:14:05 - issues channel

**foxwood**

Solved - bit brain bendy. In check_market_book I was using market.seconds_to_start to ignore unwanted early packets. When used in backtest that field is calculated using the packet "published time" but for live usage is calculated using "now". Since live always has some latency, at the time it considered it needed to start, the current packet to be processed was actually timestamped 200ms earlier than the wanted start time. Proved it by winding the stream back by 1 packet and it did exactly as the live did and eventually bet on the same runner. QED



My solution is therefore to use the "published time" as the processing trigger and not market.seconds_to_start which is a true real time value. The backtest and live "should" then be in sync I hope.



Be interesting to find out if we do all get the same timestamps - thanks for comments [@UBS7QANF3](@UBS7QANF3)

---

## 2022-02-03 12:24:13 - issues channel

**foxwood**

Puzzled by differences between live and backtest that I'm not expecting. Yesterday recorder and live betting were running on same VPS as separate processes under PyCharm.  Placed 28 live bets. Running the backtest later on it came up with bets on different runners on 4 of the races compared to what the live had done - sufficient to show a significantly different PL.



Looked at one in detail - no latency issues in log - recorder saw bet placed 187ms after logged by bet process. EX_BEST.. not used. Strategy source code the same for backtest/live. Betting triggering on EX_ALL.. price movements.



I expected the backtest to trigger on the same runner at the same time as the live did.



The recorder packets seem to be 4, 5 or 6 per second - could it be dropping packets that the live betting is seeing ? I thought they were all kept and cached if the app couldn't keep up ie excess latency compared to "pt" - ie not possible to miss any packets that BF push out ?



Any suggestions as to cause or where to look next ?

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

## 2022-02-02 07:23:48 - general channel

**Mo**

Will it be possible to leverage this speed improvement in bflw or is constructing the Python objects a bottleneck that would dominate any improvement?

---

## 2022-02-02 05:47:16 - general channel

**Mo**

Firstly, you are being paranoid, this has nothing to do with you being blocked



It's a simple network error and the fact you have 200 mb fibre is irrelevant. Your bandwidth has nothing to do with latency and the packets have a very long way to travel to you from Dublin



I don't speak Brazilian Portugese but I believe it's saying the remote host (i.e. Betfair) has closed the connection. Possibly at the TCP level your ACK packets are not getting back to them so they believe the connection has been lost. You might be able to keep the connection from dropping by tweaking some of your network settings but I don't use Windows so can't offer any specific advice there



The simple solution is what you're already doing which is to use a server (much) closer to Betfair

---

## 2022-02-01 23:12:06 - general channel

**VT**

Hi [@U030L8PPSHM](@U030L8PPSHM), VM stands for Virtual Machine? If so, I have no problems with the VPS, I never had an error in the market stream hosted on AWS, the error is on my local machine and has nothing to do with CPU or memory.

---

## 2022-02-01 23:08:43 - general channel

**Alex Alex**

Never encountered this kind of error before but my guess would be that it takes some time to get a response for your request reaching the server. `Latency high` sounds like it. What is the CPU load on your VM when you encounter this error?

---

## 2022-02-01 22:45:22 - general channel

**VT**

Guys, if anyone can help, I'm not able to proceed with my tests, every 5 minutes the error stream.



I ran the example code for examplestreamingerrhandling.py errors and the answer is below.



I even thought it could be due to data consumption, but the account I currently use must have already paid more than 20 thousand pounds just in commissions. I use a VPS on AWS and I leave the stream market running there, I believe it has nothing to do with it, I connect to the server and my computer at the same time.



I'm going to stop testing because I'm afraid my account will be blocked.



+++++++++++++++++++++++++++++++++++++++++++++++++++++++



The latency error appears 100% of the time, but it used to be between 0.6 and 0.9, this value above 1 had never seen. I'm in Brazil and this is the best we can get, 200mb download and upload, fiber optics.



WARNING:betfairlightweight.streaming.stream:[MarketStream: 1003]: Latency high: 1.6549324989318848



+++++++++++++++++++++++++++++++++++++++++++++++++++++++



ERROR:__main__:MarketStreaming run error



Traceback (most recent call last):

  File "C:\Users...\anaconda3\lib\site-packages\betfairlightweight\streaming\betfairstream.py", line 230, in _receive_all

    part = self._socket.recv(self.buffer_size)

  File "C:\Users...\anaconda3\lib\ssl.py", line 1226, in recv

    return self.read(buflen)

  File "C:\Users...\anaconda3\lib\ssl.py", line 1101, in read

    return self._sslobj.read(len)

ConnectionResetError: [WinError 10054] Foi forçado o cancelamento de uma conexão existente pelo host remoto



During handling of the above exception, another exception occurred:



Traceback (most recent call last):

  File "C:\Users...\AppData\Local\Temp/ipykernel_6984/859485830.py", line 61, in run

    self.stream.start()

  File "C:\Users...\anaconda3\lib\site-packages\betfairlightweight\streaming\betfairstream.py", line 60, in start

    self._read_loop()

  File "C:\Users...\anaconda3\lib\site-packages\betfairlightweight\streaming\betfairstream.py", line 212, in _read_loop

    received_data_raw = self._receive_all()

  File "C:\Users...\anaconda3\lib\site-packages\betfairlightweight\streaming\betfairstream.py", line 234, in _receive_all

    raise SocketError("[Connect: %s]: Socket %s" % (self._unique_id, e))

betfairlightweight.exceptions.SocketError: [Connect: 1003]: Socket [WinError 10054] Foi forçado o cancelamento de uma conexão existente pelo host remoto

INFO:__main__:Starting MarketStreaming

---

## 2022-02-01 15:00:22 - general channel

**Rob**

if betfair slightly changed the json to make sure ids were always the first field I could probably eek out a decent chunk more performance using a simdjson processor. But I dont see that ever actually happening

---

## 2022-02-01 14:58:50 - general channel

**Rob**

Yea I dont think that it would cost me much performance, would be the most expensive when lots of new prices get added and the vec needs to allocate a new buffer. But that wouldnt happen on many updates.

I imagine my biggest slow down is in the json and number parsing

---

## 2022-02-01 14:53:24 - general channel

**Rob**

happy to answer any questions. I imagine the big speed up is from the in place deserialisation

---

## 2022-02-01 14:51:25 - general channel

**Rob**

hey [@U4H19D1D2](@U4H19D1D2), get it all working ok? and have any feed back or performance results?

---

## 2022-01-31 13:17:56 - general channel

**liam**

Its CPU bound so threads won't help, are you assuming the decompression is slow or have you profiled? Can you share the profile if so?

---

## 2022-01-31 13:00:47 - general channel

**liam**

Is this rust or python? My understanding is that to make rust bindings you need to have a pretty good knowledge of cpython? Is the code open source?



Regarding your example you would need to set `lightweight=True` and `update_clk=False` on the listener for a fairer comparison. Ideally the `[speed]` install is used as well, see [https://liampauling.github.io/betfair/advanced/#performance|here](https://liampauling.github.io/betfair/advanced/#performance|here) for the performance docs

---

## 2022-01-31 12:46:18 - general channel

**liam**

Real shame you haven't looked to improve / speed up bflw instead

---

## 2022-01-31 12:42:23 - general channel

**Rob**

```from typing import Sequence 



import logging

import unittest.mock

import os

import tarfile

import zipfile

import bz2

import glob

import betfairlightweight



market_paths = [

    "data/2021_10_OctRacingProAu.tar",

]



# loading from tar and extracting files

def load_markets(file_paths: Sequence[str]):

    for file_path in file_paths:

        if os.path.isdir(file_path):

            for path in glob.iglob(file_path + '**/**/*.bz2', recursive=True):

                f = bz2.BZ2File(path, 'rb')

                yield f

                f.close()

        elif os.path.isfile(file_path):

            ext = os.path.splitext(file_path)[1]

            # iterate through a tar archive

            if ext == '.tar':

                with tarfile.TarFile(file_path) as archive:

                    for file in archive:

                        yield bz2.open(archive.extractfile(file))

            # or a zip archive

            elif ext == '.zip':

                with zipfile.ZipFile(file_path) as archive:

                    for file in archive.namelist():

                        yield bz2.open(archive.open(file))

    return None





logging.basicConfig(level=logging.WARN)

trading = betfairlightweight.APIClient("username", "password", "appkey")

listener = betfairlightweight.StreamListener(max_latency=None)



count = 0

for i, file_obj in enumerate(load_markets(market_paths)):

    with unittest.mock.patch("builtins.open", lambda f, _: f):  

        stream = trading.streaming.create_historical_generator_stream(

            file_path=file_obj,

            listener=listener,

        )

        gen = stream.get_generator()

    

        for market_books in gen():

            for market_book in market_books:

                count += 1



        print("&gt; Market {} Update {}".format(i, count), end='\r')

                ```

---

## 2022-01-31 12:42:06 - general channel

**Rob**

Hi Guys (I’m a lurker from the Aus Quants channel), Im doing some work with [@UUUAJQZ5J](@UUUAJQZ5J) writing some content for the BF Aus Automation hub around using the historic data files. The main problem I’m tasked with addressing is the speed and performance of how long it takes to parse through the files and the ease and developer experience when doing so. 

I’ve written a new python library whose aim is solely to read/parse these files and I’ll be open sourcing it along with my article and tutorials. The library is written entirely in rust and uses some tricky things like in place deserialisation and offloading decompression to threads to significantly speed up the parsing performance.



Im now onto writing the accompanying article and I want to make sure I cast betfair_lightweight in the best possible light. Im not a python dev at all, I don’t understand its concurrency patterns or its async capabilities and Im worried my benchmark code (stolen from the hub tutorials) is missing some simple optimisations that might dramatically increase the performance. In particular the bz2 decompression seems to happen in the same thread blocking everything else, so seems like a good candidate to offload to a thread/async?



Any help people could share here would be much appreciated!

---

## 2022-01-29 22:22:53 - random channel

**Jonjonjon**

I've found that changing the my backtest latency up to 0.3 seconds can have a big impact.:disappointed:

---

## 2022-01-29 14:54:10 - random channel

**thambie1**

I do it once in a blue moon, to check how latency sensitive my strategies are

---

## 2022-01-29 14:32:58 - random channel

**Jonjonjon**

Do many people fiddle with the latency setting of the backtester?

---

## 2022-01-26 13:34:39 - issues channel

**foxwood**

Much more suitable for your architecture than WIndows. You can do IPC on Win but not trivial if you want quick performance

---

## 2022-01-26 08:16:56 - issues channel

**Jorge**

Just my 2 cents, I finally understood what is consuming my RAM memory. Just by the packages I import in my bot, it consumes 68MB. `import pandas` alone consumes 36 MB. This is a bit of a problem when I run 100x bots :smile:

---

## 2022-01-25 20:39:25 - random channel

**James T**

They also have a prop trading team who trades against customers on their own exchange (obviously without charges and probably at lower latency). And they can see whose bets are whose. I don't think that's a fair market. 



Last time I looked a couple years ago, they make far more money from betting against customers than they do on exchange revenue. 

---

## 2022-01-25 19:06:26 - strategies channel

**birchy**

Are you getting the same latency on the VPS?

---

## 2022-01-25 18:36:15 - strategies channel

**foxwood**

Latency is always around 0.8ish it seems. Clock updates regularly (win10) but tried forced update but got same result. VPS connections are to 84.20.208.166 NET-BETFAIR-001 and same for local PC. Local PC ping time to that IP is 17ms and VPS is 13/14/19ms so both near enough same so unlikely network latency. If I patch down MAX_LATENCY to 1.0 will the message just go away - seems to be overriding normal logging output and certainly generating miles of log :upside_down_face:

---

## 2022-01-25 17:31:29 - strategies channel

**foxwood**

ok fixed that safely. strategy prints out immediate info from process_closed_market for markets still on BF but closed so getting there. Actually made some bets but I'd changed stake to £1 so not taken but no error message in log - maybe it doesn't - no probs. However, nothing in log except high latency messages for {MarketStream: 2201] with typical time of 0.84 - no flumine setup messages / bet errors / markets or anything like that - not sure what to expect lol. What section of processing / transmission is the latency referring to ?

---

## 2022-01-25 16:18:22 - strategies channel

**liam**

is the latency increasing?

---

## 2022-01-25 16:17:28 - strategies channel

**foxwood**

VPS running 2 x mktrec + 1 x BA fine today - 5 connections. Tried strategy live locally today (simply removed paper_trade=True). Seemed to log in ok but after 20 mins log had about 18k lines all like this `{"asctime": "2022-01-25 10:21:47,343", "levelname": "WARNING", "message": "[MarketStream: 2001]: Latency high: 0.8610439300537109"}` No other message about set up or starting of flumine which appears normal in mktrec. Message printed "starting strategy xxx"  when strat class started so it was starting off ok but that was all. Killed it after 20 mins and went for long walk lol. Any suggestions/clues - I can see the time it gives exceeds max latency of 0.5 but presume things should still function but quite slowly.

---

## 2022-01-25 09:42:52 - strategies channel

**foxwood**

[@U4H19D1D2](@U4H19D1D2) Was a dead connection I believe. I'd think I'd bust the connection limit - I had 5 open on a VPS (2 x mktrecord + 1 BA) and then my paper testing crashed or I thought of something to change so killed it to make a quick change. That meant 2 connections were abandoned each time and I read here somewhere that it takes about 15 mins for them to clear them. I know I killed it about 10 times in 30 mins lol. End result was BF pulled the plug on the earliest connections or maybe all connections for a short time. Killed all the server jobs including BA. The latency message was on server with a dead connection. Must find a way of doing a graceful terminate that closes connections - running under PyCharm currently. Thanks anyway - see what today brings lol.

---

## 2022-01-25 09:09:24 - strategies channel

**liam**

[@U02RN7YDRQ9](@U02RN7YDRQ9) what are your strategies doing? If you are getting latency issues its likely you are maxing CPU or doing something slow in the strategy (network or db call etc)

---

## 2022-01-25 08:04:45 - issues channel

**liam**

I do this, you should certainly look at chunking the markets due to memory leaks and performance reasons [https://liampauling.github.io/flumine/performance/#multiprocessing](https://liampauling.github.io/flumine/performance/#multiprocessing)

---

## 2022-01-24 21:22:02 - strategies channel

**foxwood**

Was worth doing as [@U4H19D1D2](@U4H19D1D2) said lol. Many confusing issues. My connection to BF from server stopped late afternoon. At that same time I had logged in to test and live at least 7 times in 20 mins after fixing issues from a local PC and also started a BA instance. Think I blew the connection limits since no graceful termination - just killed flumine. Local ran for the rest of the day but server didn't get any live data it seems and stuck cycling non-stop with Latency high: 3317.0....."". Not sure if they simply killed that IP. See what tomorrow brings.

---

## 2022-01-24 11:00:53 - issues channel

**Jorge**

Is it normal for a python process to take 68 MB of RAM (Resident) ? (It takes 22 MB of Shared Memory)

---

## 2022-01-24 10:11:48 - issues channel

**Jorge**

Question related with the Python logging library: If my process is writing a .log file that is 20 MB big, does that mean that the process will consume 20 MB worth of RAM memory? Is this how it works?

---

## 2022-01-23 10:00:53 - random channel

**Jorge**

Thanks, I created a Disk and RAM alarms with CloudWatch following this tutorial: [https://kumargaurav1247.medium.com/aws-cloudwatch-agent-installation-for-memory-metric-integrate-with-grafana-365404154](https://kumargaurav1247.medium.com/aws-cloudwatch-agent-installation-for-memory-metric-integrate-with-grafana-365404154)

---

## 2022-01-21 20:16:07 - general channel

**VT**

Hi guys does anyone have a simple script to measure our latency with betfair?

---

## 2022-01-20 13:33:30 - random channel

**Oliver Varney**

sounds like one of [@UBS7QANF3](@UBS7QANF3) latency sensitive ones

---

## 2022-01-20 13:32:43 - random channel

**Oliver Varney**

someone must have a great strategy catching out people to slow to cancel orders

---

## 2022-01-16 10:58:58 - random channel

**Mo**

Sounds very similar to [@UPMUFSGCR](@UPMUFSGCR)’s approach above which seems to have performance issues

---

## 2022-01-16 05:45:03 - general channel

**Colin**

Does anyone have any experience with developing their own bot and using it with a stake that is below the default minimum amount in your region/country for a prolonged period of time and for betting types that were not classed as closing out? If so, did you receive a warning from Betfair quite swiftly?

I note the 4th bullet point here, [https://developer.betfair.com/en/exchange-api/faq/](https://developer.betfair.com/en/exchange-api/faq/)

I'm keen to production-ise my bot soon, but I also want to start slow given it is not feasible for me to use Betfair's historical data to back test the algorithm I am using.

---

## 2022-01-15 21:18:22 - random channel

**Jonjonjon**

When doing A/B testing, what do people use to check whether to choose A or B?



So I have a strategy, and given a market_id, I want to always choose the same A or B, but at random.



I currently have the following code, but it is the slowest part of my program and is causing performance issues:



```def rand_int_from_market_id(

        market_id: str,

        low: int=0,

        high: int = 2

):

    """

    Deterministic way to generate a random int from a market id.

    The purpose of this is to help us do A/B testing

    Parameters

    ----------

    market_id



    Returns

    -------



    """

    seed = int(market_id.replace('.', ''[-6:]))

    state = np.random.RandomState(seed)

    return state.randint(low, high)```

Would it be safe to just choose odd market ids for A, and even numbers for B? Or could something like this be safer:



```(((market_id % 7) % 5) % 3) % 2```



---

## 2022-01-15 12:33:56 - strategies channel

**foxwood**

I'm developing some analysis based on the example datacollectinwom.py and am gathering lists of data per runner for graphing etc. I hadn't allowed for getting a None price from non-runners so it blew up (expected behaviour lol). However, that got me thinking about some key assumptions I had made and I wonder if they were safe, particularly with non-runners - maybe those with more knowledge could comment.

Assumptions:

1) the strategy callback argument "market_book" is the same object as could be accessed at "market.market_book"

2) the strategy callback "check_market_book" is made for every "mcm" streaming packet received and if that returns True then "process_market_book" is called - this means the strategy is offered every packet

3) for each callback all the data from the supplied market/market_book pointers has been updated to reflect the changes implied by the packet

4) the list of runners in the market_book and their index order is invariant ie runner Fred will be at the same index in "market_book" from first recording through to closed market



I think the first three are correct but not sure relying on the index position is safe - perhaps selection_id has to be used as a dict key for my saved lists which would slow things down quite a bit - important if it was a live betting strategy ?



I have noticed that BF change the "sort_priority" field for runners when there are withdrawals but not sure how/if that impacts flumine.



One area of difference I have found is with "market.market_book.market_definition.runners" which appears to be in BF sort order with N/R at the end whereas "market.market_catalogue.runners" and "market.market_book.runners" appear to remain in fixed positions regardless of withdrawal.

---

## 2022-01-15 10:40:10 - random channel

**Mo**

Given the process got killed, presumably by the OOM Killer, seems like memory would have to have been the problem

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

## 2022-01-10 15:12:38 - random channel

**Stefan**

[@UPMUFSGCR](@UPMUFSGCR) My connection latency to betfair servers is around 120ms. I wrote my test code for 4 combination using rest api or streaming api, and placing 10 bets in one api call, or bet by bet in succession checking whether rest or order streaming api updated market bets.  Results are following:



                            | RestApiInOneApiCall -&gt; 0.504 seconds

                            | RestApiBetByBet -&gt; 3.134 s

                            | StreamingApiInOneApiCall -&gt; 0.332 s

                            | StreamingApiBetByBet -&gt; 2.308 s



[https://github.com/StefanBelo/Bfexplorer-BOT-SDK/blob/master/TestBetPlacementSuccession/Program.fs](https://github.com/StefanBelo/Bfexplorer-BOT-SDK/blob/master/TestBetPlacementSuccession/Program.fs)

---

## 2022-01-09 23:29:54 - random channel

**Dave**

Cheers guys. Was just reviewing performance over the past 12 months and wanted to compute some benchmarks in other asset classes, hence the q.

---

## 2022-01-09 18:52:08 - random channel

**Dave**

Question RE benchmarking performance. How do you guys quantify how much better off / worse off you are by allocating your money to your gambling activity rather than some index fund? Especially as on Betfair your money is turned over many times, and also the concept of a "bank" doesn't make much sense given recurring withdrawals etc

---

## 2022-01-09 18:02:48 - random channel

**ShaunW**

I'm non-flumine [@UPMUFSGCR](@UPMUFSGCR) but you could do as I do and have a generic performance checking prog that for the sake of minimum maintenance is attached to a long term market, maybe next President, which checks things like you're looking at. 10 individual placements, 10 placements with confirmations between, 10 cancellations etc which is scheduled to run a few times a day. No reason you couldn't use one on an in-play market too if you want to look at delays.  Basically the best answer to your question is just to find out because your specific situation will be whatever it is.

---

## 2022-01-07 07:55:45 - strategies channel

**D C**

Don't forget it is not just about model data but also speed of getting hold of that data. Consider a team sport using a model that has parameters that are team aggregated statistics versus one that uses the selected players individual statistics. Model A won't change if a player is injured/dropped from the team but model B will - and people with the first knowledge of lineups/injuries will update their model and have the advantage. So much depends on the type of sport and whether you use exchange or bookie. For example, the former big syndicate employee Misha used to inform us regularly that in horses, the big players don't get involved until 2 minutes before the race off - but in other sports betting with bookies, chances are you want to get in early before all the sharps snap up the value.

---

## 2021-12-30 18:55:01 - random channel

**James T**

I personally still worry whether the global stock market will continue to grow as it has done like in the hundreds of years in the past. I think one major driving factor of the past has just been population growth, which leads to consumption growth, which leads to economic growth - but I think we're beginning to see a slow down in population growth now. So who knows. 



I expect for hundreds of years people have always questioned whether stocks can just go up forever or not, and so far it has! So maybe this is just the same. There's too much incentive for people to want that to happen. Then again, perhaps times are changing…

---

## 2021-12-28 21:14:12 - random channel

**Michael**

That's a very small sample..... presumably not even 250 markets...? Do you have in place some procedure for analysing the performance of your analysis?

---

## 2021-12-28 20:31:01 - random channel

**PeterLe**

Merry Christmas!

Someone asked me a question today and although I had an inkling as to the answer I wasn’t sure..

The question was..how would you measure the performance of an inplay manual ‘trader' over time.

Assuming the stakes would increase over time as the trader got better



Would you use ROI (Profit/Total Stakes) or even MC as indicators as you would with automation? Then do a comparison between periods (by Month Quarter etc)

Thanks

---

## 2021-12-28 15:41:06 - general channel

**VT**

I've been asking about the subject out there, some recommended changing the language to C but I discarded it, I intend to do my studies in Python, I'm a beginner.



Others have suggested Cython, Cpython or Pypy, I'm still studying about that. My application is simple, just send orders and close the matched orders and speed is the most important.

---

## 2021-12-28 15:21:51 - general channel

**Mo**

Use a session. Having to do an SSL handshake on every request is going to kill performance

---

## 2021-12-28 00:02:58 - general channel

**VT**

I searched the Betfair API documentation and it seems to me that there is really only one way to send orders (via placeOrders) but here in Python it takes almost 1 second to place bets (on pre-live market), a little slow for me.

---

## 2021-12-26 13:59:34 - random channel

**Jonjonjon**

Betfair keep sending me free bets  (6 on the last month) and my bot performance has been lackluster. Am I at risk of being classified as the wrong sort of VIP?

---

## 2021-12-22 23:09:36 - random channel

**Beeblebrox**

There's a seconds_to_start flag you can use as well. [https://liampauling.github.io/flumine/performance/|https://liampauling.github.io/flumine/performance/](https://liampauling.github.io/flumine/performance/|https://liampauling.github.io/flumine/performance/)

---

## 2021-12-19 19:01:36 - strategies channel

**Aaron Smith**

however, latency issues will likely be resolved

---

## 2021-12-19 18:59:01 - strategies channel

**Aaron Smith**

I had a strategy placing a lot of orders (not reaching the 5k though) and immediatly got latency issued

---

## 2021-12-19 18:53:05 - strategies channel

**Ruben**

hello everyone, I am experimenting with running my first strategy live, and I am running it in an EC2 t3.micro instance (2 vCPUs, 1gb memory). However, looking at the logs, I am seeing a lot of latency warnings, some with very high latency, like 60s. Could this be due to the CPU of the instance not being fast enough to process updates at the rate they come in?

---

## 2021-12-18 08:09:04 - general channel

**D**

Just to add another viewpoint to all the good advice above: I used RDS (postgres) for quite a while but it started to seem expensive, especially for historical data I was hardly ever querying. My current approach is to upload csv, parquet and json data to S3 locations and use Athena to query them into pandas dataframes. Don't have any issues so far; performance is good and I can add new data to my json files without breaking existing queries.

---

## 2021-12-17 20:04:31 - general channel

**Peter**

There's no inherent slowness in Mongodb, so if your retrievals are slow, that's probably an indexing issue. Mongo (and indeed any schema-less database) makes more demands on the technical skills of the person setting it up and administering the data than a traditional SQL-based database.



Personally I use a MariaDB instance at RDS as, while a huge fan of Mongodb and Elastic, I haven't in my trading activities found a strong enough case to store data in documents, rather than well-designed rows, to warrant the added complexity.

---

## 2021-12-17 19:17:06 - general channel

**Beeblebrox**

Database questions... I currently have a single MongoDB database, running locally on the same machine as Flumine is running, to store all my orders with each strategy in a separate collection. I chose MongoDB as I know next to nothing about databases and the fact it could easily store JSON data seemed like the easiest solution just to get something working.



However...



1. Getting data from the db for analysis is pretty slow

2. It's crashed a couple of times and lost a load of orders

So I'm thinking there's probably a better choice of db I could chose, but I'm not really sure what and I'm not sure how to design it.



• Is an RDS db a better choice?

• Do people host their db's locally or do you use AWS to host it?

• Do you have one big db with all your orders (and separate tables for each strategy) or separate dbs to store orders for different strats?

I guess the general question is: what do people use and why?

---

## 2021-12-16 08:23:53 - general channel

**Paul**

Performance/price, and the architecture is quite novel. We should probably just flat out benchmark some of this stuff really, shouldn't we?

---

## 2021-12-14 14:26:14 - general channel

**C0rnyFlak3s**

Has anyone deployed their backtesting engine to an AWS service? I am planning on porting my data and engine to a service that allows me to load files very fast and offers me enough performance to run parallel backtests on given data. For this I figured, I need 1.) enough fast read/write storage (more so the read speed should be maximized). 2.) enough CPUs to start multiple backtesting processes at once. For this I am looking for a suited AWS service, where I can run my IDE and have my data stored on fast memory. Can you guys point me in the right direction on this one? I am not so experience with cloud computing and finding the right configuration for a given purpose. Would gladly appreciate any pointers. :slightly_smiling_face:

---

## 2021-12-11 15:00:20 - random channel

**Oliver Varney**

Very high memory requirements in terms of models here unfortunately

---

## 2021-12-08 23:45:31 - general channel

**Jonjonjon**

[@U012XF5CNPN](@U012XF5CNPN) I'm afraid I read them a while ago. And they tended to go above my head. From memory, nothing was worth mentioning. I think that following the David Silver course in YouTube, and then reading the free Sutton book should be enough. Then you just need to use your own imagination/experience. I spent a few months writing up a basic RL library in Python but neve found time to finish it.



[https://www.google.com/search?q=reinfo+cement+learning+market+making&amp;oq=reinfo+cement+learning+market+making&amp;aqs=chrome..69i57j33i22i29i30l2.10566j0j7&amp;client=ms-android-xiaomi-rvo3&amp;sourceid=chrome-mobile&amp;ie=UTF-8|https://www.google.com/search?q=reinfo+cement+learning+market+making&amp;oq=reinfo+cement+learning+market+making&amp;aqs=chrome..69i57j33i22i29i30l2.10566j0j7&amp;client=ms-android-xiaomi-rvo3&amp;sourceid=chrome-mobile&amp;ie=UTF-8](https://www.google.com/search?q=reinfo+cement+learning+market+making&amp;oq=reinfo+cement+learning+market+making&amp;aqs=chrome..69i57j33i22i29i30l2.10566j0j7&amp;client=ms-android-xiaomi-rvo3&amp;sourceid=chrome-mobile&amp;ie=UTF-8|https://www.google.com/search?q=reinfo+cement+learning+market+making&amp;oq=reinfo+cement+learning+market+making&amp;aqs=chrome..69i57j33i22i29i30l2.10566j0j7&amp;client=ms-android-xiaomi-rvo3&amp;sourceid=chrome-mobile&amp;ie=UTF-8)

---

## 2021-12-08 23:44:22 - general channel

**Paul**

So I think knowing a lot about successful strategies can help close the avenues down, and then with a few hundred hours of building the gym and feature engineering you might get somewhere. I'm on that path myself, albeit slowly.

---

## 2021-12-07 07:49:59 - general channel

**river_shah**

Traversing the abstract syntax tree and dumping out llvm is probably the cleanest way to go full compiled speeds with python. I hope this kind of feature and  complete GIL removal makes it into python 3.11+

---

## 2021-12-07 07:46:25 - general channel

**river_shah**

Haha, I have recently been working with `Julia` on a project so I do have a soft spot for people new to python wanting to get “compiled” language speeds

---

## 2021-12-07 07:37:46 - general channel

**river_shah**

If you really are in interested in cython, [https://towardsdatascience.com/use-cython-to-get-more-than-30x-speedup-on-your-python-code-f6cb337919b6](https://towardsdatascience.com/use-cython-to-get-more-than-30x-speedup-on-your-python-code-f6cb337919b6) may be helpful.



If you use numpy based numerics, it is usually going to call into efficient c++ code anyways and will release global interpreter lock too (in case you have to parallelise certain sections)

---

## 2021-12-06 08:32:31 - general channel

**Javier Martín Pérez**

I have been using csv files to store data like bets placed, etc but I have had several problems with Excel when I have to edit them. Apparently most of the most annoying features of Excel (like the rounding up of 16+ digit numbers) are unavoidable and I was wondering if there is a better software that you are usually using. The notepad works relatively well but is generally difficult to work with. I remember that when I used Tableau in the past it was very slow, is it better nowadays?

---

## 2021-12-05 09:33:00 - general channel

**liam**

Use smart_open [https://liampauling.github.io/flumine/performance/#file-location|https://liampauling.github.io/flumine/performance/#file-location](https://liampauling.github.io/flumine/performance/#file-location|https://liampauling.github.io/flumine/performance/#file-location)

---

## 2021-12-02 21:20:18 - general channel

**TT**

How do people deploy the market recorder alongside strategies? My initial thoughts are to try and keep them separate but I can see a few options:

 - Deploy two separate ec2 instances (one for the market recorder and one for running strategies)

 - Use one ec2 instance but run 2 separate python processes

 - Use one instance and just add both the market recorder strategy to the framework alongside the other strategies



 How do other people approach this? And are there any other things to consider i.e latency/connection limit issues etc?

---

## 2021-12-02 18:58:40 - strategies channel

**birchy**

If I was asked to give just ONE piece of advice, it would definitely be to NOT look at short term performance. And I learnt that the hard way. One of my best ever strategies lost over £500 in the first week and left me with around £100 in my account. I was pretty pissed off at the time, so logged out in frustration, thinking I'd never return. I left the bot running. A month or two later, I logged in expecting to see my account empty. It wasn't. It had placed 1000's of bets during my absence and turned out to be a £3K a month strategy at £2 stakes and ran for around 18 months before it started to decline. So the moral of the story is NOT to write-off a strategy just because it's showing a short term loss. Variance can take several months to shake out and you need some fairly large bollocks and a lot of patience to ride on this rollercoaster.

---

## 2021-12-01 22:35:30 - strategies channel

**AndyL**

[@U4H19D1D2](@U4H19D1D2) correct i am doing a simple approach. Basically ive been watching loads of races and corresponding odds and looking at recent form, and ive created my own price formula from the standard features, recent finish positions, recent normalised speed avg and max, recent normalised sectional timings...

I actually quite like the prices it produces, i watch races and compare mine v market, and quite often think mine are more true. For example i quite often see a dog go up a grade and the market immediately gives it a very short fav price say 2.0,but my model has it say more at 3.5+, and to me the market has it so wrong the dog typically finishes near last...

This is where i think my model falls down it's trying to cover all prices and all dogs. Taking what [@UNQGKT0CR](@UNQGKT0CR) i think said isolate more specific variables, eg.short priced upgrade...

---

## 2021-12-01 13:13:40 - random channel

**birchy**

With ref to the earlier chat about getting bet histories, I seem to have some distant memory that `listClearedOrders` can retrieve bets way beyond the 90 days that the documentation suggests? And IIRC, it's about 2 or 3 years?? Can anyone confirm?

---

## 2021-12-01 09:36:55 - strategies channel

**AndyL**

Using previous form and performance of the dogs

---

## 2021-11-30 23:03:01 - random channel

**Jonjonjon**

Yes. Please also be aware that if you have more cores, you need the RAM to use them. And performance gains don't scale linearly with number of cores (they scale less), due to shared hard drive and memory bandwidth.

---

## 2021-11-30 21:45:00 - issues channel

**Aaron Smith**

Network out in bites has some spikes, but rather than spikes i d say its "spikey" all over with rather consistent spike height, doesnt seem to correlate with the latency times

---

## 2021-11-30 21:32:18 - issues channel

**Tom**

Thanks Liam. Turns out that `get_order_from_bet_id` bottleneck was *a* bottleneck but not *the* bottleneck that was causing my issues. I managed to get my `process_market_book` step down to an average of 1-5ms from 10-40ms by removing some pandas objects and using blotter exposures rather than calculating the matched exposures from the orders myself. Seems to have done the trick runs only like 10% CPU utilisation on a 2vCpu 4 Gb ram machine now and none of these accumulating latency issues

---

## 2021-11-30 20:43:27 - issues channel

**Aaron Smith**

Hey ppl, last few days i m getting flooded with both

```"WARNING", "message": "[MarketStream: 2001]: Latency high: 9.45749306678772"}```

and

```"WARNING", "message": "High latency between current time and MarketBook publish time", "market_id": "1.191643732", "latency": 13.961846351623535, "pt": "2021-11-30T18:37:48.781000"}```

First, i would like to understand the difference between the two. Both compare current time to publish time, but i recall them being different in some way.

Also any leads on how to approach this problem are appreciated. I ve got flumine running on aws (eu-west-1b), newly set up the servers (but also was on aws before). I m running t2-micro instances. CPU utilization seemingly never goes higher than 6%. The strategies are also very light in terms of computing time. Could the internet connection/bandwidth of the ec2-instances be a limiting factor?

Also, i realized, instead of piling up latency (as in getting more and more behind on each update), it seems to jump from 0 to 20 seconds (and then gradually gets lower), which seemed like an odd behaviour to me.

---

## 2021-11-30 12:15:55 - issues channel

**C0rnyFlak3s**

Has anyone experienced issues with purchasing data from betfair so far? I am currently running into a problem where on the last step (confirming the purchase) I get an error code: 0x05479P . Unfortunately the support response either doesn’t help or is slow to begin with. They for now just told me to clear the cache and cookies, but without success. Any ideas? :slightly_smiling_face:

---

## 2021-11-28 17:57:41 - issues channel

**liam**

Yep that will work but you have no error handling and fairly sure .start is blocking from memory 

---

## 2021-11-28 15:20:42 - general channel

**Mo**

Despite being latency sensitive, none of my strategies are triggered by the price stream so I've never looked personally. But I do these kinds of optimisations with the data feeds I do trigger off

---

## 2021-11-28 13:58:49 - general channel

**D C**

I see what you mean. I was just thinking about if you had 2 order stream subscriptions - one on your home machine where you are placing the bet and another on AWS, both order streams will push the bet ID when it is created and you can compare arrival times for latency because they will both have the same publish time. But as you say, that only tests a one way performance on the stream side, not the actual lag in the whole bet placement timeline. I don't know enough about this stuff other than working on real time embedded stuff where you can get more accurate timings on things. A bit different to comms between machines running full OS with multiple processes.

---

## 2021-11-28 13:24:21 - general channel

**PeterLe**

Thanks DC for your thoughts. So to answer the first part of that, Im probably 180 miles to Dublin, so there will probably be a slight variation when the inplay signal is received. If it was found that my home PC was consistently slower to receive the data that the instance in AWS, I wouldn't be concerned as Im not measuring the first part of the leg, but the whole trip, ie the ability to receive the data , act upon it; place an order and receive a Betid.

Re the second part, Im not as technical as you guys DC :grinning:, so I wouldn't know how to test that (I actually deleted the Lightsail instance last night anyway)

---

## 2021-11-26 19:52:36 - general channel

**D C**

Surely latency is not the only concern is it? Internet down time at home is a lot more frequent than it is if you use AWS surely?

---

## 2021-11-26 17:00:59 - general channel

**ShaunW**

4 does seem tiny given it can vary quite a bit from one order to the next .... I ran mine all day and averaged, running on both local and aws simultaneously to rule out any daily variations in the backbone in general. I couldn't find any tangible benefit to running locally so for me, the pros of being on aws outweigh the cons and performancewise it's much of a muchness.

---

## 2021-11-26 16:00:16 - general channel

**Unknown**

I was just testing connection time to the API..comparing my home PC (Quite powerful system) v AWS eu-west-1a (Low powered but adequate : 2Gb 4 vCpu's)

from previous threads on here i know that the connection to betfair is asymmetric (as it goes via prolexic)

So I thought i check it out...

Same strategy on each system, simply fires in a lay order at 1.01 as the market signals it is in-play

In 3 out of 4 tests the home PC was able to receive the price data, and obtain a bet reference faster than AWS(as my strategies react to market prices, I thought this was the best way to measure and not worry about the asymmetry)

Would you say this was a reasonable test?

Just putting aside the other benefits of running on AWS, If speed to market is the main important factor is AWS worth it?

---

## 2021-11-26 09:20:28 - general channel

**liam**

Just added a '[https://liampauling.github.io/flumine/performance/|performance](https://liampauling.github.io/flumine/performance/|performance)' tab in the flumine docs as it seems to be a common question, let me know if I have missed anything

---

## 2021-11-26 00:53:48 - issues channel

**Tom**

Recently tried deploying a flumine strategy (which works well locally) to an AWS machine and was experiencing some of the same latency warnings I've seen posted above: `"... High latency between current time and MarketBook publish time", "market_id": "...", "latency": 53.55.."` which sort of continually escalates to the point the strategy was acting on market book updates from 30 seconds prior. CPU utilization was pretty high (40-50%) on a EC2 t3a.medium but not enough to cause this huge bottleneck I thought but i tried it on a EC2 t3a.2xlarge and experienced the same behaviour.



Took the advice to profile the code using cProfile and the biggest difference was the `process_orders` calls [ `baseflumine.py:220(_process_current_orders)` and `process.py:33(process_current_orders)` ] were completing in approx 10ms per call locally but 350ms on the AWS machine. Any ideas why this might be happening? Or anything i can do to clean out + speed up `process_orders` generally? Strategy is pretty order heavy so the partial fills and price updates etc start adding up to a big order list for each market but flumine seems to barely feel it locally.

---

## 2021-11-25 11:15:59 - general channel

**Mike Walpole**

Good question James, and one we get asked quite regularly. 

I would say that the main benefit we offer is a chance to accelerate your career as a sports trader with investor capital, similar to the way that many traders have done with equities and bonds. If you love what you're doing and think you can build a truly professional trading book, we support you through the process with everything from capital, to trade support, to understanding your actual risk position. 



We hire top tier individuals and help them become world class traders. For example, you will benefit from:



• sessions with sports/performance psychologist to help you unlock your trading potential

• speakers from best equities, FX, commodities trading outfits (Goldman Sachs, Morgan Stanley, Optiver)

• regular debrief on how you're tracking against expectations and what to “do more of”, “stop” and “try”. You will know how you are performing and won’t have to second guess yourself or waste time guessing.

 

We have intentions to list on the stock exchange within 36 months and you have a chance to join us on the ground level of what we are confident will be a truly global trading operation.

---

## 2021-11-22 21:07:14 - general channel

**Amit Patel**

hey guys! I'm running back tests with a simple strategy for horse WIN markets and it takes around 25 mins for a weeks worth of data. Is this expected and is there anything I can do to improve performance other than buying a better pc? :slightly_smiling_face:

---

## 2021-11-17 10:59:14 - random channel

**Mick**

I have been working on a website [http://sprintratings.com|sprintratings.com](http://sprintratings.com|sprintratings.com) which displays my horse ratings. The ratings are significantly more accurate (i.e. correlate better with finishing position) than the Racing Post ratings (RPR). The site also displays the history of each horse's past performance in a rather unique way which I hope people will find useful. This site is not open to the general public yet but it is running with updates every day so I can give the automated systems a good workout. The site has a simple username and password of "horse"/"123". I am looking for general feedback both on the website and the individual ratings themselves. If you prefer to give feedback directly to me, please email [mailto:michael@sprintintelligence.com|michael@sprintintelligence.com](mailto:michael@sprintintelligence.com|michael@sprintintelligence.com)

---

## 2021-11-14 15:04:28 - general channel

**Mo**

The higher the risk the more you should expect to get paid. The further you are from the off the more uncertainty there is about the true price and the wider the spread. Ditto third division Thai football versus EPL. In running you have the risk of being picked off by latency arbers

---

## 2021-11-12 20:44:26 - general channel

**D**

I don’t have the details to hand but for the vast majority of time, your cpu is just waiting - waiting for disk, memory, network packets etc. I’m not an expert on flumine and obviously it depends what you’re worker is doing…

---

## 2021-11-06 08:40:59 - strategies channel

**Oliver Varney**

btw I think my model uses both although im not sure off memory which has a higher weight

---

## 2021-11-01 13:47:10 - random channel

**Oliver Varney**

A performance on a given day probably cant be boiled down to one attribute. Youve got weight carried, going + actual going, jockeys, weight allowances, interference all sorts really. I think you will end up creating a feature that is way too specific and wont generalise. Furthermore if a horse cant place the jockey will walk the horse over the line and distances then can be misleading. What I will say is in-play odds can be used to determine how well a horse has run, even if it hasnt won.

---

## 2021-10-31 17:04:14 - strategies channel

**Ruben**

I'm thiking there's always going to be some degree of ambiguity simply because of the latency right? at any point an order that I believe is executable, could be matched and hence no longer available. maybe there's no perfect solution to the problem, but rather some "best effort" solution

---

## 2021-10-27 09:16:49 - general channel

**Lennart**

Thanks, Mo. "Data feed" was perhps a bit broad - as a starter I'm looking for accurate and low-ish latency game scores and game clock. Low latency compared to BF's inplay service which seems to be often delayed by 10-20 seconds.

---

## 2021-10-26 16:28:10 - general channel

**Mo**

We were trialing I think the BetRadar feed which at the time was the official feed with the lowest latency at a cost of $250,000 per season. This was prior to the opening up of the US market so I wouldn’t be surprised if you’d pay a lot more for the equivalent feed today

---

## 2021-10-26 08:53:49 - betfair-news channel

**George**

Agreed, I think a millisecond-precision version of placedDate would be of great help to anyone with even a passing interest in optimising their speed.

---

## 2021-10-25 16:21:09 - betfair-news channel

**Neil T (Betfair)**

Hi [@UCQB6S222](@UCQB6S222)



Thanks for clarifying your points. You can measure network latency to the edge of the Betfair infrastructure using well-known techniques (traceroute, ping, etc) based on the endpoints that we provide ([http://api.betfair.com|api.betfair.com](http://api.betfair.com|api.betfair.com)). For any API request, the difference between the HTTP request and response time (available as an HTTP header) will provide an indication of the total round trip time. 



placedDate is the time that the order arrived at the Betfair servers for processing at which point the bet will be placed (matched/unmatched) or subject to the in-play delay, if applicable, before being placed. Within the above parameters, you only have the potential to control the latency between your machine and our infrastructure. Once your request is received, you are subject to the speed at which the bet is processed within our matching engine. This itself may vary around the ~100m/s processing time.

---

## 2021-10-25 09:37:38 - strategies channel

**liam**

Thats an event file full of 'OTHER_PLACE' markets, as the docs state you need to add the event flag if providing an event file



[https://liampauling.github.io/flumine/quickstart/#event-processing](https://liampauling.github.io/flumine/quickstart/#event-processing)



Note this will be slower than processing single files

---

## 2021-10-23 10:35:59 - strategies channel

**Oliver Varney**

5% in real life is good if you can scale it to high stakes. It sounds however that you could be overfitting slightly. Remember you should only keep refining a signal if it increases both the performance of the training and crucially the test set.

---

## 2021-10-23 10:01:00 - strategies channel

**Adrian**

Thanks Oliver. I don't really know how to approach historical data analysis. My only skill right now is backtesting, then iterating the backtest for better performance. THere must be a way to make it work

---

## 2021-10-22 16:52:55 - betfair-news channel

**Neil T (Betfair)**

There is room for a more in-depth &amp; definitive technical article on this, so I’ll see if our dev team will consider writing something to be included on our Technology blog ([https://ppb.technology](https://ppb.technology)). We might not be able to provide the full and more explicit technical details you want though :slightly_smiling_face:



In the meantime, here’s a high-level summary:

 

• For performance reasons, all bet matching takes place in a bulk betting matching cycle, each of which takes ~100 m/s. 

• All bets within a single cycle are queued (matched/unmatched) on a FIFO basis. 

• Cross-matching occurs both at the market and event level. 

• There is no concept of exactly the same time, one bet will always be picked up before another even if one is microseconds before the other.



---

## 2021-10-22 16:22:49 - betfair-news channel

**George**

Hi [@UNW8Q88EL](@UNW8Q88EL), thanks very much for getting back to me with this impressively comprehensive response, which is much appreciated, and thanks again for this initiative which is brilliant I think we all agree.

A few things come to mind:

• I probably phrased question 1 in a misleading way. I didn't mean to sound as if I was asking about asynchronous orders. I am really just interested to know how best to measure latency from door to door - and I am sure others would be too. Your thoughts on that would be greatly appreciated.

• Something like placedDate is _*possibly*_ what I am looking for, and I should have mentioned it as a possible solution. However, it currently doesn't help because it seems to be rounded to the nearest second or at least doesn't display any precision further than that at all, which is frustrating.

• Furthermore, even if placedDate was a millisecond-precise quantity it's not entirely clear (to me) what the meaning of this value actually is. Does it describe the time that the order arrived at Betfair's servers, or does it represent the time that the order was considered by the matching engine perhaps?

• In terms of question 2, I suppose what I am really after is a way to figure out exactly how much slower my order was than the one which got the fill that I wanted. Let's say a horse falls and I want to be the first to lay it. So I send a LAY order to Betfair, but it doesn't get filled, because someone else was faster. It's pretty hard in this situation for me to know whether I "lost" the race for liquidity by 1 millisecond or 200 milliseconds. I can look at the publishTime of the stream update which shows the successful order, but there's no way to track that successful order backwards in time to know what time it arrived at Betfair's server compared to what time my order arrived. I was just thinking that, if I knew how long the specific matching cycle in question had taken, that would enable me to work backwards and make a good estimate of when the successful order arrived. And, if I also had a good idea of what time my order arrived, then the difference between the two represents how much I lost the race by. 

• If I'm going to lose the race by 200ms then I may as well give up; if I'm mostly losing by 20ms then I should probably carry on trying and maybe invest in some better technology!

---

## 2021-10-22 10:47:39 - betfair-news channel

**George**

Would Betfair be willing to provide accurate(ish - down to millisecond precision) internal timestamps in responses and in the stream?

1. When I send a bet in-play, for example in horse racing, I get a 'pending' response, but this response doesn't include the timestamp that the order was received at the Betfair server. This timestamp must exist in order for Betfair's tech to know in which sequence all orders were received. It would be great to have this timestamp included in the pending response, so that I can measure my latency "from door to door" accurately.

2. On the market data stream we receive a 'publishTime' which is presumably the time at which the matching engine cycle finished. It would also be useful to have a field that represents the time at which the matching engine cycle began. This would enable me to look back at the logs and say: OK, my order didn't arrive in time to make it into this matching cycle which began at T1, so it was delayed a bit longer and had to wait for the next one, which began at time T2.

---

## 2021-10-22 00:06:22 - betfair-news channel

**AndyL**

A good explanation by your chief architect here: [https://youtu.be/tyhx3FNCogA|https://youtu.be/tyhx3FNCogA](https://youtu.be/tyhx3FNCogA|https://youtu.be/tyhx3FNCogA)

So it looks fairly clear Kafka is not the problem, Kafka currently fronts the Stream API, but the Order Input Handler and Order Processor modules are still native monolithic Oracle DB programs, which he highlights is a current problem they are working to replace with a Kafka solution. That sounds like WIP... but looks to be heading in the right direction. Im not surprised having watched this video. The responsive slow down ive heard people report immediately prior to an outage probably points at those DB order processor apps.

Good luck with the Kafka migration for those.

---

## 2021-10-20 12:19:16 - general channel

**ThomasJ**

[@U01UN2R5LM8](@U01UN2R5LM8) You said "But if doing so does not speed up the backtesting, i guess that is pointless." ... well it might speed things up if you summarize data...but what to summarize? You'll find that over even a short time of backtesting you'll want to look at data in many different ways and you'll keep on producing different summaries. So the production of the summaries and then testing on them will probably be way longer than just reading from the raw data, putting it into memory via, as liam mentioned a Pandas DataFrame (I presume it's Pandas), and then you can look at the data in an infinite number of ways directly, and super fast.

---

## 2021-10-19 13:36:53 - general channel

**Alessio**

Indeed, i'm not at the level yet where i can invest in lower latency feeds fees, so I spend quite some time on my side to detect the risk of having to cancel pretty soon and anticipate that

---

## 2021-10-19 13:08:34 - general channel

**Mo**

I'm asking because I'd expect high latency to be most punishing when you don't cancel in time and maybe this is not something you care about

---

## 2021-10-19 12:20:27 - general channel

**Peter**

[@U01UN2R5LM8](@U01UN2R5LM8) What Thomas said. Re-streaming the raw data from a file is pretty fast, and very flexible. Once you start storing the data in a database you're either losing information or adding complexity if you go the relational route, or having to pull lots of records (which is slower than re-streaming) if you go schema-less / document-based.



My approach is a compromise. I have a daily job that re-streams the previous day's files to extract meta information and adds it to a database-held index of markets. Then when I want to backtest, I query the market index and pass the files matching my criteria to my backtesting script.

---

## 2021-10-19 12:09:26 - strategies channel

**Oliver Varney**

from a ML perspective but I think it generally applies, is that you have some form of loss function (a way to measure performance), you take iterative steps changing values of the signal which decrease this loss function in training set. Then you would predict the estimates for the test set in that step and if its loss decreases also then you continue repeating, until teh point where a change to the signal value decreases the loss in the training set but increases the loss in the test set

---

## 2021-10-19 12:02:27 - strategies channel

**Oliver Varney**

looking at the performance in the training set has little value normally

---

## 2021-10-19 12:01:26 - strategies channel

**Oliver Varney**

Typically you would change a value(s) of signal then at each step evaluate the performance in the test set. This should help as it sounds like your data mining essentially

---

## 2021-10-19 11:51:21 - strategies channel

**Oliver Varney**

When your training / fitting are you evaluating its performance against the training or test set ?

---

## 2021-10-19 11:00:27 - random channel

**Oliver Varney**

Imo, There would have to be a latency advantage over TPD (maybe fairly large as well) as processing images into a useful representation will take some time assuming you can correct for visual effects. I guess we will never know without getting the feed. Maybe betfair can add it into their available feeds :grinning:

---

## 2021-10-19 10:47:15 - random channel

**liam**

Are you not seeing the fact the suspensions is based on the feeds rather than the latency? The edge is in the angle when it comes to the drones

---

## 2021-10-19 02:13:10 - general channel

**ThomasJ**

[@U01UN2R5LM8](@U01UN2R5LM8) If my memory serves me correct...the consensus from prior discussions here is that it's best to store the stream as raw data (code is provided by Flumine) and then you can do as you please with that. Eg in your case, read the stored raw data, apply some code to it, store whatever you like in a DB.

---

## 2021-10-18 21:09:03 - general channel

**rjj**

I just get ever increasing latency warnings. Yeah im logging the returned bet ids in one message hence I need to join them at some point. Maybe logging is the issue I will try and surround it with a lock see if that helps

---

## 2021-10-18 18:57:08 - general channel

**rjj**

Question what would be the most appropriate place in a strategy to place a 'sibling' bet on another exchange like smarkets or matchbook. I've tried doing it in process_market_book but if the other exchange is slow in responding then the whole framework complaina of latency. If I try and background the call in a separate thread this seems to cause all manner of difficult to see issues. Any ideas?

---

## 2021-10-17 08:49:50 - random channel

**Oliver Varney**

Morning, im looking for some advice on hosting platforms, mainly AWS vs the rest. I am just about to start re-writing some of my services and was just wondering what peoples thoughts are on the best way to go. From what I understand if I go with AWS (rather then something like linode) im getting a large product/ feature set but in return paying higher costs and potentially slightly slower performance (from what ive read thus far). Is there any specific things around AWS and Betfair/betting that are also advantages of using it. From my understanding betfair are hosted on AWS? im pritty clueless when it comes to this stuff so would be interested in the techy guys thoughts.

---

## 2021-10-17 07:26:38 - general channel

**Mo**

Any idea what the latency is like with sportsmonks?

---

## 2021-10-13 15:25:07 - general channel

**liam**

the heavy CPU is done in bflw so removing from flumine doesn't do much and as you are finding out anything remove gets re-added as it gets pushed from bflw. The latency issues will probably be due to some lazy code?

---

## 2021-10-13 15:17:18 - general channel

**Jono**

should streaming ~1000 markets but only actively running pmb on 20 have any noticeable effect on the performance of the strat on these 20? I know [@U4H19D1D2](@U4H19D1D2) you have mentioned before that number of markets shouldnt noticebly effect performance but now i am streaming 2 orders of magnitude more markets than last month i wanted to be certain since im still wrestling with latency issues ~0.5-1 seconds, even when all that is occurring in process_market_book is a log message

---

## 2021-10-13 14:51:42 - issues channel

**rjj**

Anyone getting latency issues with bf streams api today? Or is it just me?

---

## 2021-10-12 15:16:37 - general channel

**Javier Martín Pérez**

INFO:betfairlightweight.streaming.stream:[MarketStream: 1]: 1.189088929 added, 9892 markets in cache

INFO:betfairlightweight.streaming.stream:[MarketStream: 1]: 1.189089012 added, 9893 markets in cache

WARNING:betfairlightweight.streaming.stream:[MarketStream: 1]: Latency high: 48.739455461502075

WARNING:betfairlightweight.streaming.stream:[MarketStream: 1]: Latency high: 48.65541315078735

WARNING:betfairlightweight.streaming.stream:[MarketStream: 1]: Latency high: 48.55740690231323

WARNING:betfairlightweight.streaming.stream:[MarketStream: 1]: Latency high: 48.459402322769165

---

## 2021-10-11 09:58:01 - random channel

**Finn**

[@UPMUFSGCR](@UPMUFSGCR) have you looked into this? [https://github.com/fmfn/BayesianOptimization](https://github.com/fmfn/BayesianOptimization) I used to use it to tune hyperparameters, not sure if its a good fit for your purpose.

---

## 2021-10-09 11:37:20 - strategies channel

**liam**

No, have a read up on processes and threads, python runs by default on a single process so the only blocker would be the GIL but tbh you can ignore that for now. Threads run in the same process and share memory but don’t block each other (ignoring the GIL)

---

## 2021-10-09 11:30:26 - strategies channel

**Aaron Smith**

When using logging control, is this going to interfer with flumine's main run thread? Can i write stuff into the db straight from the _process_event functions or should i hand it over to something seperate to not slow down the important stuff?

---

## 2021-10-08 13:59:30 - issues channel

**liam**

So few things,



• the market / order streams are in separate threads and main handles the market updates/processing so a slow strategy won’t cause conflation

• workers are also threads so don’t impact anything else (unless they are CPU heavy / bound)

• 100 markets is small and will be very light on cpu 

• check your clock is correct 

• lines are meaningless, it will be what you are doing 

• what are you doing?

• cprofilev is very good at finding slow code 

---

## 2021-10-08 11:54:12 - issues channel

**Lee**

Unless you're placing 50 from the same update then the thread pool should be fine. Just for context i usually have a latency, of &lt; 0.001

---

## 2021-10-08 11:32:08 - issues channel

**Aaron Smith**

I m getting a lot of

```{"asctime": "2021-10-08 10:15:59,227", "levelname": "WARNING", "message": "High latency between current time and OrderPackage creation time, it is likely that the thread pool is currently exhausted", "trading_function": "place", "session": "&lt;requests.sessions.Session object at 0x7f6c242e3450&gt;", "latency": 0.128, "order_package": {"id": "bb7959ae-2820-11ec-8a2b-0a13a1974215", "client": "&lt;flumine.clients.betfairclient.BetfairClient object at 0x7f6c4037dc90&gt;", "market_id": "1.188799555", "orders": ["138529809590672740"], "order_count": 1, "package_type": "Place", "customer_strategy_ref": "run_dogs", "bet_delay": 0, "market_version": null, "retry": true, "retry_count": 0, "async": false}, "thread_pool": {"num_threads": 32, "work_queue_size": 0}}```

today

---

## 2021-10-08 11:02:42 - issues channel

**EJono**

Im experiencing high latency warnings at ~100 markets on flumine. I was wondering best practices broadly speaking for strategy logic so I can improve what I have in my thus far so I can best scale up 



Should not in use market id stand be removed from the strategy?



Is the best way of timing a strategy simply a datetime time stamp comparison at the beginning and end of the process market book function?



I currently have all long running requests executing in workers, but do these effect runtime if executing too often. I have 5 running polling various APIs every 20-30 second. 



For code executing in process market book and process orders should the length of this be limited to 100 lines for example after which conflation is necessary?



Sorry for question dump, any other general pointers to improve speed would be also be greatly appreciated. Cheers!

---

## 2021-10-07 07:14:41 - general channel

**Kunal Maneck**

Does Flumine keep orderbook in memory for query, and can it generate orderbook from cricket tick data?

---

## 2021-10-01 09:18:38 - issues channel

**liam**

the reason you split is because the second part is slow and very likely to be repeated when you realise you have forgotten to parse something, raw bflw is also very quick at processing the files

---

## 2021-10-01 09:16:35 - issues channel

**liam**

but if you are going to be doing slow io/network request in `process_market_book` you will have latency issues as its blocking

---

## 2021-10-01 09:09:01 - issues channel

**Finn**

Performance isn’t really an issue if you can’t tell  haha

---

## 2021-09-29 14:45:07 - general channel

**Finn**

What’s the recommended method to record prices into a custom DB? Flumine middleware? Reading this talk about adjustment factors made me worried I’d miss some element of the data (such as recording scratching times, something I now know I need to add), and I’d be unable to test my strategies even slightly accurately.

I think it matters that I am interested in fundamentals, and I would just like to see when I can place $20-50 bets at a particular price. Nothing high performance required.

---

## 2021-09-28 13:29:25 - general channel

**JC**

Thanks so much, did you run this on a decent EC2 instance for speed?

---

## 2021-09-26 21:54:05 - general channel

**ShaunW**

Thanks Jack. I was just interested in whether the final difference was a slow accumulation or a series of bigger diffs. I think that answers the question pretty clearly.

---

## 2021-09-25 17:40:16 - general channel

**Jack**

Recent performance not been too good?

---

## 2021-09-25 17:39:06 - general channel

**AndyL**

Given my recent performance and reliance on strategies born from backtesting, I'm not sure it matters, quite happy to get i told you so from [@UGV299K6H](@UGV299K6H) on that one!

---

## 2021-09-21 13:18:59 - general channel

**liam**

You just need to watch out for latency if you are doing anything in the strategy as it is blocking

---

## 2021-09-21 12:19:16 - general channel

**ThomasJ**

I want to record to a DB the LTP movements during a race for use by another app. I can do that using a worker and the data in Flumine's  &gt; markets &gt; market &gt; runnerbook  every X secs. no problem.



But I want to speed things up by minimizing the IO to the DB by setting a 'price_changed' flag in the RBcache so that I only do a DB method when something has changed. This attribute ends up in RunnerBook OK.



(I have added attributes to the appropriate classes and have changed serialise/d() to propagate the value of the flag from the RBcache to the RB along with the changed data.)



So after the flag is 'used' I want to reset it to false in RBCache so an old value does not end up in RB.

---

## 2021-09-18 17:36:43 - issues channel

**Aaron Smith**

Also at the same time i tried installing betfairlightweight[speed], which failed at the ciso8601 package, so i only have the orjson one

---

## 2021-09-17 08:45:03 - general channel

**liam**

flumine [https://github.com/liampauling/flumine/blob/master/HISTORY.rst#1200-2021-09-17|v1.20.0](https://github.com/liampauling/flumine/blob/master/HISTORY.rst#1200-2021-09-17|v1.20.0) now released, updated to use bflw 2.14.0 and moves the `listener_kwargs` optimisation down a level in the stack, this results in massive reduction in function calls, I am seeing roughly 2x speed up in backtesting when restricting to inplay only with no loss in functionality :rocket:



Let me know if you have any issues, especially those that have integration tests on backtest markets :thumbsup:

---

## 2021-09-16 19:24:27 - issues channel

**Dave**

attribute access causes latency

---

## 2021-09-13 10:44:27 - random channel

**liam**

The low latency feed betfair are looking to supply is an estimated 3s delay so not quite 'low latency', my understanding is that a lot of the feeds come from guys on the ground via phone (similar to racing with facetime)

---

## 2021-09-12 18:50:56 - general channel

**jhaa**

anybody else having issues with high latency this weekend or is this an issue on my side?

---

## 2021-09-11 13:37:02 - random channel

**Tosin**

I went with the simdjson library and  rough timing shows single digit micro-second latency on average except for occasional jitter that can go to 3 digits

---

## 2021-09-11 12:57:10 - random channel

**thambie1**

Sounds like rapid json is pretty slow. Single digit microsecond is definitely possible, just a question of if it's worth the effort

---

## 2021-09-10 23:01:17 - random channel

**thambie1**

What magnitude of latency are you aiming for?

---

## 2021-09-10 22:56:13 - random channel

**Tosin**

Inspired by flumine, but wanting to go for a low latency approach. I developed(still developing) this: [https://github.com/tosinalagbe/hedg](https://github.com/tosinalagbe/hedg) . If anyone is interested in this approach and knows a bit of C++ , please do chack it out. Would love to see

it tested by anyone other than me. [https://github.com/tosinalagbe/hedg](https://github.com/tosinalagbe/hedg)

---

## 2021-09-09 20:23:40 - general channel

**liam**

I currently do a bit of inbetween by locking an order whilst ‘executing’ and then taking the stream as the golden source, I feel this keeps things simple and removes the potential for race conditions.



However this makes async requests tricky and as you mention it introduces the potential for latency if the response is returned before the stream etc. 

---

## 2021-09-09 15:24:47 - general channel

**liam**

or



```pip install betfairlightweight[speed] --upgrade```

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

## 2021-09-09 15:05:22 - general channel

**liam**

`betfairlightweight` is enough, speed is for speed

---

## 2021-09-09 14:54:08 - general channel

**George**

If I'm using a Mac or Linux, do I still need to install using

```pip install betfairlightweight[speed]```

or is it enough just to do

```pip install betfairlightweight```

---

## 2021-09-08 21:42:04 - general channel

**Jeff Waters**

Thanks Jon.



The big challenge I'm having is aggregating the data.



To be honest, I might revert back to the non multi-processing approach (which, thanks to the help I've received in this forum, is now running at a speed that will allow me to run back tests reasonably quickly). I think that, with my current level of Python knowledge, I could easily spend days getting bogged down in multi-processing, when I could be spending that time creating indicators and running tests.



Saving the data to disk is an interesting idea, btw. One solution could be for me to append each core's results separately to a CSV file. It would then be easy to summarise the results using a spreadsheet or a program that imports the data.

---

## 2021-09-08 19:50:40 - general channel

**Ke**

Any drawback to put in middleware if not to share with different strategies? Would it affect latency? My prediction will use not just market data, would it be easier to plug in 3rd part data in strategy directly?

---

## 2021-09-08 19:39:13 - general channel

**liam**

Best practice would be within the strategy itself unless there is latency involved in the prediction itself in which case you want to push this out to a worker or external process (e.g redis)



Middleware would be suitable if lots of strategies require the prediction as it can be calculated once and then shared. 

---

## 2021-09-08 08:34:25 - general channel

**Jonjonjon**

[@U013K4VNB6D](@U013K4VNB6D) It depends on what you are doing. If you are planning on using Flumine with backtesting and multiprocessing, I would recommend a minimum of 1GB RAM per CPU thread.



So I have 32 CPU threads and 32GB RAM. I will occasionally run out of RAM when backtesting on 31 threads. That could be due to my bad coding, or maybe there's a memory leak (I have a feeling it might be a Pandas memory leak rather than BFLW/Flumine memory leak), but if I'd bought 64GB my life would be easier.

---

## 2021-09-07 14:44:02 - general channel

**Jeff Waters**

No, they are stored in a folder on my C drive.



Because the files are in different folders within the PRO folder, I modified the get_markets method, as I was getting a 'file not found' error message:



```def get_markets(data_dir):

    markets = []

    for dir_, _, files in os.walk(data_dir):

        for file_name in files:

            dirName = Path(dir_).absolute()

            rel_file = os.path.join(dirName, file_name)

            markets.append(rel_file)

    return markets```

I wouldn't have thought that would slow things down, though?



Apart from that, you and I were running the same code.



The fact that you guys aren't seeing any major errors or omissions suggests to me the the slow speed is hardware-related?

---

## 2021-09-07 11:22:18 - general channel

**liam**

Change logging to critical to speed things up, error line 47 in the strategy, should be

```str(len(market.blotter))```

---

## 2021-09-07 09:45:46 - general channel

**Stefan**

Your python code will be always slower, and it is not just about it is interpreted, but how python treat data, for instance what is representation of your api data, dictionary I think.



No problem, you should stick with programming language that best suits you. I use python sporadically, but I would not use it on this kind of projects.

---

## 2021-09-07 09:29:23 - general channel

**liam**

Just give it a handful of markets and see how long it is taking, chances are that something in TestStrategy is slowing it down

---

## 2021-09-07 09:25:37 - general channel

**Jeff Waters**

Thanks [@U4H19D1D2](@U4H19D1D2). I have 4 cores (but no hyperthreading).



My (very limited) understanding of multiprocessing is that it causes Python to use multiple cores. However, given that it is already using all of the cores for back testing, will it give me a speed advantage?



Thanks



Jeff

---

## 2021-09-06 15:49:18 - general channel

**Peter**

I use Colabs a lot for analysis. Love it. But backtesting isn't something that I would do there. There are a number of reasons: it's designed to be run in a browser, which just isn't how I run my backtests at volume, resources are limited, not guaranteed and prioritised for users using the service interactively, and you've got to get all that data up to Google somehow before you can start analysing it.



So my volume backtesting is done on a budget VPS with 12 processors, 48GB of memory and taking advantage of python multiprocessing to ensure that those resources are fully-utilised.

---

## 2021-09-06 13:51:19 - general channel

**Jonjonjon**

If you have plenty of cores and memory, you can also use Python's `multiprocessing` module to run backtests in parallel.

---

## 2021-09-06 13:50:37 - general channel

**Jonjonjon**

[@U013K4VNB6D](@U013K4VNB6D) The time will depend a lot on how much processing your own code does. And how many orders it places.



If you place lots of limit orders, flumine will check them for fills on every market book update. That takes time.



You'll get up to 20 market book updates per second. So if you do time-consuming work in process_market_book, that will increase the time.



It also depends on your CPU and size of data. From memory, on a single-thread, and with a very simple strategy that does virtually nothing, I think my Ryzen 3950x CPU, with a Samsung EVO 970 PRO NVME drive, can process a single GB horse racing WIN file in under 3 seconds. It might even be under 1 second. You can do a crude comparison of your CPU, vs the 3950X, just by comparing the single thread ratings here: [https://www.cpubenchmark.net/cpu.php?cpu=AMD+Ryzen+9+3950X&amp;id=3598](https://www.cpubenchmark.net/cpu.php?cpu=AMD+Ryzen+9+3950X&amp;id=3598)

---

## 2021-09-05 14:20:48 - general channel

**Mo**

Good to know, I’m still thinking of replacing Redis with ZMQ in certain parts of my stack for latency reasons

---

## 2021-09-05 12:07:17 - strategies channel

**Aaron Smith**

the 2 main money makers (not talking about any big numbers still, but enough to pay my bills so i can be chill while playing around with different stuff :smile: ) are one market making and the other taking, so both works. Its difficult to say which is easier, as from what i have seen, different ppl have a really different perception of what is easy to find and what isnt. Both strategies i got running without any backtesting (this is surely not best practice, but i was lacking the data at the time). Backtesting is a strong tool, but sometimes i feel like ppl get lost in it. I still have an intentionally very slow backtest (single core), so i focus more on ideas and only use the backtest to validate an already worked out strategy.

---

## 2021-09-05 11:20:03 - strategies channel

**Newbie99**

and performance monitored for each sub category

---

## 2021-09-05 11:03:27 - random channel

**Mo**

Examples of what we worked on:



• Insurance for a William Hill promotion where you had to predict the exact final Premier League table one season

• Hedging Andy Murray's sponsors' exposure to his on court performance

• Hedging Bundesliga teams' risk of demotion

---

## 2021-09-05 10:38:56 - random channel

**Dave**

Came across this which I am sure some of you guys are already acquainted with: [https://www.airtonrisk.com/](https://www.airtonrisk.com/) - pretty cool, helping sports teams/firms hedge their exposure to performance-based risks (e.g. bonus payouts etc)

---

## 2021-08-31 11:03:06 - strategies channel

**Michael**

Yeah - and the ratios between actual and fully-matched performance. 90% of all analysis time is spent on this.

---

## 2021-08-30 11:55:07 - strategies channel

**Michael**

[@UEA14GBRR](@UEA14GBRR) if you want to view means across a range you've got no choice but to chunk. The other way is to do a running total which you might prefer (fair enough) but that adds a layer of interpretation to understanding the plot as you're having to interpret the change in gradient rather than just looking at the height of the line. For my part I don't see the merit of it, if you're looking at the performance of a variable against profit I think using a running total is quite counter intuitive compared to just looking at the means.

---

## 2021-08-28 16:31:26 - general channel

**Jono**

how often does the betfair ui refresh? im placing using flumine for the first time and i just got wondering since not all the bets placed and alterations can be observed in the ui due to the speed - at least thats what it seems like so far

---

## 2021-08-27 02:56:56 - general channel

**JK**

does anyone have an opinion on the max amount of time you want to be processing the market_book using flumine before it starts to degrade performance?

---

## 2021-08-25 15:12:14 - general channel

**liam**

any latency warnings before this? Are you using the error handling example? where are you located?

---

## 2021-08-25 00:59:53 - strategies channel

**Van**

Don’t see why not. That could incorporate fatigue and explain some of the performance..

---

## 2021-08-24 08:17:33 - general channel

**liam**

For market data it will be your network or maxing out CPU, bet placement flumine tries to keep a few sessions active to reduce latency, the logic could be improved

---

## 2021-08-23 10:16:49 - general channel

**Steve**

I'm in Australia so I always get latency warnings. But that isn't the issue because the df is never correct. the matched amount never shows up in the df.

---

## 2021-08-23 10:14:42 - general channel

**liam**

Are you getting any latency warnings? You could be working off stale data

---

## 2021-08-22 12:58:49 - strategies channel

**Van**

I question the utility of these funds though.

&gt; Priomha’s Fund returns are not correlated to the performance of traditional investment products such as stocks, bonds, property etc. Subsequently, Priomha’s Fund can provide your investment portfolio with valuable diversification.

If COVID stopped all sports, is it really uncorrelated?

It also seems to be a good way to turn tax-free money to taxable money

---

## 2021-08-22 09:36:31 - strategies channel

**Jonjonjon**

Profit by market

 Out of sample performance.

---

## 2021-08-22 08:57:11 - strategies channel

**Adrian**

100% and that's something i'm slowly coming to realise as i learn form you guys how you approach it. The whole strategy and execution side of things wasn't something I considered as a beginner

---

## 2021-08-20 20:46:29 - general channel

**Jack**

Just added a fix for a memory leak

---

## 2021-08-20 17:44:28 - general channel

**Unknown**

Thought I’d been lurking here long enough and about time to contribute something. Just got multiprocessing working over backtests quite nicely and though I would share.

It should figure out how many cores you’re on and pick a good amount of markets for each process.

Implemented a counter as well so you can track progress in a memory safe way across processes (`check_market_book()` in the strategy file) :+1:

---

## 2021-08-20 11:38:03 - general channel

**George**

This morning I tested BFLW's place_orders with no Session passed, and with a Session passed. As advised by Liam, the speedup was quite significant when passing a Session. I wonder whether there is a case for implementing this as the default behaviour in BFLW?

---

## 2021-08-19 19:50:24 - issues channel

**Michael**

It's not like [@UBS7QANF3](@UBS7QANF3)'s saying anything outlandish that's how it works. If your operation is well designed and you don't hit any exceptional circumstances you can expect it to last a long time.



As far as markets changing goes - yes they change but usually gradually. There are occasional step changes like the introduction of cross-matching (I struggle to thing of a second example) and you get weird situations like the pandemic but generally it's a slow evolution.

---

## 2021-08-18 14:51:29 - strategies channel

**thambie1**

If you want to save $5 a month, go for it. A VM will be easier to maintain. It will have stable power and internet. It will likely have lower latency too.

---

## 2021-08-17 12:27:17 - issues channel

**Jack**

Hi everyone, I hope that this is the right place for this question.



I believe that my backtests are running much slower than they are supposed to after reading some of the posts here. [@U4H19D1D2](@U4H19D1D2) mentioned that Flumine is capable of running 1000's markets a minute out of the box, and I am getting something more like 1 market per second or worse.



To check what was is going on I am running a slightly modified flumine example `backtest.py` (added `"listener_kwargs"` and removed logging to speed things up).



```import time



from flumine import FlumineBacktest, clients

from strategies.lowestlayer import LowestLayer



client = clients.BacktestClient()



framework = FlumineBacktest(client=client)

markets = ['data/1.181018785', 'data/1.181018790', 'data/1.181018780', 'data/1.181018795']



strategy = LowestLayer(

    market_filter={"markets": markets,

	"listener_kwargs": {"inplay": False, "seconds_to_start": 600}},

    max_order_exposure=1000,

    max_selection_exposure=105,

    context={"stake": 2},

)



framework.add_strategy(strategy)



start = time.process_time()

framework.run()

end = time.process_time()



print("time taken: ", end-start)```

Output:

`time taken:  10.760373999999999`



I have run this on two machines now, one is a 2017 Macbook Pro, the other is a pretty beefy Desktop rig with an intel 9600k CPU and 16GB of RAM. Both have similar results.



Appreciate if anyone knows whether this is expected or if I am not set up correctly. Thanks!

---

## 2021-08-12 23:03:23 - general channel

**liam**

You don’t care about latency and/or don’t plan on making another request 

---

## 2021-08-12 11:25:36 - general channel

**Mo**

You seem to think courtsiding is a loaded term. I’m just using it as a colloquialism for latency arbitrage

---

## 2021-08-12 11:05:46 - general channel

**liam**

you can still pass params such as locale etc. but flumine will create a session on any latency sensitive calls

---

## 2021-08-12 10:42:53 - general channel

**George**

wow! anything else i should know for latency sensitive BFLW users?

---

## 2021-08-12 10:40:50 - general channel

**George**

just seen this in BaseEndpoint:

```param Session session: Requests session to be used, reduces latency.```

so passing in an already active session reduces latency? by how much roughly do we think?

---

## 2021-08-12 07:53:27 - random channel

**Laybot McBackbot**

One thing I learned from losing a lot -- if a couple of mistakes (regardless of the sources) could significantly ruin your P/L -- then it's probably not a good system.  These days I am spending most of my time backtesting and compiling all the worst possible outcome that I came across in my testing/live and whatever strat I come up with must be able to survive those.



Of course,  past data is no indicator of future performance but how could one say a system is working if it could not even do well when backtested? :sweat_smile:

---

## 2021-08-09 16:35:22 - general channel

**Mo**

I agree performance is a problem so think C/C++ is a reasonable alternative

---

## 2021-08-09 16:28:35 - general channel

**S G**

sure, I was more interested in performance aspects of both libraries

---

## 2021-08-09 16:26:32 - general channel

**S G**

I was about to ask diffs between Flumine and bflw. is Fulmine slower considering that only works with clients that has lightweight=False

---

## 2021-08-09 16:25:58 - general channel

**thambie1**

Harder to read code, harder to debug, harder to guarantee it works as you expect, slower

---

## 2021-08-08 11:47:56 - strategies channel

**Unknown**

these Friendly games are dying out, they're roughly 2.5% of games currently and excluding them from the model also means excluding them from betting so it's as if they never happened (and the hypothesis is that the presence of them does not have some predictive ability on performance in competitive leagues). The top chart is total number of games per day across all competitions in my dataset, and the bottom is Friendlies only

---

## 2021-08-08 11:24:38 - strategies channel

**Dave**

Yeah that's a good question for me - nope I don't model individual player performance. I guess the real question is what should I expect to be similar between team A vs B in a friendly league when compared to team A vs B in a competitive league. I don't follow football enough (or much at all really) to know this nuance, but perhaps it might be more common domain-specific knowledge for more religious football followers.

---

## 2021-08-08 11:11:14 - strategies channel

**Mo**

I suppose an equivalent question would be do you model individual player performance

---

## 2021-08-08 11:09:29 - strategies channel

**Mo**

Would these international performances only affect your team strengths for international teams or would they also filter down to club level?

---

## 2021-08-08 09:50:44 - strategies channel

**Dave**

those trading football - are you doing anything to your models to exclude any performance from the recent international friendlies matches?

---

## 2021-08-07 11:28:45 - strategies channel

**Michael**

It totally depends on what kind of markets you're betting in. For what [@U4H19D1D2](@U4H19D1D2) and I do every penny counts, in other scenario's it'll be different scales but the mechanisms are the same. As a broad brush: If you have a big modelling, speed or data edge then you'll be a bit less stake sensitive because you'll be taking all you can get whereas if you're more about betting off market dynamics phenomena you'll be more so.

---

## 2021-08-06 19:55:12 - strategies channel

**Michael**

In all seriousness though - I would suggest that you think about this. I'm going to guess that your stakes are somehow proportional to prices? You could consider randomising them in a range that would keep your average exposure the same for your comfort but would generate stake/return data. Use discrete price increments and track the performance of each increment in each price bracket against the 'ideal' performance of the bets if fully matched at requested odds. You'll learn a lot from it.

---

## 2021-08-06 18:48:23 - strategies channel

**Michael**

[@U016TGY3676](@U016TGY3676) As far as I'm concerned optimising execution is mostly just deciding what prices and sizes to bet at. There are a couple of little tricks that can help but price and size is most of it. Some people look for speed edges but that's a specialist thing and honestly beyond most of us - it's certainly beyond me so I choose my battles. The basics of it are totally obvious - if you lay too long you lose on the price and if you lay too short you don't get matched so it's finding the optimum. Mostly I try to do that with graphs and I use quite a bit of randomisation but it's always rather unsatisfactory. Likewise stakes. Similarly obvious dynamics and similar strategy. It's not unusual for beginners to assume that they can take a model that makes a bit of money on small bets and scale it in a linear way to make life changing returns but it should be quite obvious to a moderately smart person that that's not how it works. I don't think anyone who's ever posted on here would make such a moronic mistake and if they did I certainly wouldn't point and laugh.



The other sorts of questions you're thinking about would be whether to spread your bets over a range of prices, whether there's a back equivalent for your lays on another runner, that sort of thing. There are some tricks to do with delaying bets and there are some other sprinkles but that's most of it.

---

## 2021-08-06 13:45:27 - strategies channel

**Dave**

It's difficult to generalise this I think. For example, in football you have new leagues starting every few weeks in all sorts of regions....I spend a fair bit of time maintaining models for so many leagues, investigating if a model is ready to be deployed for a recently started league etc. Per-league effort is probably quite small but it adds up, and then you need time for execution optimization, and r&amp;d into new features. Maybe racing markets are more stable in this regard (idk). This is coming from a truly fundamental approach.

---

## 2021-08-06 11:04:24 - strategies channel

**liam**

I think it is very dependant on where your edge lies, my weak link is strategy development so my focus is on execution, infra/ease of deployment, rt analysis and speed (probably in that order)

---

## 2021-08-04 12:14:13 - general channel

**liam**

However since the major streaming refactor in 2.12, I haven't actually benchmarked speed

---

## 2021-08-04 12:10:36 - general channel

**river_shah**

[@U4H19D1D2](@U4H19D1D2) can we please discuss what `betfairlightweight[speed]` actually does / how it is compiled / any [https://github.com/liampauling/betfair/blob/master/docs/advanced.md|benchmarks](https://github.com/liampauling/betfair/blob/master/docs/advanced.md|benchmarks)? I have not made an effort to dig through this aspect of the code yet, but any direction from your side will help me understand better. Thanks

---

## 2021-08-04 09:59:01 - strategies channel

**Mo**

I don't think it's a function of time. You should be asking questions like is the recent performance in line with the variance observed in the backtest? Have any metrics changed that might indicate a change in market conditions?

---

## 2021-08-03 09:43:55 - random channel

**Oliver Varney**

The rationale for maybe populating the lower levels is that the user doesnt have to constantly check whether each level is None or not  and im not sure whats preferable. i.e. if you have a horse object that has a attribute flat_statistics which include like number of runs, percentage of wins etc, if for some horses its provided and other its not you would have to constantly check whether it exsists and that just for one level. Performance would not be a concern as its just a regular get request with unlikely need to constantly poll.

---

## 2021-08-02 21:18:11 - strategies channel

**ShaunW**

Can't give concrete advice cos I don't know exactly what you're doing but is there a 2nd way to measure your performance? Simplistic example would be backing at fractionally better than SP, the gods of random could give you nightmares but you know your theoretical returns are sound and given enough time you'll catch up. Is your net position at the off looking good even though the actual return isn't?

---

## 2021-08-02 17:11:57 - strategies channel

**thambie1**

When I first started and was concerned about my strategy's performance, I'd just buy more backtest data :sweat_smile:. Can never have too much data

---

## 2021-08-01 11:37:36 - general channel

**thambie1**

I was messing around with my simulated execution latency in backtests, and saw flumine defaulted to 0.12 for placing orders, and 0.17 for cancelling. Why would cancel latency be greater than place?

---

## 2021-07-27 22:12:15 - general channel

**Dave**

There are a billion and one tutorials written by kagglers which give decent tips on hyperparameter tuning and measuring model performance

---

## 2021-07-27 15:17:29 - general channel

**liam**

Considering speed is important and the data size is tiny, yes, I wouldn't look to move this out to a dedicated k/v store until you start hitting the limitations of python or need multi process support etc. Easy to get lost and waste a lot of time on over engineering stuff like this (imho)

---

## 2021-07-27 13:23:17 - general channel

**James**

What's the fastest way to write/read/clear data with a time series in python? I've got a script that scrapes data every few seconds and stores it in a mysql database. It deletes data more than x seconds old so there's usually only 5 records of 2 fields. One is the scrape time the other is the data, a 20 digit number. Speed is important and using mysql seems OTT

---

## 2021-07-26 22:13:10 - general channel

**George**

What do we think is the theoretical minimum value for this network latency?

---

## 2021-07-26 22:12:46 - general channel

**George**

Latency. So i logged the raw updates directly from listener.py (as I was advised not to do!) and compared my timestamp to the Betfair publishTime value. The reason I did this is because the difference between my log timestamp and the Betfair publishTime should be equal to the network latency (assuming logging is negligibly fast).

---

## 2021-07-26 12:12:58 - general channel

**George**

just to log the latency!!

---

## 2021-07-26 11:03:54 - general channel

**George**

Just going back to this briefly [@U4H19D1D2](@U4H19D1D2) if you don't mind. I probably want to record what time I received the raw update. This would be useful because then I can deduct the publish-time from this and determine the latency. What would be the best way of doing this without using the listener.py logger?

---

## 2021-07-25 10:06:19 - issues channel

**azevedo**

[@UBS7QANF3](@UBS7QANF3) in your experience, do you see much competition for those sort of sub millisecond latencies? as in do you think you would make more money should you drop this latency from 300microseconds to say 30 microseconds?

---

## 2021-07-25 09:13:55 - issues channel

**Mo**

You seem to be talking about throughput rather than latency?

---

## 2021-07-25 09:05:59 - issues channel

**Mo**

If you care about latency then that number is huge. If you don’t care about latency then :man-shrugging:

---

## 2021-07-25 07:22:27 - issues channel

**Oliver Varney**

I think it was billed as an alternative / replacement with more functionality. A stream is a different datastructure (has memory / storage) but communication functionality similar to pub/sub can be achieved easily.  Its sub milliseconds read from anywhere off the stream. Im not too sure of the scale of your sub/pub and whether that would have any effect performance as my use case I guess isnt that complex. Typically I use it for IPC communication. Its real strength is saving timestamped data such as analytics which can be retrieved between ranges in sub millisecond using timestamps.

---

## 2021-07-24 22:19:45 - issues channel

**azevedo**

[@UBS7QANF3](@UBS7QANF3) you won’t recommend using redis pub/sub for redistributing Betfair streaming messages to multiple processes? I assumed that’s what you had set up?



does redis streaming have better performance vs pub/sub for that sort of thing? [@ULDAVFDRP](@ULDAVFDRP) 

---

## 2021-07-24 22:10:24 - issues channel

**Mo**

Yeah it would be for performance reasons 

---

## 2021-07-24 09:09:20 - issues channel

**river_shah**

The author has moved on to nanomsg but that is for more ultra low latency stuff. 

---

## 2021-07-23 09:17:59 - general channel

**liam**

Regarding the streaming update filter, the simulation middleware does [https://github.com/liampauling/flumine/blob/a7aff28371b1a7a30122dfd76a1effcee4ddc127/flumine/markets/middleware.py#L40|this](https://github.com/liampauling/flumine/blob/a7aff28371b1a7a30122dfd76a1effcee4ddc127/flumine/markets/middleware.py#L40|this) you can actually take [https://github.com/liampauling/flumine/blob/a7aff28371b1a7a30122dfd76a1effcee4ddc127/flumine/markets/middleware.py#L169|this](https://github.com/liampauling/flumine/blob/a7aff28371b1a7a30122dfd76a1effcee4ddc127/flumine/markets/middleware.py#L169|this) function as is to get a list of runners that have been updated. Was shown to have a big impact on speeding up that code, quickest way to make code quick is to not execute it :wink:

---

## 2021-07-23 07:39:17 - general channel

**liam**

You also have the conflate var on streaming to slow down the number of updates if you don’t need every update 

---

## 2021-07-23 07:38:10 - general channel

**liam**

So you can use the streaming update to tell you which runner has been updated, that can speed things up

---

## 2021-07-23 07:30:05 - general channel

**liam**

I think you answered your own question, it won’t be bflw that is slow/blocking 

---

## 2021-07-23 07:29:16 - general channel

**Adrian**

speed isn't really my concern, i'm just trying to reduce any possible blocking from creating my numpy arrays from ltp and other vars

---

## 2021-07-22 22:39:37 - strategies channel

**Dave**

Oh I just remembered... The bayes_opt package is kind of a stepping stone in between basic regression and ML. You can define a custom optimization target as a function, and provide a search space of parameters and it will optimize for you. [https://github.com/fmfn/BayesianOptimization](https://github.com/fmfn/BayesianOptimization) (usual data science practices apply ofc to avoid overfitting etc).

---

## 2021-07-22 08:34:24 - strategies channel

**Oliver Varney**

yes train/test performance diverges fairly quickly in my experience, but thats most likely due to features not being predictive enough. That will apply to pritty much all optimisations though I would of thought.

---

## 2021-07-20 10:26:12 - general channel

**Mo**

[@UUUAJQZ5J](@UUUAJQZ5J), sort of, and I think the latency is actually overstated in the documentation, based on my preliminary work on implementing the virtualisation. However, the other points are pretty important I think. For example, any kind of logic involving wanting to be exclusive best price/stepping inside the market is going to be thrown off by 3.

---

## 2021-07-20 09:53:45 - general channel

**KG**

really it comes down to how efficient you can be in calculating the 'cross matching' values yourself right, [@UBS7QANF3](@UBS7QANF3)?  I believe the latency associated with pulling the feed with virtual bets is ~100ms delayed compared to without

---

## 2021-07-20 08:25:25 - general channel

**Mo**

A few points:



1. As previously discussed on here, the virtual price stream is delayed relative to the non-virtual one. You reduce latency by receiving the non-virtual price stream and doing the virtualisation yourself

2. The virtual price stream is limited by ladder levels so you cannot see the full order book

3. The virtual price stream has roll-up applied so you do not know the true best price if the volume available at that price is less than £1

4. I _believe_ that it is easier to remove your own orders from the order book using the non-virtual price stream then do the virtualisation yourself rather than trying to remove them from the virtual price stream

---

## 2021-07-13 20:16:06 - strategies channel

**thambie1**

[@U01PJ5YMFBJ](@U01PJ5YMFBJ) The first thing I'd suggest doing is verifying the accuracy of your backtest. And understanding all differences between live and backtest performance. If you do that, you can then launch strategies with a high degree of confidence even if they hit an initial downswing

---

## 2021-07-10 15:39:47 - general channel

**liam**

I have found the optimum for me to be 8 processes (m1 8 core) and then chunk into 16 markets per flumine instance, there will be a slight memory leak if you go higher due to some of the loops so it’s better to keep markets per instance as low as possible (flumine startup time is negligible) 

---

## 2021-07-10 14:27:57 - general channel

**Dave**

Fair enough, yeah you gotta be careful with memory leaks I suppose. When I backtest I split my markets into n_worker chunks, spin up n_workers and give them each a chunk. Avoids the overhead of flumine startup on each market basically

---

## 2021-07-10 14:05:33 - general channel

**Jonjonjon**

My solution obviously has performance overhead due to spinning up the processes. I timed it at 4.5 seconds per 1,000 processes.

---

## 2021-07-09 08:53:41 - general channel

**Mo**

To clarify I'm talking about the raw stream, obviously I'm not up to speed with what flumine does or even how bflw handles the cache

---

## 2021-07-05 08:59:36 - general channel

**Mo**

1. Better to use the raw stream live because of the latency of the virtual stream

2. Can always go raw -&gt; virtual, I would imagine it's impossible to go the other way

---

## 2021-07-05 01:39:53 - general channel

**Adrian**

I think i found the reason for this and it is a design decision:

&gt; """"

&gt; django style `lazy` object creation, the main bulk of processing

&gt; is turning {priceSize} into &lt;PriceSize&gt; objects but this is

&gt; pointless a lot of the time as the object is not used or can be

&gt; handled as a dict instead.

&gt; The inclusion of slots further reduces the processing time as well

&gt; as reducing memory.

&gt; This optimisation will improve normal streaming as well as

&gt; backtesting, with more speed, less CPU + ram and minimal reduction

&gt; in usability.

&gt; """

---

## 2021-07-03 10:42:20 - issues channel

**Adrian**

Could someone tell me where would be the appropriate place to insert a resource intensive algo into flumine? I tried placing it in process_market_book but that led to this error: "WARNING", "message": "High latency between current time and MarketBook publish time". Thanks!

---

## 2021-06-26 21:11:48 - general channel

**Dave**

[@U01DCR5PXDY](@U01DCR5PXDY) how's your euros performance been?

---

## 2021-06-25 13:24:31 - strategies channel

**Michael**

Oh well that's easy you can just back-test both and see how the back-tests compare. How they compare to real performance is a different thing, but assuming the strategies are comparable the back-tests will be and likewise the respective relationship to real performance.

---

## 2021-06-23 09:29:51 - issues channel

**Newbie99**

[@U4H19D1D2](@U4H19D1D2) I've noticed something else about the Replace function (I'm guessing most people just cancel and place a new order, which perhaps I should do!), below the replace fails as the bet has already had an action on it, that error makes sense, however after this the order is never removed from the blotter and the status remains as OrderStatus.REPLACING until I kill the process. This of course means no further orders can be placed on this runner as the blotter thinks there is 1 order remaining. This is obviously a pretty rare occurrence, but I've noticed it a few times and I think the below shows the process flow, but at the end presumably a better outcome would be that the order is removed (i.e. set to EXECUTION_COMPLETE) instead?



This is going to be very tricky to replicate, but if you agree its a bug I'll raise an issue (this is in live btw not simulation).



```{"asctime": "2021-06-22 18:50:10,695", "levelname": "INFO", "message": "execute_replace", "trading_function": "replace", "elapsed_time": 0.05340576171875, "response": {"customerRef": "abcf9b20d38a11ebbbac02054918c7c6", "status": "FAILURE", "errorCode": "BET_ACTION_ERROR", "marketId": "1.183248116", "instructionReports": [{"status": "FAILURE", "errorCode": "BET_TAKEN_OR_LAPSED", "cancelInstructionReport": {"status": "FAILURE", "errorCode": "BET_TAKEN_OR_LAPSED", "instruction": {"betId": "236404314713"}}, "placeInstructionReport": {"status": "FAILURE", "errorCode": "RELATED_ACTION_FAILED"}}]}, "order_package": {"id": "abcf9b20-d38a-11eb-bbac-02054918c7c6", "client": "&lt;flumine.clients.betfairclient.BetfairClient object at 0x7f148822e790&gt;", "market_id": "1.183248116", "orders": ["236404314713"], "order_count": 1, "package_type": "Replace", "customer_strategy_ref": "ip-172-31-4-105", "bet_delay": 0, "market_version": null, "retry": true, "retry_count": 0, "async": false}}

{"asctime": "2021-06-22 18:50:10,701", "levelname": "INFO", "message": "Trade status update: Pending", "id": "511443a4-d388-11eb-bbac-02054918c7c6", "strategy": "politics_lay_mm", "place_reset_seconds": 0.0, "reset_seconds": 0.0, "orders": ["236404314713"], "offset_orders": [], "notes": "", "market_notes": null, "status": "Pending", "status_log": "Pending, Live, Pending, Live, Pending, Live, Pending"}

{"asctime": "2021-06-22 18:50:10,707", "levelname": "INFO", "message": "Order status update: Executable", "market_id": "1.183248116", "selection_id": 5191378, "handicap": 0.0, "id": "236404314713", "customer_order_ref": "3203239236f2d-236404314713", "bet_id": "236404314713", "date_time_created": "2021-06-22 18:33:19.422805", "publish_time": null, "trade": {"id": "511443a4-d388-11eb-bbac-02054918c7c6", "strategy": "politics_lay_mm", "place_reset_seconds": 0.0, "reset_seconds": 0.0, "orders": ["236404314713"], "offset_orders": [], "notes": "", "market_notes": null, "status": "Pending", "status_log": "Pending, Live, Pending, Live, Pending, Live, Pending"}, "order_type": {"order_type": "Limit", "price": 1000.0, "size": 0.09, "persistence_type": "PERSIST", "time_in_force": null, "min_fill_size": null, "bet_target_type": null, "bet_target_size": null}, "info": {"side": "LAY", "size_matched": 0.0, "size_remaining": 0.09, "size_cancelled": 0.0, "size_lapsed": 0.0, "size_voided": 0.0, "average_price_matched": 0.0}, "responses": {"date_time_placed": null, "elapsed_seconds_executable": null}, "runner_status": null, "status": "Executable", "status_log": "Executable, Replacing, Executable, Replacing, Executable, Replacing, Executable, Replacing, Executable", "violation_msg": null, "simulated": {"profit": 0.0, "piq": 0.0, "matched": []}, "notes": "", "market_notes": null}

{"asctime": "2021-06-22 18:50:10,718", "levelname": "INFO", "message": "Order status update: Replacing", "market_id": "1.183248116", "selection_id": 5191378, "handicap": 0.0, "id": "236404314713", "customer_order_ref": "3203239236f2d-236404314713", "bet_id": "236404314713", "date_time_created": "2021-06-22 18:33:19.422805", "publish_time": null, "trade": {"id": "511443a4-d388-11eb-bbac-02054918c7c6", "strategy": "politics_lay_mm", "place_reset_seconds": 0.0, "reset_seconds": 0.0, "orders": ["236404314713"], "offset_orders": [], "notes": "", "market_notes": null, "status": "Pending", "status_log": "Pending, Live, Pending, Live, Pending, Live, Pending"}, "order_type": {"order_type": "Limit", "price": 1000.0, "size": 0.09, "persistence_type": "PERSIST", "time_in_force": null, "min_fill_size": null, "bet_target_type": null, "bet_target_size": null}, "info": {"side": "LAY", "size_matched": 0.0, "size_remaining": 0.09, "size_cancelled": 0.0, "size_lapsed": 0.0, "size_voided": 0.0, "average_price_matched": 0.0}, "responses": {"date_time_placed": null, "elapsed_seconds_executable": null}, "runner_status": null, "status": "Replacing", "status_log": "Executable, Replacing, Executable, Replacing, Executable, Replacing, Executable, Replacing, Executable, Replacing", "violation_msg": null, "simulated": {"profit": 0.0, "piq": 0.0, "matched": []}, "notes": "", "market_notes": null}

{"asctime": "2021-06-22 18:50:10,718", "levelname": "INFO", "message": "Trade status update: Live", "id": "511443a4-d388-11eb-bbac-02054918c7c6", "strategy": "politics_lay_mm", "place_reset_seconds": 0.0, "reset_seconds": 0.0, "orders": ["236404314713"], "offset_orders": [], "notes": "", "market_notes": null, "status": "Live", "status_log": "Pending, Live, Pending, Live, Pending, Live, Pending, Live"}

{"asctime": "2021-06-22 18:50:10,719", "levelname": "INFO", "message": "Thread pool submit", "trading_function": "execute_replace", "session": "&lt;requests.sessions.Session object at 0x7f144b600050&gt;", "latency": 0.0001, "order_package": {"id": "abdbd200-d38a-11eb-bbac-02054918c7c6", "client": "&lt;flumine.clients.betfairclient.BetfairClient object at 0x7f148822e790&gt;", "market_id": "1.183248116", "orders": ["236404314713"], "order_count": 1, "package_type": "Replace", "customer_strategy_ref": "ip-172-31-4-105", "bet_delay": 0, "market_version": null, "retry": true, "retry_count": 0, "async": false}, "thread_pool": {"num_threads": 32, "work_queue_size": 1}}

{"asctime": "2021-06-22 18:50:10,719", "levelname": "CRITICAL", "message": "Execution unknown error", "exc_info": "Traceback (most recent call last):\n  File \"/home/ec2-user/trading/env/lib64/python3.7/site-packages/flumine/execution/betfairexecution.py\", line 243, in _execution_helper\n    response = trading_function(order_package, http_session)\n  File \"/home/ec2-user/trading/env/lib64/python3.7/site-packages/flumine/execution/betfairexecution.py\", line 214, in replace\n    instructions=order_package.replace_instructions,\n  File \"/home/ec2-user/trading/env/lib64/python3.7/site-packages/flumine/order/orderpackage.py\", line 152, in replace_instructions\n    return [order.create_replace_instruction() for order in self]\n  File \"/home/ec2-user/trading/env/lib64/python3.7/site-packages/flumine/order/orderpackage.py\", line 152, in &lt;listcomp&gt;\n    return [order.create_replace_instruction() for order in self]\n  File \"/home/ec2-user/trading/env/lib64/python3.7/site-packages/flumine/order/order.py\", line 394, in create_replace_instruction\n    bet_id=self.bet_id, new_price=self.update_data[\"new_price\"]\nKeyError: 'new_price'", "trading_function": "replace", "exception": "'new_price'", "order_package": {"id": "abdbd200-d38a-11eb-bbac-02054918c7c6", "client": "&lt;flumine.clients.betfairclient.BetfairClient object at 0x7f148822e790&gt;", "market_id": "1.183248116", "orders": ["236404314713"], "order_count": 1, "package_type": "Replace", "customer_strategy_ref": "ip-172-31-4-105", "bet_delay": 0, "market_version": null, "retry": true, "retry_count": 0, "async": false}}

{"asctime": "2021-06-22 18:50:10,719", "levelname": "INFO", "message": "1 order packages executed in transaction", "market_id": "1.183248116", "order_packages": [{"id": "abdbd200-d38a-11eb-bbac-02054918c7c6", "client": "&lt;flumine.clients.betfairclient.BetfairClient object at 0x7f148822e790&gt;", "market_id": "1.183248116", "orders": ["236404314713"], "order_count": 1, "package_type": "Replace", "customer_strategy_ref": "ip-172-31-4-105", "bet_delay": 0, "market_version": null, "retry": true, "retry_count": 0, "async": false}], "transaction_id": 10}

{"asctime": "2021-06-22 18:50:10,722", "levelname": "INFO", "message": "Deleting requests.Session", "sessions_created": 14, "session": "&lt;requests.sessions.Session object at 0x7f144b600050&gt;", "session_time_created": 1624387784.7466655, "session_time_returned": 1624387810.701893, "live_sessions_count": 0, "err": true}```



---

## 2021-06-21 11:47:10 - strategies channel

**Michael**

In terms of workflow I also do all analysis in jupyter notebook using Pandas. What I actually do is process every market file into an equivalent compressed csv which includes all derived variables. Then I extract the subset of data points that I'm interested in from each market file into another CSV and load that up into my notebook.  So maybe I want 1/5th of all instances where 1.5 &lt; best available back price &lt; 2 or whatever. That way I don't have to re-process all my markets every time I want a different data set, just relatively quickly extract what I need. I do both the initial processing and the extraction using multiprocessing and when I get frustrated by slowness I buy a new computer.

---

## 2021-06-20 21:43:32 - strategies channel

**Peter**

[@U01PJ5YMFBJ](@U01PJ5YMFBJ) Completely agree with [@U4H19D1D2](@U4H19D1D2) re: Pandas. It's like a cross between a spreadsheet on steroids and a database without all the overhead, but with the added benefit of transparently supporting parallel processing across however many CPU (or GPU) cores are available to it. If you've not used it before, investing some time there would dramatically speed up your analyses, making it easy to load and analyse data and then keep tweaking your parameters as you home in on finding value. Backtesting general revolves around a strategy about which you already have some confidence and running it against a large number of market files - a much slower process.

---

## 2021-06-20 11:11:43 - strategies channel

**PeterLe**

Yes its given me a good idea and ive stuck with those settings for a long while now. Once I found what I thought was the best fit, I would then turn to the next variable, lets say bet position and then go through the same process. Then onto the next etc. In my mind a logical methodical approach.

I was wondering how some of you guys go about using linear regression to model rather than the blunt/slow  approach that I have taken.

---

## 2021-06-20 10:39:28 - strategies channel

**PeterLe**

[@U4H19D1D2](@U4H19D1D2) /All, So how might you go about doing this in practice? Lets say you had a laying system and one key variable you wanted to test (fill/kill). 

If the Fill/Kill was too fast, (and it can be) you would miss opportunities and too slow you’d get taken to the cleaners.

Over the years I have reached what I think is near an optimum through trail and error. 

What would be the steps you would take in practice (could you only do this by backtesting?) Or maybe you would use backtesting to get in a range and then fine tune by live testing perhaps?

Thanks in advance

---

## 2021-06-19 09:04:20 - strategies channel

**Oliver Varney**

me telling you your approach is very slow and flawed wont give away my advantage over you and will help you save time. Me telling you what data I input, what the learning task is, what are good indicators,  what to look out for / take advantage will give away my advantage over you and the 1000 others in here.

---

## 2021-06-18 20:46:18 - strategies channel

**Dave**

Yeah...this is what I do actually when I do my retraining, I rerun my old model on the same out of sample set and assert performance at least doesn't degrade

---

## 2021-06-18 20:45:27 - strategies channel

**Oliver Varney**

Generally you should have an idea of the maximum performance of your data, if its past this then generally stinks of something going wrong

---

## 2021-06-18 20:33:50 - strategies channel

**Dave**

Nah, football. For my forecasting target and features, anything over 4-6 months has never added additional predictability. 4 months gives me 20-30,000 samples too which is sufficient to obtain good OOS performance. I put it down to change in dynamics as a competition progresses through its stages tbh. Im sure there are people for whom 10 years of data in football is useful tho, but their features must be way diff to mine 

---

## 2021-06-16 19:06:09 - strategies channel

**Dave**

Individual team performance has rather high variance, probably better to cluster teams first maybe and then use those clusters as features

---

## 2021-06-16 16:56:32 - strategies channel

**Frankz**

currently main problem is that from training with 10,000 rows and 100,000 rows the training speed increases quite a lot. I mean I could scrap the team id and replace it with a kickscore rating or try with catboost instead.

---

## 2021-06-16 09:47:25 - strategies channel

**Michael**

Truthfully I'm not sure what the best mathematical way of doing it is. For my own part it's a 'lick of the finger' thing, I know what the difference has been in the past so I go with that. You always have to assume a bit of adverse selection, but what you're really looking for here is an overfit bias - which doubtless has a proper mathematical name but I don't know what it is.



There are statistical ways of estimating over fit that others can elucidate better than I can, my own approach would be more about evaluating the process and one's own level of experience. You can simply step back and ask yourself honestly _'what's the probability that I did this right?'_



Having done that; if you have promising results I'd still usually advocate a very slow and cautious switch on starting only with your best bets - i.e. those bets where your signals are strongest. Impatience never pays, if your strategy is sound there's no reason to rush and if it's not sound you'll be glad you didn't.

---

## 2021-06-15 16:34:26 - general channel

**river_shah**

lowest layer is just an example strategy. considering that you need to get your python skills up to speed first, my recommendation is don’t worry about recording data just yet. “buy” some of the free pro data and see if you replay back a market file. go into flumine github repo and follow the examples.



put a breakpoint after `def process_market_book(self, market: Market, market_book: MarketBook) -&gt; None:`see if the data structures make sense to you. get a good ide or editor such as pycharm or vs code. bring up python skills first and then the code will make a lot more sense.

---

## 2021-06-12 01:42:14 - strategies channel

**birchy**

[@U01PJ5YMFBJ](@U01PJ5YMFBJ) I've been sat on the sidelines reading the various threads on here and feel your frustration with this whole "easy money" malarkey. I've been interested in gambling for over 30 years. For the first couple of years, I was a typical "mug" punter who did a 25p EW Lucky 15 every Saturday and watched the horse racing on TV. It was great entertainment and not a particularly expensive hobby, because I was pretty decent at reading form and had a lot of "unusual" insights that gave me a slight edge. During that time, my father and I decided to put £10 each into a pot and we both picked a few horses every Saturday. I always placed mine as single bets, ranging from £1 to £10 depending on how strongly I felt about the horse's chance of winning. He always did a Lucky 15 or a 3 horse Patent. From that point onwards, I no longer did Lucky 15s or any other kind of multiple bet beyond a (very) occasional EW double. And that was because I realised quite early on, that when I had 1 or 2 winners out of the 4, that backing them as singles paid out far more often, albeit at the cost of missing out on "the big one". But more crucially, I also realised that you could build a bank by taking lots of small profits rather than waiting for occasional bigger payouts. After 18 months, we had just over £1000 in the pot, most of which came from my bets. We split it 50/50 because I'd just discovered beer and women. The money didn't last long.

Several years later, I started looking at betting again and developed many strategies, writing them all in a notepad. Around 1999/2000, I bought my first laptop and discovered spreadsheets. And porn. One pixel at a time, because internet was dial-up back then. I learnt VBA because Excel just wasn't cutting it. Then VB6 because VBA was too slow. Then I discovered Flutter, who were bought out by Betfair shortly after. While watching the markets in bewilderment, I noticed that the books would occasionally go the wrong side of 100%. Knowing how bookies made their money, I attempted to catch these spikes manually. It didn't go well. So I made it my mission to automate it. It took me the best part of a year to learn how HTTP, HTML, Ajax, etc worked. It was hard going as I was never academically minded. But I never gave up. Finally, I had a home-made web browser spoofing, 50 times a second polling, page scraping, data collecting, bet placing API that (so I thought) was totally unique. Another year or so of tweaking and testing followed. I made a few grand from that strategy, but it took me several years to get there. Then competition started to grow and finally, it died a long, slow death, particularly when cross-matching was introduced.



Roll forward to the present.... I still have lots of "wacky" strategy ideas that I need to test but rarely have enough time to give them the devotion they need. The markets are far more efficient nowadays than they were years ago, BUT small edges (&lt;=0.5% ROI) are still fairly easy to find and can make reasonable long-term profits with lower variance. The biggest issue with these is getting large quantities of bets matched. You won't become a millionaire overnight, but it's a step in the right direction.



To put things in perspective, the professionals on here are generally peaking at 4% or 5% ROI over millions of bets. Mere mortals like us can't even get close to that level without a LOT of work. Or a lucky find.



So my suggestion is: go right back to basics. Pick an obvious strategy like laying 3 runners at &lt;3.0, backing both players in 2-player markets to achieve a book &lt;100% or even laying any runner&lt;2.0. If executed correctly, all of these will make a small profit. And it's obvious why. Then work on increasing your match and hit rates. Pick ONE strategy and do everything you possibly can to make it work. Avoid shooting off at a tangent when you think of something else. Write it down. You can work on that next year.



Above all, never attempt to build a "trading" strategy where you are intentionally hedging your bets. Trading is for mugs. There's nothing wrong with hedging bets in order to reduce volatility, but, as [@UGV299K6H](@UGV299K6H) has already said, if your initial bets are not profitable, then your hedge bets certainly won't be.

---

## 2021-06-11 21:49:11 - strategies channel

**liam**

As far as performance goes it’s brilliant, software compatibility has been a pain although things improved a lot since the beginning 

---

## 2021-06-11 17:33:04 - strategies channel

**liam**

Error between keyboard and chair regarding speed, flumine/bflw is capable of about 1k markets per minute out the box 

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

## 2021-06-10 18:39:28 - random channel

**Sam Asin**

Not sure if Mo is being sarcastic or not but yeah I think it'd be hilarious if this could add even a little value to an already profitable strategy. Some situation where you have a profitable strategy, but you can up your belief about your edge slightly when betting against a fast sounding horse, and lower it slightly when betting against a slow sounding horse, and improve your bet sizing or something.

---

## 2021-06-10 09:43:15 - general channel

**Jono**

when you get up to those large numbers 100, 150, 200+ has this been shown to impact speed or does flumine handle scaling up to this number of markets without slow down? I've seen quotes of iteration speeds near the 10-50ms running simultaneously on multiple markets. can speeds like this be expected when operating on hundreds of games

---

## 2021-06-10 09:02:09 - general channel

**Jono**

is it known if applications such as like bet angel make use of betfairlightweight or flumine? i watched a video of theirs talking about streaming data improving the speed and performance of their software and am curious if they have made use of whats available from these two packages

---

## 2021-06-09 23:02:51 - strategies channel

**V**

Your strategy is probably slow

---

## 2021-06-09 22:15:29 - strategies channel

**V**

Backtests are important tools, but they should be as realistic as possible. Latency is quite important (depending on what you’re doing) you can quite easily find a great backtest with 0 latency but it’s for good reason… it’s impossible to trade it in real life! Or maybe the strategy is too slow for the message throughout and your queue gets backed up, so you can’t trade on all price updates in practice… the backtest won’t show the latter, production will.

---

## 2021-06-07 16:56:15 - general channel

**Aaron Smith**

well, put it back in, if its 45seconds or 90seconds latency doesnt really make a difference, both is not viable. Personally i would probably even comment out a bunch of code and let it run, then add stuff step by step and see when it falls flat

---

## 2021-06-07 16:49:28 - general channel

**John**

Many thanks both [@UFTBRB3F1](@UFTBRB3F1) and [@U4H19D1D2](@U4H19D1D2). What the strategy does is mostly based on the the example strategy: 1) calculate the trigger price - an arithmetic function of the bsp, to place an order; 2) calculate the stake size: another arithmetic function of the best available price. everything else is the same as the example strategy. I was trying to get lots of logs in a file, but found the log file size slows the script down a lot, so I removed the logs and comment out most of the print/logging I added.

---

## 2021-06-07 15:41:14 - general channel

**John**

Hi on the just past 15:15 Lingfield race, I could see my testing script (using flumine) was running like crazy, even after the race had ended, it kept running for a minute, with some of the warning saying high latency, counting down from 45 seconds to finally 2 seconds when the script stopped... I have only one script running, the CPU usage is OK (about 50% with 2 CPUs), and this high latency happened only on some markets, not all. This high latency happens less in AU races. In the script (based on the flumine example strategy), I changed a little by adding a few lines for working out trigger prices, and calculating the stake sizes, so not too complicated. Does it mean there are too many stream events for the UK races (due to higher betting volume) to be coped by my script/VPS. Should I get a better VPS (with faster CPU), or I am missing something? Any comments will be appreciated.

---

## 2021-06-03 10:51:05 - issues channel

**liam**

looks like it, the way the latency increases like that isn't good, why HK?

---

## 2021-06-03 10:49:18 - issues channel

**liam**

there are no known memory leaks in bflw or flumine

---

## 2021-06-03 10:48:45 - issues channel

**James McKenzie**

I was going to ask about that as well. I have noticed that when I run my flumine code, or a previous betfairlightweight price scraper I have on the HK box I see the RAM usage slowly creep up until the process is killed. I had previously tried to flush the queue every 10 seconds (presuming it was the queue gathering data) and I still saw the RAM usage increase. The same code ran on a UK based AWS instance for my own use didnt have the memory problems.

---

## 2021-06-03 10:44:30 - issues channel

**James McKenzie**

typically the latency from HK seems to be stable at around 0.5s

---

## 2021-06-03 10:38:19 - issues channel

**James McKenzie**

Hi guys, I have a Betfair account that's been set up by a client who is based in Asia. I have been told that all betfair code needs to be ran from a Hong Kong server. I am running into connection problems when I run some flumine based price scraping code from an AWS server in HK. I see a huge ramp up in the latency and then a fairly nasty connection error message:



```{"asctime": "2021-06-02 12:37:54,900", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 0.5828690528869629"}                                                                        

{"asctime": "2021-06-02 12:40:35,503", "levelname": "INFO", "message": "[MarketStream: 2001] 1.184035567 removed, 139 markets in cache"}                                                                    

{"asctime": "2021-06-02 12:45:32,223", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 5.051729917526245"}                                                                         

{"asctime": "2021-06-02 12:46:17,490", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 50.812371015548706"}                                                                        

{"asctime": "2021-06-02 12:46:55,148", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 88.5535352230072"}                                                                          

{"asctime": "2021-06-02 12:47:41,872", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 133.0834095478058"}                                                                         

{"asctime": "2021-06-02 12:48:34,090", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 182.7278220653534"}                                                                         

{"asctime": "2021-06-02 12:50:47,754", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 297.83341121673584"}                                                                        

{"asctime": "2021-06-02 12:56:28,947", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 664.3587987422943"}                                                                         

{"asctime": "2021-06-02 12:57:00,334", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 695.7359499931335"}                                                                         

{"asctime": "2021-06-02 12:58:46,348", "levelname": "ERROR", "message": "get_account_details error", "exc_info": "Traceback (most recent call last):\n  File \"/usr/lib/python3/dist-packages/urllib3/connec

tion.py\", line 159, in _new_conn\n    conn = connection.create_connection(\n  File \"/usr/lib/python3/dist-packages/urllib3/util/connection.py\", line 61, in create_connection\n    for res in socket.geta

ddrinfo(host, port, family, socket.SOCK_STREAM):\n  File \"/usr/lib/python3.8/socket.py\", line 918, in getaddrinfo\n    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):\nsocket.gai

error: [Errno -3] Temporary failure in name resolution\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File \"/usr/lib/python3/dist-packages

/urllib3/connectionpool.py\", line 665, in urlopen\n    httplib_response = self._make_request(\n  File \"/usr/lib/python3/dist-packages/urllib3/connectionpool.py\", line 376, in _make_request\n    self._v

alidate_conn(conn)\n  File \"/usr/lib/python3/dist-packages/urllib3/connectionpool.py\", line 996, in _validate_conn\n    conn.connect()\n  File \"/usr/lib/python3/dist-packages/urllib3/connection.py\", l

ine 314, in connect\n    conn = self._new_conn()\n  File \"/usr/lib/python3/dist-packages/urllib3/connection.py\", line 171, in _new_conn\n    raise NewConnectionError(\nurllib3.exceptions.NewConnectionEr

ror: &lt;urllib3.connection.VerifiedHTTPSConnection object at 0x7f7c3bde0c10&gt;: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution\n\nDuring handling of the above exception,

 another exception occurred:\n\nTraceback (most recent call last):\n  File \"/usr/lib/python3/dist-packages/requests/adapters.py\", line 439, in send\n    resp = conn.urlopen(\n  File \"/usr/lib/python3/d

ist-packages/urllib3/connectionpool.py\", line 719, in urlopen\n    retries = retries.increment(\n  File \"/usr/lib/python3/dist-packages/urllib3/util/retry.py\", line 436, in increment\n    raise MaxRetr

yError(_pool, url, error or ResponseError(cause))\nurllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='[http://api.betfair.com|api.betfair.com](http://api.betfair.com|api.betfair.com)', port=443): Max retries exceeded with url: /exchange/account/json-rpc/v1 (Ca

used by NewConnectionError('&lt;urllib3.connection.VerifiedHTTPSConnection object at 0x7f7c3bde0c10&gt;: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))\n\nDuring handli

ng of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages/betfairlightweight/endpoints/baseendpoint.py\", line 

36, in request\n    response = [http://session.post|session.post](http://session.post|session.post)(\n  File \"/usr/lib/python3/dist-packages/requests/api.py\", line 116, in post\n    return request('post', url, data=data, json=json, **kwargs)\n  File \"/usr/l

ib/python3/dist-packages/requests/api.py\", line 60, in request\n    return session.request(method=method, url=url, **kwargs)\n  File \"/usr/lib/python3/dist-packages/requests/sessions.py\", line 533, in 

request\n    resp = self.send(prep, **send_kwargs)\n  File \"/usr/lib/python3/dist-packages/requests/sessions.py\", line 646, in send\n    r = adapter.send(request, **kwargs)\n  File \"/usr/lib/python3/di

st-packages/requests/adapters.py\", line 516, in send\n    raise ConnectionError(e, request=request)\nrequests.exceptions.ConnectionError: HTTPSConnectionPool(host='[http://api.betfair.com|api.betfair.com](http://api.betfair.com|api.betfair.com)', port=443): Max retrie

s exceeded with url: /exchange/account/json-rpc/v1 (Caused by NewConnectionError('&lt;urllib3.connection.VerifiedHTTPSConnection object at 0x7f7c3bde0c10&gt;: Failed to establish a new connection: [Errno -3] Te

mporary failure in name resolution'))\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages

/flumine/clients/betfairclient.py\", line 50, in _get_account_details\n    return self.betting_client.account.get_account_details()\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages/betfairlightwe

ight/endpoints/account.py\", line 54, in get_account_details\n    (response, response_json, elapsed_time) = self.request(method, params, session)\n  File \"/home/ubuntu/.local/lib/python3.8/site-packages/

betfairlightweight/endpoints/baseendpoint.py\", line 43, in request\n    raise APIError(None, method, params, e)\nbetfairlightweight.exceptions.APIError: AccountAPING/v1.0/getAccountDetails \nParams: {} \

nException: HTTPSConnectionPool(host='[http://api.betfair.com|api.betfair.com](http://api.betfair.com|api.betfair.com)', port=443): Max retries exceeded with url: /exchange/account/json-rpc/v1 (Caused by NewConnectionError('&lt;urllib3.connection.VerifiedHTTPSConnection o

bject at 0x7f7c3bde0c10&gt;: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))", "error": "AccountAPING/v1.0/getAccountDetails \nParams: {} \nException: HTTPSConnection

Pool(host='[http://api.betfair.com|api.betfair.com](http://api.betfair.com|api.betfair.com)', port=443): Max retries exceeded with url: /exchange/account/json-rpc/v1 (Caused by NewConnectionError('&lt;urllib3.connection.VerifiedHTTPSConnection object at 0x7f7c3bde0c10&gt;: F

ailed to establish a new connection: [Errno -3] Temporary failure in name resolution'))"}             

{"asctime": "2021-06-02 12:58:46,360", "levelname": "WARNING", "message": "[FlumineStream: 2001]: Latency high: 801.6888477802277"}

Killed```

Does anyone have any ideas about the cause of the problem and how I might resolve it. Much appreciated.

---

## 2021-05-27 11:51:13 - random channel

**Jonjonjon**

Thanks @dave. I'm not keen on performance being reported as a single monthly figure. It doesn't mean much. Equity curves tell a lot more.

---

## 2021-05-27 11:29:29 - random channel

**Jonjonjon**

Where is their public performance?

---

## 2021-05-27 07:52:19 - general channel

**liam**

nah but streaming is so lightweight it would be pointless, however when backtesting you can skip data to speed things up [https://liampauling.github.io/flumine/quickstart/#listener-kwargs](https://liampauling.github.io/flumine/quickstart/#listener-kwargs)

---

## 2021-05-23 12:25:49 - general channel

**thambie1**

[@UBS7QANF3](@UBS7QANF3) probably understands this stuff better, but here's how I would figure it out. If subscribing to the order stream, you can get the publish time of any orders you place. Thus you can figure out the matching time on betfair servers. The time between the matching time and when you got the return response, is the second leg. Though for the first leg, it includes both latency, bet delay, plus some part of the 50ms delay between matching cycles (which in theory on average should be 25ms).

---

## 2021-05-21 11:30:54 - issues channel

**liam**

premature optimization imho, keep it simple, 1-2k orders per market is normal for me (on every uk horse race)

---

## 2021-05-20 17:57:07 - issues channel

**liam**

Latency shouldn’t impact, yeah logs would help, I assume the strategy is using a simple place_order only 

---

## 2021-05-20 17:48:45 - issues channel

**Newbie99**

Do you want the logs (not sure if they will help)...my only guess is potentially a latency issue (I noticed a couple of high latency warnings around the same time)?

---

## 2021-05-19 20:08:00 - strategies channel

**MacrcoPolo**

Maybe you can get a near-exact approximation, but your objective is maximizing the log-wealth function, and in general that's a numerical optimization

---

## 2021-05-19 20:07:28 - strategies channel

**MacrcoPolo**

You won't get something exact - the wiki algo is just a numerical optimization recipe

---

## 2021-05-19 11:24:04 - random channel

**Mo**

[http://www.totalperformancedata.com/](http://www.totalperformancedata.com/)

---

## 2021-05-17 23:08:52 - issues channel

**Newbie99**

I seem to have the latest version of flumine, so its not that.



Removing the logic does remove the errors as expected, but seems to produce a lot of latency warnings on startup (may just be co-incidence as I'm not sure why that would be...it did take a long time to cycle through everything)!



```WARNING:flumine.baseflumine:High latency between current time and MarketBook publish time

{"asctime": "2021-05-17 22:06:31,634", "levelname": "WARNING", "message": "High latency between current time and MarketBook publish time", "market_id": "1.167249195", "latency": 2.0103297233581543, "pt": "2021-05-17T22:06:29.624000"}```

---

## 2021-05-17 16:04:24 - issues channel

**Newbie99**

Ah thats much better than my way! I just called list_current_orders and got a net exposure from that!



Are there likely to be any performance issues here if you have 1000's of orders (I'm thinking a use case for this could be say Wimbledon - Tournament Winner, so you could have a strategy running that market for potentially weeks)?

---

## 2021-05-14 23:28:11 - general channel

**Paul**

Most people probably don’t want to stand a lot of infra up, so basically just write as fast as possible to anything that works, and have other stuff use that as input to give you info you want to read. If you care about latency: do it all in memory.

---

## 2021-05-14 16:59:08 - strategies channel

**John A**

Thanks guys that’s a great help, on the speed front has anyone tried to calculate the acceleration over a number of seconds?

---

## 2021-05-14 16:53:39 - strategies channel

**John A**

Question for you guys that use TPD, what’s the best indicator; speed or order?

---

## 2021-05-14 15:21:51 - general channel

**Jono**

honestly tho do you think my concern of the back catalogue of json objects is valid due to the limited rate that the db can process them? I witnessed a slow down and assumed it was due to many existing threads hindering performance after multiple iterations. if i instead changed things to just have a single thread with a queue of the json objects it would solve the many threads issue but not the timing issues resulting in dozens (potentially hundreds or thousands) of payloads waiting to be sent and processed.

---

## 2021-05-14 15:08:26 - general channel

**MacrcoPolo**

Yeah, still that fits happily in memory and will load in a few secs into pandas

---

## 2021-05-14 14:33:05 - general channel

**liam**

you only need a single thread dedicated to recording to your db, should be zero performance impact

---

## 2021-05-14 14:32:09 - general channel

**Jono**

it is an ever growing table currently so no doubt you are right. I tried out the threading solution you suggested about a week ago and saw a significant improvement in speed. Eventually tho it seemed to cause a performance dip when climbing to a high number of threads as the backlog of payloads gradually climbed

---

## 2021-05-14 14:24:25 - general channel

**Jono**

for the purposes of filling in an orders to database that an app then uses to display bets, strategy performance etc. Sending the payloads to db directly during the stragey was slowing runtime quite so moving things to this other independent script seemed like a prefereable avenue

---

## 2021-05-14 10:33:02 - strategies channel

**PeterLe**

Yes thats what has threw me to be fair. Ive tried to smooth the data out by using moving averages etc it helped but slowed things down too much

If I could strip out the outliers that would make sense.

---

## 2021-05-12 09:25:11 - strategies channel

**Jonjonjon**

[@U01DPK9PGMC](@U01DPK9PGMC) That's quite a great suggestion. I've recently been having problems with slow backtests, as my strategy recalculates "fair value" with every market book update. But I could probably just calculate "fair value" at a single fixed time (e.g. 5 minutes before the race), and then start analysing the performance of the fair value signals.

---

## 2021-05-11 11:07:02 - random channel

**Jonjonjon**

Thanks for the tip [@U4H19D1D2](@U4H19D1D2). I might also try patching the market cache to keep everything in numpy arrays. Insertions and deletions could be slower, but if it saves my code from creating new numpy arrays at every time step, perhaps it will be faster anyway.



[https://github.com/liampauling/betfair/blob/ee4488ddb4f4bee775450f7497c08ea0fb470e9b/betfairlightweight/streaming/cache.py#L45-L72](https://github.com/liampauling/betfair/blob/ee4488ddb4f4bee775450f7497c08ea0fb470e9b/betfairlightweight/streaming/cache.py#L45-L72)

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

## 2021-05-10 22:15:58 - general channel

**Alex A**

Bit late, but a lot of exchanges either offer a price depth feed like Betfair, an “Order by order” feed where you can see exactly where you are in the queue and the breakdown of all orders ahead or behind you, or both, one typically with better latency than the other.

---

## 2021-05-09 23:53:52 - strategies channel

**AndyL**

Better day today...

Theoretical BSP performance was good too

Will see how week goes, but thanks on hedging advice chaps

Just moved BA from failing Laptop to a VPS, great stuff 24x7 without noisy laptop fan i could hear from the other side of the house!

---

## 2021-05-09 23:15:48 - strategies channel

**ShaunW**

@goatwish if you're not hedging then don't measure your performance by actual pnl. You'll have weeks or months where that runs ahead or behind your theoretical return (the one that assumes you'd hedged at bsp). At your stage I think you'd be best to hedge and then analyse your bets to see where the profit is coming from. Prove you're actually profitable first otherwise this could get expensive.

---

## 2021-05-08 16:50:55 - general channel

**Sam Asin**

[@U012XF5CNPN](@U012XF5CNPN) Yeah I get that logic, but there are some confusing situations especially when I'm dealing with the site and whatever potential latency there is. I.e. batb is 6, I put  $20 offer at 6.2, and the next update I get says there is $180 available at 6.2. I then put a $20 offer at 6.4, and next update there is $150 at 6.4 as well. Is someone getting in front of me? Behind me? It's hard to say.

---

## 2021-05-08 15:04:54 - strategies channel

**Oliver Varney**

again maybe another stupid question, but by the time your bet hits the market the situation has changed? So if for example you had GPS and you had some formula to define value based of distance to line, distance deltas to other runners, speed, etc , are you not looking to build the value function for T+bet delay

---

## 2021-05-08 13:17:20 - strategies channel

**Atho55**

[@U01L8D326AK](@U01L8D326AK) If you have a bit of Promo data it`s possible to compare past BSP to IPMIN and use it as a measure of performance like this [http://prntscr.com/12oaxpn](http://prntscr.com/12oaxpn) It produces a shortlist depending what you are looking for. Over Average picks work reasonably well.

---

## 2021-05-07 00:31:29 - strategies channel

**Greg**

I have only just started to beat SP regularly (via bot but more arse than class).It has taken me 10 years to start to understand value (even with a retired pro gambler for a father in law---slow learner:slightly_smiling_face:) and even then I am not always sure of it. I am up quite a bit this time but only after 110 bets (1k markets analysed by the bot) and variance is a bitch. On the plus side I haven't had to top up my BF account for ages-haven't taken money out either of course:laughing:..but to be fair working full time, family taking time as well as and not being able to stay up and watch UK markets slowed me a bit. I can print money on NSW tracks manually for some reason (predictable volatility maybe-55 bets a race usually) but the turnover charge limits you massively. Gawd I wish I could understand Python (dedicating hours everyday) better and ML of course. Chemo is not helping but hey gives me something to do instead of thinking about life and death:flushed:.Hang in [@U01PJ5YMFBJ](@U01PJ5YMFBJ)!!:grin: Its tough but tackle the bastard to the ground!!!:gorilla:

---

## 2021-05-06 11:07:03 - strategies channel

**Unknown**

[http://betfairlightweight.com|betfairlightweight.com](http://betfairlightweight.com|betfairlightweight.com) is available, and we could put sticky stuff on it. However, I don't know what web host would be good to use. Godaddy is VERY slow:

---

## 2021-05-05 14:59:14 - general channel

**Jono**

So far its looking as if introducing a separate thread to handle the latency filled request solves this issue ive been struggling to get around. I was wondering if the trading object can be used in multiple threads in order to speed up run times further? For instance if i wanted to run a strategy over 10 events currently listed on the exchange would it be possible to initiate a thread per event, pass each thread the trading instance, and then place/adjust orders without causing problems?

---

## 2021-05-05 11:07:19 - general channel

**liam**

Unless you are async best practise is to remove any blocking io/network requests from your strategies main thread, this will prevent latency or network errors causing issues

---

## 2021-05-05 11:02:33 - general channel

**Jono**

Thats looks just like the field i'd need to do as you suggested [@UBS7QANF3](@UBS7QANF3) and set up an independant script keeping track of all relevant orders to the strat :ok_hand:

similarly [@U4H19D1D2](@U4H19D1D2) [@ULDAVFDRP](@ULDAVFDRP) i'll try out generating a thread to handle the slow requests in the event i run into problems attempting to separate the post to the db from my current strategy logic. Thank you very much everyone, ill shoot back with anything else i get held up with along the way, the helps been class as usual

---

## 2021-05-05 10:58:57 - general channel

**liam**

Just create a new thread with a queue that handles all slow / db requests, flumine does this via logging control

---

## 2021-05-05 10:53:13 - general channel

**Jono**

thanks guys. so certainly latency in the post made at the end of strategy is causing unnecessary time to be wasted. i suppose this kind of goes beyond bflw but basically i want to make this post request and forget about it.

---

## 2021-05-05 10:40:30 - general channel

**Jono**

network latency specifically is the problem here, the database is hosted on a cloud server which regardless of how im keeping track of the bets will always be where i have to send updates to. I dont need the strategy to use any info from this db endpoint i just need to send it updates. the resp time is holding things up. If threading is what sounds best for this issue i will definitely look into it.

---

## 2021-05-05 10:38:53 - general channel

**Oliver Varney**

redis does allow for remote connections/hosts but you will still have network latency(better then http request library from my testing). can you not run it in a background thread, continue with the event loop but have some kind of status check that wont fire new orders till confirmation has returned?

---

## 2021-05-05 10:26:12 - general channel

**Jono**

has anyone had any success using bflw with the aiohttp package? i have to perform a post request to a database after each event iteration performed and the wait time for the response is slowing the strategy down quite a bit. There isnt anything in the post response that is needed for the next iteration so i was thinking about implementing  some async logic along with aiohttp in order to perform other tasks without holding up the next run waiting for the response. I noticed though there is quite a bit suggesting that regular python requests will hold up an async event loop defeating the purpose of creating the event loop to save time in the fist place. Will this be the case with bflw and if so is ther a way to make my post request to db and not wait for the response before carrying on with the next event in the strategy?

Cheers!

---

## 2021-05-01 05:41:58 - strategies channel

**Oliver Varney**

Just a couple of things on coming up with a model, be careful your not over fitting or data mining whereby you apply filters till you hit a profit, yet are left with such a small sample size that it isnt really significant.  if you have historical data, split it into two sections (80-20% split is generally okay with a smaller sample which you have by the sounds), train / come up with the model on the 80% and test it out applying the logic on the 20%. The performance should only be measured against the 20% and any performance on the 80% should be disregarded.

---

## 2021-04-30 12:23:16 - issues channel

**Oliver Varney**

just literally change this second from Performance issues to operational

---

## 2021-04-30 12:21:37 - issues channel

**Oliver Varney**

stream authentication - Performance issues

---

## 2021-04-30 12:20:30 - issues channel

**Oliver Varney**

actually status page is saying performance issue for auth

---

## 2021-04-26 09:29:43 - issues channel

**liam**

Its either a network or CPU issue, do you have monitoring in place to check either? The latency is calculated by comparing the MarketBook `publish_time` with your current clock time to alert you to issues.

---

## 2021-04-25 10:24:13 - issues channel

**rjj**

Hi, can someone tell me what messages of the form [marketstream: 2001]: latency high: 0.57733 mean. My algo seems to freeze when I get a batch of these, does it result in unsubscribing from a market for instance?

---

## 2021-04-22 17:17:07 - general channel

**Dave**

Flumine q: Will there be a big performance difference if I instantiate a strategy twice with different params and add them to a flumine instance Vs adding one strategy that takes both sets of params and applies them based on the market? The former seems cleaner but not sure if you lose some performance by having multiple strategy objects

---

## 2021-04-22 12:06:57 - general channel

**D C**

[http://www.totalperformancedata.com/news-all/2021/4/22/tpd-buys-bet-mover-from-level-software](http://www.totalperformancedata.com/news-all/2021/4/22/tpd-buys-bet-mover-from-level-software)

---

## 2021-04-22 12:00:03 - general channel

**Oliver Varney**

realtime prediction depending on the size of the model and latency requirements can either block or personally I stick into into a redis stream queue, picked up by a prediction service, then pushed back

---

## 2021-04-22 07:09:06 - strategies channel

**IndikaE**

Football question: I have noticed that the hometeam win frequency has fallen a lot across all leagues since matches starting being played without crowds(no big surprise there). My model is performing alright, but much worse than in backtesting(using Jan-may data 2020). Towards the end of that period I see a performance decrease even in backtest(when some leagues started reopening with no crowd?). My training set stops in December 2019. I must do my split along the time axis, otherwise I will surely be leaking. How have other people been dealing with this significant change in base distribution of home/away wins? Do you have data on crowd attendance, and is that enough to fix it? I don’t like that this whole period should probably be held out when retraining in the future, so I’m building a new model that will predict probabilities relative to baseline win frequencies instead. I can only imagine that this has been debated before, so sorry if I’m reviving a dead topic.

---

## 2021-04-17 16:09:01 - strategies channel

**Dave**

qq guys - is there anyway to precisely determine when an order was actually made available for matching? would `placed_date + estimated latency + inplay delay` be the best estimate?

---

## 2021-04-16 10:08:11 - issues channel

**Oliver Varney**

and maybe it would need regex as well as for example the latency warnings that may pop up all are slightly differnent ?

---

## 2021-04-15 16:45:55 - strategies channel

**Dave**

Point being, flumine won't solve your problem if you are still going to your database at each tick (if anything maybe kill your db :sweat_smile: ). Maybe you need to replace your db with some kind of in-memory db, e.g. redis

---

## 2021-04-15 15:50:38 - strategies channel

**Mo**

Can’t you make those calls in parallel? I measure latency in microseconds, not tens of seconds

---

## 2021-04-15 15:37:49 - issues channel

**Jorge**

I installed bflw using: `pip install betfairlightweight[speed]` , which installed orjson

---

## 2021-04-15 15:34:05 - strategies channel

**Peter**

I'd echo Mo's earlier comment ... "20 seconds!". flumine provides  near instantaneous and certainly sub second data from the Betfair data stream as it is pushed out to subscribers. I suspect (feel free to correct me if I'm wrong) that you're currently polling the Betfair API and so haven't yet experienced the speed of streaming.

---

## 2021-04-15 14:55:45 - strategies channel

**Jono**

Ive recently managed to implement a trading script able to turn a small profit when certain odds exist on the exchange but is extremely reliant on the speed at which it is able to check the exchange. I am wondering the best way to move forward with trying to upscale the program to run on several events at once and potentially tackle the speed issue in this second version i am writing. I need to be able to check as many 1X2 markets on the exchange as quickly as possible in order to be profitable. When testing, if the time between checking markets reaches ~20 seconds the profitability of this strat takes a large dip, so small scale running sequentially on a 3 or 4 events is do able but more than that results in barely breaking even/losses. I believe streaming the odds would be the first significant improvement to be made instead of calling the api in a long winded loop to look for changes in listed prices, and soon after looking into this as an option i ended up at the flumine docs - which look very promising. Before i dive in and commit to the flumine framework is this what is designed for or at least useful in this scenario; high speed retrieval of bf exchange info for efficient strategy execution?



Any help is really appreciated and if ive got the wrong idea about flumine or should try another avenue for what im looking to do please let me know your thoughts, cheers!

---

## 2021-04-15 12:07:00 - strategies channel

**Mo**

If you care about latency why use Python at all?

---

## 2021-04-15 07:18:50 - strategies channel

**Tosin**

just generally for lower latency. would a dictionary in python work well for low latency?

---

## 2021-04-14 11:39:08 - general channel

**RicHep**

Liam, do you have your server set up near Betfairs to get that latency or is that just from the UK?

---

## 2021-04-14 11:11:53 - general channel

**liam**

My median round trip is around 130-140ms depending on which way the wind is blowing, exchange cycles are 50ms, so in reality it should be around 80ms ish however:



a) You can change this by overriding in execution

b) Backtesting is never going to be 100% so this latency is trying to be worst case and if you are finding big differences in matching/profit based on this latency I recommend you stop and go live

---

## 2021-04-14 11:06:38 - general channel

**Chris C**

Hey, I’ve got a question on the simulated latencies for the backtest. I can see for the backtest the default place latency is 120ms. How’d you come up with this number? Surely the order arrives at betfair faster than 120ms. Does it rest at betfair that long before it gets executed?

---

## 2021-04-13 18:20:41 - general channel

**river_shah**

cross market near-arbs or arbs can be seen as special case of choice markets. they give you option to agress on the side you like without incurring bid / ask spread. this can have beneficial impact on your strategy, both from trade entry and or exit. not a strategy in its own right but an execution optimization large scale strats should do

---

## 2021-04-12 11:57:00 - strategies channel

**Michael**

Yeah - there's a sliver of value just in the fact that you're offering and willing to wait to match. If you're not sure how that works imagine doing it constantly on both sides of the book. The problem is adverse selection, which is where your bad bets match and your good ones don't. If you've got a model that's good enough to reduce that just a little bit and then offer into the market that's enough to get you into the black. That's why so many people get off to what looks like a flying start but then stall when they scale. They imagine it's the amazing performance of their model that's generating their profits at small stakes but they're really just partial market makers. When they scale beyond the capacity of those forces they get a reality check. You can watch this play out live on these forums.

---

## 2021-04-12 09:32:18 - general channel

**liam**

[@U019HMPCQT0](@U019HMPCQT0) [@U0155J92A7Q](@U0155J92A7Q) there was a bug, I hadn't noticed as I delete all files on cleanup, small fix in [https://github.com/liampauling/flumine/blob/66089f81a8d5cd7f74ffe2d864745e823cb6bf51/examples/strategies/marketrecorder.py#L110|1.18.2](https://github.com/liampauling/flumine/blob/66089f81a8d5cd7f74ffe2d864745e823cb6bf51/examples/strategies/marketrecorder.py#L110|1.18.2) that checks the txt file exists. The reason it checks for the gz first is that we know a market has closed if that is the case, we can't rely on checking the txt file as it might be a very slow market.

---

## 2021-04-08 06:49:44 - random channel

**Mo**

Some matches have insane volume but not that many matches in total per year (around 2000). In play seems like a tough nut to crack because of the importance of latency and hard to model considerations like the impact of weather

---

## 2021-04-06 16:40:42 - random channel

**James T**

I think it’s a different skill though - betting track side. There must be a bit of race reading involved. GPS vs drone vs trackside must be pretty similar in terms of latency now. In-running has been doing particularly well since there were zero crowds (hence drones attempting to replace trackside), so it’ll be interesting to see how our strategies do once crowds do return. Has GPS completely wiped out trackside potential? I doubt it. 

---

## 2021-04-04 21:14:08 - random channel

**MacrcoPolo**

"Under some applications WSL was delivering slightly better performance over WSL2, but in general the WSL/WSL2 performance was very close to that of bare metal Ubuntu 20.04."

---

## 2021-04-04 21:09:49 - random channel

**Jonjonjon**

Is the performance for WSL as good as running Linux natively? I do a lot of flumine backtesting

---

## 2021-04-04 11:10:01 - strategies channel

**Unknown**

Generating these kinds of "average" fair values means that you will most likely be filled at the worst instances. The odds in a given match are a function of a variety of parameters, including historical performance, current game state which takes into account which players are playing, who's injured etc. You cannot generate any reasonable fair value for a specific match given the time into the match and current score

---

## 2021-04-01 18:33:33 - general channel

**river_shah**

My suspicion is that for latency sensitive situations is it possible that my account or bets are being routed through a slow component

---

## 2021-03-29 00:20:49 - random channel

**Dave**

i suppose if one is reacting to changes in the book then latency is more of a concern.

---

## 2021-03-29 00:20:14 - random channel

**Dave**

my biggest focus is football, IP though. All execution via the REST api...never really had a concern for latency for this :sweat_smile:

---

## 2021-03-28 20:46:40 - random channel

**thambie1**

Hmm, weird. I'm also doing 100% taking for the time being. Surprised in such a similar space we would see such different latency considerations

---

## 2021-03-28 20:36:57 - random channel

**thambie1**

[@U011VL3CA2Y](@U011VL3CA2Y) When I started trading football pre, I didn't notice any latency competition, despite taking some really obvious trades. Which makes me wonder if if the competition you're talking about is me. If you want to send me one or two of the trades you missed out on, I'll let you know if I took them.

---

## 2021-03-28 18:23:59 - random channel

**Ruben**

is pinging [http://betfair.com|betfair.com](http://betfair.com|betfair.com) a reliable way to measure latency? In other words, will a lower ping latency translate into less latency when receiving streaming data from betfair?

---

## 2021-03-27 08:41:25 - random channel

**Oliver Varney**

Is it worth adding a dict at the class level with keys = market ids then, with latency for last updates stored etc

---

## 2021-03-26 16:37:25 - random channel

**Mo**

Direct from the source: [http://www.totalperformancedata.com/](http://www.totalperformancedata.com/). Betfair have a number of licenses they give out, speak to your account manager

---

## 2021-03-24 23:22:24 - strategies channel

**Dave**

generally done most of my calibration looking at charts in sample, calibrating based on that and then measuring out of sample performance

---

## 2021-03-23 17:48:40 - strategies channel

**birchy**

With my strategy that I inadvertently over-fitted, I'd basically been using the same training data over and over (because I had no other data at the time), using various triggers and ideas until I ended up with a simulated P&amp;L that was satisfactory. I've never actually looked at the training data manually but unintentionally found the sets of triggers and values that hit the sweet spot _for that dataset._ Meanwhile, I was gathering more data for use as a testing sample and that was when I realised what I'd done. An expensive lesson was learnt. :grinning:

The other problem was that this was straight laying only and I'd calculated that a maximum drawdown of &gt; £1000 was to be expected, so even at -£700, I left it playing live. It went up, it went down, but the overall trend was slowly down. Luckily, I have some other strategies that earn small amounts at lower risks, but truth be told, I managed to undo 6 months of profit in a matter of weeks.

---

## 2021-03-19 21:56:19 - strategies channel

**Dave**

Should be fairly straightforward to eliminate the latency warnings, it's not something I'd put up with tbh! Is your internet connection a bottleneck maybe? Perhaps try unning it on AWS and see if you get the same warnings.

---

## 2021-03-19 21:54:27 - strategies channel

**IndikaE**

Currently running it on my MacBook Air m1. I wouldn’t say I do heavy computation. The computation is done asynchronously in a different process, and the Flumine process reads the predictions from files(could switch to redis?), and does very little except for some simple bookkeeping. I do have some custom middleware for keeping track of  price movements that I might want to optimize, though. I’ve noticed that the warnings occur quite frequently right after starting Flumine, but then seem to disappear after a time. The reason why I want to use flumine is because I plan to add some HFT element to improve the prices I am getting in the future. Anyway, if you recommend that I eliminate latency issues whatever the cause, I will get to work straight away! Thanks for the input :slightly_smiling_face: 

---

## 2021-03-19 21:21:33 - strategies channel

**Dave**

The fact that you have latency issues is odd. Are you running on a machine in a data centre? Or is it because you're doing some heavy computation so it becomes a bottleneck? Probably best to solve those issues

---

## 2021-03-19 21:03:14 - strategies channel

**IndikaE**

I am papertrading my first strategy implemented in flumine, and I occasionally have latency issues. My strategy is really a straight (football) value betting strategy that will just take a backprice if it is +EV according to my model and lay when it is -EV. Dead simple with no need for precise timing, since the model operates on a timescale of minutes. With such a strategy is latency even something to worry about? To me it seems obvious that it is not, but being a noob and all, I’m a little scared I might be missing something in my reasoning. Apologies for the vagueness of the question!

---

## 2021-03-19 19:46:51 - random channel

**Paul**

Also, it might be interesting to see how things perform on Graviton2. The price/performance is pretty :ok_hand:  if you can get the things you need compiled

---

## 2021-03-19 17:27:59 - random channel

**Dave**

Yup. No need to bang out the big guns until you start seeing latency issues

---

## 2021-03-17 08:39:33 - strategies channel

**Jorge**

Got it, and isn't the upload of "big" files slowing down the whole process? This is python so I guess this is not done in parallel

---

## 2021-03-16 17:27:40 - strategies channel

**Jorge**

How do you avoid that your Python Script loads the complete fills to memory when storing files in S3? Do you always keep the connection with the cloud open?

---

## 2021-03-16 12:57:44 - general channel

**Mo**

Example: fitting your model to BSP gives you the distribution of speeds of the horses. You use these distributions in running combined with each horse's distance to the finish line to calculate an in running probability. Then you compare that to the current prices to find value. You're not comparing the current prices to the BSP to find value

---

## 2021-03-16 10:00:49 - general channel

**D C**

SE - standard error. Like a standard deviation you can apply around a point estimate. From memory most maximum likelihood estimates thrown out by a linear model are shown to be normally distributed.

---

## 2021-03-12 12:39:42 - strategies channel

**Unknown**

Hi Dave, what do you mean by speedbump and how is it helpful for a MM?

---

## 2021-03-12 08:33:39 - random channel

**Mo**

I suppose the newer dividends based on match performance that were time limited were an attempt to encourage more trading activity

---

## 2021-03-11 18:26:14 - general channel

**Lee**

```latency = time.time() - (market_book.publish_time_epoch / 1e3)

if latency &gt; 2:```

---

## 2021-03-11 18:25:05 - general channel

**river_shah**

working from a dodgy internet connection at the moment on my dev machine. having trouble finding the parameter that controls this: `WARNING High latency between current time and MarketBook publish time` where can I set this high enough please to reduce occurrences of this log?

---

## 2021-03-11 18:02:52 - random channel

**river_shah**

modern exchanges are radically different from betfair and a surprisingly huge amount of volume and opportunity is derived from latency races. none of that applies here. that being said, constantly thinking about bets, expectations, risk management, those skills are transferrable

---

## 2021-03-11 16:30:11 - strategies channel

**Dave**

betfair's speedbump is one of those glorious things that helps a market maker quote tighter than they otherwise would

---

## 2021-03-11 16:29:40 - strategies channel

**Unknown**

latency arb is bad for most market participants - unless there are mechanisms that protect the market maker, they'll be less confident about quoting a tighter spread due to fear of being picked off. Less tight spreads = higher transaction costs for everyone

---

## 2021-03-11 15:48:47 - strategies channel

**Dave**

latency arb = Not useful for society.

high frequency MM/low latency liquidity provision: useful for society

---

## 2021-03-11 11:40:03 - strategies channel

**Jonjonjon**

Who is latency arbitrage bad for? And are they people we should feel sorry for?

---

## 2021-03-11 11:38:26 - strategies channel

**Mo**

I think when most people say HFT is bad what they mean is latency arbitrage is bad

---

## 2021-03-10 11:06:42 - random channel

**river_shah**

[@U4H19D1D2](@U4H19D1D2) was hoping for something like this: [https://github.com/taskflow/taskflow](https://github.com/taskflow/taskflow) (see the section on launch async tasks) but for python. ok, looks like with python I will need to embrace zmq for these kind of function calls. totally happy with python speeds, however the gil does get in the way of these async function / task evals

---

## 2021-03-09 20:19:06 - random channel

**river_shah**

beginning to look at in-play football a bit more. orders adds are N second delayed and take N seconds to reflect in the stream. order cancels are network / matching engine latency instantaneous and reflect in the stream straight away? If guys with better pictures and more manual attention are cancelling a side, do my algos see that behaviour quickly enough to take defensive measures themselves?

---

## 2021-03-07 10:26:28 - strategies channel

**Dave**

QQ to racing specialists: Have you noticed any impact to your existing strategy performance when deploying another strategy in a seperate market on the same event? I'm deploying some stuff on the place markets and worried I will impact price action on win markets. Hopefully starting off with minimal stakes should show negligible impact...

---

## 2021-03-06 11:20:55 - strategies channel

**Misha**

I never gauge performance on any single match/bet. I gauge performance over at least 1000 matches (which might be at 50,000 bets)

---

## 2021-03-06 11:07:10 - general channel

**V**

Yeah, this is how I’ve done it historically. But my stuff is relatively latency sensitive so want to reduce internal latency on the trading path as much as possible.



[@U4H19D1D2](@U4H19D1D2) this is probably a stupid question, but then again this is Betfair we’re talking about so can never be too sure: they only care if you’re consuming data and trading at the account level right? So if you’re only consuming with one client, but trading (and also consuming) with another, that’s fine?

---

## 2021-03-05 11:20:58 - issues channel

**Lee**

currently getting lots of high latency warnings

---

## 2021-03-02 12:26:01 - strategies channel

**Unknown**

[@U01PQ9SR9MJ](@U01PQ9SR9MJ) the point is that your conclusion of "what is the likely outcome going forward" is unlikely to be useful unless you evaluate this conclusion on data you have not incorporated when doing your data mining. To put it simply, you can't say that your observation of some pattern is a useful observation unless you find that this observation is profitable on data you have kept seperate from where you identified this pattern in the first place. indeed you are attempting to do something like this with your "forward testing", but you can very easily learn the results of your forward testing by just holding out some of your historical data. (This is of course not to disqualify the usefulness of actually taking your strategy to the market with small stakes).



also to add - if you are relying on real trading to do this "validation" for you, your whole process is going to be slow. By holding out some historical data you can instantly check if the patterns you've identified have some profitability (and  therefore meaning you have not just overfit your historical data set).

---

## 2021-03-02 12:08:36 - strategies channel

**Oliver Varney**

The performance in the 80% is somewhat irrelevant and should be mainly disregarded, its the 20% you care about

---

## 2021-03-02 12:05:22 - strategies channel

**Oliver Varney**

This is the typical learning approach from machine learning. Take your all the historical data you have and randomly shuffle it. Once shuffled take 20% of you data and put it aside, forget about it for now, almost like it doesn't exist.  With the remaining 80% you will use this data to come up with your model / script / decision maker. Apply the process of learning to this data solely making sure it never sees any of the 20% hidden away. A typical learning approach could be linear regression (gradient descent) but it can be as simple as using excel to filter records although this is sub optimal. Once you think you have constructed your model / script / decision maker, return to that 20% of data and apply the rules / model to it and evaluate performance.

---

## 2021-03-01 20:46:05 - general channel

**Lee**

Hi,

`market.context` is fine to use, I use it too



I think you can put a streaming timeout on the strategy when instantiating to make it trigger? Not sure what the default is.



I’d do both, `listener_kwargs` just filters out to speed up backtesting but you’ll need to do it in `check_market_book` for live trading / testing logic

---

## 2021-03-01 20:38:06 - strategies channel

**Oliver Varney**

so you want to bet blind at BSP? If I had to hazard a guess you will be at best flat in the long run doing this. What is your out of training set performance (i.e. test set and or holdout) ?

---

## 2021-02-26 07:52:49 - general channel

**Unknown**

Market total matched delay

Not using delay key but seeing (in a slow moving market this time in the AM) that the total matched seems to be behind - using betfairlightweight==2.12.0

Anything obvious to check?

---

## 2021-02-24 15:10:44 - issues channel

**Aaron Smith**

Hey guys, i m still struggeling with my Latency issue, i have little clue how to "debug" this. I thought i d just put out all my current warning logs, maybe someone can make any sense of it, i d be grateful :smile: first: the latency issue seemingly isnt the result of to much processing per market update, even when i m not processing anything, i still eventually get the same problem. The framework is running on an ec2 instance, which i thought should be rather stable. Its a linux instance, so OS time should be in sync with an NTP server.

Problem: _"[MarketStream: 2001]: Latency high: 1.0108046531677246"_

Latency can go up to 6s.



That said, my suspicous logs:

• sometimes i get _"Market &lt;market_id&gt; not present when closing"_, i dont know why it happens, timewise it doesnt seem to correlate with the _Latency high_ warning.

• And now the probably bigger problem:

```{"asctime": "2021-02-23 21:19:59,560", "levelname": "ERROR", "message": "[MarketStream: 4001]: SUBSCRIPTION_LIMIT_EXCEEDED: trying to subscribe to 12930 markets whereas max allowed number was: 200"}

{"asctime": "2021-02-23 21:20:10,572", "levelname": "ERROR", "message": "MarketStream run error", "exc_info": "Traceback (most recent call last):\n  File \"/usr/local/lib/python3.7/site-packages/betfairlightweight/streaming/betfairstream.py\", line 216, in _receive_all\n    part = self._socket.recv(self.buffer_size)\n  File \"/usr/lib64/python3.7/ssl.py\", line 1056, in recv\n    return self.read(buflen)\n  File \"/usr/lib64/python3.7/ssl.py\", line 931, in read\n    return self._sslobj.read(len)\nsocket.timeout: The read operation timed out\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File \"/usr/local/lib/python3.7/site-packages/flumine/streams/marketstream.py\", line 32, in run\n    self._stream.start()\n  File \"/usr/local/lib/python3.7/site-packages/betfairlightweight/streaming/betfairstream.py\", line 59, in start\n    self._read_loop()\n  File \"/usr/local/lib/python3.7/site-packages/betfairlightweight/streaming/betfairstream.py\", line 198, in _read_loop\n    received_data_raw = self._receive_all()\n  File \"/usr/local/lib/python3.7/site-packages/betfairlightweight/streaming/betfairstream.py\", line 220, in _receive_all\n    raise SocketError(\"[Connect: %s]: Socket %s\" % (self._unique_id, e))\nbetfairlightweight.exceptions.SocketError: [Connect: 4002]: Socket The read operation timed out"}

{"asctime": "2021-02-23 21:20:12,575", "levelname": "WARNING", "message": "[Listener: 4002]: stream already registered, replacing data"}```

These 3 fellas are getting logged right behind each other. The first few hours everything seems fine, until eventually these show up. I m not sure why it tries to subscribe to 12k (its always roughly 12k) markets, thats at least not what i m telling it to do. The fact it doesnt give this error the first few hours makes me feel like something bad is stacking up in the background (allthough if this was to log as soon as i hit &gt;200 markets, the jump from 200 to 12k seems kinda big). I know its not you guys job to solve my probs, but maybe some smart being immediatly has an idea of whats up - i d surely appreciate it :slightly_smiling_face:

---

## 2021-02-24 15:06:44 - strategies channel

**river_shah**

It is not a one to one mapping to the trading domain but ml techniques such as support vector regression have a built in concept of “margin” to separate points better and give better out of sample performance. maintaining margin for trading strats to me is similar to how SVR creates bands around training examples to help classify points better. too low of a margin and SVR has high variance. Something similar happens to trading strats

---

## 2021-02-22 10:53:54 - general channel

**liam**

i then use the slack plugin so I get notifications on errors, I have done but it was in beta and started slowing things down for me so i left it but it was very cool

---

## 2021-02-22 10:53:25 - general channel

**Oliver Varney**

do you use the performance monitoring stuff

---

## 2021-02-22 10:49:07 - general channel

**Oliver Varney**

Morning chaps, just looking into improving exception handling / logging /performance monitoring etc, and I know [@U4H19D1D2](@U4H19D1D2) and other use sentry. Other then their site is there any good resources people would recommend?

---

## 2021-02-21 10:53:50 - issues channel

**birchy**

Just to add to the latency issue, it's important to ensure that your OS time is synchronised with an NTP server. Linux does this by default. Windows tries, but it's a bit fluffy.

---

## 2021-02-21 06:05:21 - issues channel

**liam**

[@UFTBRB3F1](@UFTBRB3F1) that was fixed a while ago by checking if the update is a snap or not. [@U01DVUAE2G1](@U01DVUAE2G1) you probably right here although its difficult to debug as betfair will start to conflate if you are not pulling off the socket quick enough. However if you are getting the 2s warning then you are either maxing your CPU or you are processing the updates too slow. If you get the `Latency High..` warning you either have network or CPU issues.

They are just supposed to be warnings to highlight potential issues, they could probably be improved in the codebase or by the user elsewhere, I did create an [https://github.com/liampauling/flumine/issues/338|issue](https://github.com/liampauling/flumine/issues/338|issue) to track this better to allow easier tracing/profiling

---

## 2021-02-20 20:19:19 - issues channel

**Newbie99**

[@U4H19D1D2](@U4H19D1D2) will be able to correct me here, but wasn't there an issue whereby if updates weren't that frequent (e.g. illiquid markets such as some of the US stuff) then you could get a latency warning, not because anything is wrong as such, but simply because the gap between the current time and last publish time is quite large?

---

## 2021-02-20 20:13:09 - issues channel

**Aaron Smith**

for `"[MarketStream: 2001]: Latency high: ___"`  it ranges from 0.5 to 5. Whenever its above 2.0, it also prints the `"High latency between current time and MarketBook publish time"` , which i guess kinda shows that the problem is not in the process time of the market_books, but rather that the first latency is part of the 2nd latency

---

## 2021-02-20 19:59:27 - issues channel

**MacrcoPolo**

What are the actual values of the latency you're getting roughly?

---

## 2021-02-20 19:45:14 - issues channel

**Aaron Smith**

I m still kinda confused, i hope you are patient with me :smile: Okay so: I get a bunch of market_books as an event. I loop over these market_books and check if _latency = current_time - publish_time &gt; 2._ If this is the case, it means that a previous market_book took to long to process or that the market_book came in late in the first place. Something here i didnt get right, because if the market_book came in late in the first place, it shouldnt throw this warning but only the `latency high`  warning if i got you right? But if the market_book arrived 2 seconds late in the first place, _latency = current_time - publish_time &gt; 2_ would be true aswell? Sencond, given a market_book takes to long to process, then the next market_book in the loop (and every market_book coming after) will have high latency and their market_ids are printed out, however its not actually those markets that caused the latency but the previous one?

---

## 2021-02-20 19:27:28 - issues channel

**Aaron Smith**

i m confused here, `High latency between current time and MarketBook publish time`  is thrown before the strategy actually processes the market_book, so it does not take processing time into account?

---

## 2021-02-20 19:16:43 - issues channel

**Aaron Smith**

and `latency high`  means the market_book update took to long to reach me?

---

## 2021-02-20 19:15:24 - issues channel

**liam**

High latency means you are spending too much time in the strategy, are you doing something slow?

---

## 2021-02-20 19:14:16 - issues channel

**Aaron Smith**

[@UUCD6P13J](@UUCD6P13J) i get both. `Latency high` disregards processing time and just checks how long it took to get the market_update? In that case, if you get the `Latency high` one, the `High Latency`  one is sorta guranteed to follow?

---

## 2021-02-20 18:33:44 - issues channel

**Lee**

[@U01DVUAE2G1](@U01DVUAE2G1) which latency warnings did you get? `Latency high` or `High latency between current time and MarketBook publish time`

I get a few `Latency high` most days.

---

## 2021-02-20 16:33:06 - issues channel

**Newbie99**

I definitely get random high latency warnings from an ec2 instance. Not to often, but some days it does seem to randomly happen

---

## 2021-02-20 16:18:31 - issues channel

**Aaron Smith**

flumine just threw a bunch of high latency warnings. I m curious what caused this high latency. I suppose one way to get high latency is by to much calculations in your strat so it cant keep up? Highest cpu-utilization was 15% though. Is it possible for an ec2 instance to just "randomly" have a bad connection sometimes?

---

## 2021-02-20 11:59:12 - random channel

**James T**

I wasn’t aware that there was a separate AUS only liquidity pool. I thought it’s always been global since the start. Used to be hosted in the AUS (and therefore had more latency from UK), but is now hosted in UK or IRE or whatever. 

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

## 2021-02-16 17:17:05 - random channel

**Aaron Smith**

like, always have it decide after 1 week (or what ever time period) decide if it should increase given its performance or decrease

---

## 2021-02-11 14:34:11 - strategies channel

**liam**

I started in 2012, from memory streaming was a big improvement both from the number of markets now available and my pnl increased. Every time I have met up with someone (normally from this group) I got another kick to improve but it has been steady with profit improving every year since I started (hopefully continues :slightly_smiling_face:)

---

## 2021-02-09 16:53:15 - issues channel

**ricky**

As i mentioned, i have two instance of fluime running, one only monitor, recording and send me signal notification, another one is check and place bet.

I only start live bet via fluinme last two weeks, i am still tesing my strategies, in particular i need solve my latency issue, i feel more confidence when i can see bet actual place in betfair website.

---

## 2021-02-09 10:31:35 - issues channel

**ricky**

nothing block, but maybe some python library function too slow to execute, not sure.

---

## 2021-02-09 10:29:40 - issues channel

**ricky**

I am running inplay football strategies, because my code might invlove heavy calculation(like dict array and sort etc). if befair push update every 30ms,

when my function/class cost more than 30 ms execution time it can cost Latency high warning?

---

## 2021-02-08 23:44:42 - issues channel

**ricky**

WARNING:flumine.baseflumine:High latency between current time and MarketBook publish time

WARNING:betfairlightweight.streaming.stream:[MarketStream: 2001]: Latency high: 1.961205244064331

WARNING:betfairlightweight.streaming.stream:[MarketStream: 2001]: Latency high: 1.808332920074463

WARNING:betfairlightweight.streaming.stream:[MarketStream: 2001]: Latency high: 1.6995792388916016

WARNING:betfairlightweight.streaming.stream:[MarketStream: 2001]: Latency high: 1.0950758457183838

WARNING:betfairlightweight.streaming.stream:[MarketStream: 2001]: Latency high: 0.7914028167724609

WARNING:betfairlightweight.streaming.stream:[MarketStream: 2001]: Latency high: 0.5924580097198486

WARNING:betfairlightweight.streaming.stream:[MarketStream: 2001]: Latency high: 0.507713794708252



bflw: 2.12.0

flumine: 1.16.0



I run flumine via ubtuntu in an virtual machine. When i place live bet, i somethime receive "Latency high" warning. (less than 300 markets running)



1) Do you think my virtual machine can cost network delay? ( My latptop 4 cores, 8GB RAMs, 120Mbps boardband)

2) "Latency high: 1.961205244064331" means 1.96s delay? should i set both conflate_ms = 2000, and streaming_timeout = 2 to reduce warning?

3) I was running inplay strategies, betfair might push more udpate from one market to other, is there a way i can meaure my code execution time so that i can improve my code?

---

## 2021-02-08 14:48:36 - general channel

**liam**

Yeah a mixture of CPU and separating anything that involves a lot of computation on the process as it risks adding some latency to your other strategies as they are processed one by one. You also need to be aware that any orders are sent in the same request per update (read into that what you will)

---

## 2021-02-06 08:09:39 - general channel

**Unknown**

• US centric but an excellent introduction to understanding betting markets and how to think about value: [https://www.amazon.co.uk/Logic-Sports-Betting-Ed-Miller-ebook/dp/B07RG6H8C2](https://www.amazon.co.uk/Logic-Sports-Betting-Ed-Miller-ebook/dp/B07RG6H8C2)

• Seminal paper for modelling football (soccer): [https://betfairlightweight.slack.com/files/UBS7QANF3/F010NTJJK88/dixoncoles.pdf?origin_team=T4G9NBD2M&amp;origin_channel=C4HL6EZTQ](https://betfairlightweight.slack.com/files/UBS7QANF3/F010NTJJK88/dixoncoles.pdf?origin_team=T4G9NBD2M&amp;origin_channel=C4HL6EZTQ)

• A follow up on in-running football: [https://betfairlightweight.slack.com/files/UBS7QANF3/F010A4MK9MY/dixon1998.pdf?origin_team=T4G9NBD2M&amp;origin_channel=C4HL6EZTQ](https://betfairlightweight.slack.com/files/UBS7QANF3/F010A4MK9MY/dixon1998.pdf?origin_team=T4G9NBD2M&amp;origin_channel=C4HL6EZTQ)

• A classic horse racing paper: [https://www.gwern.net/docs/statistics/decision/1994-benter.pdf](https://www.gwern.net/docs/statistics/decision/1994-benter.pdf)

• An excellent starting point for tennis modelling: [http://www.strategicgames.com.au/PhD.pdf](http://www.strategicgames.com.au/PhD.pdf)

• Outstanding book on cognitive biases: [https://www.amazon.co.uk/Thinking-Fast-Slow-Daniel-Kahneman-ebook/dp/B005MJFA2W](https://www.amazon.co.uk/Thinking-Fast-Slow-Daniel-Kahneman-ebook/dp/B005MJFA2W)

• Excellent introduction to probabilistic forecasting in general: [https://www.amazon.co.uk/Signal-Noise-Art-Science-Prediction-ebook/dp/B0097JYVAU](https://www.amazon.co.uk/Signal-Noise-Art-Science-Prediction-ebook/dp/B0097JYVAU)

• Inspiration for how far you can go: [https://www.amazon.co.uk/Man-All-Markets-Beating-Street-ebook/dp/B07ZWJFYW5](https://www.amazon.co.uk/Man-All-Markets-Beating-Street-ebook/dp/B07ZWJFYW5)

If you can be more specific about what sport(s) I can recommend more papers

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

## 2021-01-30 16:33:52 - issues channel

**birchy**

I can probably use specific filters for each event type and run a strategy per sport. Tempted to go 100% polling with this bot and save streaming for inplay, where speed IS important.

Also, just checked in and bot had crashed and burned. Last log was:

`{"asctime": "2021-01-30 08:31:23,529", "levelname": "WARNING", "message": "High latency between current time and MarketBook publish time", "market_id": "1.178427846", "latency": 752.4693222045898, "pt": "2021-01-30T08:18:50.921000"}`

I'm guessing it's been terminated by the Linux OOM killer as ram was on 65% of 2GB when I last looked yesterday. That is/was using only

`streaming_market_filter(event_type_ids=['1'])`

---

## 2021-01-30 15:56:41 - issues channel

**mandelbot**

i used betfairlightweight[speed] --upgrade though

---

## 2021-01-30 12:44:02 - issues channel

**liam**

Yeah its a complication I want to avoid at all costs, do you know the latency you add by doing that?

---

## 2021-01-30 12:31:01 - issues channel

**birchy**

My usage for this particular strategy is to have a small number of bets in lots of markets preplay, where speed is not required. Slow and steady wins this particular race, so polling is probably better suited. It's a shame that `listMarketCatalogue` doesn't have a param like `notMarketIds` where we could specify a list of market IDs that we're no longer interested in.

---

## 2021-01-28 15:59:04 - general channel

**liam**

```trading = betfairlightweight.APIClient("username", "password")



# create listener

listener = StreamListener(max_latency=None)



# create historical stream (update file_path to your file location)

stream = trading.streaming.create_historical_generator_stream(

    file_path="/tmp/BASIC-1.132153978",

    listener=listener,

)



# create generator

gen = stream.get_generator()



data = []

for market_books in gen():

    for market_book in market_books:

        data.append(market_book)```

---

## 2021-01-27 20:52:21 - random channel

**Alex A**

You can do some pretty simple maths to work out roughly what an options price should be, and I’m sure this applies to other assets too, but a load of exchanges have “speed bumps” so you can put up prices, and then if the underlying moves against you the aggressive orders face a 250 ms (or whatever) delay, so even though you’re up against people who are colocated running FPGAs, you can still get out of the way running a simple python bot over the internet.

---

## 2021-01-27 19:48:46 - random channel

**river_shah**

Re asset class for retail quant, I would recommend to steer clear of CME and EUREX futures trading. They are extremely deterministic and dominated by &lt; 5 players for delta one strats. If you know about options, then your space opens up significantly as options trading (especially delta neutral strats) are more about modelling than execution speed. Look at more niche sectors, for example agricultural products, Chinese products, LME metals. I am not sure about market access for those at the retail level though.

---

## 2021-01-21 15:14:20 - issues channel

**Jonjonjon**

[@UE72WCRR8](@UE72WCRR8) I had similar problems due to a memory leak.



In `process_market_book` I stored market-level data, and forgot to delete it when the market closed.

---

## 2021-01-21 15:08:15 - issues channel

**jhaa**

I have a slow thread and a fast thread that do different things and have different urgencies. A week ago I could see in the logs that the slow thread stopped working because I only had output from the fast thread in the logs. Today it was the other way around. There are no error messages.

---

## 2021-01-21 12:02:19 - strategies channel

**Misha**

Be careful with published performances. It might be "here are our last 2 years' returns", because the year before that they made a big loss

---

## 2021-01-21 11:50:58 - strategies channel

**Jonjonjon**

Where can numerai's performance be seen?

---

## 2021-01-21 09:34:16 - strategies channel

**Jonjonjon**

How did Mercurius raise EUR 800k? They've got a well presented website. Shame about the performance statistics.

---

## 2021-01-21 09:20:13 - strategies channel

**liam**

But if you are backtesting there is no latency 'time' is not updated till the next book comes through

---

## 2021-01-21 09:17:54 - strategies channel

**liam**

What do you mean latency?

---

## 2021-01-21 09:07:40 - strategies channel

**Jonjonjon**

No.



I am backtesting a strategy that places orders below/above the best "available to back"/"available to lay" prices. The strategy cancels the orders if a condition is met. However, if the latency is high, the strategy might not cancel them fast enough. So if the latency is too high, I'd prefer not to cancel the orders.

---

## 2021-01-21 06:56:35 - general channel

**Misha**

OK, so you could do it with one connection, but risk adding latency to the orders (coming through the same connection as markets). But chosen not to (a fair enough design decision - I do too)

---

## 2021-01-21 06:48:59 - general channel

**Misha**

So yes, if you are worried about order latency, then you can use two connections/sockets

---

## 2021-01-21 06:46:52 - general channel

**liam**

Sharing a socket means you have to handle all the edge cases and more latency, having a separate socket per connection removes all of this

---

## 2021-01-21 00:21:50 - general channel

**Misha**

Why don't you get market and order data through the same stream? Personally I split the streams, for lower latency, but initially I had both from the same stream. Now I split my markets over multiple streams and have an additional stream for orders

---

## 2021-01-20 21:32:58 - strategies channel

**Jonjonjon**

If I wanted to pull orders if my latency was above 0.5 seconds, what would be the recommended way of doing it in Flumine?

---

## 2021-01-20 18:52:50 - random channel

**Mo**

From memory, the point by point data is not part of the database but is pulled in on demand when you click a button for a given match in the application. I’m not sure if that still holds and how hard it would be to reverse engineer where it’s getting it from

---

## 2021-01-20 18:41:55 - random channel

**bb**

*So you’re conflating two numbers here. Pre race what you are seeing is a projected RPR that the horse will run too. This is is a projection generated pre-race by the in house handicappers for the Racing Post. As you say these numbers are no longer accessible after a race has been run.* 



*What you see post race is a performance metric for the ability the horse showed on the day. This is set by the handicappers taking into account a number of factors including the weight carried by the horse, distance beaten/ahead of the other horses in the race any trouble in running etc. This number is generally set but is also the one I was warning about potentially being adjusted according to subsequent information (e.g. the race turning out to be a strong form race).*

---

## 2021-01-20 16:51:24 - general channel

**river_shah**

I see that each instance of flumine uses up two connections, one for `MarketStream` and another for `OrderStream`. Is this expected behaviour or am I logging in wrong? Can we not use the same connection for both market stream and order stream or does that entail some performance issues?

---

## 2021-01-20 16:43:43 - random channel

**Jonjonjon**

I've done some performance tests. There doesn't seem to be any speed difference if I load the files into ram first, and then iterate over that. It seems to reduce the SSD temperature by 10-20C. Hard to test this well, as if I run the test twice in a row on the same data set, it doesn't heat up on the 2nd run.

---

## 2021-01-20 16:23:55 - strategies channel

**Dave**

Just curious, background suggests some sophisticated data collection and analysis, though overall pnl suggests almost just break even performance

---

## 2021-01-20 16:21:11 - strategies channel

**Dave**

Came across this a while ago when looking for more "industrial" market participants, appears to be some kind of service where you give these guys money and their platform identifies value and takes positions. Thought their PNL path was very peculiar: [https://mercurius.io/en/trader-app/performance](https://mercurius.io/en/trader-app/performance)

---

## 2021-01-19 10:22:40 - general channel

**liam**

you will still have the request latency blocking in the main thread

---

## 2021-01-18 11:52:04 - issues channel

**liam**

If you are not creating any yourself then it is likely to the bflw and the Available class, is the memory leaking or stable?

---

## 2021-01-18 11:49:11 - issues channel

**Unknown**

Hi [@U4H19D1D2](@U4H19D1D2) I am now using pympler to track my memory leaks and found that some 'list' are taking a lot of my RAM memory. Do you know how can I locate the exact lists which are causing the problem?

---

## 2021-01-16 13:38:17 - random channel

**Michael**

You're probably doing exactly the right thing. If you're investing relatively modest sums then a couple of Index funds is ideal because it limits your transaction costs. That's what I did to start with. When the amounts get bigger I think it makes more sense to buy a broad portfolio of individual shares with a leaning towards value as index funds always slightly under-perform the index because of costs and fees whereas shares held directly give you all the performance of those shares. Although I have done well from investing I've always made much more money from betting so I never found it all that exciting. This is likely to be true of any investment. However you probably already know that in real life betting profits don't compound like they do in the movies so you have to put the money somewhere....

---

## 2021-01-12 10:33:41 - general channel

**Carsten**

i got a errand shortly, and will be away for a couple of hours. again thanks for all the help. Hope we can continue later on.  hope i can provide you all the info you need to help me. I was using chrome browser would it make a difference using other browser ?  Also if you think it would be easier if you saw the output your self, we could setup a remote view of it. If its easier and speed up the process so i dont keep you active in here for weeks :slightly_smiling_face:

---

## 2021-01-11 14:46:40 - strategies channel

**Jonjonjon**

Do bet volumes tend to vary a lot by season? I don't really have any stats gathered to measure performance properly.:disappointed:

---

## 2021-01-11 08:14:20 - general channel

**liam**

Just released a beta of [https://github.com/liampauling/betfair/pull/371|2.12.0b0](https://github.com/liampauling/betfair/pull/371|2.12.0b0) which contains the streaming refactor, using [@UBS7QANF3](@UBS7QANF3) benchmark looking at the following improvements:



```# lightweight (2.3x improvement)

#  master: 6.860s (100%|██████████| 10/10 [00:06&lt;00:00,  1.46it/s])

#  2.12.0: 2.998s (100%|██████████| 10/10 [00:02&lt;00:00,  3.34it/s])



# Non lightweight (3.4x improvement)

#  master: 36.005s (100%|██████████| 10/10 [00:35&lt;00:00,  3.60s/it])

#  2.12.0: 10.625s (100%|██████████| 10/10 [00:10&lt;00:00,  1.06s/it])



# Non lightweight with flumine patching/listener/stream (2.8x improvement)

#  master: 13.896s (100%|██████████| 10/10 [00:13&lt;00:00,  1.39s/it])

#  2.12.0: 5.005s (100%|██████████| 10/10 [00:04&lt;00:00,  2.00it/s])```

A quick [https://github.com/liampauling/flumine/pull/361|test](https://github.com/liampauling/flumine/pull/361|test) on flumine and this equates to around a 2.3x speed improvement which is massive and equates to flumine running through a market faster than the current lightweight implementation! CPU has also halved when running live which is a nice bonus.



Going to stay in beta until I can test this properly in production but I have carried out some regression tests on various markets throughout (hasn't just been optimised for this one market) However feel free to test when backtesting and let me know if there any bugs.

---

## 2021-01-10 20:41:00 - strategies channel

**Michael**

I think a lot of this comes down to how you do your analysis. Some people are into analysing the performance of a strategy as a whole and will test strategy A against strategy B and so on. To me this doesn't make much sense as your strategy is only visible or meaningful to you, the exchange only sees your bets and treats them individually. Personally I like to take my bets independently of whatever triggered them and analyse them that way round.

---

## 2021-01-10 20:36:31 - general channel

**Dilla**

:wave: Perhaps someone knows how to open bet365 livescore bypassing the main site?

In my country bet365 is blocked, and VPN does not accept this site or only for a short time.

I could only find such options. But they are very slow. They differ in the speed of updating the livescore, which is on the main site. And also there does not show every point in tennis, only games.

[https://livescore.sportradar.com/bet365/en/tennis](https://livescore.sportradar.com/bet365/en/tennis)

[http://ls.betradar.com/ls/livescore/?/betfair/en/page](http://ls.betradar.com/ls/livescore/?/betfair/en/page)

---

## 2021-01-07 13:58:55 - general channel

**Taking Value**

Infact I say 20mins but that's how long it takes on my laptop, the EC2 environment is deffinately running slower than that but I haven't had time to investigate why yet. Spent most of yesterday re-doing my code to see if that could speed it up but it hasn't.

---

## 2021-01-07 13:52:35 - general channel

**liam**

Full fat then, you can patch priceSize like flumine does, this gives 3-4x speed improvement and you can wait for v2.12.0 which will hopefully give the same again once I have finished it. Aim is for sub 1s per file, do you know how many seconds each file is currently taking? Are you processing using multiple cores / processes?

---

## 2021-01-07 11:48:42 - general channel

**D C**

File IO can be slow though. I store a large amount of market data as text files and extracting anything useful takes a lot longer than would be the case if it were all in a database. Depends on what you need really and how much data you are processing but DB definitely has advantages.

---

## 2021-01-05 09:27:07 - random channel

**river_shah**

If you truly want to avoid heuristics then my suggestion is to look at markowitz multi period mean variance optimization (this is the generalisation of kelly to multiple bet scenarios with no assumptions of independence either)

---

## 2021-01-05 09:23:39 - random channel

**river_shah**

hmmm, maybe look up multi period mean variance optimization papers. [https://opus4.kobv.de/opus4-zib/files/418/SC-99-30.pdf](https://opus4.kobv.de/opus4-zib/files/418/SC-99-30.pdf)

---

## 2021-01-03 14:04:06 - general channel

**Dave**

Liking the optimizations [@U4H19D1D2](@U4H19D1D2) , glad to see less attribute lookups!

---

## 2021-01-03 10:46:10 - general channel

**Lee**

wow, that's a massive performance increase

---

## 2021-01-03 10:45:25 - general channel

**liam**

[@UBS7QANF3](@UBS7QANF3) when you get a second can you try issue373 again on your machine? With a small change required on the listener I am getting the following (same file)



```listener = StreamListener(max_latency=None, lightweight=True, debug=False, update_clk=False)```

```# master: 6.879s  (100%|██████████| 10/10 [00:06&lt;00:00,  1.46it/s])

# 373: 3.640s  (100%|██████████| 10/10 [00:03&lt;00:00,  2.75it/s])```

This is even without c/rust libraries :sunglasses:

---

## 2021-01-03 00:42:27 - strategies channel

**Michael**

I agree with [@U0128E7BEHW](@U0128E7BEHW)’s advice but I'd add that 15% matched seems very low to me. People's operations differ but personally I look to get a much higher proportion on, like maybe 70% for a purely market based strategy.  Might you be asking for too much value? Have you tried asking for less? Also at just 15% matched I'd bet that the orders that do match do so quite a long time after being posted (unless you're cancelling most of your transactions quite quickly). If your bets match too slowly then the signals you're using are rendered ineffective because they've likely expired by the time your money is taken. Any profit that's left probably either comes from the spread or from skimming a bit of noise - either way it won't be much and won't scale well.

---

## 2021-01-02 12:26:21 - general channel

**Mo**

Where benchmark.py is:



```import time



import betfairlightweight

from tqdm import tqdm

from tqdm import trange

from betfairlightweight import StreamListener



trading = betfairlightweight.APIClient("username", "password", "app_key")

listener = StreamListener(max_latency=None)

stream = trading.streaming.create_historical_generator_stream(

            file_path="/tmp/1.172557162",

                listener=listener,

                )

gen = stream.get_generator()

# Warmup

number_of_market_books = sum(1 for market_books in gen())

start_time = time.time()

for _ in trange(10):

    for market_books in tqdm(gen(), total=number_of_market_books):

        pass

print(time.time() - start_time)```

---

## 2021-01-02 11:39:15 - general channel

**Mo**

Even ignoring his example, when I retested it myself the performance was pretty much the same as the pure Python implementation

---

## 2021-01-02 11:36:11 - general channel

**liam**

I need to have another look but @[https://github.com/synapticarbors|synapticarbors](https://github.com/synapticarbors|synapticarbors) example isn't representative of the data you get from the streaming API as you get very different speed comparisons due to the way python caches certain calls + the o notation this problem has

---

## 2021-01-02 11:30:47 - general channel

**liam**

On the subject of performance just been [https://github.com/liampauling/betfair/pull/374/commits/52e439d3b6ee6bd3ca585bd7bd4cacf1ac40168e|refactoring](https://github.com/liampauling/betfair/pull/374/commits/52e439d3b6ee6bd3ca585bd7bd4cacf1ac40168e|refactoring) the marketCache in the bflw streaming code, seen huge reduction in function calls and thus runtime by only serialising the runner data when there has been an update. This will also fix the issue you raise [@ULDAVFDRP](@ULDAVFDRP) with removed runners sometimes not being present in the book



[@UBS7QANF3](@UBS7QANF3) hoping to look at your PR on refactoring the Available class as well soon (sorry been distracted recently)

---

## 2021-01-02 10:16:23 - general channel

**liam**

it is pythonic but ugly code tends to be quicker, its a balancing act between readability and speed. Backtesting opens up the performance issues Dave mentions because you start to make 100's of millions of function calls so saving 0.001s on each execution suddenly becomes seconds or even minutes

---

## 2021-01-02 09:34:02 - general channel

**Misha**

Basically I know what takes time to execute in my code, and converting string lookups to integer lookups wouldn't save me 0,01% of the processing time. Good design is how you gain performance. I have a pipeline threading framework so even if running hundreds of threads there is no thread contention. Immutable objects that can be shared across thread with no copying is the biggest performance gain I have made in the last couple of years

---

## 2021-01-02 09:15:02 - general channel

**Misha**

Negligible in terms of performance - makes no difference at all

---

## 2021-01-01 21:57:25 - issues channel

**Misha**

Yes, all database servers have improved performance and efficiency over the years

---

## 2021-01-01 14:29:00 - issues channel

**Misha**

Oh, and disk I/O is incredibly slow in comparison to in-memory processing. Databases even slower. Don't have this stuff in a time-sensitive processing pipeline unless absolutely necessary

---

## 2021-01-01 14:25:35 - issues channel

**Misha**

Things to watch for in any language: string concatenation if strings are immutable (true for C#), sorted lists versus dictionaries (if you don't need sorting, dictionaries which use hash tables are much faster). streaming to/from text (always comparatively very slow), deep copying of tree-like objects (better to copy references to nodes that don't change)

---

## 2021-01-01 13:19:21 - issues channel

**liam**

+1 [https://wiki.python.org/moin/PythonSpeed/PerformanceTips|this](https://wiki.python.org/moin/PythonSpeed/PerformanceTips|this) is a good read if you haven’t read yet

---

## 2021-01-01 12:16:27 - issues channel

**Misha**

Optimisation is about working out the bottlenecks, as one or two simple optimsations usually account for 90% of the performance gains. But I still come back to the fact that if you aren't measuring the performance gain, how would you know if you are getting a gain/

---

## 2021-01-01 12:09:17 - issues channel

**Misha**

Is Python's implementation slow?

---

## 2021-01-01 12:08:08 - issues channel

**Dave**

Well, at least newer versions of python use a faster decimal implementation. Generally I like to keep things as fast as possible, maybe in real-time trading it doesn't matter too much given network bottlenecks and whatnot, but if it cuts my backtesting time 10x due to a large number of markets pumping through at once then I find that to be a win. For me, decimal slowdown is indeed negligible.

---

## 2021-01-01 12:03:35 - issues channel

**Misha**

Would think that any performance penalty would be negligible

---

## 2020-12-31 12:46:05 - general channel

**river_shah**

Currently I am using cloud service providers for back testing however when it comes to live trading, just launching scripts off my London based laptop (have high bandwidth reliable residential broadband). Could I please be guided on what the best way to run a prod model may be from a colo perspective? Speed is not so important to me but if I can get a few milliseconds for free running from AWS Dublin or some other location, won’t say no to it. Think this topic was discussed earlier but search history has run out. Thanks

---

## 2020-12-31 08:03:46 - random channel

**Oliver Varney**

Cant remember exactly what the standard version has vs it but it has stuff like viewing pandas data frames , coverage for testing, threading debugging and performance stuff. Maybe not worth it for a developer of my skill but yes, the debugging tools are much better. Im surprised you dont have it. I think its only a few quid a month. They have monthly rolling options so id recommend trying it for a month and then binning it if you dont think its worth it

---

## 2020-12-29 10:17:40 - strategies channel

**Mo**

My view is that you would be crazy to unnecessarily introduce 150ms of latency when betting in-play

---

## 2020-12-24 21:12:57 - random channel

**Dave**

Just use a proxy list that refreshes daily and rotate proxies on each request (if you don't care about extra latency in the order of few hundred ms)

---

## 2020-12-24 20:24:42 - general channel

**Jonjonjon**

Happy Christmas everyone. BFLW has put in a solid performance for me this year. Thanks for sharing [@U4H19D1D2](@U4H19D1D2).

---

## 2020-12-15 19:34:02 - general channel

**river_shah**

very cool. do you know if the file stays in host memory once opened with smart_open? i.e if I want to read the same file multiple times and want to avoid excess latency of s3

---

## 2020-12-15 19:17:28 - general channel

**river_shah**

We can benchmark using the dummy strategy by the way. The patching method that [@UBS7QANF3](@UBS7QANF3) suggested is very easy. Using bz2, in some simple backtests I see runtime increase 3-6% but space saving is 8-10X. Well worth the speed vs space saving for my use case.

---

## 2020-12-15 17:23:21 - random channel

**Oliver Varney**

I use sql server, and I think they have something similar. I think it came down to performance in the end. I purely only use it for training models, basically pushes the historical files into it

---

## 2020-12-10 17:04:33 - general channel

**river_shah**

Why would horse racing change drastically please? For example I can understand that for football having crowds makes a huge difference (due to home/ away impact), how does crowd size interact with horse performance?

---

## 2020-12-10 12:13:59 - general channel

**Oliver Varney**

ive probably asked this before, but think ill recheck due to the market_book.runners issue ( requiring market catalogue also to rebuild runners), but is it a safe assumption to assume that runners remain in the same position in the list, even after stream reconnects (which flumine handles). Off memory the cache in lightweight adds them and the order remains, but just want to double check

---

## 2020-12-10 11:45:56 - general channel

**liam**

problems as in betfair updating slower than betdaq/others? yes, check out the graphs after a removal

---

## 2020-12-07 17:25:55 - issues channel

**liam**

The issue you have is that things rarely recover, you have a latency issue that then exponentially increases as the process hogs CPU and before you know it you are looking at 500+ seconds delay with no escape.



Skipping updates before processing could help but I would always push for finding and removing any potential bottleneck.

---

## 2020-12-07 17:09:20 - issues channel

**Oliver Varney**

[@UE72WCRR8](@UE72WCRR8) I had a latency issue due to some dodgey code (for which i have fixed now). My experience of what will happen if your check + process functions in flumine take longer to process then the stream takes to update is a steady increasing in backlogged market books. you can add a latency check in these flumine functions not to process the market book if the latency is greater than X s (so you catch up). Id assume it would be much more preferable to fix the code to be able to keep up with the stream.

---

## 2020-12-07 01:18:58 - strategies channel

**MacrcoPolo**

Short answer is this: with kelly there's 2 highly undesirable things happening, despite it being the optimal way to grow _log_ wealth. Firstly, the setting for kelly is that you're not constrained by the amount you can wager, and that you know the edge on the bet. If you have uncertainty in your edge, then wagering slightly smaller is optimal I believe (I don't have the proof at hand - can try and throw something together tomorrow if you want). Second, even if you are wagering at kelly where the relevant odds and proabilities are known, you still put yourself in a spot where your bankroll halfs before doubling 1/3rd (again, this is from memory, might be a little higher, a little less) of the time. That's terrifyingly large swings for most mortals, and not good for the mind. Cut to half kelly, and you dramatically reduce the chances this happens (I have no hard numbers and it's 1 am!).

---

## 2020-12-06 17:18:47 - strategies channel

**bb**

As the impact of odds on a model's performance will differ according to each

---

## 2020-12-03 15:57:14 - strategies channel

**Dave**

Not much use forecasting over a horizon shorter than your latency (where latency is anything slowing you down including the enforced delay). Remember it's asymmetric though, so your total latency for cancels doesn't include this enforced delay ;o

---

## 2020-12-03 12:57:52 - strategies channel

**liam**

So two issues I can see, the first one is the logging module is actually spiralling out of control using more and more CPU cycles as the latency increases the second is the `_add_market` function is slow, its slow because `.info` property is really really slow however not sure why it is soo slow

---

## 2020-12-03 12:18:50 - strategies channel

**birchy**

[@U4H19D1D2](@U4H19D1D2) Update:

The following runs for about 15 minutes with CPU at 100% and memory gradually increases until 80%+ and then starts using swap. Lots of 'High Latency' warnings in the logger ~700 (not sure if this is seconds or milliseconds?). This is on a Lightsail instance with 2GB RAM. Are you able to replicate?

```class Dummy(BaseStrategy):

    """dummy strategy"""

    def __init__(self, *args, **kwargs):

        BaseStrategy.__init__(self, *args, **kwargs)



    def check_market_book(self, market, market_book):

        return True



    def process_market_book(self, market, market_book):

        """only called if check_market_book() returns True"""

        return



    def process_orders(self, market, orders):

        return```

```strategy = Strat(

    conflate_ms=3000,

    market_filter=bflw.filters.streaming_market_filter(

        event_type_ids=['7', '1', '4339'],

    ),

)

framework.add_strategy(strategy)

framework.run()```



---

## 2020-12-03 08:24:58 - random channel

**Artur Gräfenstein**

You can’t say it’s not JSON. Transit is on top of JSON.

```Transit is designed to be implemented as an encoding on top of formats for which high performance processors already exist, specifically JSON and MessagePack. ```

---

## 2020-12-02 17:19:07 - issues channel

**liam**

Always a balancing act between speed and readability/use but this is worth the confusion, see my favourite [https://github.com/liampauling/flumine/commit/64ae76f0cb5571a040ce9904febf35df733931c4|commit](https://github.com/liampauling/flumine/commit/64ae76f0cb5571a040ce9904febf35df733931c4|commit) 

---

## 2020-12-02 12:22:48 - general channel

**Mo**

• GPS data is provided by TPD ([http://www.totalperformancedata.com/](http://www.totalperformancedata.com/))

• Betfair have a number of licenses they give out for free (speak to your account manager)

---

## 2020-12-02 11:50:16 - general channel

**Thomas JAMET**

I am surprised you don't :grin:

I think that players tend to graduate from ITF to ATP Challenger (and on to other tournaments) and I hope that tracking their performance early on can give some insight in events offered on BetFair. Does it make sense?

---

## 2020-11-30 10:54:38 - general channel

**Newbie99**

[@UFPEU7URG](@UFPEU7URG) Others are far more sophisticated than me, but one thing I'd say, is that for streaming I very quickly found a MySQL database impossibly slow to connect to for streaming purposes, so I would consider another option if you need to refer to external data sources (e.g. json, csv or Reddit as example).



In terms of accessing other scripts, with BFLW using multiple threads I think is probably the approach you need, but it may be worth considering Flumine as that has 'worker' threads built in by design which appear to be what you might need.

---

## 2020-11-30 10:27:31 - strategies channel

**birchy**

So I have a preplay strategy that I'm currently live testing on UK horse racing WIN markets. Long term, I want to extend this strategy to cover _every_ horse racing market, followed by implementation on other sports and ultimately coverage for ALL betfair markets.

Last week, during initial testing, I attempted to start Flumine with:

```market_filter=bflw.filters.streaming_market_filter(

    event_type_ids=['7'],

),```

...and managed to crash an AWS Lightsail instance when CPU &amp; RAM (2GB) hit 100% during startup. This is only a small % of where I actually want to be. I know Flumine creates a lot of objects, but is it actually THAT resource hungry?

Regarding implementing ALL markets, what's the recommended way to achieve this? Currently thinking that I may have to redesign as a polling bot instead. The strategy is not speed sensitive.

---

## 2020-11-27 11:42:25 - random channel

**Oliver Varney**

question for the techies, I am just running cprofilev suggested by liam to find slow parts of code. I have already found some simple enhancements. one thing that is throwing me of is, that if I sort by tottime when looking at the report  {method 'acquire' of '_thread.lock' objects} comes out massively at the top. Is this expected?

---

## 2020-11-27 08:12:13 - general channel

**liam**

So a market update comes in and processed through all strategies, after this an order package is created which like say can have multiple orders to reduce the number of requests.



The number of orders shouldn’t increase latency, are you monitoring CPU / ram? AWS? And have you tried profiling? I use cprofilev, quickly show you anything that is slow.

---

## 2020-11-27 08:04:40 - general channel

**Oliver Varney**

morning all, im looking for some advice when it comes to effectively batching up orders (place and cancels) within flumine. Now I have upped the number of trades + strategies I think I may be ineffectively sending updates to betfair (leading to latency from time to time, not confirmed yet but a hunch from looking at the logs ). I believe order packages are designed to combat this, by batching up from market orders from the market blotters (I am right in my understanding?). I am looking to better understand this process and how I could improve my code to prevent unnecessary extra messages to betfair. Does anyone have any advice / be able further explain the process and how it can be optimised ?

---

## 2020-11-26 15:27:31 - random channel

**thambie1**

[@U01EYDA8345](@U01EYDA8345) In backtesting, I have noticed changes in the performance in soccer pre vs post corona.

---

## 2020-11-26 13:04:50 - general channel

**Oliver Varney**

[@U4H19D1D2](@U4H19D1D2) would it be worth adding the latency attribute in _process_market_books to the market book, so that in check_market_book if for what every reason there is a temporary spike in latency we can ignore processing this market_book? or is this a bad idea / already available somewhere

---

## 2020-11-25 19:32:06 - strategies channel

**JC**

Hi guys, got a question about evaluating the performance of a model. What is the best way, mathematically, to evaluate how accurate a model is at spitting out probabilities in-play. I guess you could for example group together all occasions where the output is 0.6 implied probability and if close to 60% of these predictions are correct then it is a good model? Is there a better way of doing this?

---

## 2020-11-25 12:47:46 - general channel

**A**

Blimey. Ok yeah I think I've connected to a market stream inherently through using Flumine. What approach would you recommend for storing the market catalogue? Is the some form of side worker? Stored in memory or a DB? Quite new to the concepts and how the system is put together (I'm an iOS dev by trade) - should be good once I get the basics

---

## 2020-11-25 09:33:31 - general channel

**liam**

I was involved in the alpha but haven’t used it since, we could do some really cool stuff with tracing within flumine for monitoring latency throughout 

---

## 2020-11-25 09:21:39 - general channel

**liam**

[https://docs.sentry.io/product/performance/distributed-tracing/|https://docs.sentry.io/product/performance/distributed-tracing/](https://docs.sentry.io/product/performance/distributed-tracing/|https://docs.sentry.io/product/performance/distributed-tracing/)

---

## 2020-11-25 09:20:34 - general channel

**liam**

Comes at a performance cost though but can look to enable / disable by default 

---

## 2020-11-25 09:14:08 - general channel

**liam**

In my old framework I had some tracing built within the Event object that I could port across to give you creation time / age / latency / time spent being processed etc. which was then logged that might be handy

---

## 2020-11-25 09:12:43 - general channel

**Lee**

I was thinking of some sort of measurement of the methods called every update. Guess the latency warning gives a pretty good idea if things are getting too slow.

---

## 2020-11-24 13:09:38 - general channel

**jgnz**

hi guys, i am jumping back in after a couple of years away. i am trying to create a basic strategy using streaming data, which is dependent on the runner name. I have a couple of questions about that;

• In a market catalogue, is a selection id unique for each runner name across all markets and events? ie a can slowly build up a reliable mapping table of selection ids and runner names.

• is it possible to make a streaming filter request that returns the market catalogue? or does it need to be a separate list_market_catalogue call(i assume yes)?

Given that my strategy needs the runner name and it is slow to make a request just for that, i am planning on building a table of selection ids and runner names in local database. checking if the runner's selection id is present, and only call list_market_catalogue if it is not found. Does that sound like a reasonable action if i need the runner name for my strategy?

---

## 2020-11-23 23:00:27 - random channel

**qwerty.nat**

Indeed, i'm not even allowed to do volunteer work without sign off. I do work for a HFT but doing ultra low latency trading, and i disagree with Misha that sports is a lot more consistent. There are lots of times where we know the price will change with 100% certainty, so if you are fast enough you can scalp a tick here and there. Free money basically. However to get to that point you need massive investments in technology / market structure research etc.

---

## 2020-11-23 16:28:12 - issues channel

**thambie1**

It's a huge pain in my development cycle waiting for backtests to run. And I've already done a ton of optimizations on my code base.

---

## 2020-11-23 05:46:28 - issues channel

**Mo**

Your results are to be expected. Improving betfairlightweight performance is an active topic of discussion here. In the mean time, you have plenty of cores so the multiprocessing approach is the way to go

---

## 2020-11-23 01:47:00 - issues channel

**Unknown**

Hi,



First of all, thank you for the betfairlightweight &amp; flumine libraries.



I am seeking advice from the community w/ respect to latency when backtesting w/ Flumine. The objective of the tests below is to compare the performance of Flumine in the context of backtesting with the performance of a simple, naive implementation.



Test1:

Using [https://github.com/liampauling/flumine/blob/master/examples/backtest.py](https://github.com/liampauling/flumine/blob/master/examples/backtest.py) with an empty strategy. The log level has been raised to CRITICAL



Test2:

A python script  iterates thru the same collection of files, reads each line and parses them as JSON. The JSON structure doesn’t get processed further.



Both tests run on the same machine sequentially. The machine has 60GB of memory and 16 CPUs.



Size on disk for data is 1.6M for `betfair/tennis/xds_nfs/edp_processed/BASIC/2019/Jan/15`



Test1 runs in ~2 minutes

Test2 runs in 5 seconds



I understand that Test1 does a lot more than Test2. Flumine will create data structures, maintain states, etc…



But am I doing it right? Before I go the route to run profiler, what would be some comments?



PS: I did try the multithreaded approach found here [https://betfairlightweight.slack.com/archives/C4HL6EZTQ/p1598171342144900](https://betfairlightweight.slack.com/archives/C4HL6EZTQ/p1598171342144900) courtesy of Jonjon &amp; Birchy and it did run in ~5 seconds. Would love to get some thoughts though. Thank you!

---

## 2020-11-20 21:49:35 - random channel

**V**

I guess it depends on how often you bet in a given week. If it’s like 10 or something then the above will be useless, but if it’s it’s like 50+ then the above could still help... if a week isn’t too slow to notice something up that is

---

## 2020-11-20 21:30:38 - random channel

**Oliver Varney**

Im more wondering about how to judge how your model performing. if your lay high odds, its very easy to hit long winning streaks, which could give a false idea of performance.

---

## 2020-11-20 21:08:27 - random channel

**Oliver Varney**

just thinking in terms of actual performance may take hundreds to thousands bets (depending on exsactly how long) to play out

---

## 2020-11-20 11:48:04 - general channel

**Oliver Varney**

is a measurement of performance

---

## 2020-11-19 12:52:37 - general channel

**D C**

[@U01EYDA8345](@U01EYDA8345) I think it is natural to stick with what you know and to your strengths. I use C++ for me serious bot work but I would never recommend anyone learn C++ to write bots. I think node is a very natural choice for a betfair bot and if you are experienced already maybe stick with it. You talk about speed a great deal but is this so important? If you are doing seriously complex back end computation to determine bet selection then I can understand you being worried about node speed. Only you know the answer to that question though. I have heard people on here (Liam I think but don't shoot me if I have that wrong) who say that if you need something THAT fast, then Python is not the right choice. I believe something along the lines of "if milliseconds are important to you then Python is not the tool to use". Apologies if I have that wrong but I am sure I remember a discussion along those lines.

---

## 2020-11-19 11:49:54 - general channel

**Artur Gräfenstein**

ahh cool! Do you think js would be too slow for live betting on betfair? Im actually working on a project with js and want to add Betfair API. But don’t know if it would be better to switch to Python.

---

## 2020-11-19 11:15:41 - issues channel

**Kai**

memory leaks can be an absolute nightmare, further complicated by the internal memory management and caching in python.

The first thing would probably be to make sure that you are still referencing the objects somewhere.

tracemalloc would be a good start, and then there are many other tools.

[https://pythonhosted.org/Pympler/muppy.html](https://pythonhosted.org/Pympler/muppy.html)

---

## 2020-11-18 23:21:18 - issues channel

**Jonjonjon**

Does anyone have any tips for hunting memory leaks in Python code?

---

## 2020-11-18 18:22:56 - strategies channel

**Alessio**

tbh (and here i'm just speaking out of cheap words instead of hard data, but ..) maybe the real fix would be to change the scheme we do these things: now we are having an asynchronous system where the listener updates the book and the market book reader is another thread, that way you have a contention point. another way would be to have a pipeline style where the strategies run in the thread that updates the book, however you may introduce latency if you do any other shit there between one update and the next one (albeit that should be measurable, not sure how much computation there is and one could move to a  lossy view where you batch all the latest updates that weren't read and are in the queue)

---

## 2020-11-18 18:16:08 - strategies channel

**MacrcoPolo**

What about adding an optional number of levels to serialize? The serialization will be far slower when we have to serialize the entire book, but not every strategy needs that. If we only serialize the top n levels (where n is enough for your strat) that can probably shave a decent amount off

---

## 2020-11-18 09:41:47 - strategies channel

**Stefan**

I think you really made big mistake when choosing programming language for your betfair framework. Betfair api is about json data interchange, and have a look how python treats json de/serialization, you take a lot of performance degradation just in such trivial part of code.

---

## 2020-11-18 08:09:22 - strategies channel

**Jonjonjon**

Thanks Mo. Does it give a performance benefit?

---

## 2020-11-17 23:26:08 - strategies channel

**birchy**

[@U0135SLHQBW](@U0135SLHQBW)'s idea is the way to go. It takes me back to about 15 years ago when I was enumerating the ~134 million possible 7-card poker hands in a couple of seconds on a P4 with 1GB or 2GB of ram.

There is often a speed/memory tradeoff, but for this case the memory required for a lookup table is minimal. When designing, bear in mind that sequential lookups are significantly faster than random lookups due to CPU L1/L2 cache.

I don't know how fast the cpython implementation is, but I would imagine that porting the `sort()` and `update()` functions to C would give a decent improvement, particularly the nested `for` loops? I'd also be looking at handling the price/size/etc as integers rather than floats/decimals as they _generally_ (but not always) run faster, depending on the CPU instruction set.



I'd also like to suggest using some bitwise lookups, but it's far too late to be thinking in binary. :grinning:

---

## 2020-11-17 22:25:26 - general channel

**Misha**

Just noting (with all the performance discussion), that in terms of performance, serialisation and deserialisation is very slow, and should be done as little as possible)

---

## 2020-11-17 19:25:35 - strategies channel

**Mo**

Fixed the memory leak but I think there's another bug

---

## 2020-11-17 19:15:21 - strategies channel

**MacrcoPolo**

Just as an aside, in high-frequency trading this is a really big important problem (get the market update and re-arrange the data into a useful form very quickly). Typical approaches use things like b-trees for their log(n) complexity on a variety of opps. The key difference here is that on betfair we know _all_ possible prices in advance, and curcially there isn't many of them. If there's anything you can do to exploit this, you can speed things up

---

## 2020-11-17 19:07:00 - strategies channel

**liam**

Interesting, so you have a dictionary of all the prices/size and then track the top, when profiling it’s the serializing into lists that just kills performance 

---

## 2020-11-17 18:54:12 - strategies channel

**liam**

Not sure you would get the performance increase without C or something really clever 

---

## 2020-11-17 11:56:24 - strategies channel

**Mo**

As recently discussed in this channel, it's hard to find good resources on the Python C API but the concept itself is great if you know C/C++ because it allows you to write performance critical parts of your application in C and the rest in Python. It also works the other way if you want to run Python code from C

---

## 2020-11-17 11:45:46 - strategies channel

**D C**

I saw you referring to reference counting and performance issues caused by object creation and immediately thought of smart pointers and move semantics. Looks like I have put 2 and 2 together and made 5.

---

## 2020-11-17 09:42:35 - strategies channel

**D C**

[@UBS7QANF3](@UBS7QANF3) is C++ an option for you? People who need very high performance code seem to have a huge hard-on for the newer features like move semantics ? Or does C++ not play well with Python?

---

## 2020-11-16 11:14:51 - issues channel

**liam**

and a worker to monitor cpu/ram every few minutes

```import os

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

    )```

---

## 2020-11-13 17:36:17 - strategies channel

**Michael**

I've always had bad code and good strategy and I've done fine. As long as your code isn't terrible the return on the bottom line of better optimised code diminishes quickly for my type of betting. At first I was worried about my code being crumby but then I decided to see how much difference slow code makes by deliberately slowing my code down. I stopped worrying after that. I can see that for someone like [@UBS7QANF3](@UBS7QANF3) it can be important to be well optimised but it does depend on how you're playing. In the end you can make money with good strategy and bad code but if your strategy is poor you will lose - or at least not win much. There's no point in posting bad bets very quickly.

---

## 2020-11-13 14:23:52 - strategies channel

**birchy**

[@U4H19D1D2](@U4H19D1D2) regarding code optimization, have you abandoned gofair? GO is not quite as fast as C, but certainly a big improvement over python.

---

## 2020-11-13 11:16:07 - issues channel

**Chris**

I'm subscribing to all GB,IE racing markets, and I'm only getting 208 markets added to the stream, but if I look up the same parameters in the API-NG I get 217 markets, I assume it is something I am doing rather than a problem at the BF side, anyone any ideas?



``` event_type_ids=["7"], country_codes=["GB", "IE"], market_types=["WIN","PLACE","OTHER_PLACE"]```

```INFO:betfairlightweight.streaming.stream:[MarketStream: 1]: 1.175438218 added, 205 markets in cache

INFO:betfairlightweight.streaming.stream:[MarketStream: 1]: 1.175438034 added, 206 markets in cache

INFO:betfairlightweight.streaming.stream:[MarketStream: 1]: 1.175438035 added, 207 markets in cache

INFO:betfairlightweight.streaming.stream:[MarketStream: 1]: 207 mc added

WARNING:betfairlightweight.streaming.stream:[MarketStream: 1]: Latency high: 1.0258991718292236

INFO:betfairlightweight.streaming.stream:[MarketStream: 1]: 1.175438002 added, 208 markets in cache```



---

## 2020-11-13 10:54:39 - strategies channel

**Alessio**

Yeah i see your point. It's easy to hack up something and do some data science, but to really put the money on it you need extensive platform done spending the necessary time and optimizations.

---

## 2020-11-13 07:27:56 - strategies channel

**liam**

I think with a bit of C we can make bflw fly when it comes to streaming/back testing, I am aiming for 5x speed improvement 

---

## 2020-11-12 20:11:00 - strategies channel

**liam**

This is the [https://github.com/liampauling/betfair/blob/1af4115d5f7493a0b0b4dfb674987830b556464f/betfairlightweight/streaming/cache.py#L14|problem](https://github.com/liampauling/betfair/blob/1af4115d5f7493a0b0b4dfb674987830b556464f/betfairlightweight/streaming/cache.py#L14|problem) it’s the sorting / list comp that is just so slow when backtesting because it is called a *lot* 

---

## 2020-11-12 19:54:52 - strategies channel

**Josh**

Cython backs a lot of scientific/numerical python code (e.g. scikit-learn, pandas, etc) and is pretty easy if you're familiar with a bit of C/C++. You typically don't get a big boost unless you go through and tell the compiler the equivalent C type of variables; It's type inference is pretty weak. But for certain algorithms using the proper data structures, you can get orders of magnitude speed-up and if you're not dealing with actual python objects, you can explicitly release the GIL to get scalable cpu-bound multithreading. Numba is JIT compiles python to efficient machine code, but is primarily for numerical work, so not general purpose, for things like json parsing. As with anything, profile, profile, profile using any combination of cProfile, line_profiler, py-spy, austin, vmprof, etc to find out where the actual hot spots are in the code.

---

## 2020-11-12 19:44:31 - strategies channel

**Alex A**

Although in hft people tend to care a lot more about latency than throughput.

---

## 2020-11-09 08:30:06 - issues channel

**Jorge**

Hi guys, I am not able to pip install betfairlightweight[speed]... I get the error:

• _maturin failed_

      _Caused by: Cargo metadata failed. Do you have cargo in your PATH?_

Can anyone help me?

---

## 2020-10-29 20:37:24 - issues channel

**liam**

It gets patched to speed things up [https://github.com/liampauling/flumine/blob/master/flumine/patching.py|https://github.com/liampauling/flumine/blob/master/flumine/patching.py](https://github.com/liampauling/flumine/blob/master/flumine/patching.py|https://github.com/liampauling/flumine/blob/master/flumine/patching.py)

---

## 2020-10-28 16:39:37 - general channel

**V**

Right, so that kind of latency is to be expected?

---

## 2020-10-28 16:38:32 - general channel

**V**

Hey guys, hopefully I can ask this here: what type of response latency can be expected for placing orders? In my case I see it in the couple hundred ms range. This is most likely a betfair thing as others have mentioned a similar response time in the betfair forums, but I couldn’t find any real info as to why that is.

---

## 2020-10-26 09:38:58 - general channel

**liam**

[https://github.com/liampauling/betfair/blob/master/HISTORY.rst#291-2020-10-26|2.9.1](https://github.com/liampauling/betfair/blob/master/HISTORY.rst#291-2020-10-26|2.9.1) released, historic improvement ([@UBS7QANF3](@UBS7QANF3)) and I have moved all C/Rust libraries to a speed install

```pip install betfairlightweight[speed]```

---

## 2020-10-22 14:00:04 - strategies channel

**river_shah**

```    def _check_pending_packages(self):

        for order_package in self._pending_packages:

            _client = order_package.client

            if order_package.package_type == OrderPackageType.PLACE:

                if order_package.elapsed_seconds &gt; (

                    _client.execution.PLACE_LATENCY + order_package.bet_delay

                ):

                    self._process_order_package(order_package)

            elif order_package.package_type == OrderPackageType.CANCEL:

                if order_package.elapsed_seconds &gt; _client.execution.CANCEL_LATENCY:

                    self._process_order_package(order_package)

            elif order_package.package_type == OrderPackageType.UPDATE:

                if order_package.elapsed_seconds &gt; _client.execution.UPDATE_LATENCY:

                    self._process_order_package(order_package)

            elif order_package.package_type == OrderPackageType.REPLACE:

                if order_package.elapsed_seconds &gt; (

                    _client.execution.REPLACE_LATENCY + order_package.bet_delay

                ):

                    self._process_order_package(order_package)```



---

## 2020-10-22 06:49:01 - general channel

**liam**

There was a bug where the latency warnings were being shown incorrectly on snapped data but his has been fixed. However if you are just recording data you shouldn’t be getting high CPU, have you set the streaming_timeout? Should be None for data recording 

---

## 2020-10-21 21:17:44 - general channel

**ricky**

Apologise, I havent used the lastest version of flumine. Occasionally when inplay football began, my CPU loading was over 100%, and memory usage is 16.4%.

I use Ubuntu 20.04. Any suggestion what tool i can use for debugging the root cause of high CPU load? My initial thought was the filesystem (nautilus), becasue i keep recording data into a file, but i have not way to prove it becuase it happened occasionally.

---

## 2020-10-21 21:07:27 - general channel

**ricky**

Last hour i got warning message from flumine: "levelname": "WARNING", "message": "High latency between current time and MarketBook publish time".

Is it just me? It looks like 10-15 mins delay.

---

## 2020-10-16 08:13:27 - random channel

**Chris**

Amazon Linux is built off of Redhat/CentOS I believe, so performance very similar there

---

## 2020-10-12 17:52:43 - strategies channel

**birchy**

I have found a couple of inplay strategies via Flumine backtesting that are showing a positive return over 500 markets/~4000 bets. Going to test against a bigger sample, but am just wondering how backtesting compares to live betting? I've not (yet) run any live betting with Flumine as I'm taking cautious steps due to the sheer speed of streaming, which means a small mistake can quickly become expensive. What would you consider as a "goer"?

---

## 2020-10-12 11:10:23 - strategies channel

**Michael**

I look at a whole bunch of things separately: Profit on each transaction if fully matched at flat stakes, proportion of that realised and so on. Optimising stakes for similar transactions is just profit. I also run a fixed 'benchmark' simulation on every market so that I can compare groups of markets in terms of their overall capacity for getting value bets in and try to control for the background performance of markets in that way (to factor out things like the post lockdown surge). It get quite complex though.

---

## 2020-10-12 10:36:16 - strategies channel

**birchy**

Ironically, I only calculate ROI every few months as more of a sanity check than anything else. As long as my balance goes up steadily, I don't really check ANYTHING, although I should probably do more analysis and optimization.

---

## 2020-10-08 19:25:31 - issues channel

**Unknown**

I was looking for memory leaks in my bot using tracemalloc, and found (I think) some big ones in bflw. This is a little over my head, and I'm not sure what I'm looking at. But basicaly I made empty bflw bot that only subscribes to all UK/AU/US racing markets, also to order stream from my live bots (~50k bets a week) and counts currenty open markets. Ran this for a 7-8 days, dumping memory snapshots every 10minutes, graphed it. Red line is resident memory, blue currenty subscribed open markets. bflw 2.8.0. Hope this helps

---

## 2020-10-08 15:55:34 - issues channel

**liam**

I have tried almost everything in finding memory leaks and this is what I did to find the above in flumine/bflw using `pympler`



```from pympler import summary, muppy

from pympler.util import stringutils



def get_pympler_memory():

    mem_summary = summary.summarize(muppy.get_objects())

    mem_summary = [

        [i[0], i[1], i[2], stringutils.pp(i[2]).lstrip()] for i in mem_summary

    ]

    mem_sorted = sorted(mem_summary, key=itemgetter(2), reverse=True)

    mem_sum_bytes = sum([i[2] for i in mem_sorted])

    mem_sum_human = stringutils.pp(mem_sum_bytes).lstrip()

    return mem_sum_bytes, mem_sum_human, mem_sorted```

Used like so:



```mem_sum_bytes, mem_sum_human, mem_sorted = get_pympler_memory()

[http://logger.info|logger.info](http://logger.info|logger.info)(

    "pympler",

    extra={

        "total_bytes": mem_sum_bytes,

        "total": mem_sum_human,

        "memory": mem_sorted[:64],

    },

)```

You can then plot or just look to see which objects are increasing in size or count.

---

## 2020-10-08 11:16:34 - issues channel

**Jorge**

Hi guys, do you know of any tool to monitor RAM usage by a Python process? I am wondering if it's the API calls what is using most of my RAM memory, or maybe it is that I am saving a row to pandas DataFrame every 10 secs with the state of the bot and I keep this dataframe in memory...

---

## 2020-10-07 08:14:29 - issues channel

**liam**

Isolated the flumine [https://github.com/liampauling/flumine/issues/248#issuecomment-704743300|memory leak](https://github.com/liampauling/flumine/issues/248#issuecomment-704743300|memory leak) to the bflw cache:man-facepalming: Going to look at either adding a clear/remove_market function or handle a clear up within the code itself (remove if closed for x seconds), not sure what peoples thoughts are on the latter as it may cause issues when betfair update results etc. at a later date

---

## 2020-10-06 15:31:35 - general channel

**Oliver Varney**

off memory I did something like strategy_hash-internal_trade_id-order_id, with it being 6-6-18

---

## 2020-10-06 08:58:09 - issues channel

**D C**

So it is actually a problem with the python internals? Something failing to release memory? I don't have much experience with languages in which you don't do your own memory allocation and cleanup so quite interested in how other languages achieve cleanup properly.

---

## 2020-10-06 08:54:57 - issues channel

**liam**

You have very limited control, python does all of the memory allocation internally using c/references

---

## 2020-10-06 08:53:45 - issues channel

**D C**

I don't really know python other than pure basics.  Does it give you control over dynamic memory allocation or is this due to some shoddy libraries/packages that already have leaks?

---

## 2020-10-06 06:46:44 - issues channel

**liam**

It’s very easy to introduce memory leaks in python, I know there is one in flumine but shouldn’t be when just recording data 

---

## 2020-10-05 23:48:26 - general channel

**ricky**

I previous used lightweight steaming API, now switch to Flumine for price recording.

I did a period of 90 mins ( football in-play) performance testing between these two, steaming API give me around 20000 data points, Flumine give around 25000 data point. For trade volume, i can see slight diffentence between these two.

Any thought, which framework is more accurate in term of steaming?



Flumin version: 1.12.1

betfairlightweight version 2.8.0

---

## 2020-10-05 21:57:38 - issues channel

**birchy**

Not sure if this is related, but I've noticed my marketrecorder is stopping unexpectedly every 4 or 5 days. Only thing I can find in the logs is that it reports high latency for a couple of hours and then exits with no other errors logged. Could it be a memory issue? Have just restarted with `logging.level = WARNING` to try and narrow it down a bit.

Flumine 1.12.3

Orjson 3.3.0

Edit: have just upgraded Flumine to 1.13.0

---

## 2020-10-05 19:35:59 - issues channel

**liam**

moved from ujson due to memory leaks and random faults however orjson complains at numpy types and now this

---

## 2020-10-03 00:37:41 - general channel

**Dave**

FWIW - I tried republishing market data internally over zmq pub/sub and latency impact is negligible. So if you wanted a setup where you had say, one process per market, then you can't use a dedicated streaming session per market if you plan on trading more than 10 markets concurrently (for the reason Misha mentioned above). But republishing internally is a way around that, and the added latency is dwarfed by external network latency. Decided not to opt for Redis now given zmq is sufficient

---

## 2020-10-01 14:46:14 - general channel

**Dave**

Qq - are there any negative implications to subscribing to the same set of markets twice from separate clients? Am I using up any alloted quota with the second subscription data-wise (bandwidth perhaps)? Still reconsidering re-publishing market data internally vs subscribing to it directly from all consumers. Don't want to end up throttled on Betfair side if I can just republish internally with negligible latency.

---

## 2020-09-27 19:48:28 - random channel

**Oliver Varney**

I thinks its secondary, you have a requirement first then if you need a feature that is suited to an in memory database /key-value store you use it.

---

## 2020-09-27 16:23:01 - random channel

**Dave**

Ahh efinancialcareers, perhaps _the_ worst "journalism" in the finance industry. I recall licensing is silly expensive, and their free licenses used to have some restrictions (time limit and performance-based I think?). Not sure if the latter is still the case. Also, that article is total BS :joy:

---

## 2020-09-25 10:02:11 - issues channel

**Chris C**

On the high latency warnings: I get crazy latency warning as well, but only for markets where nothing is happening, like:

```{"asctime": "2020-09-25 08:58:20,824", "levelname": "WARNING", "message": "High latency between current time and MarketBook publish time", "market_id": "1.173462701", "latency": 2271.97003865242, "pt": "2020-09-25T08:20:28.854000"}```



---

## 2020-09-24 20:45:40 - issues channel

**Kai**

[@UFTBRB3F1](@UFTBRB3F1) what are the latency values that you get? The t3 instances have far more CPU steal so they might not be the best choice for latency critical applications.

It shouldn't be 30 sec, but a few seconds might be caused just by CPU steal

---

## 2020-09-24 18:29:51 - issues channel

**Newbie99**

[@U013R0E7SUV](@U013R0E7SUV) are you using AWS by chance? I'm now getting the same error, with crazy latency times on a t3.mico, on a t2.micro running an older version no issues it seems (also locally no issues).

---

## 2020-09-24 13:58:01 - general channel

**agberk**

redis probably the easiest to set up, especially with python; if you have some very specific performance requirements you might want to consider zeromq but depending on what you care about most it may not really make a difference

---

## 2020-09-24 12:32:38 - issues channel

**Andrey Yunoshev**

```WARNING:flumine.baseflumine:High latency between current time and MarketBook publish time: 14.497617959976196

WARNING:flumine.baseflumine:High latency between current time and MarketBook publish time: 2.081183910369873

WARNING:flumine.baseflumine:High latency between current time and MarketBook publish time: 2.5980770587921143

WARNING:flumine.baseflumine:High latency between current time and MarketBook publish time: 6.860579967498779

WARNING:flumine.baseflumine:High latency between current time and MarketBook publish time: 2.2120819091796875

WARNING:flumine.baseflumine:High latency between current time and MarketBook publish time: 28.355962991714478

WARNING:flumine.baseflumine:High latency between current time and MarketBook publish time: 28.356460094451904```

---

## 2020-09-24 12:29:09 - issues channel

**liam**

The latency is increasing so it is probably the timeout 

---

## 2020-09-24 12:11:04 - issues channel

**Andrey Yunoshev**

Hi guys, I got distracted and then returned to the project, updated everything and get the latency warning all the time

Constantly increasing



Here is simple code



[https://gist.github.com/yunoshev/b4705edeea0fd5851657c1a86553f343](https://gist.github.com/yunoshev/b4705edeea0fd5851657c1a86553f343)



Here is INFO log



[https://gist.github.com/yunoshev/8f7b553365f9635eee37cc5d14dd1079](https://gist.github.com/yunoshev/8f7b553365f9635eee37cc5d14dd1079)





with small modification



```"High latency between current time and MarketBook publish time: " + str(latency),```



I miss something? :slightly_smiling_face: o_O?

---

## 2020-09-24 01:03:21 - general channel

**Taking Value**

Can I just check, is the base listener a lot faster than stream listener? I switched to the error handling code that [@UBS7QANF3](@UBS7QANF3) very kindly pointed me in the direction of. Its great but it uses the stream listener and it keeps flashing latency warnings at me. I am only using it for recording data at the moment so its not an issue but presumably it is an issue when its being used to place bets.

---

## 2020-09-22 03:30:39 - random channel

**Chris**

Second - for storage I have no idea what to get. AWS seems to define speed in IOPS, which I am researching now but haven't seen before. If I am recording all ticks + basic logging is 1k IOPS enough? (common consumer SSDs have ~50 to 100k). Is the default of 100 enough (similar to what a common HD has)?

---

## 2020-09-16 14:25:57 - issues channel

**jhaa**

I am trying to find the memory leak with tracemalloc from the std lib. I run coarse order and market stream for like 1500 markets. After a few hours the python process uses 900gb in ram. This is the tracemalloc output sorted by memory used :



/home/code/PycharmProjects/venv/lib/python3.8/site-packages/betfairlightweight/streaming/listener.py:105: size=16.6 MiB, count=274719, average=63 B

/home/code/PycharmProjects/venv/lib/python3.8/site-packages/betfairlightweight/streaming/cache.py:346: size=15.6 MiB, count=51110, average=320 B

/home/code/PycharmProjects/venv/lib/python3.8/site-packages/betfairlightweight/resources/bettingresources.py:651: size=10.7 MiB, count=55851, average=200 B

/home/code/PycharmProjects/venv/lib/python3.8/site-packages/betfairlightweight/streaming/cache.py:36: size=6651 KiB, count=63150, average=108 B



That does not add up to 900gb. What am I missing? Anybody has a best practice how to do this?

---

## 2020-09-14 17:58:02 - issues channel

**jhaa**

ok i just uninstalled ujson so it defaults to the slow python version

---

## 2020-09-13 13:29:29 - general channel

**Mo**

EC2: Elastic cloud compute. It lets you provision servers on demand. They can be Windows, Linux, with multiple distro options, or your own saved configuration. The hardware resources (CPUs and memory) can be as small or large as you like. There are specialist options for e.g. GPUs, FPGAs etc.



S3: Simple storage service. A way to store files for quick and easy access.



Lambda: lets you run serverless code e.g. a scraping process that runs hourly and saves some data to S3

---

## 2020-09-13 12:45:13 - general channel

**liam**

The speed of being able to develop / deploy in python is more important to me 

---

## 2020-09-13 12:25:10 - general channel

**Taking Value**

If speed is this crucial, is it not better to write all the code in a lowerlevel language rather than have a higher level abstraction such as python? Does the extra layer not add a significant time lag in code execution?

---

## 2020-09-12 10:49:47 - general channel

**PeterLe**

I think that anyone who is relying on speed as the major factor  in their strategy is on a long and tortuous road these days, especially if you are offering money to the market. (not to say that it hasn't worked in the past). There is no point being first to a party only to find that there is no one else to talk to....and just as you leave, someone else turns up. You could for example still get there first, but wait around a little longer..or any other combination

---

## 2020-09-11 21:24:48 - general channel

**Chris**

good point - not super worried but mine is bad now so I definitely have to buy server space somewhere.



I know if you are really trying to squeeze out performance you have to move to a compiled language like C++ and that's what most HFT firms use but do you have any idea how big of a difference it actually makes? For example, do you have stats on your average time difference between receiving a message and trading on that info? Is it &lt;10 ms or is it more in the neighborhood of 50 ms? I was assuming it was &lt; 10 ms but I am genuinely not sure

---

## 2020-09-11 19:11:55 - general channel

**liam**

So 7k isn’t going to help things, 15s, I doubt the snap function took that long, I assume you mean from the snap to actually processing the data?



This is a problem with using queues, you have a slow down due to an increase in updates that then clogs up your ram, you then max out your CPU in trying to clear the queue, the queue then starts to exponentially increase in size before the dreaded memory fault  

---

## 2020-09-11 09:44:15 - issues channel

**DH**

Wow, I'm seeing latencies of much more like 100ms here when I use `async=True` (as opposed to 120ms ish when using `async=False`), from a London-based VM. I'm using bflw though - is this an area where bflw is known to be slow? I can't see anything that could be responsible for adding so much latency!

---

## 2020-09-11 09:27:40 - strategies channel

**DH**

Yeah fair point. I can see the argument for restricting order types (especially given the way this has played out in US equities microstructure) albeit that I do prefer your definition of FOK to theirs, but the latency point seems little odd given that an API user by default will have the ability to interact at much lower latencies. Nonetheless, I guess applying a 10ms 'speed bump' equally across all users seems fair! Thanks for the extra context you provided elsewhere in the thread around exactly where the speed bump is applied, I hadn't been aware of that.

---

## 2020-09-06 10:44:06 - issues channel

**liam**

Using up to one gb is impressive, I have an issue open [https://github.com/liampauling/flumine/issues/248|https://github.com/liampauling/flumine/issues/248](https://github.com/liampauling/flumine/issues/248|https://github.com/liampauling/flumine/issues/248) I use a mixture of docker and a worker to log memory usage 

---

## 2020-09-06 00:37:52 - issues channel

**birchy**

Agree with [@U0128E7BEHW](@U0128E7BEHW). Python Memory Error triggers the OOM process killer on Linux systems. Usually happens if you're appending to a list/dict/etc but forgetting to remove old entries and/or limiting the size. For lists, it's simply a case of doing something like `mylist = mylist[-1000:]`

---

## 2020-08-29 11:19:43 - random channel

**Newbie99**

Just going back to your earlier point about the priority order queue, thinking about it, I think it does make sense then with regards to this masking issues such as above (i.e. slow code), what if there was another flag (like the high latency warning), that lets you know local processes aren't processing quickly enough?

---

## 2020-08-29 09:50:17 - random channel

**Misha**

[@UU1URJ8L8](@UU1URJ8L8) - speed isn't really helpful to "beat" others. The randomness of delays from the Betfair exchange server and across the stream (which needs only to be milliseconds) means that trying to be the fastest is useless. Good performance is more about the ability to process all updates in real time. I am moving into in-play tennis where there is a 3 or 5 second delay to actually place orders, and all the money disappears during the point so you need to wait for a few seconds after a point anyway for the volume to "arrive"

---

## 2020-08-29 09:40:14 - random channel

**Remi**

I have chosen to not play the speed game at all (for now). I am coming at it more from a math/machine learning angle. Volume is a big problem for me but when I get matched it is very reliably profitable. I have tried updating orders faster but I find that it can quickly turn into a race to the centre of the spread.

---

## 2020-08-28 21:48:46 - random channel

**birchy**

[@U4H19D1D2](@U4H19D1D2) just read your comment above regarding "slow" code... what's the recommended way to implement strategies that do a lot of number crunching/processing? The problem I can foresee is that by the time the calculation process is completed, the market may have updated several times, thus making any calculation results obsolete.

---

## 2020-08-28 16:52:54 - random channel

**Unknown**

[@U4H19D1D2](@U4H19D1D2), with regards to the pending orders that disappear saga, I've attached a log from the 16:40 today (Curragh- WIN market), now interestingly when the market suspends at the end the pending orders (placed approx 2 mins before the scheduled start) all fail (which looks to be correct as the market is suspended)....but the bigger question is, why did they sit in pending for the entire race, I can't work it out from the logs tbh, but hopefully you might spot something I've missed which may shed some light on it (I didn't receive any high latency warnings, but then given the timeframe, I don't think it can be a pure latency issue anyway)?

---

## 2020-08-27 18:40:01 - random channel

**Newbie99**

Just after this I got a high latency warning btw, maybe unrelated of course

---

## 2020-08-27 17:22:45 - random channel

**Newbie99**

(and latency could explain why its only happening to me, perhaps a connection / machine issue...although I've tried on AWS and have replicated so I guess its not that).



Okay cool, will try that and report back...

---

## 2020-08-27 17:20:30 - random channel

**Newbie99**

It seems random, but I've had markets where it hasn't placed a single order (but I can see them going into pending). Is there any timing issue, where it could somehow kick them out without warning if the latency got to high?

---

## 2020-08-25 22:53:58 - random channel

**birchy**

All this talk of gps issues makes me wonder if it's actually reliable enough to be used for triggering bets? In particular, this is concerning:



`How accurate is the live data?

Accuracy is recorded as the difference between the official finish time and the GPS derived finish time, 

the BHA defined conversion between time and length varies by ground and code between 4 and 6 

lengths per second, taking speed = 5.5ls-1 and L=2.4m, and a standard deviation of a sample of the 

data measured as 100ms, then 95% of the live data is within 2.59m of the true position.`



...considering that there are often multiple runners within a 2.59m section. I would imagine GPS could easily be reporting positions in the wrong order? And that's only 95% of the time. The other 5% must be a monumental fuckup, particularly where all the runners are tightly bunched?

---

## 2020-08-20 10:41:11 - general channel

**D C**

I agree regarding the speed and complexity. Look at something like Hawkeye to capture motion of cricket ball which is a VERY simple problem by comparison. You basically just need to fit an ellipse to the outputs of some edge detection. Cameras positioned accurately to optimise that. Not sure if they do that in real time or just run it after the ball has been delivered. Imagine a foggy February day over the fences trying to use image recognition in a 20 strong field. Really can't see it being feasible.

---

## 2020-08-18 20:08:14 - random channel

**Newbie99**

Using flumine (live), when an order goes into a pending state and then the "message": "1 order packages created" appears in the next line as expected. Sometimes the orders never actually make it onto the order book. Given the orders weren't in any violation of the controls and there don't appear to be any API issues, does this mean there is some kind of latency logic built in (i.e. if the order book receives the order x seconds after it was sent it automatically fails or something along those lines)?

---

## 2020-08-18 10:40:10 - random channel

**Jonjonjon**

For anyone with a 3950x chip, what sort of CPU temps and clockspeeds do you get when running Flumine with the multiprocessing module?



I'm getting CPU temps of around 61C this morning, and clockspeeds of just over 3.8GHz.

---

## 2020-08-16 18:19:58 - general channel

**Lee**

so based on that the PLACE_LATENCY to match in backtesting would be 0.139 (if i was being pedantic)

---

## 2020-08-16 18:14:16 - general channel

**Lee**

Out of interest, what does elapsed_time include and does the following time seem slow?

```{

	"message": "execute_place",

	"trading_function": "place",

	"elapsed_time": 1.1396217346191406

}```

I mainly ask because a few of my offered prices did not match in live and if I increase `PLACE_LATENCY`  in simulatedexecution.py it seems to match live more accurately.

---

## 2020-08-13 12:23:21 - issues channel

**Remi**

A few weeks ago I made a script to go through the account statements to evaluate performance for different markets etc. This is the call I am making:

```account_statement = Trading.account.get_account_statement(item_date_range=time_range(from_=from_date, to=to_date),

                                                                      from_record=from_counter)```

---

## 2020-08-07 12:04:35 - strategies channel

**PeterLe**

Sorry just another question..do you pay for the subscription for the feed on a meeting by meeting basis from Toal Performance data, or is the feed direct from Betfair? ([@UUE6E1LA1](@UUE6E1LA1) I like less complex least advanced :grinning:

---

## 2020-08-06 20:23:08 - issues channel

**Josh**

I tried deserializing all of the market catalogues and market books from a session where I saw a segfault that I had managed to write to disk and I couldn't reproduce it. I'm guessing the source must have been a call within bflw and the raw data that caused it was lost while still in memory.

---

## 2020-08-06 11:27:48 - general channel

**Twatter**

I haven't used docker myself, but wouldn't that just make it easy to deploy a working bot? i.e. if you've already got it running on a server, and it's a bot/strategy that won't benefit from deploying the same code to a 2nd/3rd server etc, then I would have thought that containerising your code and deployment into docker would only help with speed of deployment and speed of recovery if the server fell over?

---

## 2020-08-06 08:20:42 - general channel

**Misha**

Architecturally it's fairly simple to explain. Two parts, a monitor and a trader. The monitor basically just monitors whatever I need (Betfair, other exchanges, tennis APIs, etc) and through a pipeline of "micro-services" pushes data into a database which is exported as a tree of JSON files with URL links accessible via simple HTTP requests. The trader takes this market information, streaming info, other price info, scores, and converts all of them to push feeds, aggregated and matched, so everything runs via object references in memory. The trader doesn't access a database

---

## 2020-08-03 08:42:12 - general channel

**Mo**

And yeah avoiding the SSL handshake is critical if you care about latency 

---

## 2020-08-03 08:40:07 - general channel

**liam**

in regards to your setup do you close anything older than 3 and create new? Do you then take the hit on the first round trip or prime it first? (in regards to latency sensitive requests such as place/cancel requests)

---

## 2020-08-03 08:33:30 - general channel

**liam**

Got a link? I have this [https://docs.developer.betfair.com/display/1smk3cen4v3lu3yomq5qye0ni/Optimizing+API+Application+Performance](https://docs.developer.betfair.com/display/1smk3cen4v3lu3yomq5qye0ni/Optimizing+API+Application+Performance)

---

## 2020-08-02 12:29:40 - strategies channel

**Michael**

I think it depends how you do it. Your bets have an effect on the market and if your two strategies are similar then they'll be competing with each-other, so if you're effectively running two bots simultaneously then you'll confuse things (at best). Depending on how you're operating it'd be better to make sure that only one version is executing at a time. If you're trying to optimise prices with a fixed trigger then that's easy and you can do a very simple a v b, if you're trying to optimise a trigger then you can't. In that case I'd either run them on separate markets or (more often) just measure the relative performance of each strategy looking deeply at the various metrics and comparing both data sets to the hypothetical performance of a fixed strategy that shows how promising the markets were but doesn't place any bets at all.

---

## 2020-08-01 09:43:06 - random channel

**Disco**

I have this version too, will check it later. Since updating, I've been having problems with color scheme applying very slowly, and real time code check/suggestions being slow too (while cpu load is normal. Didn't have it in preview versions, seems like a bug)

---

## 2020-07-28 17:56:24 - issues channel

**mlpanda**

Hey again, I was wondering if you know how to get the aggregate liability on a specific selectionid? It is a bit slow to fetch all trades and sum up the matched amount when the number of trades grow quite fast (testing some market making). Is there any endpoint for that?

---

## 2020-07-27 15:18:28 - general channel

**Twatter**

Quick question - I'm slowly getting to grips with Betfairlightweight, and figuring out how to use Flumine, and looking at the BaseStrategy class, does this work on one market book at a time? e.g. process_market_book(self, market, market_book) - would I have to overwrite the BaseStrategy class if I wanted to get it working with two separate markets as an input ?

---

## 2020-07-27 11:46:45 - strategies channel

**Mo**

I don't use Python for latency sensitive strategies. And yes, I know my way around the OpenSSL source code :wink:

---

## 2020-07-27 11:45:25 - strategies channel

**D C**

I would like to avoid busy loops that is for sure. My background is mostly C++ stuff in comms for hardware (stuff like CAN and serial port connections) so when it comes to socket coding I try to stick to blocking socket stuff within a designated thread and thread safe queues to read/write. I am sure there are far better ways, but for HTTPS stuff and python users I imagine you are using higher level packages rather than some low level stuff using OpenSSL libraries. I was just wondering what kind of analysis you guys had done on latency. I am moving to this headless deployment on designated server (not sure yet probably AWS) but these things take time when you are essentially migrating to a new language.

---

## 2020-07-27 11:39:35 - strategies channel

**D C**

And to get the lowest latency do you need to assign applications to specific cores/processors or can you get the same results using max (min) nice level or similar?

---

## 2020-07-27 11:36:52 - strategies channel

**Mo**

To answer your question, yes I've studied latency a lot

---

## 2020-07-27 11:32:16 - strategies channel

**D C**

With all this talk of milliseconds and latency, has anyone done a study of this in detail? I mean you will surely get different results due to thread/process scheduling times unless you are running things such that you have a process single connection using a blocking socket connection configured such that the process runs on a specific processor? I mean I know that people have multiple processors and cores etc but everything is subject to OS scheduling. I mean yesterday I was getting over 100ms delays (close to 200ms at one point) on the GPS feed as calculated from the FEED time (not the 'pt'). I had Firefox running too and once I closed that down the delay dropped to a steady 70ms. I imagine that some of the people here making larger profits are running setups that have minimal lag. Anyone looked at this kind of thing in depth, or can point out any flaw in my thinking on this matter?

---

## 2020-07-27 11:04:02 - general channel

**liam**

happy to add it to the listener via bflw as long as it doesn't slow things down (too much), BSP offload would be up to the user wouldn't want to default that behaviour

---

## 2020-07-27 10:48:52 - general channel

**Oliver Varney**

I was thinking that the order status would still be in pending right ? so even if orders have been sent and they are having latency issues, as long is a check against the order.status then no orders / hedges will be refired

---

## 2020-07-26 15:00:10 - strategies channel

**birchy**

Very true. I like to optimise my find bet -&gt; place bet turnaround time, but 12ms is the same as my current Tagadab VPS so I've not lost anything performance-wise moving to AWS.

---

## 2020-07-26 09:29:00 - strategies channel

**SrFabio**

Cool that makes sense! Thanks for the insight that's really useful. I think sub account is probably overkill for now as the customerStrategyRef should cater for it + some internal logic to build performance metrics which I already have

---

## 2020-07-26 09:15:16 - strategies channel

**Dave**

Yeah sorry I wasn't clear - if you have all the underlying bets grouped by strategy then you can do whatever aggregation you want (e.g. performance over time). Given Betfair's pnl tracking at account level is pretty basic you might as well do it yourself anyway, for which customerStrategyRef is totally sufficient to look at performance by strategy at whatever granularity/aggregation level IMO. Besides, betfairs orders only persist for 90 days so you ought to write em to a file anyway, at which point self-aggr is the way to go. Same advantages of the field apply to bankroll management, e.g. computing your exposure and whatnot.

---

## 2020-07-26 09:09:47 - strategies channel

**Michael**

I think [@U013Z24LD0U](@U013Z24LD0U) is thinking about how to track the absolute performance of a strategy over time rather than the individual bets so that he can scale automatically according to performance (or something like that). For that he needs to keep some sort of overall record and write it out to a file.

---

## 2020-07-23 12:50:38 - issues channel

**liam**

[@U013R0E7SUV](@U013R0E7SUV) you must have some sort of memory leak, without seeing the code it will be hard to debug but bflw streaming code shoudln't be the cause

---

## 2020-07-23 12:31:46 - issues channel

**Andrey Yunoshev**

I always (around each 10 min) have warning "latency high", at home and at ec2 Ireland also. Its is normal?

---

## 2020-07-23 11:31:27 - general channel

**Misha**

A quick question on API access: There is a REST endpoint and an RPC endpoint. Where there is both, the requests and responses are identical. There are some calls (the scores endpoint) that are only on the RPC endpoint. Is there any difference in performance or reliability? Is it possible for one to be up and the other down during a partial outage? I have always used the REST endpoint but have recently updated code to switch between either because I will be using the scores endpoint at some stage

---

## 2020-07-22 20:08:28 - strategies channel

**birchy**

oh... I must of been lucky then, as I've not had any noticeable issues other than regular connection errors, but I've always assumed that was a betfair issue rather than Tagadab? What's the latency like on EC2?

---

## 2020-07-22 19:35:20 - strategies channel

**birchy**

So yes...and no. lol

[@U4H19D1D2](@U4H19D1D2) are you running your bots on EC2? I've been using Tagadab (now SimplyHosting) VPS for years as it had low latency to the bf servers.

---

## 2020-07-22 19:21:44 - strategies channel

**liam**

I download as I process, run everything on ec2 or lambda so latency is low anyway 

---

## 2020-07-22 19:17:24 - strategies channel

**birchy**

Quick backtesting question....if your market data is stored on S3, are you downloading it to the local machine first to avoid latency issues?

---

## 2020-07-22 13:12:49 - general channel

**Mo**

[http://www.totalperformancedata.com/|http://www.totalperformancedata.com/](http://www.totalperformancedata.com/|http://www.totalperformancedata.com/) is the original source but Betfair have a limited number of licenses they give out

---

## 2020-07-20 20:27:27 - general channel

**Twatter**

Hi All.. Stumbled upon the betfairlightweight library recently, and so just starting out trying to write my own Betfair bot. Slowly trawling through the history of these slack channels to pick up some info. Quick Q - I got an idea for a strategy that involves intra market trading across a horse races Win/EW/Place(s) markets. I'm confused as to whether I should be coding it with Flumine, or Betfairlightweight? What's the guide on choosing Flumine or just rely on betfairlight?

---

## 2020-07-19 14:20:52 - general channel

**liam**

Used to have separate but slowly moving to a single app via [https://github.com/liampauling/flumine|flumine](https://github.com/liampauling/flumine|flumine) 

---

## 2020-07-14 11:04:18 - issues channel

**liam**

_While we have snapshots disabled (for performance reasons), this will happen whenever we do a release or restart. This is a defect that we have listed to fix at a future date._



_In the meantime, the dev team will look at an alternative solution e.g. excluding closed markets from the initial image._

---

## 2020-07-13 13:10:28 - general channel

**Evaldas**

Hi,

Does anyone know someone on betfair, that could help to speed up reopening of my closed account?



Not doing anything against rules here, but my account got closed on Thursday, left me with 3k+ of exposure that day, funds now suspended, no explanation, no warnings, and didn't get a single replay to emails since Thursday..

Helpdesk explained that I need to provide proof of funding, which is laughable as I'm fulltime bf trader and was about to became PC2 payer this month. I did withdraw all my funds during quarantine, and then slowly deposited it back, which is I guess what triggered closure. But I'm being ignored now, and no idea what to do.. Already sent all my statements, showing deposits to betfair, cards photos etc..

---

## 2020-07-08 18:07:39 - general channel

**birchy**

[@UQL0QDEKA](@UQL0QDEKA) Interesting that you mentioned your main profits were in the period 2011-2013, because I experienced exactly the same thing! I was averaging £3K a month profit for about 15 months in 2011/2012 from a single £2 strategy that was basically placing Lay bets at silly prices on low liquidity markets. I did once lose around £600 in a space of 2 hours (at £2 a bet!) and it turned out that someone had worked out how to exploit my strategy on Aussie greyhound races at 4am when everyone else, including myself, was fast asleep. Soon patched that up and continued to profit for several months after, but then the bot slowly started to decline and I pulled the plug when my P&amp;L graph started to flat-line. Using a graph to plot the P&amp;L showed a definite change in the markets. Tried lots of fine-tuning, etc but never got back to that golden period. Betfair launched the Sportsbook in 2012, so I can only assume that the "mugs" I was profiting from were attracted by the Lucky 15's, 6-fold accumulators, etc.



Regarding the £2 thing, I've found that 5x £2 bets are more likely to get matched than one £10 bet. Doesn't make much sense because £10 is a tiny drop in the ocean, although it may just be a psychological thing and in fact £10 is £10, whether it be in one lump or 5 parts...

---

## 2020-07-07 19:52:58 - general channel

**Mo**

It sounds like you might be conflating the term mining data with scraping, in which case your comments on throttled speed are irrelevant with streaming because there is no polling involved

---

## 2020-07-07 19:48:03 - general channel

**birchy**

Hi all,

I'm new to bflw/flumine but not new to betfair api/python. Have been running bots since around 2004 - back then I had VB6 and a carefully crafted web scraper. Here in 2020, and after using my own library ([http://BespokeBots.com|BespokeBots.com](http://BespokeBots.com|BespokeBots.com)) for many years, I've decided it's time to get to grips with this new-fangled streaming API malarkey. Was going to code my own library but there is no good reason for me to do so when [@U4H19D1D2](@U4H19D1D2) has already created this marvellous resource. I'm on a bit of a learning curve at present because Liam has written "modern" Python code, whereas mine is very old fashioned and only uses very basic implementations. Having said that, my simple library has served me well for many years and has more than paid for itself.



Moving forward, I've run a couple of the bflw/flumine examples (copy/paste code!) and have login/etc working as expected. Planning on mining some data initially to get familiar with the syntax, pitfalls, etc. Can anyone suggest the best way to go about mining data with this library? Also of interest, what format is required for backtesting?



Regarding data mining, has anyone considered combining data as a pooled group? i.e. if "N" people were all mining data, the combined efforts would help to eliminate those "missing" sections that we encounter when we lose connection. Also, if we were mining ALL available markets at a sensibly throttled speed, the combined data would achieve a much better granularity, simulating something close to what we would get if we were concentrating on specific markets at balls-out speeds. This would require a pre-agreed structure, but is easily solved if all members use the same framework. Is this do-able, or does it contravene some clause in Betfair's T&amp;C's?

---

## 2020-07-05 14:35:49 - general channel

**Mo**

Ah that piece of information came from the GitHub repo README: [https://github.com/TotalPerformanceData/gmaxfeed](https://github.com/TotalPerformanceData/gmaxfeed)



&gt; Whip strikes can cause sudden spikes in the data, velocities hitting near 50m/s and skewing the X,Y way off the track, there's nothing we can do about this as the trackers are padded as much as the weight/size guidelines will allow.

---

## 2020-07-05 12:01:01 - strategies channel

**Sandy Caskie**

So I have streamed horse racing data saved this and used this to build a predictive price model. My streamed data is not of a super high latency though. I will have to look in more detail the reason for this though it seems pretty accurate on a first glance. My question relates to historical data. I also built a predictive model using the free package but this was pretty useless with a frequency of per minute. For anyone else who has done something similar was the pro data particularly useful for building a predictive model?

---

## 2020-06-28 19:45:43 - general channel

**Jorge**

Hey guys, does anyone know what is /usr/bin/fail2ban-server ?? I had problems with Python scripts using a lot of RAM memory and I have found out it is actually because of some executions of this....

---

## 2020-06-28 13:01:53 - general channel

**fjt1973**

So this is my handler, very basic to return the balalce of my account.



def lambda_handler(event, context):

    # TODO implement

    trading = betfairlightweight.APIClient(username=my_username,

                                       password=my_password,

                                       app_key=my_app_key,

                                       certs=certs_path)



    trading.login()

    account_funds = trading.account.get_account_funds()

    balance = account_funds.available_to_bet_balance

    return balance

    #return {

    #    'statusCode': 200,

    #    'body': json.dumps('Hello from Lambda!')

    #}



And this is the execution results



Response:

{

  "errorMessage": "None \nParams: None \nException: join() argument must be str or bytes, not 'tuple'",

  "errorType": "APIError",

  "stackTrace": [

    "  File \"/var/task/lambda_function.py\", line 33, in lambda_handler\n    trading.login()\n",

    "  File \"/opt/python/lib/python3.7/site-packages/betfairlightweight/endpoints/login.py\", line 31, in __call__\n    self.url, session=session\n",

    "  File \"/opt/python/lib/python3.7/site-packages/betfairlightweight/endpoints/login.py\", line 53, in request\n    raise APIError(None, exception=e)\n"

  ]

}



Request ID:

"f4b6780c-fb3a-485f-881d-3fc75f1cfddd"



Function Logs:

START RequestId: f4b6780c-fb3a-485f-881d-3fc75f1cfddd Version: $LATEST

[ERROR] APIError: None

Params: None

Exception: join() argument must be str or bytes, not 'tuple'

Traceback (most recent call last):

  File "/var/task/lambda_function.py", line 33, in lambda_handler

    trading.login()

  File "/opt/python/lib/python3.7/site-packages/betfairlightweight/endpoints/login.py", line 31, in __call__

    self.url, session=session

  File "/opt/python/lib/python3.7/site-packages/betfairlightweight/endpoints/login.py", line 53, in request

    raise APIError(None, exception=e)

END RequestId: f4b6780c-fb3a-485f-881d-3fc75f1cfddd

REPORT RequestId: f4b6780c-fb3a-485f-881d-3fc75f1cfddd	Duration: 19.17 ms	Billed Duration: 100 ms	Memory Size: 128 MB	Max Memory Used: 85 MB	Init Duration: 782.62 ms

---

## 2020-06-27 16:52:35 - general channel

**Mo**

But this is where it comes from: [http://www.totalperformancedata.com](http://www.totalperformancedata.com)

---

## 2020-06-22 15:39:48 - general channel

**Evaldas**

maybe it's just the way python reserves memory. I run mine non-stop, and it gains 200-300MBs over 2weeks

---

## 2020-06-22 15:29:46 - general channel

**Evaldas**

Hi,

If I have 2-3k markets in market/order stream cache, could that take significant amount of memory in bflw?

And if so, is there a way to clean that cache on market close?

---

## 2020-06-19 08:08:11 - strategies channel

**SrFabio**

[@U013MLED3V1](@U013MLED3V1) That's a very good point, I don't think even the betfair cashout does that optimization (for the correct score example) and it's certainly way too much work for me to do it at this point and feels beyond the scope of the app. What I'll do is simply remove the individual selection cashouts that would make the overall market PL worst, and still thinking about the option of not using the best price, but the 3rd best price for the calculations as a way to avoid orders not being matched (since they will be matched at the best price available anyway)

---

## 2020-06-17 21:26:11 - random channel

**JonJonJon**

I've had a doodle with it. Hard to say if it improves performance or not directly, as we can't change live orders to a set, and leave it as that. We have to hack this bit too:



```# process current orders

blotter = market.blotter

completed = set()

for order in blotter.live_orders:

    process.process_current_order(order)

    if order.trade.status.value == "Complete":

        #blotter.complete_order(order)

        completed.add(order)

blotter._live_orders = blotter._live_orders - completed```

The above change is obviously not suitable for production as we are modifying the private variable. But I just did it as a quick hack to make things work for testing.



Given variable run times. It might or might not shave 0.2-0.4 seconds off my backtest which, takes around 12.5 seconds to run. But there is variability, so it is impossible to say for sure.



However, using sets expresses the intent of the code clearer, as there should be no duplicates in "live orders", and they should be unordered.



Perhaps we should just leave this for now, but be aware of it anyone reports bottlenecks in this part of the code. I think using sets is more likely to be better if a user has hundreds of live orders at once. I think that is unlikely. But I could be wrong!

---

## 2020-06-17 15:30:55 - random channel

**Mo**

In most applications the RAM speed is not that important, I think latency is an equally important consideration

---

## 2020-06-17 08:34:17 - random channel

**SrFabio**

Current AMD cpus are far better especially when it comes to price/performance

---

## 2020-06-15 16:24:39 - issues channel

**Peter**

[@U010GM77S4W](@U010GM77S4W) An extra tip when setting up new instances. At the top of the list that AWS will offer you are the t2 series, but scroll down to the t3s - they're better and cheaper. E.g. Your t2.micro in London is $0.0132 ph, but the t3.micro is only $0.0118 ph. Moreover your t2 has a single cpu, the t3 has two (memory is the same 1GB for both).

---

## 2020-06-15 14:42:43 - random channel

**liam**

it would be a daemon similar to this [https://github.com/liampauling/betfair/blob/master/examples/examplestreamingerrhandling.py|example](https://github.com/liampauling/betfair/blob/master/examples/examplestreamingerrhandling.py|example) but set the queue to None as you don't need it (leaving it would cause a memory leak in your use case as it would fill)

---

## 2020-06-15 14:25:11 - random channel

**Chris**

A naive question as I'm only really dipping in and out of using bflw when needed, and not really a developer, but I've got a setup where I'm basically only ever grabbing prices from BFEX, and storing/comparing them with input i am providing from scraping other sites or manually, right now I generate a list of markets, and store the current available back/lay price, I'm only ever really interested in that price, currently that runs over a series of (now fairly slow) loops for the events and markets i'm interested in, I'd like to be able to expand that list of markets/events but this then makes some of the data at the beginning of my loops quite old by the time it's gone through the rest of the markets i'm interested and stored those (in a MySQL database), I think the right answer is to use Flumine, but I just wanted to see if anyone else does similar and how they handle it, in terms of getting the data back out for "current price", as I'd always been storing it in a db that was easy but i'm not sure if it's feasible with the rate that the data comes into flumine whether to then store that in a db to be able to use with my comparisons, hope that makes sense

---

## 2020-06-15 14:22:32 - issues channel

**mandelbot**

Happened again, one python this time

`{"asctime": "2020-06-15 13:19:45,614", "levelname": "ERROR", "message": "DataStream run error", "exc_info": "Traceback (most recent call last):\n  File \"C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages\\betfairlightweight\\streaming\\betfairstream.py\", line 220, in _receive_all\n    part = self._socket.recv(self.buffer_size)\n  File \"C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\lib\\ssl.py\", line 1226, in recv\n    return self.read(buflen)\n  File \"C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\lib\\ssl.py\", line 1101, in read\n    return self._sslobj.read(len)\nConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host\n\nDuring handling of the above exception, another exception occurred:\n\nTraceback (most recent call last):\n  File \"C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages\\flumine\\streams\\datastream.py\", line 113, in run\n    self._stream.start()\n  File \"C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages\\betfairlightweight\\streaming\\betfairstream.py\", line 59, in start\n    self._read_loop()\n  File \"C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages\\betfairlightweight\\streaming\\betfairstream.py\", line 202, in _read_loop\n    received_data_raw = self._receive_all()\n  File \"C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages\\betfairlightweight\\streaming\\betfairstream.py\", line 224, in _receive_all\n    raise SocketError(\"[Connect: %s]: Socket %s\" % (self._unique_id, e))\nbetfairlightweight.exceptions.SocketError: [Connect: 3002]: Socket [WinError 10054] An existing connection was forcibly closed by the remote host"}`

`{"asctime": "2020-06-15 13:19:45,614", "levelname": "WARNING", "message": "[Stream: 1001]: Latency high: 302.40696835517883"}`

---

## 2020-06-15 14:12:20 - issues channel

**mandelbot**

Just put them all into one python and got a bunch of latency warnings again

---

## 2020-06-15 14:02:20 - issues channel

**mandelbot**

I noticed one of them wasn't reporting any logs, so when I hit return it dumped a bunch of latency errors

---

## 2020-06-15 14:00:41 - issues channel

**mandelbot**

no latency errors and recording markets

---

## 2020-06-15 13:27:30 - issues channel

**mandelbot**

I keep getting latency warnings when I run the marketrecorder (even though other instances are fine). I am running on an AWS EC2. Any ideas why? Is it because im running a few instances?

`{"asctime": "2020-06-15 12:20:13,784", "levelname": "WARNING", "message": "[Stream: 1001]: Latency high: 2465.7244164943695"}`

that instance gets jammed up and continues only after hitting return

---

## 2020-06-13 08:32:30 - random channel

**liam**

I use 1c but that is just because what I started with and have never bothered to move, I think London is more expensive but some have said the latency is now better but I would worry to start off with 

---

## 2020-06-12 20:21:53 - random channel

**JonJonJon**

It's related to how Python works. Under the hood, doing a set difference is probably doing some C-level fast code.



If we do something like [x for x in blotter where x.status=='EXECUTABLE'], it has to go through slow Python code every time it looks at x.status.

---

## 2020-06-12 17:04:23 - random channel

**Dave**

One possible solution might be to write a CSV in memory and compress it (gzip) prior to writing to disc (and you can use `zcat` to access the data via the terminal). I think numpy even has a function that can save the array directly as a zipped file but not sure if it transforms it to some prop format before zipping it (rather than -&gt; CSV &gt; zip).

---

## 2020-06-12 11:39:38 - strategies channel

**Dave**

[@UGV299K6H](@UGV299K6H) - indeed, you pretty much hit the nail on the head there. If you want to be putting through decent volume then you most definitely need to look at market impact. The only optimization I've made is to bet over a longer time period rather than go in with a large swipe.

---

## 2020-06-11 11:29:27 - strategies channel

**James T**

Thanks for the tip, [@U4H19D1D2](@U4H19D1D2). I’m initially talking about Take for now, but eventually Offer as well. I do already measure amounts matched and performance against SP. I find that days are too variable to be comparable though. Even if I don’t change anything figures vary a lot between days. I do trade from early morning. So to get a feel I’d need a sample over a long period. But then over a long period lots of other things change - weather, competitors, race types... 



Then split testing doesn’t really work because the algos will just compete?

---

## 2020-06-11 07:42:11 - random channel

**Mo**

Yeah the RAM is fine. The only problem I had was that the BIOS defaulted to much lower clock speed and timings than it was rated for. I only discovered this when I started to dig into my Monero mining hashrate :wink:

---

## 2020-06-10 21:01:48 - random channel

**liam**

Yes that bit is unnecessary once initialised but only for backtesting, a question of reducing readability for performance 

---

## 2020-06-10 20:51:58 - random channel

**JonJonJon**

I don't think it's the bit I fixed. This comes after. I think it's because it gets called so many times.



My profiler is not providing any details worth sharing.



As a baseline, after my prior changes, it takes 32s for the backtest, cumtime 4.5s for size_matched.



If I change the code to the below, then it becomes 28 seconds for the backtest, cumtime 1.1s for size_matched ( I know the numbers don't quite add up, but I'm also using my PC to play some music off youtube which might affect things)

```@property

def size_matched(self) -&gt; float:

    return self.simulated.size_matched or 0.0```

So it could be because the original size_matched calls current_order, which has the "if" statement to return self.simulated:



```    @property

    def current_order(self) -&gt; Union[CurrentOrder, Simulated]:

        if self.simulated:

            return self.simulated

        elif self.responses.current_order:

            return self.responses.current_order

        elif self.responses.place_response:

            return self.responses.place_response```

Perhaps the use of the @property is slow?



But the repeated test of "if self.simulated" is unnecessary, especially when it essentially comes down to a test of whether or not config.simulated is True or False.

---

## 2020-06-10 16:31:27 - general channel

**jhaa**

Which one gives me the latency waarning?

---

## 2020-06-10 16:30:57 - general channel

**jhaa**

06/10 16:30:50 [Stream: 1]: Latency high: 0.6275410652160645

---

## 2020-06-08 10:30:42 - strategies channel

**Remi**

So I finally got a live key activated a few days ago (thank you [@U4H19D1D2](@U4H19D1D2)!) and the first results look good though this is just a single weekend. Mean is around 7 cents per trade (a single trade can be multiple orders/markets for this strategie), value at risk on that 7ct is low but sometimes I do have small negative returns, and I calculated the probability that the mean is higher than 0 with a one-sided T-test and that came out very close to 1. I feel pretty confident this thing is working (for now). 



I have a few questions though. 



1. Do you optimize order size for rounding+commission? Sometimes you can get one extra cent for free because of rounding. Is this a micro optimization or worth some effort?

2. I don’t mean to be impolite but, do you see markets being manipulated? E.g. in more regulated markets you are not allowed to match your own orders but on Betfair you can (I don’t know if it is allowed on bf). I don’t plan on doing this but I’d like to know better what I am dealing with.

3. What are some strategies to lower the commission? Right now I have 0% commission discount and my Betfair Points isn’t growing.



---

## 2020-06-07 01:14:41 - general channel

**Ruben**

I agree that this is a much better way to measure latency

---

## 2020-06-06 19:44:03 - general channel

**liam**

And if you want to measure your latency you should be comparing the time to `MarketBook.publish_time`

---

## 2020-06-06 17:21:18 - general channel

**Jonatan (skyw)**

Yeah, that's the latency I'm referring to :)

---

## 2020-06-06 17:17:52 - general channel

**Jonatan (skyw)**

Try just printing market Id  and see what latency you get.

---

## 2020-06-06 14:49:13 - random channel

**Jonatan (skyw)**

Ill add to this slow saturday discussion, I do not think point 3 is the real benefit, the real benefit comes from readability and that it makes it easier to type check arguments as well doing validation.



Something that bflw actually missing a.t.m. : )

---

## 2020-06-06 11:50:30 - random channel

**liam**

For back bets the liability is technically the size but for lays you can only select the liability. This is to prevent you setting a size of x and the BSP being calculated at 1000 or similar (due to error / slow start from the suspend guy) you would therefore have a massive exposure (something betfair couldn’t calculate before BSP is reconciled)

---

## 2020-06-05 14:06:49 - issues channel

**Dave Simonds**

Yeah I’ve had a few back and forwards with Neil (assuming you mean the guys on their helpdesk)… he seems a good guy… i think he’s probably fed up of me hounding him over this.



I certainly wouldn’t say I’m spamming, betfair publish a market and I place my bets fast, in the event of a failure I retry, speed is imperative for many strategies (from what i can gather).



Private APIs? …. never heard of them, keen to learn tho!!! what are they for?

---

## 2020-06-02 23:20:45 - random channel

**Dave**

If useful, ping roundtrip is 18ms from the London DO datacentre. I think Mo mentioned the path is asymmetric though, I've never really tried to measure the outbound latency.

---

## 2020-06-02 14:11:19 - general channel

**Andrey Yunoshev**

&gt;flumine seems to be getting some users



this is a lot of work, and most importantly is done by a person who understands the subject

I, as usual, wrote the parser myself, and then I caught bugs - and then I decided to google it :)



in general, at the moment, it bothers me a little that everything is slow - it takes 2-3 hours to process a month of greyhounds records

on the other hand, it's almost 10 gigabytes of data :)



I have a couple more questions - you can somehow immediately get the name of the runners?

currently, I call client.betting_client.betting.list_market_catalogue in check_market_book



And second, for backtesting, I do not receive any market with CLOSED status - for getting WIN/LOSE runners status - but need dig more, possible my bug

---

## 2020-06-02 10:30:03 - general channel

**liam**

yes it uses OrderPackages, so you may have orders from [https://github.com/liampauling/flumine/blob/master/flumine/baseflumine.py#L130|multiple strategies](https://github.com/liampauling/flumine/blob/master/flumine/baseflumine.py#L130|multiple strategies) being sent at once to try and reduce latency and load, in that code you can see the strategies being processed and then `process_market_orders` being called which handles the pending orders

---

## 2020-06-01 12:11:09 - random channel

**Jonatan (skyw)**

[@UBS7QANF3](@UBS7QANF3) I've used vs code for python, I did not like the experience. For me everything is just not as good.

• Visuals, easier to navigate project explorer, notice errors in code

• Easier to refactor code

• Less buggy, Microsoft Language  Server just felt buggy and slow overall

• A lot better auto imports

---

## 2020-05-31 20:17:12 - issues channel

**Remi**

&gt;  I can see the price and size (see image) , but when I run it in BFLW I can only see “object at 0x0000018286D26108” for example. Is this a location in memory where the EX_BEST_OFFERS values are stored?

&gt; if so, how do you access those values via python?

Yes, that is just the address to the PriceSize object. PriceSize does not implement __str__ method so if you print it it doesn’t get converted to a pretty string representation. If you want to see price and size you need to print price_size.price and price_size.size. The visualizer shows it as json which is ‘just’ text and not a python object.

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

## 2020-05-31 03:35:16 - general channel

**Steve**

I've been having a bit of an issue with latency and I'm trying to figure out what benchmark latency I should be striving for. What is the optimal time I could expect for a strategy to be able to register a change in the orderbook, process the change and have a new order posted back into the orderbook? So essentially, if I'm responding to change in the BF orderbook what latency should I expect between that change being made and my new order being placed in the orderbook?

---

## 2020-05-27 15:53:54 - general channel

**brightcake**

quick pycharm question: has anyone ever had 'waiting for REPL response' in pycharm? Seems to be really slowing down code that shouldn't be slow

---

## 2020-05-25 12:30:12 - strategies channel

**James T**

I trade order flow on racing, but am actively trying to move to a more fundamental based approach. Order flow techniques tend to be lower margin and less scalable but can be very consistent, but will soon have issues with transaction limits (number of bets you can place and cancel as you move with the price). 



And on fundamentals it’s sort of flipped. You’d aim for bigger margins, fewer bets, but end up with bigger volatility in returns. 



I suppose it’s looking like I might end up somewhere in between that actually. But I won’t know until I finish my project and go live with it. 



Trouble with fundamentals, especially in this current situation, is that it needs historical performance data for the runners. And if there’s been a two month break for the sport, it’ll be hard to know how that translates when it restarts. It’s not something that could be backtested because it’s never happened before. So I’d be cautious on any fundamental approach until there’s at least a couple months of new data. I might even wait until next year now. 

---

## 2020-05-24 19:34:51 - strategies channel

**Unknown**

I have difficulty correlating data with the target (bet market). When I put everything on a dataframe (3 seasons) the number of goals scored, the recent performance, and other data like shots in the goal, corners etc ... has almost insignificant correlation, many goals seem just random.



I am doing a combination of all this and also with the SofaScore chart and there is improved a little, nothing very safe but enough to invest and try to profit.

---

## 2020-05-24 16:28:46 - strategies channel

**SrFabio**

Would you guys mind sharing which metrics do you normally consider when assessing the performance of your strategies? I use the list below but I'm curious if you guys use a simpler or more complex set of metrics

• Win / Strike Rate

• Volume Weighted Win Rate

• ROI

• Streaks

• Profit Factor

• Maximum Drawdown



---

## 2020-05-24 15:51:12 - general channel

**Sandy Caskie**

Ok so I went on my account with Global Sports API and use the swagger editor to load data endpoints. This works fine but when I try to load the object names such as  "[https://www.globalsportsapi.com/ODATAv1/HorseRacingSample/performances](https://www.globalsportsapi.com/ODATAv1/HorseRacingSample/performances)?" (I removed my app key) I get an internal service error. Is this a problem at there end?

---

## 2020-05-24 11:56:19 - issues channel

**Steve**

Hi, I'm just started using the streaming API. I consistently get the following message: WARNING:betfairlightweight.streaming.stream:[Stream: 1]: Latency high: 0.5950710773468018. Is this an issue with my connection or the BF server? And what precissely is the 0.5950710773468018 a reference to.

---

## 2020-05-23 00:18:28 - general channel

**VT**

Hi, I'm in the final stage of developing my BOT and now I need to automate and I still don't know how to do that, it's nothing exceptional just cheap json feed for live statistics + previous performance database + a little scraping.



I don't want to leave my computer on 24 hours a day running the system. Any suggestions for (cheap) servers that work and have no problem with the IP? ( my account is from Brazil).

---

## 2020-05-22 17:52:21 - general channel

**Julio**

I am going to use this time at home to try to migrate my personal strategies to flumine.

My understanding is that:

• check_market_book: defines the set of conditions to look at a market (status, time to start, number of runner, venue etc...)

• process_market_book: looks at the prices and volumes, computes indicators and places trades.

• process_orders: checks the order executions (ex: cancellation after x seconds)

The part that I am missing is that how:

• my current orders / positions feed back to process_market_book (as orders not in inputs). For instance my indicator flags a trade, but i do not want to trade each time I process_market_book, I only want to trade if len(orders)=0 

• the maketBook feeds back to order. I might want to cancel my pending order if the price drift away to much from the current price.

I could do self.orders=orders and self.market_book=market_book, but flumine is an efficient way and I'd prefer not introduce memory leakage.

---

## 2020-05-22 11:38:25 - general channel

**liam**

[https://pypi.org/project/memory-profiler/](https://pypi.org/project/memory-profiler/) to get an idea of where the leak was as it was processing, then created just a single generator using bflw (no memory leak) so realised it was how it was implemented in flumine, then noticed the queue being initialised in the base class

---

## 2020-05-21 22:10:14 - general channel

**Lee**

Also appending to bf_runs_list for every market book probably doesn’t help the memory leak

---

## 2020-05-21 21:53:16 - general channel

**Andrey Yunoshev**

Hi, guys. Nice framework, a great foundation for the future.



I'm just trying to analyze all the greyhound races in one day (and in the future I need a month).

The code is as simple as two pennies - but I never waited for it to finish.

Python eats up 29 gigabytes of memory and everything freezes :)



Is this expected at the moment or am I doing something wrong?



```class PastStrategy(BaseStrategy):

    def start(self) -&gt; None:

        None

    def check_market_book(self, market: Market, market_book: MarketBook) -&gt; bool:

        if market_book.status not in ["CLOSED", "SUSPENDED"]:

            town = market_book.market_definition.venue

            run_time = market.market_start_datetime.isoformat()

            key = "{0} at {1}".format(town, run_time)

            if town and key not in bf_runs_list:

                bf_runs_list.append(key)

                print("start processing new BF run: {0}, total {1} runs".format(key, len(bf_runs_list)))

            return True

        return False



    def process_market_book(self, market: Market, market_book: MarketBook) -&gt; None:

        None

    def process_orders(self, market: Market, orders: list) -&gt; None:

        None



markets = sorted(list_files_in_folder("./data/bf_uncompress/PRO/2020/May/1", "*.*"))



strategy = PastStrategy(

    market_filter={ "markets": markets},

    max_order_exposure=50,

    max_selection_exposure=10,



)



client = clients.BacktestClient()



framework = FlumineBacktest(

    client=client,

)



framework.add_strategy(strategy)

framework.run()```

---

## 2020-05-21 08:55:26 - general channel

**Jonjonjon**

I had a think last night. Handling of the generator in backtest.py would depend on whether or not iterating over stream_gen() is iterating over Market Books, or strings from the streaming data files. So I'm not sure how to implement it cleanly without uglifying your beautiful code.



At this point, I'm thinking that hard drive space is cheaper than developer time, especially when iterating over every file within a tar archive is slow (my computer averages 0.67 seconds to read a file from a tar archive). Also, using a tar does not save space, as it is the individual members of the tar that are zipped up.



Unzipping the soccer match odds files from Jan2020... The disk usage goes up from 472MB to 4.4GB.

---

## 2020-05-20 12:05:08 - general channel

**liam**

flumine patches it to speed streaming up

---

## 2020-05-19 14:21:00 - strategies channel

**mandelbot**

No I'm currently transitioning to bflw quite slowly as my background in coding is limited. I operate mainly on Bet Angel, which has some very good functionality but ultimately want to get to grips with bflw.

---

## 2020-05-19 11:41:00 - strategies channel

**James T**

This is all down to backtesting though. Not live split testing. 



So that’s another good use for a backtesting system like flumine. You can adjust your simulated latency and see what effect that has on returns. 

---

## 2020-05-19 11:39:38 - strategies channel

**James T**

In terms of strategy sensitivity to latency it really depends on the strategy. I would expect something fundamental based to be less sensitive to arbitrage for example. I would class what I do as statistical arbitrage, and I’m sensitive to around 100ms when betting pre-race. ie. I can notice lower returns with an extra delay of 100ms. 1ms not. 

---

## 2020-05-18 12:10:16 - random channel

**Remi**

I wonder if you could build any kind of edge in this market if it were traded. An edge could exist because the host may influence outcomes to create interesting matches or developments in the sport. Or maybe marble surface/density affects performance.

---

## 2020-05-18 07:54:27 - general channel

**Mo**

I think it's very hard/pointless to be optimising network latency given this infrastructure

---

## 2020-05-18 07:49:46 - general channel

**MrBIN**

Hi All. Do you know where is Betfair's matching engine server is located? and what is the best AWS datacenter \ availability zone in terms of latency?

---

## 2020-05-18 07:42:20 - general channel

**liam**

Agreed, or if you want a raw dict you can run streaming in [https://liampauling.github.io/betfair/advanced/#lightweight|lightweight mode](https://liampauling.github.io/betfair/advanced/#lightweight|lightweight mode) by

```listener = StreamListener(max_latency=None, lightweight=True)```

---

## 2020-05-17 15:49:19 - strategies channel

**Mo**

This was a good talk at MathSport 2019 "Establishing a performance edge in P2P betting": [https://rstudio-pubs-static.s3.amazonaws.com/509874_7a4aef970d924450bb246cc4b5128d52.html](https://rstudio-pubs-static.s3.amazonaws.com/509874_7a4aef970d924450bb246cc4b5128d52.html)

---

## 2020-05-14 12:51:47 - random channel

**Mo**

Generally if a game will run under proton then performance will be as good if not better than under windows. Use [http://protondb.com|protondb.com](http://protondb.com|protondb.com) to check compatibility of your games. 

---

## 2020-05-13 15:20:22 - random channel

**Lee**

So a profitable strategy eventually loses it's edge over time and needs optimizations

---

## 2020-05-12 15:45:32 - general channel

**klozovin**

yeah, I'm not that worried about GIL for performance sake, mostly for understanding how things actually work. I'm working on a Rust client for Betfair so I'm comparing how are things done...

---

## 2020-05-12 09:09:34 - general channel

**liam**

flumine does that + latency

---

## 2020-05-08 13:01:16 - general channel

**jhaa**

I have 'latency high' warnings - all the way up to 5 seconds for a while.  Then they stop for a while and then they come back. The difference between 'published time' and my local time is always below one second though.



What is likely happening here?

---

## 2020-05-05 09:09:46 - random channel

**liam**

do the latency logs increase or is it stable? It might be your clock as 70 markets is nothing

---

## 2020-05-05 09:06:26 - random channel

**liam**

No you can't, out of interest how many markets are you subscribed to? As you really shouldn't have latency issues with greyhounds as the data/updates are minimal

---

## 2020-05-04 19:27:12 - general channel

**MacrcoPolo**

Solely latency

---

## 2020-05-04 19:27:01 - general channel

**MacrcoPolo**

Latency

---

## 2020-05-03 08:53:05 - random channel

**liam**

With flumine the target is making a simple framework which is going to come at a cost of performance. 

However eventually we can add the ability to use lightweight mode and handle the raw json, this will rapidly speed up backtesting, not worth it for the 99% when live trading unless speed is a priority or you are processing lots of markets. 



Very keen on benchmarking, with my own framework it’s about a minute for each racing market or sub 10s when using lightweight mode. I use a variation of threads, processes and AWS lambda for overnight backtesting. 

---

## 2020-05-02 23:35:32 - random channel

**Lee**

The Ryzen CPUs cost/performance is tempting me to make the switch to linux.

---

## 2020-05-02 23:15:08 - random channel

**Jonatan (skyw)**

[@UPMUFSGCR](@UPMUFSGCR) I created benchmarks for the bflw market cache above, that should give you an upper bound on how fast it can be.



I'm interested in performance in simulated execution.



If you want to benchmark just run the script using timeit I would say is the simplest.

---

## 2020-05-02 22:56:07 - random channel

**Jonjonjon**

Is anyone interested in, and is there any way, to benchmark and compare the performance of Flumine on our different machines? I've got a very old PC, and am just wondering how much faster a newer machine will be.

---

## 2020-04-30 13:32:54 - issues channel

**Julio**

Thanks Jonatan. indeed I can see that: WARNING:betfairlightweight.streaming.stream:[Stream: 1001]: Latency high: [tel:15264482498|5.526448249](tel:15264482498|5.526448249). Is this represents the number of seconds a message stays in the queue before being pick up?

---

## 2020-04-30 12:58:20 - issues channel

**Jonatan (skyw)**

[@U7E6NE1DM](@U7E6NE1DM) you could also check latency when you pull from queue you will probably notice blocking code / long running calculations quicker instead of waiting for the queue to fill up.

---

## 2020-04-27 12:01:47 - random channel

**James T**

Hi DC, by coincidence I got an agent email looking for a C++ developer with low latency and or trading platform experience. Contract job, potentially long term though. DM me your email and I’ll forward to you. 

---

## 2020-04-26 10:29:19 - issues channel

**user34**

import logging

from betfairlightweight import StreamListener



logging.basicConfig(level=[http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))

listener = StreamListener(max_latency=None)

---

## 2020-04-26 10:28:53 - issues channel

**user34**

import logging

from betfairlightweight import StreamListener



logging.basicConfig(level=[http://logging.INFO|logging.INFO](http://logging.INFO|logging.INFO))

listener = betfairlightweight.StreamListener(max_latency=None)

---

## 2020-04-25 19:43:38 - issues channel

**user34**

listener = StreamListener(max_latency=None)

---

## 2020-04-25 19:43:03 - issues channel

**user34**

File "/anaconda3/lib/python3.6/site-packages/betfairlightweight/streaming/listener.py", line 91, in __init__

    super(StreamListener,self).__init__(max_latency)



TypeError: super(type, obj): obj must be an instance or subtype of type

---

## 2020-04-25 12:15:59 - issues channel

**Dave**

Fair enough - when I looked at customerRef in the past as I was concerned there was some extra latency on Betfair side for insertion of order into the market (as it checks for dupes first) but probably won't end up being the bottleneck unless you're colo'd and using your own network stack :grin:

---

## 2020-04-24 10:11:20 - random channel

**Unknown**

For your reference this is a flumine instance that has been up for 2 weeks recording 200-400 markets, memory is very flat. I have noticed that there might be a memory leak in the race_card.login() endpoint, are you using that?

---

## 2020-04-24 08:10:09 - random channel

**Newbie99**

Just going back to the high latency warnings, I got some strange ones last night (which might just be a limitation of my machine, in which case so be it, but wanted to get the opinion of others):



`CRITICAL:streaming_errors:MarketStreaming run error`

`MemoryError`



`During handling of the above exception, another exception occurred:`



`Traceback (most recent call last):`

  `File "D:\Python37\lib\site-packages\betfairlightweight\resources\bettingresources.py", line 504, in __init__`

    `self.ex = RunnerBookEX(**ex) if ex else None`

  `File "D:\Python37\lib\site-packages\betfairlightweight\resources\bettingresources.py", line 377, in __init__`

    `self.available_to_lay = [PriceSize(**i) for i in availableToLay]`

`MemoryError`



`During handling of the above exception, another exception occurred:`



`Traceback (most recent call last):`

  `File "D:\Python37\webpages\streaming_errors.py", line 46, in run`

    `self.stream.start()`

  `File "D:\Python37\lib\site-packages\betfairlightweight\streaming\betfairstream.py", line 59, in start`

    `self._read_loop()`

  `File "D:\Python37\lib\site-packages\betfairlightweight\streaming\betfairstream.py", line 209, in _read_loop`

    `self._data(received_data)`

  `File "D:\Python37\lib\site-packages\betfairlightweight\streaming\betfairstream.py", line 248, in _data`

    `if self.listener.on_data(received_data) is False:`

  `File "D:\Python37\lib\site-packages\betfairlightweight\streaming\listener.py", line 127, in on_data`

    `self._on_change_message(data, unique_id)`

  `File "D:\Python37\lib\site-packages\betfairlightweight\streaming\listener.py", line 167, in _on_change_message`

    `self.stream.on_update(data)`

  `File "D:\Python37\lib\site-packages\betfairlightweight\streaming\stream.py", line 59, in on_update`

    `self._process(data[self._lookup], publish_time)`

  `File "D:\Python37\lib\site-packages\betfairlightweight\streaming\stream.py", line 153, in _process`

    `self.unique_id, market_book, self._lightweight`

  `File "D:\Python37\lib\site-packages\betfairlightweight\streaming\cache.py", line 229, in create_resource`

  `File "D:\Python37\lib\site-packages\betfairlightweight\resources\bettingresources.py", line 585, in __init__`

    `self.runners = [RunnerBook(**i) for i in kwargs.get("runners")]`

`MemoryError`

---

## 2020-04-22 23:36:41 - random channel

**Newbie99**

and somehow once the high latency warnings appear it just never seems to recover

---

## 2020-04-22 21:46:32 - random channel

**Newbie99**

It basically occurs around 2am when some weird processes occur (nothing to do with BFLW), so I'm not too worried about my code, its just something else that I need to resolve, but as a stop gap, I find restarting the script once the process has stopped does the trick, so I just wanted to establish a high latency warning had occurred, then pause for x seconds until the process completes and then restart the script (for some reason once the warning appears the script never seems to recover)

---

## 2020-04-22 21:18:00 - random channel

**Newbie99**

I keep getting high latency warnings over night (they are genuine, I seem to have some weird processes running that I need to sort out), anyway, that aside, as a stopgap, a quick restart of the python script always seems to get things back on track. But is there a way I can look for a high latency warning and then automatically perform a restart somehow (well I presume I can work that bit out, its more a case of where do I need to be looking to determine programatically that I'm getting a high latency warning, then I can do something like pause for x seconds then restart)?

---

## 2020-04-11 08:06:43 - general channel

**liam**

So I use flumine for all my data recording and I have a separate framework for strategies. I can’t open source the latter due to their being too much secret sauce tightly coupled to it but I am slowly advancing flumine to be at the same level (if not better / more dynamic / plug and play) 

---

## 2020-04-10 22:05:10 - issues channel

**liam**

10ms seems pretty quick, I don’t think you will get quicker than that with something that isn’t in memory, why is speed important? / do you need use a db for this and not just python?

---

## 2020-04-10 14:11:43 - general channel

**ClauMor**

anyway i get warning with 1.5 seconds latency

---

## 2020-04-10 14:09:29 - general channel

**Mo**

The publish time is divided by 1000 during calculation of the latency

---

## 2020-04-10 14:03:39 - general channel

**ClauMor**

that means, in the betfairlightweight package, the default max_latency is .5

---

## 2020-04-10 07:28:26 - random channel

**liam**

Yeah always open to performance improvements

---

## 2020-04-09 21:25:47 - random channel

**Jonjonjon**

Do you think it's worth investigating? There is a chance it could improve performance. Though I have not done any detailed analysis, so I could be wrong.

---

## 2020-04-09 20:39:37 - random channel

**Unknown**

[@U4H19D1D2](@U4H19D1D2) In this bit of code in streaming.cache, did you compare the performance against an implementation using an OrderedDict to store prices?

---

## 2020-04-09 07:16:01 - issues channel

**JK**

changed the `max_latency` to 0.01 and it worked. Thanks for your help :slightly_smiling_face:

---

## 2020-04-09 07:02:34 - issues channel

**JK**

Thanks a lot! It's now reading it, but getting another issue:

```INFO:betfairlightweight.streaming.stream:[Stream: HISTORICAL]: "MarketStream" created

Traceback (most recent call last):

  File "C:\Users\jhgwa\Documents\101-layer\stream_[http://listener.py|listener.py](http://listener.py|listener.py)", line 74, in &lt;module&gt;

    stream.start()

  File "C:\Users\jhgwa\AppData\Local\Continuum\anaconda3\lib\site-packages\betfairlightweight\streaming\[http://betfairstream.py|betfairstream.py](http://betfairstream.py|betfairstream.py)", line 286, in start

    self._read_loop()

  File "C:\Users\jhgwa\AppData\Local\Continuum\anaconda3\lib\site-packages\betfairlightweight\streaming\[http://betfairstream.py|betfairstream.py](http://betfairstream.py|betfairstream.py)", line 294, in _read_loop

    if self.listener.on_data(update) is False:

  File "C:\Users\jhgwa\AppData\Local\Continuum\anaconda3\lib\site-packages\betfairlightweight\streaming\[http://listener.py|listener.py](http://listener.py|listener.py)", line 115, in on_data

    self._on_change_message(data, unique_id)

  File "C:\Users\jhgwa\AppData\Local\Continuum\anaconda3\lib\site-packages\betfairlightweight\streaming\[http://listener.py|listener.py](http://listener.py|listener.py)", line 148, in _on_change_message

    self.stream.on_update(data)

  File "C:\Users\jhgwa\AppData\Local\Continuum\anaconda3\lib\site-packages\betfairlightweight\streaming\[http://stream.py|stream.py](http://stream.py|stream.py)", line 51, in on_update

    if latency &gt; self._max_latency:

TypeError: '&gt;' not supported between instances of 'float' and 'NoneType'```

Have you seen this one before? To do with the `max_latency` param?

---

## 2020-04-09 06:41:30 - issues channel

**JK**

Hey guys, ive got some historic stream data in bz2 files, 1 per market, but im having trouble reading it. Im using the example script at [https://github.com/liampauling/betfair/blob/master/examples/examplestreaminghistorical.py](https://github.com/liampauling/betfair/blob/master/examples/examplestreaminghistorical.py)



My main code looks like this



```# create listener

listener = HistoricalListener(max_latency=None)



# create historical stream, update directory to file location

stream = trading.streaming.create_historical_stream(

    directory='../data/Jan/1/29636351',

    listener=listener,

)



# start stream

stream.start()```

But I am getting the error `[Errno 13] Permission denied: '../data/Jan/1/29636351` , anyone else had this issue? Have googled to no avail. Is this the correct way to write the data to txt?

---

## 2020-03-16 20:24:53 - strategies channel

**James T**

Sorry for the slow reply. How to calculate a favourable price (but one which will get matched) is obviously a trade secret for anyone that’s profitable. My only tip with offering is to say it’s just as important to remove your offer if you deem it not to be of good value anymore. A favourable price you calculate now might not be the same favourable price in X seconds. So just leaving an offer up indefinitely is generally a route to ruin. 

---

## 2020-03-15 21:37:47 - issues channel

**Alex A**

It has lower latency than polling, is easier, and doesn’t have the same system around weighting of requests.

---

## 2020-03-09 12:46:10 - general channel

**Alexander Keliris**

I love Haskell, have done a few side projects with it and used to attend the Hoodlums meetups at Barclays. But since getting into Rust I found it gives you similar runtime guarantees but with much better performance. More importantly, I found Rust much easier to work with for real projects (better tooling, `cargo` etc.)

---

## 2020-03-06 20:12:42 - general channel

**Jonjonjon**

[@UUM0N2B6W](@UUM0N2B6W) Yes I am using the customer order ref field. I listen for a current orders stream. And when orders come in with those trade refs, I delete them from the Python "set" or hashes that I have stored in memory

---

## 2020-02-29 17:03:39 - general channel

**liam**

You can remove the errors by upping the latency on the listener 

---

## 2020-02-29 17:01:10 - general channel

**Unknown**

With a utilisation on the right, max below 5%, would you expect the number of high latency warnings?

---

## 2020-02-28 15:01:22 - issues channel

**Ian**

on flumine I'm receiving constant high latency warnings on all 3 streams - dogs, horses &amp; football

---

## 2020-02-27 13:55:15 - general channel

**LK**

Question for [@U4H19D1D2](@U4H19D1D2) maybe? Yesterday my app that subscribes to the Orderstream got "Latency high" warnings, latency went as high as couple hundred seconds (!). Then the connection to betfair got disconnected. After reconnecting everything was fine again. I am wondering: could this be a betfair issue? Should I pre-emptively disconnect/reconnect when I get "Latency high" warnings?

---

## 2020-02-24 16:31:40 - strategies channel

**liam**

they have a similar gui to yourself, positions overlayed onto google maps (i think), they monitor latency and accuracy, replacing any trackers which aren't up to scratch

---

## 2020-02-24 16:10:44 - strategies channel

**D C**

I'm adjusting for latency as best I can to cater for asynchronous packet transmission from the sensors themselves but I still seem to get constant offset vectors. Even when in the stalls they don't always line up in what I would call a "line"

---

## 2020-02-20 13:02:03 - general channel

**liam**

nothing is excluded, creating python objects is slow

---

## 2020-02-19 22:10:35 - general channel

**IamYou**

If you really need to parse json on each line then maybe check ujson for performance.

---

## 2020-02-17 10:55:53 - strategies channel

**James T**

I’ve researched / tried something similar with decent (low latency) bookmaker feeds for horse racing and didn’t find a massive edge, and in the end wasn’t worth the high fees for the feeds. TxOdds is like £6k a month. 

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

## 2020-01-29 20:15:39 - general channel

**bting91**

ash ok so theres a bit of latency

---

## 2020-01-11 16:58:30 - general channel

**AP**

```def process_betfair_historical_file(file_path):

    print("Processing: " + file_path)

    

    class HistoricalStream(MarketStream):

    # create custom listener and stream



        def __init__(self, listener):

            super(HistoricalStream, self).__init__(listener)

            self.file_path = file_path.split("/")[-1]

            self.output = open(self.file_path + '.txt', 'w')

            self.output.write('Time,MarketStartTime,MarketType,MarketId,Status,Inplay,SelectionId,VWAP,BestLayPrice,LastPriceTraded,\n')



        def on_process(self, market_books):

            for market_book in market_books:

                for runner in market_book.runners:



                    # how to get runner details from the market definition

                    market_def = market_book.market_definition

                    runners_dict = {(runner.selection_id, runner.handicap): runner for runner in market_def.runners}

                    runner_def = runners_dict.get(

                        (runner.selection_id, runner.handicap)

                    )



                    # calculate lay wap

                    price = 0

                    vol = 0

                    for trade in runner.ex.traded_volume:

                        price += (trade.price * trade.size)

                        vol += trade.size

                    try:    

                        wap = price / vol

                    except:

                        wap = np.nan



                    # get best lay price

                    try:

                        best_lay = runner.ex.available_to_lay[0].price

                    except:

                        best_lay = np.nan



                    self.output.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (

                        market_book.publish_time, market_def.market_time, market_def.market_type, market_book.market_id, market_book.status, market_book.inplay,

                        runner.selection_id, wap or '', best_lay or '', runner.last_price_traded or ''

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

    stream = trading.streaming.create_historical_stream(

        directory=file_path,

        listener=listener

    )



    # start stream

    stream.start(async_=False)

    

    return "Processed" + file_path```

---

## 2020-01-11 15:48:00 - general channel

**Jonatan (skyw)**

I "solved" it by opening it in the _init_ method and never closing it...I think it should be taken care of automatically.

In my head it went a little faster. Would be nice if you could report the speedups : )

---

## 2020-01-08 17:14:44 - general channel

**AP**

Ok so for trading live the historical data is stored in memory for the most part 

---

## 2019-12-24 17:25:56 - general channel

**Chris**

If you have high latency on a streamer (downloading data with flumine on a server), does this mean it could potentially miss updates? Or is it just saying that it will take longer to process

---

## 2019-12-19 14:27:48 - general channel

**ash**

Dose anybody know how an in-memory sqlite database would compare speed wise to redis?  Saving the database to disk when the market completes?

I am not sure about accessing the data between processes either, that should be possible though I presume?

---

## 2019-12-18 13:06:44 - general channel

**Newbie99**

I could refine my code and keep more in memory, but then it gets a lot more complex and I'm not sure whether its the best option for me, if super low latency isn't a huge concern (which it isn't)

---

## 2019-12-18 13:05:46 - general channel

**Newbie99**

Yeah, that I feel would be useful, as I can then play around with the Redis data and analyse a bit more (to refine my models over time).



I don't need super speed, my hardware isn't good enough currently to make that worth worrying about, so not fussed about nano-seconds, but MySQL is just not usable for this kind of a thing, if you have more than a handful of runners the whole thing just grinds to a halt if you're inserting and select querying regularly!

---

## 2019-12-18 12:56:34 - general channel

**Newbie99**

A very general question, but what do people tend / prefer to use for storing 'live data', by which I mean price data or similar from currently live markets?



I have been using MySQL for my static stuff, but thats way too slow to use for pricing data, so until now I've just created a previous market state in my Python scripts, however I want to get a bit more sophisticated (and possibly tidy up the code too!), so was thinking of an in-memory database like Reddis (which I have seen mentioned on here previously), but was just curious to see what others are using.

---

## 2019-12-16 09:43:49 - general channel

**liam**

[@U7R5CEDAL](@U7R5CEDAL) do you get the 'Latency: xx.xxxs' log? I can't see anything from my logs yesterday

---

## 2019-12-03 11:55:08 - random channel

**Tom Poole**

Liam has given me permission to post a job that my Colleague is currently working. A super exciting greenfield project with the UKs #1 odds comparison site, owned by a major player in the gambling industry. He is looking for high caliber Java/Python/Go Developers to join the highly autonomous and creative team to work on their highly scalable and low latency core platform, moving into inplay streaming. Salary is incredibly competitive in addition to a bonus scheme of up to 25%! For more details please email James Full at [mailto:James@formularecruitment.co.uk|James@formularecruitment.co.uk](mailto:James@formularecruitment.co.uk|James@formularecruitment.co.uk) or give him a call on 020 3940 7464.

---

## 2019-12-02 10:52:13 - random channel

**Tom Poole**

Liam has given me permission to post an exciting new DevOps Lead Engineer opportunity in a high traffic data and streaming platform sports company, based in Central London.



As Lead DevOps Engineer you will report to the VP of Technology and will be tasked with shaping and executing the cloud and DevOps strategy. Given the seniority of the role, you should have a strong analytical mindset, be a natural problem-solver and enjoy working closely with Software Engineering teams to create a best in breed infrastructure ecosystem. You'll be responsible for shaping, building and monitoring a scalable cloud-based infrastructure (hybrid AWS / GCP… you decide!) and live operations environment. Given this is a new greenfield team you’ll have the opportunity to do this speed, scalability and security in mind. You’ll be given the autonomy to choose the best technologies and processes that will allows Engineers to consumer services effortlessly. The company has a great culture with lots of autonomy and empowerment to do things the right way.



As Lead DevOps Engineer you will need the following:

•	DevOps Engineer

•	Cloud experience AWS and/or GCP

•	Containerisation

•	CI / CD Pipelines

•	Strategy and execution

•	Docker and Kubernetes

•	Excellent communication skills

•	Advocate Agile working

•	Sports enthusiast



In return you will receive a generous salary package ranging from £90,000 - £110,000 plus bonus as well as some great benefits including free gym memberships, private medical/dental insurance and a competitive annual holiday plan.



If you are interested in learning more about the role, then please let me know when you’re next available, so I can update my diary. I look forward to hearing from you

---

## 2019-11-29 09:33:44 - general channel

**liam**

Anyone seeing latency issues on the hour during the day? Not sure if its me or Betfair but started on the 21st which coincides with the SUB_IMAGE update

---

## 2019-11-28 21:55:20 - general channel

**Jonjonjon**

What exactly does includeOverallPosition mean in relation to the order filter in the streaming api? If I turn it off will get I better performance?

---

## 2019-11-28 12:54:03 - issues channel

**Evaldas**

Hi, today at about 10:12am all market and order streams just stopped for me. No errors, no timeouts, just nothing. Ive been running this same code for 1+ years, never seen anything like this. Was it just me? I have max_latency=0.5 and heartbeat_ms=3000 on subscribtions. so confused, I have no idea what happened :confused:

---

## 2019-10-19 22:22:57 - general channel

**JonJonJon**

I need something like that to help differentiate the performance of different strategies.

---

## 2019-09-27 15:55:56 - general channel

**Mo**

Unless you use the async parameter then your order is in the book when your call to placeOrders returns.



The only reason a streaming price update received after that would not include your order would be if you had some latency in receiving the updates. 

---

## 2019-09-22 16:14:42 - general channel

**liam**

Yeah threads are your friend, ideally you don’t want to block the queue, the latency warning is handy in telling you that you have network or cpu issues. It’s based off your clock so common issue is it not being in sync 

---

## 2019-09-22 15:52:07 - general channel

**ash**

I think it’s cpu..   its only sporadic so correlates with increased demand due to more frequent stream updates.

isn’t the clock updated prior to calculating the latency?

I am trying to do calculations in the same program as reading the stream which is a bit to much of an ask i think. I need to rethink my overall structure maybe

---

## 2019-09-22 15:11:42 - general channel

**ash**

quick question, I hope. When i get ```betfairlightweight.streaming.stream:[Stream: 1]: Latency high: 0.8129971027374268``` is that due to latency at my end working through the Que,   or is it warning me that the data I am getting from bet-fair is delayed in some way? Likewise, is market_book.publish_time the time I receive the update or is it the time bet-fair sends it?

---

## 2019-09-18 14:16:02 - general channel

**liam**

i record all round trip latency for any requests and log, then aggregate via cloudwatch and datadog and monitor periodically / alerts when above certain thresholds

---

## 2019-09-13 16:10:15 - general channel

**liam**

yeah event driven single threaded, dont care about latency

---

## 2019-08-16 22:01:02 - general channel

**William**

Still having difficulty with speed and historical streaming. Seems to be taking 20s to go through a single race but it is only using around 4% of CPU? Is it because it is limited by other factors? I am doing a fair bit of csv writing so that could be an issue.

---

## 2019-08-15 13:05:55 - general channel

**Mo**

Redis is an in memory database but it has lots of functionality built upon that (you can use it for pubsub messaging for example). MySQL, Postgres etc would be RDBMSs. From your brief description, I suspect Redis might be a better fit for what you’re using MySQL for. Very generally speaking, I think Redis is better suited for live trading and a RDBMS for all of your “offline” data needs like backtesting, bet reconciliation etc

---

## 2019-08-09 15:00:12 - general channel

**Robert**

Hi, we are doing streaming of historical berfair data

like in the example [https://github.com/liampauling/betfair/blob/master/examples/examplestreaminghistorical.py](https://github.com/liampauling/betfair/blob/master/examples/examplestreaminghistorical.py)

and we are only interested in data &lt;1200s before the race starts and not the rest and its very slow to process all of the data

how can we filter out all the requests so I dont have to stream all the requests

---

## 2019-08-05 15:05:07 - general channel

**liam**

what warnings are you getting, on every update? average latency?

---

## 2019-08-04 15:37:07 - general channel

**liam**

You can hide by setting the max_latency on the listener 

---

## 2019-08-04 15:26:21 - general channel

**Ian**

Hi all, on flumine, I'm seeing high latency issues. Searching back this is can be clock or CPU (or some other bottleneck). Time looks good, In the logs, CPU is never &gt;1.5% utilisation. Network solid:



PING [http://ie1-ang.betfair.com|ie1-ang.betfair.com](http://ie1-ang.betfair.com|ie1-ang.betfair.com) (84.20.208.147) 56(84) bytes of data.

64 bytes from 84.20.208.147 (84.20.208.147): icmp_seq=1 ttl=243 time=11.8 ms

64 bytes from 84.20.208.147 (84.20.208.147): icmp_seq=2 ttl=243 time=11.10 ms

64 bytes from 84.20.208.147 (84.20.208.147): icmp_seq=3 ttl=243 time=11.7 ms

64 bytes from 84.20.208.147 (84.20.208.147): icmp_seq=4 ttl=243 time=11.6 ms

64 bytes from 84.20.208.147 (84.20.208.147): icmp_seq=5 ttl=243 time=11.8 ms

64 bytes from 84.20.208.147 (84.20.208.147): icmp_seq=6 ttl=243 time=11.7 ms

64 bytes from 84.20.208.147 (84.20.208.147): icmp_seq=7 ttl=243 time=11.6 ms



Anything else I should check?

---

## 2019-07-28 07:00:04 - general channel

**liam**

Python is slow 

---

## 2019-07-22 15:22:25 - general channel

**Oliver Varney**

by default visual studios wasnt spitting these out to the console for me. I am however seeing a high latency message now. What is the typical latency people see via the streaming market option ?

---

## 2019-07-22 12:10:07 - general channel

**Oliver Varney**

Morning all, hope everyone had a nice weekend! Liam just looking through the flumine code now and was wondering if you separate out your market recording via flumine from your trading programs or can the two be easily used in conjugation without hacking code or performance issues?

---

## 2019-07-12 21:21:29 - general channel

**Newbie99**

I didn't realise it was possible to use a single queue, I thought they had to be split...is there a recommended approach (i.e. is different threads likely to be better or does it not make much difference performance wise)?

---

## 2019-06-21 10:53:03 - issues channel

**liam**

you can remove it by setting a higher value on the listener (max_latency)

---

## 2019-06-21 10:51:41 - issues channel

**Newbie99**

morning, I keep getting the following today, am I right in thinking this is just an issue at Betfair and there's not really much I can do, other than wait it out?



```

WARNING:betfairlightweight.streaming.stream:[Stream: 1]: Latency high: 1.112811803817749

WARNING:betfairlightweight.streaming.stream:[Stream: 1]: Latency high: 1.1146831512451172

WARNING:betfairlightweight.streaming.stream:[Stream: 1]: Latency high: 1.1135742664337158

```

---

## 2019-05-31 07:09:22 - issues channel

**liam**

my issue was that in framework I had a Market class which was storing a history of all prices/analytics, so come the end of a race this had a rather large memory footprint. I was deleting on closure along with what I thought was all references but after a lot of debugging I found i had a reference to it in my logging framework. you can try deleting all closed markets in the cache (listener.stream._cache)

---

## 2019-05-31 02:16:25 - issues channel

**richard_h**

I'm running betfairlightweight to stream data and its memory footprint is slowly increasing over time, is there a way to clear memory? I read something in the history about using snap, is that necessary to not have memory issues? I don't need to save price history but I can't really see where it's being saved.

---

## 2019-04-25 11:31:15 - general channel

**Filippo Bovo**

I am a data scientist and have been using Pandas for about three years. Pandas was built with speed in mind using C (and Numpy), and it is good to manipulating static data. However, I have never tried dealing with live data with Pandas DataFrames. The main bottleneck I see in this case is appending and dropping data to an existing DataFrame. If I will test this in the future, I will let you know.

---

## 2019-04-04 07:55:33 - general channel

**LK**

to measure marketstream latency I simply compare the publishTime on incoming messages with the current time (time.time()).

---

## 2019-04-03 17:19:20 - general channel

**LK**

these are stats for every 100 messages received from betfair, comparing the publishTime with the time on the server. Latency is 1-way latency, since it is market datastream.

---

## 2019-04-03 17:18:20 - general channel

**LK**

8.54 timedelta | latency min 9.17 ms | avg 10.10 | median 10.04 | 90th 11.42 | 95th 11.69 | max 11.84 ms

6.24 timedelta | latency min 9.17 ms | avg 10.29 | median 10.05 | 90th 11.24 | 95th 14.10 | max 14.29 ms

4.13 timedelta | latency min 9.26 ms | avg 10.32 | median 10.11 | 90th 10.99 | 95th 11.18 | max 17.97 ms

---

## 2019-04-03 17:17:29 - general channel

**LK**

Often I feel speed as advertised seems to be confused with bandwidth. Bandwidth is not the issue, but latency and variance in latency are key.

---

## 2019-04-03 17:05:06 - general channel

**Paw**

so I'm an GCP expert but have no time right now to check latency from their servers

---

## 2019-03-04 11:23:28 - issues channel

**liam**

yeah just ignore anything you dont want, streaming is very light on CPU/memory so having a few markets you don't want isn't a problem

---

## 2019-02-17 13:48:17 - general channel

**Marcel**

Hello, nice there is a Phyton Betfair API community! I am new to Python and the Betfair API. Currently I use a vendor application in combination with Excel VBA.



To improve speed and flexibility I would like to build a bot in Python for betting on Match Odds soccer. Does someone has a script which generates a coupon of matches for the day with betting functionality which I can use as a starting point to add my criteria to place bets on those markets? That would be great!

---

## 2019-02-05 21:19:57 - issues channel

**liam**

It was more python is really slow and creating millions of resources is really really slow but if it just passes the json back to the user it’s just slow 

---

## 2019-02-05 20:41:28 - issues channel

**Newbie99**

Which is the best set of docs, to get up to speed with the various calls etc. when using betfairlightweight. I had a look on Github, but I thought there was another extensive doc I found previously (which I now can't find)?

---

## 2018-11-12 11:33:28 - general channel

**George**

still interested in what people think the internal latency (receiving order at their server through to order being placed) is, roughly

---

## 2018-11-12 11:29:05 - general channel

**liam**

I don't think it decreases latency because sometimes you will get a response from placeOrders before you get an orderStream update

---

## 2018-11-12 11:27:17 - general channel

**George**

interesting. i am not 100% following all the details but this is good info. are you saying that async mode has better latency when sending multiple orders in a single message?

---

## 2018-11-12 11:16:19 - general channel

**George**

does anyone know about latency within Betfair's systems - as in, if my order reaches their servers at time X, roughly how long does it take before the order gets matched?

---

## 2018-09-20 15:00:38 - issues channel

**loken92**

Hi!

I am implementing the stream listener and experiencing some issues. For some reason the python script stops at random, without any error. I think it could be related to high latency. Any tips on what could be causing this and how to fix it? Thanks!

---

## 2018-09-19 15:18:56 - general channel

**liam**

Your first issue is python is slow

---

## 2018-08-16 21:41:45 - general channel

**Rory**

do you mean in performance?

---

## 2018-07-26 16:40:20 - random channel

**Anatoliy**

Do you know whether a latency of 160ms for the complete operation, including roundtrip is fast enough, or way too slow?

---

## 2018-07-09 16:26:54 - general channel

**klozovin**

[@U93H3483E](@U93H3483E) yeah, AWS and Linode are okay for that, that's what I'm planning. I was just wondering about Sporting Servers because they promise low latency, maybe lower than one can achieve with just a VPS in the UK

---

## 2018-06-06 21:25:30 - general channel

**Ben**

and also return HistoricalStream(

                unique_id, self.output_queue, self.max_latency, self.lightweight

            ) by HistoricalStream(self)

---

## 2018-06-06 21:24:05 - general channel

**Ben**

and def __init__(self, unique_id, output_queue, max_latency, lightweight): just above by

---

## 2018-06-06 21:23:30 - general channel

**Ben**

super(HistoricalStream, self).__init__(unique_id, output_queue, max_latency, lightweight) try to replace by:

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

## 2018-03-10 08:06:19 - general channel

**liam**

It’s a lightweight calculated value, how long the request took, can be ignored unless you want to monitor latency 

---

## 2018-02-17 17:29:52 - general channel

**seaders**

"performance"?

---

## 2018-02-17 17:29:07 - general channel

**Ian**

in your experience performance is typically better on streaming, or not?

---

## 2017-12-14 02:20:06 - general channel

**seaders**

```from betfairlightweight import APIClient

from betfairlightweight.streaming import StreamListener, MarketStream





class HistoricalStream(MarketStream):

    def __init__(self, listener):

        super(HistoricalStream, self).__init__(listener)

        print('Time,MarketId,Status,Inplay,SelectionId,LastPriceTraded\n')



    def on_process(self, market_books):

        for market_book in market_books:

            for runner in market_book.runners:

                print(

                    market_book.publish_time, market_book.market_id,

                    market_book.status, market_book.inplay,

                    runner.selection_id, runner.last_price_traded or '')





class HistoricalListener(StreamListener):

    def _add_stream(self, unique_id, stream_type):

        if stream_type == 'marketSubscription':

            return HistoricalStream(self)





apiclient = APIClient('aa', 'bb', 'cc')



stream = apiclient.streaming.create_historical_stream(

    directory='/Users/seaders/Downloads/data/xds/historic/BASIC/27641921/27641921',

    listener=HistoricalListener(max_latency=1e100))

stream.start(async=False)

```

---

## 2017-10-31 08:03:10 - general channel

**OT**

[@U4H19D1D2](@U4H19D1D2), would it be too much to ask of you to make a quick example of how to feed a historical file into the gofair package? I am trying to replicate the betfairlightweight historical example so I can back to back speed test the two.

---

## 2017-10-26 21:07:47 - issues channel

**liam**

Yeh performance is an issue, I have moved to golang for parsing historical data 

---

## 2017-10-26 20:55:35 - issues channel

**OT**

I've written a backtester but having big performance problems with the volume of 1sec advanced data.

---

## 2017-08-27 16:40:23 - general channel

**liam**

Why do you want to give it parameters? Betfair have removed the aus wallet so wallet does nothing for now, although they are talking about adding the ability for more wallets. Session is for passing a requests session, reduces latency when making multiple requests however can be ignored for most requests 

---

## 2017-07-11 11:18:28 - general channel

**agberk**

If the strategy isn't speed dependent then spawning threads on demand is what I do

---

## 2017-07-11 11:12:47 - general channel

**liam**

To get around the delay I just start a new thread but I know this isn't very pythonic and starting a new thread is also slow 100ms ish I think 

---

## 2017-07-09 06:44:13 - general channel

**liam**

The reasoning behind it is that lightweight is only really beneficial on marketbook requests as that is when you want to reduce latency, I don't use it but if I were to use it I would want to have a full resource for all the other requests. Happy to remove but wanted it to be dynamic as I am not sure how others are using it

---

## 2017-06-02 14:44:05 - general channel

**agberk**

[@U4H19D1D2](@U4H19D1D2) am running into situations quite frequently today where the stream / socket stops receiving data but I'm not getting an exception or the read loop isn't exiting as I'm expecting; I know there was something recent discussion on subscribing multiple times on a socket, or perhaps creating multiple streams or something - I'm about to go look at the issues to refresh my memory - I'm still on v1.0.0 so it might be the problem is fixed just thought I'd check to see whether describing that behaviour made you think of anything obvious

---

## 2017-05-17 14:41:58 - general channel

**liam**

docker speeds things up for me, can go from no ec2 instances available to a program running and i just have to install docker

---

## 2017-05-17 14:13:05 - general channel

**agberk**

so by default its thread safe; and presumably you get better performance creating a session for each thread to use?

---

## 2017-05-12 08:42:51 - general channel

**jfo**

haven't done anything on it for a while, but i'm interested to see the speed of it vs python

---

## 2017-05-08 16:47:14 - general channel

**liam**

I average around 0.2s for placeOrders on AWS (Ireland region) BA is good but when using automation or the excel integration there is going to be a big delay between your trigger and the order hitting the market. When it comes to In play racing milliseconds can count. So when it comes to getting matched you need to process your trigger quicker or reduce the latency on your orders 

---

## 2017-05-08 16:36:05 - general channel

**jfo**

still in the process of putting together my own order placing strategy so using betangel server with streaming to get up and running before coding it all. so not sure on latency, at what number does latency become bad? obviously the lower the better

---

## 2017-05-08 16:30:33 - general channel

**liam**

What sort of latency have you got at the moment? Easy way to access is to log the following place_order_response.elapsed_time 

---

## 2017-04-27 21:09:11 - general channel

**liam**

Yeh streaming data is cached so as the day goes on memory use will increase but shouldn't be that much, you seeing big increases? 

---

## 2017-04-19 17:50:25 - general channel

**liam**

Yeh, you only pay for out beyond the free tier, streaming has reduced this for me a lot. There is a data centre in London as well but I haven’t done any latency tests

---

## 2017-04-19 17:33:52 - general channel

**favetelinguis**

yes pandas is nice as long as your data fits in memory

---

