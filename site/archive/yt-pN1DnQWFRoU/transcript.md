# Proper's transparent prop firm on Hyperliquid: 9.5% pass rate, AI agents, and radical disclosure

_Founder Lou discusses building crypto's most transparent prop firm with open APIs for AI agents and a public P&L dashboard._

> Two CEOs of very large prop firms told me this approach is very wrong and I'm not welcome in the industry. That tells me I'm doing something different.
> — Lou, Propr

**Host:** @B33Fbanks
**Date:** 2026-05-04
**Duration:** 30:09
**Tags:** perps, infrastructure, ecosystem
**Source:** https://www.youtube.com/watch?v=pN1DnQWFRoU

## Who's talking

- **B33Fbanks** (@B33Fbanks) _host_
- **Lou** — Propr _guest_

## Key moments

- **[0:07]** Lou's background: traditional finance to crypto founder
- **[2:39]** Banned from Bybit, fell in love with Hyperliquid
- **[4:10]** What prop firms do: evaluations, capital access, efficiency vs leverage
- **[5:11]** Transparency as moat: public pass rates, margins, revenue on dashboard
- **[8:12]** AI agent-first infrastructure: 33% of users are agents with funded accounts
- **[9:43]** Pass rates: 9.5% overall, 10.14% one-step, 7.69% two-step challenges
- **[22:50]** Open-sourced algorithm determines A-book vs B-book based on Sharpe ratio and consistency
- **[26:22]** Proper Points reward early users; token-only fundraising to align value

## Transcript

**[0:07] SPEAKER_00:** what's going on everybody super excited to be chatting with lou the founder of proper and ceo of xborg appreciate you coming on lou side note i love the raw vlogs you're doing documenting the grind of growing proper so before we dive into proper well can you tell us a little bit about your background and how you found your way to hyperliquid hypermeat is proud to be sponsored by silhouette the shielded layer on top of hyperliquid not only will you be able to obfuscate

**[0:38] SPEAKER_00:** your trades but you will be trading with some of the steepest hyperliquid feed discounts that are available awaken tax crypto taxes for crypto natives could not have submitted my taxes without the team at awaken awesome customer service and they are always improving their hyperliquid support get started with awaken today shout out to purposeful node for being our newest sponsor validator selection is in your hands which means who you stake with actually matters purposeful is part of the kinetic

**[1:08] SPEAKER_00:** active set they're aligned with the ecosystem supporting builders and even donate to in real life initiatives stake with purpose stake with purposeful nothing discussed on hypermeat is investment advice always do your research and make your own decisions i'm not responsible for any actions you take myself and my guests may hold positions in the protocols we talk about all right buddies let's get back to the show well background is in traditional finance um out of university i went

**[1:38] SPEAKER_00:** to the the large bank where i was doing risk uh so i was in you know basically just a quote doing risks in the lending department there was during covid so it was really interesting because of all the credit facilities you know kind of ironic but the crisis blew up and got bailed out by ubs and uh just after that but i was very junior at the time and then i joined uh roth charlin co uh

**[2:09] SPEAKER_00:** in zurich and in and that's where i've created basically the crypto division there and then fast forward to like 2022 just got very bored of uh threat fi and really sort of potential of crypto and so it just went all in and so i was um you know swissborg a pretty large actor today in europe brought me on as a ceo of export to run the gaming division which i've

**[2:39] SPEAKER_00:** run up to now and i'm a big purpose trader i actually have like my public hyperliquid address is quite well known out there but how i actually came to use hyperliquid pretty heavily is when i got banned from bybit and then i just i was using hyperliquid daily and then i kind of fell in love with the platform and then i was one of the largest airdrop recipients so

**[3:10] SPEAKER_00:** i think you know i i owe a lot back to hyperliquid so i just kind of stuck around and then as i dug deeper into because my background is threat fi so i understand like the edge that hyperliquid has over the opacity of cfd brokers and the overall like threat fi infra and i just really believe in the team and and now just super glad to be building on top of of hyperliquid holy cow man that's that's quite the story i did not expect you to be

**[3:40] SPEAKER_00:** name dropping like that that's that's pretty awesome an incredible background awesome story on the hyperliquid airdrop too does that mean you got a hyper as well or did you just opt for the tokens yeah yeah no i luckily assigned the right things and i opted in for the nft so that's super dope man let's dive right into proper so for people who might not be familiar especially like the more casual type users what exactly is a prop firm and how does proper

