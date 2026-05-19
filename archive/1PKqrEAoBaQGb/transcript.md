# 80+ teams building on Hydromancer: infrastructure, HIP4, and trader profitability

_Xeno from Hydromancer shares data insights, HIP4 prediction market strategy, and how 29% of Hyperliquid traders are actually profitable._

> Hyperliquid uniquely cultivated a community of people who actually want to trade, unlike Binance or Coinbase.
> — Xeno, Hydromancer

**Host:** @rekt_gang
**Date:** 2026-04-22
**Duration:** 1:00:40
**Tags:** infrastructure, ecosystem, perps
**Source:** https://x.com/i/spaces/1PKqrEAoBaQGb

## Who's talking

- **Zerk** (@rekt_gang) _host_
- **Xeno** — Hydromancer _guest_

## Key moments

- **[5:07]** Xeno introduces Hydromancer's origin: HyperDash experiment
- **[7:09]** HyperDash acquired by pvp.trade, Hydromancer pivots to infra
- **[11:48]** 80+ teams using Hydromancer for data, market-making, and app building
- **[13:49]** Priority fees system: REITs vs RFQs explained for execution speed
- **[20:25]** HIP4 prediction markets coming soon, more creative than HIP3
- **[33:04]** Xeno predicts HIP4 launch in early June
- **[40:12]** Research paper: 29% of Hyperliquid traders are profitable
- **[44:16]** Eastern European scalping terminal shows 80% user profitability

## Transcript

**[3:05] SPEAKER_00:** gm gm everybody happy wednesday we shall get started very shortly oh there we go it seems it's working how you doing hydromancer i don't know who i'm speaking with hello hello can you guys hear me yes we can hear you loud and clear are you joining from the desktop yeah i'm joining from the desktop with new tech good tech yeah elon does not phone there um

**[3:35] SPEAKER_00:** funny enough you could only host spaces from the desktop just only a month ago so this is like the latest and greatest of x -tech wow incredible incredible that they uh they've done it you get a beer has done it again oh i love that dude he's hilarious um all right so for those that just joined the space bottom right corner there's a little bit of space for you to get a little purple bubble you can click

**[4:06] SPEAKER_00:** on the purple bubble drop a comment retweet the space give it a like always helps with the algorithm um and we shall get started in just one minute i'm super excited about this space y 'all have been cooking on hyper liquid for such a long time i'm very proud and happy that we're collabing together on the validator as well but that's a separate thing um really want to be talking about what y 'all have been doing for a long time and i'm excited about what you guys have been building and

**[4:36] SPEAKER_00:** about hyper liquid as well as your new research paper that just came out today so that's exciting yeah well uh i'll give a bit of background about us so um yeah let's get the spaces started all right so i'm zerk co -founder of wreck gang and today we have the privilege the honor the prestige of hosting the team at hydromancer so how about you introduce yourself real quick and then we'll go from there well

**[5:07] SPEAKER_00:** yeah as i said i'm xeno founder of hydromancer and we've been building on hyper liquid since 2024 so me and my co -founder previously have been building products in crypto and well our first product didn't really take off and around the same time we started trading on hyper liquid as well and in 2024 absolutely blew our minds because it was a dex that

**[5:38] SPEAKER_00:** felt good to use like that was actually a nice product and that was the first i think my co -founder used to trade on dy dx before and hyper liquid was much much nicer right um so then we decided hey uh why not we start building on hyper liquid as well and it really started as an experiment because we realized hey the data is open

**[6:09] SPEAKER_00:** and transparent right like when you can see how leaderboards traders are positioned right so how are people who are actually making money in our position hyper liquid um so yeah it actually it actually started as an excel sheet because basically we just pulled some data from apis and then sent it to a couple of trading chats yeah said like hey do you see the power of excel yeah yeah yeah so like i said to a couple of like trading chats and

**[6:39] SPEAKER_00:** said oh you can see like the winning traders are like very long btc and very short old whatever right and then people started asking oh what are their updates well they're long now can you add more traders to the yeah to the absurd list and that basically became hyper dash then we found like uh third core team member who helped with frontend and yeah who

**[7:09] SPEAKER_00:** was helping with everything like UI and that became HyperDash and that really took off in 2025 when they were like these weird insider traders on HyperLego and then everyone was sharing these trades and then the HyperDash team blew up and it got acquired by the incredible team at pvp .trade who are now turning it into a proper trading terminal and

**[7:40] SPEAKER_00:** we decided to focus all in on infra and data because as someone who built a very data -heavy product from HyperLiquid, early ecosystem dev tooling was like bad but it was very bad it was like a four data -heavy product was like especially bad it felt like just bad. It was like chewing glass basically so we thought about it and decided that nobody has to go through the same pain again ever.

