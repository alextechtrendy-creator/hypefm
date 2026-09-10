# Delta neutral yield on hype and stablecoins: Monetrix's transparent on-chain strategy

_Monetrix builds yield-bearing stablecoins and hype tokens using funding rate arbitrage and portfolio margin on Hyperliquid._

**Host:** @rekt_gang
**Date:** 2026-09-02
**Duration:** 1:00:28
**Tags:** perps, vaults, ecosystem
**Source:** https://x.com/i/spaces/1oJMvNLMDYRxQ

## Who's talking

- **Rekt Gang** (@rekt_gang) _host_
- **Syc.hype** (@Sychype) _guest_
- **Monetrix** (@monetrix_xyz) _guest_

## Key moments

- **[9:00]** Monetrix introduces USDM and MX hype yield products
- **[10:31]** On-chain transparency solves off-chain yield protocol risks like Ultra and Neutral
- **[12:31]** Delta neutral hedge mechanism: long spot hype, short perp with portfolio margin
- **[25:15]** MX hype launches with 18% APY first week, caps increased from 5k to 50k hype
- **[27:47]** MX hype clarified: hype deposited is collateral for strategy, not delta hedged itself
- **[34:21]** Points campaign and SBT for genesis depositors, future governance token planned
- **[49:34]** RWA strategy roadmap: delta neutral yield on stocks once spot assets and portfolio margin enabled
- **[52:36]** Stocks as collateral plus yield could be the execution unlock for Hyperliquid's next phase

## Transcript

**[3:20] SPEAKER_00:** GM, GM, how are you doing? Hello, hello. How are you? I'm great. I can hear you loud and clear. Perfect. The mic is working nicely. Are we waiting anybody else from your team? No, just be me. The Monotrix is my other device. Yeah,

**[3:52] SPEAKER_00:** we do that as well. Yeah, you kind of have to, huh? It's good for the algorithm. Speaking of algorithm, if you just join the space. Oh, that's a little loud. Bottom right corner, there's a little purple bubble. Give the space a like, give it a little retweet, drop a comment. Always helps with the algorithm. And we shall get started in just two short minutes. What an

**[4:27] SPEAKER_00:** interesting start of the day. Feels like volatility is going to be on the menu today. Oh, it's quite late where you're at, I think, correct? It's 11 p .m., which is honestly not a bad time. Yeah, well, thanks for making the time, actually, because it's

**[4:58] SPEAKER_00:** pretty late for me if it was 11. I mean, whenever you talk to, whenever I talk to people from America or EU or anywhere, basically anywhere in the world, I always have to either talk, call them at night, which is like around now or in the mornings. So it's one or the other. Kind of very used to different time zones. Yeah, crypto is very worldwide now.

**[5:29] SPEAKER_00:** So, you know, I think everybody has stayed awake a little longer than they wanted to for some sort of, I don't know, if it's a meme coin or whatever you prefer. All right, well, let's get this spaces started. I like to start these on time. Let me amplify one more time from my account. And, yeah, as always, I mentioned these paces are

**[5:59] SPEAKER_00:** recorded so you can listen to a time that at a time that works best for you. And I'm Zerk, co -founder of RecGang. We love to host educational spaces about hyperliquid. And today we have the pleasure, the privilege, the prestige. Of hosting Syk, I hope, or Syk, from Monetrix. Again, please give me the correct pronunciations for these two and maybe introduce

**[6:29] SPEAKER_00:** yourself real quick here. Yeah, I prefer to go by Syk, but either way works perfectly fine. Yeah, a bit about me. I've been in the crypto space for almost. Six years now, made my way really deep in, in the NFT bull run back in like 2021, did marketing, worked

**[6:59] SPEAKER_00:** on a marketing agency back then, and then worked at a VC, a Singaporean VC in 2023, 2024, not in 2025, kind of full deep dove into hyperliquid with hyperfinance and now Monetrix. Yeah. Nice. Very cool. And you are based in Singapore, correct? So I expect you to be at the annual convention, annual big hype meeting this year.

**[7:30] SPEAKER_00:** No, I'm a, I'm based in Japan actually, but I will be going to Singapore. I will be going to token. I got, I got accepted to the hyperliquid event the other day. I mean, you are a builder on hyperliquid. If they don't accept you, who are they accepting at that point? Yeah. Yeah. I. I don't know. I feel like I haven't been accepted into, into a few events. So yeah, they're, they're very picky, but anyways,

**[8:00] SPEAKER_00:** that's whatever topic enjoy that event. It's always a great event and a good to know. I didn't know many builders in Japan. I'm always talking about, you know, there's crypto in Korea, there's crypto in Singapore, but very few builders from Japan. So nice to meet you. Uh, I mean, technically, I mean, I'm Australian, I'm just living in Japan currently. Uh, but, uh, I guess I'm wondering why that is though. Why is there like so

**[8:30] SPEAKER_00:** few, you know, builders in Japan? I don't know. I think there are, I mean, there, yeah, I don't think there are that many, but I think the, like Japan has like its own crypto bubble. Um, I went to the hyperliquid Japan event. Uh. Uh, but I think a lot of people were just kind of traders. There weren't that many builders. Yeah. Yeah. Very interesting to me. I, I meet so few from Japan, but cool to know that they do have hyperliquid

