# Betfair News Knowledge Base

*Generated from Slack chat history - 125 technical conversations*

---

## 2021-10-21

**Unknown** - *10:44:57*

set the channel description: Post your questions here directly to Betfair on any Betfair Exchange related topic

*Tags: General Technical*

---

**Neil T (Betfair)** - *10:46:40*

*Post your questions here directly to Betfair on any Betfair Exchange-related topic.* 

 

*Moderation &amp; Etiquette*

*·*        Replies to a single question will be confined to a single thread and any follow-up question (on the same topic) should be posted in the same thread.

*·        DO NOT* provide your Betfair username or email address in any correspondence. 

·        Any specific Betfair account-related queries should be directed to the usual Betfair Customer Services or Betfair Developer Support channels.

·        Betfair will respond directly to the channel (Monday-Friday 10am-5pm).  

·        The channel will be open until 1700 on Thursday 28th October

*Tags: General Technical*

---

**Mo** - *11:39:06*

Would you be open to sharing actual production code for certain pieces of functionality? Specifically I am thinking:



1. Order book virtualisation

2. Projected SP calculation (near and far)

I'm working on the virtualisation myself and even knowing the answer I should be getting by cross-refencing the virtual and non-virtual price streams, it is very challenging to reproduce exactly. There are too many questions around e.g. how you handle rounding of stakes at various steps in the process

*Tags: Deployment*

---

**Mo** - *11:44:52*

Does anyone actually purchase PRO historic data more than three years old?



If you made this freely available I think it would be great for attracting more automated bettors and for the exchange ecosystem.



Data science and machine learning are very popular skills to learn right now and people are always looking for good free data sets on which to apply and develop their skills

*Tags: General Technical*

---

**Mo** - *12:24:13*

Thanks Neil. Fair enough if there is indeed interest in this older data. I take your points but just wanted to highlight a couple of things I think we (as the "cyberpunks") consider canonical:



1. Anything other than PRO is a waste of time

2. You need at least a year's worth of data to have confidence in a strategy

So although there are some free months of PRO available, I would still argue for a contiguous year - and not one that was affected by COVID!



(I realise - mainly through the hackathon participation - that there is still a demand for ADVANCED data from Harold)

*Tags: Strategies*

---

**Oliver Varney** - *12:57:55*

*Derivative style products on the exchange (Apologies for the long winded question / paragraph im not sure the best way to phrase this):*

*[@UNW8Q88EL](@UNW8Q88EL)* I think ive mention this to you at the meetups.



Sports like horse suffer from largely inactive markets apart from big meets, up until very close to the off (like the last 5 mins). The exposure imbalance of laying vs backing is a big contributor to this. Why would someone who is willing to lay a horse at 100 lock up all that exposure for large amount of time (lets say 2+ hours) with the current betting products we have available to us. This is probably one of the reasons you are forced to market make and the early markets are dire.



Furthermore there is a large "trading" community out there that mainly care about "trading" the price difference and want no exposure on the result. These "traders" are currently getting screwed over when the exchange goes down as they cant ditch their exposures and there is no voiding under the current exchange rules.



These two reasons combined scream out for a betting option more akin to a contract for difference (CFD) from the finance world.



*Is Betfair thinking about / would betfair consider something like this?*



Thinking about horses, I could see a massively popular product being a CFD style contract where the final value comes from the entry price being settled to BSP, thus only requiring one trade instead of the current two (entry + hedge). Users could also trade in and out of this contracts similar to current hedging with actual bets. In combination with a stop loss settlement mechanism, whereby the entry price is compared to the current market price, we could improve the imbalance of lay side exposure vs back side.



With the example of laying at 100, a CFD contract could be striked with an entry price of 100, closing price of whatever BSP is, and an automatic stop loss settlement if the current market price goes below 10 lets say. In this example the lay side would only require 10x exposure instead of 100x exposure due to the maximum loss being ten times smaller.



A product like this could lead to much more active markets and could boost volumes offered and matched.

*Tags: Strategies*

---

**Neil T (Betfair)** - *13:23:22*

Hi [@U4H19D1D2](@U4H19D1D2), you are correct.  See the following from the Betfair terms and conditions that answers this question in full.

*Tags: General Technical*

---

**Neil T (Betfair)** - *13:23:36*

*Section 1: Betting - General Conditions*

Betfair provides a platform upon which you can enter into various betting transactions in relation to the markets available on our site ("Markets").

Where customers bet with each other on the Exchange, Betfair acts as a facilitator and does not act as a counterparty. However, Betfair may act as a counterparty on the Exchange but only in the following limited situations:

• for wagers between Australasian Customers. Betfair also offers Tote bets, as well as singles (which we call "˜Fixed Odds") and "Multiples" bets at odds fixed by us.

• for Betfair's Starting Price ('SP' or 'Betfair SP') on the Exchange. The Betfair SP is calculated by Betfair, by balancing all SP bets and other Exchange bets when the market is suspended at the 'off' of the relevant event. Betfair group may act as risk counterparty to SP bets if necessary to ensure a fair SP. The Betfair personnel involved in determining the SP in such circumstances will have no undeclared personal or other interest in the SP in question. When you place a bet at SP you are betting against other Betfair customers. However during the reconciliation of the Betfair SP, Betfair acts as counterparty in order to balance liabilities between Betfair SP bets and other Exchange bets; and

• occasionally (and such bets represent a tiny fraction of the overall volume of betting activity on the Exchange), in one of the two following circumstances:

    ◦ on less liquid markets to improve “liquidity” and stimulate market activity (“liquidity” is the amount of money available for you to bet on each selection). We may do this on ancillary markets (particularly when the market is first made available) or on markets on less popular events. The rationale for providing this liquidity is to enhance the betting proposition for our customers; and

in order to reduce the Betfair group’s liability against a particular outcome. We may do this on a high-profile event where our sportsbook has a very large exposure to that outcome.

*Tags: Errors Debugging, Strategies*

---

**Neil T (Betfair)** - *13:53:12*

Hi [@UBS7QANF3](@UBS7QANF3) - we wouldn't share the production code for this functionality.  We have a couple of articles that explain how we &lt;http://(https://docs.developer.betfair.com/display/1smk3cen4v3lu3yomq5qye0ni/Additional+Information#AdditionalInformation-VirtualBets)|virtualize bets&gt; and how [https://promo.betfair.com/betfairsp/FAQs_detailedWorkings.html|Near and Far prices are calculated](https://promo.betfair.com/betfairsp/FAQs_detailedWorkings.html|Near and Far prices are calculated) (appreciate that you may be already of both of these.

*Tags: Deployment*

---

**Oliver Varney** - *15:31:50*

sweet cool and you raise good points! I would be very open for community ideas long these lines to up volumes. Bankroll can be the limiting factor for users, so any product type that allows a similar effect but more effective use of capital is a tick in my book.

*Tags: General Technical*

---

## 2021-10-22

**AndyL** - *00:06:22*