**[8:14] SPEAKER_00:** So getting back to HyperDash that was a product that I feel a lot of people are familiar with on HyperLiquid I think everybody has seen the interface at some point or has used it and now it's operated by pvp .trade do you feel you know I guess this is a little sidebar but do you feel there's still opportunities in copy trading I know loracle kind of

**[8:41] SPEAKER_00:** opened the hype short yesterday and the btc long he's in profit do you think like copy trading is still a thing or all these advanced traders are now so good because of HyperDash because of getting copy traded so often kind of to obfuscate their strategy or their market making? Well I think it's a good question. I think ultimately copy trading is very very hard to solve because well you

**[9:14] SPEAKER_00:** don't really have a lot of control over what the trader is doing and I remember seeing stuff like there was this popular vault and people just well copy traded it and deposited it to the absolute cap of the vault and then the guy just blew up right and a lot of people lost a lot of money basically well the reason is

**[9:44] SPEAKER_00:** well it's just how it works even it works like this with like hedge funds right there's often people just chasing good performance and withdrawing at the bottom but in general I think it's quite tough but aggregating what winning traders are doing is quite cool so I think some kind of like semi -discretionary copy trading works very well when you understand the thesis.

**[10:15] SPEAKER_00:** Nice I love that don't just blindly copy trade without you know not knowing what the you're doing if you have a thesis and it kind of aligns with somebody that's a good trader I guess that makes sense right? Yeah yeah I think that makes a little sense. And yeah and then also people like then some people like once insane

**[10:46] SPEAKER_00:** risk I remember like one of the funniest stories was that when we were starting Arbor Dash copy trading people asked us to leverage copy trading and we were like why would you do that why would you do that? This is the pump fund era yeah 20x is not enough they want they want more that's

**[11:18] SPEAKER_00:** funny um all right so after hyper dash y 'all decided to really focus on being the data layer for hyperliquid so talk to me about you know the genesis of hydromancer and what you guys are focused on today yeah so today we're mostly focused on data pipelines and dev tooling so the boring stuff right but I think we're becoming an

**[11:48] SPEAKER_00:** important pillar for the ecosystem and like currently 80 plus teams are using us in some capacity I think you can prove like our clients in one of three groups first is our app builders we need data to well

**[12:18] SPEAKER_00:** build their terminals uh and get advanced features to the users second are market makers who obviously need the good data from hyperliquids uh for their trading activities and then we're also very active with uh hip3 and hip3 deplorers and well hopefully we'll also do that in the near future. We'll be very active with hip4 as well and we actually already rolled out oh snap

**[12:50] SPEAKER_00:** hip4 is coming um so you know you told me that you have market makers app builders and uh perhaps some hip4 stuff coming up uh let's focus on the first one so you know one of the big things that came out last week was the implementation of this fee system which is kind of a你以我所知是一個益心的規定 for market makers to have

**[13:19] SPEAKER_00:** their transaction come in earlier basically to have priority I wouldn't call it MEV um I would call you know just basically a fee system here uh and previously there was no fee system so how does that work like who who gets to be fastest before they implemented this who was the fastest before yeah so I guess

**[13:49] SPEAKER_00:** it's important to say that um I guess it's important to say that that there are two types of priority fees. One are REITs, right? And the other are rights. So rights are more straightforward. It's basically, you can pay up to eight dips, which is basically like basis points, 100 % to get your order in faster. And REITs

**[14:19] SPEAKER_00:** is basically getting your data faster, right? Getting the data, like everything that's happening on Hyperliquid and reading it faster and acting on it faster. And well, before that I was, it's still like to a huge degree infrastructure optimization, but before that I was, even more of that. But I

**[14:52] SPEAKER_00:** think it's also important to say that the infrastructure optimization on Hyperliquid is not at the same level yet as normal exchange and track by world, because they're like two milliseconds is already an eternity rate. And Hyperliquid is slower. Well, it is slower. So it's not as

**[15:21] SPEAKER_00:** important. Yeah, cause I heard if you had like a server in Singapore or I think somebody posted like in Japan, they get like quicker execution of transactions than if they're located, I guess in the U .S. or North America. I don't know if that's true, but now with these fees, the playing field is kind of more level. I'm not sure, actually, like because,

**[15:51] SPEAKER_00:** because. the like the servers are in japan yes but the there was some kind of like a speed bump already right so and obviously if you do one like fastest data you would um co -locate in japan but for like a random retail user i think because of

**[16:21] SPEAKER_00:** the speed bump the difference was um not that yeah it's definitely not for me but i'm wondering like the market makers they probably want the fastest you know execution they want to be in there first right so to me that would make sense for them to use hydromancer and i'm sure some of them do they kind of leverage your infrastructure to be the quickest one out there well i mean our servers are also in japan right and uh that's uh i'm

