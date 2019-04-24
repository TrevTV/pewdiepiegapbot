from discord.ext import commands
from config import Config
import urllib.request
import importlib
import discord
import count
import time
import json

cfg = Config(open('config.cfg'))

class util(commands.Cog, name='Utilities'):
    def __init__(self, client):
        self.client = client
        self.client.remove_command("help")

    @commands.command()
    async def gap(self, ctx):
        importlib.reload(count)
        print("Sending the gap to chat")
        await ctx.send('The gap is currently at' + ' ' + str(count.a) + "!")

    @commands.command(pass_context=True)
    async def help(self, ctx):
        author = ctx.message.author
        try:
            embed=discord.Embed(title="Commands", description="Here are the commands:", color=0xF9013F)
            embed.add_field(name="!help", value="What do you think?", inline=True)
            embed.add_field(name="!gap", value="Displays the gap between PewDiePie and T-Series.", inline= True)
            embed.add_field(name="!subcount {youtuber}", value="Displays the subscriber count of a specified YouTuber.", inline= True)
            embed.add_field(name="!meme", value="Displays a meme from reddit.", inline= True)
            embed.add_field(name="!trump", value="Displays a dumb trump quote.", inline= True)
            embed.add_field(name="!urban {word}", value="Searches the Urban Dictionary for a specified word. Only works in NSFW channels.", inline= True)
            embed.add_field(name="!owo {text}", value="Turns english into owo.", inline= True)
            embed.add_field(name="!trivia", value="Gives you a true or false trivia question.", inline= True)
            embed.set_footer(text="See full list of commands at gaplk.gq")
            await author.send(embed=embed)
            print("Sent commands to " + str(author))
            await ctx.send("The command list has been sent to your PMs.")
        except:
            await ctx.send(embed=embed)
            print("Sent help to chat.")

    @commands.command()
    async def subcount(self, ctx, sarg):
        key = cfg.ytapi
        yt = sarg
        pp = 0
        data = urllib.request.urlopen(
                "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + str(yt) + "&key=" + cfg.ytapi).read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        pp = "{:,d}".format(int(subs))
        pp = pp.replace(',', '')
        pp = int(pp)
        await ctx.send(str(yt) + " " + 'is currently at' + " " + str(pp) + " " + 'subscribers.')
        print('Sending' + " " + yt + "'s" + " subcount" + " to chat")


def setup(client):
    client.add_cog(util(client))
