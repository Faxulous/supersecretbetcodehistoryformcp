# Betconnect Knowledge Base

*Generated from Slack chat history - 139 technical conversations*

---

## 2022-03-24

**Unknown** - *12:32:36*

Hello everyone, we've got a few spots left for our first API event in Mayfair next week. It will be hosted at the Candy Capital bar where we will be chatting about our business model and the value that we are bringing to API bettors. This first event will be focused on backers, let us know if you want to come! :beers:

*Tags: Strategies*

---

**liam** - *13:26:05*

[@ULDAVFDRP](@ULDAVFDRP) has kindly transferred his [https://github.com/betcode-org/betconnect|betconnect API python](https://github.com/betcode-org/betconnect|betconnect API python) wrapper to betcode and can now be installed via pypi :grin:



`pip install betconnect`

*Tags: Getting Started*

---

## 2022-03-25

**Joel Beasley** - *12:03:20*

ok no problem [@U02V5MNA8SW](@U02V5MNA8SW) I will contact you directly with the details :thumbsup:

*Tags: General Technical*

---

## 2022-03-29

**Graham** - *13:24:08*

```bet_create_response

Out[53]: BaseRequestException(message='Market type id is not valid for fixture.', request_url='[https://stgapi.betconnect.com/api/v2/bet_request_create](https://stgapi.betconnect.com/api/v2/bet_request_create)', status_code=400)```

getting this from the staging env when passing `6` as the market type ID

*Tags: Errors Debugging*

---

**Graham** - *13:29:08*

```CreateBetRequestFilter(fixture_id=108391776, market_type_id=6, competitor='1052767814', price=2.88, stake=500, handicap=None, bet_type='Win')```



*Tags: Errors Debugging*

---

**Joel Beasley** - *13:30:24*

Hi [@U01EZ613ZCZ](@U01EZ613ZCZ) the `market_type_id` changed to `10160` recently - are you seeing 6 in our documentation somewhere?

*Tags: General Technical*

---

**Oliver Varney** - *13:30:48*

ah [@U02KNTX2Z7X](@U02KNTX2Z7X) beat me to it, are you calling that function first? im assuming nothing on the api has changed, so id say check [https://github.com/betcode-org/betconnect/blob/master/examples/dailyhorseracing.py](https://github.com/betcode-org/betconnect/blob/master/examples/dailyhorseracing.py) which should help with the workflow of getting correct ids

*Tags: General Technical*

---

**mandelbot** - *13:37:09*

I'm getting

```{"asctime": "2022-03-29 12:35:10,069", "levelname": "ERROR", "message": "Issue with request for: [https://stgapi.betconnect.com/api/v2/bet_request_create](https://stgapi.betconnect.com/api/v2/bet_request_create), message: Input payload validation failed", "exc_info": "NoneType: None"}```

my bet looks like this:

```                            client.betting.bet_request_create(                                request_filter=resources.filters.CreateBetRequestFilter(

                                fixture_id=selection.source_fixture_id,

                                market_type_id=selection.source_market_type_id,

                                competitor=selection.competitor_id,

                                price=max_price,

                                stake=5,

                                bet_type="Win",

                                handicap=None

                                )

                                )```



*Tags: Errors Debugging, Strategies*

---

**Graham** - *13:39:10*

I'm using this one [@U010GM77S4W](@U010GM77S4W)

```bet_create_response = client.betting.bet_request_create(

                request_filter=resources.filters.CreateBetRequestFilter(

                    fixture_id=fixture.fixture_id,

                    market_type_id=win_market_type.market_type_id,

                    competitor=selection.competitor_id,

                    price=best_price.price,

                    stake=500,

                    bet_type=win_bet_type,

                    customer_order_ref=resources.CustomerOrderRef.create_customer_order_ref(

                        str(uuid.uuid4())

                    ),

                )

            )```

*Tags: Errors Debugging, Strategies*

---

**Oliver Varney** - *13:43:04*

[@U010GM77S4W](@U010GM77S4W) can you take a screenshot of the debugger / provide values for that data?

*Tags: Errors Debugging*

---

**Graham** - *13:45:47*

placing a bet request with some manual fields

```            bet_create_response = client.betting.bet_request_create(

                request_filter=resources.filters.CreateBetRequestFilter(

                    fixture_id=fixture.fixture_id,

                    market_type_id= 10160, #win_market_type.market_type_id,

                    competitor=selection.competitor_id,

                    price=2.75,#best_price.price,

                    stake=500,

                    bet_type=win_bet_type,

                    customer_strategy_ref=resources.CustomerStrategyRef.create_customer_strategy_ref(

                        STRATEGY_NAME

                    ),

                    customer_order_ref=resources.CustomerOrderRef.create_customer_order_ref(

                        str(uuid.uuid4())

                    ),

                )

            )```

returns a validation error

```

Traceback (most recent call last):



  File "C:\Users\Graham\AppData\Local\Temp/ipykernel_3964/974456888.py", line 67, in &lt;module&gt;

    bet_request_get = client.betting.bet_request_get(



  File "C:\Users\Graham\anaconda3\lib\site-packages\betconnect\endpoints\betting.py", line 221, in bet_request_get

    return self.process_response(



  File "C:\Users\Graham\anaconda3\lib\site-packages\betconnect\endpoints\baseendpoint.py", line 192, in process_response

    return resource.create_from_dict(data)



  File "C:\Users\Graham\anaconda3\lib\site-packages\betconnect\resources\baseresource.py", line 26, in create_from_dict

    return cls.parse_obj(d)



  File "pydantic\main.py", line 572, in pydantic.main.BaseModel.parse_obj



  File "pydantic\main.py", line 400, in pydantic.main.BaseModel.__init__



ValidationError: 1 validation error for BetRequest

backer_stats

  field required (type=value_error.missing)```

*Tags: Errors Debugging, Strategies*

---

**mandelbot** - *13:48:02*

```fixture_id=108391794

market_type_id=10160

competitor= 1052139537

price= 34.0 

bet_type='Win'```

*Tags: Errors Debugging*

---

**Joel Beasley** - *14:37:31*

`market_type_id` has been fixed in Staging now [@U01EZ613ZCZ](@U01EZ613ZCZ), will update Production in the morning :thumbsup:

*Tags: Errors Debugging, Deployment*

---

**mandelbot** - *16:43:18*

getting the same error

*Tags: Errors Debugging*

---

**Oliver Varney** - *16:49:49*

do you have a new exmaple fixture as the old onelooks like it may have finished?

*Tags: Errors Debugging*

---

**mandelbot** - *16:52:22*

Yeah will have a go with dailyhorseracing.py, i took the bet request from that and added it to Liam's example and thats what's been throwing errors

*Tags: Errors Debugging*

---

**Oliver Varney** - *16:56:40*

okay let me have a look but have you tried without flumine just using that horse racing example? might be best to just rule out anything in that alone, i.e. creating a bet without flumine?

*Tags: General Technical*

---

**Oliver Varney** - *17:05:54*

try this maybe:

```client.betting.bet_request_create(

    request_filter=resources.filters.CreateBetRequestFilter(

        fixture_id=selection.source_fixture_id,

        market_type_id=int(selection.source_market_type_id),

        competitor=selection.competitor_id,

        price=max_price,

        stake=5,

        bet_type="Win",

        handicap=None

    )

)```



*Tags: Errors Debugging, Strategies*

---

**mandelbot** - *17:10:08*

tried also wrapping fixture_id as an int

*Tags: Errors Debugging*

---

**Oliver Varney** - *17:13:56*

hmm okay let me debug it properly it just was on the odd chance it was that

*Tags: Errors Debugging*

---

**Oliver Varney** - *17:54:06*

found it just working on a fix now

*Tags: Errors Debugging*

---

**Oliver Varney** - *18:02:02*

no its todo with customer order ref and strategy refs

*Tags: Strategies*

---

**Oliver Varney** - *18:08:00*

just working on a fix will be either later on or early tomorrow morning, for now if your testing just populate customer_order_ref and customer_strategy_ref per the horse racing example

*Tags: Errors Debugging, Strategies*

---

**Graham** - *18:22:38*

I'm running the `horseracingexample.py` and am getting the following

```AttributeError: module 'betconnect.resources' has no attribute 'filters'```

*Tags: Errors Debugging*

---

**Graham** - *18:29:49*

I'm pretty sure it's an import error

*Tags: Errors Debugging*

---

## 2022-03-31

**Graham** - *11:43:07*

```{'source_fixture_id': '108400418', 'source_market_id': '101608400418', 'source_market_type_id': '10160', 'source_selection_id': '10840041852297932', 'trading_status': 'Trading', 'name': 'Patagonia', 'competitor_id': '1052297932', 'max_price': '4.33'}```

*Tags: Errors Debugging, Strategies*

---

**Graham** - *13:17:38*

```CreateBetRequestFilter(fixture_id=108400430, market_type_id=10160, competitor='10840043052320480', price=29.0, stake=500, handicap=None, bet_type='Win', customer_strategy_ref=Customer strategy ref: horse_racing, customer_order_ref=Customer order ref: 9168296c-23e7-4abd-b158-6355ddc5615f)```

*Tags: Errors Debugging, Strategies*

---

**Karl Sutt** - *13:22:12*

Also not sure about the `customer_strategy_ref` and `customer_order_ref` fields — it doesn't look like valid Python to me. Is that just the representation?

*Tags: Strategies*

---

**Oliver Varney** - *13:25:08*

I'm away from my PC but it's not valid python strings / function args

*Tags: General Technical*

---

**Peter** - *13:27:51*

I can replicate the problem as described exactly by extending the competitor ID, and leaving the rest of the code in the same format as the horse racing example. If I put in the correct competitor ID, the bet is placed.

*Tags: General Technical*

---

**Oliver Varney** - *13:30:08*

[https://github.com/betcode-org/betconnect/blob/055158f8fc89a7491d19396f91373de0dfee81b4/examples/dailyhorseracing.py#L131|https://github.com/betcode-org/betconnect/blob/055158f8fc89a7491d19396f91373de0dfee81b4/examples/dailyhorseracing.py#L131](https://github.com/betcode-org/betconnect/blob/055158f8fc89a7491d19396f91373de0dfee81b4/examples/dailyhorseracing.py#L131|https://github.com/betcode-org/betconnect/blob/055158f8fc89a7491d19396f91373de0dfee81b4/examples/dailyhorseracing.py#L131)

*Tags: General Technical*

---

**Peter** - *13:31:51*

So doesn't appear to be a problem at the BetConnect end, though the error message received when the competitor ID is invalid is very misleading.

*Tags: Errors Debugging*

---

**Oliver Varney** - *13:36:09*

In the latest push which I'm waiting on something from BC end, error messages are added to provide more detail when error codes are returned, plus a fix for customer / order refs and maybe a few type  changes if I get some confirmation

*Tags: Errors Debugging*

---

**Oliver Varney** - *13:38:02*

I can probably put together some helper functions if needs be, but it would be good if people raise these as issues/requirements

*Tags: General Technical*

---

**Karl Sutt** - *13:43:09*

`__repr__` should generally be the Python representation of the object, if at all possible. You should be able to copy-paste the representation into a Python shell and get a valid object out. [https://docs.python.org/3/reference/datamodel.html#object.__repr__](https://docs.python.org/3/reference/datamodel.html#object.__repr__)

*Tags: Strategies*

---

## 2022-04-01

**Unknown** - *10:10:48*

Thanks to all of you that came to our first API event yesterday! Great to meet some of you in person and talk about our platform as well as listen to your ideas, strategies and feedback on how to keep improving BC.



For those of you outside London, and also those that couldn't make it yesterday,  we'll be hosting a virtual event soon and sharing more information in this channel so stay tuned! :eyes:

*Tags: General Technical*

---

## 2022-04-29

**Mauricio Garcia** - *13:49:20*

As chosen by the community, we'll be hosting the event at *5pm!*



Please register here and we'll send the invite link beforehand: [https://forms.gle/4CuiS5MNTKiG6d449](https://forms.gle/4CuiS5MNTKiG6d449)



Feel free to drop questions in this channel about BetConnect's API platform and business model or any other questions you have, so we can address them on the call.



Happy bank holiday!

*Tags: Strategies*

---

## 2022-05-04

**Mo** - *09:22:12*

[@U02QTC0RWDC](@U02QTC0RWDC) afraid not, I have the same error as [@U010GM77S4W](@U010GM77S4W)

*Tags: Errors Debugging*

---

**Mauricio Garcia** - *09:24:31*

found the problem

*Tags: General Technical*

---

**Jonjonjon** - *17:53:16*

My phone went fuzzy when they were discussing how to get the mug. Watching it from Clapham Junction is hard.

*Tags: General Technical*

---

## 2022-05-06

**Mauricio Garcia** - *14:04:12*

Hi guys,



As we promised we'll be dropping short edits from the Virtual Event to share the information discussed and also use this channel as a platform to communicate with all of you moving forward.



Keep an eye on this space as we'll be giving out transparent and direct answers on your questions!

*Tags: General Technical*

---

**Mauricio Garcia** - *14:50:38*

we'll start uploading snippets in this channel :slightly_smiling_face: If you have a specific question, just let us know

*Tags: General Technical*

---

## 2022-05-09

**Ruben** - *21:05:55*

very interesting stuff....I am wondering what is your business model? meaning, if it is possible to back at bookmaker prices when they offer value, who is taking on this risk? the bookmakers? will they continue to do so once they realise that the bets coming from your bettors are -EV for them?

*Tags: Strategies*

---

## 2022-05-10

**Daniel** - *12:50:57*

Thanks for the question [@U011VL3CA2Y](@U011VL3CA2Y). BetConnect is an exchange and commissions are only paid by the backer (competitive rates + No premium Charge!). Matched bettors are attracted to the layside on BetConnect because you (API backers) are providing them with liquidity.



They will offset their risk on BetConnect by backing the same bet with bookmakers and take advantage of any promotions they offer. A match bettor is agnostic as to whether the bet represents -EV, all types of liquidity are valuable to them. Through our api, the ability to pump out hundreds of bets across multiple sports adds liquidity to the exchange eco system.



Hope this answers your question [@U011VL3CA2Y](@U011VL3CA2Y) - we'll upload more information on matched bettors and how they use our liquidity to make money.

*Tags: General Technical*

---

## 2022-06-23

**Unknown** - *14:50:12*

[!here](!here) back again with a Head to Head liquidity comparison ! :bc:



This time we've chosen an Each Way bet to show also how those perform in BetConnect vs. Betfair. As requested by some of you in the feedback, we are displaying the markets in both platforms for pure transparency.  Please keep the feedback coming and get in touch with us if you need more information or any API documentation for testing.



Best!



-The BetConnect Team :bc:

*Tags: General Technical*

---

**Mauricio Garcia** - *16:56:07*

No problem, please keep me posted :handshake:

*Tags: General Technical*

---

## 2022-07-05

**Sam - DH** - *20:43:08*

Hi Mauricio, could I possibly also join this chat please? Have quite a lengthy, BetConnect API specific issue - not sure it belongs in/should be cluttering this channel, nor the BF Lightweight/Flumine issues channel. Alternatively if you could direct me to the most appropriate channel, would be most grateful! Cheers



Edit: I whacked it in here anyway, excitement got the better of me, feel free to re-locate me/my thread if needs be

*Tags: General Technical*

---

## 2022-07-06

**Sam - DH** - *13:14:07*

Afternoon BC, hit a bit of a wall using the api and python wrapper (has been blinding up to this point - nice work). Searched your git repo and this workspace, haven't seen this 'issue' addressed yet so, hoping it’s not my incompetence and is just that we're the Lay-side early birds.



In short, I'm struggling to find an acceptable 'True' value for the accept_each_way param in /bet_request_get. I think there is also an issue in the way it's defined in filters.GetBetRequestFilter(), but, the parameter as a whole, server-side, I don't think is working as expected.



The above alone is probably enough for someone more switched on than me to work this out but, I’ll detail some more troubleshooting I did in this thread, in case it’s useful.

*Tags: Deployment*

---

**Sam - DH** - *13:14:41*

I thought initially the issue was just GetBetRequestFilter() erroneously converting this param to a String value before making the request, as it's currently defined as

```accept_each_way: Optional[str] = Field(default=0)```

Which meant that even passing in the default value of 0 resulted in a

```message: accept_each_way value is invalid.```

error when attempting .bet_request_get().



Although I changed this param param definition to

```accept_each_way: Optional[int] = Field(default=0)```

and it still wouldn't allow 1 as a valid value; passing in 0 was now fine however.



Went on to try this just using the requests library and found similar problems, allows 0, doesn't allow 1, nor any other combination of 'True', 'Included' etc. so, main issue seems outside the scope of the wrapper.



Finally, had a quick look through the JS on your site for closure, and found a section that seems to confirm it should be dictated by a 1 or a 0 so, time to call in the big boys.



Cheers in advance for any help.

Sam

*Tags: Errors Debugging*

---

**Sam - DH** - *17:16:17*

Don't think I can feel too silly, did my best :joy:

Will raise request via wrapper's git to add option to exclude param - if possible.

Cheers again for your help

*Tags: General Technical*

---

## 2022-07-07

**Mauricio Garcia** - *10:25:38*

No problem, happy to keep the thread here in case it can help future API bettors

*Tags: General Technical*

---

## 2022-07-19

**Mick** - *14:46:53*

I've fallen at the first hurdle trying to use betconnect. I have done pip install betconnect, then if I just run this:



`import betconnect`

`from betconnect.apiclient import APIClient`



I get... ModuleNotFoundError: No module named 'betconnect.apiclient'; 'betconnect' is not a package

*Tags: Getting Started, Errors Debugging*

---

**liam** - *14:52:29*

spent hours on that before, python need to sort that error out

*Tags: Errors Debugging*

---

**Mick** - *15:07:15*

Ok, next problem... in the following code:

`client = APIClient(    username=config("STAGING_BETCONNECT_USERNAME"),`

    `password=config("STAGING_BETCONNECT_PASSWORD"),`    

   `api_key=config("STAGING_BETCONNECT_API_KEY"),` 

   `environment=Environment.STAGING,` 

   `personalised_production_url=config("PRODUCTION_URI"),)`

I think I know what to put for username, password and key, but no idea what to put for "PRODUCTION_URI"

*Tags: Deployment*

---

## 2022-08-08

**rob smith** - *08:29:23*

`I'm having a first crack with Bet Connect but have run into this error:`

`Traceback (most recent call last):`

  `File "C:/Users/James/PycharmProjects/betConnect/betConnectv1.py", line 20, in &lt;module&gt;`

    `personalised_production_url="[https://xxxxxxxapi.betconnect.com/api/v2](https://xxxxxxxapi.betconnect.com/api/v2)",`

  `File "C:\Users\James\AppData\Local\Programs\Python\Python37\lib\site-packages\betconnect\apiclient.py", line 35, in __init__`

    `personalised_production_url=personalised_production_url,`

  `File "C:\Users\James\AppData\Local\Programs\Python\Python37\lib\site-packages\betconnect\baseclient.py", line 37, in __init__`

    `self._set_endpoint_uris(environment)`

  `File "C:\Users\James\AppData\Local\Programs\Python\Python37\lib\site-packages\betconnect\baseclient.py", line 142, in _set_endpoint_uris`

    `assert self._personalised_production_url[-16:] == ".[http://betconnect.com/|betconnect.com/](http://betconnect.com/|betconnect.com/)"`

`AssertionError`

*Tags: Errors Debugging, Deployment*

---

**rob smith** - *08:30:06*

Here's the code:

`client = APIClient(`

    `username="xxxxxxxxxxx",`

    `password="xxxxxxxxxxx",`

    `api_key="xxxxxxxxxxxxxxx",`

    `environment=Environment.PRODUCTION,`

    `personalised_production_url="[https://xxxxxxxapi.betconnect.com/api/v2](https://xxxxxxxapi.betconnect.com/api/v2)",`

`)`



`assert client.environment == Environment.PRODUCTION`





`# Login`

`login = client.account.login()`

*Tags: Deployment*

---

**liam** - *08:31:56*

I believe it should be



`personalised_production_url="[https://xxxxxxxapi.betconnect.com](https://xxxxxxxapi.betconnect.com)",`

*Tags: Deployment*

---

**rob smith** - *08:34:50*

Thanks Liam. That throws a different error:

`Traceback (most recent call last):`

  `File "C:/Users/James/PycharmProjects/betConnect/betConnectv1.py", line 20, in &lt;module&gt;`

    `personalised_production_url="[https://xxxxxxxxapi.betconnect.com](https://xxxxxxxxapi.betconnect.com)",`

  `File "C:\Users\James\AppData\Local\Programs\Python\Python37\lib\site-packages\betconnect\apiclient.py", line 35, in __init__`

    `personalised_production_url=personalised_production_url,`

  `File "C:\Users\James\AppData\Local\Programs\Python\Python37\lib\site-packages\betconnect\baseclient.py", line 37, in __init__`

    `self._set_endpoint_uris(environment)`

  `File "C:\Users\James\AppData\Local\Programs\Python\Python37\lib\site-packages\betconnect\baseclient.py", line 142, in _set_endpoint_uris`

    `assert self._personalised_production_url[-16:] == ".[http://betconnect.com/|betconnect.com/](http://betconnect.com/|betconnect.com/)"`

`AssertionError`

*Tags: Errors Debugging, Deployment*

---

**rob smith** - *08:40:20*

Thanks. Now I get this:

`betconnect.exceptions.UnexpectedResponseStatusCode: Unexpected status code (500) returned for request`

Seems like an issue their side?

*Tags: Errors Debugging*

---

**rob smith** - *08:58:59*

I'm using the dailyhorseracing example without amendment

`Traceback (most recent call last):`

  `File "C:/Users/James/PycharmProjects/betConnect/betConnectv1.py", line 27, in &lt;module&gt;`

    `login = client.account.login()`

  `File "C:\Users\James\AppData\Local\Programs\Python\Python37\lib\site-packages\betconnect\endpoints\account.py", line 70, in login`

    `method_uri=f"{self.api_version}/login"`

  `File "C:\Users\James\AppData\Local\Programs\Python\Python37\lib\site-packages\betconnect\endpoints\account.py", line 188, in _post`

    `status_code=response.status_code, url=response.url`

`betconnect.exceptions.UnexpectedResponseStatusCode: Unexpected status code (500) returned for request: [https://xxxxxxxapi.betconnect.com/api/v2/login](https://xxxxxxxapi.betconnect.com/api/v2/login)`

*Tags: Errors Debugging*

---

**Peter** - *09:49:33*

Mine may be different as I was an early API user, but when I access the production API endpoint, my URI is in the form [https://xxxxx.betconnect.com](https://xxxxx.betconnect.com) and not [https://xxxxxapi.betconnect.com](https://xxxxxapi.betconnect.com)

*Tags: Deployment*

---

## 2022-08-18

**Akwera Junior** - *08:24:37*

Hello, I have a project that I would like anyone to help me complete building.

*Tags: General Technical*

---

## 2022-09-12

**Mauricio Garcia** - *12:51:44*

Hi guys,



Thanks for your votes, interest and the questions you have sent over to us far. We’ll be postponing the live stream session to next week. We’ll keep you posted with the confirmed dates ASAP!

*Tags: Deployment*

---

## 2022-09-22

**Sam** - *12:56:34*

Hey [@U9JHLMZB4](@U9JHLMZB4), we made some changes to `bet_request_get` to improve performance + added some functionality around layside filtering.

I'm not sure what specifically has caused the break because the output for `bet_request_get` hasn't changed, nor has the input.



We've rolled the changes back and we're investigating in the meantime. Can you let us know if you're able to get bet requests through the api again?

*Tags: Performance*

---

**Peter** - *15:03:43*

It's a pretty trivial change my end to drop that parameter. So I'll make the change. Because of the way my infrastructure works, it won't take effect until tomorrow. So if leaving that param out will cause a problem with your current codebase, please let me know ASAP. Thanks Sam.

*Tags: General Technical*

---

**Mark Wells** - *23:18:00*

Hi guys. I'm trying to log in to the api for the first time with a staging account. I'm getting an error in

```client.account.login() ```

*Tags: Getting Started, Errors Debugging*

---

**Mark Wells** - *23:18:17*

```ValidationError: 1 validation error for AccountPreferences

kyc_result

  none is not an allowed value```

*Tags: Errors Debugging*

---

## 2022-09-30

**Peter** - *15:06:33*

Your question appears to be predicated on the assumption that layers on the platform are match bettors rather than traders. Though there appears to be a strong (and actively encouraged) leaning in that direction, it's not wholly accurate.

*Tags: General Technical*

---

## 2022-10-05

**Unknown** - *22:20:44*

Hi Everyone, i was invited by paulliam. My name is Jeffrey and I want to backtest some betting strategies on betfair historic data, and while doing so i stumbled accross the betfairleightweight code. Using the Betfair historic Data Processor, I do get a nice and tidy dataset. However this is a manual excersise and since I will have to do this for 10k+ matches it is not feasible to do it manually. I did some research and it seems to me i need 2 steps in which i am stuck:



1. get the json file into a nice and tidy format (csv), using `json.normalize` it does not achieve the desired result i get this (first image) while im looking for (second image, used by json converter) :

2. Still this is not a nice data set, when i go to [https://www.betfairhistoricdata.co.uk/](https://www.betfairhistoricdata.co.uk/)  I can put in my bz2 file and get a nice output (but this is all manual). 

I was wondering if it was possible to automate this process for a batch of bz2/tar files, so that I can rapidly process &gt;1k matches (files). I cannot find it in the python code of the the betfairleightweight package though. Can somebody help me out please, or point me to the code which does the conversion from json to the nice tidy dataset i get from the betfair processor.



Much appreciated, cheers Jeff

*Tags: Strategies*

---

**Jeffrey Been** - *22:22:19*

If you need any clarification please feel free to ask, I am happy to explain my problem.

*Tags: General Technical*

---

**Mr West** - *22:46:57*

As far as betfair historical data is concerned I wouldn’t go back more than a couple of years.  If you’re strategies are looking at the amount of money being matched then old data behaves differently.

*Tags: Data Quality*

---

## 2022-10-06

**Unknown** - *15:49:02*

Sorry I have to bother again: I am getting an error message when calling the the prices_file_to_csv_file method like this:

`betfairutil.prices_file_to_csv_file("1.119760905.bz2", "betfair_test2.csv")`



Following the signature of the method, I believe I only have to specify input file and output file? I am getting a key_error(see image)? Why am I getting this error and how should I fix this? Again any help is appreciated :smile:

*Tags: Errors Debugging*

---

**Jeffrey Been** - *16:05:09*

I think so: I want to see what prices were available before the event goes into play. The scenario I want to simulate is: what odds are available pre-play, so I can compute the profit/loss for a certain strategy say: only backing the favourite

*Tags: Strategies*

---

**Jeffrey Been** - *16:12:56*

Ah, thats explains the error :slightly_smiling_face: well im gonna look into this branch then. If I have any questions I will post. Thanx a lot for now! Saves a lot of time and frustration.



One final question though: would it be worth the 70 quid to switch to advanced?

*Tags: Errors Debugging*

---

**Jeffrey Been** - *16:21:30*

thnx for all your help:) that was it

*Tags: General Technical*

---

**Unknown** - *22:17:32*

Still getting the key error with the new code:(

*Tags: Errors Debugging*

---

## 2022-10-20

**liam** - *07:56:04*

I think you are misunderstanding the advantages of streaming, the [https://betcode-org.github.io/betfair/streaming/|docs](https://betcode-org.github.io/betfair/streaming/|docs) give a very good overview of why it exists.



So in your example you wouldn't stream each marketId but rather all the markets you require and then process/save what you require.



Although better practice would be to save the raw data via flumine or similar to then allow you to process at a later date when you need that extra field (this will happen)

*Tags: General Technical*

---

## 2022-10-21

**Liam Querido** - *01:57:36*

Ah okay, I was wondering if it would be better to use Flumine rather than just betfairlightweight for streaming.



Do you know of any specific documentation that has what I'm looking for - using Flumine for streaming. After a brief search I see that there is plenty of documentation for Flumine.

*Tags: General Technical*

---

**Liam Querido** - *01:59:39*

I originally thought that Flumine was purely for backtesting, but by the sounds of it, it can be used to stream and save market data to csv?

*Tags: General Technical*

---

## 2022-10-23

**Artiom Giz** - *16:27:45*

Hi people!

I have a question about Streaming API messages rates, can't find an answer in the forum/docs.

Currently I use a "*delayed*" key and MCMs are received once a minute.

If I move to "*live*" key, will I be able to receive MCMs "*tick by tick*"?

I saw in the forum that there is limitation of 150/sec - so this will be the frequency?

*In general, what is the best option to be able to receive updates (MCM) in highest possible way?*

Thanks!

*Tags: Deployment*

---

## 2022-10-29

**Liam Querido** - *14:04:40*

Hi there. I'm trying to use Flumine to stream the Market Book, using the code under the Stream Class subheading from the following link.

[https://betcode-org.github.io/flumine/quickstart/#event-processing](https://betcode-org.github.io/flumine/quickstart/#event-processing)

Nothing is returned when running the code - I'm wondering you could help me understand what's happening here. Note that I also changed the "flumine.add_strategy(strategy)" line to "framework.add_strategy(strategy)."



The code that I am running is below. Please let me know if logging would be useful. Thanks in advance!



from flumine import BaseStrategy

from flumine.streams.datastream import DataStream





class ExampleDataStrategy(BaseStrategy):

    def process_raw_data(self, publish_time, data):

        print(publish_time, data)



strategy = ExampleDataStrategy(

    market_filter=streaming_market_filter(

        event_type_ids=["7"],

        country_codes=["GB"],

        market_types=["WIN"],

    ),

    stream_class=DataStream

)



flumine.add_strategy(strategy)

*Tags: Strategies*

---

## 2022-10-31

**Beeblebrox** - *10:21:01*

Ha ha - classic error! Thanks

*Tags: Errors Debugging*

---

**Beeblebrox** - *11:59:11*

Thanks Joel, I've only just started using BetConnect in the last couple of days and I've been placing bets manually to get a feel for it.



I'd like to set up API access and I've messaged Mauricio, but not sure if he's around at the moment as he's not logged into Slack.



Is there someone else who can help set me up?  Once I have that I think the api link you've shown should be good enough for what I want for now.

*Tags: General Technical*

---

## 2022-11-07

**Unknown** - *20:08:28*

But I get a validation error

*Tags: Errors Debugging*

---

**Beeblebrox** - *20:09:55*

It's because the handicap field on the ActiveBet class is defined as a float, but what's being returned from the API is a string.



[https://github.com/betcode-org/betconnect/blob/6b901b04efc6a630537b12cebd3116d4268da4fd/betconnect/resources/betting.py#L590](https://github.com/betcode-org/betconnect/blob/6b901b04efc6a630537b12cebd3116d4268da4fd/betconnect/resources/betting.py#L590)

*Tags: Strategies*

---

## 2022-11-08

**Jack Broom** - *08:50:54*

Hey [@U01MPC0GUK1](@U01MPC0GUK1), no your not doing anything wrong and this issue was raised in the repo last week.



[https://github.com/betcode-org/betconnect/issues/35](https://github.com/betcode-org/betconnect/issues/35)

*Tags: General Technical*

---

## 2022-11-24

**Yll Kelani** - *22:00:17*

Hey sorry if I've missed something obvious but couldn't find any docs on getting an api key or a "personalised production url" - are these available upon request?

[https://github.com/betcode-org/betconnect#client-requirements](https://github.com/betcode-org/betconnect#client-requirements)

*Tags: Deployment*

---

## 2023-01-10

**Andy** - *09:37:54*

also apologies if not, but is this the right place for the *betfairlightweight* community?

*Tags: General Technical*

---

## 2023-05-23

**Joel Beasley** - *08:51:28*

Hi [@U055JA2PK7F](@U055JA2PK7F) currently it is not possible to get all bet requests with a single call [https://github.com/betcode-org/betconnect/issues/14](https://github.com/betcode-org/betconnect/issues/14)



We are working on changing this, but for now you are right in that you need to hit `bet_request_get` until none are left, and cache the list of IDs - then any can be updated by supplying the ID to `bet_request_get`

*Tags: General Technical*

---

## 2023-05-25

**Sam - DH** - *16:01:53*

Afternoon team, could someone confirm for me please if the customer_strategy_ref is designed *only* to be used on the back side?

Searched far as I could before coming here, [https://developer.betconnect.com/](https://developer.betconnect.com/) suggests it's supported on both, and the bet_request_match and bet_request_match_and_more endpoints seem to accept my custom refs and lay my bets, but am having no luck getting them to actually stick to our lay bets. I did also note there's no mention of customer_strategy_ref in the python wrapper so, requesting backup. Cheers in advance for any help

*Tags: Strategies*

---

**Adam O'Dwyer** - *19:43:01*

Hi Sam, from the BetConnect side - that field can be passed and stored from the Back and Lay perspective. With regards to it sticking, is their a particular endpoint or call that you expect to see it on? I see mention of it in the Betcode betconnect wrapper [https://github.com/betcode-org/betconnect/blob/683cbff1248106613c26038b9a84aecbb5036f1a/betconnect/resources/betting.py#L62|here](https://github.com/betcode-org/betconnect/blob/683cbff1248106613c26038b9a84aecbb5036f1a/betconnect/resources/betting.py#L62|here).

*Tags: Strategies*

---

## 2023-05-27

**Alejandro Pablos Sánchez** - *23:37:54*

Hi everyone, I got a question. When trying to connect to the API, I am getting the following exception error: betfairlightweight.exceptions.LoginError: API login: AUTHORIZED_ONLY_FOR_DOMAIN_ES

*Tags: Errors Debugging*

---

**Alejandro Pablos Sánchez** - *23:39:10*

I'm a beginner in this world so I'm trying to setup a software infrastructure that allows me to automatically place bets on the exchange. Did anyone encounter this problem before? I'd really appreciate if someone could help me. Thanks in advance !

*Tags: Getting Started*

---

## 2023-05-28

**Alejandro Pablos Sánchez** - *12:16:08*

I'm going over it again and what I don't really understand is that, having an account registered in [http://betfair.es|betfair.es](http://betfair.es|betfair.es), it does not work. Does anyone know how to change the login domain or something like that?

*Tags: General Technical*

---

## 2023-05-29

**Jorge** - *07:37:28*

[@U059W9V61QC](@U059W9V61QC) Are you trying to login using certificates? If so the endpoint is [https://identitysso-cert.betfair.es/api/certlogin](https://identitysso-cert.betfair.es/api/certlogin) Can you show us your code so we can help?

*Tags: General Technical*

---

## 2023-05-30

**Alejandro Pablos Sánchez** - *21:49:40*

`import betfairlightweight`



trading = betfairlightweight.APIClient('username', 'password', 'app_key')

trading.api_base = '[https://identitysso.betfair.es/api/login](https://identitysso.betfair.es/api/login)'

trading.locale = 'es'



trading.login_interactive()

*Tags: Strategies*

---

**Alejandro Pablos Sánchez** - *21:51:44*

Hello again, this is the code I'm using changing now the locale attribute but still getting the same error. I cannot figure out why that's happening... Anyone that has been able to login like this can help me? It would be great definitely, getting this to work is being a headache really. Btw, the error I'm getting is the following:

*Tags: Errors Debugging*

---

**Alejandro Pablos Sánchez** - *21:51:46*

[Running] python -u "c:\Users\aleja\OneDrive\Escritorio\Tipster_Auto\src\login2.py"

Traceback (most recent call last):

  File "c:\Users\aleja\OneDrive\Escritorio\Tipster_Auto\src\login2.py", line 7, in &lt;module&gt;

    trading.login_interactive()

  File "C:\Users\aleja\AppData\Roaming\Python\Python38\site-packages\betfairlightweight\endpoints\logininteractive.py", line 30, in __call__

    (response, response_json, elapsed_time) = self.request(

  File "C:\Users\aleja\AppData\Roaming\Python\Python38\site-packages\betfairlightweight\endpoints\logininteractive.py", line 63, in request

    self._error_handler(response_json)

  File "C:\Users\aleja\AppData\Roaming\Python\Python38\site-packages\betfairlightweight\endpoints\logininteractive.py", line 70, in _error_handler

    raise self._error(response)

betfairlightweight.exceptions.LoginError: API login: AUTHORIZED_ONLY_FOR_DOMAIN_ES

*Tags: Errors Debugging, Strategies*

---

**Alejandro Pablos Sánchez** - *21:52:04*

Thanks in advance for any help you cabn provide :slightly_smiling_face:

*Tags: General Technical*

---

## 2023-06-01

**Alejandro Pablos Sánchez** - *18:00:15*

Could anyone give me some help to log in the exchange and place a bet? I would love to automate that process but idk if I don't know how to do it or this is just not possible from Spain. Anyone who has achieved to do this?

*Tags: General Technical*

---

**Alejandro Pablos Sánchez** - *18:01:23*

From the API-NG visualizer looks as working, I can get markets, selections etc, and also using the requests python module. However it does not work with the betfairlightweight module. Any clue? Thanks :smiley:

*Tags: General Technical*

---

**Lee** - *18:04:04*

what’s the error? same as before?

*Tags: Errors Debugging*

---

**Lee** - *18:04:42*

have you tried setting the locale in the way liam mentioned

```trading = betfairlightweight.APIClient(

        "username", 

        "password", 

        app_key="app_key", 

        locale="spain"

    )```

*Tags: Strategies*

---

**Alejandro Pablos Sánchez** - *19:46:58*

Hello again, I'm going over the QuickStart tutorial of the API and I got another question. I'm about placing a trial bet with small size and for that I just find a market that is open and then I pick one selection id at random. The thing is, I'm not able to place it, and I guess it might be due to the following reasons: 



• last price traded does not match the price I'm setting as parameter in limit_order function

• persistence type should not be 'LAPSE', not sure

• order type should not be 'LIMIT'

*Tags: General Technical*

---

## 2023-06-12

**Alejandro Pablos Sánchez** - *21:42:51*

Okey, great, thanks a lot for your help and sorry for the misuse of that channel, I will ask about betfair in the general thread I guess

*Tags: General Technical*

---

**Mo** - *21:44:32*

No worries, just keeps it cleaner for those who are looking for BetConnect help

*Tags: General Technical*

---

## 2023-06-13

**Sam - DH** - *17:39:46*

Cheers for getting back to me Adam - I think maybe I've overlooked the necessity to officially create these strategy refs before assigned them to Bets. Thanks for pointing that section out in BC wrapper, I'll have a mess about with this from here and get back to you if I run into issues. Sam

*Tags: Strategies*

---

## 2023-06-15

**MrRob** - *19:11:48*

Can anyone help me get a list of all football team names that Betfair use, exported into a spreadsheet? Any help would be much appreciated!

*Tags: General Technical*

---

## 2023-06-21

**Peter** - *08:33:42*

Question about BetConnect. Horse racing markets are being opened an hour earlier than normal in honour of Royal Ascot. But they're not available for that extra hour via the API, only the website. Was that intentional?

*Tags: General Technical*

---

## 2023-06-26

**Carl Nielsen** - *05:49:59*

I'm having trouble trying to get the Betfair Streaming API to respond to me..  I'm using Delphi INDY TCPClient and I have SSL set up. I can log in as I have been using the Polling AI for years but I'm not having any success with the streaming API.  The endpoint URL's just result in "Host Not Found" and the integration url appears to open but doesn't respond with the connection message.



Anyone have any ideas ?

*Tags: General Technical*

---

## 2023-08-02

**Riccardo Fresi** - *10:28:21*

Hi,

i nees assistance on connet, since here everything is ok

```session = requests.session()

trading = betfairlightweight.APIClient(

  'xxxxxxx', 

  'xxxxx', 

  app_key='xxxxxxs', 

  certs='C:/xxxxxxx/certs',

  locale='italy',

  session=session)```

then

```login = trading.login()

print(login.login_status)



&gt;&gt;&gt;SUCCESS```

later

```results = trading.betting.list_event_types()

print(results)



    raise APIError(None, method, params, e)

betfairlightweight.exceptions.APIError: SportsAPING/v1.0/listEventTypes

Params: {'filter': {}}

Exception: HTTPSConnectionPool(host='[http://api.betfair.com|api.betfair.com](http://api.betfair.com|api.betfair.com)', port=443): Max retries exceeded with url: /exchange/betting/json-rpc/v1 (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1002)')))```

what's wrong? should use endpoint '.it' but i see '.com'

or the problem is something else?

*Tags: Errors Debugging, Strategies*

---

**Mo** - *13:36:04*

There's something wrong with the way you generated the certificate. To investigate further we need to know what version of Python you're running

*Tags: General Technical*

---

**Mo** - *13:36:34*

Also you are asking for help with Betfair in a channel about BetConnect. You're better off asking in [#C4H05ML2E|issues](#C4H05ML2E|issues)

*Tags: General Technical*

---

## 2023-08-18

**Mo** - *03:03:38*

You’re asking for Betfair help in a channel for BetConnect. You’ll have better luck asking in a more appropriate channel like [#C4H05ML2E|issues](#C4H05ML2E|issues) 



Most likely explanation is a temporary problem on Betfair’s end

*Tags: General Technical*

---

**Troy Edwards** - *05:53:52*

No worries Mo.  Thanks I'll post the question over there.

*Tags: General Technical*

---

## 2023-08-26

**Mo** - *11:12:11*

Understood RE: multiple matches but then my question is simply how to get the times (and sizes) of individual matches? From your answer it sounds like this is impossible from the API?

*Tags: General Technical*

---

**Peter** - *11:16:36*

From the answers I've had to questions to them, I would expect that it is. So certainly worth asking :+1:

*Tags: General Technical*

---

## 2023-09-03

**Mo** - *10:16:22*

Obviously I'm only just getting started with the platform but this seems to be a high incidence so I was wondering if this is a known problem

*Tags: Getting Started*

---

**Ralegh** - *11:27:02*

Hmm ok, were they fixed later? Checked with support? Any market specific rules in play (eg horses)? Seems high

*Tags: Errors Debugging*

---

**Mo** - *12:03:12*

1. No they haven't been fixed

2. No haven't spoken to support, would rather speak to someone on here who knows what they're talking about

3. No, just football Double Chance and 1X2 markets

*Tags: Errors Debugging*

---

## 2023-09-05

**Mo** - *12:02:43*

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



*Tags: Feature Engineering, Strategies*

---

**Mo** - *12:22:49*

I think we've established this is not a known problem which is a surprise given the high proportion of bets I've had it happen on. This suggests perhaps it's something sport specific if those of you who have engaged are not placing (many) football bets



I can take it up with support or privately with the BetConnect guys on here

*Tags: General Technical*

---

**Jimmy** - *12:37:28*

Hi [@UBS7QANF3](@UBS7QANF3), we are looking into these problem bets now 

*Tags: General Technical*

---

**Jimmy** - *12:58:13*

Hi [@UBS7QANF3](@UBS7QANF3), we've identified the issue here. I can confirm that the settlement of these bets are correct, but it looks like there is slight display issue with the decimal odds on some of the bets.



We believe it is due to a mapping error for a particular bookmakers odds. We are looking into this now and will get it fixed ASAP. Apologies for the confusion here.

*Tags: Errors Debugging*

---

## 2023-10-02

**Sam - DH** - *15:28:52*

Hey guys, I've been receiving a lot of 'Unauthorised' API response messages recently (earliest occurred on 16/08).



Couple observations:

• Seems to only occur when attempting to match a bet request, doesn't occur when retrieving bet request info etc.

• Happens maybe once or twice a week, and usually only lasts for around 45mins or so, but it is sporadic and bet-dependant it seems

• Restarts/re-authenticating don't appear to resolve the 'issue'

I've enabled some more verbose logging to determine which node it's happening to etc. If there's no obvious reason as to why this is happening from your end, I can provide more info over DMs.



Todays timestamps of errors are 14:16-14:26



Just curious to see if there's anything I'm doing wrong, and cautious to not be operating out of line with expected use. Having said this, I haven't changed anything in the X amount months we've been working with the API so, a bit stumped.



Any assistance greatly appreciated, cheers in advance

*Tags: Errors Debugging*

---

## 2023-10-06

**Sam - DH** - *13:06:54*

Getting them right now [@U043G3YDB1Q](@U043G3YDB1Q)  if helpful. Last one 13:04. Generic 401 error code whilst trying to lay.

EDIT: Another now 13:07

*Tags: Errors Debugging*

---

**Sam** - *13:18:25*

Thanks [@U035RKUN199](@U035RKUN199), just on a call but will check these in about 45mins.

I spent quite some time some digging into this over the past few days but haven't gotten to the root cause of the issue.

We have a planned release around session management/authentication for next week which I think could potentially fix this but it's speculative without knowing the exact cause.



I'll keep you updated

*Tags: Errors Debugging*

---

**Bookworms Inbox** - *13:45:37*

I have had developed a bot that looks to a certain telegram alert service for football games. The bot then sends the games to a csv for another software called BF Bot Manager to place the bets.



The problem we had was that the team naming convention from the alert service did not comply with that of Betfair and as such the bets were not placed.



We attempted to get round this by having the bot take the team names from the alerts and then comparing them with Betfair, and then interchanging the teams names to suit Betfairs naming convention, then the bot would send the amended team names to the csv for the other software to place the bets.



Problem is, it works well but does not match well, with very obsecure team names being returned, not even related tot he alert team names..



Please let me know, hopefully you can help

*Tags: General Technical*

---

## 2023-10-09

**Elliot** - *18:03:26*

Hi, Is anyone using websockets for price updates?

I have some code but its not quite performing as I imagine.

I subscribe to an event and the websocket is open however i receive no updates in real time. The ws stays open then dumps all the updates at once when the event starts and immediately closes the ws.

I imagined that i should get these onmessage returns as the price updates are happening live as opposed all at once to when the ws is closed.

I can send over code in a dm if anyone can help

Thanks

*Tags: Deployment*

---

**Peter** - *18:52:04*

I get the messages in real-time with no issues using the python websocket-client package.

*Tags: General Technical*

---

**Elliot** - *21:57:44*

Would you mind to have a look at my code if i dm you to see if i have something obviously wrong? I'm using python + VS Code. Im using the websockets doc provided by betconnect team

*Tags: General Technical*

---

## 2023-10-17

**MMW** - *17:17:25*

Cancel Order single bet



[https://api.betfair.com/exchange/betting/rest/v1.0/cancelOrders/|https://api.betfair.com/exchange/betting/rest/v1.0/cancelOrders/](https://api.betfair.com/exchange/betting/rest/v1.0/cancelOrders/|https://api.betfair.com/exchange/betting/rest/v1.0/cancelOrders/)



C# 

{"params": {"marketId": "1.219815567", "instructions":[{"betId": "325032312929"}]}, "id": 1}



How to cancel a single bet I am trying to cancel a bet but cancel all bets back or lay kindly help me, please

*Tags: Strategies*

---

**Peter** - *17:24:07*

This question doesn’t seem to have anything to do with BetConnect.

*Tags: General Technical*

---

## 2024-05-30

**trev** - *11:40:46*

I have api key and url but get error 401 all the time, although winsocket works ok for bookmaker price changes.

*Tags: Errors Debugging*

---

**trev** - *12:34:29*

import betconnect

import requests

from requests.auth import HTTPBasicAuth

from time import sleep



# Define your username, password, URL, and additional data

username = 'developer-not shown here'

password = 'not shown here*'

login_url = '[https://developer.betconnect.com/api/v2/login](https://developer.betconnect.com/api/v2/login)'

balance_url = '[https://developer.betconnect.com/api/v2/get_balance](https://developer.betconnect.com/api/v2/get_balance)'

data = {

    'api_code': '2468163c-5efb-47f1-8952-789ae3d60652'

}



try:

    # Send the POST request to the login endpoint

    login_response = [http://requests.post|requests.post](http://requests.post|requests.post)(login_url,      auth=HTTPBasicAuth(username, password), json=data)

    login_response.raise_for_status()  # Raise an error for bad status codes



    # Parse the JSON response to get the access token

    login_data = login_response.json()

    if login_response.status_code == 200:

        token = login_data['data']['token']

        print('Login Status Code:', login_response.status_code)

        print('Login Response Text:', login_response.text)

    elif login_response.status_code == 400:

        print('Login Error:', login_data['message'])

    elif login_response.status_code == 401:

        print('Login Error: Could not verify Username and Password.')

    elif login_response.status_code == 403:

        print('Login Error:', login_data['message'])

    else:

        print('Login Error: Unexpected status code:', login_response.status_code)



except requests.exceptions.RequestException as e:

    print('An error occurred during login:', e)

    token = None



if token:

    # Introduce a delay

    sleep(1)



    # Send the GET request to the balance endpoint with the token

    headers = {

        'accept': 'application/json',

        'Authorization': f'Bearer {token}'

    }



    try:

        # Send the GET request to the balance endpoint

        balance_response = requests.get(balance_url, headers=headers)

        balance_response.raise_for_status()  # Raise an error for bad status codes

        print('Balance Status Code:', balance_response.status_code)

        print('Balance Response Text:', balance_response.text)

    except requests.exceptions.RequestException as e:

        print('An error occurred while fetching the balance:', e)

else:

    print('Login failed; skipping balance request.')

*Tags: Errors Debugging*

---

**trev** - *13:34:58*

Hi, I have tried but unfortunately I still get the same 401 error

*Tags: Errors Debugging*

---

## 2024-06-04

**Ben** - *11:02:47*

anyone know why putting accept each way to 0 gives me invalid payload error but 1 is fine?

*Tags: Errors Debugging*

---

## 2024-08-30

**Jimmy** - *12:15:11*

Your account should be open, getting an error?

*Tags: Errors Debugging*

---

**Mo** - *12:18:37*

Nevermind, looks like someone fixed it at 10 am yesterday

*Tags: Errors Debugging*

---