**[16:52] SPEAKER_00:** not fully sure about the how that came to be but i think most of the like og crypto exchange exchanges had servers in japan and that's how japan became the well the dominant venue really because i think binance was located there and then just everything crypto started being located there because well binance was already there and binance is the price

**[17:23] SPEAKER_00:** discovery venue nice so uh you help market makers basically be the first on chain is that accurate partially i would say because um some uh because obviously like market makers have to do like a lot of optimization themselves and they all have uh they all have their strategies right and we can only help

**[17:53] SPEAKER_00:** with uh getting good data to them fast essentially nice and um so outside of the market makers you mentioned the builders right the app builders i think you guys work already with kinetic and native markets and all those teams already kind of your your guys's infra um to get data create some cool dashboards as well uh lots lots of cool tech coming

**[18:23] SPEAKER_00:** out that is powered by you guys yeah well i mean for app builders i guess i could tell like a bit more than uh market makers because there's also well uh more fun stuff and more stuff that well issuers can actually touch and experience right um well hyperliquid native apis they're good for um building like a normal trading terminal but they're

**[18:54] SPEAKER_00:** not optimized for builders right and um that's essentially what we did we kind of channeled our own pain that we experienced when we were building hyperdash and also well uh what are the builders we're talking about selling as they lack currently and this will kind of became our um our product and i guess

**[19:25] SPEAKER_00:** if i had to explain it without using like any technical terms i would just say that it's the easiest way to ship on hyperliquid i love the painless ways i love that and there are so many builders right on hyperliquid it is one of the i feel the most exciting venue to be building on today and you guys get lots of the man for this um and

**[19:55] SPEAKER_00:** that allows me you know we spoke about the teams that are already using you everybody's familiar with them if you've spent some time on hyperliquid um i want to talk about some of the teams that maybe we're not familiar with and perhaps you're not allowed to disclose which is fine but what can you tell us about people building hip4 right and anything you can tell us about people building hip4 right and tell us about hip4 in terms of like prediction markets are coming soon when do you anticipate

**[20:25] SPEAKER_00:** this and will we have like a front end right from the start like i have so many questions on this and if you guys are working with teams on this already i'd be like super interested in learning more yeah well i think that hip4 is going to be more fun and creative than hip3 first of all because there's just um more

**[20:57] SPEAKER_00:** stuff that you can build essentially right because well hip3 is obviously important but well there if you deploy to deploy a market and then well you just trade this uh delta one uh product right with hip4 it can be binary options it will be like politics markets eventually uh well really just anything and then you can also be

**[21:26] SPEAKER_00:** very creative uh in terms of ui and ux right and create um almost like an app where you like swipe on each market right you can just copy like bullion market ux or you can create the like app with uh having have an analytic flare right so i think there's just the creativity surface is much larger so that's interesting and i also think that hip4 markets for sure

**[21:56] SPEAKER_00:** for the floors uh can also be more creative right because one team can focus on sports the other team can focus on politics then also stuff in binary auction i think there's just that's an excellent point right because for hip3 i am most bullish on hip3 by the way i'm i'm not the biggest fan of these binary markets but i know they have huge pmf some people love it and And

**[22:26] SPEAKER_00:** yes, sometimes I will place a sports bet on Polymarket, but just for fun, usually small amounts. That being said, you're very correct in saying they can be more fun than HIP3 because HIP3 right now, it's get listed on Hyperliquid front end and then trade from there. That's it. I think TradeXYZ has a great UI, but I don't go there. So does Native Markets. I don't really visit it either, even though I think they have some new features

**[22:56] SPEAKER_00:** now. But with these binary prediction markets, you mentioned like, you know, they could have, it's like that Facebook app, right? That Mark Zuckerberg had like our hot or not, swipe left, swipe right, or I guess Tinder. And people can really explore outside of the box with these markets compared to what is currently done with HIP3, which is okay. Maybe I have like OpenAI or something like that, but the

**[23:27] SPEAKER_00:** UI, UX is still just the front end of Hyperliquid. It's not so complicated. Yeah. So I think there's, yeah, there's a lot of stuff that you can build. And also, I mean, I think everyone here is bullish, right? On HIP4, obviously, but. How bullish are you? How bullish are you? Are you more bullish? I'm quite bullish. And I think the. The reason is that Hyperliquid uniquely

**[23:57] SPEAKER_00:** cultivated a community of people who actually wants to trade, right? Because you would think how difficult it is to launch like an S &P 500 or an oil. I mean, it's not, it's not rocket science, right? It's just picking good, well, Oracle and then like, yeah. It's not rocket science, right? But Binance and Coinbase didn't manage

**[24:28] SPEAKER_00:** to get any traction on their products, right? And the reason is that the audience that they cultivated for years is just not conductive to getting actual real traction on these products anymore. Well, I'm just quite various about Binance, I guess, like you can hear it. But it's like. It's like we are aligned on our Binance bearishness. Yeah. It's like you

