import requests
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from discord import Game
import random
from discord import server

Client = discord.Client()
client = commands.Bot(command_prefix = "/")



amountofservers = str(client.servers)

serversindiscord = ("I am in ", amountofservers, " servers!")




@client.event
async def on_ready():
    coolo = len(client.servers)
    print("Bot is ready!")
    for i in range(1,999999999999999999999999):
        await client.change_presence(game=discord.Game(name=f"/help || {coolo} servers! http://bit.do/helperbotdiscord", url="https://www.twitch.tv/itscoolo2", type=1))
        
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current Servers:")
        for server in client.servers:
            coolo = len(client.servers)
            await client.change_presence(game=discord.Game(name=f"/help || {coolo} servers! http://bit.do/helperbotdiscord", url="https://www.twitch.tv/itscoolo2", type=1))
            print(server.name)
        coolo = len(client.servers)
        await asyncio.sleep(600)
        

client.loop.create_task(list_servers())

@client.event
async def on_member_join(member):
    server = member.server.default_channel
    fmt = 'Welcome to the {1.name} Discord server, {0.mention}, please read the rules and enjoy your stay.'
    await client.send_message(message.channel, "hi")

choice = ("Tails", "Heads")
dice = ("123456")

version = "v2.3.5"

@client.event
async def on_message(message):
    if message.content.upper().startswith("/PINGME"):
        await client.delete_message(message)
        userID = message.author.id
        await client.send_message(message.channel, ":white_check_mark: <@%s> Pinged! \U0001F44D" % (userID))
    if message.content.upper().startswith("/YES"):
        await client.send_message(message.channel, ":negative_squared_cross_mark: No")
    if message.content.upper().startswith("/INFO"):
        em = discord.Embed(title=':white_check_mark: Info', description=f"Created by Coolo2 \n\nCreated On The **12th of May 2018**\n\nHaving constant updates.\n\n**{version} Change Log:**\n\n-**/kys** command improved!\n\n\n*Need more help?*\n\nDo /ask [your question] to ask a moderator a question!\n\nor...\n\n ***Join:*** \n\nHelper Bot Discord: https://discord.gg/QBzsbmh      \n\n**{version}**", colour=0xff9400)
        em.set_author(name='HelperBot', icon_url=client.user.default_avatar_url)
        await client.send_message(message.channel, embed=em)
        await client.send_message(message.author, "Make sure to join Helper Bot Discord for giveways, bot chat, support, news and more: https://discord.gg/QBzsbmh")
        await client.delete_message(message)
    if message.content.upper().startswith("/AMICOOLO"):
        if message.author.id =="368071242189897728":
            await client.send_message(message.channel, ":white_check_mark: Yes, you are Coolo!")
        else:
            await client.send_message(message.channel, ":negative_squared_cross_mark: No, you are not Coolo")
    if message.content.upper().startswith("/AMIADMIN"):
        if "439860652010635264" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, ":white_check_mark: Yes, you are admin!")
        else:
            await client.send_message(message.channel, ":negative_squared_cross_mark: No, you are not admin.")
    if message.content.upper().startswith("/HELP"):
        lolomg = await client.send_message(message.channel, ":white_check_mark: Sending Help...")
        em = discord.Embed(title="Bot Help", description=f'**/pingme** - /pingme - pings you with an @. \n\n**/help** - /help - gives help on the bot. \n\n**/amicoolo** - /amicoolo - shows wheather you are coolo. \n\n**/amiadmin** - /amiadmin - shows if you are admin \n\n**/info** - /info - shows info on the bot. \n\n**/say** - /say [your message] - says what you say.\n\n**/flip** - /flip - Flips a coin\n\n**/discordpythonversionversion** - /discordpythonversion - shows discord version.\n\n**/servers** - /servers - shows how many servers the bot is in.\n\n**/roll** - /roll - rolls dice.\n\n**/dm** - /dm @[the user] [the message you want to send] - DMs the user with  the message you wrote.\n\n**/members** - /members - DMs you all members in the server that the message is sent in. Sends them 5 at a time (Warning: cloggs up DM with the bot for a short while.)\n\n**/spamme** - /spamme [Spam message] - **Warning:** Spams you in DMs\n\n**/embed **- /embed [top title(no spaces)] [middle title(no spaces)] [message] - embeds the message you wrote.\n\n**/emoji emoji**- /emoji emoji [your emoji](can do as many emojis as you want) - Display emoji(s).\n\n**/animate** - /animate - Display a random animation(**Warning:** Can Lag).\n\n**/emoji type** - /emoji type - say the message with emojis! (Put a space in between each letter)\n\n**/purge** - /purge [amount] - mass delete messages\n\n**/poll** - /poll [your question] - create a poll!\n\n**/calculate** - /calculate [Math question] - calculates a math question! (cant use decimals)\n\n**/rps** - /rps [rock, paper or scissors] - plays rock paper scissors\n\n**/warn** - /warn @[The username] [Reason] - warn users who break a rule!\n\n\n**{version}**', colour=0xff9400)
        em.set_author(name='HelperBot', icon_url=client.user.default_avatar_url)
        await client.send_message(message.channel, embed=em)
        em = discord.Embed(title="Bot Help", description=f'\n\n**/userinfo** - /userinfo @[The User] - Sends Info On The User In DM.\n\n**/reportbugs** - /reportbugs [The Bug] - Report A Bug To A Moderator!\n\n**/reportabuse** - /reportabuse @[The Abusive Player] [A Breif Description About The Abuse] - Report abuse to a moderator **(must be about the bot or it will be ignored)**\n\n**/invite** - /invite - Get The Bot Invitation Link!\n\n**/channelid** - /channelid [the channel] - Get the ID for the channel!\n\n**/roleid** - /roleid [the role] - Get the ID for the role!\n\n**/playerid** - /playerid [the player] - Get the ID for the player!\n\n**/hyperlink** - /hyperlink [URL] [text] - Make A Hyperlink In An Embed!\n\n**/binary** - /binary [decimal number] - convert decimal to binary.\n\n**/question** - /question ,[number of answers],[question],[answer],[answer],[answer],[answer]etc - ask a poll-like question!\n\n**/cat** - /cat - Get a random cat image!\n\n**/dog** - /dog - Get a random dog image!\n\n**/kys** - /kys @[the member] - Something Happens (see what happens if you @ helper in the first argument!)\n\n  \n*Need more help?*\n\nDo /ask [your question] to ask a moderator a question!\n\nor...\n\n ***Join:*** \n\nHelper Bot Discord: https://discord.gg/QBzsbmh          \n\n**{version}**', colour=0xff9400)
        em.set_author(name='HelperBot', icon_url=client.user.default_avatar_url)
        await client.send_message(message.channel, embed=em)
        await client.edit_message(lolomg,":white_check_mark: Help Sent!")
        await client.delete_message(message)
    if message.content.upper().startswith("/FLIP"):
        man = random.choice(choice)
        em = discord.Embed(title="Coin Flip", description=f"{man} \n\n{version}", colour=0xff9400)
        em.set_author(name="Helper Bot", icon_url=client.user.default_avatar_url)
        await client.send_message(message.channel, embed=em)
        
    if message.content.upper().startswith("/ROLL"):
        men = random.choice(dice)
        em = discord.Embed(title="Dice Roll", description=f"{men} \n\n{version}", colour=0xff9400)
        em.set_author(name="Helper bot", icon_url=client.user.default_avatar_url)
        await client.send_message(message.channel, embed=em)
    contents = message.content.split(" ")
    if message.content.upper().startswith("/SERVERS"):
        await client.send_message(message.channel, "I am in %s servers." % len(client.servers))
        
        coolo = len(client.servers)
        await client.change_presence(game=discord.Game(name=f"/help || {coolo} servers! http://bit.do/helperbotdiscord", url="https://www.twitch.tv/itscoolo2", type=1))
        await client.delete_message(message)
    if message.content.upper().startswith("/DISCORDPYTHONVERSION"):
        await client.send_message(message.channel, discord.__version__)
    if message.content.upper().startswith("/SAY"):
        args = message.content.split(" ")
        thetts = "%s" % (" ".join(args[1:]))
        nospam = "%s" % ("".join(args[1]))
        if nospam =="/say":
            await client.send_message(message.channel, ":negative_squared_cross_mark: Dont Even Try.")
            await client.delete_message(message)
        await client.send_message(message.channel, thetts)
        await client.delete_message(message)
    if message.content.upper().startswith('/MEMBERS'):
        await client.send_message(message.channel, ":white_check_mark: Counting Members In DM.")
        x = message.server.members
        count =0
        for member in x:
            await client.send_message(message.author, member.name)
    if message.content.upper().startswith('/SPAMME'):
        await client.send_message(message.channel, ":white_check_mark: Spamming Started (In DM)")
        args = message.content.split(" ")
        messages = "%s" % (" ".join(args[1:]))
        for i in range(1,50):
            await client.send_message(message.author, f"{messages}")
            time.sleep(0.1)
    if message.content.upper().startswith("/PURGE"): 
        args = message.content.split(" ")
        howmany = int("%s" % ("".join(args[1])))
        uu = await client.send_message(message.channel, ":negative_squared_cross_mark: You Do Not Have Delete Message Perms.")
        await client.delete_message(message)
        await client.delete_message(uu)
        deleted = await client.purge_from(message.channel, limit=howmany)
        await client.send_message(message.channel, ':white_check_mark: Deleted {} message(s)'.format(len(deleted)))
    if message.content.upper().startswith("/EMBED"):
        args = message.content.split(" ")
        yeaht = "%s" % (" ".join(args[3:]))
        yeahtoo = "%s" % ("".join(args[1]))
        yeahthree = "%s" % ("".join(args[2]))
        em = discord.Embed(title=yeahthree, description=f"{yeaht}\n\n{version}", colour=0xff9400)
        em.set_author(name=yeahtoo, icon_url=client.user.default_avatar_url)
        await client.send_message(message.channel, embed=em)
        await client.delete_message(message)
    if message.content.upper().startswith("/EMOJI"):
        args = message.content.split(" ")
        herewego = "%s" % ("".join(args[1]))
        if herewego =="emoji":
            await client.send_message(message.channel, ":%s:" % (": :".join(args[2:])))
        if herewego =="type":
            await client.send_message(message.channel, ":regional_indicator_%s:" % (": :regional_indicator_".join(args[2:])))
        await client.delete_message(message)
    if message.content.upper().startswith("/ANIMATE"):
        first = await client.send_message(message.channel, ":white_check_mark: Choosing a random animation.")
        time.sleep(0.3)
        await client.edit_message(first,":white_check_mark: Choosing a random animation..")
        time.sleep(0.3)
        await client.edit_message(first,":white_check_mark: Choosing a random animation...")
        time.sleep(0.3)
        await client.edit_message(first,":white_check_mark: Choosing a random animation..")
        time.sleep(0.3)
        await client.edit_message(first,":white_check_mark: Choosing a random animation.")
        randomting = random.choice("12")
        if randomting =="1":
            for i in range(1,10):
                await client.edit_message(first,":)")
                time.sleep(0.2)
                await client.edit_message(first,":|")
                time.sleep(0.2)
                await client.edit_message(first,":(")
                time.sleep(0.2)
                await client.edit_message(first,":|")
                time.sleep(0.2)
        if randomting =="2":
            for i in range(1,10):
                await client.edit_message(first,"|")
                time.sleep(0.2)
                await client.edit_message(first,"/")
                time.sleep(0.2)
                await client.edit_message(first,"-")
                time.sleep(0.2)
                await client.edit_message(first,'\\')
                time.sleep(0.2)
    if message.content.upper().startswith("/POLL"):
        args = message.content.split(" ")
        thetime = "%s" % (" ".join(args[1:]))
        em = discord.Embed(description=f"{thetime} \n\n**{version}**", colour=0xff9400)
        whatisit = await client.send_message(message.channel, embed=em)
        await client.add_reaction(whatisit, "\U0001F44D")
        await client.add_reaction(whatisit, "\U0001F937")
        await client.add_reaction(whatisit, "\U0001F44E")
        await client.delete_message(message)
    if message.content.upper().startswith("/MED"):
        await client.send_message(message.channel, discord.User.avatar)
    if message.content.upper().startswith("/CALCULATE"):
        args = message.content.split(" ")
        argone = "%s" % ("".join(args[1]))
        argtwo = "%s" % ("".join(args[2]))
        argthree = "%s" % ("".join(args[3]))
        argthree = int(argthree)
        argone = int(argone)
        if argtwo =="+":
            await client.send_message(message.channel, argone+argthree)
        if argtwo =="-":
            await client.send_message(message.channel, argone-argthree)
        if argtwo =="/":
            await client.send_message(message.channel, argone/argthree)
        if argtwo =="÷":
            await client.send_message(message.channel, argone/argthree)
        if argtwo =="*":
            await client.send_message(message.channel, argone*argthree)
        if argtwo =="x":
            await client.send_message(message.channel, argone*argthree)
        if argtwo =="X":
            await client.send_message(message.channel, argone*argthree)
    if message.content.upper().startswith("/RPS"):
        args = message.content.split(" ")
        xd = "%s" % ("".join(args[1]))
        ye = ("rock", "paper", "scissors")
        lol = random.choice(ye)
        time.sleep(.3)
        await client.send_message(message.channel, lol)
        time.sleep(0.5)
        if lol =="rock":
            if xd=="rock":
                await client.send_message(message.channel, ":white_check_mark: Draw!")
            if xd=="paper":
                await client.send_message(message.channel, ":white_check_mark: You Won!")
            if xd=="scissors":
                await client.send_message(message.channel, ":white_check_mark: I Won!")
        if lol =="paper":
            if xd=="paper":
                await client.send_message(message.channel, ":white_check_mark: Draw!")
            if xd=="scissors":
                await client.send_message(message.channel, ":white_check_mark: You Won!")
            if xd=="rock":
                await client.send_message(message.channel, ":white_check_mark: I Won!")
        if lol =="scissors":
            if xd=="scissors":
                await client.send_message(message.channel, ":white_check_mark: Draw!")
            if xd=="rock":
                await client.send_message(message.channel, ":white_check_mark: You Won!")
            if xd=="paper":
                await client.send_message(message.channel, ":white_check_mark: I Won!")
    if message.content.upper().startswith("/WARN"):
        args = message.content.split(" ")
        theid = "%s" % ("".join(args[1]))
        theid = theid.replace('<', '')
        theid = theid.replace('>', '')
        theid = theid.replace('@', '')
        theid = theid.replace('!', '')
        print(theid)
        themessage = "%s" % (" ".join(args[2:]))
        userID = message.author.id
        yes = userID
        await client.send_message(await client.get_user_info(theid), f"**You were warned by <@{yes}>. The Reason Is:** %s" % (themessage))
        await client.send_message(message.author, "You Sucsessfully Warned <@%s>." % (theid))
        await client.send_message(message.author, "The User ID Is: %s" % (theid))
        await client.send_message(message.channel, ":white_check_mark: Warned The User: %s." % (theid))
        await client.send_message(await client.get_user_info(theid), "To Report Abuse, Type **/reportabuse @[The User To Report] [The Reason]** Now")
        await client.delete_message(message)
    if message.content.upper().startswith("/REPORTABUSE"):
        args = message.content.split(" ")
        theiddd = "%s" % ("".join(args[1]))
        messagess = "%s" % (" ".join(args[2:]))
        userID = message.author.id
        omgg = userID
        await client.send_message(await client.get_user_info("368071242189897728"), f"**Abuse Was Reported By: <@{omgg}>, The User Is: {theiddd}, The Reason Is:** %s  " % (messagess))
        await client.send_message(await client.get_user_info("325358716499001345"), f"**Abuse Was Reported By: <@{omgg}>, The User Is: {theiddd}, The Reason Is:** %s  " % (messagess))
        await client.send_message(message.channel, f"<@{omgg}> Reported {theiddd}. The Reason Is: %s  " % (messagess))
        await client.delete_message(message)
    if message.content.upper().startswith("/REPORTBUGS"):
        args = message.content.split(" ")
        messagesss = "%s" % (" ".join(args[1:]))
        userID = message.author.id
        omggg = userID
        await client.send_message(await client.get_user_info("368071242189897728"), f"A bug Was Reported By: <@{omggg}>, The Bug Is: **%s**  " % (messagesss))
        await client.send_message(await client.get_user_info("325358716499001345"), f"A bug Was Reported By: <@{omggg}>, The Bug Is: **%s**  " % (messagesss))
        await client.send_message(message.channel, f":white_check_mark: <@{omggg}> Reported A Bug. Thank You! :thumbsup: !")
        await client.delete_message(message)
    if message.content.upper().startswith("/ASK"):
        args = message.content.split(" ")
        messagessss = "%s" % (" ".join(args[1:]))
        userID = message.author.id
        omgggg = userID
        await client.send_message(await client.get_user_info("368071242189897728"), f"A question was asked By: <@{omgggg}>, The Question Is:** %s**  " % (messagessss))
        await client.send_message(await client.get_user_info("325358716499001345"), f"A question was asked By: <@{omgggg}>, The Question Is: **%s**  " % (messagessss))
        await client.send_message(message.author, f":white_check_mark: <@{omgggg}>, You Will Get A Reply ASAP. ")
        await client.delete_message(message)
    if message.content.upper().startswith("/USERINFO"):
        args = message.content.split(" ")
        ids = "%s" % ("".join(args[1]))
        ideas = "%s" % ("".join(args[1]))
        ids = ids.replace('<', '')
        ids = ids.replace('>', '')
        ids = ids.replace('@', '')
        ids = idss.replace('!', '')
        await client.send_message(message.author, "User ID: %s" % (ids))
        await client.send_message(message.author, "Username : %s" % (ideas))
        await client.send_message(message.author, "To DM The User, Go Into A Server That They Are In, And Type: /dm %s [Your DM Message]" % (ideas))
        await client.send_message(message.channel, ":white_check_mark: User Info Sent In DM.")
        await client.delete_message(message)
    if message.content.upper().startswith("/CHANNELID"):
        args = message.content.split(" ")
        idss = "%s" % ("".join(args[1]))
        idss = idss.replace('<', '')
        idss = idss.replace('>', '')
        idss = idss.replace('#', '')
        await client.send_message(message.channel, f":white_check_mark: The ID of the channel is {idss}")
    if message.content.upper().startswith("/ANSWER"):
        args = message.content.split(" ")
        theidaa = "%s" % ("".join(args[1]))
        theidaa = theidaa.replace('<', '')
        theidaa = theidaa.replace('>', '')
        theidaa = theidaa.replace('@', '')
        print(theidaa)
        userID = message.author.id
        omgggga = userID
        themessage = "%s" % (" ".join(args[2:]))
        await client.send_message(await client.get_user_info(theidaa), f':white_check_mark: Your Message Was Seen By A Moderator (<@{omgggga}>). Their Reply Is: **{themessage}**')
        await client.send_message(await client.get_user_info("368071242189897728"), f":white_check_mark: <@{theidaa}> s Question Answered by Moderator <@{omgggga}>")
        await client.send_message(await client.get_user_info("325358716499001345"), f":white_check_mark: <@{theidaa}> s Question Answered by Moderator <@{omgggga}>. ")
        await client.delete_message(message)
    if message.content.upper().startswith("/QUESTION"):
        warning = await client.send_message(message.channel, ":negative_squared_cross_mark: Something Went Wrong, Did You Use ',' Inbetween Each Argument? Did You Use The Right Amount of arguments that you stated in argument 1?")
        args = message.content.split(",")
        howmany = "%s" % ("".join(args[1]))
        if howmany=="1":
            question = "%s" % ("".join(args[2]))
            firstarg = "%s" % ("".join(args[3]))
            content = f"{question}\n\n :regional_indicator_a: : {firstarg}\n\n\n**{version}**"
            em = discord.Embed(title="Question", description=content, colour=0xff9400)
            wowow = await client.send_message(message.channel, embed=em)
            await client.add_reaction(wowow, "\U0001F1E6")
        if howmany=="2":
            question = "%s" % ("".join(args[2]))
            firstarg = "%s" % ("".join(args[3]))
            secondarg = "%s" % ("".join(args[4]))
            content = f"{question}\n\n :regional_indicator_a: : {firstarg}\n\n :regional_indicator_b: : {secondarg}\n\n\n**{version}**"
            em = discord.Embed(title="Question", description=content, colour=0xff9400)
            wowow = await client.send_message(message.channel, embed=em)
            await client.add_reaction(wowow, "\U0001F1E6")
            await client.add_reaction(wowow, "\U0001F1E7")
        if howmany=="3":
            question = "%s" % ("".join(args[2]))
            firstarg = "%s" % ("".join(args[3]))
            secondarg = "%s" % ("".join(args[4]))
            thirdarg = "%s" % ("".join(args[5]))
            content = f"{question}\n\n :regional_indicator_a: : {firstarg}\n\n :regional_indicator_b: : {secondarg}\n\n :regional_indicator_c: : {thirdarg}\n\n\n**{version}**"
            em = discord.Embed(title="Question", description=content, colour=0xff9400)
            wowow = await client.send_message(message.channel, embed=em)
            await client.add_reaction(wowow, "\U0001F1E6")
            await client.add_reaction(wowow, "\U0001F1E7")
            await client.add_reaction(wowow, "\U0001F1E8")
        if howmany=="4":
            question = "%s" % ("".join(args[2]))
            firstarg = "%s" % ("".join(args[3]))
            secondarg = "%s" % ("".join(args[4]))
            thirdarg = "%s" % ("".join(args[5]))
            fourtharg = "%s" % ("".join(args[6]))
            content = f"{question}\n\n :regional_indicator_a: : {firstarg}\n\n :regional_indicator_b: : {secondarg}\n\n :regional_indicator_c: : {thirdarg}\n\n :regional_indicator_d: : {fourtharg}\n\n\n**{version}**"
            em = discord.Embed(title="Question", description=content, colour=0xff9400)
            wowow = await client.send_message(message.channel, embed=em)
            await client.add_reaction(wowow, "\U0001F1E6")
            await client.add_reaction(wowow, "\U0001F1E7")
            await client.add_reaction(wowow, "\U0001F1E8")
            await client.add_reaction(wowow, "\U0001F1E9")
        if howmany=="5":
            question = "%s" % ("".join(args[2]))
            firstarg = "%s" % ("".join(args[3]))
            secondarg = "%s" % ("".join(args[4]))
            thirdarg = "%s" % ("".join(args[5]))
            fourtharg = "%s" % ("".join(args[6]))
            fiftharg = "%s" % ("".join(args[7]))
            content = f"{question}\n\n :regional_indicator_a: : {firstarg}\n\n :regional_indicator_b: : {secondarg}\n\n :regional_indicator_c: : {thirdarg}\n\n :regional_indicator_d: : {fourtharg}\n\n :regional_indicator_e: : {fiftharg}\n\n\n**{version}**"
            em = discord.Embed(title="Question", description=content, colour=0xff9400)
            wowow = await client.send_message(message.channel, embed=em)
            await client.add_reaction(wowow, "\U0001F1E6")
            await client.add_reaction(wowow, "\U0001F1E7")
            await client.add_reaction(wowow, "\U0001F1E8")
            await client.add_reaction(wowow, "\U0001F1E9")
            await client.add_reaction(wowow, "\U0001F1EA")
        if howmany=="6":
            question = "%s" % ("".join(args[2]))
            firstarg = "%s" % ("".join(args[3]))
            secondarg = "%s" % ("".join(args[4]))
            thirdarg = "%s" % ("".join(args[5]))
            fourtharg = "%s" % ("".join(args[6]))
            fiftharg = "%s" % ("".join(args[7]))
            sixtharg = "%s" % ("".join(args[8]))
            content = f"{question}\n\n :regional_indicator_a: : {firstarg}\n\n :regional_indicator_b: : {secondarg}\n\n :regional_indicator_c: : {thirdarg}\n\n :regional_indicator_d: : {fourtharg}\n\n :regional_indicator_e: : {fiftharg}\n\n :regional_indicator_f: : {sixtharg}\n\n\n**{version}**"
            em = discord.Embed(title="Question", description=content, colour=0xff9400)
            wowow = await client.send_message(message.channel, embed=em)
            await client.add_reaction(wowow, "\U0001F1E6")
            await client.add_reaction(wowow, "\U0001F1E7")
            await client.add_reaction(wowow, "\U0001F1E8")
            await client.add_reaction(wowow, "\U0001F1E9")
            await client.add_reaction(wowow, "\U0001F1EA")
            await client.add_reaction(wowow, "\U0001F1EB")
        await client.delete_message(message)
        await client.delete_message(warning)
    if message.content.upper().startswith("/INVITE"):
        em = discord.Embed(title=":white_check_mark: Invite me here! :white_check_mark: ", url= "https://discordapp.com/api/oauth2/authorize?client_id=444882566529417216&permissions=8&scope=bot", colour=0xff9400)
        await client.send_message(message.channel, embed=em)
        await client.delete_message(message)
    if message.content.upper().startswith("/PLAYERID"):
        args = message.content.split(" ")
        idss = "%s" % ("".join(args[1]))
        idss = idss.replace('<', '')
        idss = idss.replace('>', '')
        idss = idss.replace('@', '')
        idss = idss.replace('!', '')
        await client.send_message(message.channel, f":white_check_mark: The ID of the player is {idss}")
    if message.content.upper().startswith("/ROLEID"):
        args = message.content.split(" ")
        idss = "%s" % ("".join(args[1]))
        idss = idss.replace('<', '')
        idss = idss.replace('>', '')
        idss = idss.replace('&', '')
        idss = idss.replace('@', '')
        await client.send_message(message.channel, f":white_check_mark: The ID of the role is {idss}")
    if message.content.upper().startswith("/HYPERLINK"):
        args = message.content.split(" ")
        secondone = "%s" % ("".join(args[1]))
        text = "%s" % (" ".join(args[2:]))
        lk = await client.send_message(message.channel, ":negative_squared_cross_mark: Something Went Wrong. Check That The First Argument **Is a link** and the second argument **is text.**")
        em = discord.Embed(title=text, url= secondone, colour=0xff9400)
        await client.send_message(message.channel, embed=em)
        await client.delete_message(message)
        await client.delete_message(lk)
    if message.content.upper().startswith("/BINARY"):
        oo = discord.Embed(title=":negative_squared_cross_mark: Invalid argument, The argument could be a decimal number or might not be a number.\n\n{version}", colour=0xff9400)
        ii = await client.send_message(message.channel, embed=oo)
        args = message.content.split(" ")
        dec = "%s" % ("".join(args[1]))
        decimal = int(dec);
        rip = bin(decimal);
        rip = str(rip)
        yy = discord.Embed(title=f":white_check_mark: {decimal} in binary is {rip}\n\n{version}", colour=0xff9400)
        await client.send_message(message.channel, embed=yy)
        await client.delete_message(ii)
    if message.content.upper().startswith("/CAT"):
        #Get a random url of a cat
        r = requests.get('http://catapi.glitch.me/random')
        json = r.json()
        if r.status_code == 200:
            await client.send_message(message.channel, json['url'])
        else:
            await client.send_message(message.channel, 'I could not access the API!')
    
    if message.content.upper().startswith("/DOG"):
        #Get a random url of a dog
        r = requests.get('https://random.dog/woof.json')
        json = r.json()
        if r.status_code == 200:
            await client.send_message(message.channel, json['url'])
        else:
            await client.send_message(message.channel, 'I could not access the API!')
    if message.content.upper().startswith("/GIVEWAY"):
        args = message.content.split(" ")
        arg1 = int("%s" % ("".join(args[1])))
        arg2 = "%s" % ("".join(args[2:]))
        themessage = await client.send_message(message.channel, f"A {arg1} Second Long Giveway For **{arg2}** Has Started! React With ~v~ To Enter!\n\n{arg1}")
        time.sleep(arg1)
        await client.delete_message(themessage)
    if message.content.upper().startswith("/KYS"):
        args = message.content.split(" ")
        at = "%s" % ("".join(args[1]))
        print(at)
        if at=="<@444882566529417216>":
            await client.send_message(message.channel, f"R.I.P {at}\n https://media.giphy.com/media/TIeCR6ntey96USIrem/giphy.gif")
        else:
            await client.send_message(message.channel, f"R.I.P {at}\n https://media.giphy.com/media/2eKa67bpYGGjfm9LJr/giphy.gif")
    if message.content.upper().startswith("<@444882566529417216>"):
        lolomg = await client.send_message(message.channel, ":white_check_mark: Sending Help...")
        em = discord.Embed(title="Bot Help", description=f'**/pingme** - /pingme - pings you with an @. \n\n**/help** - /help - gives help on the bot. \n\n**/amicoolo** - /amicoolo - shows wheather you are coolo. \n\n**/amiadmin** - /amiadmin - shows if you are admin \n\n**/info** - /info - shows info on the bot. \n\n**/say** - /say [your message] - says what you say.\n\n**/flip** - /flip - Flips a coin\n\n**/discordpythonversionversion** - /discordpythonversion - shows discord version.\n\n**/servers** - /servers - shows how many servers the bot is in.\n\n**/roll** - /roll - rolls dice.\n\n**/dm** - /dm @[the user] [the message you want to send] - DMs the user with  the message you wrote.\n\n**/members** - /members - DMs you all members in the server that the message is sent in. Sends them 5 at a time (Warning: cloggs up DM with the bot for a short while.)\n\n**/spamme** - /spamme [Spam message] - **Warning:** Spams you in DMs\n\n**/embed **- /embed [top title(no spaces)] [middle title(no spaces)] [message] - embeds the message you wrote.\n\n**/emoji emoji**- /emoji emoji [your emoji](can do as many emojis as you want) - Display emoji(s).\n\n**/animate** - /animate - Display a random animation(**Warning:** Can Lag).\n\n**/emoji type** - /emoji type - say the message with emojis! (Put a space in between each letter)\n\n**/purge** - /purge [amount] - mass delete messages\n\n**/poll** - /poll [your question] - create a poll!\n\n**/calculate** - /calculate [Math question] - calculates a math question! (cant use decimals)\n\n**/rps** - /rps [rock, paper or scissors] - plays rock paper scissors\n\n**/warn** - /warn @[The username] [Reason] - warn users who break a rule!\n\n\n**{version}**', colour=0xff9400)
        em.set_author(name='HelperBot', icon_url=client.user.default_avatar_url)
        await client.send_message(message.channel, embed=em)
        em = discord.Embed(title="Bot Help", description=f'\n\n**/userinfo** - /userinfo @[The User] - Sends Info On The User In DM.\n\n**/reportbugs** - /reportbugs [The Bug] - Report A Bug To A Moderator!\n\n**/reportabuse** - /reportabuse @[The Abusive Player] [A Breif Description About The Abuse] - Report abuse to a moderator **(must be about the bot or it will be ignored)**\n\n**/invite** - /invite - Get The Bot Invitation Link!\n\n**/channelid** - /channelid [the channel] - Get the ID for the channel!\n\n**/roleid** - /roleid [the role] - Get the ID for the role!\n\n**/playerid** - /playerid [the player] - Get the ID for the player!\n\n**/hyperlink** - /hyperlink [URL] [text] - Make A Hyperlink In An Embed!\n\n**/binary** - /binary [decimal number] - convert decimal to binary.\n\n**/question** - /question ,[number of answers],[question],[answer],[answer],[answer],[answer]etc - ask a poll-like question!\n\n**/cat** - /cat - Get a random cat image!\n\n**/dog** - /dog - Get a random dog image!\n\n**/kys** - /kys @[the member] - Something Happens (see what happens if you @ helper in the first argument!)\n\n  \n*Need more help?*\n\nDo /ask [your question] to ask a moderator a question!\n\nor...\n\n ***Join:*** \n\nHelper Bot Discord: https://discord.gg/QBzsbmh          \n\n**{version}**', colour=0xff9400)
        em.set_author(name='HelperBot', icon_url=client.user.default_avatar_url)
        await client.send_message(message.channel, embed=em)
        await client.edit_message(lolomg,":white_check_mark: Help Sent!")
        await client.delete_message(message)
        
        


client.run(os.getenv('TOKEN'))









