# SuperSexy brings centralized exchange UX to Hyperliquid, $750M volume in one month

_Chris from SuperSexy explains building on-chain finance on Hyperliquid with familiar CEX experience, competitive 6bp fees, and Turnkey self-custody._

**Host:** @hypurr_co
**Date:** 2025-09-04
**Duration:** 45:18
**Tags:** infrastructure, trading, ecosystem
**Source:** https://x.com/i/spaces/1mnxeNMaXWZKX

## Who's talking

- **HypurrCollective.hl 🐱** (@hypurr_co) _host_
- **chroma** (@chromatique) _guest_
- **Chris Ling | NLH** (@chrisling_dev) _guest_

## Key moments

- **[5:56]** Hyperco intro: 1.5B AUM validator, content, IRL events
- **[8:27]** Chris background: 6-7 years DeFi, MEV, Talisman wallet, Hyperliquid interview 2023
- **[11:30]** SuperSexy motivation: nobody actually doing on-chain finance despite Hyperliquid hype
- **[13:02]** SuperSexy builds CEX-like frontend on Hyperliquid with HyperLend integration
- **[21:09]** Fee structure: 6bp all-in, competitive with Binance 5.5bp, invite codes lower rates
- **[24:10]** $750M volume, top 5 ARPU, power users, no active marketing yet
- **[29:16]** New feature tonight: chase limit orders, feature parity with CEX priority
- **[34:24]** Security: Turnkey enterprise self-custody, audits in progress, in-app education

## Transcript

**[2:26] SPEAKER_00:** GM, GM, just waiting for Chris from SuperSexy to join us as a speaker, and then we'll begin. Sorry,

**[4:13] SPEAKER_00:** just having a bit of technical errors will await Chris to be back on. All right,

**[5:56] SPEAKER_00:** perfect. I think we can hear you now. Chris, can you unmute again and test your mic? Yeah, yes, thanks for your time. All right, perfect. Okay, I think we can go ahead. So for those unfamiliar with Hyperco, we regularly conduct this PMA. Hyperco is founded by three of us, Kirby, Noel, and myself, Velocity. Started Hyperco with the mission to

**[6:26] SPEAKER_00:** unite different demographics of users, builders, and traders, and pretty much everyone that are excited about Hyperliquid in this ecosystem. We've done this through... a variety of different key initiatives. I think the first one being the most well -known for the largest validator outside of Foundation Notes, together with Nansen. We have, I think, like, 1 .5 billion in AUM on that stake amount.

**[6:58] SPEAKER_00:** We also do a lot of content creation in the form of weekly recaps, ecosystem guides, and also project guides, which we've collaborated mainly with Uncoiled, like, recently. We've pushed out a couple of pieces in the past two to three weeks of projects building on top of Hyper -EBM. So do check that out if you are interested to dive deeper. We host a lot of in -real -life events to connect different builders and

**[7:27] SPEAKER_00:** traders in person. So if you've been to one of those, I think most of you would have enjoyed it. So we really do a lot of stuff in this ecosystem, and I think that's not exhaustive list. So I guess we also help with projects, Spotlight, push -trapping of liquidity and users. So today we have one of the one

**[7:57] SPEAKER_00:** of a very special project that I've met the founder, Chris, in person a few times and only have great things to say about him. So I'm very excited to have to do this one with him. Chris, why don't you give a quick introduction about yourself and your motivation behind building in SuperSexy? Sure. Thanks, Velocity. It was very great meeting you in person as well. You're a great, great, great guy. My background,

**[8:27] SPEAKER_00:** I've been building in DeFi for the past six, seven years. I started building, started my crypto career building in DeFi. I was in a prediction market back in 2020, I think. At the time, it was a pre -prev era. It was pre -turnkey. There was no Moonpay for onboarding, on -ramping and off -ramping. And so at the time we were, I was spending a lot of my time trying to figure out how do you onboard

**[8:57] SPEAKER_00:** normies to trade this on -chain speculative stocks in a way that anyone can try. So I know that I can trade without much knowledge of crypto. And so I spend a lot of my time over the past few years just getting into designs, user experience, and also getting out front end applications. Later on, I spent about a year doing MEB. I did solo searching for some time. Not everyone knows I have this kind of past experience, but I did a year of very competitive MEB searching where

