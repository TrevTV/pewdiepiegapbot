import discord
import importlib
import count


client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!gap'):
        importlib.reload(count)
        msg = 'The gap is currently at' + ' ' + str(count.a)
        repr(msg)
    await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='people type !gap', type = 3))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Bot Online!')
    print('------')

client.run('but your token here')