**[9:00] SPEAKER_00:** events and a crypto community as well, but let's get down to business. Let's kick it off. So thanks for, for taking the time today and please introduce us. What is monotrix, you know, what are you guys trying to solve and we'll deep dive afterwards. So monotrix is a yield, um, yield platform, uh, we started off with USDC, which was, uh, USDC

**[9:30] SPEAKER_00:** deposits, which was USDM and staked USDM, so SUSDM, uh, and basically what we're trying to do is be kind of like a on -chain transparent version of Athena, so a yield bearing stable coin. Um, and yeah, USDM was our first. Product we recently just rolled out, uh, MX hype, which is pretty much the same, um, strategies, but using hype as the, um, like deposits. So that

**[10:00] SPEAKER_00:** way we can, uh, that way you can gain yield on your hype as well as USDC, um, just in a different format. Uh, I guess the problem that we've been trying to solve is most yield sources have been run through CXs and a lot of black. Black boxes we've seen in the, like in literally just like the recent month or so there's been two, um, yield protocols that had like OTC blow ups or, um, you

**[10:31] SPEAKER_00:** know, off chain, uh, just like mishaps, which was, uh, ultra and neutral and those types of stuff can't really happen if it's on, um, on chain. Uh, so yeah, I guess that's the biggest problem that we're trying to solve making, um, yield transparent. Very cool. And if we go back to Athena, am I correct in saying that that was in part responsible of the liquidation cascade on 10, 10, like, uh, you know, were

**[11:01] SPEAKER_00:** they not, or I guess it was some Oracle issue on Binance related to Athena's USD. Yeah, yeah, it was, uh, it was definitely a factor in on 10, 10. I mean, till this day, I think no one knows exactly what happens, which is absolutely crazy. When there's like. Like, you know, billions on billions in liquidations. Um, but yeah, I feel like, you know, thing, like if that happened on chain, you could, you could see it exactly as it happens. And it's not like, you know, Binance only reported one liquidation per

**[11:31] SPEAKER_00:** like millisecond, which, you know, kind of covered up their numbers by billions. Well played CZ, uh, on that note, you know, yield bearing USD. There was a lot of talk about stable coins. I'm not gonna read it out. Uh, but all of the ones on hyperliquids specifically, uh, you know, what USDH and now circle doing their buybacks with AQA V2. But this one is yield bearing all the other ones, uh, were not. So. Could

**[12:01] SPEAKER_00:** you maybe explain us how it works, how it gets that yield and, uh, you guys being fully transparent on chain? Which I think everybody on hyperliquid kind of agrees with that ethos. Uh, yeah. Talk to me a little bit about the mechanics. of yield accrual on the stablecoin? For sure. So everything is basically currently caught on Hyperliquid and it's purely by funding rates. So we have a delta neutral hedge

**[12:31] SPEAKER_00:** at all times. So say, for example, with USDC or hype, we buy spot hype for the long position and then with the same amount of money, thanks to portfolio margin, we can actually short the exact same amount on the delta neutral side. So basically, as long as hype goes up or Bitcoin goes up or there's just more people

**[13:02] SPEAKER_00:** that are long than short, then we'll keep getting paid on the funding rates, even though we're completely delta neutral. And then all of the money that we make through funding rates actually goes back into... For USDC, it value accrues into itself. So USDM, you keep getting... Your balance just keeps going up and it's the same for hype. It's just your hype balance goes up instead of USDC. Very cool. Reminiscent of

**[13:32] SPEAKER_00:** Liminal's delta neutral strategy, correct? Back in the day. I think they're still around as well. But here, the yield is paired to a stablecoin. Yeah, yeah. Yeah, pretty much. Nice. And you mentioned hype obviously being very liquid, convenient spot asset to acquire and Bitcoin as well. I think there's some good liquidity on hyperliquid. Can you... But sometimes those funding rates go

**[14:02] SPEAKER_00:** below 13%, especially for hype. What are your thoughts on kind of integrating stocks and eventually that they are way more liquid assets, perhaps not on... Could be a play there as well. Yeah. So it's actually something that we've been looking into a lot. I mean, HIP3 being what it is with when spot stocks come out. There are actually a few deployers that are coming out. There's one that we were talking to

**[14:32] SPEAKER_00:** a few weeks ago. I think it was called EQX Labs. They are building spot stocks for the actual purpose so that you can be able to build stocks. delta neutral or you can hedge with the spot stocks um and hip3 markets but yeah so the reason that we said we're that we're currently using hype and bitcoin is because portfolio margin is enabled on hype and bitcoin uh it's not enabled on like most assets

**[15:02] SPEAKER_00:** on hyperliquid i mean just because there's not enough liquidity and i mean everything's not as liquid as hype and bitcoin is on on hyperliquid um so yeah i think yeah yeah once um hyperliquid expands we can definitely look into doing more things so you know spot stocks as the long side and hip3 as the short side so that we like hip3 funding rates are actually absolutely

**[15:33] SPEAKER_00:** insane i don't know if you're taking a look at like a few months ago when oil was going crazy you were getting paid like up to i don't even think i think like 80 to just be on the shorting side um i mean if you look that sandisk uh i i remember it was in the thousand percent at a certain point or sk hynix as well when the ram was running crazy yeah even um what was it uh spacex you can