**[24:58] SPEAKER_00:** basically have all of these like insane bump and dumps happening on your platform, right? And I guess you just. Okay, let me flip it on you here. This is a good point that you raised. You're saying Hyperliquid did an excellent job at cultivating a trader community, hence HIP4 is going to be very successful because they have this trader community. So the flip question is, how bullish are you on Polymarket and Kalshi

**[25:29] SPEAKER_00:** perps because they kind of have this D -gen binary lovers. I don't know if they're going to like perps, but I would call them a trader community as well, unless it's all bots just trading between each other. I don't know, like how organic Polymarket and Kalshi is, but it seems like they have some real world adoption. Well, I'm not. I'm a bearish. I'm a bearish. Yeah, but like I actually said it, and I even have receipts of this. I said it like for

**[25:59] SPEAKER_00:** a long time. I think like obviously Kalshi and Polymarket are going to converge on well, perps as well. Right. I didn't expect them to announce it the same day because that was insane that they actually announced the same day. Right. But I think it's just obvious that they would verticalize there as well. So I think it's also a matter of

**[26:29] SPEAKER_00:** execution. Right. But the problem for Polymarket, I think it's also like their info is not good. It's still on the Polygon blockchain, bro. You don't want to mess with that. Yeah. And then there's also, I guess, like there's also the approach is also quite different. I think. For example, there is the. Yeah. There was this like

**[26:59] SPEAKER_00:** Y Combinator Polymarket API startup that I think got acquired by Polymarket itself, basically. So they just got like acquired on Polymarket, by Polymarket, essentially. Yeah. The whole team. Yeah. So I think in this sense, like Polymarket and Colossio

**[27:29] SPEAKER_00:** is way more centralized. It's a different approach. Yeah. You were working with hip four builders. Do you know anybody that's working to build a product on top of Polymarket? Most of the time? No. Right. Like most. Folk that are building in this prediction market space. Are. They want to develop their own prediction markets, which I don't think is a good idea. Because unless

**[28:00] SPEAKER_00:** they have like some huge differentiator. But in this case, we might see the coming of a new trade X, Y, Z, or the coming of a new native markets, a new team that builds on top of Hiker liquid that gets great success. And perhaps downstream some other teams, I think like Phantom, for instance, who integrated the builder codes and I don't know, all these different apps. I feel like just the fact that it's going to be so easy to build on top of it and integrated gives

**[28:31] SPEAKER_00:** a huge edge to hip four or hyperliquid versus Polymarket and Colossio. You're trying to retain most of the business themselves. But you've probably, you know, that's why you're working with so many hip four builders. So, so tell me more, how many teams are working on hip four right now and what can you tell us more? Well, there are teams that are exploring currently, right? And there are teams that are looking to

**[29:01] SPEAKER_00:** be deployers. So and eventually, I think every prediction market terminal is going to integrate hip four. And yeah, well, I think most of the people building on Polymarket. Are trading terminals, which is essentially same as teams who

**[29:31] SPEAKER_00:** use builder codes on hyperliquid. Basically the same thing. There's also like a couple of info startups and there's also teams who do like leverage and margin on prediction markets. So that's basically the ecosystem. I'm not that deep into prediction market eco, but that's

**[30:02] SPEAKER_00:** basically what exists for Polymarket and Colossio. And I think it's going to be pretty much the same for hip four. I think there are already a couple teams who are trying to be the first prediction market terminal on hyperliquid and they're hyperliquid native. One is liquidiction. Yeah. That's the one I saw. I saw that one.

**[30:32] SPEAKER_00:** What a weird name. Who came up with that name? Let me pin it. Well, I mean, I think it's fine. The other one is Azali, I think. And these are both, I think, hyperliquid native builders. Yeah. I think they're both, like, hyperliquid native builders who just basically saying, okay, hip four is a new thing and then we are going to build the best hip four experience. But I think the

**[31:03] SPEAKER_00:** same kind of verticalization is going to happen. So for those that are familiar with this one. And everyone is going to have a hip four, hip three and whatever else. Yeah. I pinned up top on the nest here for those that want to check out liquid diction. Oh, boy. I feel like, yeah. It reminds me a lot of liminal as well. This logo. But anyways, that's besides the point. I did click on the dashboard and it does look good. So

**[31:33] SPEAKER_00:** it looks good. And when is hip four going to be live? Have they told anybody? Probably not. Sorry. Again. When is hip four going to be live on mainnet? Nobody knows. I think. Well, a hyperliquid core team. The core team is quite tight -lipped about that and so I think they're still testing

