# Paragon Power Perps: convex exposure without expiries

_Paragon's new primitive lets you trade squared and cubed assets with built-in convexity, funding-based pricing, and vault strategies._

**Host:** @rekt_gang
**Date:** 2026-11-11
**Duration:** 38:49
**Tags:** perps, trading, ecosystem
**Source:** https://x.com/i/spaces/1mdRlgWOjEyAel

## Who's talking

- **Rekt Gang** (@rekt_gang) _host_
- **Paragon²** (@tradeparagon) — Paragon _guest_
- **Taha** (@tahathinks) _guest_

## Key moments

- **[5:19]** Zerk introduces Paragon as HIP3 deployer with treasury yields
- **[6:50]** Taha: creating on-chain exposures that don't exist elsewhere
- **[10:51]** Power perps explained: price of asset raised to a power
- **[18:29]** Pay-as-you-go funding vs. upfront options premium model
- **[21:30]** 50-70% gross funding yield on power perp shorts during normal markets
- **[28:35]** Straddle strategy: long volatility bet using power and linear perps
- **[31:07]** Paragon.trade/power with FAQs; vault products coming soon
- **[32:39]** Vision: convexity market for every major asset on Hyperliquid

## Transcript

**[0:00] SPEAKER_00:** GM, GM,

**[2:07] SPEAKER_00:** how you doing? Can you hear me? Hey, how's it going? Doing great. Nice to hear your voice. Likewise, man. How you been? Been good. Today's a nice day. We're getting a

**[2:37] SPEAKER_00:** little bounce. Yeah, we need it. All right. We shall get started in just a couple of minutes. For those that have already tuned in, bottom right corner, there's a little purple bubble. Give the space a like, give a little retweet, drop a comment. Always helps with the algorithm. And we shall get started very, very shortly. By

**[3:16] SPEAKER_00:** the way, the space is recorded and then transcribed. We'll make a little YouTube video out of it. So hope that's okay with you. Yeah, no problem. Have you been trading? Have you been trading a little bit? Have you been babbling in pharma,

**[3:46] SPEAKER_00:** robotics, or other things? I guess AI is always on top of mind, but now it's a little down. I don't know if you bought the dip. Any trading, not financial advice? No. Honestly, we've been pretty locked in on the launch for PowerPerps. So I've done a little bit of trading on the coins, but not much on the stocks personally. Oh, that's cool. I always like to ask what people are trading. It's always interesting.

**[4:19] SPEAKER_00:** Yeah. Yeah. I'm trying to decide when to kind of step in front of this falling knife here. And get wrecked. Yeah, exactly. All right. Very cool. Let's get this spaces started. People are going to be trickling in afterwards. Actually, let me ping Phil one more time here. We shall start. Okay,

**[4:53] SPEAKER_00:** let's do this. All right. So I'm Zerk, co -founder of Wrecking. We run a validator on Hyperliquid in partnership with Hydromancer. So do stake with us if you're staking or don't. It's still cool to be part of the network. And we love to host educational spaces on people that have been working on Hyperliquid builders. So today, for the second time, actually, we have the

**[5:19] SPEAKER_00:** privilege. The honor, the prestige of hosting Taha from Paragon. How are you doing? Doing well. Thanks for having me back. Thanks for accepting it. So means the first time was okay, I guess. And today, I think we have a very different conversation than our first conversation. For those that aren't aware, and I'm going to let you introduce yourself, but Paragon is actually a HIP3 deployer with lots of great tickers, lots of innovation as well, bringing treasury yields.

**[5:49] SPEAKER_00:** Bringing, I guess, you were very early to some companies that, you know, many deployers got afterwards. So really good picks for HIP3, plus some novelty, like I mentioned, the yields and the Bitcoin dominance that you guys had as well, which was very, very new, and now working on a new product. So today is going to be the focus of this conversation is going to be this new product called PowerPerps that I'm very excited. I'm

