# Quick Reference - Questions & Answers

*Most frequently asked questions with expert answers*

## Q: What issues are you seeing the historical data? Thought the pro stuff was good.

**A:** flumine can do whatever you want, the selling point is the switch to backtest / paper / live with no changes to your code.  Switching wouldn’t make sense depending on how advanced your current setup is and/or you want some of the features.

*Expert response by liam*

*Asked 5 times*

---

## Q: So a question to the pro’s please

**A:** So once you have your data (in sample and out of sample etc)..its useful to tweak existing strategies etc I’ve used this lately with some good success (even found a brand new strategy too)

*Expert response by PeterLe*

*Asked 5 times*

---

## Q: In response to the question : summarise the key points from the book - efficiency of racetrack betting markets by william T Ziemba and which is the most optimal strategy:

**A:** "Efficiency of Racetrack Betting Markets" is a book by William T. Ziemba and Donald B. Hausch that provides a comprehensive analysis of the betting markets in horse racing. The book examines the efficiency of these markets and explores various strategies for betting on horse races. Here are the key points from the book:

*Expert response by PeterLe*

*Asked 5 times*

---

## Q: I wasn't planning on doing this but I decided on Monday to also compare `Strategy0`'s live bets to the backtest and discovered some big problems with my execution which meant I'd missed out on - very roughly - about 15,000 bets over the past three months. This was largely down to handling the start of races and using the `marketStartTime`. I've completely overhauled the logic and it appears to have fixed things. I made a separate tweak that should also help reduce the number of missing bets but, checking that now, it's been somewhat less successful

**A:** Right, back to `Strategy2`. I've definitely made significant improvements to the model over the past week but none of the changes have translated into a meaningful shift in backtest performance. Intuitively, where the model is strongest it must just be agreeing with the market. However, I did have a small breakthrough last night with the filters I'm applying to try to avoid adverse selection and I think the strategy is just about at the stage where I'm happy to start live testing it again today. I don't think the backtest performance is quite good enough but the thing that convinced me it's worth live testing is that I can run it against many more markets than I have scraped prices for - i.e. all of the `OTHER_PLACE` markets. As in my last update, I can use BSP to quickly assess whether it's actually finding value on those markets. The breakthrough I'm referring to should apply to pretty much any taker strategy so I'm excited to apply it to other strategies

*Expert response by Unknown*

*Asked 5 times*

---

## Q: Big [https://forum.developer.betfair.com/filedata/fetch?id=32354|changes](https://forum.developer.betfair.com/filedata/fetch?id=32354|changes) in transaction charges

**A:** Over the years, the Exchange has processed an increasing number of transactions at an ever-increasing cost to infrastructure and stability.

*Expert response by liam*

*Asked 4 times*

---

## Q: The `Market` object has a helper method for accessing other linked event markets (live and simulated):

**A:** This allows you for example to backtest win/place in racing or all football markets as per live, this also only seems to add around 5% in processing time. I don't think there is anything else out there on the market which allows backtesting like this :sunglasses:

*Expert response by liam*

*Asked 4 times*

---

## Q: Would you say this was a reasonable test?

**A:** Just putting aside the other benefits of running on AWS, If speed to market is the main important factor is AWS worth it?

*Expert response by Unknown*

*Asked 4 times*

---

## Q: [@UUX1L88MC](@UUX1L88MC) - rust beginner question, I am trying to build the package from source. I have cloned it and am running `maturin develop` and get this error:

**A:** Caused by: Cargo metadata failed. Does your crate compile with `cargo build`?

*Expert response by Mo*

*Asked 4 times*

---

## Q: flumine v2.0.0 now released, this has a few breaking changes 99% around naming (Backtest-&gt;Simulated) hence the major version bump (over 2yrs since v1!) but now allows multi clients/exchanges, see [https://betcode-org.github.io/flumine/clients/|docs](https://betcode-org.github.io/flumine/clients/|docs) on how to use. Also added a rough [https://github.com/betcode-org/flumine/blob/master/examples/example-betconnect.py|example](https://github.com/betcode-org/flumine/blob/master/examples/example-betconnect.py|example) on using the BetConnect client.

**A:** I have been testing for a few weeks now and I believe it to be bug free, any issues are likely to be around simulation rather than live due to the changes but let me know if you spot anything.

*Expert response by liam*

*Asked 4 times*

---

## Q: 1. If you’re making rather than taking, and your prices are more than 1-2 pips away from each other (back/lay spread on US racing can be very broad), someone new could be doing the same strategy “inside” your prices. Can you go back and check what volume was matched at a price other than your own?

