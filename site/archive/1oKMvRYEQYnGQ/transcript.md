# Trading Bitcoin dominance and market structure ideas on Hyperliquid

_Paragon makes abstract crypto ideas tradeable: Bitcoin dominance, Total2, Others as single instruments via HIP3._

**Host:** @hypurr_co
**Date:** 2026-04-16
**Duration:** 32:39
**Tags:** perps, ecosystem, trading
**Source:** https://x.com/i/spaces/1oKMvRYEQYnGQ

## Who's talking

- **HypurrCollective.hl 🐱** (@hypurr_co) _host_
- **Paragon** (@tradeparagon) _host_
- **Taha** (@tahathinks) _guest_

## Key moments

- **[2:32]** Introduce Taha, founder of Paragon
- **[5:34]** Paragon makes buy/sell buttons for front-of-mind ideas real
- **[8:06]** Standardization and exact exposure versus synthetic replication
- **[10:06]** Oracle design: hard to manipulate due to concentration
- **[15:38]** Current liquidity: 1M depth within 100bps for Bitcoin dominance
- **[20:40]** Arbitrage opportunities and low-latency trading games emerge
- **[22:11]** Why Hyperliquid: perps represent unique opportunity for index products
- **[26:47]** Future expansion: crypto indices first, then commodities under consideration

## Transcript

**[1:00] SPEAKER_00:** gm gm we will begin in probably a minute or two just gonna let a few more people come on board first sounds good all right

**[2:32] SPEAKER_00:** i think we can probably just go ahead um it's been a while since hypercode did an ama so uh today we have uh quite a special guest the newest hit three day of paragon uh with us who is the founder of paragon um why don't you share more about your background and past experiences in the industry sounds good how's the audio coming

**[3:02] SPEAKER_00:** through it's great awesome yeah so i've been in the space for a little bit now uh prior to paragon i ran a product studio called meridian lab um we focused on all things you know capital markets tech as it relates to the blockchain really finding a niche in validator and oracle infrastructure um so i i really like to say you know what i was doing immediately before this lends itself well to being a hip3 deployer uh

**[3:32] SPEAKER_00:** before that i spent some time in the solana ecosystem building dow treasury management tooling before pivoting to an analytics website on tokenization and stepping -up on blockchain and money problem uh it's been a while we've been working on the stablecoins called rwa .xyz. You know, prior to my crypto professional career, I spent some time on Wall Street, you know, learning what it means to be a fundamental investor, helping to build out a data platform at an alternative asset manager for the first time. And that's where I really

**[4:02] SPEAKER_00:** saw, you know, during DeFi summer, basically that, you know, my seat there in the debt capital markets and TradFi was definitely in the crosshairs of this new innovation. So decided to kind of leave and start building in the crypto space full time. Nice. What personally motivated you to build Paragon? Like, how different has it been between your

**[4:33] SPEAKER_00:** experience in TradFi and ever since you made the shift into crypto, Web3? How different has it been? Yeah, I mean, it's been a learning experience every step of the way. You know, even between what I was doing before, right, with Meridian and what we're doing now with Paragon, it's very different. You know, before I was very much building enterprise on the enterprise and institutional side of crypto, where a lot of my end users were, you know, developers or engineers at a bank

**[5:03] SPEAKER_00:** or at a crypto financial services firm. So shifting gears, right, and shifting mindsets to thinking of hyperliquid, which is certainly a retail first, right, and consumer first, platform at the moment, although we're seeing a ton of, you know, institutional interest and, you know, some serious Wall Street firms plug in. That's been, you know, a fun learning experience, right, to kind of understand, you know, go to market and customer

**[5:34] SPEAKER_00:** lifetime values and all of these things. Great. So for perhaps, let's touch a bit more on Paragon for those who haven't yet interacted with Paragon. I'm familiar with Paragon. Do you want to share a bit more about maybe just a quick overview of what Paragon is? Yeah. So Paragon is making the buy and sell buttons for front