**[6:19] SPEAKER_00:** curious to learn more about, but you are also right now a HIP3 deployer. So maybe we can introduce yourself real quick and talk a little bit about Paragon, and then we'll deep dive into PowerPerps. Yeah, yeah, appreciate the intro. I feel like the common theme between, you know, everything that you had mentioned just now was, we're really interested in creating exposures on chain that don't exist. That's been the motivating factor. That's been the motivating factor behind

**[6:50] SPEAKER_00:** a lot of our listings on HIP3, right, whether it was, hey, we think the AI trade is maybe more than, you know, just chips and memory stocks. So we brought a lot of optics and photonics names right before that rotation happened, or whether it was something like IGV, where, you know, sort of like a software peer play didn't really exist on chain. And I think, yeah, PowerPerps is, you know, really the next. iteration of

**[7:20] SPEAKER_00:** that, we're still on this journey to, to really find our niche and find like, where we can deliver the most value to the ecosystem. And I think people have been, you know, chatting about options and sort of convex exposure on chain for quite some time. There's been a lot of attempts, you know, both previously and current at kind of bringing the power of of curve payoffs on chain, and we think, you know, what could be different

**[7:50] SPEAKER_00:** this time around is really hyperliquid. Um, not only like the stack that it brings but the fact that like getting a, an idea like this off the ground is really only possible with something like HIP3. Yeah. I love that common theme of trades that you wish existed, and now you guys are bringing them. So now they do, options, right. I feel like there's a lot of talk about options every year, and even

**[8:20] SPEAKER_00:** Jef's talked about it this year. Yet, no, I guess there are some good products. I have used Risk in the past as an options product, but still, I feel like there's something lacking. So maybe this question is twofold. So one, why focus on options? And what do you think is missing from greater adoption here? Yeah, I think as far as like why options, it's

**[8:50] SPEAKER_00:** really like the flexibility that they bring to finance, right? There's a reason that they're so popular. We're talking like quadrillions in terms of notional volume traded per year. And you can just do things with them that you can't do, candidly, with like a linear per. So the idea of being able to get accelerating upside to an asset or cap your downside. These are things that only really exist once you have

**[9:21] SPEAKER_00:** options on chain. As far as why they haven't taken off quite yet, I think it's a couple of things. I think it's, you know, there hasn't been, I think more recently, we've gotten performance enough blockchains and order books to be able to run these things on. But you're still kind of fighting an uphill battle in terms of bootstrapping liquidity across, you know, all of the different

**[9:51] SPEAKER_00:** strikes and expiries. And then I think the other piece of it is just, they're a bit like of a daunting thing to take down, right? Or to kind of grok for retail. Like even beyond just having to pick a strike and an expiry. There's a lot of language around the maths and the Greeks and, you know, even just like, the different types of multi -leg strategies you can run with options that I just don't think are super retail

**[10:21] SPEAKER_00:** friendly. And we think like, you know, perps, like as a form factor actually solve pretty much all of those issues. They aggregate, you know, liquidity from an options chain into one deep liquid book. And then from like a user perspective, they're a lot simpler, right? You don't have to manage any sort of expiry or roll. You're really just thinking in terms of like the familiar, you know, UIs you see with perps where it's just a long

**[10:51] SPEAKER_00:** short button and a lever slider. And we really think like that's, you know, that amongst other things is what has been missing in the past. So where did this idea for power perps come from? Because it's not options, right? It's like a completely new privative. What are power perps? Where that idea came from? Yeah. So very simply put,

**[11:22] SPEAKER_00:** it's the price of an asset raised to a power. The example I like to use all the time is, okay, if hype is going up 2x, then hype squared, right, the power perp would go up 4x. And if there were a cubed perp, for instance, that would go up 8x. So what that does is it introduces convexity to your payoff, meaning every dollar, of rise is worth more than the last one. Whereas with like a linear perp, right, it's kind of the same every step of the way. As

