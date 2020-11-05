import discord
from discord.ext import commands
from discord.utils  import get
import random

client = commands.Bot(command_prefix='--')

#Command for version
@client.command(name='version')
async def version(context):
    myEmbed = discord.Embed(title="YouSmellNiceBot", description="Multi-purpose bot for funnies", color=0xf2b16b)
    myEmbed.add_field(name="Version Code", value="v1.0.0 Beta", inline=False)
    myEmbed.add_field(name="Date Released", value="November 02, 2020", inline=False)
    myEmbed.set_footer(text="yousmellnice for asking me this ;)")
    myEmbed.set_author(name="Aniketh Aatipamula")

    await context.message.channel.send(embed=myEmbed)


#Say When Ready
@client.event
async def on_ready():
    print('I am ready')
    bot_channel = client.get_channel(int)
    await bot_channel.send('Hi, you smell nice, I am ready to go!')

@client.event
async def on_message(message):

    bot_channel = client.get_channel(int)
    yousmellnice = get(client.emojis, name='yousmellnice')

    penis_message_responses = ["no penis fu", "penis", ">:("]
    fuck_message_responses = ["fuck you too", "I'll fuck your mom", ":rotating_light: bad word alert :rotating_light:"]

    #Title card embed
    if message.content == 'ver.':
        myEmbed = discord.Embed(title="YouSmellNiceBot", description="Multi-purpose bot for funnies", color=0xf2b16b)
        myEmbed.add_field(name="Version Code", value="v1.0.0 ", inline=False)
        myEmbed.add_field(name="Date Released", value="November 02, 2020", inline=False)
        myEmbed.set_footer(text="yousmellnice for asking me this ;)")
        myEmbed.set_author(name="Aniketh Aatipamula")
        
        await bot_channel.send(embed=myEmbed)

    await client.process_commands(message)

    if message.content == 'simp':
        await message.add_reaction (yousmellnice)

    #React to specfic people with Reaction
    if message.author.id == int:
        await message.add_reaction (emoji)

    #Pin message for andrew in his channel
    if str(message.author.id) == "#author-id" and str(message.channel.id) == "#channel-id" and "you know what sounds good rn?" in message.content:
        await message.pin()
    
    #Pin message for nabeel in his channel
    if str(message.author.id) == "#author-id" and str(message.channel.id) == "#channel-id" and "appreciation" in message.content:
        await message.pin()

    #Add a random message when omar says penis in his message
    if str(message.author.id) == "#author-id" and "penis" in message.content:
        random_response = (random.choice(penis_message_responses))
        await message.send(random_response)

    #Add a random message when anyone says fuck
    if message.content == "fuck"
        random_response = (random.choice(fuck_message_responses))
        await message.send(random_response)

client.run('#bot-token')