**[6:05] SPEAKER_00:** of mind ideas and trades real, starting with Bitcoin dominance, Total2 and others. You know, we believe that folks have been tracking these tickers for quite some time. They do an excellent job of describing market participant activity. And I think that's a really good way to kind of understand what's going on in the flow of funds in the crypto space. And what Paragon is seeking to do is basically make those tickers that are inactual, actionable through HIP3 and Hyperliquid. So if

**[6:35] SPEAKER_00:** we can boil an idea down to a data feed, right, and create a robust methodology around it, we're pretty interested in creating a market around, you know, either an asset or an encoded idea, you know, for investors and investors to kind of have a new tool set for exact exposure to the concept or theme that they really want to trade. Yeah. So everyone, I think a lot of people, especially traders, already watch

**[7:05] SPEAKER_00:** Bitcoin dominance and Total2, like you mentioned. What do you think fundamentally changes now that we can trade them with Paragon? So if I'm a trader today, what new trades become possible with Paragon that weren't possible before? Thao, are you still there? I

**[7:35] SPEAKER_00:** think you're on mute. Apologies. How's that? Yep. Hear you loud and clear. Yeah. So I was going to ask, do you need me to repeat the questions? No, I think I've got the question. So yeah. So what exactly is net new about Paragon, I believe was the question. So I think the first piece to note here is the idea of standardization.

**[8:06] SPEAKER_00:** I was saying, this is a concept, that exists in TradFi. You have firms like the S &Ps and the MSCI's that come up with, you know, standardized methodologies for the markets to operate on. So that's the first thing that, you know, the first value add that we believe Paragon is delivering here is standardizing the methodology behind, again, a lot of these consensus front of mind ideas or indicators, because everybody has a different definition of it. So what that does is, you know, it allows traders

**[8:36] SPEAKER_00:** to understand, you know, what exactly the, you know, the, you know, the, you know, the index is, the benchmark is that they're seeing, and it allows market makers to hedge their, their deltas efficiently because they understand what makes up the basket. The other improvement here, right, is this concept of exact exposure through one instrument. You know, it brings capital efficiency benefits. It brings operational efficiency benefit, like not being able, not having to manage multiple legs can get a bit unruly and just like, I guess, overwhelming.

**[9:08] SPEAKER_00:** Yeah. And then it really relates to this concept of being able to trade trends, right? And, and directional flows without having single name risk. So a lot of folks form of an opinion on where they think the market or particular parts of the market is, are heading, you know, before they have an opinion on a specific asset. And we think that this is an incredible tool for discretionary and fundamental traders in the space, you

**[9:36] SPEAKER_00:** know, to be able to take views and then go and do the work that they need to be able to do. And then we have a lot of stuff that's very similar to how they would in TradFi, like, you know, going long or short SPY or QQQ options. So how exactly are these Bitcoin dominance total to and others constructed on Paragon? Where does the pricing come from and how do you prevent manipulation? Yeah. So what's really cool about, about these assets is they're, they're hard to

**[10:06] SPEAKER_00:** manipulate because they're so top heavy in nature. Right? So. So over 50 % of Bitcoin dominance, right, is attributable to Bitcoin. So as long as we have a robust enough oracle in place, you know, manipulating the price to Bitcoin is going to be a costly exercise for some sort of third party, malicious third party. And the same thing with others in total, too. So again, a lot of the weight is concentrated in assets that it would cost

**[10:36] SPEAKER_00:** quite a pretty penny to go out there and sort of manipulate the oracle for the purpose of, you know, messing with Paragon markets. The other thing is, you know, our oracle design. So we've taken a lot of inspiration from what the Hyperliquid Labs team has done. And then we layer on Pith pricing on top of that. You know, so our partners at Pith have really helped out. That gets us pretty solid coverage. And

