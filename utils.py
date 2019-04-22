from discord.ext import commands
from config import Config
import urllib.request
import importlib
import discord
import count
import json

cfg = Config(open('config.cfg'))

class util:
    def __init__(self, client):
        self.client = client
        self.client.remove_command("help")

    @commands.command()
    async def gap(self):
        importlib.reload(count)
        print("Sending the gap to chat")
        await self.client.say('The gap is currently at' + ' ' + str(count.a) + "!")

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
            embed.add_field(name="!quickpoll {title} {option} {option}", value="Starts a poll, it can have more than two options", inline= True)
            embed.add_field(name="!tally {pollid}", value="Tallys votes from a poll.", inline= True)
            embed.add_field(name="!urban {word}", value="Searches the Urban Dictionary for a specified word.", inline= True)
			embed.add_field(name="!owo {sentence}", value="Turns the sentence into owo talk.", inline= True)
            await self.client.send_message(author, embed=embed)
            print("Sent commands to " + str(author))
            await self.client.say("The command list has been sent to your PMs.")
        except:
            await self.client.say(embed=embed)

    @commands.command()
    async def subcount(self, sarg):
        key = "AIzaSyASRlUYVQPbu15YC_tRFG5TfBx8Vwdi4fg"
        yt = sarg
        pp = 0
        data = urllib.request.urlopen(
                "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=" + str(yt) + "&key=" + cfg.ytapi).read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        pp = "{:,d}".format(int(subs))
        pp = pp.replace(',', '')
        pp = int(pp)
        await self.client.say(str(yt) + " " + 'is currently at' + " " + str(pp) + " " + 'subscribers.')
        print('Sending' + " " + yt + "'s" + " subcount" + " to chat")


def setup(client):
    client.add_cog(util(client))
