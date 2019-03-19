import discord
from discord.ext import commands
import importlib
import urllib.request
import json
import count
pp = 0
yt = 'null'
if count.p > count.t:
    w = "PewDiePie"
else:
    w = "T-Series"


client = commands.Bot(command_prefix='!')

# Startup


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='people type !gap', type = 3))
    print('Bot Online!')
    print('-----------')

# Commands


@client.command()
async def gap():
    importlib.reload(count)
    print("Sending the gap to chat")
    await client.say('The gap is currently at' + ' ' + str(count.a) + " " + 'with' + " " + str(w) + " " + "winning!")


@client.command()
async def subcount(arg):
    key = "put your google api key here"
    yt = arg
    data = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + str(yt) + "&key=" + key).read()
    subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    pp = "{:,d}".format(int(subs))
    pp = pp.replace(',', '')
    pp = int(pp)
    print('Sending' + " " + yt + "'s" + " " + "to chat")
    await client.say(str(yt) + " " + 'is currently at' + " " + str(pp) + " " + 'subscribers.')


@client.command()
async def meme():
    data = urllib.request.urlopen("https://meme-api.herokuapp.com/gimme").read()
    meme = json.loads(data)["url"]
    print('Sending meme to chat')
    await client.say("meme review :clap: :clap:" + " " + meme)


client.run('put your token here')