**[11:06] SPEAKER_00:** then, you know, we essentially fall back to a Hyperliquid inspired mechanism, pulling the same sort of exchanges with the same weights to cover any sort of gaps there. All right. So do you guys do any sort of rebalancing or changes in the underlying components? I know others is probably more relevant here. I think it's like the market cap of all the altcoins, except for the top 10. But I'm not sure

**[11:36] SPEAKER_00:** where exactly the cutoff is. And I suppose. A lot of these tokens on the low end of the range probably changes hands quite frequently. You probably get booted out of the index prefab fast. So, yeah. Do you guys. How do you guys rebalance that? Yeah, we reconstitute every day at midnight UTC. You can actually, you know, reach out and request for we have an index composition API where anyone can

**[12:06] SPEAKER_00:** pull any of the indices. See the constituents. And see the supplies, right? The circulating supplies that we're actually using for our index calculations. So those supplies, snapshots stay relevant for 24 hours and then refresh at midnight UTC. Yeah, you raised a good point. So just to define the indexes, right? The baskets real quick. Bitcoin dominance is Bitcoin's market share of the top 125 assets. So all of these index start with a hundred twenty five, you know, top one twenty five

**[12:36] SPEAKER_00:** asset universe. Um. Others is the top one, twenty five, excluding the top ten total to the top one, twenty five, excluding that coin. Gotcha. I think that's helpful. So for traders right now, they can, they probably express a Bitcoin dominant trade by simply longing Bitcoin and shorting any out stick that they could pair it with. Uh,

**[13:07] SPEAKER_00:** what do you think trading the Bitcoin dominance on Paragon? All right. It's better than what they've done before with the Patrick's. Yeah, it's, it's this, uh, this idea of, you know, exact exposure, right. Versus synthetic replication. Um, so, you know, before the, the S and P 500 ETFs or options existed, the way to go about it was to recreate the 500 name basket. Um, today, you know, the S

**[13:37] SPEAKER_00:** and P is pretty dominated in, in the top seven names, so it's a bit easier to get. Uh, one -to -one, you know, basket replication or as, as close to one, but still people opt for the exact instrument, because again, if, if that's the trade that you have in mind. Um, you always want to choose the instrument that maps as closely as possible to it, right? You want to prevent the site, this concept of drift. Um, so, so that, that's really the, the. The reasoning here, right? Um,

**[14:07] SPEAKER_00:** what, when, when you, you go about synthetically replicating total prizes. total two or others, you're talking about 50 or 40 names to get something that looks even similar to the 125 name exposure that we've replicated through one instrument. Yeah, but I think I fully agree with you here. I deploy long -shot strategies myself. I think it's a lot easier to trade something. So you

**[14:38] SPEAKER_00:** mentioned earlier, you guys work with Parrot. I do use Parrot occasionally because it's a lot simpler to just have one trade than to manage three or four or even maybe 10 different assets that you are long -shot on. Obviously, this AMA is about Paragon, not about Parrot, but you can simplify all those into a single trade. So I think that's what someone can do with Bitcoin dominance as well if they really feel like, oh, Bitcoin is probably

**[15:08] SPEAKER_00:** going to outshine. Or compared to the rest of the market, altcoins are probably going to go to shit. They can easily just long Bitcoin dominance or maybe just short others over here. So I think it's not only starting the trade, like you said, it's also maintaining the trade. So the idea of rebalancing across however many legs gets eliminated when you boil it

**[15:38] SPEAKER_00:** down to. You know, one instrument with exact exposure. Yep. So it simplifies a lot of the execution that traders have. But I think with that, how do you plan to source for liquidity as well? I'm sure like that's probably a very big bottleneck right off the bat. Yeah. So, you know, our liquidity is steadily improving since we've launched. There's about a million in depth within 100 bps for Bitcoin dominance and