**[11:53] SPEAKER_00:** far as like the history of it goes, back in 2021, some mechanism design experts at Paradigm and a couple of others wrote this paper on power perps. I think it has been discovered maybe independently a couple of other times before that. And yeah, one of the first implementations of that was this product called Squeef. It became like, you know, somewhat of a meme. I think it really just has to do with the fact that Squeef is quite fun

**[12:23] SPEAKER_00:** to say. But yeah, like people have attempted this before. Again, they didn't really have what we have today when it comes to hyperliquid. This was all being done on like a Uniswap MM and hedging like, hedging your ETH delta had to happen on like a totally different venue. So the idea of power perps has existed, I guess, now for about five or six years. And even back then, people were kind of envisioning this

**[12:54] SPEAKER_00:** as like an alternative to an options chain. So why would somebody use a power perp instead of just adding leverage? Like why Hype Squared or Hype Cubed versus, you know, let me just do 10x or let me do 20x? And whatnot. Yeah, I think it really takes like seeing the payoff curves to

**[13:24] SPEAKER_00:** understand this. But the idea is, it's this concept called convexity, which really means like, as hype, the price of hype moves in your favor, your exposure to it is basically like automatically increasing. And so that's really like the benefit of it is you get that kind of kinked, curved option style exposure, right? Whereas like, if you're just sliding the leverage slider from two to 10, you're just really changing the slope of your line. And

**[13:54] SPEAKER_00:** you're just adding more risk on the downside, right? So those are really the reasons that you would use power perps is you want, honestly, like amplified exposure. Aside from that, you can create pretty much any continuous payoff function, right? When you combine power perps and with different weights with linear perps. And then I guess like, one of the other sort of benefits here is you actually get less, or

**[14:24] SPEAKER_00:** like more protection on the downside as well. So if we're looking at like a power squared perp versus a 2x perp, and the trade actually goes, you know, in the opposite direction, the 2x perp will be liquidated before the power does. So you get a bit more cushion on the on the opposite direction as well. So you're doubling down, right? So you're doubling down, or I guess you're squaring down, if price goes up. But

**[14:55] SPEAKER_00:** if price doesn't move so much, you're not losing here, or even if it goes down, you're not losing. Exactly. Like, if you, you know, if you start off 10x levered, and that position starts to gain, right, your leverage, like goes down based on the game. Like how much you've borrowed versus, right, how much, like, actual leverage you've borrowed versus, right, how much, like, actual equity you've gotten the account. So in order to kind of recreate a power perp type of payoff there,

**[15:25] SPEAKER_00:** you would be re -levering every single time the price of hype went up by some amount. Instead of, like, doing that manually, we've really just baked that curved nature into the index itself, into the payoff itself. Yeah. So this is very interesting to me. Like, you guys are bringing a new primitive, adding convexity is what you call it, right? And I think that that's really the definition of it all. How will users be

**[15:55] SPEAKER_00:** able to interact with these power perps? Do they go on hyperliquid .xyz and then they just open, I guess, along on HIP squared? Walk me through the retail experience here on how to use it. Yeah. I think for the most part, that'll be the user experience. People will access this through the hyperliquid front end. So they're going to log in and they're going to be able to see like, front -end or whatever builders they're currently using, you know, just like they would any other Paragon market

**[16:25] SPEAKER_00:** or any other HIP3 market. And then we love for people to kind of build strategy and apps on top of this, right? We really see PowerPerps as like a building block to being able to create all sorts of types of strategies. So we'll actually have a few ourselves out of the box. So a handful of strategies, both on like being able to just bet directionally, maybe bet on volatility just generally, or earning

**[16:56] SPEAKER_00:** yield using PowerPerps. So I'd love to see a world where, again, a lot of the complexities of the management of the different legs are kind of abstracted away from the user. And they're just starting with like, you know, kind of how options work. Strategy builders are built today where they're starting with what they want to do. And like the asset selection is basically handled for them. That's

