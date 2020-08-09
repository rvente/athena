import os

import discord
import time
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    channel = client.get_channel(741893621778874390)
    await channel.send('hello')
    print(f'{client.user.name} has connected to Discord!')


client.run(TOKEN)