**[16:08] SPEAKER_00:** about 600k for the other two indices. At the moment. So, you know, where versus where we were last week, we're talking about a three X improvement. This is this is this is something that will be iterative and warm up. We expect six to seven figures with sub one percent slippage. We're already at six figures for that right now. The idea is to be at seven fairly soon. It just it's just a matter of getting market makers to understand what these baskets are. And you

**[16:39] SPEAKER_00:** know, when we make the analogies to TradFi. And we make the analogies to QEQ and S &P, they understand the hedging mechanisms, right, that are tried and true there can actually be ported over one to one and be applied here. So, you know, we have a lot of market makers who are are ready to plug in fairly soon. It's really just, you know, we're just getting started here. Are you able to share who are these market makers and or if any sort

**[17:09] SPEAKER_00:** of retail? Or pro retail traders that want to basically run their own elbow shop? How can someone on board? Is it as simple as plugging in the API and then learning how to hatch these risk elsewhere? Yeah, so if anyone is interested in making these markets, you know, they are able to via the hyperliquid GUIs or the API. So there's no sort of gate to to do that, you know, completely

**[17:39] SPEAKER_00:** open access. If you want to reach out for an index composition API key, you know, please, please find us on Telegram or Twitter. We're happy to provide that. And that'll give you, you know, the constituents that you need to then start pulling your pricing model together. As far as who are our market makers are, yeah, we want to respect the privacy of them. So let me go back and ask them if they're OK with with sharing that information. I'm not sure that that's something, you know,

**[18:09] SPEAKER_00:** other deployers have shared to date. But yeah, you know, we have we have private contracts with these counterparties, so we want to make sure that we respect them. Yeah, that's pretty much all I've got on that front. Yeah, I think that's totally understandable. With the current assets, it's pretty much all of the names that you would be expecting to be market making on hyperliquid.

**[18:40] SPEAKER_00:** So, you know, a lot of the same folks, right, who are. Who are involved in hyperliquid and HIP3. Yeah, but basically most of the current market makers that are already live, I suppose. Exactly. Yeah, it's a pool of familiar faces, you know, and our goal really is to to make that pool as wide as we can and introduce new parties, you know, both onboard new retail users and onboard new institutional users to hyperliquid. Sounds good. Do you expect any

**[19:10] SPEAKER_00:** sort of arbitrage opportunities between. Program listed assets and other spot and index benchmarks? I'm actually not very familiar because I think if I'm not wrong, there's no outright venue that lists these benchmarks elsewhere right now. Correct me if I'm wrong. That's correct. Yeah. So these are these are exclusively available on hyperliquid at the moment. And yeah, we think that there's some interesting orbs that present themselves. So between the indexes, for

**[19:40] SPEAKER_00:** instance, Bitcoin, you know, along Bitcoin .com. Yeah. So, you know, the indexes, you know, the indexes that represent the dominance or a short to two or others leg if if sized appropriately can can represent delta neutral exposure. What's also really cool is the indices or subsets and ratios of one another. So, you know, constructing total two with an others leg plus assets two through ten, all of which have hyper core perps and HIP3 perps. That is a strategy that you can you can play and, you know, collect a delta

**[20:10] SPEAKER_00:** neutral orb. Yeah. Which which at times is, you know, let's call it mid double figures to the three figure low three figures right now. So we'll see how that persists as the markets mature. But, yeah, we expect a lot of sort of fun, you know, low time frame games to develop. We think that the first folks that that'll enter these markets are traders looking to build OI and kind of swing those positions for several days to months. But then

**[20:40] SPEAKER_00:** around that, we expect a lot of, you know. Fun, low stat orb and lower time frame games to to to emerge. Yeah, you mentioned earlier, so like they're all different ratios and have different weightage of the somewhat crossover with each other. So I suppose on for like HFT firms, they probably have all those coded in their algo. Once the weightage, once the ratio kind of. Yeah. Widen something, you can definitely