**[16:03] SPEAKER_00:** just get paid to short spacex which was uh yeah kind of kind of wild so uh yeah it's it's very much on our roadmap um but it's also determined by when hyperliquid scales for us to be deploying that so anything that does get filtered into their portfolio margin system we will be able to make into a strategy very cool and what was i guess the decision process here of deploying a stable

**[16:33] SPEAKER_00:** coin on top you know kind of using this delta neutral strategy to create yield on a stable coin or perhaps not just give out the yield flat out like what does the stable coin bring in here okay um so yeah having a stable coin just kind of gives more um more composability and accessibility um throughout and any ecosystem so i was thinking about this today um so you know people

**[17:04] SPEAKER_00:** can uh one thing popular with stable coins or yield bearing stable coins is looping um so you can you know use a borrow lending protocol take for example um hyperlend you can borrow uh you can't right now but you potentially can in the future borrow usdm on um hyperland for more usdc and then deposit it back into monitrix for like 2x yield so basically as long as the um the

**[17:35] SPEAKER_00:** yield rates are better than the borrower rates you're going to be making much more money um we're working with uh we're actually working with someone on this it's called um flex they're the team from言 um and we're trying to kind of make a 4x borrowing loop so it's like the max apy could potentially be up to like a hundred percent i mean if you're a you gotta be a bit of a deegen to go that far um but yeah there's a there's a lot of more

**[18:05] SPEAKER_00:** interesting um approaches that you can take when you layer on the stablecoin and then there are even more updated yeah which would be a lotaze potential opportunities like having a hip three markets or having like a hip four um quote asset uh against it i mean this is like completely speculative but um it kind of gives that uh opportunity in the future rather than just have a have a vault do you remember abracadabra mim where you could uh loop it

**[18:35] SPEAKER_00:** was ust back then maybe this was a little while ago but uh eventually it was a little too dgen that being said here you are your stable coin is 100 back by usdc is that correct yeah yeah so you know there's no risk of d pegging is is my point yeah i gotta gotta be yeah save from from getting pegged um

**[19:07] SPEAKER_00:** so very cool yeah obviously having the option to use you know your stable coin in hyperlend is really cool i'm i'm always thinking you know on the perp side what do you think about using it as collateral for hyper liquid perps and then earning yield on top right like right now i have open positions and i'm not earning anything i'd love to use stocks as well as collateral but

**[19:37] SPEAKER_00:** what about using usdm you know perhaps i want something that's less volatile than certain stocks and might as well earn 13 on top yeah i mean there's yeah that's kind of just the um the the the factor of having a stable coin built into it or any uh any kind of you know lst uh to play around with it yeah just opens up the Koran as let's do it but as we've just realized that it's a bit of a stretch for us so how many more doors nice and you know let's let's

**[20:07] SPEAKER_00:** close this usdm by kind of talking about risks i said there was no pegging risk but you're still running a strategy is there any risk with abl you know auto deleveraging something like 10 10 i think liminal handled that quite well but still maybe walk me through um you know what are some of the mitigation or i guess some of the risk strategies y 'all y 'all have implemented in case of a huge downturn and y 'all being

**[20:37] SPEAKER_00:** stuck you know with one position or the other yeah uh fair enough i think it's a valid concern that everyone has after 10 10 um we have a like adl defense mechanism so um we have an automatic rebalancing that um i mean we have our own internal thresholds that shows like a um what is it like a range where

**[21:07] SPEAKER_00:** you can see the neutral like neutral so you're in like a good range and then the um like low end so you're about to get liquidated or the high end where you know nothing's going to happen or high and low can be the opposite of the same thing so i think it's a valid concern that everyone has after 10 10 10 directions as well um so anytime we get into the um threshold of being you know anywhere close to a liquidation we rebalance the positions um automatically it's all executed on chain as well but yeah and

**[21:37] SPEAKER_00:** yeah that's the main thing we we back tested it against we back tested it against 10 10 just to like kind of make sure that it works um and have that as a um as a testing function uh yeah i guess that's the biggest risk um in terms of i mean other than say contract risk uh would be the liquidations on hyperliquid um which yeah yeah gotta be

**[22:08] SPEAKER_00:** mindful i mean there there is yield here which is sustainable which is consistent but there's always you know the smart contract risk in this day and age with ai i feel like now it's when you say smart contract risk people actually respect it back then it was like you know whatever but it seems you guys also have an approach or back tested you know very very big downturns such as 10 10 and um the strategy is robust here yeah pretty

**[22:40] SPEAKER_00:** much um i think in d5 right now everyone is pretty much concerned about where their money is going i mean it's it's more prominent than ever because there's been so many different breaches and so many different uh just that have happened in d5 um we kind of have been affected just you know talking to different people and uh you know people have different um you know risk tolerances now that uh how

**[23:12] SPEAKER_00:** much d5 stuff has happened in the last i don't know six to six months to a year it's kind of insane when you when you actually go back and look at how many things have happened um yeah like trying to bring a new or a different approach is um is the way that we're trying to take this about because you know just the examples that i brought up before like altura and neutral you know neither of these contracts actually got exploited

