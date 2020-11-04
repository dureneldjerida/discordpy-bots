import discord
from discord.ext import commands
from discord.utils  import get

client = commands.Bot(command_prefix='--')


@client.command(name='version')
async def version(context):
    myEmbed = discord.Embed(title="Current Version", description="Version 1.0 Beta", color=0xf2b16b)
    myEmbed.add_field(name="Version Code", value="v1.0.0 Beta", inline=False)
    myEmbed.add_field(name="Date Released", value="November 02, 2020", inline=False)
    myEmbed.set_footer(text="yousmellnice for asking me this ;)")
    myEmbed.set_author(name="Aniketh Aatipamula")

    await context.message.channel.send(embed=myEmbed)


@client.event
async def on_ready():
    print('I am ready')
    bot_channel = client.get_channel(451074658012233729)
    await bot_channel.send('Hi, you smell nice, I am ready to go!')

@client.event
async def on_message(message):

    bot_channel = client.get_channel(451074658012233729)

    if message.content == 'ver.':
        myEmbed = discord.Embed(title="Current Version", description="Version 1.0 Beta", color=0xf2b16b)
        myEmbed.add_field(name="Version Code", value="v1.0.0 Beta", inline=False)
        myEmbed.add_field(name="Date Released", value="November 02, 2020", inline=False)
        myEmbed.set_footer(text="yousmellnice for asking me this ;)")
        myEmbed.set_author(name="Aniketh Aatipamula")
        
        await bot_channel.send(embed=myEmbed)

    await client.process_commands(message)



    if message.content == 'simp':
        emoji = get(client.emojis, name='yousmellnice')
        await message.add_reaction (emoji)

    if message.author.id == 543195354212859926 or 485177071409037344:
        emoji = get(client.emojis, name='yousmellnice')
        await message.add_reaction (emoji)


client.run('NzczMjUxMDU3NTgwNTA3MTc4.X6GgKg.dXlxXfQ1_gC-a0MFl-yhIT-R9X4')