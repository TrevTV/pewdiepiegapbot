from discord.ext import commands
from config import Config
import urllib.request
import importlib
import discord
import json


cfg = Config(open('config.cfg'))
client = commands.Bot(command_prefix=cfg.prefix)
extensions = ['quickpoll', 'fun', 'utils']


@client.event
async def on_command_error(error, ctx):
    channel = ctx.message.channel
    author = ctx.message.author.mention
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Incorrect Usage", description="Please use !help to find out how to use that command.", color=0xF9013F)
        await client.send_message(channel, embed=embed)
		

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='people type !gap', type = 3))
    print('Discord.py Version: ' + discord.__version__ )
    print("{} Online".format(client.user.name))
    print('-----------')


if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))


client.run(cfg.token)