**[23:42] SPEAKER_00:** so nothing happened like to their contracts um so like you know it should be quite and quite safe but like because they were um off chain and the um you know the the the the the the the the the the the the the the the the the the yield wasn't transparent people don't know exactly where their money is going then you know it's a different set of risk factor other than um contract risk as well so yeah there's a there's a lot of different um problems and uh

**[24:12] SPEAKER_00:** yeah being on chain is uh one uh one big advantage that we have compared to you know say our predator successors especially on hyperliquid i remember when Athena made their bid to have the USDH ticker. That was one of the big criticisms is, you know, they kind of were using these sexes and that wasn't part of the ethos. And you guys being fully transparent and fully on hyperliquid to generate your yield

**[24:42] SPEAKER_00:** using a delta neutral strategy. I feel it's very aligned. So pivoting from USDM, which I feel is a great asset. You know, if you want to hold stable coins, get a little bit of yield on it. If you guys get more composability, I'm sure you're going to get more adoption. Now I want to talk about what people are really interested in and not that they don't love stable coins, but they really love hype and getting yield on their hype. So talk to me about MX hype. Yeah,

**[25:15] SPEAKER_00:** cool. So we just launched MX hype pretty much a week ago. I think it may have been just over a week. But it's still a very, actually coming close to two weeks now, I just checked, but it's still a very new product of ours. We incrementally increased the caps from 5 ,000 hype to 20 ,000. And now we just recently updated the caps to 50 ,000 hype. Yeah,

**[25:46] SPEAKER_00:** this was, we basically just increase it gradually at the start to make sure the strategy is going to be as good as possible. It's running as planned. I mean, obviously we test internally with our own funds first, but then, you know, growing, it's a much safer approach to grow a bit at a time gradually than all at once and the unknown happening. Yeah, it was actually a very, very good first week. We had

**[26:17] SPEAKER_00:** a average of, I think, 18 % APY for that first week of deposits. You know, I myself almost got like one hype back in one week, just from staking, or just from staking MX hype on Monatrix and the same amount got me maybe like 0 .2 hype on native staking. Did you say 18 %

**[26:47] SPEAKER_00:** on hype? It was a very good week. I wouldn't say that. I missed out. I missed out. I'm here getting paid 2%. Yeah, it was a one very good week. I mean, hopefully, whenever hype pumps, because we use hype as our main funding rate strategy right now. So, you know, whenever hype pumps and there's a bunch of

**[27:17] SPEAKER_00:** longs, the funding goes crazy on the short side. So, yeah. Could you walk me through on how this yield, basically, what is MX hype, you know, kind of the structure behind it, is it a liquid stake derivative, is it, you know, and then we can talk about where the yield comes from as well. Yeah, sure. So, I think something that confuses people on

**[27:47] SPEAKER_00:** MX hype is that how is hype still, how are you still exposed to hype if it's running a delta neutral strategy? For the yield, and this is because we use the hype that people deposit to borrow more hype and then use that borrowed hype in a portfolio margin strategy to short it with the same amount of hype that we have borrowed in the short. So, the hype that's deposited is actually, like, not part of the strategy.

**[28:18] SPEAKER_00:** It's only a part of the strategy to be borrowed against. And this is partially why the APYs on MX hype is lower than the USDM yields because of the borrowing rates. So, the strategy, though, is pretty much the exact same. It's the exact same strategy as USDM. So, it's the funding rates arbitrage on both hype

**[28:48] SPEAKER_00:** and BTC, mostly hype. Yeah, that's pretty much it. So, here, it's not a liquid stake derivative at all, right, is what we're saying. Here, it's running a strategy on hype enabled by portfolio margin, so a delta neutral strategy. And what kind of yield are you looking at on average? You know, you mentioned there were, you know, 18 % last week, but what

**[29:19] SPEAKER_00:** about, like, today or once the caps reach? And it's probably a little bit dependent on the quantity, right? Like, if you're borrowing, the rates must change. Is that accurate? Not exactly. Hypercore rates are pretty standard across the board. But, yeah, the average yield that we're… I mean, the average yield that we're trying to aim for is at least 5 % APY. This is still,

**[29:49] SPEAKER_00:** like, you know, much better than native staking. But it's just the… I mean, the 30 -day projected growth on our website right now is 6 .9%. And this is going over the past two weeks. And there are some days, the highest day was, yeah, that 24%, I think. And then the lowest day, which was… 0 % because hype had a bad day. But, yeah, it's just we're trying to find an average

**[30:19] SPEAKER_00:** of at least 5 % APY. That's the goal. I think that's a… On the smaller side, hopefully, we can have an average of 7 % to 8%. I think that would be an extremely good rate for pretty much every hype holder. Another advantage, and again, this is not an LST. But another advantage of this is minimal lockup, correct?

**[30:50] SPEAKER_00:** So, if you want to be liquid, you can just withdraw pretty much. Is that accurate? I mean, you can… You have the… You have the token, so USDM or SUSDM or MX hype or SMX hype in your wallet. You can sell it at any point of time. There is liquidity on… On HYBRA right now. But it also depends on how much liquidity is on HYBRA. And

