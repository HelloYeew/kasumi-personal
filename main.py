from check import *

# check requirement
check_library()

# import requirement
import discord
from discord.ext import commands
import random
import requests
import json
from genius_command import *
from tenor import *
import os

# personal function
from meet_link import *

# before run please don't forget to put bot token

description = "All Kasumi command is here"

# put all API key and bot token here

bot_token = os.getenv("DISCORD_BOT_TOKEN")
tenor_token = os.getenv("TENOR_TOKEN")

# First Config

nsfw_mode = True

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents, help_command=None)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game('Finding a star!'))


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))


@bot.command()
async def genius(ctx):
    """I'm genius!"""
    await ctx.send('กูฉลาดไอสัส อย่าเถียงกู')
    await ctx.send('https://tenor.com/view/saint-rock-head-shot-to-screen-smile-gif-19946978')


@bot.command()
async def pfp(ctx):
    author = ctx.message.author
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.title = "This is"
    embed.description = "Your profile image"
    # embed.colour = "#FF5522"
    embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    embed.set_thumbnail(url=author.avatar_url)
    await ctx.send(embed=embed)
    # add color!


# @bot.command()
# async def saint(ctx):
#     await ctx.send('''
#     while True:
#         await ctx.send('https://tenor.com/view/saint-rock-head-shot-to-screen-smile-gif-19946978')''')
#     while True:
#         await ctx.send('https://tenor.com/view/saint-rock-head-shot-to-screen-smile-gif-19946978')


@bot.command()
async def speedo(ctx):
    await ctx.send('https://media.tenor.com/images/afc316d68f9cc2fd1dab30cea5b85450/tenor.gif')
    await ctx.send('https://media.tenor.co/videos/144c5f3300c50d2c33251483f2d910ee/mp4')

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('ชั่ยๆ, status:{0.subcommand_passed} เอาแบบเบิ้มๆอะ คือลืออะ เหมือนเซ้นอะ'.format(ctx))


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


# @bot.command()
# async def repeat(ctx, text: str, time: int):
#     """Repeat a message x times"""
#     for i in range(time):
#         await ctx.send(text)

@bot.command()
async def ping(ctx):
    """ Check Ping"""
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.title = "🌟 I have caught a star that you throw to me!"
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    embed.description = f"I catch it in {bot.latency} seconds!"
    await ctx.send(embed=embed)



# help command

@bot.command()
async def help(ctx):
    help = '''
    **General Command**
    - !pfp : Sender's profile picture
    - !saint : while True Saint's Emoji (You cannot stop it) *(Disabled)*
    - !speedo : P'To SPEEEEEEEEEED
    - !genius : I'm genius!
    - !ping : Check ping
    - !repeat (text_or_sth) (x) : Spam a text x time(s) *(Disabled)*
    
    **Genius Command**
    - !roots2 (float_x^1) (float_x^0) : Calculate a roots of one-dimension polynomial (two numbers)
    - !roots3 (float_x^2) (float_x^1) (float_x^0) : Calculate a roots of one-dimension polynomial (three numbers)
    
    **SKE Command**
    - !discrete : Get a link for Discrete Mathematics Meet room
    - !compro2 : Get a link for Computer Programming II Meet room
    - !labphy2 : Get a link for Laboratory in Physics II (453) Meet room
    - !math2 : Get a link for Math II Meet room
    - !thaicom : Get a link for Thai Communication Meet room
    
    **NSFW Command**
    - !pornhub (keyword1) (keyword2) : Get first search result from Pornhub
    '''
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.title = "❓ Help"
    embed.description = help
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    await ctx.send(embed=embed)


# genius command zone

@bot.command()
async def roots2(ctx, n1: float, n2: float):
    """Root an poly"""
    author = ctx.message.author
    num = [n1, n2]
    answer = numpy.roots(num)
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
    embed.title = "🧮 Calculation"
    # embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/762347346993348659/335e22e0f77a6bb717502981f57221e2.png")
    embed.description = "A roots of one-dimension polynomial (two numbers)"
    embed.add_field(name="Input", value=str(numpy.poly1d(num)), inline=False)
    embed.add_field(name="Results", value=str(answer), inline=False)
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    await ctx.send(embed=embed)


