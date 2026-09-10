# Harmonix: 10% USD yield and delta-neutral vaults on Hyperliquid

_How Harmonix generates sustainable yield through delta-neutral strategies and TradeXYC funding rates._

**Host:** @rekt_gang
**Date:** 2026-07-02
**Duration:** 33:07
**Tags:** vaults, trading, perps
**Source:** https://x.com/i/spaces/1wxWjjkajMDJQ

## Who's talking

- **Rekt Gang** (@rekt_gang) _host_
- **Christophorus** (@christophorusan) _guest_

## Key moments

- **[6:41]** Zerk introduces Christopherus from Harmonix
- **[7:42]** Chris shares background: DeFi trader, now building basis trades
- **[8:42]** USDC vault launch with 30% APY on commodities
- **[13:15]** Deep dive: how delta-neutral strategy generates 10% APY
- **[18:49]** HYPE and kHYPE vault yields: 3.4% to 5% annually
- **[22:51]** TVL breakdown: 6M total across three vaults
- **[23:21]** Bullish on Hyperliquid EVM, integrating AI agents into strategies
- **[26:54]** HAAR token governance plans and convertible bond experiments

## Transcript

**[1:22] SPEAKER_00:** gm gm can you hear me yeah i can hear you pretty good very cool let me just amplify the space cool more people in and then we'll get started are you

**[2:05] SPEAKER_00:** a big world cup fan a little bit yeah i've been going to a couple of matches um yesterday you went to a match um i mean i'm in seattle right now so it's mainly kind of around the stadium and there's a lot of people a lot of movement it's kind of cool oh that's really cool that's super fun must be a really good uh you know vibe yeah uh it's really cool to see

**[2:35] SPEAKER_00:** everybody from different countries come um yeah have you been going to a couple of matches no i'm i'm in montreal canada we are actually not even hosting any here um and they say it's a good thing because i think it's kind of expensive for the city i don't know in our state we don't have football stadiums right like so it's kind of complicated to fit all those people in okay okay yeah

**[3:05] SPEAKER_00:** is uh is canada still in the knockout phase of course man we're still in it i'm probably gonna lose i think we're playing morocco next so not not sure about that yeah i've been following they have a pretty good team um exciting yeah for sure it's been fun it's been really enjoyable

**[3:35] SPEAKER_00:** i'm more of a hockey person and this year in particular i feel um i don't know if it's me but i feel like they they're not calling the diving right or they're making like less calls which maybe some get you know some aren't happy with it but for me i like when it's more physical and there's less crying there's less you know whining so yeah that

**[4:06] SPEAKER_00:** was great um we have climate pledge here and the hockey team isn't great but it is really fun to go watch that's cool man um all right let me just do a few more places let me just do this did i mess something up no i think i'm good you know these spaces are always recorded and archived as well as now i

**[4:36] SPEAKER_00:** don't know if i'm front running an announcement but might as well tell you um i don't know if you're familiar with the hl .eco dashboard uh yeah yeah so they will have like an educational channel and they're going to put up those spaces there as well so i think it's a great reference for anybody that wants to learn about hyperliquid in the future yeah it's pretty good i'll definitely check it out soon

**[5:07] SPEAKER_00:** tm all right let's get started in just a minute if you just join the space give the space a like give a little retweet always helps with the algorithm perhaps drop a comment um and we will get started very shortly it's cool yeah

**[5:39] SPEAKER_00:** I've seen a lot of the podcasts um the spaces and they're pretty cool uh love to see all the projects in hyperliquid and everybody that's building in this yeah we we host everybody man we we've had Jeff and yesterday um oh no yesterday was in Cosmos spaces but the day before that we had sempi the AI folk had uh outcome we have tread five tomorrow it's just been very busy um

**[6:11] SPEAKER_00:** how was it for you to meet everyone there and um talk with uh everybody building like um yeah that's what I enjoy that's what I enjoy I enjoy learning about what people are building and it's not only a great educational opportunity but also I guess you know people say do your own research this is kind of the best way of doing it yeah definitely yeah all right let's kick the space