**[17:27] SPEAKER_00:** very cool. And I think we had discussed as well vaults, right, for people that perhaps want to be participating in one of these strategies, but don't want to do it themselves. So perhaps they can just deposit in a vault and then the strategy runs for them. Yeah. Yeah. I think that that's like an excellent, you know, way of participating on PowerPerps, especially in times where maybe you're not expecting crazy moves on the price. And yeah, like

**[17:57] SPEAKER_00:** I think the kind of classic DeFi vault or vault is, you know, that's an interface that I don't think necessarily needs a bunch of reworking. Nice. So PowerPerps versus options, getting back to it. So you have the convexity with PowerPerps. Yeah. But with options, you usually have the expiry, right? So what are traders giving up here to classical options? Yeah. So

**[18:29] SPEAKER_00:** I think the difference would be paying a premium upfront, right, knowing what your costs are versus more of a pay -as -you -go model with PowerPerps. They're just like any other perp where funding is paid and settled hourly. So that's really like the trade -off. That I think that I think of is, hey, rather than paying this premium upfront for a fixed amount of time, it's almost like I'm renting convexity, right? For as long as I hold the position. Outside of that,

**[18:59] SPEAKER_00:** they function very similarly, right? You can make a lot of the sort of payoff structures with pretty solid approximation. Yeah. I think like, you know, it's really interesting. It's really just this market -driven funding rate versus a premium. A lot of our back tests have kind of shown that we can achieve much better pricing than not only the current on -chain options venues, but those in

**[19:29] SPEAKER_00:** TradFi. But yeah, that's really how I think about it. Rather than like, hey, I'm paying upfront for this convex exposure for a fixed amount of time, we've just broken that into like a funding rate where you're just paying for rent as you go. So how does that work? You know, how does that funding work? I guess longs are going to pay for the convexity and then you can probably have shorts out there that get paid for this or try

**[20:00] SPEAKER_00:** to get paid. So yeah, walk me through a little more about the funding rate. Exactly. So the funding rate is it's set by the market, right? So based on how the market works. The market is performing relative to the index. And what it should track is basically the volatility or the variance of the underlying plus the cost of hedging, right? And hedging happens for power perps on hyperliquid

**[20:30] SPEAKER_00:** on HIP3 markets or on core. So if you're going short the power perp, right, you're going short something like hype squared, you're more likely than not buying 2x delta on hype, right? Through the linear perp on hypercore and collecting the difference in that funding rate. So you think most of the people are going to be hedging, you know, the ones that are going to be shorting hype squared because I'm

**[21:00] SPEAKER_00:** wondering how sustainable of a yield opportunity that is for hedged market makers. Yeah, we suspect a lot of the people coming in on the short side will be those like looking to generate yield, generate income. It's a pretty healthy yield. There's obviously risks involved to something like a game of squeeze and how often you're hedging, re -hedging. But we're talking like 30 % on calm weeks for

**[21:30] SPEAKER_00:** a gross return, somewhere in the 50 % to 70 % for hype squared normally. I mean, more recently, right, the funding rate on hype has been pretty elevated. So if you extrapolate that to what the power perp would pay. And again, like you're, you know, you're getting compensated appropriately, hopefully for the risk that you're taking as a maker. But yeah, we suspect initially some pretty, pretty handsome yield here. Did you say 70%,

**[22:01] SPEAKER_00:** 50 to 70 % in terms of funding that you can, I guess, quote unquote farm or get paid from power perps? Yeah, yeah, on the gross side. So then on the other side, you're still playing out, you know, two times the hype. Funding, which I think historically has been about, you know, 10 to 14%. So almost, you know, I guess, 30 to 50%, depending on your math here. Yeah, exactly. I think those numbers

