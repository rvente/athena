from urlextract import URLExtract
import os
import discord
import time
import datetime

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CH_ID = int(str(os.getenv('BOT_CHANNEL')))

import logging
logging.basicConfig(
  level=logging.INFO,
  handlers=[logging.FileHandler('filename.log'), logging.StreamHandler()],
  format='%(name)s - %(levelname)s - %(message)s')

def human_readable_time_now():
    timestamp = time.time()
    return datetime.datetime.fromtimestamp(timestamp)

class ScraperBot(discord.Client):
    def run_bot(self):
      self.run(TOKEN)

    async def on_ready(self):
        channel = self.get_channel(CH_ID)
        await channel.send(f'Hello, the time is {human_readable_time_now()}')
        logging.info(f'{self.user.name} has connected to Discord!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        extractor = URLExtract()
        urls = extractor.find_urls(message.content)
        logging.info(urls)
        await message.channel.send(" ".join(urls))