**[4:10] SPEAKER_00:** fit into that model yeah prop firms enable traders to trade with their own capital the way it works is you have evaluations that assess traders evaluations typically have a profit target and a drawdown limit if you pass this evaluation then you get access to the firm's capital and then you can trade with the the capital so you can purchase like a 50k accounts if you pass the evaluation then

**[4:41] SPEAKER_00:** you can trade with 50k uh it is specifically for um traders that don't have access to capital like let's say you're very good but you don't have access to more capital then that's i would say a much more efficient way to look at leverage because instead of let's say you only have 5k of available capital with a 50k account you can deploy 10 exercise and you know you don't have to go 10x levered you can just go 3x or 2x levered and

**[5:11] SPEAKER_00:** that's basically how it works now the model is super opaque there is no transparent actors overall it's a super scammy industry and that's the whole opportunity i saw when coming into this industry to not only build a platform in hyperliquid but also be super transparent about the operations of the firm you've mentioned me going on stream every day that's one of the things that i do is most of the founders are not known behind the large prop firms and i think traders

**[5:42] SPEAKER_00:** now deserve a much more transparent capital layer that they can trust and when you build on top of hyperliquid you have transparent execution you know exactly the the spreads the slippage that you that you have um we're also able to list a lot of assets um and be transparent about how we list assets and yeah we've got this transparency dashboard that lists everything that you need to know about our business like the pass

**[6:12] SPEAKER_00:** rate the revenue even our margin rates um we're pretty much going out there naked about our business operations awesome yeah no you kind of dove into a bunch of things i wanted to ask about so would you say then the main thing you were focusing when it comes to the prop is that you guys are being so transparent about how the all the inner workings work we use um a couple of things is one is like the ux of prop firms generally suck like when you use um threat

**[6:42] SPEAKER_00:** five products like uh interactive brokers or meta traders i think the ux of like when you when you're using a lot sizes it's just very complex and we're using perps and uh well -known crypto ui uh like crypto perps ui which is much better and then so that's like one point which makes us better vs the other prop firms my view is that perps is the best way to express delta on an asset

**[7:12] SPEAKER_00:** it's much more efficient than the other um other products whether that's options or just uh traditional futures contracts or swaps the other thing that's interesting is we are ai agent first like our stack is anyone can be plugged onto our stack um which is not today possible with platforms um and lastly is listening assets that people want to trade like the more exotic alcoins um

**[7:42] SPEAKER_00:** or with ap4 having the ability to have prediction markets talking about ai agents i did see that you guys are building out infrastructure to support that i'm sure there's going to be some people who deploy what they've been working on it seems to be the hot thing everybody's doing now yeah and you know the all of the prop firms are built on top of a few actors and and they are like meta traders dx trade and those folks don't have open apis that you

**[8:12] SPEAKER_00:** can tap into which means that none of the ai agents can today access uh funded accounts which is exactly what we what we built the platform for when when i thought of proper initial i was like i want to build this new operating system for firms what does it look like it has to be transparent and it has to be a a agent first and today we have like a third of our users that are agents uh that directly are plugged into our

**[8:42] SPEAKER_00:** system wow i was not expecting that too and you guys have been live now for what a couple weeks so you've got a pretty good sample size so far yeah 15 days to be accurate so still quite early but things are moving pretty fast awesome we got sidetracked there so talking about the evaluation before you actually unlock this founded account funded account can we can we talk about that like what percentage of these traders pass that evaluation yeah

**[9:13] SPEAKER_00:** it's it's pretty low uh industry standards are around 10 to 15 percent and our pass rate at this very moment is like latest data i have is 9 .5 percent so it's actually quite small my take on this is that proper we're building the best infrastructure for you to get the best like trade execution so that if you fail

**[9:43] SPEAKER_00:** the challenge it means that you're simply just not not good enough it's not because we're like trading against you which is what other platforms are doing with like manipulating sleep pages um changing the rules etc we would just want to be as fair as as possible now that makes sense if you could give someone advice for kind of advancing through this evaluation but not financial advice what would it be and we actually help you if you go on the terminal

**[10:14] SPEAKER_00:** you can go on the settings tab and you have one toggle that you can turn on which is the sizing guide and the sizing guide is telling you with some amber signs whether you're risking too much and today people approach the evaluations like almost like a lottery ticket where they would trade just like you would trade on a discretionary trading account but you have to understand that the daily drawdown is three

