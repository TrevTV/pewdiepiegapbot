from discord.ext import commands
from config import Config
import discord


cfg = Config(open('config.cfg'))
client = commands.Bot(command_prefix=cfg.prefix)
extensions = ['fun', 'utils']


@client.event
async def on_command_error(error, ctx):
	if isinstance(error, commands.MissingRequiredArgument):
		embed=discord.Embed(title="Incorrect Usage", description="Please use !help to find out how to use that command.", color=0xF9013F)
		await ctx.send(embed=embed)



@client.event
async def on_ready():
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