**[21:10] SPEAKER_00:** put on a trade. And basically collect that risk for you. Difference in the spread. Yeah, exactly. Yeah. So that's just one strategy that that's emerged. You know, some folks are going like a top down approach. So the idea being you can since these things follow the market more generally, just a handful of the top names right with the most liquid instruments to them will do if you size them appropriately. And then some folks are going the bottoms up approach. So.

**[21:41] SPEAKER_00:** You know, I want to get as many of these perps that are available on hyper liquid. I think that number sits around 80 or 90, you know, of the 125. And I'm going to, you know, get as many of the legs possible in my basket. So I guess time will tell as to what what's the most effective. But we're pretty happy to be seeing a diversity of strategies and thoughts there. Nice. So let's

**[22:11] SPEAKER_00:** talk a little bit about infrastructure. So what do you think? Hyper liquid was the right place to launch this? And what's so special about being a hit three deployer? Yeah, that's a great question. So I think for index products in particular, perps represent a pretty unique opportunity, right? They're kind of having their moment in the sun right now. This product would be much more challenging to pull off in a spot implementation. So for those reasons, you know, building

**[22:41] SPEAKER_00:** on top of perps and then hyper liquid. Being the clear winner in that category was sort of a no brainer for us as product focus builders. You know, hyper liquid allows us to narrow our focus. It allows us to play with infrastructure and developer tooling right off the shelf. That makes a ton of sense for our use case. And it feels the most like a like developing in the world of Web two and, you know, sort of mature SAS companies where you can grab and

**[23:11] SPEAKER_00:** go and ship pretty fast and get something. Out of out to market, you know, rather than reinventing the wheel many times over. So that's what really excites me about hyper liquid. You know, being able to to kind of focus exclusively on this idea of finding product market fit and this concept of turning ideas to instruments and then being able to lean heavily on a network of builders. Right. Who specialize in

**[23:41] SPEAKER_00:** making products where. Yeah. You know, where we're we're kind of consumers of those raw goods. So whether that's data from someone like Hydro Mancer or reliable price feeds from someone like Piff, it seems like. You know, if you need something, it either exists or somebody is actively working on it. I think that's a great part. Everyone's so close to that. And and the fact that anyone can come on and become a deployer themselves of any markets that

**[24:11] SPEAKER_00:** they wish to launch. I think that's great. Out of it with quite a pretty high barrier to entry. But I think that's what democratizes the entire process. What's so great about hyperliquid for trader today? What sort of fees are they looking at when they want to trade on Paragon? So so I know you guys just launched. So the pricing is a bit different. All different

**[24:42] SPEAKER_00:** hip three deployers. A bit of variance in their pricing fees. Do you want to share more about how you derive at your current pricing fees? Yeah. So so we followed the same sort of, you know, one X fee multiplier that a lot of the other deployers have used. I believe all of the deployers, except for Hyena, have used a one X multiplier, which means, you know, they layer on a second layer of

**[25:12] SPEAKER_00:** fees. So that the validators get paid the same amount on hip three markets versus hyper core markets. So fees on on Paragon markets right now sit at three bits and nine bits. We're looking into what we can do regarding getting those lower for users. But, yeah, right now, these are the only places that these these markets are available. You know, we're exploring the idea of. Yeah,

**[25:44] SPEAKER_00:** basically abatements and fees to help kickstart some of the liquidity here. Nice. Do you have any plans to incentivize any sort of trading traders or in terms of fee reduction or any sort of rebates? Yeah. So, you know, we currently have some programs live with TradFi with pair and a few other builders. So, you know,

**[26:14] SPEAKER_00:** if. If those are your preferred. Third party GUIs, or if you want to give them a try, you're more than welcome to go and trade Paragon markets through those front ends or through those APIs. They each have USDC rewards available for at least a week for each of them. We've got a competition coming up with the folks at bullpen as well in a couple of weeks. And yeah, we'll have many more, you know, kind of fun trading competitions to come. Awesome.