A good explanation by your chief architect here: [https://youtu.be/tyhx3FNCogA|https://youtu.be/tyhx3FNCogA](https://youtu.be/tyhx3FNCogA|https://youtu.be/tyhx3FNCogA)

So it looks fairly clear Kafka is not the problem, Kafka currently fronts the Stream API, but the Order Input Handler and Order Processor modules are still native monolithic Oracle DB programs, which he highlights is a current problem they are working to replace with a Kafka solution. That sounds like WIP... but looks to be heading in the right direction. Im not surprised having watched this video. The responsive slow down ive heard people report immediately prior to an outage probably points at those DB order processor apps.

Good luck with the Kafka migration for those.

*Tags: Performance*

---

**George** - *10:47:39*

Would Betfair be willing to provide accurate(ish - down to millisecond precision) internal timestamps in responses and in the stream?

1. When I send a bet in-play, for example in horse racing, I get a 'pending' response, but this response doesn't include the timestamp that the order was received at the Betfair server. This timestamp must exist in order for Betfair's tech to know in which sequence all orders were received. It would be great to have this timestamp included in the pending response, so that I can measure my latency "from door to door" accurately.

2. On the market data stream we receive a 'publishTime' which is presumably the time at which the matching engine cycle finished. It would also be useful to have a field that represents the time at which the matching engine cycle began. This would enable me to look back at the logs and say: OK, my order didn't arrive in time to make it into this matching cycle which began at T1, so it was delayed a bit longer and had to wait for the next one, which began at time T2.

*Tags: Performance, Deployment*

---

**Neil T (Betfair)** - *11:07:41*

Hi [@UBS7QANF3](@UBS7QANF3) - yes it is possible for a bet to be placed if a TIMEOUT occurs.  See the below guidance from the API docs regarding this - _"The order timed out &amp; the status of the bet is unknown. * *If a TIMEOUT error occurs on a *placeOrders/replaceOrders* request, you should check *listCurrentOrders* to verify the status of your bets before placing further orders. *Please Note:* Timeouts will occur after 5 seconds of attempting to process the bet but please allow up to 15 seconds for a timed out order to appear. After this time any unprocessed bets will automatically be Lapsed and no longer be available on the Exchange."_

*Tags: Errors Debugging*

---

**thambie1** - *11:36:36*

If there were mass adoption of CFD it would increase incentives to manipulate market prices for the purposes of manipulating CFDs. It would exacerbate the problem. Spoofing is problematic, but has nowhere close to the same level  of impact. With CFD manipulation you have a customer who may make a reasonable bet, but gets shafted after the fact due to manipulation. The customer has no way to mitigate this problem, and thus the offering itself is fundamentally flawed. CFDs are an interesting idea, but with the fractured liquidity due to so many sporting events (as opposed to fewer stocks/currencies/etc), I don't think it can work.

*Tags: General Technical*

---

**Newbie99** - *15:40:30*

A while back there were a few users on here that got blocked and didn't seem to know why, obviously Betfair have certain legal obligations that can't be avoided and have to adhere to these, but aside from that, when permissible by local laws (i.e. when its not AML related basically), it would be good if users were given a warning if their betting behaviour would be likely to cause them to be blocked (e.g. an e-mail warning saying you are making an excessive number of REST API calls without placing sufficient bets or something to that effect).



In essence it would hopefully be mutually beneficial to allow people to change behaviour, rather than taking the nuclear option and closing down accounts without warning.



I should stress I have no idea what actually happens/happened in these situations personally, I'm just going on what people have posted.



So I guess the question is, would it be possible to have a slightly more formalised / structured approach to this type of occurrence to provide piece of mind that no-one is going to get shut down without just cause?

*Tags: Deployment, Strategies*

---

**George** - *16:22:49*

Hi [@UNW8Q88EL](@UNW8Q88EL), thanks very much for getting back to me with this impressively comprehensive response, which is much appreciated, and thanks again for this initiative which is brilliant I think we all agree.

A few things come to mind:

• I probably phrased question 1 in a misleading way. I didn't mean to sound as if I was asking about asynchronous orders. I am really just interested to know how best to measure latency from door to door - and I am sure others would be too. Your thoughts on that would be greatly appreciated.

• Something like placedDate is _*possibly*_ what I am looking for, and I should have mentioned it as a possible solution. However, it currently doesn't help because it seems to be rounded to the nearest second or at least doesn't display any precision further than that at all, which is frustrating.

• Furthermore, even if placedDate was a millisecond-precise quantity it's not entirely clear (to me) what the meaning of this value actually is. Does it describe the time that the order arrived at Betfair's servers, or does it represent the time that the order was considered by the matching engine perhaps?

• In terms of question 2, I suppose what I am really after is a way to figure out exactly how much slower my order was than the one which got the fill that I wanted. Let's say a horse falls and I want to be the first to lay it. So I send a LAY order to Betfair, but it doesn't get filled, because someone else was faster. It's pretty hard in this situation for me to know whether I "lost" the race for liquidity by 1 millisecond or 200 milliseconds. I can look at the publishTime of the stream update which shows the successful order, but there's no way to track that successful order backwards in time to know what time it arrived at Betfair's server compared to what time my order arrived. I was just thinking that, if I knew how long the specific matching cycle in question had taken, that would enable me to work backwards and make a good estimate of when the successful order arrived. And, if I also had a good idea of what time my order arrived, then the difference between the two represents how much I lost the race by. 

• If I'm going to lose the race by 200ms then I may as well give up; if I'm mostly losing by 20ms then I should probably carry on trying and maybe invest in some better technology!

*Tags: Performance, Deployment*

---

**liam** - *16:47:57*

Ok, from my side it would be helpful to know what wrong so that I can better prepare for something similar. From writing tests to changing logic to make code more resilient, often things break but can be hard to fix/replicate after the fact due to not even knowing what caused it 

*Tags: Errors Debugging*

---

**Neil T (Betfair)** - *16:52:55*

There is room for a more in-depth &amp; definitive technical article on this, so I’ll see if our dev team will consider writing something to be included on our Technology blog ([https://ppb.technology](https://ppb.technology)). We might not be able to provide the full and more explicit technical details you want though :slightly_smiling_face:



In the meantime, here’s a high-level summary:

 

• For performance reasons, all bet matching takes place in a bulk betting matching cycle, each of which takes ~100 m/s. 

• All bets within a single cycle are queued (matched/unmatched) on a FIFO basis. 

• Cross-matching occurs both at the market and event level. 

• There is no concept of exactly the same time, one bet will always be picked up before another even if one is microseconds before the other.



*Tags: Performance, Strategies*

---

## 2021-10-25

**Neil T (Betfair)** - *16:21:09*

Hi [@UCQB6S222](@UCQB6S222)



Thanks for clarifying your points. You can measure network latency to the edge of the Betfair infrastructure using well-known techniques (traceroute, ping, etc) based on the endpoints that we provide ([http://api.betfair.com|api.betfair.com](http://api.betfair.com|api.betfair.com)). For any API request, the difference between the HTTP request and response time (available as an HTTP header) will provide an indication of the total round trip time. 



placedDate is the time that the order arrived at the Betfair servers for processing at which point the bet will be placed (matched/unmatched) or subject to the in-play delay, if applicable, before being placed. Within the above parameters, you only have the potential to control the latency between your machine and our infrastructure. Once your request is received, you are subject to the speed at which the bet is processed within our matching engine. This itself may vary around the ~100m/s processing time.

*Tags: Performance, Deployment*

---

## 2021-10-26

**George** - *08:53:49*

Agreed, I think a millisecond-precision version of placedDate would be of great help to anyone with even a passing interest in optimising their speed.

*Tags: Performance*

---

**George** - *12:00:58*

Thanks. There's no doubt that cross-matching is a fine idea. The problem is the way that it has been implemented.

In the example given, if the Back Player A bet at 1.32 was 'converted' (e.g. within the matching engine) into a Lay Player B bet at 4.1 then Betfair doesn't need to stand in the middle as a counterparty, and there's absolutely no rounding done at all. I can't think of anything simpler than that?

No manipulation possible in that scenario whatsoever.

No need for Betfair to stand in the middle as a counterparty.

This is how cross matching (or rather "implied liquidity") is done on every financial exchange.

*Tags: General Technical*

---

**Newbie99** - *13:14:12*

Are there any plans to improve data harmonisation across markets? Not a massive problem for horse racing, but sometimes the runner names on other sports can mismatch (e.g. Man Utd. or Manchester United or Man United and so on). Would there be any possibility of looking at a solution to standardise naming conventions at least for the more frequent runners?

*Tags: General Technical*

---

## 2021-10-27

**Neil T (Betfair)** - *15:31:08*

Hi [@UFTBRB3F1](@UFTBRB3F1) - the ops teams a very aware of the problems this can cause and do already have manual checks in place to help maintain consistency.  The vast majority of these issues are the result of differences in the naming conventions used across third-party feeds; many of which are used for automated market creation.  Such inconsistencies are typically corrected at our side with reference to our internal list of id's but some do still slip through the net.

*Tags: General Technical*

---

## 2021-10-28

**Neil T (Betfair)** - *14:09:39*

Hi [@UFTBRB3F1](@UFTBRB3F1) - I've raised this request to the Exchange Ops team and will let you know what can be done here.  It would make sense to offer a no-reply email address so that error notifications can be sent directly to our Ops team

*Tags: Errors Debugging*

---

## 2021-10-30

**Michael** - *12:16:17*

Well this went well. I was wondering if we might get an influx of new posters from one of the other forums (like the one where they don't believe in value and can't afford pies) asking questions about PC and why they got banned when they totally can afford their losses (which are just a temporary blip) but either that didn't happen or there was frantic behind the scenes moderating so kudos to all involved.

*Tags: General Technical*

---

## 2021-11-01

**Neil T (Betfair)** - *10:22:16*

Hi [@U01U24AG35W](@U01U24AG35W) - See the answer from our API dev team -  "_This would be an artefact of settlement kicking off that moves the bets away from trading db into the longer-term store. Any price change notifications triggered during this process will result in attempts to reconstruct the market view based on no bets being available and would result in this kind of notification being sent. There is no straightforward way to suppress this end of market clear-out messages, so not sure yet how to signal this to customers. It can be classified as a bug, but it’s a behaviour that has existed for some time. We'll have  a think about if there is a definitive way to stop this or at least signal it appropriately to customers"_

*Tags: Errors Debugging, Strategies*

---

## 2021-11-02

**Neil T (Betfair)** - *10:46:09*

HI [@UFTBRB3F1](@UFTBRB3F1) - I have received an update from our Exchange Ops team and although they understand why this would be useful, they have no plans to introduce a direct contact address for customers.  The current process ensures that any contacts regarding errors (etc) are logged and monitored through our CRM system.   If you contact CS Chat via *[https://support.betfair.com/app/home/](https://support.betfair.com/app/home/) &gt; Get In Touch* the team should report any issues directly to the relevant Exchange Ops team.   Also, feel free to contact [mailto:BDP@betfair.com|BDP@betfair.com](mailto:BDP@betfair.com|BDP@betfair.com) (Monday-Friday) if you notice any market-related issues.

*Tags: Errors Debugging*

---

## 2021-11-13

**V** - *18:02:49*

When will the next AMA be? I think the format is pretty good here… the questions and answers were pretty insightful imo 

*Tags: General Technical*

---

## 2022-03-28

**Neil T (Betfair)** - *15:10:06*

Hi [!here](!here) - just giving everyone advanced notice of the Ask Betfair Anything session from 29th-31st March - see full details below, format the same as last time.  Please feel free to post questions in advance!  Thanks Neil

*Tags: General Technical*

---

**Neil T (Betfair)** - *15:10:14*

Post your questions here directly to Betfair on any Betfair Exchange related topic.



*Moderation &amp; Etiquette*



• Replies to a single question will be confined to a single thread and any follow up question (on the same topic) should be posted in the same thread.

• DO NOT provide your Betfair username or email address in any correspondence. 

• Any specific Betfair account related queries should be directed to the usual Betfair Customer Services or Betfair Developer Support channels.

• Betfair will respond directly to into the channel (Tuesday-Thursday 10-5pm). 

• The channel will be open until 1700 on Thursday 31st March.

*Tags: General Technical*

---

## 2022-03-29

**Mo** - *12:02:38*

Can the historic data API error messages be improved? A lot of the time when someone comes here with a problem it's hard to tell if they're doing something wrong - like passing in invalid arguments - or if the API is just being its usual flakey self

*Tags: Errors Debugging*

---

**Mo** - *12:09:24*

Have you ever considered more sophisticated security settings? For example:



• Only allowing API access from specific IP addresses

• Generating access keys with specific permissions. e.g. generate a key that only allows read access to the account statement endpoint. This key can then be used by a reconciliation application without it being an attack vector for placing bets

The use of certificates seems an oddity compared to other APIs both financial (e.g. Binance, IG Index) and not (e.g. AWS). They seem to be a bit of a pain point with new users, especially those on Windows

*Tags: Deployment*

---

**Neil T (Betfair)** - *12:09:41*

Hi [@UBS7QANF3](@UBS7QANF3),  yes, we can get something added to the historical data dev backlog for this.

*Tags: Data Quality*

---

**Alessio** - *13:44:43*

Is there any chance we'll get to enable buying historical data on regional exchanges like the Italian one?

*Tags: Data Quality*

---

**Neil T (Betfair)** - *14:06:32*

We made some changes to the non-interactive login documentation towards the end of 2021 to help improve the onboarding experience

*Tags: General Technical*

---

**Mo** - *14:09:33*

I think you need to add a line in the XCA documentation to make sure the signature algorithm is SHA 512 - see this thread for background: [https://betcode-org.slack.com/archives/C4H05ML2E/p1647009507466239](https://betcode-org.slack.com/archives/C4H05ML2E/p1647009507466239)

*Tags: General Technical*

---

**Neil T (Betfair)** - *14:14:06*

Hi [@U011VL3CA2Y](@U011VL3CA2Y) - thanks for the question, i'll come back to you on this as soon as I have further info

*Tags: General Technical*

---

**Neil T (Betfair)** - *16:44:58*

When we initially launched the service back in 2017 data for all Exchanges (.com, .it and .es) was recorded and packaged as part of each monthly file on [https://historicdata.betfair.com/](https://historicdata.betfair.com/). However, due to time constraints, a dedicated historical data site for Spain and Italy was out of scope. The .es and .it data was subsequently purged from the existing published files to reduce complexity and the overall size of the stored files.

*Tags: Data Quality*

---

**Alessio** - *17:04:25*

Thanks [@UNW8Q88EL](@UNW8Q88EL). That's unfortunate indeed. Is there anything that could help Betfair be interested into restoring recording? Say, a 10-20 people set willing to buy? I believe from a UI/localization point of view a dedicated site is probably not necessary.. if you are interested into these piece of data, your english is usually reasonable :wink:

*Tags: General Technical*

---

**Alessio** - *17:37:23*

From my point of view, and I believe i'm not the only one, I think the most useful historical data stretches up to 2-3 years in the past., not more

*Tags: Data Quality*

---

## 2022-03-30

**Neil T (Betfair)** - *16:26:59*

Hi [@U4H19D1D2](@U4H19D1D2) - this was on the roadmap several years ago and we got fairly close to doing it before it was de-prioritized in favor of other projects.  There was also subsequent conflict between offering this as a service and a separate historical data service post settlement.

*Tags: Data Quality*

---

**liam** - *16:32:39*

I assume it's now completely off the roadmap? I imagine it has an overlap with the historical data sales.



I have been thinking about adding the private graphs endpoint to bflw, will that cause any 'issues'?

*Tags: Data Quality*

---

**Neil T (Betfair)** - *16:37:47*

Yes, its off the roadmap, the main priorities are further feed integrations, passive bets work.  There's too much cross over with historical data sales and again, hard to determine real benefits

*Tags: Data Quality*

---

## 2022-04-01

**Neil T (Betfair)** - *10:08:12*

Morning [@UUE6E1LA1](@UUE6E1LA1) - This isn’t something under consideration. The main reasons for this are lack of liquidity, the practicalities of managing it accurately and picture latency. Many greyhound races are largely determined by what happens in the first second or two after the traps open so it isn’t something which lends itself easily to Exchange in-play betting.

*Tags: Performance, Strategies*

---

## 2022-05-11

**KG** - *09:21:23*

hey [@UTYFXUKRB](@UTYFXUKRB) shoot an email to [mailto:automation@betfair.com.au|automation@betfair.com.au](mailto:automation@betfair.com.au|automation@betfair.com.au) and we can help you out :)\

*Tags: General Technical*

---

## 2022-05-15

**PATTY BET** - *15:33:21*

hi guys, pretty new here. i'm currently using the python betfairlightweight library for some testing... how can i add more markets to streaming?  I mean, using the example on streaming how can i subscribe/unsubscribe to markets when a particular event occurs? Thank you for your time

*Tags: General Technical*

---

**PATTY BET** - *16:04:41*

for example... now i place a bet and maybe 5 min from now i place another limit order... how can i subscribe to streaming based on my changing bets?

*Tags: General Technical*

---

**Mo** - *16:23:14*

That requires you to subscribe to the order stream as opposed to the price stream if I've understood the question correctly. Or are you asking how to subscribe to markets on the price stream on which you have placed bets?

*Tags: General Technical*

---

**PATTY BET** - *16:37:53*

Order stream returns real live data of my current orders? My needs is to adapt the examplestreamingerrhandling.py to subscribe to new markets where i place bet on. if now i place a limit that excute correctly i need to track real time data to protect or cashout. i don't know if i'm clear enogh. thank you anyway for trying to understand.

*Tags: Deployment*

---

## 2022-05-25

**Alvin** - *11:17:13*

hello everyone, I'm new here, I wanted to know what's the best sample code to use when making a bot in python,  I've seen there's the Betfair sample code and then betfairlightweight library and Betfair.py, which one is best?

*Tags: General Technical*

---

**Newbie99** - *11:20:28*

Firstly, welcome aboard!



For Python, your best bet is to start here:



[https://github.com/betcode-org/flumine/tree/master/examples](https://github.com/betcode-org/flumine/tree/master/examples)



If you're not planning to use streaming data then you can try BFLW without Flumine:



[https://github.com/betcode-org/betfair/tree/master/examples](https://github.com/betcode-org/betfair/tree/master/examples)



and then any questions, ask away (this thread is only monitored by Betfair on specific dates, so you may be better off posting in one of the other threads btw).

*Tags: General Technical*

---

## 2022-05-27

**Wilcox** - *05:41:46*

Hey guys, I am new here. What is the best way to convert historical data to a csv file? The data is from BASIC tier 

*Tags: Data Quality*

---

**liam** - *08:27:57*

It's just betfairlightweight underneath 

*Tags: General Technical*

---

**Wilcox** - *23:53:59*

Thanks, It will be handy but the documentation is incomplete

*Tags: General Technical*

---

## 2022-05-28

**thambie1** - *09:05:54*

I had this problem with a different company. I took a screenshot of my Revolut card, they accepted that.

*Tags: General Technical*

---

**Mo** - *10:19:14*

I'm happy to add any documentation if you can be more specific



Check the docstring for prices_file_to_data_frame if you haven't already 

*Tags: General Technical*

---

## 2022-06-09

**Cez Klimczuk** - *13:43:41*

Hey guys, I'm a newbie to betfairlightweight - I was wondering what's the best way of obtaining market_ids from a given event? Of course I could find them using the navigaiton endpoint, but that's an overkill. I'm currently using the betting.list_events() function with a filter. But I do not know how to bridge this with betting.list_market_book(), which requires market ids as an input. What the best way to go about it?

*Tags: Strategies*

---

**Newbie99** - *15:41:20*

I think the way you're looking at it, you'll need to make 3 calls:



1. list_events() to get your desired events

2. list_market_catalogue() to get the required market details (including market_id) for your sub-set of events

3. list_market_books() to get the pricing info, for your subset of market_ids

You can of course write that into one function to make it easier and if you're going to be repeating the above frequently you can always switch to streaming to make life easier.

*Tags: General Technical*

---

## 2022-06-13

**Oliver Archer** - *11:54:23*

Hi all, potential noob question incoming.. I'm looking to write an automated trading script in Python that uses a scheduler to run every couple of minutes. I could run it on my local machine but ideally don't want to have to have my laptop on 24/7 so looking to move it to the cloud. I've previously written a similar automated script trading crypto through a Binance API using a combination of Kaggle notebooks and PythonAnywhere (followed a guide on Towards Data Science) but when I try to do the same using betfairlightweight I get a 403 error when logging in which I'm assuming is a result of the servers being based in the US. So question is, how would people recommend I move my script to the cloud? Would ideally like to use the Kaggle/PythonAnywhere route if at all possible given I'm paying for that already, but can sign up to something else if I have to! Thanks in advance!!

*Tags: Errors Debugging, Deployment, Strategies*

---

**Mo** - *12:02:46*

I don't know the details of the Kaggle notebook infrastructure or PythonAnywhere but best practice would be to host in AWS Dublin given proximity to Betfair servers

*Tags: Deployment*

---

**Oliver Archer** - *12:10:41*

Thanks, very helpful, will do some research on AWS :+1::skin-tone-3:

*Tags: Deployment*

---

**Steve** - *23:28:44*

Hey all! :slightly_smiling_face: I’m brand new here and I’m trying to figure out how much more I need to study before I should put together my first betting angle/model using statistics and data analysis. What exact prerequisite knowledge should I have before even attempting to do so? I’m specifically interested in doing Horseracing if that helps.

I’ve got a background in Math (studied Civil Engineering at uni) and I’ve studied Python for a few months now (was playing around with Selenium in Pycharm to automate work things) but not too confident on what I should be learning exactly from all the Python content out there. I’m just wondering what the next steps for myself are. I’ve watched a few tutorials on the Betfair Youtube channel and have had a look through a few resources that I think I should go through:

1. Learn Intro to Stats 110x - [https://learning.edx.org/course/course-v1:HarvardX+STAT110x+2T2021/home](https://learning.edx.org/course/course-v1:HarvardX+STAT110x+2T2021/home)

2. Learn how to use R - using [http://Datacamp.com|Datacamp.com](http://Datacamp.com|Datacamp.com)

I'm just trying to put together a learning curriculum for myself to give myself a realistic timeline, and I feel like there’s more to it than just what I’ve found as I don’t know what I don’t know, so does anyone have any suggestions? Also let me know if this question has been asked already as I couldn’t find a similar thread anywhere.

*Tags: Strategies*

---

## 2022-06-14

**Mo** - *08:59:38*

I agree with [@UGV299K6H](@UGV299K6H) but in the mean time some brief comments:



1. I think it's pointless to learn R if you already know Python

2. Domain knowledge is very valuable - i.e. how the Betfair API works, how betting in general works, how horse racing works. For example, the choice of modelling technique will be largely irrelevant compared to knowing the valuable factors to put into your model. I would prioritise learning these above anything you've mentioned

*Tags: Strategies*

---

## 2022-07-31

**Mo** - *20:56:11*

Not sure who this question is directed at but Betfair don't monitor this channel unless they are running an AMA event 

*Tags: General Technical*

---

## 2022-08-01

**Phil** - *10:18:47*

Hi [@U027P3N2WMQ](@U027P3N2WMQ) - Not something I can help with directly but I believe this is something customer services can assist with. You won't be able to have the limit removed entirely, but will likely need to provide evidence that a higher limit is within your financial means.

*Tags: General Technical*

---

## 2022-08-03

**Enodeg Enodoff** - *14:27:01*

Hi guys, I’m new here. Currently I try to use the python betfairlightweight library, and have a question.



Maybe someone knows how to use this library with session tokens.

I have a vendor app key and want to try to use this library to work with my user’s accounts. (Session token we got with Oauth)



For single user we use “trading” class, where we get access with username and pass, this is ok:

trading = betfairlightweight.APIClient(username, password, appKey)



But Can’t find where we can modify login endpoint, and headers for access only with users session token.



Anybody can help?



Thanks.

*Tags: Strategies*

---

**liam** - *14:29:22*

You tried setting it? Or do you need to modify the headers as well?



```trading = betfairlightweight.APIClient(username, password, appKey)



trading.set_session_token("asdfgh")



event_types = trading.betting.list_event_types()```

*Tags: Strategies*

---

**Enodeg Enodoff** - *14:34:37*

I want to use this library : Making API Calls On The Users Behalf



(documentation : [https://docs.developer.betfair.com/display/1smk3cen4v3lu3yomq5qye0ni/Vendor+Services+API#VendorServicesAPI-vendorwebapiVendorWebAPI](https://docs.developer.betfair.com/display/1smk3cen4v3lu3yomq5qye0ni/Vendor+Services+API#VendorServicesAPI-vendorwebapiVendorWebAPI) )

*Tags: General Technical*

---

## 2022-08-05

**moseley82** - *22:19:00*

Hi guys quick question, is it possible to stream BSP data for football the same way it is with horses?

*Tags: General Technical*

---

## 2022-08-10

**Brøndby IF** - *14:06:34*

Good morning everyone (good afternoon to the people of Europe)!



A few days ago I asked about keeping my code running on a server in Ireland and I live in Brazil, if that had a problem ([@U80AMMRKP](@U80AMMRKP) even commented to me that there were no problems). This morning I woke up with several access errors on the server and when I went to access the account manually, it asked me to change my password.



I contacted Betfair chat and they told me that there was an unauthorized IP access in Ireland. I argued that this IP and this access I knew, that it was from the server that I kept my code executing the access to the Betfair API.



At that moment the attendant started asking if I worked with Betfair, asked how I didn't know about the other emails or access to Betfair, told me he couldn't help, gave me a contact email and ended the service without even finishing answering my questions.



Has anyone ever experienced this? The attendant talked to me like I was a hacker or something, doubting everything I said.



Is it normal to have the password changed from time to time if we have a server in a different country to which we reside?

*Tags: Errors Debugging, Deployment*

---

**Douglas Hickling** - *14:29:54*

I was asked to change my password a least a few times over the course of 2 weeks when I (uk based) ran my system from Mexico. It went back to normal when I ran it back in the uk. Not sure if this is helpful, I didn't contact support 

*Tags: General Technical*

---

**Brøndby IF** - *14:37:42*

Yes [@U018QJ00C2G](@U018QJ00C2G), this information already helps me a lot because it's exactly the same thing that happened to me. Thanks!

*Tags: General Technical*

---

## 2022-08-13

**Pos** - *10:00:11*

Hi guys, I was looking at using the NPM package when connecting to the betfair api. However I noticed its fairly old. Do you recommend this? Thanks [https://www.npmjs.com/package/betfair-api-node](https://www.npmjs.com/package/betfair-api-node)

*Tags: General Technical*

---

**Mo** - *10:04:08*

Also doesn't look like the streaming API is implemented

*Tags: General Technical*

---

**Mo** - *10:11:10*

Because the vast majority of people here using the Python [https://github.com/betcode-org/betfair|betfairlightweight](https://github.com/betcode-org/betfair|betfairlightweight) package

*Tags: General Technical*

---

**Mo** - *10:21:43*

The second package you linked to for example says



&gt; Note: Current version does not support refreshing authentication tokens. This will need to be handled manually.

This is pretty basic functionality



It seems clear there is not a big community of javascript Betfair API users but there is a big community of Python users (you're in it)



We're not dogmatic about what language you code in - there are people on here that use C/C++, C# and other languages - but there is a huge amount of value to leverage in the off the shelf Python packages:



1. [https://github.com/betcode-org/betfair|betfairlightweight](https://github.com/betcode-org/betfair|betfairlightweight), the most cutting edge Betfair API implementation across all languages

2. [https://github.com/betcode-org/flumine|flumine](https://github.com/betcode-org/flumine|flumine), a fully featured trading platform built on top of betfairlightweight

and the community expertise you have access to if you're using something everyone is familiar with

*Tags: Feature Engineering, Strategies*

---

**D C** - *13:02:19*

I've got some raw nodejs scripts in  git repo [@U03TJKFLE8K](@U03TJKFLE8K) . It is not in package form but if you are good with JS then you might be able to use it as a base and improve it. My JS works but its quite rough. Not what you would call "production" standard. DM me if you want a link

*Tags: Deployment*

---

## 2022-08-15

**Unknown** - *17:08:59*

A few days ago I posted on "issues" about a question I have in relation to the values ​​provided by `tradedVolume`, because I want to follow the matches, seeing the movement of the market with each request I make, easily indicating how much in *Back* was transacted between the requests in how much in *Lay* it took to match.



[@U9JHLMZB4](@U9JHLMZB4) helped me to better understand the calculations but I decided to put a complete example so that if there is still an error in what I'm doing, it's easier to see the problem.



So an example without real values ​​(from odds 1.20) from this week's Liverpool game:



```[{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/listRunnerBook", "params": {"marketId":"1.200236669","selectionId":"56323","priceProjection":{ "priceData":["EX_TRADED"]}}, "id": 1}]```

*Request 1:*

`"tradedVolume":[{"price":1.2,"size":100}]`

Back liability: 100

Lay liability: 20

Total Matched: 100

Total Money Transacted on the Betfair System: 120



*Request 2:*

`"tradedVolume":[{"price":1.2,"size":300}]`

Back liability: 300

Lay liability: 60

Total Matched: 300

Total Money Transacted on the Betfair System: 360



*Request 3:*

`"tradedVolume":[{"price":1.2,"size":800}]`

Back liability: 800

Lay liability: 160

Total Matched: 800

Total Money Transacted on the Betfair System: 960

`------------------------------------------------------------`

So, let's say I want to register on the chart how much liability we had between:



_*Request 1 and 2:*_

Back liability: 200

Lay liability: 40

Total Money Transacted on the Betfair System: 240



_*Request 2 and 3:*_

Back liability: 500

Lay liability: 100

Total Money Transacted on the Betfair System: 600



Now is the view I want to have of the separate values ​​correct?



I understand that it is a simplistic view because there are more details that must be taken into account (such as, for example, there is no way to know if it was a single transaction that corresponded to the entire amount or if there were multiple ones) but I want to create a follow-up just to help me to visualize in more detail the financial movement of the market in each odds.



Otherwise, I want to create a real-time chart to see how much money traders will lose if their investment result is 100% negative.

*Tags: Errors Debugging, Deployment*

---

## 2022-08-18

**Akwera Junior** - *08:06:22*

I am looking for someone to help me with my project I am abit stuck and I need some assistance with react based website.

*Tags: General Technical*

---

## 2022-08-29

**Mo** - *14:09:45*

There's no official Betfair Slack group. You're messaging a channel that is used intermittently when Betfair run Ask-Me-Anything style events which they're not currently. Betcode is the name of an organisation that evolved out of the developer and users of the betfairlightweight and flumine Python packages. The new name reflects that we're not exclusively focused on Betfair

*Tags: General Technical*

---

## 2022-09-11

**Brøndby IF** - *21:19:16*

Values were collected via betfairlightweight at:



runners[0].selection_id (both were home teams in yesterday's match)

*Tags: General Technical*

---

## 2022-09-12

**Mo** - *06:10:59*

I don't think you should be relying on Betfair selection IDs for this purpose. Your database should have your own internal team ID and you should maintain a mapping between your team ID and Betfair's selection ID(s)

*Tags: General Technical*

---

**Newbie99** - *08:36:16*

[@UBS7QANF3](@UBS7QANF3) but in this instance wouldn't the result be the same?



If you have your internally mapped team here, Guadalajara which your own ID ABC this would be mapped to betfair 230909, but the problem here is that betfair have applied the wrong id from their end, so surely your mapping would still 'work' in the sense it would map 230909 to ABC and flag up the wrong team due to Betfair's error?

*Tags: Errors Debugging*

---

**Mo** - *08:41:12*

Internally you correctly have 2 teams, Guadalajara (MEX) and Guadalajara (ESP) with internal IDs X and Y. Both of these have selection ID 230909 in their lists of Betfair selection IDs (maybe Betfair uses others for these teams, I don't know)



As far as modelling is concerned, I don't think this needs to involve Betfair selection IDs at all



As far as reporting - yes you will need to account for this situation in your code if you want to do breakdowns by your internal team IDs. For example, do the breakdown by team and league



By all means this can be reported to Betfair but:



1. I wouldn't hold out hope that anything will be actioned

2. It doesn't change anything retrospectively

So IMHO the correct thing to do is still to be robust to Betfair's data issues

*Tags: Strategies*

---

**Newbie99** - *09:51:17*

So in effect matching internal team name A, internal team name B, fixture time &amp; league to the Betfair event name (I do something to that effect currently)?



However I then do an additional check on selection ID, so in the above case I would simply bypass this market.

*Tags: Errors Debugging*

---

**Mona** - *12:04:28*

Hi anyone knows how to filter football matches by league? like English Premier league etc, is there a field in the Betfair data that I can filter?

*Tags: General Technical*

---

**Newbie99** - *12:28:46*

*with the caveat that competition_id is stored within the market_catalogue in flumine, so you can create your own filter for example when check_market_book() is called

*Tags: General Technical*

---

## 2022-09-25

**Mick** - *12:10:06*

I got blocked once before for reading too much data whilst making too few bets and it was a painful and slow process getting unblocked so now I'm paranoid about getting blocked again. My data use/bet size ratio has improved very dramatically so that's not an issue anymore but there's a couple of things I've been doing recently that I wanted to check on. Firstly - I'm wanting to leave my trading unattended for hours and just for safety I'd like to take all but the bare minimum required cash in my account each day and put more back in the following day - we're talking a few hundred pounds. Would that cause a problem? Secondly, I've been trying a strategy of putting in a bet request above the market price and then gradually lowering it as race time approaches. But for programming simplicity it's actually easier to cancel and then make a new request (not sure if the API lets you change your requested odds anyway). So for any one horse I might make of the order of a dozen bets that get requested and cancelled before an order is accepted. The duration of any single requests is at least ten seconds. Might this cause me any trouble?

*Tags: Performance, Strategies*

---

## 2022-10-10

**Michael McGarry** - *12:24:36*

does anyone know how to tell which sport a market book refers to when working with data from 'Other Sports'? I'm trying to find historical data for darts matches differentiated by competition and can't see any field for 'sport' and when querying for historical data the sport field will only take 'other sports' as an input.

*Tags: Data Quality*

---

## 2022-10-12

**Neil T (Betfair)** - *16:56:31*

Hi *[!here](!here)* - just giving everyone advanced notice of an *Ask Betfair Anything* session from *19-21st October* - see full details below, format the same as last time. Please feel free to post any questions in advance!  Thanks, Neil

*Tags: General Technical*

---

**Neil T (Betfair)** - *16:57:37*

Post your questions here directly to Betfair on any Betfair Exchange-related topic.



*Moderation &amp; Etiquette*

• Replies to a single question will be confined to a single thread and any follow-up question (on the same topic) should be posted in the same thread.

• DO NOT provide your Betfair username or email address in any correspondence.

• Any specific Betfair account-related queries should be directed to the usual Betfair Customer Services or Betfair Developer Support channels.

• Betfair will respond directly to the channel (*Wednesday – Friday 10-5pm BST*).

• The channel will be open until *1700* on *Friday 21st October*.

*Tags: General Technical*

---

## 2022-10-19

**Neil T (Betfair)** - *11:38:53*

To receive downtime notifications you need to subscribe to the Developer Forums Announcements section ([https://forum.developer.betfair.com/forum/developer-program/announcements](https://forum.developer.betfair.com/forum/developer-program/announcements)) and opt to receive e-mail notifications - [https://forum.developer.betfair.com/help?q=notifications&amp;btnSearch=&amp;titleandtext=1&amp;match=any](https://forum.developer.betfair.com/help?q=notifications&amp;btnSearch=&amp;titleandtext=1&amp;match=any)

*Tags: General Technical*

---

**Neil T (Betfair)** - *13:07:51*

There's an outstanding question to be answered relating to this so have chased up

*Tags: General Technical*

---

## 2022-10-20

**Dave** - *22:10:54*

One thing I would love to have is some understanding of where my betting activity lies amongst the activity of other participants. E.g. a weekly email that includes stuff like ranking by total volume (percentile is fine), total time that you had the best back/lay in the market, a distribution of your market share etc. Perhaps in the form of a weekly personalized email. I'd love to understand how my volume / liquidity compares. I think this kind of thing could help drive up engagement too - any thoughts on whether it is something you could offer? The premium charges section could be a decent place for this kind of thing too.

*Tags: Strategies*

---

## 2022-10-21

**Neil T (Betfair)** - *15:06:40*

Hi [@U4H19D1D2](@U4H19D1D2) [@U02K1MG7YCA](@U02K1MG7YCA) - Exchange plans over the next 6-8 months are focused on rebuilding the mobile experience.  This project is already well down the line for the Betfair Sportsbook the focus will be on the Exchange mobile product from early 2023.  See [https://betting.betfair.com/betfair-announcements/whats-new-on-betfair/help-shape-the-new-betfair-get-a-first-look-at-our-new-mobile-experience-220221-204.html|https://betting.betfair.com/betfair-announcements/whats-new-on-betfair/help-shape-the-[…]t-a-first-look-at-our-new-mobile-experience-220221-204.html](https://betting.betfair.com/betfair-announcements/whats-new-on-betfair/help-shape-the-new-betfair-get-a-first-look-at-our-new-mobile-experience-220221-204.html|https://betting.betfair.com/betfair-announcements/whats-new-on-betfair/help-shape-the-[…]t-a-first-look-at-our-new-mobile-experience-220221-204.html) for more details,

*Tags: Strategies*

---

**Carl** - *17:41:40*

Hi all, Carl from Betfair here. I've been collating feedback to help with the business case for launching BSP in new sports. I'd be very keen to hear from you if we haven't already spoken to you about it. Please contact me on [mailto:carl.albon@betfair.com|carl.albon@betfair.com](mailto:carl.albon@betfair.com|carl.albon@betfair.com)

*Tags: General Technical*

---

## 2022-10-24

**Neil T (Betfair)** - *11:18:47*

Hi [@U01665WFPD3](@U01665WFPD3) Ltp is only provided if there has been a change in the Ltp value.  This is mentioned in the Stream API documentation via [https://docs.developer.betfair.com/display/1smk3cen4v3lu3yomq5qye0ni/Exchange+Stream+API#ExchangeStreamAPI-MC/MarketChangeMessage](https://docs.developer.betfair.com/display/1smk3cen4v3lu3yomq5qye0ni/Exchange+Stream+API#ExchangeStreamAPI-MC/MarketChangeMessage)

*Tags: General Technical*

---

## 2022-11-04

**Pos** - *03:00:52*

how much faster is betfair api compared to the betfair website

*Tags: General Technical*

---

## 2022-11-05

**river_shah** - *06:07:08*

This channel is only active per announced times. Though in answering your question, last info is that there are no immediate plans for changing bet or passive delay behaviour 

*Tags: General Technical*

---

## 2022-11-14

**Pos** - *07:56:43*

Noob question but Is BSP efficient on Aussie greyhound markets? I've found the variance to be quite a lot more than horses. What kind of liquidity and overround would you target to ensure efficient odds?

*Tags: General Technical*

---

## 2022-11-18

**Newbie99** - *09:28:29*

[@U03TJKFLE8K](@U03TJKFLE8K) I don't know the answer, but this channel is only monitored by Betfair on specific occasions, you may have more luck posting the question in one of the other channels.

*Tags: General Technical*

---

## 2022-12-28

**Mick** - *10:37:55*

I just thought I'd have a little play with streaming (normally I just use the non-streaming API) but I got a message "AppKey is not configured for service". Do I need to somehow seek extra permission to use streaming?

*Tags: General Technical*

---

**D C** - *11:16:49*

There used to be so I assume there still is. I had to fill in a short questionnaire to be approved. There used to be a link on the BF pages somewhere but it was several years ago now so things might all be different.

*Tags: General Technical*

---

## 2023-01-20

**Carl** - *17:27:49*

Hi all,

Carl from Betfair here. _Betfair Starting Price (BSP) for new sports_ has been a discussion point in two of the last ABA's [@UNW8Q88EL](@UNW8Q88EL) has hosted on here. Following the demand from yourselves and other BSP customers, we're pleased to announce that we'll be launching the BSP on Football (Match Odds) *next week*. There will be some final testing Wednesday morning however the intention is to launch it on Wednesday 25th Jan for the Nottingham Forest v Man Utd Carabao Cup game. I'll update you here if we do have to delay launch due to unforeseen circumstances. We'll also offer it on the following fixtures as part of the first phase;



• Friday 27 Jan – Man City v Arsenal– FA Cup

• Saturday 28 Jan – All five 14:30 (UK time) Bundesliga games

• Sunday 29 Jan – All four La Liga games

A review will then take place to make sure prices are holding up but all being well, we plan to start offering BSP on all fixtures for the following competitions from Saturday 4th Feb;



• English Premier League

• Spanish La Liga

• Italian Serie A

• German Bundesliga

• UEFA Champion’s League

At the end of February, we'll undergo another review and listen to any suggestions for other competitions such as French Ligue 1 or International Football. In theory we could offer on every competition but we're keen to avoid massively skewed SP's. If all of the above is a success, we could then look at other markets and sports.



I'm disappearing for the weekend now but happy to answer any questions you have next week!

*Tags: Errors Debugging*

---

## 2023-01-24

**Techno** - *20:29:33*

Hi. I am wondering if you can use the advanced historic data to see the amount traded for each runner per second. I can write the last traded price, it is  runner.last_price_traded but I don't know how to locate the amount of money was traded on it at that moment. Could you tell me please?

*Tags: General Technical*

---

## 2023-01-27

**Unknown** - *10:04:21*

Morning all, everything went smoothly with the Forest v Man Utd game on Wednesday. Over £20k matched at SP including "take BSP if unmatched bets" (which don't show as SP bets on the graphs). There was also money matched against "non-SP unmatched bets" that were in the market and pulled into the reconciliation, which is promising and helps towards reducing the amount of bets that lapse. It's been enabled for tonight's game, the 14:30 Bundesliga games tomorrow and Sunday's four La Liga games.

*Tags: General Technical*

---

## 2023-02-02

**Yosef Mentzer** - *11:14:54*

Hi, is the Historical Data API down? I am getting error 500 when I make requests and the web API does not show plans, "My Data", etc.

*Tags: Data Quality, Errors Debugging*

---

## 2023-02-03

**Herugrim** - *08:41:49*

In the long run, bookies will ban you if you're winning too much (unless you're protected by minimum bet laws). Your initial question was a bit vague is all. You can beat BSP and still lose if you're making bad selections.

*Tags: Deployment*

---

## 2023-02-12

**Chantelle** - *16:49:41*

Hey guys, new here.  I've been using a bot program to execute all my bets the last year, so no coding required. I run about 8 profitable systems atm since March (39000 bets placed).   Would like to learn bit more on the API side from a purely beginners level.  I have had some exposure to Python language in the past, is Python useful or should I look more into a different language?  Are there any free resources to learn about developing and executing your strategies using the betfair API? Thanks!

*Tags: Getting Started*

---

**Aaron Smith** - *16:55:41*

this channel is reserved for news straight from betfair and Q&amp;A's run by betfair.

On topic: Python is the perfect language to jump in with as there are quality api-wrappers and frameworks already developed by liam which you can use. Check out [https://github.com/betcode-org/betfair](https://github.com/betcode-org/betfair) (api-wrapper) and [https://github.com/betcode-org/flumine](https://github.com/betcode-org/flumine) (framework build on top of betfairlightweight)

*Tags: General Technical*

---

**Aaron Smith** - *16:56:42*

most ppl here are using betfairlightweight and probably nearly as much are using flumine

*Tags: General Technical*

---

## 2023-02-23

**Carl** - *13:36:34*

We've released a fix today which will take effect tomorrow to address the column headers concern i.e. they will revert back to upper case. If you can provide some more info re: the MENU_HINT issue, we will explore this too.

*Tags: Errors Debugging*

---

## 2023-03-07

**Unknown** - *15:46:17*

Hi [@U02K5EBKNBF](@U02K5EBKNBF) - please see further details regarding the root cause of Saturdays issue - _We had multiple failovers of the Exchange Bet Stream on Saturday, which caused a full snapshot to be sent out to our other downstream applications. One of these applications ran out of memory when trying to process the snapshot, causing long garbage collection, and leading to bet placement failures. To mitigate such problems, we are currently in the process of aggressively reducing &amp; tuning memory usage across both the Bet Stream and our downstream applications_

*Tags: Performance*

---

## 2023-03-08

**Unknown** - *09:40:49*

Morning all. Not meaning to take attention away from Neil's message above on a far more important matter but for the BSP fans....After another solid month of BSP Football, we've decided to add all Grade 2 competitions, which will more than double the number of BSP Football markets to around 4,000 per annum. This means we'll be capturing match odds markets that account for over 60% of volume but less than 10% of football fixtures, so we have headroom to explore further if there's demand. I've attached a list of all Grade 1 and 2 competitions with their current status.



We'll review again next month to see whether we should add new football markets (over/under goals, correct score) or a new sport such as golf or look at Grade 3 football. I'd be keen to hear from anyone who had a particular view on this.

*Tags: Errors Debugging*

---

## 2023-05-18

**Sher Khan** - *20:07:29*

I want to betfair api 

How can buy betfair api [@U031UL88GG6](@U031UL88GG6)  [@UNW8Q88EL](@UNW8Q88EL)  @betfair

*Tags: General Technical*

---

## 2023-07-04

**Neil T (Betfair)** - *17:05:19*

We are pleased to announce details of the *Betfair Developer Summer Meetup*! Please see [https://forum.developer.betfair.com/forum/developer-program/announcements/38417-betfair-api-developer-summer-meetup#post38417](https://forum.developer.betfair.com/forum/developer-program/announcements/38417-betfair-api-developer-summer-meetup#post38417) for further details on how to register.

*Tags: General Technical*

---

## 2023-10-10

**Neil T (Betfair)** - *17:48:35*

[@U02K1MG7YCA](@U02K1MG7YCA) this issue is now fixed 

*Tags: Errors Debugging*

---

## 2023-12-01

**Carl** - *15:25:36*

Hi everyone,

I'm pleased to announce the launch of our 3-part Cricket webinar which can be found below;



[https://betting.betfair.com/betfair-announcements/exchange-news/forecasting-for-cricket-markets-webinar-watch-episode-1-of-our-expert-guide-221123-272.html|https://betting.betfair.com/betfair-announcements/exchange-news/forecasting-for-cricke[…]webinar-watch-episode-1-of-our-expert-guide-221123-272.html](https://betting.betfair.com/betfair-announcements/exchange-news/forecasting-for-cricket-markets-webinar-watch-episode-1-of-our-expert-guide-221123-272.html|https://betting.betfair.com/betfair-announcements/exchange-news/forecasting-for-cricke[…]webinar-watch-episode-1-of-our-expert-guide-221123-272.html)



In a bid to increase Cricket education amongst our more technical clients, we've teamed up with Ian McHale (Professor of Analytics, University of Liverpool) and Muhammad Asif (Head of Statistics at the University of Malakand). Alongside Ed Hawkins, they run through the basics of Cricket before progressing quite quickly on to the more technical elements, including areas of their academic research such as the Duckworth & Lewis method.



Part 2 will focus on factors of their own in-play model which should be released before Xmas. Part 3 will follow in the new year and is _expected_ to introduce player ratings although this is subject to change.

*Tags: Deployment, Strategies*

---

## 2024-09-16

**Jemima Cecil** - *15:55:00*

Anyone have any issues with the Betfair API today?

*Tags: General Technical*

---

## 2024-11-12

**liam** - *11:18:20*

I imagine it was on the betfair dev forum but I have no idea how to login into that anymore

*Tags: General Technical*

---

## 2024-11-19

**liam** - *10:38:36*

I imagine its a big change to the matching engine, no idea how I am going to get flumine to simulate it accurately :sweat_smile:

*Tags: General Technical*

---

**D C** - *14:53:16*

[@U02GSMUSG56](@U02GSMUSG56) does this mean that currently when you place a bet (inplay) your bet is "paired" with other bet(s) at the point of first being received and is then held back until the delay is over and would then appear as matched at placement (assuming the other bet is not cancelled). Sorry if this is a dumb take, but your first sentence kind of suggests this. On the assumption that the above is true, how then does BPE get implemented? If a better price becomes available, does my bets "pair" get replaced with the better offer while the delay is still in action?

I'd always assumed that your bet was received, and queued at time of receipt and that once the delay was over the matching took place based on the market state. Is there anywhere we can get more details on how the matching engine operates currently with the inplay delay?



Sorry for all the questions but I've confused myself trying to run this through my head.

*Tags: General Technical*

---

**Michael** - *15:47:01*

Massive props to Befair for finally getting onto this. Thanks [@U02GSMUSG56](@U02GSMUSG56), [@UNW8Q88EL](@UNW8Q88EL) and others.



I just bloody love it when something new happens. I loved it when streaming happened, I had a ball when TPD arrived and whatever the outcome of this the early stages will be a blast. Finally something fun. Hallelujah!

*Tags: General Technical*

---

## 2024-11-28

**Joe** - *16:52:49*

[@U02GSMUSG56](@U02GSMUSG56) will there be an indicator on the market definition as to which delay model (legacy or this new one) is going to be used? I think we will need this.

*Tags: Strategies*

---

## 2025-01-24

**liam** - *22:06:00*

I recommend having a play with one of these markets, a bet will skip the delay either at initial placement if passive when it reaches the matcher or during the delay if it becomes passive.



Maybe I have misunderstood your question though as how would the matcher know the price you are reacting to? 

*Tags: General Technical*

---