**[9:27] SPEAKER_00:** I got to learn a lot of things about very low level EVM programming. And that's where I kind of gathered a little bit of my knowledge. of somewhat HFT, a little bit of experience there. And then also spent about a year building a sub -custody wallet called Talisman. It was the largest wallet in the Polkadot ecosystem. I also worked pretty closely with Parity Tech to build a multi -sig product for their day -to -day finance operation guys. They

**[9:58] SPEAKER_00:** don't necessarily know about gas fees, things like that. And I had to, I was kind of forced to figure out how do you build things with these guys that don't necessarily know how to properly approve a transaction on -chain. And so most of my experience in the past have been related to building high performance and user -facing products, consumer products. Bit of a fun fact, I actually got a chance to interview for a

**[10:28] SPEAKER_00:** front -end role at Hyperliquid Team back in early 2023, we got to the very final stage of the interview and beyond. We went back and forth on email multiple times, but then unfortunately the time zone didn't work out. But I think that's when I got a first look at Hyperliquid in the very early days and began following the projects. And then earlier

**[10:59] SPEAKER_00:** this year, I joined our funnel in the holdings. I actually met our partners through a Hyperliquid event as well, but got a chance to meet the gentlemen here and they gave me a lot of opportunities to kind of learn and invest alongside them as well as see how we could help out with some of the ecosystem projects in Hyperliquid. And then got to see a lot of things. And one thing

**[11:30] SPEAKER_00:** we talked about a lot was, everyone talks about Hyperliquid being the on -chain finance, or on -chain By -Pay, but we looked at a lot of projects. We don't actually see anyone actually doing an on -chain finance. And so the motivation for me was actually, why don't we try to do an on -chain finance ourselves? And so, yeah, there you go. Right. So SuperSexy

**[12:01] SPEAKER_00:** is definitely a name that is pretty attention grabbing. Do you want to share a bit on how you guys arrived at this name? Yeah, I mean, it's very straightforward. We wanted to build something very similar to Centralized Exchanges, because I think Centralized Exchanges invested a lot of resources and talent into building some of the best user experience in crypto in general. And so we think, like, why reinvent the wheel? Why not just build something that someone has

**[12:31] SPEAKER_00:** really spent so much time and effort trying to master or perfect, right? And we think, actually, Centralized Exchanges have some of the best user experience. And so I thought, like, I think the way to grow something like Hyperliquid from here is you actually want to try to get more of these people that have never gone on -chain to try to trade on -chain. And so we wanted to build something that is very similar to the experience on a Centralized Exchange, but fully on -chain on Hyperliquid, where you subclassify your assets. And so SuperSexy is basically like, I

**[13:02] SPEAKER_00:** guess it's like, you know, the app feels like a sex, like an on -chain sex type of thing. Yeah. Nice. So for those who are unfamiliar and haven't actually interacted with SuperSexy, how do you build upon the existing infra of Hyperliquid? And what's the plan with SuperSexy? Yeah. I think potentially most of us

**[13:32] SPEAKER_00:** here have used Hyperliquid, and you know what Hyperliquid is. But in our view, Hyperliquid is a building block for the next generation of application, much like, you know, Aave or Uniswap and so on, where you can build beautiful applications on top of the logics behind. We're trying to build, leverage Hyperliquid as the kind of auto -matching infrastructure to build beautiful

**[14:02] SPEAKER_00:** on -chain trading experience similar to Centralized Exchanges, without, you know, users having to compromise on security and separsity of the assets. So for example, one thing we did was something like a Hyperland integration, where I think we actually created an experience that is extremely similar to Centralized Exchange in the sense that users don't have to think about things like bridging. This is about the current process of bridging, trying to deposit into a DeFi

**[14:32] SPEAKER_00:** protocol, right? You have to go to Hyperliquid, you have to transfer or bridge your assets. So EVM, you have to get hyper gas, you have to connect your wallets to multiple sites and so on. With SuperSaxxy, we're trying to create this experience where you just buy hype or buy BTC or whatever, you click on earn, for example, and you can deposit your assets into DeFi protocols in one click, right? And in trading, we're trying to create an experience that most Centralized Exchange users that come here wouldn't feel like they are getting a downgraded experience. Instead, they are getting a

**[15:02] SPEAKER_00:** experience that is at least on par or upgraded. While also getting an upgrade in their secrecy of their assets. So I would say SuperSaxxy is a front -end that does a lot more than what Hyperliquid offers today, trying to match the experience of Centralized Exchanges on Hyperliquid. Well, I think you just touched on one of the key products about users, since you have Hyperland

