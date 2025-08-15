# Multi Client - Community Knowledge

*17 relevant conversations from across all channels*

---

## 2023-11-14 23:00:39 - random channel

**PeterLe**

Thanks gents, yes I thought the same [@U02RN7YDRQ9](@U02RN7YDRQ9) I hadn’t read it properly till [@UBS7QANF3](@UBS7QANF3) just pointed it out that it was ‘successful’ logins, I couldn’t possibly have done that manually, but flumine has been running on multiple accounts for many months and I’ve never seen it before? 

I’ll just leave flumine running and check every other day the balances via the master account 

thanks for the thoughts though both

---

## 2023-08-23 11:01:33 - strategies channel

**George**

I would like to run two strategies from two different subaccounts.

Can I do this using one flumine process?

If not - is it ok to have two separate flumine processes running on the same machine?

---

## 2023-06-17 10:54:50 - general channel

**AI Trader**

Hi guys,

I am looking for a solution to test strategies with small amounts of money. I know I. can limit that through software and using the concept of strategies in the orders and etc, but I was wondering if there is any way to have anything similar to a sub-account (as in crypto exchanges), so regardless of software bugs, I can guarantee I will be using a limited amount of money for a strategy. Any ideas on this? [https://support.betfair.com/app/answers/detail/a_id/94|Betfair seems not to allow multiple accounts per client](https://support.betfair.com/app/answers/detail/a_id/94|Betfair seems not to allow multiple accounts per client)

---

## 2023-04-19 18:18:28 - general channel

**Andrey Luiz Malheiros**

I was reading in the documentation about workers, and this really seems to be the ideal way to update the context according to data in my database. Thank you for your help, Liam. Regarding the situation of adding and renewing a strategy, is it possible to use any approach with workers and CustomEvent to add or remove strategies? I ask this because of the following situation: let's suppose I have 12 strategies for 4 different sports being executed. If I use one instance of Flumine for each strategy, I will end up with 12 different clients. Would this pose any issues with the connection limit allowed by Betfair, for example? Another option would be to run all the strategies in the same instance of Flumine. However, if I wanted to stop running only one of these strategies, it wouldn't be possible. I would have to remove all of them and then restart Flumine. Is there any solution to address this?

---

## 2023-01-25 13:11:50 - random channel

**PeterLe**

:thinking_face: If you were to run the exact same strategy (inc stakes), on the same system, on multiple accounts, how close would you expect the end of month profits to be on each account?

---

## 2022-12-12 15:54:42 - random channel

**George**

Everyone has a different risk tolerance of course but in my case I generally get referred by people who know me / existing happy customers and that helps. I have never had anyone worry about sharing account details - easy to set up a subaccount with a small balance until you get comfortable.



As a matter of principle i believe the risk is confined to the value of the funds in the account - whether that counts as "safe" or not is in the eye of the beholder!

---

## 2022-03-25 09:59:02 - general channel

**liam**

flumine v2.0.0 now released, this has a few breaking changes 99% around naming (Backtest-&gt;Simulated) hence the major version bump (over 2yrs since v1!) but now allows multi clients/exchanges, see [https://betcode-org.github.io/flumine/clients/|docs](https://betcode-org.github.io/flumine/clients/|docs) on how to use. Also added a rough [https://github.com/betcode-org/flumine/blob/master/examples/example-betconnect.py|example](https://github.com/betcode-org/flumine/blob/master/examples/example-betconnect.py|example) on using the BetConnect client.



I have been testing for a few weeks now and I believe it to be bug free, any issues are likely to be around simulation rather than live due to the changes but let me know if you spot anything.



Future work will involve opening up the framework to be more exchange/API agnostic in terms of execution/market/orders etc.

---

## 2022-02-24 12:08:46 - random channel

**liam**

Currently refactoring flumine for multi clients (likely to be a v2 bump due to the number of changes and renames), any feedback on this [https://github.com/liampauling/flumine/blob/8fe3329734b3a24aa425caf25d979b56a3cb8fce/docs/clients.md|API](https://github.com/liampauling/flumine/blob/8fe3329734b3a24aa425caf25d979b56a3cb8fce/docs/clients.md|API) welcomed.



Initial release would be the limited in use but future work would allow orders/execution via the framework and the addition of further ExchangeTypes (betdaq etc)

---

## 2021-09-05 08:45:04 - general channel

**Mo**

For previously discussed reasons, even if you get a connection limit per subaccount, if you end up using that many connections they will come down hard on you



It sounds like all of your problems go away if you use a coarse market filter and do the filtering locally as is best practice

---

## 2021-05-05 10:34:04 - general channel

**Mo**

I run the same strategy across multiple accounts

---

## 2021-01-28 17:55:59 - strategies channel

**liam**

`The trigger was a guy running a ridiculous bot on the API on one of his unfunded sub accounts.



It was doing a martingale over and over again, going from tiny to huge stakes in a cycle. The max stake on the exchange was some very large number, I don’t remember what, but bigger than 2e31.



Two things happened at the exact same moment: this martingale bot tried to place some huge bet way over the numeric max (and crucially, over that subaccount’s exposure limit) this caused a numeric error inside the trading engine exposure checking code.



This bet was rejected and you never saw it: all good. Unfortunately, the long dormant bug activated and allowed another bet which was not over the numeric max stake but was over the exposure limit for the account (it had nothing like the 20m to bet in it) to skip the exposure check.



Because it was a valid stake and the exposure check was missed, it went into the market and became good value pretty quickly. The nature of the bug meant that both bets had to be placed effectively at the same time, otherwise the tiny window of time that the numeric error opened up for the second bet to skip the exposure check would be closed again.



All involved in all aspects of handling this bug at the time were given the usual spiel of secrecy, which was fair because the bug was exploitable for a little while until fixed.



However, it was fixed long ago (although similar bugs probably existed because the codebase was very difficult to reason over) and now that whole trading system has been rewritten in a more modern language with a safer architecture (and it’s much much faster). I imagine there are all sorts of bugs in it, but they won’t be this type.`

---

## 2020-10-14 13:04:33 - strategies channel

**D C**

No idea then [@U0160KZB6QP](@U0160KZB6QP). I thought multiple accounts at same address were a problem (even with different person) but I have not used a bookie in years so that might be nonsense. No idea why responsible gambling department would get involved unless you or your partner were registered SE at some point in the past. It is very frustrating getting no response like that. Have you tried contacting by phone? Not sure what else you can do really. You could try casinomeister site - novibet is accredited there and that used to mean they had a rep from the casino as a forum member. You could try that  to get some answers but its a long shot.

---

## 2020-07-26 09:11:14 - strategies channel

**Mo**

In principle MSA structure is very useful for having a per strategy absolute exposure limit but in practice I rarely use more than one of my subaccounts

---

## 2020-07-23 10:00:55 - issues channel

**Mo**

Application name needs to be _globally_ unique. Not necessarily your problem but that tripped me up on the last subaccount I created 

---

## 2020-07-08 20:05:48 - general channel

**birchy**

[@UQL0QDEKA](@UQL0QDEKA) was just thinking...you mentioned earlier that you use multiple accounts. I have 2 accounts, but only because I use one for testing and the other for my production bots. I don't have any issues with multiple bots placing bets on the same markets. It used to be beneficial to use one account as it boosted the commission discount, but of course they have the 2% package now. Do you not use the strategyRef parameter to identify bots?

---

## 2020-07-08 10:50:01 - general channel

**PeterLe**

[@U016TGY3676](@U016TGY3676), I think many of us have visited your website over the years, so looking forward to your participation on here

I read your comments on being a fan of £2 bets rather than larger bets, Im the same and wondered if others had found this too.



I run multiple accounts with a slight variation of a theme and recently I was contemplating whether to simply create more accounts (and effectively clone the strategies) and stick to lower stakes £2 stakes (In play for the back strategies) or increase the stakes on my existing accounts. 

Around 2011 to 2013/14 I was using stakes circa 17 times bigger than I do today and the bulk of my lifetime profits are from this period.

I know you have been around a while; I was just curious was to find out how your staking had changed (if any) over the years. Interested to hear others comments too, Thanks (PS if the answer is “Backtest with Flumine, Im trying to implement!! :grinning:)

---

## 2019-12-02 19:20:40 - general channel

**Mo**

My suggestion is to try to get an account manager and use them to get a master/subaccount setup. But I think they don’t really give them out any more. I think their intention is for people to separate strategies using the customerStrategyRef functionality instead. I could be wrong though. [@U4H19D1D2](@U4H19D1D2) do you have any more insight?

---

