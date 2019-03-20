import discord
from discord.ext import commands
import importlib
import urllib.request
import json
import count
players = {}
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


@client.command(pass_context=True)
async def commands(ctx):
    author = ctx.message.author
    await client.send_message(author, "Current Commands: \n !gap : Displays the gap between PewDiePie and T-Series. \n "
                                      "!subcount {youtuber} : Can display the subscriber count of a specified YouTuber."
                                      "\n !meme : Displays a meme from reddit. \n \n !play {youtube url} : Can play mus"
                                      "ic to channel (must already be in voice channel). \n !leave : Makes bot leave it"
                                      "s current voice channel. \n !pause : Pauses currently playing music. \n !resu"
                                      "me : Resumes currently paused music.")
    await client.say("You should have received it in a private message. If you do not see it you have have direct mess"
                     "ages from users disabled.")


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

# MUSIC BOT PART #
# NOTE: MUST HAVE FFMPEG INSTALLED FOR THE MUSIC BOT TO WORK #


@client.command(pass_context=True)
async def play(ctx, url):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()
    print("Bot has started playing music in a channel")


@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    print("Bot has left a channel")


@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()


@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

# END OF MUSIC BOT #


client.run('put your discord bot token here')