**[31:19] SPEAKER_00:** then if you want to instantly withdraw it, there is a 0 .3 % fee on withdrawals for instantaneous. Otherwise, it can take one to three days, absolute maximum. I don't think it's ever taken three days to withdraw at any point of time. And this is just because we have to unwind the strategy. Yeah, it makes absolute… It makes absolute sense. I mean, one, there is already liquidity. Two, if you want

**[31:49] SPEAKER_00:** to take the haircut, 0 .3%. And three, if you just want to slow roll it, give you guys time to unwind the positions, then it's going to take one to three days, which is way less than native staking. That's my point. Yeah. Yeah. The… I think one… Honestly, one thing good about native staking, though, is seven days is so long that you don't want to… You don't want to unstake it. That's been my situations for high staking. It's just like,

**[32:20] SPEAKER_00:** you could, but it's going to take a week, something's going to change. I mean, there was a lot of FUD a month ago, right? Are these guys multi -coins unstaking and these dudes are unstaking? I think it was $52. You know, if you were lazy and didn't unstake, now it's 80 bucks, so in a sense, you're right. You're right. Paper hand protection here. Yeah. Yeah. Yeah. It's great. But so

**[32:50] SPEAKER_00:** aiming to get about 5 % plus yield and still you keep full exposure to hype. You're not… If hype goes up, your assets go up, plus you're getting paid 5 % yield on top. Yeah. Exactly. Because… I mean, me, Leo, the whole team. Yeah. Yeah. And everyone, I'm sure, wants hype exposure. We all think it's going to go at least well above $100, so

**[33:21] SPEAKER_00:** having it be delta neutral doesn't really make sense for that. So yeah, the hype deposited is not delta neutral. You're definitely having the same hype exposure. That's great because native staking yield on hyperliquid isn't amazing. I think we can all agree on that. And to its point, the asset is very precious. You don't want to have too much inflation. You're

**[33:51] SPEAKER_00:** looking at other chains. They often have 7%, 10%, right? Here you have 2 .1%, 2 .2%. If you do some sort of looping strategy on an LST, you can bump that to, what, 3%, 4%. And with you guys, we're looking at 5%, 7%, depending on if hype goes up or hype goes down and the funding rate. Yeah. Very nice. So you guys are running currently a campaign, I guess. I

**[34:21] SPEAKER_00:** don't know what you would call it. I call it a campaign, but bootstrapping, right? You guys want folk to be using your products. I'm seeing points. I'm seeing caps. I'm seeing lots of cool stuff. How can the community get involved right now, today, and maybe talk me through some of the campaigns, some of the incentives you guys got? Okay. Sure. So we've been running different campaigns with Merkle, first of all. We

**[34:52] SPEAKER_00:** had a 10 % APY backstop with Merkle on USDM deposits. So if our yield wasn't at least 10 % APY, then we would backstop. That ended a while ago. We were launching a Merkle campaign on MX hype as well, but things kind of got delayed. They're delayed there because the MX hype contracts were live on the first day and

**[35:22] SPEAKER_00:** then they needed a day to import the data from MX hype. So yeah, that took an extra day and then they said they needed to do additional development for at least another week. So yeah, we've been delaying that one, although it was supposed to go live on launch, it will go live sooner or later. And then, yeah, we have points for Monitrix. So this is going to be for

**[35:52] SPEAKER_00:** our governance token that will come out sooner or later. There will also be - Don't promise anything. You know, hyper EVM people, they're going to get back at you. They're going to be like, where's my airdrop? I mean, I see both sides of that. As someone that has farmed many... Yeah. There are many protocols and those said protocols have never TGE'd and also as a builder. But

**[36:24] SPEAKER_00:** yeah, from us, I mean, we built hybrid finance as well and we airdropped 38 .5 % of the total supply to users. I think, I mean, from now. I think the tokens being live for about a year, I've gotten, I think at least all of the money I've put in and then additional from the

**[36:54] SPEAKER_00:** rewards on Hybro. So yeah, for Monitrix, we're looking to follow the same ethos of rewarding the community and having as much of a say in the project as we do, basically. Yeah. I mean, you're giving them 5 % yield on hype. They can shut up after for the, I mean, what airdrop you want on top of it, you're getting yield on your hype and

**[37:25] SPEAKER_00:** then you want a token on top. I mean, that's very generous of you and I agree for decentralizing the project. That makes sense. But once you guys ready and have constant revenue stream, don't need to force it is my point. So yes, points is something that you guys have. I think I saw some stuff. I think I saw some sort of badges or I think there were, what are they called again? Those NFTs that you can't move. SBTs. Right. Yes. What

**[37:56] SPEAKER_00:** is that? Yeah, that was for our Genesis depositors. So I'm actually not even sure if we deployed them yet, but yeah, we still have all the wallets recorded. So anyone that deposited into Genesis. Which was a one mil cap pre -deposit campaign that we ran before Monitrix went live officially. This was to help bootstrap liquidity at this, at the very, very beginning like

**[38:26] SPEAKER_00:** when we, we didn't even launch yet. So yeah, all, so yeah, we recorded all of those wallets. All of those people got gems, which translated into points boost on Monitrix and yeah, an SBT. Nice. So points, SBT and few more campaigns in the pipeline as well. How can people get involved? I guess, obviously give you