**[10:44] SPEAKER_00:** percent or five percent depending on the accounts and so you have to have very strict limits so typically what you need to factor in is the risk per trade um so typically you should not risk more than one percent of the rate or two percent per trade of your account otherwise you'll just blow up the account so you have to approach the evaluation from a risk perspective that each trade should have its own stop loss and the risk should be measured and again we do help you

**[11:14] SPEAKER_00:** so like you can when you set a tp or stop loss or when you put in an order we tell you how much risk you're taking on this trade and we help you to yeah take the the right risks the reason like the the thing is the people that lose i would much rather have them lose on an evaluation accounts than actual capital the cool thing about the prop from business is the risk is defined so people that lost they know what they lost it's not like

**[11:44] SPEAKER_00:** they're blowing up their own live training account yeah that makes sense for people who aren't really familiar there's two options there's a one step and a two -step account i think this is a big one too like how do traders think about choosing between them i would say it depends on your strength on your trading style the if you're if you've like if you've a well -structured traders with very strict risk parameters you

**[12:14] SPEAKER_00:** should take the the two step and if you're just getting started i'm sorry miss right there but like the the one step if you're like very structured but like two -step daily loss limit or two -step is 5 % daily loss limit, which means that you have more buffer. So if you're not accustomed to the prop firm business and you've never traded on the prop firm, I advise you to take the challenges which has the largest daily

**[12:44] SPEAKER_00:** loss limit. At the end of the day, it depends on your style as well, on whether you're a swing trader or you're doing scalping. If you're doing scalping, then you don't really care so much about the daily loss limit as in it's okay. But if you're doing swing trading, the 5 % is gonna be better for you. But if you know you're not the type of person to have good risk parameters, I would say in the first place, you shouldn't take a chance at an evaluation.

**[13:16] SPEAKER_00:** The chances is that you'll fail too quickly. But if you still wanna give it a try, you should opt in for the two -step challenge, which, you know, has more buffer on the daily loss limit. Yeah, so I'll be trying out the two -step account then for sure. It's a two -step thing, so it's like you still, the pass rates, we actually show you the pass rates for the different accounts, but it's... So what we know from data is the one -step account

**[13:45] SPEAKER_00:** has 10, well, we've got 10 % pass, 10 .14 % pass rate, two -step is 7 .69. So if you want, you know, the odds of a few passing one step today are higher. Now the sample size is quite limited. We only have 200 pay traders that try the platform. Well, you keep referring to like this dashboard. You call it the transparency dashboard where it's got all kinds of metrics. It's

**[14:15] SPEAKER_00:** another example of how you guys are trying to set the standard there, right, on transparency. I appreciated it when I was doing my research. It's the whole reason why I'm here in the first place, is I think, I mean, it's one of the reasons, but I think prop firms suck so much. They're not transparent. Their tech sucks equally, and we're trying to solve all angles at once. Like the tech angle, hyperliquid is a way in which we

**[14:45] SPEAKER_00:** fix this through the AI agent, and then it's transparency. We have to embody this from day one, and I also understand this industry's super, super, super, competitive and so to me i'm like what can i do that others can't do and i think transparency is a moat because i'm willing to share the our margin rates i'm willing to share everything about a business there is nothing i can't i can't share to the ex except or

**[15:15] SPEAKER_00:** how we how we intercept some um attack vectors on on the on the app the rest i'm 100 open to everything and i know a lot of people like there's basically no one doing what we do because they're just not they don't they don't have the crypto ethos and that makes me comfortable about our ability to gain some market share out there today it's clearly something that a lot of people

**[15:46] SPEAKER_00:** don't know about but it's a lot of people don't know about but it's a lot of people don't mention i actually had in the last week i had two ceos of very large prop firms tell me uh that this approach is very wrong and that i'm basically not welcome in the industry so that tells me that i'm doing something that's different and that's exactly what i'm after let's dive into some of this vocabulary when it comes to prop trading so you used equity -based drawdown instead of balance -based what does that mean exactly yeah so your balance

**[16:16] SPEAKER_00:** your equity is what factor like what is um is basically what what's in your account but it's not factoring into the the upnl so your your unreal sp now sorry so the unreal spnl is not going to be in your equity but it's going to be in your in your balance if if you want to know like equity specifically is the balance plus or minus the unrealized pnl so you like