**[6:41] SPEAKER_00:** off so uh I'm zerk co -founder of wrecking we like to host spaces as we just discussed talking about Builders on the hyperliquid blockchain and today we have the privilege the honor the prestige of hosting Christopherus I'm hoping that I pronounce this correctly from harmonics um how you doing Chris I'm doing great really happy to be here thanks uh for having me oh the pleasure is all mine

**[7:11] SPEAKER_00:** I've seen harmonics the hyper liquid timeline for a while now you guys have been cooking on the blockchain for some time now so really happy that you guys joined on this space where we'll get to learn more about what you guys have have been building and are going to be building in the near future as well yeah um it's great to be here um my background is a bit in i come from mainly doing publicity and marketing campaigns and web 2. um mostly

**[7:42] SPEAKER_00:** based in europe but i was always a d5 user and i just found out about hyperliquid in 2023 late and started trading buying and selling and doing delta neutral strategies so that's kind of what brought me to harmonix team and what we're building uh basis trades on hyperliquid yeah the delta neutral thing was quite popular at a certain point do you remember liminal they're still around obviously but

**[8:12] SPEAKER_00:** i feel like uh folk thought they found you know the the golden trinket there uh the holy grail yet you know it's it's tricky to do delta neutral trading so i'm happy that you guys got involved with this yeah it's actually great because the liquidity is really deep the execution is good the team is always looking for new tokens and especially with trade xyc the new you know real world assets on in february

**[8:42] SPEAKER_00:** the yields on copper gold silver it was really good to see almost 30 apy on that um that's kind of what brought us to build the usdc vault right um that we just launched recently nice very cool all right before we get into all that good stuff let's do some introductions so uh maybe you can let us know a little bit about your crypto journey and what you're doing in this role and why you decided to join the harmonix team you told us you know kind of got involved in hyperliquid in

**[9:12] SPEAKER_00:** 2023 but a little bit more about yourself is always good yeah so uh 20 years old i founded a marketing company uh just working with public and private institutions in europe i did digital ads and full life cycle marketing campaigns for paid ads and yeah i got into crypto like i said trading buying and selling tokens I really connected with Jeff and the guys with the

**[9:42] SPEAKER_00:** vision that they had of building an exchange, connecting people peer -to -peer in a decentralized way, and providing liquidity in a sustainable way. That's really what brought me to Hyperliquid, and just seeing what they're building, that community focus of bringing people together and making them part of everything, it just seemed something unique at the time. I feel a lot of builders resonate with the ethos of Hyperliquid, bringing

**[10:13] SPEAKER_00:** us back to the OG roots of crypto, pushing for freedom, decentralization, and not being scammers, basically. Yeah, and I love that, for example, the HLP vault, that you can actually see everything that's going on behind the scenes. I mean, that was something new. And especially after being... Being in the space for a while, and, you know, you always have to research what's the strategy, what's behind, what's the token,

**[10:43] SPEAKER_00:** what's it backed, how's it backed. And, yeah, Hyperliquid was something that you could see all that in a transparent way. That's kind of what brought us to building also on the EVM. Love it. So, huge fan of Hyperliquid, I understand. Then you decided to join the Harmonix team, and what got you kind of... What pushed you to join that team and continue building with them? Yeah, so I met Frank Bean.

**[11:13] SPEAKER_00:** They had been doing stuff for hedge funds in Singapore, and I loved their background and everything that they were doing. The first vault that we released with Harmonix was a delta -neutral strategy on hype, so pretty simple, right after the TGE. And I could see... We talked a lot of what was going on, what were people looking for, and, I mean, the next thing that we released was the delta -neutral

**[11:44] SPEAKER_00:** vault with hype and K -hype right after the EVM launch. It was great because we could integrate into lending, staking, borrowing with Felix. Yeah, it was great. Great to see the EVM launch and everything that was happening with the ecosystem and how it was growing. So, you're talking a lot about vaults, right? And I feel like it's a product that is one of the easiest to sell