@bot.command()
async def roots3(ctx, n1: float, n2: float, n3: float):
    """Root an poly"""
    author = ctx.message.author
    num = [n1, n2, n3]
    answer = numpy.roots(num)
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
    embed.title = "🧮 Calculation"
    # embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/762347346993348659/335e22e0f77a6bb717502981f57221e2.png")
    embed.description = "A roots of one-dimension polynomial (three numbers)"
    embed.add_field(name="Input", value=str(numpy.poly1d(num)), inline=False)
    embed.add_field(name="Results", value=str(answer), inline=False)
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    await ctx.send(embed=embed)


@bot.command()
async def roots4(ctx, n1: float, n2: float, n3: float, n4: float):
    """Root an poly"""
    author = ctx.message.author
    num = [n1, n2, n3, n4]
    answer = numpy.roots(num)
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
    embed.title = "🧮 Calculation"
    # embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/762347346993348659/335e22e0f77a6bb717502981f57221e2.png")
    embed.description = "A roots of one-dimension polynomial (four numbers)"
    embed.add_field(name="Input", value=str(numpy.poly1d(num)), inline=False)
    embed.add_field(name="Results", value=str(answer), inline=False)
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    await ctx.send(embed=embed)


# tenor command zone

@bot.command()
async def gif(ctx, word: str):
    """Return first GIF search result"""
    author = ctx.message.author
    try:
        result = tenor(tenor_token, word, 1)
        if result is not None:
            embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
            embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
            embed.title = f"🔎 Result of GIF search '{word}'"
            embed.description = f"First GIF search result of *{word}*"
            embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
            embed.set_image(url=result)

        else:
            embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
            embed.set_author(name=author.display_name, url="https://youtu.be/dQw4w9WgXcQ", icon_url=author.avatar_url)
            embed.title = f"🥲 No result of GIF search '{word}'"
            embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
            embed.description = "Sad"
        await ctx.send(embed=embed)
    except:
        await ctx.send("🔎 No search result!")


@bot.command()
async def gif5(ctx, word: str):
    """Return 5 GIF search result"""
    result = tenor(tenor_token, word, 5)
    for i in range(5):
        embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
        embed.title = f"🔎 Result of GIF search '{word}'"
        embed.description = f"Five top result in GIF search result of *{word}*\n **Result {i + 1}**"
        embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
        embed.set_image(url=result[i])
        await ctx.send(embed=embed)

# NSFW Command

@bot.command()
async def pornhub(ctx, word1: str, word2: str):
    """Return first search pornhub results"""
    if nsfw_mode == False:
        await ctx.send("You must enable NSFW command by **!nsfw on**")
    else:
        result = pornhub_search(word1,word2)
        embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
        embed.title = f"🔎 Result of Pornhub search '{word1} {word2}'"
        embed.description = f"First GIF search result of *{word1} {word2}*"
        embed.add_field(name="Name", value=result[1], inline=False)
        embed.add_field(name="Link", value=result[0], inline=False)
        embed.add_field(name="Duration", value=result[2], inline=True)
        embed.add_field(name="Rating", value=result[3], inline=True)
        embed.set_image(url=result[4])
        embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
        await ctx.send(embed=embed)

# SKE command

link = MeetLink()

@bot.command()
async def discrete(ctx):
    """Return discrete math meet link"""
    await ctx.send(link.discrete_link)

@bot.command()
async def compro2(ctx):
    """Return compro2 math meet link"""
    await ctx.send(link.compro2_link)

@bot.command()
async def labphy2(ctx):
    """Return labphy2 math meet link"""
    await ctx.send(link.labphy2_link)

@bot.command()
async def math2(ctx):
    """Return math2 math meet link"""
    await ctx.send(link.math2_link)

@bot.command()
async def thaicom(ctx):
    """Return math2 math meet link"""
    await ctx.send(link.thaicom_link)

@bot.command()
async def essencom(ctx):
    """Return math2 math meet link"""
    await ctx.send(link.essencom_link)

bot.run(bot_token)