**[16:47] SPEAKER_00:** the the pn that the trades that you haven't closed will sit in your equity uh sorry in your balance and equity is going to be the actual um like what's locked into your into your account it's super important to understand this because uh how we compute the daily loss limits is equity based which means that if you have ongoing trades then

**[17:17] SPEAKER_00:** uh that can go against you um because like the day loss limit let's say you were long btc overnight and then btc you know uh crash well like you know went down overnight then that's going to be counted as in the loss and that's uh you know something you have to take into account some other firms do balance based we purposefully did equity based mostly as a risk management framework

**[17:48] SPEAKER_00:** and we'll likely to shift this back to balance in i would say two three weeks from now well you kind of talked about that daily loss reset do you see people using methods to where they they make sure that they never leave a trade open towards the end of the day when that timer goes off yeah we actually uh so we take the the snapshots at midnight utc yeah so we take the snapshots at midnight utc there we go so we have two months at so we've got a bunch of folks that

**[18:18] SPEAKER_00:** just wake up at you know five minutes before midnight UCC to just close the trade and then they would just wake up or like reanalyze the markets to take on a different trade because they want to make sure that the equities is you know you close your trade so your equity is reflected correctly what I want to say is that this is going to change in the next two weeks

**[18:48] SPEAKER_00:** I would say two to three weeks that was a mainly a risk management measure and that's something we'll likely implement breakout like one of the prop firms I respect the most they are doing balance based and will likely adapt to their model in the next few days let's talk about another phrase that you guys use so what exactly is a breach like what triggers it so you have the our two

**[19:18] SPEAKER_00:** rules are very simple is one the drawdown limit and then the daily loss and that's all you have to respect within the account rules and then we have some other rules which are more around exploits or trying to abuse the system so for example if you do what we refer to as account cycling so if you're just trying to gamble basically if you treat if you treat an account as a lottery ticket and you do this over time on

**[19:49] SPEAKER_00:** multiple accounts our system will flag you and and that will be counted as a breach but overall we're very loose on on our rules and just like breakout we only have two rules which are only you know drawdown limits and well the max showdown and the daily drawdown limit it's just to kind of hammer the point home if there's one thing that a new trader like needs to understand to make sure that they don't you know make sure that they don't you know make sure that they don't you know make sure that they don't i guess blow the account you know treat it like a lottery ticket

**[20:19] SPEAKER_00:** would you say that the number one thing is risk management and just setting those parameters or yeah overall in trading it's uh you you have to take a risk approach um like every trade needs its own invalidation and you should only be you'll never pass you might be lucky and like an evaluation but you'll never keep your funded accounts if

**[20:49] SPEAKER_00:** you're not taking very strict risk management measures um and the ones that win over time are the best risk managers and that's true in i guess true in in prop trading but it's also true like um also in in in live training yeah just in general too awesome so let's talk about how proper is earning revenue can you break that down for us sure uh we're actually in a full disclosure we actually have the our

**[21:19] SPEAKER_00:** life p l on the transparency dashboard so you can actually see um the revenue flows uh but the so how it works is we make the most today the most amount of money from evolution fees so it's people trying to take well taking a challenge so we earn from this like people when people purchase a 50k account or 25k account we earn from this um and then we have a lot of people who are trying to take well taking a challenge so we earn from this like people when people purchase a 50k account or 25k account we earn from this then we earn from the profit that's made from the here i'm

**[21:49] SPEAKER_00:** going to use a specific term but a book traders on our platform um i'm not sure if we want to go into this it might take some time but what we basically like how platforms operate overall is when you're funding a trader you have two things you have b book and hey book b book means that you don't uh you keep the trade internally centralized uh and a book means that you deploy the the real

**[22:19] SPEAKER_00:** capital uh in our case we deploy on hyperliquid when it's a booked but when it's b booked it's kept uh internal but how we earn money today is on evaluation fees and profit split from a book traders okay that's kind of got me curious though how do you determine who gets their their trades deployed on a book versus b book how we how we treat this is we have a first we have we're

**[22:50] SPEAKER_00:** very transparent about the process we are the only firm out there that i know of that is open sourcing the algorithm that treats you between an a book traders or b book trader and we might link in the in the video there we we actually show you also on the platform how you're treated and how we do it specifically like what's the algorithm is it's revolving around the ability of the platform to be able to treat you as an a book trader and how we do it specifically like what's the algorithm is it's revolving around the ability of a trader to be consistent over time under specific market