**[32:04] SPEAKER_00:** and nobody knows. And then, well, they also rolled out this priority fees, which I think was their focus for a bit. So there's that. But then again, they should work quickly. So subject to chicken shred, for example, with priority fees. Yeah. They launched it on testnets and then like three days later it was already on mainnet. So

**[32:34] SPEAKER_00:** if you had to have an educated guess, you know, if you had to do a prediction market on when hip four would launch, what would be your bet? June. I think I would say June. June. Oh, okay. So not this month, not next month, but the month after. I thought. Yeah. It was like second, second half of May. Yeah. Okay. So like from second half of May to like early June.

**[33:04] SPEAKER_00:** Early June. Yes. But now I'm like hedging my bets a bit. But I don't know. I think it's going. Yeah. It's going to be launched quite soon. Okay. Cool. I think a lot of people are excited to see if they can get some of that prediction markets market share. Pretty sure they will. But how much? I think that is the big question. It's just like any perp decks that launches, you know, right? Like it's very hard for them to get a significant chunk

**[33:34] SPEAKER_00:** off of hyperliquid. They do get some people that want to be farming points and whatnot, but then that's about it. So polymarket and being so old as a prediction markets, I guess, you know, it's going to be hard to displace, but we'll see, especially if they offer a better experience, better transparency. And perhaps easier to build upon for new teams to come in basically. Yeah. And there's also like two elements to

**[34:04] SPEAKER_00:** it. So I think the binary options part is like the easier part. I think that they could release quite soon, I would assume. Why? Because, well, the Oracle, you can basically, it's like a self -contained system, right? Because you can use hyperliquid reference price for your binary options thing. So yeah, like what is going to be the price of pipe and then you just use like mark price or like mid price on hyperliquid, it's quite obvious, right? But

**[34:36] SPEAKER_00:** obviously politics and other things like that, it's a much tougher problem to solve, right? Because a lot of problems are also like on polymarket or due to their like UMA integration, which sucks, which is horrible. Yeah. So how will they solve for that? Because I have Trendy down here actually got really pissed that one of the polymarket bets that didn't go his way, I think it was something

**[35:06] SPEAKER_00:** like shaking the hand of the president of China and then they did that, but UMA said no, right, for some obscure reason. Like those instances happen all the time, like UMA whales controlling whatever outcome they want to be controlling, which makes it... A complete joke. But how will hyperliquid solve for this? No idea. Like I don't think anybody knows,

**[35:37] SPEAKER_00:** but they're obviously like great Oracle teams in the space like SATA and others. But yeah, like I think it's still... Nobody really knows. Okay. Well, it's again, it's also less centralized than bullet market of culture. So hyperliquid would have to design a system which is secure, but

**[36:09] SPEAKER_00:** also that's not like authoritarian in a sense. Yeah. I feel like that's a big challenge and yeah, you're right. If we get some sort of transparent, neutral way of determining if a market is resolved, yes or no. Yeah. Yeah. But sometimes there are gray areas, right? And so that's kind of like my concern on how they handle this, but I'm bullish on the team. So I think they will. Yeah.

**[36:41] SPEAKER_00:** Well, I'm also quite bullish, I think. I think it's going to do really well, but also it's quite an exciting time, obviously. Like everyone is trying to verticalize, everyone is trying to win. So obviously we're all afraid. We're all here rooting for hyperliquid, so let's see, but competition is also quite good. Yeah. Makes for a better product ultimately. So everybody wins. Okay. So

**[37:11] SPEAKER_00:** now we spoke about the market makers, the app builders, and the hip four. I want to talk about a public goods that you guys launched. I want to call it that way, called Reservoir. So this is also pinned up top on the nest, on the spaces. And this allows anybody to get the components. It's a complete historical hyperliquid data, free forever. Isn't that so cool? We had so many issues with data before, and now you

**[37:41] SPEAKER_00:** guys are allowing this. Well, yes. We think it's cool. That's why we launched it, right? And we think it's very important, really, that people can actually verify that. Yeah. Hyperliquid traction is real. All the trades are real. You can go and verify. You can do it for free, right? So we didn't charge anything

**[38:11] SPEAKER_00:** for it. You just go and verify. So I think that's cool. And yeah, we also always had problems with pricing for historical data because it's kind of always annoying, right? Most of our, I guess, business are... Yeah. Most of our apps who signed for our real -time stream data for monthly subscriptions, right?

**[38:42] SPEAKER_00:** And then historical data was always kind of weird. Yeah. It was just a one -off export for that. And then we thought, okay, people are actually asking us to verify what's happening on hyperliquid. Why don't we just make it available for everyone for free? Because well, it's kind of transparent anyway. And I think it's very... It's very aligned to

