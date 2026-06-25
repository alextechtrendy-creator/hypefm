# Tokenized US stocks on Hyperliquid: real ownership, dividends, and DeFi composability

_Denari's dShares bring actual stock ownership on-chain with full corporate actions, not wrapped tokens._

**Host:** @rekt_gang
**Date:** 2026-06-23
**Duration:** 32:40
**Tags:** perps, ecosystem, trading
**Source:** https://x.com/i/spaces/1mGPaamnZBbJN

## Who's talking

- **Rekt Gang** (@rekt_gang) _host_
- **Anna B. Wroblewska** (@annabelleacta) _guest_

## Key moments

- **[7:31]** Zerk introduces Denari and tokenized equities topic
- **[8:02]** Anna explains Denari's custodial model and regulatory approach
- **[10:34]** Denari's history since 2021 across multiple chains
- **[13:05]** 18-month SEC and FINRA approval process for US broker-dealer
- **[19:08]** dShares pass through dividends, splits, mergers—everything
- **[23:13]** Choice between KYC wallets or permissionless DeFi trading
- **[27:16]** Roadmap: more composability, international markets, US access
- **[30:48]** Korean stocks as top community request, high priority

## Transcript

**[3:42] SPEAKER_00:** GM, GM, how are you doing? GM, can you hear me? I can hear you. How's it going? I'm doing great. How are you doing? I'm good. Very good. We shall get started shortly. Let me just amplify the space real quick,

**[4:12] SPEAKER_00:** and we'll get started in a couple of minutes. Seems it's a little wonky today. I don't know if you had any technical difficulties joining in. It might completely be me. I'm having... Yeah, I don't know if there's connection issues. Very

**[4:43] SPEAKER_00:** red day in the markets today, so a great time to have spaces, learn more. I see some little crying emojis out there. Definitely a good time for joining the rec gang. Do you want to try that? Let's see if those internet connection issues have been... Resolved, if you want to say like a sentence. Oh, Hyperliquid

**[5:28] SPEAKER_00:** Hub, I got to follow you back. There we go. Anna, are you there? A little technical. Oh, the old trick here of leaving and coming back to the space. That always does the charm. So

**[6:01] SPEAKER_00:** today's going to be a really fun space. I'm very excited to learn about Denari. Anna's going to come back. She's going to... Oh, I hope it's going to work. Please tell me this is working now. Oh, now I hear you well. Amazing. Okay. Phew. Sorry about that. I'm in one of the biggest cities in the world, and yet I cannot seem to make the internet work. So thank you. You found the secret trick to all these spaces, which is leaving and

**[6:31] SPEAKER_00:** coming back. It's my most used technical support strategy. Have you tried on and off? Yeah. It's always the go -to, and thankfully, it works much of the time. All right. So usually, I like to amplify the spaces, but I know you have 30 minutes, so I want to make most of the time. The spaces are recorded afterwards. They're archived. They're posted on YouTube. We do the timestamps.

**[7:01] SPEAKER_00:** We put the overlays. Everything's done. So let's just kick it off, and we'll have all the goodies afterwards in terms of amplifying. The content as well. Is that good with you? Sounds good. All right. Let's do this. So I'm Zerk, co -founder of RecGang. We run a validator on Hyperliquid, as well as a community. We love to do educational series on builders of Hyperliquid. And today, we have the privilege, the honor, the prestige of hosting Anna

**[7:31] SPEAKER_00:** from Denari. She's going to be talking to us about stocks on Hyperliquid, or I guess tokenized equities as a whole. I'm very, very interested in this topic. Because we've seen it on the timeline often. It's been like a booming space, so really timely to have you. Thank you so much for taking the time today. Yeah. Thank you. I really appreciate it. Awesome. Awesome. So let's get to some introductions. So Anna, maybe you can tell us what you do for the Denari team.

**[8:02] SPEAKER_00:** And then we'll go into what is Denari and some of the questions kind of around tokenized equities and crypto space as a whole. Yeah. That's good. So I'm Anna. I'm our chief business officer. I came to Denari out of a combination of traditional finance and a bit of DeFi. And what we do, so Denari is a tokenization platform. So we've developed kind of an end -to -end technology for tokenization and distribution. As

**[8:34] SPEAKER_00:** the subject of this conversation implies, we have focused on what are called Reg NMS shares. So publicly traded securities from the US. And Denari pioneered what the SEC now calls the custodial model of tokenization. And what that means is that the token is a mirror of the security. So if you're a token holder, you get the rights and benefits of owning a security. So in practical terms, that's like things like a