**[38:57] SPEAKER_00:** a follow. What else they should be doing here? I mean, it really depends on what type of, you know, I think there's three things that people can really do here. One is deposit USDC. If you want. Yes. If you want to hold a stable coin and want yield on top of that stable coin. Two is, you know, the same thing with hype, deposit hype or stake hype for additional

**[39:28] SPEAKER_00:** hype yields. It actually auto accrues hype as well. So that's a nice bonus. And then three, we have a yield sharing function, which we just introduced the other day. And this is anyone that you refer. Yeah. So if you go to Monitrix, you will get 10 % of their yield forever. And that will come out of the platform fee. It won't come out of the, like the user that you referred fee. So it's

**[39:57] SPEAKER_00:** kind of a win -win situation for the referrer and the referee that, yeah, you can, you can make money just by, you know, referring people and tweeting it out. Nice. And yeah, I love that approach. It's a hyperliquid. Referral code ask where you get reduction in fees and that person gets, you know, some of your fees on top. So it's a great concept to win, win, like you

**[40:27] SPEAKER_00:** mentioned. Okay. So there's a lot that you can do today on Monitrix .xyz. I feel like getting some MX hype exposure to me makes a lot of sense. Getting 5 % yield on hype. You can on top of that pretty easily LP that. On Hybra, right? I think I saw something like 30 % in terms of wrapped hype, MX hype, something like that seems pretty safe to me. So double dipping, you know, in terms of yield

**[40:57] SPEAKER_00:** generating strategies, probably that one's not going to last for so long because people are going to be depositing because they want to take advantage of that still. And referring your friends, getting some points and yeah, being on the lookout for more cool campaigns. For the adoption. What can you tell us of your plans within the next year? Sorry, I had to dive on my computer.

**[41:29] SPEAKER_00:** No worries. Did you hear the question? So what can we expect in the future? Oh, okay. So there's a few things that we're trying to work towards. One being more integration. So working with, you know, Monitrix .xyz. I think that's a really good way of saying that, you know, we're aiming to be able to I think people are going to need a lot of different ways to like borrow and lending protocols, to be able to use your USDM as collateral for whatever, if you want to loop it. If you want to borrow more hype against

**[41:58] SPEAKER_00:** or if you want to just use that money for whatever else while gaining yield. Second is we're aiming to have more integrations as well, like Pendl. So you can have, you know, YTs and PTs. Kind of just the more yield, however you see it, or YT's. I think YT's is the D -Gen one and PT is the sixth one. I

**[42:28] SPEAKER_00:** can never remember exact, but yeah, Pendle is cool. And we're working towards having a listing there. What else? We are working with, as I said before, Flex, which is a sub -project from Yeun. Yeun was a major DeFi protocol. It still has, I think, a few hundred mil in TVL on the looping mechanism for

**[42:59] SPEAKER_00:** USDM. And this one will go pretty crazy on the APYs when it does come out. So I'm pretty excited to abuse that, at least at this point. Yeah, I'm excited to abuse that myself. And then what else? Yeah, there's a few different things we're working towards. We were talking to a neobank the other day on being the yield provider for them as well. I mean, Web3

**[43:29] SPEAKER_00:** is growing in a hole where we're trying to kind of position ourselves as the greatest yield on Hyperliquid, at least for now. And yeah, hopefully go cross -chain and be able to kind of bridge the gap a little bit for taking over kind of some of the spots of major DeFi protocols that have not lived up to their transparency. And being

**[43:59] SPEAKER_00:** on -chain kind of puts us in a great position for that. Yeah, I love to hear it. Lots of DeFi composability here. And you guys getting... I love getting yield that to me is quite sustainable for a perps, you know, running a delta neutral strategy on perps. That yield is almost always there. So I'm really bullish on USDM and MX hype. I'm definitely going to be depositing some. You mentioned as well neobanks. I think this is one of the big

**[44:30] SPEAKER_00:** unlocks is being able to spend, right, like perhaps getting integrated within, I don't know. I use PlasmaCard now. But I'm going to shell Hyper -B too. Being able to earn, right, 13 % yield. And then eventually if I want to buy a coffee, well, then I can. I don't need to do all these, you know, conversion steps that create a lot of friction. I think that'd be really cool too, if you guys have that. Yeah,

**[45:00] SPEAKER_00:** I mean, I think Athena just launched their neobank yesterday. On Arbitrum, I think, or something like that. No, it was Ava. It was Ava. Oh, Ava, right. I was like, why Ava? I was questioning myself. I was looking at that like out of every chain. I mean, you know, when you think about it, the chain doesn't really matter. It hasn't been hacked recently, so

**[45:31] SPEAKER_00:** it's not reliable enough. So it's fine. Yeah, yeah, no. I mean, most neobanks. I think like 90 % of them are powered by Solana right now. Yeah, Hyperbeat is like, I think, the only neobank on Hyperliquid at the current moments. And then there's Ilios Pay, which is coming soon. Nice. Okay, well, cool. All right, all right. Let me ask a few more questions I had