**[39:12] SPEAKER_00:** hyperliquid ethos, so. Yeah. Well, thank you for that. Yeah. Definitely aligned with the ethos. I think that post has like a thousand likes or something. A lot of people are very happy about it. And from that, right? I think it's a great segue to talk about what you published today, which is to me in all essence a research paper on, you know, people building. People building. Yeah. People building on hyperliquid. That's one thing. But

**[39:42] SPEAKER_00:** most, you know, these builder apps. So what did you discover from this research paper? And maybe you can kind of real quick tell us what the hypothesis was and we'll go from there. Yeah. Well, that's also like another board of public goods they want to do. Like we're obviously bullish on the ecosystem, but we also want to remain objective. Yeah. Right. So we

**[40:12] SPEAKER_00:** decided to pick this like topic of profitability of perp traders on hyperliquid. And what we released today is basically part one, which is kind of like a tease for a larger research paper. And essentially it's an analysis of trader profitability

**[40:44] SPEAKER_00:** and how many users on hyperliquid. Actually make money trading. Right. And. I was impressed with the numbers, by the way. So I feel like I'm one of the bad traders here. But 29 % of users are profitable. That's pretty good. That's one out of three. Right. Like if we're, you know, putting up the rounding it up to the top. Yeah. I mean, that's actually not too bad. Right. And even

**[41:14] SPEAKER_00:** like it's, you know, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's, it's I guess a close like larger people with more volume radials are like 24, 27 % ish. And it's actually not too bad because some papers on bait trading say that like 95 % users lose. Right. And all of these CFD brokers post statistics that like that's just PUMFUN. Like we have the numbers for PUMFUN. I think it's, it's even less than 95 % The only

**[41:44] SPEAKER_00:** ones making money or the industry, insiders and here you get one out of three so that's pretty cool so yeah that's obviously not not too bad right and yeah then we just well did this research and then we also checked what like the builder app uh users are doing right and are they more or less profitable and i guess they're like a couple of very uh fun tidbits right so there are um most

**[42:18] SPEAKER_00:** of like the big wallets right like metamask and phantom they are their users are significantly less profitable than native content and to be fair like it makes sense right because obviously like you had to go through some like onboarding friction if you use a hyperliquid native content right and if you

**[42:45] SPEAKER_00:** just saw like a burp stab and metamask there's basically no friction right it's kind of well imposed on you so uh i mean it checks out the users would be like less sophisticated right i mean that's funny right when you think about it they develop a product for for it to have less friction but ultimately who's paying for that it's the users

**[43:15] SPEAKER_00:** so yes yes and this effect also like if you remove builder fees from the equation completely right users are like still less profitable so like if you if you remove the rate that the apps take like their users are just generally like trade wars but then again it also it also makes sense right because i think uh the native front that at least gives you like desktop app basically

**[43:46] SPEAKER_00:** right most of the time whereas metamask you can trade from your phone and i think it's just harder i for example i never trade from my phone anymore like i banned myself from doing that and i only use it for like for monitoring and then you can also see there there are like some smaller terminals uh they're apparently from like um kind of eastern european region right and they have like 200 users but they

**[44:16] SPEAKER_00:** have 80 percent user profitability wow the reason the reason being right they just self -select for like scalpers these are like scalping terminals they self -select for well very advanced users right and that's why they have like the this amount of people can we copy trade those users like you guys must have like a lot of people have all the data you guys must know at this point who's you know i mean theoretically you can like

**[44:46] SPEAKER_00:** the data is available on the flow scan or explorer so you could go click find their users see their addresses and then uh then you could copy trade but i i'm not sure like usually copy trading scalpers is not the best idea because basically they're very like uh a lot of their edge comes from well entries and axes and like weird like limit order thing is on wix so but you could at least like uh watch what they're doing yeah that's really interesting

**[45:17] SPEAKER_00:** because i think there's been this huge push um for ai to learn how to trade perps and so far they're all bad um we had last week somebody from robo net they actually kind of are working on this um working on this tirelessly and they have developed uh a strategy using their own uh uh uh uh uh uh uh uh uh uh uh uh uh uh uh uh uh uh uh uh uh uh uh and and it is profitable so far so it's doing decent but still i feel

**[45:47] SPEAKER_00:** like there isn't um kind of like this golden goose of saying to the i make me money trading perps on hyperliquid that doesn't exist and but perhaps leveraging your infra the data that you guys have and some of the you know findings from this research paper that could give like the ai something to learn and maybe eventually it'll get better at it i don't know what are your thoughts on this like do you guys

**[46:17] SPEAKER_00:** run some of these data sets through ai or just like mock copy trading and see if it actually could make you money or not well we we use i would say like we use ai for a bunch of stuff right i mean like uh uh hopefully best practice is not just like uh i would slop i would put right but and and i'm actually quite excited about some teams or