**[12:14] SPEAKER_00:** to retail. So, your vaults today, I feel, if we're talking about USD yield, that's probably one of the highest yields in DeFi, is it not? And I know it's not like I'm advertising 100 % here. It's 10%, but it's a reliable 10%. So... So, anybody in retail, you tell them, I can give you 10 % on your US dollar, you're going to take it, right? Like, people are happy with 4%, 5%.

**[12:45] SPEAKER_00:** Maybe in crypto, they're happy with like 6 % to 8%. But 10 % is, to me, pretty industry -leading. So, maybe can you talk to us a little bit about this USD vault that you guys have cooking? Yeah, I mean, especially after spending a lot of time in Europe when we have funds in your bank account. And the bank is giving you like 2%. Yields off of it, 3%. I mean, it was kind of frustrating not to have something reliable that was long -term and scalable. And that's what brought us to build

**[13:15] SPEAKER_00:** the USDC vault. It's pretty reliable in the sense that it's built on hyperliquid. Liquidity is deep to enter and exit positions, to deposit and withdraw. It's very clear and simple. We integrated Octav, too. So, you can see exactly where the funds are as time goes by. And since it's a delta -neutral strategy now that's built dynamically, which means that as the market moves, for example, in February, there was gold, silver,

**[13:45] SPEAKER_00:** copper. And now it's, you know, we're always updating it to the highest returns for the depositors. That's what makes it so we can deliver almost 10%, even higher sometimes, APY. And that's without any token incentive. I know if you deposit into the vault, too, you can get points from Hyena, which is the Athena group that are building on hyperliquid. So, on top of the yield, you also get ecosystem points, which is kind of cool. Yeah,

**[14:17] SPEAKER_00:** let's dive in a little deeper here. This yield is sustainable is, I think, the critical part. There is no token incentive. You mentioned some Hyena points. Maybe they'll be worth something, maybe not. But the 10%, you're getting that day in, day out. And mainly because... I guess, you know, the funding rates are kind of crazy on some of these equities slash commodities, all the stuff that trades on TradeXYZ. So walk me through

**[14:47] SPEAKER_00:** a little more in terms of what the strategy is behind the hood. What's actually happening here? Yeah, so, I mean, especially after, you know, I feel like hyperliquid kind of came, rose up after FTX and everything that happened there. So, again, our idea is not only providing a high yield, but also a way for users to verify their funds. So if you go to the web page and you can see, tap

**[15:17] SPEAKER_00:** into the vault, you can open up and see Dbank and Octav have provided a way for us to show what's happening. So, for example, there is a spot side with Felix that we do tokens. And then we have perps for TradeXYZ. And you can see it's around 77 % of the deposit of the vault. There's around 18 % in Pendle. And then we have HyperLend and Morpho, which is usually the Felix team as

**[15:47] SPEAKER_00:** well. They have like a Frontier Vault. That's pretty good. I mean, we also adapted a lot, but mainly that little buffer in lending is for users to, you know, because of the ADL and automatic deleveraging, we always have to have the system to track it and have... You know, in case of a huge market movement to adjust the strategy. So that's kind of how it is. Our idea is to keep most of it in the perps and spot. But there's a little buffer that we keep in Pendle and lending and staking.

**[16:18] SPEAKER_00:** We do have like a three day withdrawal period, but that's mainly because since we keep some part in staking, it requires time to unwind the positions. And we do do it in a smooth way. So just to monitor for slippage and everything like that. It's kind of our grace period. That's mainly the overview of the strategy. Very cool. And you've ran this vault for how long now?

**[16:48] SPEAKER_00:** We can say the yield has been consistently around 10 % for... I think you guys have been around for a year. Is it a year? This one actually, I mean, TradeXYC has been live for a couple of months. Right, right. So, yeah. And SpotFusion. Felix, it took a bit for the spot to come in. So it's been around since May and yeah, kind of like something two months. But we started building it right

