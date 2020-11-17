import discord
from discord.ext import commands
from discord.utils  import get
import random

client = commands.Bot(command_prefix='--')

#Command for version
@client.command(name='version')
async def version(context):
    myEmbed = discord.Embed(title="YouSmellNiceBot", description="Multi-purpose bot for funnies", color=0xf2b16b)
    myEmbed.add_field(name="Version Code", value="v1.1.1", inline=False)
    myEmbed.add_field(name="Date Released", value="November 05, 2020", inline=False)
    myEmbed.set_footer(text="yousmellnice for asking me this ;)")
    myEmbed.set_author(name="Aniketh Aatipamula")

    await context.send(embed=myEmbed)


#Command for functionality
@client.command(name='features')
async def features(context):
    myEmbed2 = discord.Embed(title="What Do I Do?", description="I have a few fucntions, all listed below", color=0xf2b16b)
    myEmbed2.add_field(name="Reacting", value="I can react to messages by specfic members, and keywords, for now try 'simp'", inline=False)
    myEmbed2.add_field(name="Pinning", value="I will Pin messages in specfic channels from specfic people contaning specfic words", inline=False)
    myEmbed2.add_field(name="Messaging", value="I will react to certain words with phrases, try 'fuck'", inline=False)
    myEmbed2.add_field(name="Redacting", value="I will redact and respond to most common forms of the n-word", inline=False)
    myEmbed2.add_field(name="Pinging", value="I can ping someone when you say 'hey __' and put their name down", inline=False)
    myEmbed2.set_footer(text="More features will be added soon, please let the developers know what you want implemented! :)")

    await context.send(embed=myEmbed2)


#Say When Ready
@client.event
async def on_ready():
    print('I am ready')
    general_channel = client.get_channel(774022903665655888)
    await general_channel.send('Hi, you smell nice, I am ready to go!')