**[46:47] SPEAKER_00:** building something on the intersection of well hyperliquid trading and ai one of them is senpai ai s -e -n -p -i um well a great team they're experimenting with agents on um hyperliquid and i'm very uh yeah very keen to see what uh their experience will lead to because obviously like even

**[47:19] SPEAKER_00:** if nothing works out and like agents don't work this will have uh a good idea why they don't work and interestingly enough i think this is only like possible in hyperliquid because uh senpai they run uh uh agent trading arena basically they have like a bunch of uh they are trading agents and they uh um um have like

**[47:48] SPEAKER_00:** a competition have like a competition have like a competition right so like which strategy performs best but it really only works in hyper liquid I guess yes theoretically you could just well uh have an read -only API Wii for hyperliquid and I would put it on the dashboard but due to hyper liquid transparency it really only works in hyper liquid and you could really only run these like experiments and hyperlipid yeah that's and i remember there was one of these um um

**[48:21] SPEAKER_00:** trading competitions back then and i think grok had done well so elon kind of amplified the post uh so yeah looking forward to seeing more of these and perhaps somebody actually finally figuring it out yeah and then like again like these things and these like experiments are are really only possible quite really good i think uh i would also shout out like legends trade uh well i think this team that's doing something super interesting is like social trading where

**[48:51] SPEAKER_00:** like one of the examples of smarter copy trading essentially where uh you could basically like post your thesis and then like every user of legend they just like post their own thesis and you can see like all the traits on a chart and then it's kind of like introduces this social elements to trading obviously like shout out hyper dash as well because you can see like all this like granular data about market positioning well and

**[49:21] SPEAKER_00:** i think with hip4 it also like expands the creativity area quite a lot as well nice yeah i'm excited about ai in general i guess but we'll see what they come up with on the purpose trading side and perhaps soon we'll see what they come up with on the purpose trading side and perhaps soon We'll see HIP4 AI bots doing, you know, cause I always see them on Polymarket doing whatever they're doing. And now we'll see them on HIP4 as well. Yeah.

**[49:54] SPEAKER_00:** Well, I think there's like definitely a lot of exciting things that can happen there. You could also see like currently you can see if a person like is a good trader or not, right. But then you'll be able to see like if the person is a good trader on Perps, and the prediction market, or just one of the categories, or they're just like a good trader in general. Well, I think it's very exciting. I think it also will

**[50:23] SPEAKER_00:** introduce quite a lot of cool apps, just aggregating like trading and market information. And I think also like going back to the, to one of your like first points that you've made, like there are a lot of builders coming. I think, yeah, a lot of builders are like capitulating into hyperliquid now, because basically there is - Capitulating to hyperliquid. Yeah, capitulating to hyperliquid.

**[50:53] SPEAKER_00:** There's basically like, there's, I think that hyperliquid and well, stable coins are the most interesting things happening in crypto at the moment, right. So a lot of builders are just like, okay, if I'm not building here, what am I doing? I agree with you, man. I agree, that's the best place to build. A lot of the ecosystems are dying and this one is just flourishing. On that note, so what are your plans for

**[51:23] SPEAKER_00:** the future? What are you looking forward to, I guess, in a year or five years from Hydromance? Or like, I feel like already in a good spot, but what spot you guys want to be in, in a year's time? Oh, five years is hard. I mean like five days is hard enough, but before like, Let's go for a year. Come on, we can dream here. Yeah, but everything is weird. Everything's weird dynamic, right? But it's well, yes, a good time

**[51:53] SPEAKER_00:** to like a shout out to Redgang and to the validator collaboration, right? Because we managed to get them to the active set. It was painful, but now we're like, we're like in a last place hanging by a thread. That's okay. Nah, it's okay. now it's okay it's good it's fine it's fine yeah yeah i mean like uh we're an active set right so that's good and uh we didn't think we would get there uh

**[52:24] SPEAKER_00:** that quickly but well we are there now so that's great and yeah i think the plan is the same just support everything that well uh uh hyperliquid is doing quickly and supporting it well like we do with like hip um like we do with hip four um endpoints essentially because we're basically ready to support hip four and even

**[52:54] SPEAKER_00:** like hyperliquid doesn't support like the endpoints for hip four so that's great and yeah just expand support all the teams i think one of our edges is really that we generally love what we're doing we're having fun it's actually great and uh invigorating to actually work with so many like sharp builders and builders who want to win essentially and delivering the best

**[53:24] SPEAKER_00:** technical and infer support so they can do fun stuff as well and obviously yes like expand on uh public goods stuff for the ecosystem we really i like really like how our you explore is coming along obviously like um we're kind of developing around explorer and the reason is that we just need it for our own

**[53:54] SPEAKER_00:** like everyday usage and we can find like much of this stuff like anywhere so we're building our own and currently it uh looks pretty good but for those who don't know it's a flow scan dots xyz and um yeah just continuing the grind and having fun in the meantime nice love it i'm excited for everything that's going to come out you