**[17:18] SPEAKER_00:** when TradeXYC launched and the funding was a bit higher then with copper and silver that were going a bit crazy, oil at the time. So, yeah, I feel like as long as there's traders on Hyperliquid and TradeXYC, we will continue to have a hyperliquid. So it's going to be a high yield. Yeah. And I'm sure there's going to be a boom of something else, right? We have the crazy AI stuff and now we're going to have some crazy robotics.

**[17:48] SPEAKER_00:** I don't know what it's going to be. Maybe it's going to be crypto. And people are going to go max long. So you'll be able to benefit from that as well within the vault. Yeah. There's also, I mean, there's SpaceX that is exciting. There's a lot of new stuff happening that we're always tracking. Everything that's going on. It's pretty cool. I noticed you had the Denari team too. We're also following that. So just all the time looking for spot and perps launching. Yeah.

**[18:21] SPEAKER_00:** Nice. So this is a yield on USD. I feel is one of the best yields. But if you are not bullish on the US dollar, you're bullish on hype. You don't want to be holding any of that inflation. It's going to be an inflationary US dollar. Although I'm not sure it's going to be inflationary anymore with the new Fed chair. We'll see. You also have vaults for hype and they offer more yield than just native staking.

**[18:49] SPEAKER_00:** Correct? Exactly. Yeah. So we have two vaults, the hype vault and the K hype vault. Both vaults have been between 3 .4 % to sometimes 5%. So we're really happy about that. The yield is really... Those have been live for a year now. So we can surely say that the yield is pretty good. Especially when you compare it to Kinetic, the K hype vault

**[19:20] SPEAKER_00:** is a lot higher. It's almost like twice as high. And then the hype, when you compare it to staking or even yields on Pendle is like three times more or something like that. It's pretty good. Yeah. So basically if you're in the K hype vault, you're already earning that 2 point whatever percent plus you're getting an extra four on your K hype. So it's kind of like almost... I don't know. It's the best, probably one

**[19:50] SPEAKER_00:** of the better yields you can get if you're bullish on hype. Yeah, exactly. And I mean, we built especially on hype because in the last year, especially when you compare it to Bitcoin or Ethereum. It's been up like 70%. It's something we believe in also, like with kind of like the market we're in, especially right now. Hype is something that we believe that's going to keep rising and especially with the multi coin outlook that

**[20:20] SPEAKER_00:** they're saying by 2028 can reach 300, even go higher than that. We feel like allocating a portion of that to yield. It's not only beneficial with the upside of hype, also something on top of it. It's pretty good. I've been mostly losing hype because I've been perps trading. I should just put it in the yield vault and set it and forget it. Right. And it's been running for a year. This one has been

**[20:50] SPEAKER_00:** running for a year. So maybe talk me through real quick about the strategies to generate that yield as well as some of the risks. Because on the USD vault. I kind of understand, you know, you're getting yield on USD. There's obviously some sort of risk, but hype, I can do the staking, right? So what are some of the risks and what is the strategy and what are the risks associated with the hype vault? Yeah, exactly. So, I mean, the strategies is a lot of,

**[21:20] SPEAKER_00:** we are integrated with Felix protocol and we usually borrow against the hype and then do another delta neutral strategy and then borrow against that. And do another. So it's kind of like a loop delta neutral, right? So obviously we have like every protocol that you're integrated with, it is a risk. So that's why we choose, you know, Hyperland, Felix, Tradex, YC products and teams we believe in that they're working

**[21:51] SPEAKER_00:** something on something that's safe and well done. There is that side. And then obviously smart contract risk. There's the risk of. Yields lowering over time, although I feel like especially with hype, that's been pretty consistent over time and yeah, smart contract risks and mainly the market movement, right? Everything like unwinding positions, our

**[22:21] SPEAKER_00:** biggest focus is the ADL, you know, that's something that we have something internally that we kind of keep as a secret of how we manage that. But it is something. Users, you know, if you're doing a delta neutral strategy and this market suddenly starts to move a lot, you have to be aware of the ADL automatic deleveraging. So you don't, you know, stop being delta neutral. Yeah. And I'm glad you mentioned this because a mechanism is important for the safety of users