**[15:32] SPEAKER_00:** integrator, users can pretty much do everything they want, right? Everything from buying of hype and supplying of hype, or even majors like Bitcoin, ETH, through Unite, and then supplying it on Hyperland, all through SuperSaxxy itself. So with that, do you have any other unique features of SuperSaxxy that you'd like to highlight that differentiate yourself from competitors? Yeah, one thing we just announced, I think two

**[16:03] SPEAKER_00:** days ago, was a trading session. We actually have been booking on this for some time. We have been setting up a massive infrastructure in the backend to sitting in Tokyo right next to some of the best location to place trades on Hyperliquid. We're setting up some of this infrastructure to be able to offer much, much more complex things for Hyperliquid users that Centralized Exchange have always had privilege to. So things like, actually I'm not gonna leak now, but stay tuned, we're

**[16:33] SPEAKER_00:** gonna announce something tonight, or release a new feature tonight. We're gonna add a lot more things that a Centralized Exchange users that comes to Hyperliquid today would feel like, wait, why do we not have this here that they are used to in a Centralized Exchange? And so we'll be offering much, much more of these features on SuperSaxxy, and also with much, much more integration with Hyper -EVM ecosystem projects that would make a Centralized Exchange users coming here not think that they are getting a downgrade experience. So

**[17:03] SPEAKER_00:** yeah, stay tuned, we have a new feature coming up tonight. I was still writing the final line of code for this call, and we'll probably be announcing it tonight. Nice. I know you've been teasing in our group for a little bit, so pretty excited to see what you announce, hopefully in a few hours. So since you have this sort of different features and extra utility on top of Hyperliquid, what are some pain points that you

**[17:34] SPEAKER_00:** hope to elevate for users? Since especially also like beginners and experienced traders have different needs, how can each of these group best benefit and maximize the experience with SuperSaxxy currently? Yeah, I think we have to first define like the audience we're trying to target here. So then we can kind of pinpoint this, what the pain points we're trying to solve for them. One of the main group of

**[18:04] SPEAKER_00:** users we actually wanna try to target are centralized exchange users that have never gone on chain. And the pain for these users is pretty straightforward. Some of them, they don't even have a MetaMask wallet. They don't know what a Seapraise wallet is, but they trade a lot on centralized exchanges. Some of them, most of them don't know how to bridge, for example. And so we wanna try to solve the entry point problem for some centralized exchange users. Some of these users that have never or rarely goes on chain. We wanna help them, you know,

**[18:34] SPEAKER_00:** we wanna build the easiest path for them to come and trade on chain and have their day -to -day activities . There's one thing we learned from speaking with a lot of centralized exchange users is that most of them have concerns around their assets being frozen, for example. Like, I mean, let's follow the white whale on that. I think he's like starting like a war with like Mexi or something because his assets got frozen. I think a lot of people, especially the smaller guys, actually faces these kind of issues

**[19:04] SPEAKER_00:** every day. But because they're much smaller, they don't get to surface this on platforms like this. And so I think, you know, the people we're trying to help them solve is by leveraging hyperliquid and kind of on -chain experience. These users will no longer have to worry about their assets getting frozen by exchanges, while at the same time, using some of the additional tools we're building for them, it would get this exact same or even better trading experience that they are used to on a centralized exchange. Yeah,

**[19:38] SPEAKER_00:** I think everyone definitely has seen the saga with MEXC by the white whale about how he controlled his funds and is just going pretty crazy over it, but I do agree. I mean, that's the famous saying of not your keys, not your coins. So, it's definitely quite a high barrier to entry, especially if you've never created your own self -custody wallet in this space. I remember when I first started it was such a pain point. And

**[20:08] SPEAKER_00:** I watched thousands of videos just to familiarize myself with the wallet and that's before even dabbling on Chain. So I think what you guys are doing with SilverSexy, especially all the different integrations and having them in your app itself without someone having to handle all of these is definitely very helpful. So with that, I think it's helpful to touch on what kind of fee structure you guys have right now and also how do you

**[20:38] SPEAKER_00:** plan to... I mean, because Builder Code actually allows you guys to have a fee on top of HyperLiquid's existing. So with that also, why should users not just use the HyperLiquid frontend itself? Do you want to touch on your fee structure and also how that extra bit is actually worth it on SilverSexy itself? Yeah. Yeah. So our total... Base fee is