**[54:25] SPEAKER_00:** guys um really pleasure collabing with y 'all if anybody i guess you know if anybody wants to reach out to y 'all i guess best way would be uh give this account a follow perhaps go to your website anything else on how they can reach out you know maybe they're building on hyperliquid or something like that so yeah i'm excited for that anything else on how they can reach out you know maybe they're building on hyperliquid or something like that so yeah i'm excited for that and they want to have access to the data as fast as they want to have access to it or or write the data as fast as they want to write it yeah um i

**[54:55] SPEAKER_00:** mean it's all in the docs it's all in the docs and you can but you can also dm on twitter you can message me on telegram you can write us an email you can set up a group on slack or i don't know like uh write us a physical mail even just yeah like we we also like if um just yeah like we we also like if um we also onboarding with early stage teams we also onboarding with early stage teams we also onboarding with early stage teams and we have this early stage and we have this early stage and we have this early stage builder program where each month we builder

**[55:25] SPEAKER_00:** program where each month we builder program where each month we give three teams give three teams give three teams uh access to our uh access to our uh access to our infer until they start infer until they start infer until they start like making money and they're getting like making money and they're getting like making money and they're getting and then they can pay right and then they can pay right and then they can pay right yeah yeah yeah yeah yeah yeah you're right you're right and funnily enough you're right you're right and funnily enough possible hyperlinks because like we have visibility into their revenues right because builder goes because on chain right so they give us a wallet and we're like okay we can actually see like like

**[55:56] SPEAKER_00:** where uh when you start making money right and then from there we can start charging and then again it's also like if they win we win right so obviously we uh want to support builders doing fun stuff nice cool yeah maybe a hackathon or something like that that could be fun like um all these ai vibe coders leveraging some of your data perhaps they come up with something cool anyways oh yes i think sponsoring hackathons is also like one of our uh one of our

**[56:26] SPEAKER_00:** ambitions and actually funnily enough uh well shout out to eric who is our newest hire and we actually it was very funny because like everyone knows the hyper pro hyper pro group right like the ecosystem yeah yeah for sure run back group yeah so it was funny because um someone came there and they posted a like a introduction

**[56:56] SPEAKER_00:** message essentially saying hey this is my name uh yeah this was my hackathon project looking to connect with uh other builders right and actually seeing this hackathon project and it's actually wasn't like it was kind of similar to what we're doing so like within i think like 20 seconds of uh him posting i uh said hi in dms we're interested in talking and yeah that's how we expanded are you sure he's not north korean did

**[57:26] SPEAKER_00:** you ask him if he you know the the insult kim jong well yeah yes actually we did but we met in person so unless he wears like you know like a skin mask and his skin walker or something that's funny but yes like uh all right very cool that's great yeah team's expanding um on that note we're at the top of the hour really really appreciate your time man and again appreciate the collab uh hope we can continue the

**[57:56] SPEAKER_00:** club yes we are going to continue the collab definitely yeah i mean i mean i think i think i think i think it's overall it's uh it's a great it's a great collab and i actually started to love the negative culture meets infrastructure more and more i think yeah every time i see this line i'm like i don't know if it's too much right like whatever you see if we're still in the active set that's kind of the first thing that pops up is like culture meets the fish i'm like okay fine no i think it's cool i think i

**[58:26] SPEAKER_00:** think it's really cool but it also it also it's culture right because i think like nobody can really say that they were like earlier to hyper liquid than like frack gang did you see the article on jeff did you see the the one that there was like a really nice article uh on jeff recently and they they mentioned us they say and we changed our um we even changed our bio they said in the early days of hyperliquid it was nft users

**[58:56] SPEAKER_00:** that were trading five dollar perps there were no serious users and i kept that i kept that in the bio no serious users and i kept that in the bio no serious users and i kept that in the bio no serious users well i mean like humble beginnings right i think that's like the beauty of uh like life just in general is that uh like you don't really uh like have full visibility into what's going to happen that's

**[59:26] SPEAKER_00:** why you asked what's going to happen in five years right and so we don't know well the goal is just to keep helping builders in our case keep having fun and hope that yeah these humble beginnings will have some glorious ends i'm sure they will man i'm sure they will uh thanks again for your time man really appreciate the space is recorded for those that tuned in a little later and i know a lot of people tune in uh at time zone that works best for them so we'll keep a recording online alive um

**[59:57] SPEAKER_00:** so thanks for tuning in once more enjoy the rest of your weekend or week wherever you are um and uh yeah thanks man for this collab really appreciate it thanks a lot yeah well let's do another time again i agree man in a year's time in a year's time or something like that but then you'll be like oh remember when i said this uh now it's that cool all right see you all

**[1:00:27] SPEAKER_00:** right see ya