**[26:47] SPEAKER_00:** That's great to hear. Perhaps before we open the floor to the audience, let's just end off with a question where you guys currently have three listed assets. I'm pretty sure there's a lot more different markets under this consideration. What can we expect? Do you plan to expand beyond crypto or keep it to crypto assets? Yeah. So for Paragon, we're really

**[27:15] SPEAKER_00:** focused again on crypto. This concept of ideas to instruments. You know, what is front of mind that we can make the buy and sell buttons real for? And while our first indices are crypto focused and crypto index focused and, you know, there's a lot of variance off of those first three that you can kind of surmise as as potential next instruments. Yeah, we were pretty interested in. And again, what was what's kind of like in the current discourse? So that relates to to non crypto assets. You

**[27:46] SPEAKER_00:** know, whether they're brand new commodities that have kind of emerged over the last 10 years or, you know, tried and true ones that have been around for, you know, decades, if not, if not longer. We think that there's some interesting ways, again, to like put process around how folks are viewing them, how folks are viewing the trade, you know, that exists and, you know, ideally purplifying that. So so, you know, the hyperliquid community can can play with it. Exciting

**[28:18] SPEAKER_00:** times. Do you want to and do you have any hints on what kind of markets you're looking at or if I just do you like figuring out if you don't want to share them? I think it's entirely fine as well. Yeah, you know, we're open to suggestions like we very much don't want to be building products in a vacuum and shipping them out there and, you know, having no input from from our community. So feel free to to to tag us or reach out to us if there's something that you want to see get listed. But our basic

**[28:48] SPEAKER_00:** process has to do with, again, like, is is there data out there that's granular enough for us to to create a low latency price feed? At least, you know, the three second threshold that satisfies hyperliquid at a minimum. And then we do a lot of customer discovery. Right. To understand, hey, there's a lot of, you know, ideas that seem solid as as trade related ideas, but actually going out there and seeing whether or not a two sided natural marketplace exists. Or there are natural hedgers

**[29:18] SPEAKER_00:** of this instrument is pretty important. So it's a lot of diligence in vendors on the data side, a lot of talking to traders and funds. I know that that's that's the sort of political workaround to your answer, but a lot of fun stuff in the pipeline. That's great to hear. I think that's a perfect way to cap off

**[29:48] SPEAKER_00:** this conversation. I'll probably just open the floor up. To the audience right now, if anyone has any question, feel free to just raise your hands and ask Taha about what you want to ask. All right.

**[30:32] SPEAKER_00:** Well, if any questions do come up after this, you know, feel free to DM me here at Taha things or you can reach out to us via telegram or email help at Paragon trade. And then our official channel, Paragon official channel on telegram. Yep. Yep. So I think. Can

**[31:03] SPEAKER_00:** you hear me? Yes. OK, I think there was a bit of offline front end glitch on my end as it says that I'm muted. OK. Yeah, I think. Yeah. If anyone has any questions, as usual, feel free to just DM Taha on his personal account on Paragon. Like you mentioned, join the official telegram channel. There's a lot of scams out there, so no one really DMs you first. So always verify the

**[31:34] SPEAKER_00:** handles. Make sure that you're not talking to some scammers. Make sure you're not sending funds to anyone. But if you want to learn more about Paragon, their assets or even be the first to know what markets are listed, be sure to give them a follow. Join our telegram channel. Keep the notifications on. And if any questions, just always feel free to pop in their DMs. So thanks, Taha, for joining us today. I

**[32:05] SPEAKER_00:** think it was a fruitful conversation. So looking forward to seeing more of Paragon on Hyperliquids front end. Thank you. Yeah, I really appreciate your time. And yeah, very excited to see you. I'm excited to finally be live. And yeah, a lot more to come from the team. So yeah, thanks for the time. Thank you. Goodbye. Bye.
