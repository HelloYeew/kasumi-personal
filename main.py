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
from nsfw import *
from spotify import *
import os
from datetime import datetime
import pytz

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
    embed.description = f"I catch it in {int(bot.latency * 1000)} milliseconds!"
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    await ctx.send(embed=embed)


@bot.command()
async def profile(ctx, member: discord.User):
    author = ctx.message.author
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    if member.id == 729919152327753768:
        embed.title = f"🐵 {member.name + '#' + member.discriminator}'s Profile"
    elif member.id == 366066360075288577:
        embed.title = f"😇 {member.name + '#' + member.discriminator}'s Profile"
    elif member.bot:
        embed.title = f"🤖 {member.name + '#' + member.discriminator}'s Profile"
    else:
        embed.title = f"😃 {member.name + '#' + member.discriminator}'s Profile"
    embed.description = f"Request by {author.display_name}"
    embed.add_field(name="Display Name", value=member.display_name, inline=False)
    embed.add_field(name="ID", value=member.id, inline=False)
    embed.add_field(name="Create Account Time", value=f"{member.created_at} UTC", inline=False)
    embed.add_field(name="Bot?", value=member.bot, inline=False)
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    await ctx.send(embed=embed)


@bot.command()
async def about(ctx):
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    father_info = """
    My Father : HelloYeew#2740
    GitHub : https://github.com/HelloYeew
    Other SNS you can see in his Discord profiles.
    """
    embed.title = "About Kasumi"
    embed.description = "I'm Kasumi Toyama. I am finding a star that can make a music band with my friend. \n This bot is change for personal use."
    embed.add_field(name="GitHub Repositories", value="https://github.com/HelloYeew/kasumi", inline=False)
    embed.add_field(name="About My Father", value=father_info, inline=False)
    embed.set_thumbnail(url="https://github.com/HelloYeew/kasumi/blob/main/icon/kasumiicon.jpg?raw=true")
    embed.add_field(name="Under Development", value="I'm under development. My father have a lot of work to make "
                                                    "me. If you find something wrong about me you can DM my father!")
    await ctx.send(embed=embed)


@bot.command()
async def send(ctx, channel_id: int, *args):
    channel = bot.get_channel(channel_id)
    author = ctx.message.author
    message = " ".join(args[:])
    UTC = pytz.utc
    await ctx.send(f"✉️ Sending your message to channel {channel_id}...")
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.title = f"✉️ Message from {author.display_name}"
    embed.description = message
    embed.set_footer(text=f"Send by Kasumi | Time : {datetime.now(UTC)} UTC")
    try:
        await channel.send(embed=embed)
        await ctx.send("✅ Complete!")
    except:
        await ctx.send("❌ Error : Check your channel ID or I can't reach that channel because I'm not in that server.")


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
    - !profile (user) : Show full user's profile
    - !send (channel_id) (message) : Send a message to a specific channel by a bot (You can target every channel that a bot can access)
    - !gif (keyword) : Send first GIF search result of a keyword
    - !about : About this bot
    
    **Genius Command**
    - !roots2 (float_x^1) (float_x^0) : Calculate a roots of one-dimension polynomial (two numbers)
    - !roots3 (float_x^2) (float_x^1) (float_x^0) : Calculate a roots of one-dimension polynomial (three numbers)
    
    **SKE Command**
    - !discrete : Get a link for Discrete Mathematics Meet room
    - !compro2 : Get a link for Computer Programming II Meet room
    - !labphy2 : Get a link for Laboratory in Physics II (453) Meet room
    - !math2 : Get a link for Math II Meet room
    - !thaicom : Get a link for Thai Communication Meet room
    - !midterm : See midterm test schedule
    - !drive : Get OneDrive link
    
    **Spotify Command (Beta)**
    - !spotify (keyword) : Get first search result from Spotify
    
    **NSFW Command**
    - !pornhub (keyword) : Get first search result from Pornhub
    - !nhentai (keyword) : Get first search result from Nhentai
    - !nhentai random : Get a random hentai from Nhentai
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
async def gif(ctx, *args):
    """Return first GIF search result"""
    word = " ".join(args[:])
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


# Spotify Command