**[46:01] SPEAKER_00:** here. So Hypercore, I think I mentioned this earlier, and I know it's not always up to you with portfolio margin assets. And so on and so forth. But do you foresee some time where MX Hype and USDM could be on Hypercore and people could use portfolio margin on those? And even perhaps open positions, you know, with pairs on USDM? I don't know if that one is going to be possible, but still like

**[46:31] SPEAKER_00:** bigger integration on the main blockchain. I think I'm using it as a court asset. It would have to be like a. A hip three market deployment, which if we do find a partner for that, I don't think that we would be in a position to launch it alone. I mean, you know, just say, for example, Athena just wound it down their hip three markets, which was Hyena the other day.

**[47:03] SPEAKER_00:** I think it's a very cool, cool thing to do in theory. But it would be much, much. A month later, down the line in all realizing in all realistic. Reality or realistic. Ness I can't speak English sometimes. Ask Circle. Ask Circle. Tell them, bros, we can earn 13 % on USDC. Why not integrate us? And they do it out of the box. Yeah.

**[47:31] SPEAKER_00:** Let me cool. Right. Let me. Let me DM them right now. I'll hook you up with Jeremy. He's launching Arc chains very soon. So he's quite busy. Right. but no, I don't know him at all. But yeah, anyways, but still, perhaps maybe MX hype on portfolio margin, that could be something we could see. Yeah, I think with scale, I don't think there are many things. I

**[48:03] SPEAKER_00:** actually think there are only majors right now that are enabled on portfolio margin, but yeah, hopefully down the line, we can see much more community -built products that will be enabled on Hyperliquid. And yeah, it would definitely be awesome if MX hype was one of those. All right, one more thing, because it's so topical. MX hype, everybody loves hype. Not everybody loves USDC, it's okay. But the new

**[48:33] SPEAKER_00:** hot thing, did you know, stocks? That was a really cool one. That was a really cool thing that people have discovered very recently. Right, right. I don't know if you know about this thing called stocks, but it seems like it's the new craze. And wondering if it was possible, and I'm sure it is, right? Like we discussed it a little earlier, but would it be in your pipeline to create some sort of, I don't know, Apple Delta neutral strategy? You mentioned SpaceX earlier, Sandisk,

**[49:04] SPEAKER_00:** SK Hynix, all of these very, very popular stocks. Yes. You still get exposure to the stock, but on top, you're actually earning yield here, which you're not when you're holding, you know, the classic stock in your, actually, usually you're paying a fee here. So yeah, please tell me more about RWAs here and how you guys plan to create some Delta neutral strategies around. Yeah. Yeah, as I said, it was, I said before, it was,

**[49:34] SPEAKER_00:** it's always been on our roadmap to use HIP3 in strategy. But it's just a bit of a, at the current moment on Hyperliquid, it's very difficult because, I mean, one, you need the assets to be exactly aligned. So you need the PERP and the asset to be like having the exact same price, the exact same oracle to be completely

**[50:04] SPEAKER_00:** Delta neutral. And, but yeah, as I said before, there was one provider, it's called EQX. They're looking to deploy spot stocks in the near future, I believe. And yeah, we're looking to work with them or just use or utilize what they're bringing to the market, which is going to be using the HIP3 markets as what they're going to deploy. They've

**[50:35] SPEAKER_00:** been, I mean, as I'm sure, anyone can imagine deploying spot stocks on a decentralized exchange is a bit of a legal nightmare. So I think it's taking a while for them. I think X stocks also launched, but yeah, the issue is just not exactly one -to -one on being able to perform a Delta neutral strategy on that. And then, so yeah, once there are more, we

**[51:06] SPEAKER_00:** have more spot options. We're definitely keen for it. And then expanding on that, once there is enough liquidity on the spot side, then I think hopefully Hyperliquid will enable portfolio margin on those assets because definitely as more spot stocks are launching right now, there's not going to be any portfolio margin on them. And then portfolio margin just kind of amplifies the strategy like much, much

**[51:36] SPEAKER_00:** more. It allows your capital efficiency to be much higher. So yeah, there's a few things that need to fall into place for us to be able to capture like the perfect HIP3 funding rates, which I think when that day comes, we will be seeing very, very high APY numbers, like 50 to 100 % on good days.

**[52:06] SPEAKER_00:** And then we can deploy more markets. So, you know, oil, gold, SanDisk, SpaceX. The future is kind of limitless in that aspect. But it's a matter of when. I love that. It's a matter of when. Would you say this is kind of the giga unlock for, you know, three -digit hype? Might as well go super chilly here. If we get liquid stocks, you know, then

**[52:36] SPEAKER_00:** at that point, you mentioned using collateral stocks. I think everybody does this in the TradFi industry, using, you know, your stocks as collateral to open positions. To me, that is absolutely huge. You guys enabling yield on them as well. So probably the next big thing, I know I'm also bullish on HIP4, but to me, it's going to be kind of the execution of good stock implementation on

**[53:07] SPEAKER_00:** Hypercore. So if you want to comment on that, go ahead. Yeah, yeah, for sure. I mean, I think just giving the opportunity of spot stocks. I mean, not everyone. I feel like a lot of people, I think there's a basket of people in Hyperliquid that are like perpetrators and then a lot of people that, you know, hold, you know, just hold hype. And then outside of Hyperliquid, there's a bunch of people that just hold Bitcoin, right? And whatever