**[22:51] SPEAKER_00:** funds, I guess. On that note, you know, you guys have, I think it's 6 million in TVL, something like that. Yeah. Yeah. So right now the K hype vault has 3 million over a little over that hype vault has 2 million and a USDC vault just launched. So we have like 300 K something like that. Very cool. So, you know, there was lots of discussion about hyper EVM and folk. I

**[23:21] SPEAKER_00:** don't want to say abandoning it, but using it less or being less excited about it. You guys are still building and excited about it. And I feel like there's lots of room to grow to increase the TVL on top. Yeah. We're really excited about also, I mean, AI and how this has developed. We are like actively integrating agents into our strategies and experimenting a lot with that. I feel like there are a lot of teams like the paper team on a hyper EVM

**[23:52] SPEAKER_00:** and more teams that are coming in that I feel like it's just since the start, it's been a space where there's a lot of innovation that's happening and that's always attracted me a lot. There's always like, yeah, there are teams like Ventrules that, you know, kind of sunset. But I feel like there's always people building, creating new things, you know, and experimenting in that. That's something we're doing as well. I feel like it is still a bit early for the AI to actually do something, you know, reliable in

**[24:22] SPEAKER_00:** the sense that, you know, we always have to have our systems be kind of monitored by humans. But as it progresses. It is helping us with like skills and information. For example, we have a quarry for every time there's a good API on Hyperliquid, we connect directly to they using Loris tools and protocols like that. And it's great. It's great to see how that is developing on the hyper EVM chain. So

**[24:52] SPEAKER_00:** you're bullish on hyper EVM. That's what you're saying. Yeah. I mean, right now, especially with everything that's happening. Yeah. In the space, I feel like this is where innovation is going to happen and continue to happen as time goes by. Very cool. I'm also bullish. That's great. So you mentioned AI, I know about the balls, but what else are you guys working on in terms of, I don't know, like, upcoming cool stuff that we should be aware of? Yeah, I mean, we're actually we want, we're

**[25:23] SPEAKER_00:** kind of keeping that side private, but we're always interested in the community of, you know, people to tell us what they actually want and not just build for ourselves. So we really want to reach out to the community and hear them. What yields do they want? What tokens do they want to hold and what products they would like to see on hyper EVM? You know, I feel like there's a big side of that, that you should come naturally. Just talking with people and builders in the space and figuring out what comes next. Yeah,

**[25:53] SPEAKER_00:** I'm always a fan of these delta neutral vaults because I feel the yield is kind of, you know, true. It's real money that's being generated. It's not like you're printing it out from a token incentive or out of thin air. So I like that concept. To me, it makes a lot of sense. Yeah, I mean, and again, building on hyper legal is great because it has deep liquidity and just a way to exit and enter positions. And especially during

**[26:23] SPEAKER_00:** huge market movements, you know, I felt like it's a place that has never had real downtime. Yeah. During those moments. So it just feels a lot safer and, you know, better performant. Agree. Agree. Never. No downtime. Can we talk about the Haar token? I think that was airdropped. I still have some in these wallets. And what's the plan with that? And I guess what's the utility as well for the folks that don't know what that is? Yeah.

**[26:54] SPEAKER_00:** So right now, mainly it's a governance token. We did a point season. That when the token went live in December last year, it was pretty good. We did a big part to the community. They're still reserved a big amount for the community. We're still set to announce that part. But right now it went live and you can stake it and earn staking rewards off of that too. And we do believe, you know, we were experimenting with it

**[27:23] SPEAKER_00:** kind of a way like Olympus DAO did. And same with Saylor of backing Harmonix with Hype. So as people enter the token, they can also swap it to Hype. It's called a convertible bond, right? But we're kind of keeping that internally still and figuring out a right way for users to get exposure to that. So right now, as it is, it's just a governance token. But in the future, we are