@client.event
async def on_message(message):

    yousmellnice = get(client.emojis, name='yousmellnice')
    response = message.channel
    bot_channel = client.get_channel(774887275955093575)

    #responses to keywords
    penis_message_responses = ["no penis fu", "penis", ">:(", "I'll penis you :smirk:"]
    fuck_message_responses = ["fuck you too", "I'll fuck your mom", ":rotating_light: bad word alert :rotating_light:"]
    omar_penis_responses = ["fuck who, me?", "penis fuck yourself", "I agree"]
    nig_responses = ["watch your fucking language you dipshit", "dont say that >:(", "you know what i don't blame you", "use BBC instead please", "please stop insulting Zonaid's brethren"]
    sabrina_face = [":pensive:", ":l", "felt that :/"]

    if message.content == "feat.": 

        myEmbed2 = discord.Embed(title="What Do I Do?", description="I have a few fucntions, all listed below", color=0xf2b16b)
        myEmbed2.add_field(name="Reacting", value="I can react to messages by specfic members, and keywords, for now try 'simp'", inline=False)
        myEmbed2.add_field(name="Pinning", value="I will Pin messages in specfic channels from specfic people contaning specfic words", inline=False)
        myEmbed2.add_field(name="Messaging", value="I will react to certain words with phrases, try 'fuck'", inline=False)
        myEmbed2.set_footer(text="More features will be added soon, please let the developer(s) know what you want implemented! :)")

        await bot_channel.send(embed=myEmbed2)

    await client.process_commands(message)

    #if message says simp then react with yousmellnice
    if message.content == 'simp':
        await message.add_reaction (yousmellnice)

    #if message says Simp then react with yousmellnice
    if message.content == 'Simp':
        await message.add_reaction (yousmellnice)

    #React to avi with Reaction
    if message.author.id == 543189972203601932:
        await message.add_reaction (yousmellnice)

    #Pin message for andrew in his channel
    if str(message.author.id) == "261190376268890123" and str(message.channel.id) == "771919025604395019" and "you know what sounds good rn?" in message.content:
        await message.pin()
    
    #Pin message for nabeel in his channel
    if str(message.author.id) == "368557189327224842" and str(message.channel.id) == "772541157262491698" and "appreciation" in message.content:
        await message.pin()

    #Pin message for sabrina in her channel
    if str(message.author.id) == "513591687948271636" and str(message.channel.id) == "772625475116990495" and "my nails" in message.content or "MY NAILS" in message.content:
        await message.pin()

    #when sabrina says :l or :|
    if ":l" in message.content or ":|" in message.content and message.author.id == (513591687948271636):
        if message.author == client.user:
            return
        random_response = (random.choice(sabrina_face))
        await   response.send(random_response)

    #Add a random message when someone says penis in their message
    if "penis" in message.content:
        if message.author == client.user:
            return
        random_response = (random.choice(penis_message_responses))
        await response.send(random_response)

    #Add a random message when omar says penis fu in his message
    if str(message.author.id) == "429389406080598018" and "penis fu" in message.content:
        random_response = (random.choice(omar_penis_responses))
        await response.send(random_response)

    #Add a random message when someone says penis in their message caps
    if "PENIS" in message.content:
        if message.author == client.user:
            return
        random_response = (random.choice(penis_message_responses))
        await response.send(random_response)

    #Add a random message when anyone says fuck
    if message.content == "fuck":
        if message.author == client.user:
            return
        random_response = (random.choice(fuck_message_responses))
        await response.send(random_response)

    #Add a random message when anyone says Fuck
    if message.content == "Fuck":
        if message.author == client.user:
            return
        random_response = (random.choice(fuck_message_responses))
        await response.send(random_response)

    #Add a random message when anyone says fuck CAPS
    if message.content == "FUCK":
        random_response = (random.choice(fuck_message_responses))
        await response.send(random_response)

    #Delete message and REDACT while responding for nigger
    if "niqq" in message.content or "Nigg" in message.content or "nibqa" in message.content or "NIGG" in message.content or "Nibqa" in message.content or "niga" in message.content or "NIGA" in message.content or "NIGG" in message.content:
        random_response = (random.choice(nig_responses))
        await message.channel.purge(limit=1)
        await response.send("**[REDACTED]**")
        await response.send(random_response)

    #Delete message and REDACT while responding for nigga
    if "nigg" in message.content or "nibba" in message.content or "nibga" in message.content or "n i g g a" in message.content or "NIGGER" in message.content  or "nibqa" in message.content or "Niqq" in message.content or "niqba" in message.content:
        random_response = (random.choice(nig_responses))
        await message.channel.purge(limit=1)
        await response.send("**[REDACTED]**")
        await response.send(random_response)

    #Message Authors
    #aniketh
    if message.author.id == (614188961216200752):
        message_author = "aniketh"

    #omar
    if message.author.id == (429389406080598018):
        message_author = "omar"

    #sabrina
    if message.author.id == (513591687948271636):
        message_author = "sabrina"

    #andrew
    if message.author.id == (261190376268890123):
        message_author = "andrew"

    #nabeel
    if message.author.id == (368557189327224842):
        message_author = "nabeel"

    #daniel
    if message.author.id == (485177071409037344):
        message_author = "daniel"

    #luke
    if message.author.id == (240989065099477003):
        message_author = "luke"

    #nihith
    if message.author.id == (316773501044523008):
        message_author = "nihith"

    #aiyan
    if message.author.id == (505806131906609152):
        message_author = "aiyan"

    #zoniad
    if message.author.id == (543195354212859926):
        message_author = "zoniad"

    #avi
    if message.author.id == (543189972203601932):
        message_author = "avi"

    #ashwin
    if message.author.id == (421748327697088513):
        message_author = "ashwin"

    #sree
    if message.author.id == (434877129398681610):
        message_author = "sree"

    #alex
    if message.author.id == (646221440881786880):
        message_author = "alex"

    #daniel c
    if message.author.id == (542430496257474561):
        message_author = "daniel c"

    #viraj
    if message.author.id == (338375504405069824):
        message_author = "viraj"

    #Hey @ People ----------------------------------------------------------
    #omar
    if message.content == "hey omar":
        omar = '<@429389406080598018>'
        await response.send(" %s {} pinged you".format(message_author) % omar)

    #andrew
    if message.content == "hey andrew":
        andrew = '<@261190376268890123>'
        await response.send(" %s {} pinged you".format(message_author) % andrew)

    #sabrina
    if message.content == "hey sabrina":
        sabrina = '<@513591687948271636>'
        await response.send(" %s {} pinged you".format(message_author) % sabrina)

    #nabeel
    if message.content == "hey nabeel":
        nabeel = '<@368557189327224842>'
        await response.send(" %s {} pinged you".format(message_author) % nabeel)

    #daniel
    if message.content == "hey daniel" or message.content == "hey danel":
        daniel = '<@485177071409037344>'
        await response.send(" %s {} pinged you".format(message_author) % daniel)

    #luke
    if message.content == "hey luke":
        luke = '<@240989065099477003>'
        await response.send(" %s {} pinged you".format(message_author) % luke)

    #nihith
    if message.content == "hey nihith":
        nihith = '<@316773501044523008>'
        await response.send(" %s {} pinged you".format(message_author) % nihith)

    #aiyan
    if message.content == "hey aiyan":
        aiyan = '<@505806131906609152>'
        await response.send(" %s {} pinged you".format(message_author) % aiyan)

    #zoniad
    if message.content == "hey zonaid":
        zoniad = '<@543195354212859926>'
        await response.send(" %s {} pinged you".format(message_author) % zoniad)

    #avi
    if message.content == "hey avi":
        avi = '<@543189972203601932>'
        await response.send(" %s {} pinged you".format(message_author) % avi)

    #ashwin
    if message.content == "hey ashwin":
        ashwin = '<@421748327697088513>'
        await response.send(" %s {} pinged you".format(message_author) % ashwin)

    #sree
    if message.content == "hey sree":
        sree = '<@434877129398681610>'
        await response.send(" %s {} pinged you".format(message_author) % sree)
    
    #alex
    if message.content == "hey alex":
        alex = '<@646221440881786880>'
        await response.send(" %s {} pinged you".format(message_author) % alex)

    #daniel c
    if message.content == "hey daniel c":
        daniel_c = '<@542430496257474561>'
        await response.send(" %s {} pinged you".format(message_author) % daniel_c)

    #viraj
    if message.content == "hey viraj":
        viraj = '<@338375504405069824>'
        await response.send(" %s {} pinged you".format(message_author) % viraj)

client.run('#token')
