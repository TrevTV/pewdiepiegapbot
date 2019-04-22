from discord.ext import commands
import urllib.request
import discord
import json

class fun:
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def urban(self, arg):
        t = arg
        term = urllib.request.urlopen("http://api.urbandictionary.com/v0/define?term=" + str(t)).read()
        defi = json.loads(term)["list"][0]["definition"]
        word = json.loads(term)["list"][0]["word"]
        exam = json.loads(term)["list"][0]["example"]
        embed = discord.Embed(title=word, description="Definition: " + defi + "\n \n Example: " + exam, color=0xF9013F)
        await self.client.say(embed=embed)
        print("Sending urban definition of " + t + " to chat.")

    @commands.command()
    async def trump(self):
        quotedata = urllib.request.urlopen("https://api.whatdoestrumpthink.com/api/v1/quotes/random").read()
        quote = json.loads(quotedata)["message"]
        embed = discord.Embed(title="Dumb Trump Quote!", description='"' + quote + '"', color=0xF9013F)
        embed.set_image(url='https://cdn.theatlantic.com/assets/media/img/mt/2016/09/RTX1GZCO/lead_720_405.jpg?mod=1533691850')
        await self.client.say(embed=embed)
        print("Sending Trump quote to chat")

    @commands.command()
    async def meme(self):
        memedata = urllib.request.urlopen("https://meme-api.herokuapp.com/gimme").read()
        memeu = json.loads(memedata)["url"]
        memet = json.loads(memedata)["title"]
        memee=discord.Embed(title=memet, description="meme review :clap: :clap:", color=0xF9013F)
        memee.set_image(url=memeu)
        await self.client.say(embed=memee)
        print('Sending meme to chat')

    @commands.command()
    async def owo(self, *, arg):
        from TextToOwO import owo
        tahowo = owo.text_to_owo(arg)
        await self.client.say(tahowo)
        print("Owooing " + arg)


def setup(client):
    client.add_cog(fun(client))