**A:** 2. Your hosting setup has changed. Data centres get new links, retire old ones, your VPS could now have a noisy neighbour sucking bandwidth, and so on, and so on. Doesn’t take much to add 10ms latency onto a box. Even worse if you’re running from home (residential broadband especially over OpenReach makes no guarantees about anything, ever)

*Expert response by Paul*

*Asked 4 times*

---

## Q: I don't understand how this error could (repeatedly) happen when I check to ensure the order is EXECUTABLE before cancelling (logs for one example attached, I have had multiple instances of this today)?

**A:** (I do appreciate it will be an error on my side, I'm just completely stumped as to what it could be), so any clues would be greatly appreciated!

*Expert response by Unknown*

*Asked 4 times*

---

## Q: When someone has some spare time, could help me out and show me how I could edit this code to make it work with multiprocessing so that these 3 loops are done at the same time to increase speed to colect the data?

**A:** I can create a question on stackoverflow if want. Any help will be most welcome!

*Expert response by Unknown*

*Asked 4 times*

---

## Q: Hi guys; I've noticed lately that my marketbooks are not being updated - I'm not sure what the problem is exactly, but in the log file the price is 11.5 where the actual price is 15.5.  It's the whole book, and it happened the other day as well. On a reboot of the program it's done the same thing again. Log files are showing old prices, with the book just not being updated.  What do I need to check to analyse the problem / what should I be on the lookout for?

**A:** I am running a beta version of my script to add untested strategy on the same ec2 instance, so there are multiple scripts pulling the data with the same address or whatever. I don't think there are any memory problems because it's happened again after I've checked that.

*Expert response by Unknown*

*Asked 4 times*

---

## Q: Well as you know I'm still learning how to use Python. From knowing nothing, it wasn't as bad as i thought to get the recorder and a few strategies running (the latter with help from others on here and your examples).

**A:** I've now started to build out from those initial strategies and 'bolt stuff' on. Its a really good way of learning by the way, by using the simulator to test code (if anyone else is a beginner)

*Expert response by PeterLe*

*Asked 4 times*

---

## Q: You're right that there are different approaches to database replication. The [https://dev.mysql.com/doc/refman/8.0/en/replication-solutions.html|MySQL documentation explains many of them](https://dev.mysql.com/doc/refman/8.0/en/replication-solutions.html|MySQL documentation explains many of them). But it's a pretty technical area and I wouldn't try to set it up and manage it yourself unless you're an experienced DBA (i which case why ask the question?).

**A:** The right solution absolutely depends on why you need a replicated database, so how others do it is pretty irrelevant. but since you asked, it's a standard feature of most cloud database services including AWS's RDS, which is how I do it, allowing me to focus on my trading apps and not get bogged down with irrelevant database issues.

*Expert response by Peter*

*Asked 4 times*

---

## Q: I've been chatting here with some people and I'm considering starting to use flumine in order to get around some issues I am having with the HTTPS client component that I currently use in my own setup. I've a question about the use of thread pools really. At times I will need to place bets across many distinct strategies in a way that they are all fired within as little as 1 millisecond of eachother. This causes the component I use a few problems the result being that my requests are queued in an opaque manner and I suffer placement latency.

**A:** When using a thread pool I'm trying to find out what the lay of the land is. Alternatively, if I write my own thread pool trying to find a best practice implementation based around the betfair API:

*Expert response by D C*

*Asked 4 times*

---

## Q: So my question is: How do you uncover what makes the ML model significantly better?

**A:** Is it by looking at (and trying to understand the individual decision trees (a subset off)

*Expert response by PeterLe*

*Asked 4 times*

---

## Q: [@U01PJ5YMFBJ](@U01PJ5YMFBJ) I started out by learning how to create the CSV  (using the price recorder) into Pandas DF's etc. (I know you are much more accomplished than me in terms of programming by the way)

**A:** The added in a couple more columns to include winner, P/L Sum of the books etc

*Expert response by PeterLe*

*Asked 4 times*

---

## Q: • Performance: The streamlined version I provided is likely to be slightly faster due to its simplicity and direct approach. However, the difference might be marginal depending on the implementation details of the helper functions you use.

**A:** • Applicability: If your codebase frequently deals with different data structures for market data or requires additional checks like the `Side.BACK` logic, your version could be more suitable despite the potential slight performance trade-off.

*Expert response by PeterLe*

*Asked 4 times*

---

## Q: [@U4H19D1D2](@U4H19D1D2) /All, So how might you go about doing this in practice? Lets say you had a laying system and one key variable you wanted to test (fill/kill).

**A:** If the Fill/Kill was too fast, (and it can be) you would miss opportunities and too slow you’d get taken to the cleaners.

*Expert response by PeterLe*

*Asked 4 times*

---

## Q: Setting the scene, the plan is to improve a live (profitable) strategy by optimising its current parameters (features) using ML.  This is going to be a learning exercise so if you have any questions / advice / criticism please get involved :wave:

**A:** The strategy is for TPD inplay racing, low stakes and taking Lay prices, market impact can be ignored for now. To keep things simple I am going to limit to Flat racing for the past 6 months, Jan-June inclusive, which gives around 1500 markets.

*Expert response by Unknown*

*Asked 4 times*

---

## Q: Question Please: As a relative beginner to Python, Im learning pandas (dataframes etc) and how to model data. I've used the price recorder to create some data in the form a of a CSV file..from my recorded markets..

**A:** Then I'm using sklearn, LinerRegression, seaborn etc...

*Expert response by PeterLe*

*Asked 4 times*

---

## Q: Haven't given up, after exploring a few algos I found that using XGBoost seemed to be the most applicable / get the best results in terms of accuracy on the problem I was trying to solve. Using my current prediction I used the algo to predict the error (delta), from my understanding this is a common technique (does it have a name?) and proved to be far more accurate than starting 'fresh'.

**A:** Had a few issues with latency when simulating using the sklearn integration as its considerably slower compared to using the low level [https://xgboost.readthedocs.io/en/stable/python/python_api.html|library](https://xgboost.readthedocs.io/en/stable/python/python_api.html|library).

*Expert response by Unknown*

*Asked 4 times*

---

## Q: Second related question: what is your workflow for going from idea to live trading strategy? Mine is usually:

**A:** 1. Get told about an idea ([@U012XF5CNPN](@U012XF5CNPN) leaking alpha) or reading about one (in a book that [@UPMUFSGCR](@UPMUFSGCR) has dismissed out of hand)

*Expert response by Mo*

*Asked 4 times*

---

## Q: First up, as mentioned in my [https://betcode-org.slack.com/archives/CTPL3R3FU/p1736081164005719|last post](https://betcode-org.slack.com/archives/CTPL3R3FU/p1736081164005719|last post), I increased stakes on `Strategy0` and `Strategy1` on Monday (2025-01-06). My plan is for these to increase in line with the notional bankroll I have set aside for this collection of personal strategies, and for this bankroll to grow organically. If I find a strategy that I'm extremely bullish on and think it could benefit from an injection of capital then I will obviously do so but that's not (yet?) the case for `Strategy0` or `Strategy1`.

**A:** So, `Strategy2`. I've been alternating between thinking I've cracked it and thinking all I have is a horribly overfit hot mess. I started off very quickly making progress in overhauling the model and staking which:

*Expert response by Unknown*

*Asked 4 times*

---

## Q: My questions are as follows:

**A:** 1. Is the model shite and can/should it be abandoned now based on attached numbers

*Expert response by Unknown*

*Asked 4 times*

---

## Q: Also at the meetup, [@U05SRUKGYCC](@U05SRUKGYCC) made some comments that gave me some perspective on `Strategy2`. It helped cement my feeling that it's not contrarian enough and I need to revert to the original vision of the strategy. I've started work on a third iteration of it with promising signs. I had really hoped I was going to be able to report today that I'd gone live with _both_ `Strategy2` and `Strategy3` this week but sadly not quite there yet

**A:** Existing strategies got absolutely crushed this week and that unfortunately coincided with it being my turn to run them. My already considerable shortfall is now even larger. Although they've been running for years, variance like this is still stressful when you're personally making the losses even if it all gets accounted for. However, these emotional factors are easier to handle being part of a group that can provide perspective and shared experience

*Expert response by Unknown*

*Asked 4 times*

---

## Q: A few days ago I posted on "issues" about a question I have in relation to the values ​​provided by `tradedVolume`, because I want to follow the matches, seeing the movement of the market with each request I make, easily indicating how much in *Back* was transacted between the requests in how much in *Lay* it took to match.

**A:** [@U9JHLMZB4](@U9JHLMZB4) helped me to better understand the calculations but I decided to put a complete example so that if there is still an error in what I'm doing, it's easier to see the problem.

*Expert response by Unknown*

*Asked 3 times*

---

## Q: Now is the view I want to have of the separate values ​​correct?

**A:** I understand that it is a simplistic view because there are more details that must be taken into account (such as, for example, there is no way to know if it was a single transaction that corresponded to the entire amount or if there were multiple ones) but I want to create a follow-up just to help me to visualize in more detail the financial movement of the market in each odds.

*Expert response by Unknown*

*Asked 3 times*

---

## Q: [@UBS7QANF3](@UBS7QANF3) when you get a second can you try issue373 again on your machine? With a small change required on the listener I am getting the following (same file)

**A:** ```listener = StreamListener(max_latency=None, lightweight=True, debug=False, update_clk=False)```

*Expert response by liam*

*Asked 3 times*

---