**[9:04] SPEAKER_00:** claim, an ownership claim on backing securities. You have cash dividends and all the funky corporate actions that come from owning stocks. So we have historically, and one of the reasons why Hyperliquid is really exciting to us is because we have historically distributed these tokens through regulated channels. So we have an API -based model where you can think of it like an on -chain brokerage model where

**[9:34] SPEAKER_00:** our distribution partners are companies like Neobank. Fintechs, brokerage applications, some centralized exchanges, and then kind of so on down the line. And the bulk of that has really been in the fintech space. So these are regulated distributors around the world. We're in about 85 jurisdictions right now. And we're very excited to show the strength and flexibility of our specific approach to

**[10:04] SPEAKER_00:** tokenization and its use cases in DeFi. Yeah, it's very unique. I feel we're so used to having wrapped assets or wrapped stocks. You get the exposure to the price action, but you're not actually owning the share. So I feel like here is really a huge differentiator for what you guys have built. But before we get into the architecture of these D shares, I think is what you guys call them, I wanted to talk about Denari as a company

**[10:34] SPEAKER_00:** or as a group. So you guys have been around the space. This is not like your first rodeo. I see you have many, many equities or assets on Avalanche and I think all these other chains. So new to hyperliquid, if we can use that term, but not new to the ecosystem. Yeah, correct. So Denari has been around since 2021. And we've actually spent a lot of time building this technology. It's kind of complicated to do it in the way that we've

**[11:04] SPEAKER_00:** done it because kind of like I mentioned before, these are really weird. You just have all kinds of edge cases all the time. And we had to build a system that can really accommodate all of those edge cases. And I mean, it's all kinds of stuff. It's like, of course, you have, you know, stock splits and reverse splits. You have ticker changes. You have mergers. You have delistings and relistings. You have dividends get paid out and then they get recalled. And then another dividend gets paid out because it was an error. There's

**[11:35] SPEAKER_00:** all kinds of weird stuff that happens. And so we've been building this technology since 2021. And we are, as you alluded to, on multiple chains. Of course, ETH mainnet, Arbitrum base, Avalanche, Plume, and now very excited to be on hyperliquid as well. And this is our first real DeFi deployment. And we can kind of get into what that means. But the idea is that, you know, this is a...

**[12:05] SPEAKER_00:** DeShares are a type of token. It's like a way of owning a stock that is incredibly flexible. Like you can have the full, you know, stock kind of almost blockchain -based traditional style stock ownership experience. Or you can kind of flexibly move in and out of these permissionless marketplaces, which I think is really exciting innovation. Yeah, I feel the future is happening right now. So lots of experience in terms of the... You

**[12:35] SPEAKER_00:** know, tokenizing equities since 2021. And I guess you must have all the licenses. And it seems like, you know, with the regulations around U .S. equities, it must be pretty complex to build something like this out. You can't just spin it in a month. You got to fill out lots of paperwork and go through the hoops in order to finally be able to offer this to the Web3 community. Yeah. Like the... So the process of... So we have a subsidiary

**[13:05] SPEAKER_00:** broker -dealer in the United States. And the process of walking FINRA and the SEC through what we were trying to do... I mean, it was, you know, 18 months, two years of just kind of creating a comfort level, right? And, you know, already last year, you know, our broker -dealer kind of passed through all the registrations. And, you know, we kind of started gearing up for, you know, being able to offer this in the U .S. I mean, as everybody here knows... All of the stuff

**[13:35] SPEAKER_00:** around tokenization is happening outside of the U .S. And so, you know, keep an eye out because the U .S. is coming very soon. There's a lot of noise around it and a lot of announcements. But operationalizing will happen in very short order here. So we're really, really excited about that. Nice. And quick, you know, little sidebar. Do you think the Clarity Act is going to get signed? Before they go to recess and

**[14:06] SPEAKER_00:** take their long summer break? I mean, I hope so. There's been a lot of, like, hurry up and wait with that, as we all know. Like, it would be great. I think it's good for the whole industry to have, not to, like... No pun intended, but it's good for the whole industry to have more clarity around these things. It certainly brings a comfort level to institutional partners. When there's, you know, clear rules of the game to play by. But,

**[14:36] SPEAKER_00:** you know, thankfully, we spent so long building something that is designed for existing securities regulations that, you know, we're excited. If it passes, it certainly makes a lot of communications and other things like that easier. But we're good. We're good either way. But let's hope so, so that we can all move on. You're ready for either or outcome. We're ready for both, yeah. All right. Let's get into these D shares because I think that's a differentiator