**[21:09] SPEAKER_00:** about six basis points for completely new users. So if you don't have any discounts or you have not traded any volumes for the volume discounts at all, you would be paying a total fee of six basis points, 0 .06 % of fees, including HyperLiquid fee. We intentionally designed the fee this way to... First of all, we're not here to build for... I guess we're not trying to extract from the existing HyperLiquid ecosystem. And so we think by putting

**[21:39] SPEAKER_00:** a higher fees, it signals our intention to bring in net new liquidity and users outside of HyperLiquid. And second, the fee structure is actually very competitive to even centralized exchanges. So if you look at some of the top, the T1 and T2 exchanges, your average fees for per trading is around six basis points to seven basis points. Binance, I think, is doing 5 .5 basis points, 5 bit as well. And so... By putting it at six basis points, we're

**[22:09] SPEAKER_00:** actually on par with a lot of centralized exchanges already. And then if you just use... Even if you just use some of the lowest tier invite codes from our users, you can pretty quickly get your fees to a rate that is much, much more competitive than a centralized exchange at 5 .5 or even five basis points. And so, yeah, total fee is six basis points. But if you just use an invite code and trade a little bit, you can pretty much get to a much, much more competitive

**[22:39] SPEAKER_00:** rate than a centralized exchange very quickly. Spot fee, obviously, it's way more competitive than a centralized exchange that charges 1%, sorry, 0 .1%. Whereas I think we are charging like... I don't think we're charging people to quote on all of the spot buy at all. It's just on selling, it's like nine basis points or something, which is still much more competitive against a centralized exchange. Yup. I think even with the beta code fee, you guys definitely have very,

**[23:09] SPEAKER_00:** very competitive and one of the lowest still compared to whatever centralized exchanges like Binance and Bybit are offering. With this, I believe SuperSaxi ranks top five in average revenue per user, which is honestly very impressive, considering that you guys, I think, went live less than a month back also. What do you think contributed to this? And... How are you guys targeting the users

**[23:40] SPEAKER_00:** that... How are you guys targeting... What kind of users... Sorry, what kind of users do you wish to target? And also, you mentioned like, users who are familiar with Saxos, but I believe a lot of the current profile are still hyperliquid users. So what kind of feedback have they given? And also, how do you... What kind of factors do you think contributed to such a high average revenue per user? Yeah. Honestly,

**[24:10] SPEAKER_00:** this... I think we picked a lot of the... We checked a lot of the boxes way earlier than I expected us to hit, but... Most of our users today, I think, are mostly power users that are trading larger sizes on even centralized exchanges today. As you may know, we haven't done any active marketings yet. We haven't... We don't have things like a points program yet. We don't have... We're not... We're not doing... We're

**[24:40] SPEAKER_00:** not very active on marketing yet because we're... We're trying to improve the product to a state where it's actually very sticky for users to use before we want to, you know, do any incentives to attract people to try. Because we don't want to... We don't want to inflate the metrics by just having incentives. We want to actually be able to talk to the users that use it every day and can give us constructive feedback on how we can improve the ad. Actually, if you're an active user, you're likely noticing some improvements here and there every day. Literally just today, we just added a new feature where when

**[25:10] SPEAKER_00:** you're trying to close a limit order, we would show the best price in the pop -up such that you don't have to close the pop -up to check the price and fill in the limit order. You can pretty much just, like, chase the limit order right within the box. These are the kind of very small details that we're putting a lot of attention to to try to make sure we create a very sticky product for the centralized exchange users. And so right now, I think it's mostly, you know, some of the power users that are giving us a lot of feedback and trading it on a day -to -day basis. In

**[25:45] SPEAKER_00:** the future, there will be more things that we will be doing to get more users on SuperSexy. But right now, I think our focus is to just work with... I guess I've been very much focused on working with some of the very active users on improving the user experience. Even the recent traction, honestly, I don't know. It was just, like, users using it. We haven't done any, like, paid marketing or campaigns. We're not forcing anyone to use it. I think the

**[26:15] SPEAKER_00:** feedback we've gotten is just that... I mean, we've processed, like, $750 million of volume so far on natural usage. You can't put $750 million through an app if it's a crappy app, right? And so I think it's just users, you know, really liking the product and using it on a daily basis as their daily driver. Yeah, I agree. I think I was probably one of the earlier users of SuperSexy. And it's really quite an honor

