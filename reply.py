from discord.ext import commands
import urllib.request
import importlib
import discord
import count
import json
yt = 'null'

client = commands.Bot(command_prefix='!')

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
    await client.say('The gap is currently at' + ' ' + str(count.a) + "!")

client.remove_command("help")

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    try:
        embed=discord.Embed(title="Commands", description="Here are the commands:", color=0xF9013F)
        embed.add_field(name="!help", value="What do you think?", inline=True)
        embed.add_field(name="!gap", value="Displays the gap between PewDiePie and T-Series.", inline= True)
        embed.add_field(name="!subcount {youtuber}", value="Displays the subscriber count of a specified YouTuber.", inline= True)
        embed.add_field(name="!meme", value="Displays a meme from reddit.", inline= True)
        embed.add_field(name="!trump", value="Displays a dumb trump quote.", inline= True)
        await client.send_message(author, embed=embed)
        print("Sent commands to " + str(author))
        await client.say("The command list has been sent to your PMs.")
    except:
        await client.say("It seems that you have disabled private messages to server members. I cannot send the list without that permission.")
        print("Failed sending commands to " + str(author))

sarg = "impropercmdusage"
@client.command()
async def subcount(sarg):
        key = "youtube api v3 key here"
        yt = sarg
        pp = 0
        data = urllib.request.urlopen(
            "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + str(yt) + "&key=" + key).read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        pp = "{:,d}".format(int(subs))
        pp = pp.replace(',', '')
        pp = int(pp)
        await client.say(str(yt) + " " + 'is currently at' + " " + str(pp) + " " + 'subscribers.')
        print('Sending' + " " + yt + "'s" + " subcount" + " to chat")


@client.command()
async def meme():
    memedata = urllib.request.urlopen("https://meme-api.herokuapp.com/gimme").read()
    memeu = json.loads(memedata)["url"]
    memet = json.loads(memedata)["title"]
    print('Sending meme to chat')
    memee=discord.Embed(title=memet, description="meme review :clap: :clap:", color=0xF9013F)
    memee.set_image(url=memeu)
    await client.say(embed=memee)

@client.command()
async def trump():
    quotedata = urllib.request.urlopen("https://api.whatdoestrumpthink.com/api/v1/quotes/random").read()
    quote = json.loads(quotedata)["message"]
    print("Sending Trump quote to chat")
    await client.say("Dumb Trump quote on the way!" + " " + '"' + quote + '"')


client.run('token here')