**[15:07] SPEAKER_00:** for you all. I think I mentioned this is very unique in terms of having two options here. So walk me through, like, how you guys decided to design something like this versus what we see most often, which is just like a wrapped stock that you can't, you know, you're not really owning the share here. Yeah. So there's kind of multiple parts to this. And as I mentioned, the design was really architected to function with U .S. markets and existing

**[15:37] SPEAKER_00:** U .S. regulation. And what it essentially means, and not to get kind of too far into the weeds, but there's multiple models of tokenization, right? You alluded to the synthetic model, which is a price exposure. There's a primary issuance model where there is no traditional side security. The token is the security. And then there's this custodial model. So Denari is a third -party issuer. We can take any security, really,

**[16:07] SPEAKER_00:** and create a token version of that. And there's some nuance to this, and I'll get into some of it, but, you know, between U .S. international markets and then, you know, international KYC markets and DeFi. But again, this is the flexibility of the token, right? So the idea is really that the token is the twin of the security. So what happens to the security happens to the token and vice versa. In, you know, in the kind of U .S. regulatory conception, the

**[16:37] SPEAKER_00:** token is not distinct from the security. So, you know, if you're a U .S. customer and you own dShares, there's like no difference at all, right, between the two. Once you get into international markets, it does get a little bit more complicated. So we launched this under the previous administration. And there was a lot of concern about things like voting rights. And even a lot of issuers today have concerns about that, right? Who owns these voting rights? So one thing that we do not

**[17:08] SPEAKER_00:** pass through to our international customers is voting rights. We are very much hoping that that will change in the near future, so keep you posted. But that's one thing that we can't confer. And, you know, some of the operational model is also a little bit different. Just to provide us the flexibility. There's a lot of flexibility to serve customers in multiple different jurisdictions. But importantly, that ability to say independent of Denarii. So like one of the things that I, you know, I wouldn't want as a

**[17:38] SPEAKER_00:** customer or an investor is to be like, cool, my stock portfolio is backed by the full faith and credit of like some random company. Like I don't, it doesn't like make me feel super comfortable. I would like to know that there is some rules in place, right? There is some legal structure that will protect me in the event that, you know, something bad happens, right? And so importantly for international customers, that ability to, and I won't get into the details because I

**[18:08] SPEAKER_00:** don't think most people care about this. But the ability to say I have a claim that is a legally and contractually protected claim is I think really important. And, you know, structuring this in a way that aligns with regulatory frameworks. Minimizes or in our case eliminates the discretionary ability to say, actually, no, we're not going to pay you. I think is really important. No, I agree.

**[18:38] SPEAKER_00:** It's very critical. I don't think you should, you know, glaze over that because the shares aren't held in somebody's basement for a pile of papers, right? Like this is, you know, there's a whole structure here. And you mentioned that every token is basically a reflection of the share. You get pretty much everything except perhaps the voting rights for the international customers or holders. Is that correct? But

**[19:08] SPEAKER_00:** if there are dividends, if there's, you know, stock splits and all these things, all that is taken into consideration. Yeah. Am I correct in that assessment? Yeah, it all passes through to the token. So if you, you know, and look, a lot of people are buying stocks because they want to. You know, buy and sell and they want to do trading activities. But, you know, it's also nice to accumulate dividends if you're sitting on something for a while. So the ability to get cash dividends, the ability to know that whatever is happening, again, to the underlying security, if

**[19:39] SPEAKER_00:** there's a merger, if there's a stock split, if there's, you know, we had, I mean, there's all kinds of weird things happen. But, like, you just want to know that that's going to propagate. And you don't have to now revalue or, you know, try to undervalue. You don't have to understand what's happening to your token. Your token is just moving on in life, mirroring that security that you're invested in. Yeah, that's great. So really, I think people can have most confidence, right, whenever they buy a D share. It's

**[20:11] SPEAKER_00:** something that has a structure. Would you say it's the closest thing to real stock in this ecosystem, in this space? Is there anybody building something that is? Yeah. Close to that? Or you guys are definitely on the frontier here? We are. I can say with confidence we are on the frontier. I'm sure other people are working on it, but I don't know of a product in the market where you can have all of that. I don't want to, you know, put

**[20:41] SPEAKER_00:** words in your mouth, but let's, you know, there's always competition between different offerings, different products, right? And on Solana, they have some versions of these tokenized backpacks. There's Xstocks, Ondo as well. So could you, you know, position Denari in terms of how different or, I guess, what are the pros of Denari? We don't have to go into the cons of the others, but