**[22:31] SPEAKER_00:** sound about right. Yeah, that's really, really cool. I think a lot of the market makers are going to get excited to farm this funding on power perps. You talked a little bit about the gamma squeeze and risks, and I guess what happens in extreme markets? Let's say we get a 10, 10 type of situation. How do you expect these power perps to react or respond? Yeah, basically in a 10, 10 sort of situation, you know, you, I

**[23:03] SPEAKER_00:** think they would respond similarly to like options market, right? So like where the implied vol is kind of spiking and you're seeing that reflected in premium prices. That would just be reflected in terms of like the premium. To the index, right, and the resulting funding rate on the power perp. So the risk that the market maker is hedging at that point is the underlying gapping faster than they can cover, right? That their hedge. So

**[23:33] SPEAKER_00:** they would just be like quoting wide enough. And that would impact the funding in a way where those, those two things hopefully net out. Yeah. And. And ADLs and things like that, I guess could happen as well. Yeah. Yeah, exactly. It would go through the same sort of process, right? With the backstop liquidator and then ADL. All right, cool. But a very new primitive

**[24:03] SPEAKER_00:** still to me and for mine, you know, on hyperliquid as well. So who do you think are going to be the target users? Do you think it's going to be like retail speculators? I'm sure market makers are going to be using it. But who do you expect to be kind of playing with these power perps? Yeah, I think the, on the short side, you know, the natural kind of hedger already exists on hyperliquid. It's people market making, it's people who are doing funding arbitrage trades. And then, yeah,

**[24:34] SPEAKER_00:** I really think it's everyone from the degen speculator who wants to amplify their, their hype returns and not necessarily. Okay. Okay. Who wants to be close risk on a leverage perspective, but then it's also going to be people who are putting on maybe more sophisticated multi link place. Right. So someone who's got experience with things like a straddle and you know, what to maybe buy, sell ball. We talked a lot about hype squared and

**[25:04] SPEAKER_00:** you know, hypeques as well. How far are you guys willing to go on the power and what kind of assets also probably more than height eventually. too. Yeah, I mean, we'd love a world where it's RWA assets, right? We expect to roll those out pretty soon as well. And then I really do envision the powers going everywhere from negative numbers, right, where you're getting

**[25:34] SPEAKER_00:** the same sort of amplification on the short bets. Um, and then, yeah, I think for like assets that are less volatile, um, something like an SPY, like going up to fourths and being able to trade for doses is like, that's not a crazy, super crazy thing. Yeah. I'm wondering how much leverage are you getting if you're doing hype to the fourth power? Like that is more than that 10 X, uh, even at

**[26:04] SPEAKER_00:** cubed as a certain point, it must be more than a 10 X. That you're getting initially, correct? Yeah. Yeah. You'd be getting four times the Delta initially. Um, I guess the other piece here, right, is you can combine power and leverage. So it's not like, you know, you're just, we're just rolling these out at one X. Um, again, we'll, we'll be pretty conservative with them starting off. Um, so something like hype squared will probably not have more than three X max leverage initially. Uh, but

**[26:34] SPEAKER_00:** for, yeah, for like an ether, a Bitcoin. Um, and then, and then, and then, and then, and then, and then, and then, you know, starting at a five or a 10 X like is, is pretty reasonable on the square and the cubes. Yeah. I feel like this could get extremely degen very quickly, especially if price goes up, right? Like you're, you're getting to the power you're gained. So, um, I'm excited to see what the degens come up with. Yeah. Yeah. As am I, I think, again, I really do think there's something for every user here from somebody

**[27:05] SPEAKER_00:** who's like, you know, lives in the, you know, the, you know, in the trenches to somebody who's maybe looking to, um, maybe run like a, a longer tail, you know, if they were looking for like a longer term two X trade, uh, on something like hype, um, perhaps, you know, a one X, uh, squared where you've get, you're actually getting more, more upside and less downside is, uh, a better alternative for them. Nice. Uh, you mentioned RWAs are coming. I think you talked about SMP,