**[26:45] SPEAKER_00:** that you guys approached Hyperco for user testing. And I think I used it pretty extensively in the beginning. I did not use it as often in the past week because I was just mainly trading on Hyperliquid from then on my other trading wallet. But when you guys first began around a month ago, I think what really stuck to me, and I believe I mentioned to you in private or so, it's

**[27:15] SPEAKER_00:** my most used app in the Hyperliquid ecosystem. And it's really because it offers such a familiar user interface. So that was what got me attracted to Hyperliquid when I first discovered it, I think, two and a half years ago. So it's the same thing that stuck. With me as well for SuperSexy. It's really the familiarity of the user interface. Everything was smooth. There are some missing

**[27:45] SPEAKER_00:** features, but that's nothing surprising since you literally just built it just a few moments ago. So with that, I think in the past month or so, you've implemented a lot of the different feedback from not just Hyperco, but a lot of your power users as well. So it's becoming quite a super app, not just for trading, but really a one -stop shop. And I think a lot of people are excited about how much more

**[28:15] SPEAKER_00:** features you can push down. I think with that, do you want to tease a bit about what kind of upcoming features that you have on the pipeline? It might not necessarily be the announcement that you want to make later, but also a bit more hint on what kind of features you have on the pipeline. But do you want to focus on what's on your roadmap in the next month or three months? Yeah. So one thing I've always wanted to... And by the way, I appreciate you

**[28:46] SPEAKER_00:** testing it out, testing the product out early on and giving us feedback. That was really helpful. A lot of your feedback were extremely good. One thing I really want to achieve is feature priority to centralized exchanges because you don't want to spend a bunch of budgets on marketing and trying to attract a bunch of sex users to come here and be like, this is missing a bunch of things we're used to on a centralized exchange. And so I think our focus is to get SuperSexy to be feature priority to centralized exchange. And

**[29:16] SPEAKER_00:** that includes... Actually, I'll just say the feature... We're going to add a new feature tonight to allow for a chase limit where if you have an open order, for example, open limit order, you can just press on the chase button and it's going to chase the limit price for you to kind of hit the top of the book. So we'll be adding more of these type of features for our users. Basically, whatever you would see on the centralized exchange that is essential for a trader, we want to have all of them. And those would be our focus to create

**[29:46] SPEAKER_00:** one of the best trading experience on HyperQuickly. And then after that, we'll be doing more GTM things. So yeah, I better not tease too much here. Yeah, we'll be doing more of that later. Nice, yeah. So on the top of the book topic, so HyperLiquid, I think one feature that I use pretty often right now is on HyperLiquid, I mean,

**[30:17] SPEAKER_00:** there's a keyword function, but every time keyword on HyperLiquid, when you execute that, it's usually taking liquidity. But on Binance, sometimes the keyword allows you to place a bid at the top of the book. So you can pay a maker fee instead of being a taker, which can be quite substantial if you're trading size. I think that's probably something that you guys can think about doing or probably in the works. It's

**[30:48] SPEAKER_00:** in the works. It's being tested right now. We have a few of these, some automated trading features that we're going to add, you know, over the next few days or next one or two weeks, because ultimately, we're building an application that deals with real users' money. We understand that, you know, like building new products, you have to ship extremely quickly. But ultimately, we think my principle here is we're building an application that deals with actual users' funds. And so we don't want to just ship fast and not test and have,

**[31:18] SPEAKER_00:** you know, flaky products that might execute an order that's inaccurate, for example. But I'm very eager to show you the, you know, the things we've built. Especially the one you just brought up. We have that already. We're testing it. We don't want to announce it yet because we don't, we're just testing it to make sure it's reliable. But we have a lot of that kind of things built out. We actually built a pretty sophisticated engine that will allow us to roll out much, much more of these type of advanced features. And now it's just a matter of testing it out

**[31:48] SPEAKER_00:** and making sure it's reliable. Actually, one thing I forgot to touch on, on some of the things we'll be adding more to improve user experience is more hybrid EVM integration. I think if you want to allow something like, hey, connect your wallet to this website and so on, I think that's actually pretty easy to build with something like Wallet Connect. I've done that multiple times in the past with a few of the products I've worked on. But with Super Sexy, we're trying to take a much, much more opinionated approach here where we want to craft every single possible path with user experience