**[21:11] SPEAKER_00:** however you want to frame that without badmouthing the others. Or if you want to, I mean, this is a free space. We love this type of content. A little spiciness. So we... I think you put it really well, right? If you want to own a security and you want to own it on a blockchain, Denari is the best way to do that. And it's because you have all of the benefits of owning a security. So, you know, your cash

**[21:42] SPEAKER_00:** dividends, your corporate actions, you have the knowledge that you are not relying on Denari to pay you out should something happen. You can be confident that that will happen for regulatory and, you know, legal protections around it. That zero discretion kind of approach. And you can always transact, if you need to, with Denari at MBBO. Now, this is a little

**[22:12] SPEAKER_00:** bit different to, you know, the secondary markets that we're standing up. And it's very much a preference thing. But if you want to be confident that you're a part of it. So you want to put on, like, at size, right? You want to put on a trade at size. And you want to make sure that you're executing at the national best bid offer. You have that option, right? So, essentially, you get all of the benefits of interacting with the traditional market plus all the flexibility of interacting in a permissionless

**[22:42] SPEAKER_00:** setting. You don't have to choose one or the other. And I think that's what makes it really powerful. Is you don't... You're not forced to, like, say, okay. I'm going to give up the flexibility of DeFi and blockchain -based systems so that I can have, you know, these kind of protections and benefits. And you don't have to say, I'm going to now sacrifice all the protections and benefits because I want to do stuff in DeFi. I think it's very, very powerful that you can have both. And that's how dShares are designed.

**[23:13] SPEAKER_00:** Now, I don't know how much detail you want to get into on this. But once, you know, once a dShare... Oh, yeah. Yeah. That's super interesting to me to understand both sides of the coin, right? Like, you can have a KYC wallet with all the classic stock perks or advantages. Or you can do what us degens and anons do, which is basically traded on, you know, non -KYC order

**[23:43] SPEAKER_00:** book decks, right? And perhaps do some composable things with it afterwards in DeFi. Yeah. And that, I mean, like, look, that's, like, one of the coolest things about crypto, right? Is, like, there's all this innovation that happens. And isn't it cool that you can now apply that to stocks, right? A lot of people are sitting on stock portfolios that do absolutely nothing. You know, they buy, hold, and sell. Like, those are your options, right? Yeah, you can get margin. But that's, like, kind of it. So

**[24:15] SPEAKER_00:** we're kind of trying to move this in two directions. One, we're trying to bring all that technological innovation and bring it to normal people who are, you know, not so fluent. And maybe haven't, you know, don't really maybe necessarily know, like, all the steps, right? How do I set up a wallet? Like, how do I find hyperliquid? Like, there's a lot of people in the world that are, this is not their jam, right? But they would really benefit from us deploying that technology for

**[24:45] SPEAKER_00:** them. Now, it also goes the other direction, right? So you're already, you know, deep in the hyperliquid community. You're already doing all kinds of stuff in crypto. Wouldn't it be cool to also be able to do that with traditional securities? Whether it's U .S. stocks or stocks from other countries or, you know, eventually other instruments. Wouldn't that be great if you could do all of those things? Now, there is, like, there are aspects of

**[25:15] SPEAKER_00:** this that I don't know about. There are things that do get somewhat complicated if you want to get into the weeds. So, you know, for example, the SpaceX spot market that we launched on HyperCore, it's a wrapped token, right? Because rebasing tokens, you know, everybody here knows all this stuff, right? So you have to kind of, like, unwrap the token again later if you want to kind of sit and hold. But you have that optionality. And I think that piece is really important. The optionality piece, I think, is, like, the biggest. For me, it's

**[25:45] SPEAKER_00:** the biggest selling point. Like, I hold a D share. I can do whatever I want. I can buy it and hold it and it can sit in a KYC wallet and, you know, maybe earn some yield in some kind of walled garden setting or just accumulate cash dividends. Or I can take it out of that walled garden and go do stuff with it. And I think that part's really awesome. Yeah. And there are enough SpaceX shares, right? If you do choose to unwrap and put it in the KYC wallet. That, you know, it's going to be there,

**[26:16] SPEAKER_00:** right? It's fully backed. Well, yeah. I mean, and that's, I mean, I think that's the piece that underpins all of this is that there's not, it's not some amorphous, mysterious situation that's happening in the background. We are regulated very heavily. In all the jurisdictions that we operate in, that Denari has operations, we are heavily regulated. And that still means something, right? And you know that your token