**[27:35] SPEAKER_00:** perhaps Nvidia is, also going to be there when could we expect top squared and all these beautiful assets to the power to be live on mainnet i think you know you guys are very close from my understanding but what what are some of the timelines here uh it'll be pretty imminently so um can't can't reveal too many details but in the very near future here um the first one of these markets will be live nice

**[28:05] SPEAKER_00:** very cool imminent means probably today tomorrow no comments no comments okay no comment is not going to give us more than that that's cool you talked about as well if we're going to a little more advanced here some of the strategies that people can run long power seems very straightforward very simple just pick hype cube or hype squared add some leverage to it you are you are you are betting on a directional trade but you

**[28:35] SPEAKER_00:** also talked about straddle and so what is that strategy uh maybe walk me through some of the other more advanced strategies that you can foresee people uh executing here yeah so straddle is a pretty common concept in in options world and basically what it what it is is uh you're selling two two options or you're yeah buying two options at the same time um and it's basically a bet on volatility so you're buying two two options at the same time and it's basically a bet on like you know long volatility you can think about it as going long volatility or

**[29:05] SPEAKER_00:** like if if the vix for that specific asset existed uh you'd be taking a long bet on that like you know fear and greed index so um if you don't really have a conviction one way or another right you think hype is maybe kind of sitting between support and resistance and you you think it could really break either way what you could do is put on a long strap straddle position which uh for for power perps would be long the power for short

**[29:35] SPEAKER_00:** the linear burp and what that does is it kind of creates a u or a v -shaped payoff where if you know say hype set 70 today if it moves to 50 or it moves to 90 you're getting paid either way nice and we don't have a vix i think anywhere on hyper liquid you can't bet on volatility as far as i'm aware yeah i know that there's a bitcoin volatility product um but

**[30:06] SPEAKER_00:** now there's there's no sort of uh you know single instrument that allows you to go long or short vol right now very cool so i think a lot of people are going to appreciate being able to kind of bet on volatility especially in this market would have been great you know the past year or or year and a half when we had tariffs and then we had war and then we had something else so every yeah every week right even like post you know the ice news with with

**[30:36] SPEAKER_00:** hype going to 96 um you know it's pretty close to that that hundred point of interest that everybody's got their eyes on so right then would have been an excellent time to maybe go long volatility um if you were thinking like hey you know this could be a top ticking type of headline or um 100 you know the hundy rule is coming and we're probably going a little bit past it um so that that's like an excellent sort of use case right there yeah absolutely

**[31:07] SPEAKER_00:** so lots of strategies can be developed with these power perps um coming imminently how else can uh people get involved with with power perps or learn more about them yeah if you go to paragon .trade power we've got a lot more detail there uh also link out to the link in the description box and some faqs um if you're interested in building on top of power perps right whether it's a trading interface or uh one of these custom sort of strategy builder

**[31:38] SPEAKER_00:** concepts that we had we talked about um feel free to reach out uh and yeah other than that um you know we'll have working with some some some folks on volt type of products where um you can participate in the yield generation from power perps from the day one so we'll we'll announce more on that soon um yeah give us a holler if you've got any questions and you know want to get involved want to build on top nice

**[32:09] SPEAKER_00:** very cool uh where do you see power perps in a year time do you see like quadrillions of volume going through paragon's power perps yeah uh that that seems like a pretty conservative estimate within a year's time um no i i think like our vision is really uh a market for convexity for for every major asset on hyper liquid um so if if it's important

**[32:39] SPEAKER_00:** um and it's trading and it's doing you know nine or ten figures a day on hyper liquid on the linear side uh we'd love for there to be a meaningfully sized convexity market alongside that so that you know you're not you're not just trading the assets that you want 24 7. you're trading the specific value of the market you're trading the specific value and exposure you want as well very cool i guess i'll ask a couple of trickier questions do you you know whenever you're a hip three deployer one

