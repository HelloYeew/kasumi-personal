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
import os

# personal function
from meet_link import *

# before run please don't forget to put bot token

description = "All Kasumi command is here"

# put all API key and bot token here

# bot_token = os.getenv("DISCORD_BOT_TOKEN")
# tenor_token = os.getenv("TENOR_TOKEN")
bot_token = 'NzYyMzQ3MzQ2OTkzMzQ4NjU5.X3n1Sw.BwKhw8i04omm0wO8kggJWmc-Kgc'
tenor_token = "CNQLXJPB8DLJ"

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

ban_pto = ["https://tenor.com/view/ajam-mirada-sexy-dance-ricardo-gif-14184806",
           "https://images-ext-2.discordapp.net/external/FFAGhF2ONklGSKcBYqkPVpDsfR4_wRCYIcfETvJHOOs/https/media.tenor.com/images/986b86fc0543ed00022770e59423aa0e/tenor.gif",
           "https://tenor.com/view/flick-esfand-esfandtv-ricardo-milos-ricardo-flick-gif-13730968",
           "https://tenor.com/view/ricardo-flick-dance-weekend-vibe-gif-13753340",
           "https://tenor.com/view/dance-weekend-vibe-ricardo-milos-gif-13248415",
           "https://tenor.com/view/naruto-ricardo-kurama-milos-meme-gif-13427812",
           "https://tenor.com/view/ricardo-milos-mijolnir-ricardomilos-mijolnir-ricardo-gif-14302852",
           "https://tenor.com/view/love-amor-te-amo-like-ricardo-milos-gif-16651051",
           "https://tenor.com/view/ricardo-milos-ricardo-milos-gif-13248430",
           "https://tenor.com/view/ricardo-dance-gif-14164395",
           "https://tenor.com/view/ricardo-milos-dancing-musical-gif-16819339",
           "https://tenor.com/view/ricardo-milos-dance-moves-ricardo-is-best-best-dancer-gif-17065700",
           "https://tenor.com/view/ricardo-milos-meme-laser-gif-13923814",
           "https://tenor.com/view/pizza-ricardo-milos-flick-gif-14626147",
           "https://tenor.com/view/ricardo-smile-dance-gif-16914659",
           "https://tenor.com/view/ricardo-milos-come-here-dance-gif-14624582",
           "https://tenor.com/view/naruto-ricardo-milos-smile-gif-15497445",
           "https://tenor.com/view/flex-ricardo-milos-dancing-dance-moves-grooves-gif-16554974",
           "https://www.youtube.com/watch?v=N7oEOPweJ-A",
           "https://www.youtube.com/watch?v=Db49Qxkkm7M",
           "https://www.youtube.com/watch?v=0aJFWWuugzs",
           "https://www.youtube.com/watch?v=_yPt5dqrwsw&t=3s",
           "https://www.youtube.com/watch?v=_yPt5dqrwsw",
           "https://www.youtube.com/watch?v=LR08PkAj0_U",
           "https://www.youtube.com/watch?v=290EtOBbjA0",
           "https://www.youtube.com/watch?v=N_tGEFRYyBg",
           "https://www.youtube.com/watch?v=cq0dDyKhGf8",
           "https://www.youtube.com/watch?v=eHmkigDZYMc",
           "https://www.youtube.com/watch?v=Fv8A_i985VM",
           "https://www.youtube.com/watch?v=adjJQPmiktM",
           "https://www.youtube.com/watch?v=995D6w2sf0Y",
           "https://www.youtube.com/watch?v=JEZKH7m0FwM",
           "https://www.youtube.com/watch?v=s15q5v429Ig&t=113s",
           "https://www.youtube.com/watch?v=s15q5v429Ig",
           "https://www.youtube.com/watch?v=dpLbwLkBVZM",
           "https://www.youtube.com/watch?v=lfr65XGYY48",
           "https://www.youtube.com/watch?v=wIkayZUmm2k&t=62s",
           "https://www.youtube.com/watch?v=wIkayZUmm2k",
           "https://www.youtube.com/watch?v=kxO4UpEyRbw",
           "https://www.youtube.com/watch?v=bz2ZhCIvMzc",
           "https://www.youtube.com/watch?v=Bx00awTBVH4"]

random_complain = "https://www.youtube.com/watch?v=wXnG6VET-dw"

send_message = False

@bot.event
async def on_ready():
    print('Banned Pto as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    # await bot.change_presence(activity=discord.Game('Finding a star!'))

@bot.event
async def on_message(message):
    # id = message.id
    global send_message
    if message.content in ban_pto:
        await message.delete()
        channel = bot.get_channel(804006192376315947)
        await channel.send(random_complain)

bot.run(bot_token)