**[32:18] SPEAKER_00:** for our users. Because I think, like, just throwing a Connect Wallet button into your app doesn't actually improve the experience. You actually need some kind of guidance, guided paths to help users understand what they're actually doing in your app. I think the problem with DeFi today is most users, when they interact with an app, there's sort of a trust assumption with the app. Like when you go on Uniswap, for example, do you actually read the call data that Uniswap is crafting for you in your wallet? No one actually reads that stuff. Most people don't read that.

**[32:48] SPEAKER_00:** And so I think to offer much, much more secure and also much, much more intuitive user experience, we're going to be doing much, much more opinionated, handcrafted user experience with the Hyper -EVM protocols that we integrate with. A few of those will be coming up recently as well. Nice. On this topic, do you want to hint or share a bit on what kind of integrations you plan, like which DApps do

**[33:18] SPEAKER_00:** you plan to integrate into SuperSexy? Is there any plans for NFT Marketplace or Social Labs or the other existing DeFi powerhouses on Hyper -EVM? There are a few DeFi ones we're talking to and working with. Some of them are integrations that are in progress. I don't like to overpromise things, especially in a public venue like this. So we'll not be naming any of those. But we are working on integrations with some of these guys. Gotcha.

**[33:53] SPEAKER_00:** So maybe just one last question with regards to SuperSexy. I think a lot of... users are especially afraid about self -custody, security concerns in the industry. What steps has SuperSexy taken to mitigate this sort of... the risk of exploits and vulnerabilities? Yeah. So...

**[34:24] SPEAKER_00:** Yes, actually, that's a very good question. We recently integrated with Turnkey to offer enterprise -grade self -custody solution for our users. Basically, what that means is... Sorry, excuse me. What that means is your keys are stored in Turnkey's TE infrastructure that... even if your phone is stolen, for example, today, your keys are not stored. Your keys are not in your phone. It's in

**[34:54] SPEAKER_00:** your encrypted infrastructure. We are talking to a few auditors as well to try to get a potential audit on SuperSexy. Audits are pretty common for smart contract projects because you have some contracts, you look at it. I spent about half a year doing smart contract audits myself. And so smart contract audits are pretty common in crypto, but kind of consumer app audits is less common in crypto. So we're talking to a few

**[35:24] SPEAKER_00:** auditors right now to try to find something that makes sense to help audit and pen test SuperSexy. I think ultimately, on one hand, I care deeply and a lot about security. On the other hand, we have a group of... We have users that usually don't really care about these things. Like, I mean, when you go on a centralized exchange, do you ask the centralized exchange, like, hey, how are you storing my encryption key? How do you store my private key? Where's my secret? Most users generally don't do that. They just have

**[35:54] SPEAKER_00:** more trust assumptions on the app they use. And so our approach here is, you know, on the front end, when users use it, it's just, you know, you put in your email, you sign in, you have your wallet created. You don't see a lot of, you know, what's going on in the background. But in the background, we are now, you know, trying to get an audit. And I don't know if you saw, one thing I really hate with a lot of applications is when you try to click on, like, a guide or, like, learn more button, for example, they just throw you to a documentation site. And

**[36:24] SPEAKER_00:** then as if anyone actually reads this documentation site. One thing we're doing is we... Some of the guides we have in SuperSexy, we actually have an in -app pop -up type of thing that shows you the guide within the app. And we're doing more of that education, you know, content within the app to explain to users how SuperSexy is using, you know, self -custody wallets to secure their assets. It takes... It will take a little bit of time for those content to come up. You know, we have to get someone to help with,

**[36:54] SPEAKER_00:** like, the translations, the and so on to make sure the wordings are correct so users aren't misguided. But... Yeah, I think it will require a lot of education for users to understand, you know, what's even a self -custody wallet, what even self -custody means for them. Yeah. I think, to be fair, a lot of people probably don't dive that deep. So I think just the baseline of reassurance, like whatever

**[37:25] SPEAKER_00:** you mentioned, turnkey and stuff like that, is probably enough for most of them. So it's definitely good to hear that a bit of a soft shield is also a hyper -collective as a partner with SELIC. So if any of the ecosystem that's all, like, SuperSexy or whoever wants to get an audit, feel free to go through us. You get a discount. We take nothing. So it's entirely passed back to you as part of our initiatives and collaboration with different

**[37:55] SPEAKER_00:** partners in the space. I think it's pretty comprehensive we've covered, like, your whatever SuperSexy, whatever products that SuperSexy offers, how you guys differentiate yourself from Hyperliquid and also the different front -ends operating on Hyperliquid and also your upcoming initiatives and security concerns. Do you have any final words that