**[53:37] SPEAKER_00:** else coins. So, yeah, there's the same thing for for stocks. And I think the basket is actually much, much, much wider on the amount of people that hold stocks than any type of crypto, especially hype. I think there's still only 300K holders. But yeah, I think that'll be a very big unlock. And the way that at least the EQX Labs guys are talking about it, they kind of understand that people would want to hedge against

**[54:07] SPEAKER_00:** HIP3 markets. So they're building towards that, which I think is a really smart idea. Very excited to hear more from them. I'm going to give a shout out as well to Denari. I think we hosted them on a space. They were the first ones to deploy a real SpaceX stock on Hypercore. Still, there's not much trading volume or liquidity. I mean, they have like half a million, which is pretty cool. But I think the composability

**[54:37] SPEAKER_00:** is. They're not lacking versus something on Robinhood chain where you can earn like crazy APYs by just LPPing on Uniswap. But once we get you mentioned this, like using it as collateral yield strategy and so on, it just can scale so much harder than AMM stuff. So I'm very excited. Yeah, yeah, definitely because, you know, when I when I first talked to the EQX

**[55:08] SPEAKER_00:** Labs, I was like, okay, that's not good. guys. I wanted to ask, will this be able to be hedged on HIP3 markets? And they were working towards exactly that function. So I thought, I mean, I'm not 100 % sure how Denari works. I haven't looked into it that much, but I'm guessing it's not one -to -one pegged with how the HIP3 oracles are. Yeah, they have different approaches here. The Denari one, you can actually have a KYC account

**[55:38] SPEAKER_00:** and have all the perks of owning a real stock. So that's their focus, having that dual approach of having it composable with DeFi if you choose to do so, or putting it in a KYC account where you can have the real stock. But anyways, like all these players, as long as there is something to do with said stocks, like earning yield on top or using as collateral, then I feel like it's going to grow really, really fast. Really, really quickly

**[56:08] SPEAKER_00:** versus now just kind of spot buying them and selling them without having any differentiator versus your classic brokerage. Yeah, I think, yeah, I'm very keen for, I think Hyperliquid can, I think I said this the other day, I tweeted it. I think Hyperliquid still has like the opportunity to grow like, like, I think, I mean, I said it was like 1 .5 % out of 100%. So yeah, I think there is a lot

**[56:38] SPEAKER_00:** more to come. I think, yeah, Hyperliquid's definitely going to continue to grow. I think it's going to be existing for the long term and, and I think it, it's going to be a huge one. Love it, love it. Everybody's bullish. Pumper hype bags, but they've already been pumped. Like, I mean, like at this point, it's it's just a cherry on the sundae and, you know, we got the ecosystem thank you for building up. Thank you for choosing Hyperliquid. You know, this is one of the questions I ask is why did you choose Hyperliquid? But at this point, like, you couldn't do this anywhere else. Right. As far as I'm concerned with, if having

**[57:09] SPEAKER_00:** on Hyper -EVM this protocol and using precompiles to run the strategy on HyperCore, it's very unique in terms of infrastructure. Yeah, it can only be done because of HyperLiquid. I mean, I think a bunch of things can only be done because of HyperLiquid. I mean, aside from this, there is a project that I'm advising called Ensemble. And yeah, they can also only be done because of

**[57:39] SPEAKER_00:** HyperLiquid. And they're like basket perps. So kind of like bounce tech, but basketed. So yeah, HyperLiquid unlocks a whole bunch. And as for the reason why someone would choose to build on HyperLiquid, I think it's the only real pathway to build something for the future right now. I mean, I'd say Robinhood is really cool. Yeah. But there's a bunch of different other chains that I

**[58:09] SPEAKER_00:** don't know why you would choose to build on them in this time. Personally, I've seen, say, BNB chain. There is a crazy amount of scams on BNB chain. And they purely only pump their own shit and use retail as exit liquidity. So there is, I think, only the only other way is to build on HyperLiquid. The only

**[58:40] SPEAKER_00:** option is to build on HyperLiquid. And I, Syke, doesn't get any more bullish than this. I love the, let's end on this. But yeah, thank you so much. I think we're going to the top of the hour. It was really a fun conversation to have with you. For those that just tuned in, the space is recorded. So you can listen at a time that works best for you. Give Syke here a follow. Give Monatrix a follow. Get some stablecoin. Get

**[59:10] SPEAKER_00:** some MX hype if you want to earn 5 % yield on your hype. Plus, you get points on top. He mentioned that the points will actually lead to some token. He has promised this on his space. You can always clip it and shoot it back to him if he doesn't follow through. I'm just messing here. But yeah, really cool project. I'm excited as well for some sort of stock offering, you know, getting yield on stocks to me would be really, really cool and unique and only possible on

**[59:40] SPEAKER_00:** Hyperliquid. And yeah, any closing thoughts? Any closing words? Any last call to actions? No, it's been a great, great space. I appreciate you taking the time for this. My cat's meowing at me as well. She probably wants treats. At this point, I mean, it's 12 o 'clock. The man stayed up late for y 'all. So thank you for the time. Really

**[1:00:11] SPEAKER_00:** appreciate hosting these. And on that note, I will end with Hyperliquid. It's Hyperliquid.