@bot.command()
async def spotify(ctx, *args):
    keyword = " ".join(args[:])
    search = spotify_first_search(keyword)
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.title = f"🔎 Result of Spotify search '{keyword}'"
    embed.description = f"First Spotify search result of *{keyword}*"
    embed.add_field(name="Name", value=search['name'], inline=False)
    embed.add_field(name="Artist", value=search['artist_name'], inline=False)
    embed.add_field(name="Album Name", value=search['album_name'], inline=False)
    embed.add_field(name="Available Country", value=search['available_country'], inline=False)
    embed.add_field(name="Release Date", value=search['release_date'], inline=True)
    embed.add_field(name="Popularity", value=search['popularity'], inline=True)
    embed.add_field(name="Preview", value=search['preview_url'], inline=False)
    embed.set_footer(
        text=f"Total result : {search['total_result']} | Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    embed.set_image(url=search["image_url"])
    await ctx.send(embed=embed)


# NSFW Command

@bot.command()
async def pornhub(ctx, *args):
    """Return first search pornhub results"""
    word = " ".join(args[:])
    if nsfw_mode == False:
        await ctx.send("You must enable NSFW command by **!nsfw on**")
    else:
        result = pornhub_search(word)
        embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
        embed.title = f"🔎 Result of Pornhub search '{word}'"
        embed.description = f"First GIF search result of *{word}*"
        embed.add_field(name="Name", value=result[1], inline=False)
        embed.add_field(name="Link", value=result[0], inline=False)
        embed.add_field(name="Duration", value=result[2], inline=True)
        embed.add_field(name="Rating", value=result[3], inline=True)
        embed.set_image(url=result[4])
        embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
        await ctx.send(embed=embed)


#
#
@bot.command()
async def nhentai(ctx, *args):
    """Return first search pornhub results"""
    keyword = " ".join(args[:])
    if nsfw_mode == False:
        await ctx.send("You must enable NSFW command by **!nsfw on**")
    else:
        if keyword == "random":
            result = nhentai_random()
            embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
            embed.title = f"🔎 You have request random hentai from me?"
            embed.description = f"You have it!"
            embed.add_field(name="Title", value=result.title, inline=False)
            embed.add_field(name="Second Title", value=result.secondary_title, inline=False)
            embed.add_field(name="Tags", value=result.tags, inline=False)
            embed.add_field(name="Artists", value=result.artists, inline=False)
            embed.add_field(name="Characters", value=result.characters, inline=False)
            embed.add_field(name="Parodies", value=result.parodies, inline=False)
            embed.add_field(name="Group", value=result.parodies, inline=False)
            embed.add_field(name="Language", value=result.languages, inline=True)
            embed.add_field(name="Categories", value=result.categories, inline=True)
            embed.set_image(url=result.images[0])
            embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
            await ctx.send(embed=embed)
        else:
            result = nhentai_search(keyword)
            embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
            embed.title = f"🔎 Result of Nhentai search '{keyword}'"
            embed.description = f"First Nhentai search result of *{keyword}*"
            embed.add_field(name="Title", value=result.title, inline=False)
            embed.add_field(name="Data Tag", value=result.data_tags, inline=False)
            embed.add_field(name="Title ID", value=result.id, inline=True)
            embed.add_field(name="Language", value=result.lang, inline=True)
            embed.set_image(url=result.cover)
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


@bot.command()
async def drive(ctx):
    """Return math2 math meet link"""
    await ctx.send("https://1drv.ms/f/s!As4sE65K0j0JgqBI4-DrvEd6aiBWVw")


@bot.command()
async def midterm(ctx):
    """Midterm test timetable"""
    embed = discord.Embed(color=discord.Color.from_rgb(222, 137, 127))
    embed.title = f"📘 Midterm Test"
    embed.description = f"Time to have some TEST!"
    embed.add_field(name=":white_check_mark: Thursday 25 February",
                    value="- Man and Society 16:30-19.30 (In Class 2 Choice with a meme)",
                    inline=False)
    embed.add_field(name=":white_check_mark: Monday 1 March",
                    value="- Physics II Part 3 10:00-11:00 (Online)\n- Discrete Mathematics 13:00-16:00 (E503,E507)\nจด Note ตัวเองด้วยนะ",
                    inline=False)
    embed.add_field(name=":white_check_mark: Tuesday 2 March", value="- Math II 13:00-15:00 (ห้องนอน)", inline=False)
    embed.add_field(name=":white_check_mark: Thursday 4 March",
                    value="- Computer Programming II 09:00-12.00 (E203, E204)",
                    inline=False)
    embed.add_field(name=":white_check_mark: Saturday 6 March",
                    value="- Essential Computer 09:00-11.00 (Online)\n- Art Perception (Online)",
                    inline=False)
    embed.set_image(
        url="https://media.discordapp.net/attachments/804006192376315947/812229747626213406/152125627_3715784875168152_5671732948970309610_o.png?width=1121&height=504")
    embed.set_footer(text="Hello! My name is Kasumi Toyama! My father is HelloYeew#2740.")
    await ctx.send(embed=embed)


bot.run(bot_token)