**[26:45] SPEAKER_00:** is, there's actually a security sitting out there. And if everything, you know, kind of goes disastrously wrong or, you know, all hell breaks loose or whatever, you still have a claim that is protected, right? You can go and you can get that stock or you can get cash. Very cool. So moving on. Because I know time is short. I'm wondering what the focus is for

**[27:16] SPEAKER_00:** Denari right now. Are you guys working on deploying more D shares on Hypercore or improving the composability of D shares through some DeFi or adding margin? What's the focus right now? That's a great question. So it's a little bit of all of the above. I think a lot of the story around tokenized stocks over the past several months has really been about tokenization. It's about access, right? So giving people access to U .S. capital markets. I

**[27:47] SPEAKER_00:** think that's sort of just, it's not even really step one. It's kind of like step 0 .5, right? There's so much more that you can do. And our overriding mission is to help people do more with stocks. So that definitely means more composability in DeFi. It definitely means bringing more utility to customers who are operating in, you know, kind of remote areas. It definitely means making this accessible to regular regulated walled garden type channels. It absolutely

**[28:17] SPEAKER_00:** means making this accessible to American consumers who haven't really been able to participate in all of this thus far. And it ultimately means really showing that tokenization and in particular the D share standard can function from all the way from the most heavily regulated, you know, publicized market. Public markets setting to the most permissionless

**[28:47] SPEAKER_00:** DeFi setting and everything in between. And, you know, there's a huge power to that and to bringing finance on chain in that way. I thought you were going to say to the Wild West. I mean. But yes, so very cool. I'm guessing there's still lots of work to be done. I was wondering as well. If you had any call to actions in terms of how the community can get involved. You have the D shares

**[29:17] SPEAKER_00:** right now for SpaceX D on HyperCorp. Anything else they should be doing? I guess they should give you a follow. Give Denari a follow. Guys are probably going to cook some announcements. Yeah. So how can the community get involved and what can we expect in the next few months? Yeah. So would love obviously, you know, follows and all that is like very helpful and wonderful to us. I would actually also really love to hear from the community. Like what spot

**[29:48] SPEAKER_00:** markets do you want? How can we improve, you know, your experience with tokenized equities on Hyperliquid? Feedback is really, really helpful. You know, we have ideas about, you know, what comes next. And I would just love to get, I would love to get actual people telling me what they want next. Because like I said, we have ideas. But it's also really, really helpful and great to get actual community feedback and participation so that we can make, you know, it helps

**[30:18] SPEAKER_00:** everybody. Right. You know, we want to launch markets that people want and we want to make, you know, be a good contributor to the ecosystem. So. Love it. Love it. And yeah, I'll give feedback. I'll, you know, I'll DM Kayla in terms of what people are asking for. Are you guys limited to U .S. equities and markets or international? Anything goes? Sorry. I missed you for like one second. It was working so well. And then I lost you for a second. Yeah. I was just wondering if we

**[30:48] SPEAKER_00:** can get like Korean stocks or, you know. That is. Please stay tuned. That is my number one biggest request from pretty much everyone I talk to. So. It's hard to get those shares, right? If you're in the U .S. or Canada or wherever, it's quite easy. But. You know. Everybody. Everybody wants access to the Korean market. Please stay tuned. Working very hard on this. High priority. High priority. Very cool. Any

**[31:18] SPEAKER_00:** closing words? I know we're at half an hour and I like to be on time. Yeah. No, just thank you. I really appreciate the time, opportunity to chat with you. Like I said, we'd love, we'd love to hear feedback from people about, you know, what's, what's interesting. You know, how it's been so far with, you know, our space XD market. And yeah, just want to make sure that we're contributing positively. Here going forward. Yeah, absolutely. Thank you for bringing this to Hyperliquid. Thank you for tokenizing equities on chain. I think it's a great

**[31:48] SPEAKER_00:** initiative and there's so much to be built. So best of luck to y 'all. I hope we can have another one of these spaces, maybe in six months, one year when you have like, you know, hundreds and hundreds of Korean and Hong Kong and U .S. Stocks equities. And we get to trade them all in huge volume on Hypercore. That'd be cool. Would love that. Thank you. Thanks so much. I really appreciate this guys. Thanks for the, thanks for the time. No, thank you. Appreciate your time. Thanks to the audience for tuning in. And as I said,

**[32:19] SPEAKER_00:** the space is recorded. We're going to put it on YouTube. We're going to timestamp it and you'll be able to listen it at a pace that you enjoy. So thanks everybody. And enjoy the rest of your day. Cheers guys. Thank you.