**[33:10] SPEAKER_00:** we've seen like everybody copies each other a little bit that that's one question but what about the hyper liquid team implementing power perps like could you foresee that happening i guess they give you lots of credit and revenue for it but wondering if that was one of the concerns i guess in theory they could you know they could go after any market um i think that we think you know they have a core focus right now um where it's the

**[33:40] SPEAKER_00:** crypto perps and building out future primitives um and it seems like they're pretty keen on deployers you know pushing the envelope forward when it comes to new market and new asset creation um so not a super high perceived risk on our side um yeah as far as like other deployers i don't think there's a lot of risk there but you know in in the copying and playbooks like we're on a mission to you know to bring new exposures to hyperliquid um i think that's been super clear from our our

**[34:10] SPEAKER_00:** curation right like none of the the assets we've chosen to list uh exist on on hypercore already um so for us it's it's really about like yeah is there something new we can be doing um and not only that like can it be pretty important right and huge at the end of the day you know speaking of huge i know you're based in the in the u .s and uh lots of talks about regulation in the u .s having perps in the u .s i think ice news

**[34:40] SPEAKER_00:** you talked about that do you expect one just to to grow through soon and two do you expect power perps to be available in the u .s as well yeah i think um you know functionally a power is no different than a than a normal perp so uh i expect them to fall into the same sort of buckets right we've got crypto and commodity and equity perps um i'm pretty bullish yeah i think uh

**[35:10] SPEAKER_00:** i think we'll probably see some somewhat of a battle on the equity perps front at least um but as far as commodity and crypto perps go from my perspective you know it seems like we're getting the green light there pretty soon um it's just a matter of like presenting a regulatory compliance solution and getting it signed off by the regulators nice yeah i'm hoping it all goes through very soon i'm not even in the u .s i just you know feel

**[35:41] SPEAKER_00:** like it's gonna pump all our bags which is great yeah yeah i think a lot of the questions that you know a lot of the theses and a lot of the hypotheses that people have about the benefits of perps um are finally getting like meaningful you know experimental playgrounds so um yeah as as as like a spectator i'm excited as a participant um i'm very very very happy i i keep saying that to people perps is such a new primitive i

**[36:11] SPEAKER_00:** think people still aren't you know nobody knows how to trade them very well still to this day or very few um and now you guys are coming out with power perps the space moves so fast yeah yeah exactly and i think like there has been you know um an ability to test this on a large scale like the only kyc you know meaningful perp venue right now is finance and um i

**[36:41] SPEAKER_00:** don't know about you but like it's it's kind of hard to take them at face value for what their numbers are are uh are saying so i think just like from a pure curiosity perspective like i'd i'd love to see how this plays out yeah it'll be it'll be very exciting times in the next couple of years all right uh anything else you wanted to share with the audience in terms of how they can get involved with power perps or i guess they can use paragon today

**[37:11] SPEAKER_00:** to long some of your hip free markets you got lots of them i think launching yeah even i think recently what did you have oh i really like the paper one i i'm and i'm sorry for everybody that got a little rugged on paper trade really like that market felt like that was so genius i'm just sad that they had to fumble it so hard but uh that was a really fun one yeah that was quite an exciting and yet short rollercoaster ride um we'll

**[37:42] SPEAKER_00:** see you know i i saw that those guys put out some updates yesterday so we'll see what the future has in store for uh for both their project and i guess our market um but yeah i guess uh we're always looking for feedback criticism um and yeah if you want to learn more about power perps our dms are open nice very cool thank you so much for the time taha appreciate it uh looking forward to playing with the power perps seeing what vaults come out seeing what

**[38:13] SPEAKER_00:** strategies come out and yeah exciting times in the hyperliquid ecosystem hope we can have another chat and i guess in when you have quadrillions of volume in a year start awesome i'll see you then thanks for having me all right thanks for everybody tuning in this space is recorded will be transcribed and we'll make a small youtube video out of it as well so thanks again and have a lovely green day