**[27:54] SPEAKER_00:** finding a way to... Make it backed by Hype and that way providing an upside to the community as well. Nice. So I guess that brings me to the question of what's next for Harmonix. You're talking about integrations, but what are you most looking forward to in the next three to six months? Yeah, we're talking with teams also like Superform that are actually building on Hyperliquid and we're really excited to see everything that's going on there. We

**[28:24] SPEAKER_00:** did a couple integrations. We're working with lending protocols and for people to be able to borrow against their positions in Harmonix. I feel like that's pretty cool because it's kind of a way to be liquid in those positions and still earn if you want to keep trading, you know. And mainly, as I said, we're working with AI and creating a way for users to tap into the yield and the ecosystem, everything that's being built. We're following really closely teams like Paper.

**[28:55] SPEAKER_00:** They're launching a lot of stuff. They're launching their products soon. So everything that's going on in the ecosystem, we're tapping into and providing the secure way for people to earn and keep their hype holdings. Yeah, max yield on hype. That's the name of the space. Makes sense to me. All right. So basically, I'm going to do a quick recap so people that just tuned in know what we're talking about. So Harmonix.

**[29:25] SPEAKER_00:** It's a protocol on Hyperliquid where you can earn yield on your USD about 10 % or earn extra yield on your hyper K hype about four to 5%, which is great to me. They have a token right now it's governance, but perhaps they're going to be doing something cool with it very soon. And definitely give Chris here a follow as well as the official Harmonix account. How else can people get involved? You know, with Harmonix? Or how? How

**[29:55] SPEAKER_00:** else would you like them to be involved with, you know, whatever you guys are building? Yeah, we would love to hear from the community what what things they would like to be built on hyper EVM, especially if they want like yields, or there's a couple of teams experimenting also with treasuries, which is exciting, you know, like bar against it and continue to get yields which are reliable off of that. So anything that the community has is what they want to see built and what they would like to, how

**[30:26] SPEAKER_00:** they would like to earn the yield, that would be great. It would be great to hear them and be in contact with them and happy to happy to reach out and send me a DM and we can talk. Yeah, Chris is very available. So do DM him do reach out if there's anything else you'd like seeing built. Any closing thoughts, anything that we haven't discussed that you wanted to discuss, I'm kind of looking over the questions. I think

**[30:56] SPEAKER_00:** we went over it, but up to you. I think we're pretty good. Yeah, just happy to keep earning the ecosystem points and figure out more teams and working with them in the ecosystem. But yeah, thanks so much for having me. It was great. It's my pleasure. And as mentioned in the beginning, the space will be recorded. Well, it's already being recorded timestamp and then I'll archive it will also be on the HLE site. So that'll be cool. So

**[31:27] SPEAKER_00:** if people want to learn more, they can always re -listen to the space afterwards. Any bullish takes on, you know, you mentioned 300 for Hype, what are your bullish takes for Hyperliquid? I mean, I do expect it to get reached 100 soon. That's kind of like my next mark. But other than that, I feel like one step at a time, let's get to 100 first and keep going. That's good. That's good. That's good. Careful. He's being careful. Not financial

**[31:58] SPEAKER_00:** advice is always right. Exactly. But meanwhile, meanwhile, it reaches $100. You can earn yield on it to maximize, I guess, your hype, which is great. So do check out Harmonix .fi. You can, yeah, earn yield on it. It's been around for a year plus in terms of the vaults and the USD vault is quite fresh. But like I said, the vault has consistency. It doesn't yield. It's using a lot of delta neutral trading. So it's not like

**[32:28] SPEAKER_00:** just token incentives printing something that's not going to be worth. So very cool. Any last words, Chris? That's it. Thank you guys for tuning in and hope to hear a lot more from you guys. See you guys soon. Yeah, we'll do. Thanks for the spaces. Keep on building on Hyperliquid and we'll reconnect. Cool. Bye bye. All right. Hyperliquid. I believe. Yeah. Thanks, everybody.
