# Optimization Guide

*Performance tips and best practices from expert users*

### Hi [@U02K5EBKNBF](@U02K5EBKNBF) - please see further details regarding the root cause of Saturdays issue - _We had multiple failovers of the Exchange Bet Stream on Saturday, which caused a full snapshot to be sent out to our other downstream applications. One of these applications ran out of memory when trying to process the snapshot, causing long garbage collection, and leading to bet placement failures. To mitigate such problems, we are currently in the process of aggressively reducing &amp; tuning memory usage across both the Bet Stream and our downstream applications_

*From Unknown*

**Context:** 

## 2023-03-07

**Unknown** - *15:46:17*

Hi [@U02K5EBKNBF](@U02K5EBKNBF) - please see further details regarding the root cause of Saturdays issue - _We had multiple failovers of the Exchange Bet Str...

---

### The reasoning behind it is that lightweight is only really beneficial on marketbook requests as that is when you want to reduce latency, I don't use it but if I were to use it I would want to have a full resource for all the other requests. Happy to remove but wanted it to be dynamic as I am not sure how others are using it

*From liam*

**Context:** 

## 2017-07-09

**liam** - *06:44:13*

The reasoning behind it is that lightweight is only really beneficial on marketbook requests as that is when you want to reduce latency, I don't use it but if I...

---

### I don't think it decreases latency because sometimes you will get a response from placeOrders before you get an orderStream update

*From liam*

**Context:** 

**liam** - *11:29:05*

I don't think it decreases latency because sometimes you will get a response from placeOrders before you get an orderStream update

*Tags: Performance*

...

---

### Unless you use the async parameter then your order is in the book when your call to placeOrders returns.

*From Mo*

**Context:** 

**Mo** - *15:55:56*

Unless you use the async parameter then your order is in the book when your call to placeOrders returns.



The only reason a streaming price update received after that would no...

---

### So I use flumine for all my data recording and I have a separate framework for strategies. I can’t open source the latter due to their being too much secret sauce tightly coupled to it but I am slowly advancing flumine to be at the same level (if not better / more dynamic / plug and play)

*From liam*

**Context:** 

**liam** - *08:06:43*

So I use flumine for all my data recording and I have a separate framework for strategies. I can’t open source the latter due to their being too much secret sauce tightly coup...

---

### It sounds like you might be conflating the term mining data with scraping, in which case your comments on throttled speed are irrelevant with streaming because there is no polling involved

*From Mo*

**Context:** 

**Mo** - *19:52:58*

It sounds like you might be conflating the term mining data with scraping, in which case your comments on throttled speed are irrelevant with streaming because there is no polli...

---

### Most people probably don’t want to stand a lot of infra up, so basically just write as fast as possible to anything that works, and have other stuff use that as input to give you info you want to read. If you care about latency: do it all in memory.

*From Paul*

**Context:** 

**Paul** - *23:28:11*

Most people probably don’t want to stand a lot of infra up, so basically just write as fast as possible to anything that works, and have other stuff use that as input to give ...

---

### So you can use the streaming update to tell you which runner has been updated, that can speed things up

*From liam*

**Context:** 

**liam** - *07:38:10*

So you can use the streaming update to tell you which runner has been updated, that can speed things up

*Tags: Performance*

...

---

### I'm asking because I'd expect high latency to be most punishing when you don't cancel in time and maybe this is not something you care about

*From Mo*

**Context:** 

**Mo** - *13:08:34*

I'm asking because I'd expect high latency to be most punishing when you don't cancel in time and maybe this is not something you care about

*Tags: Performance*

...

---

### Use smart_open [https://liampauling.github.io/flumine/performance/#file-location|https://liampauling.github.io/flumine/performance/#file-location](https://liampauling.github.io/flumine/performance/#file-location|https://liampauling.github.io/flumine/performance/#file-location)

*From liam*

**Context:** 

## 2021-12-05

**liam** - *09:33:00*

Use smart_open [https://liampauling.github.io/flumine/performance/#file-location|https://liampauling.github.io/flumine/performance/#file-location](https://liamp...

---

### Personally I use a MariaDB instance at RDS as, while a huge fan of Mongodb and Elastic, I haven't in my trading activities found a strong enough case to store data in documents, rather than well-designed rows, to warrant the added complexity.

*From Peter*

**Context:** 

**Peter** - *20:04:31*

There's no inherent slowness in Mongodb, so if your retrievals are slow, that's probably an indexing issue. Mongo (and indeed any schema-less database) makes more demands on ...

---

### Use a session. Having to do an SSL handshake on every request is going to kill performance

*From Mo*

**Context:** 

**Mo** - *15:21:51*

Use a session. Having to do an SSL handshake on every request is going to kill performance

*Tags: Performance*

...

---

### Lightweight mode won’t work in flumine as it’s designed to use resources however a few things are patched to improve speed (check out the patch file)

*From liam*

**Context:** 

**liam** - *21:05:37*

Lightweight mode won’t work in flumine as it’s designed to use resources however a few things are patched to improve speed (check out the patch file)

*Tags: Performance*

...

---

### Worth adding that the real cost of the switch is very difficult to evaluate. It's fairly easy to understand "faster" and to see from the docs what can be done using Polars. But the real pain point would come in the edge cases when I hit an "oh shit" moment as I realise that this thing I do in Pandas may not exist in Polars and I've got to code it up myself or keep using Pandas anyway.

*From Peter*

**Context:** 

**Peter** - *15:01:38*

Looked at it a couple of times, but each time felt that the overhead of adjusting to it outweighed the performance benefits. For context my dataframes can run to several mill...

---

### 1. No one uses `ujson` any more, use `orjson`

*From Mo*

**Context:** 

**Mo** - *15:48:41*

1. No one uses `ujson` any more, use `orjson`

2. From what I can tell, you do things differently in Python than rust. In Python you read the entire contents of the file into me...

---

