from discord.ext import commands
import urllib.request
import discord
import json

class fun(commands.Cog, name='Fun'):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def urban(self, ctx, *, arg):
        word = arg.replace(" ", "+")
        term = urllib.request.urlopen("http://api.urbandictionary.com/v0/define?term=" + str(word)).read()
        defi = json.loads(term)["list"][0]["definition"]
        word = json.loads(term)["list"][0]["word"]
        exam = json.loads(term)["list"][0]["example"]
        if ctx.channel.is_nsfw():
            embed = discord.Embed(title=word, description="Definition: " + defi + "\n \n Example: " + exam, color=0xF9013F)
            await ctx.send(embed=embed)
            print("Sending urban definition of " + arg + " to chat.")
        else:
            await ctx.send("Due to the nature of the Urban Dictionary this command only works in nsfw channels.")

    @commands.command()
    async def trump(self, ctx):
        quotedata = urllib.request.urlopen("https://api.whatdoestrumpthink.com/api/v1/quotes/random").read()
        quote = json.loads(quotedata)["message"]
        embed = discord.Embed(title="Dumb Trump Quote!", description='"' + quote + '"', color=0xF9013F)
        embed.set_image(url='https://cdn.theatlantic.com/assets/media/img/mt/2016/09/RTX1GZCO/lead_720_405.jpg?mod=1533691850')
        await ctx.send(embed=embed)
        print("Sending Trump quote to chat")

    @commands.command()
    async def meme(self, ctx):
        memedata = urllib.request.urlopen("https://meme-api.herokuapp.com/gimme").read()
        memeu = json.loads(memedata)["url"]
        memet = json.loads(memedata)["title"]
        memee=discord.Embed(title=memet, description="meme review :clap: :clap:", color=0xF9013F)
        memee.set_image(url=memeu)
        await ctx.send(embed=memee)
        print('Sending meme to chat')

    @commands.command()
    async def owo(self, ctx, *, arg):
        from TextToOwO import owo
        tahowo = owo.text_to_owo(arg)
        await ctx.send(tahowo)
        print("Owooing " + arg)

    @commands.command()
    async def trivia(self, ctx):
        triv = urllib.request.urlopen("https://opentdb.com/api.php?amount=1&difficulty=medium&type=boolean").read()
        question = json.loads(triv)['results'][0]['question']
        answer = json.loads(triv)['results'][0]['correct_answer']
        question = question.replace('&#039;', "'")
        question = question.replace('&quot;', '"')
        question = question.replace('&minus;', "-")
        embed=discord.Embed(title="Trivia", description="True or False? " + question, color=0xF9013F)
        await ctx.send(embed=embed)
        print("Sent trivia question to chat.")
        msg = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
        if msg:
            while msg.content.lower() not in ['true', 'false']:
                await ctx.send("Please only choose true or false.")
            if msg.content.lower() == answer.lower():
                await ctx.send('Correct!')
            elif msg.content.lower() != answer.lower():
                await ctx.send('Incorrect. The correct answer was ' + answer.lower() + ".")

    @commands.command()
    async def echo(self, ctx, *, arg):
        await ctx.send(arg)

    @commands.command()
    async def clapify(self, ctx, *, arg):
        clap = arg.replace(" ", "👏")
        await ctx.send(clap)

    @commands.command()
    async def cat(self, ctx):
        cat = urllib.request.urlopen("http://aws.random.cat/meow").read()
        cati = json.loads(cat)['file']
        cat=discord.Embed(title='Random Cat', description="Cats are cute.", color=0xF9013F)
        cat.set_image(url=cati)
        await ctx.send(embed=cat)

    @commands.command()
    async def lenny(self, ctx):
        lenny = urllib.request.urlopen("https://api.lenny.today/v1/random?limit=1").read()
        lenni = json.loads(lenny)[0]['face']
        await ctx.send(lenni)


def setup(client):
    client.add_cog(fun(client))