**[38:26] SPEAKER_00:** you'd like to talk about, share about SuperSexy before we open the floor up to listeners, for questions? A quick one. It can be announcements or any sort of specific features or sort of stuffs. Yeah, just a quick one. I guess for features, please just try out the app. We put a lot of love into the app. I stay out until very late every single

**[38:56] SPEAKER_00:** day to make sure our users have the best reading experience. So if you're curious about any of the features, just try the app out. There's one last, one thing I would share is if you have any friends today that are still bugging you with questions about centralized exchange, tell them to give SuperSexy a try. It feels like centralized exchange onboarding is very seamless and your users wouldn't have all the concerns around their assets getting frozen, for example, or which

**[39:26] SPEAKER_00:** exchange is shady, which exchange has expired before and so on. If you have some friends that are not that divisive, not that technical, but are exploring ways to trade or get on chain, please give SuperSexy a try. Have them try it out. And if they have any feedback based in your blog, you can reach me through the end. Always happy to answer any questions. Yep. Chris has been very

**[39:56] SPEAKER_00:** helpful and is chronically online doing the best for users. So if you haven't tried it, do try SuperSexy out. Let me add just one more thing. And if you are building a project on Hyperliquid or even outside of Hyperliquid, please reach out to me. We're happy to and we're looking for projects to integrate with as well as invest in as a fund. And so anyone, if you're building anything,

**[40:27] SPEAKER_00:** please talk to me. We'd love to talk to more people. Nice. Very solid. We'll just open up the floor for listeners. If you guys have any questions to ask Chris right now, do feel free to just raise your hands and request to speak if you have a question. I

**[41:18] SPEAKER_00:** think we have one from Paul. Can you hear me? Yep. Good morning. Hi. So I just had a quick question. So it kind of relates back to the discussion surrounding TWAP. So I'm a big user of in silico terminal. I love it. And in that they have functions for like swarm and batch orders. Do you guys have any plans to

**[41:48] SPEAKER_00:** integrate those type of order functions or order features into super sexy? Because alongside TWAP, that would be amazing to have, you know, to have like, you know, swarm orders as well. We'll be open to integrating those features. Actually, I'll send you a DM and then I would love to hear from you, you know, what specific things you want to achieve with this feature and what, what do you want to, you know, what are

**[42:18] SPEAKER_00:** your favorite things on those exchanges? I'll send you a DM. We'd love to chat about that. Absolutely. Yeah. Cause I, yeah, cause in silico terminal, you know, it's one of the best rating terminals that I've used in a long time. And again, they have really robust order feature sets. And so I doubt to, to have something integrated like that into your guys' platform, you know, alongside the TWAP would be just fantastic. And you know, the, the

**[42:48] SPEAKER_00:** having that, you know, maker ordering at the top of the order books too. That is, that is, I'm glad HyperCollective pointed that out because that's really understated for DEX experiences. Yeah, a hundred percent. Yeah. We'll, we'll, we'll explore that. And then I'll reach out to you to see how we can make that happen. One thing we, we do have today is we posted a video somewhat recently, or you can customize our DEX operation. And

**[43:19] SPEAKER_00:** you can pretty much arrange it to, you know, something like, you can say, for example, but yeah, more order types. We're looking to add more order types and we'll chat with you about, you know, this specific one. Bless. Awesome. That was my only question. So I appreciate it. You guys are like actually cooking some good products. So yeah, I'm here for it. Awesome. Yeah. We are all big fans of super sexy and nice

**[43:49] SPEAKER_00:** to hear a bit more sophisticated users coming on for features and requesting features that are not, you know, currently available on hyperliquid or any of the front ends. So hopefully Chris cooks something soon. I don't think we have any other requests to speak. So perhaps we will just end it off here today. I think for those who are

**[44:19] SPEAKER_00:** unfamiliar or have been wanting to try out a different front end, super sexy is definitely a very good place to start. If you have any questions, please feel free to just reach out to Chris or super sexy X on a super sexies at on X. So he's very receptive to feedback, criticisms, open to help you run through the entire process of getting your trading started on super sexy as well.

**[44:49] SPEAKER_00:** So yeah, don't be afraid to DM him and just buck him. So yeah, my PM is open and super sexy is on this space as well. If you want to give it a follow. All right. Thank you everyone for joining today. That would be all. And thank you, Chris, for coming on. Thanks for having me. Goodbye.