**[23:20] SPEAKER_00:** regimes so it's super easy to be super performance in an uptrend let's say in october november 2024 everyone was a genius on the market but our algorithm is specifically specifically looks at traders that are consistent across different market regimes and the data that you that we look at is the shop ratio what's

**[23:51] SPEAKER_00:** the expectancy per trade and other more sophisticated ways to look at like the ability it's basically it boils down to the ability to dissect who is likely to make money in the future and the sharp ratio is you know sharp ratio being the the expected return per units of risks or volatility that you're taking is is one of the best measures out there like a trader that has a shop of two to three over

**[24:21] SPEAKER_00:** like a year is typically a very good a very good trader and you obviously look at other things like what's the max drawdown of the accounts but these are rule sets that are baked into the account from from from day one awesome yeah once again it sounds like you're you're offering something that these traditional firms wouldn't tell you that's pretty cool so if i'm a a new trader hearing about this for the first time why would i choose proper over just trading with my own

**[24:52] SPEAKER_00:** capital one is instead of you know let's say you have 10k of capital if you want to generate money quickly or like amplify your return today you can use leverage but the issue with leverage is your you're tied to specific risks and we we saw it with 1010 for example where sometimes you have liquidity

**[25:22] SPEAKER_00:** vacuum so you have adls and you're you know you can lose everything so to me prop firms is a way to amplify your capital and to take a very set amount of risk you know exactly what you're losing so if you blow up you know exactly how much you're losing and it also just trains you so to me the the short answer is amplifying your capital like access to more capital is always better obviously

**[25:52] SPEAKER_00:** if you're good and then having very defined amount of money that you can lose and there's also limited counterparty risks in in the sense that we you know we are the ones that are deploying on hyperliquid and you're not you're not the person that is taking like the defy risks directly let's talk about some incentives it's proper points are live so not only will profitable funded traders be getting paid out but they're also going to be

**[26:22] SPEAKER_00:** stacking these points do you want to talk about any details yeah um a big thing i'm after is uh what i understand is for me to win in this industry is i have to have the best tech i have to be the most transparent and i have to be the most aligned with the users that's also why i'm streaming every day and like you see me very often on discord at almost every hour of the day responding to customers and on user alignments and i intend to give

**[26:53] SPEAKER_00:** the value back to the users and for example today we're raising capital it will announce the closing of the round very soon and we're only raising with a token and not raising with equity to concentrate the value that we create around the token and for us this point program is a way in which we reward early platform users so for example it was still super early in on the journey but the people

**[27:23] SPEAKER_00:** that helped us test the product that did the free trials because you can try the platform for free very early on that tried to break the infrastructure break the product it really helps us build the best product out there and i want to reward them so for me for example if i test something i'm going to be able to get the that's what this is doing i'm going to be able to get the value that they are getting out from this point at the end of the way and i'm also So we have this point program and the point program to me, it's a single value that at the end of the day for us reflects how much value you brought to the, to the protocol. Well,

**[27:55] SPEAKER_00:** was there anything else you wanted the hyperliquid community to know about proper? I think the big thing is risk management is, is whenever you discuss with a prop firms, you have to assume that most of those firms are, are pretty shady. And one angle that we focus on the most is, is risk management. And that's a pretty big angle, but risk management is what will make

**[28:25] SPEAKER_00:** us a lasting business. And again, this is super transparent. So the transparency dashboard, for example, you can, you can check the different risks that we highlight. And for example, we have the liquidity risks that is exactly telling us how much, like what's the equity that we have available and, and what's the expected expectancy of, of payouts to make sure that we are, we can honor payouts and run the

**[28:55] SPEAKER_00:** business properly. So just important to, to tell the hyperliquid community that we're running the prop firm business from a risk perspective, which helps us guaranteeing, we guaranteeing liquidity and just the best conditions for traders. Awesome. When you go to a restaurant, what's your favorite cut of meat? Wait, how's this? What's this? The, is

**[29:25] SPEAKER_00:** it the Pina something? What's the, Picanha? Picanha. Yeah, there we go. Picanha is just so good. Oh yeah. Picanha is pretty awesome. How do you like your, your steak cooked? I would say medium rare is what I go for. Fantastic. That's the way I get it done too. Awesome. Well, thanks so much Lou for spending some time with me. Make sure you guys give Lou a follow. I'll tag him down

**[29:55] SPEAKER_00:** below and make sure you set those notifications on for everything that proper is doing. Thanks again, Lou. No, thanks so much for your time.
