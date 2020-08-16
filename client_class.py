import logging
import warnings
from urlextract import URLExtract
from typing import Callable, List
import discord
import time
import datetime

logging.basicConfig(
  level=logging.INFO,
  handlers=[logging.FileHandler('filename.log'), logging.StreamHandler()],
  format='%(name)s - %(levelname)s - %(message)s')

def human_readable_time_now():
  timestamp = time.time()
  return datetime.datetime.fromtimestamp(timestamp)

StringValued = Callable[[str],str]

class DiscordClientObserver(discord.Client):
  def __call__(self,
      channel_id: int = None,
      scraper: StringValued=None,
      summarizer: StringValued=None):
    if not all((channel_id, scraper, summarizer)):
      raise ValueError("Called with insufficient arguments")

    self.scraper = scraper
    self.summarizer = summarizer
    self.CH_ID = channel_id
    return self

  async def on_ready(self):
    channel = self.get_channel(self.CH_ID)
    await channel.send(f'Hello, the time is {human_readable_time_now()}')
    logging.info(f'{self.user.name} has connected to Discord!')
  
  async def on_message(self, message):
    if message.author == self.user:
      return
      
    message_text = message.content
    extractor = URLExtract()
    urls = extractor.find_urls(message_text)

    if not urls:
      return

    if len(urls) > 1:
      return

    (url,) = urls
    article_text = self.scraper(url)
    
    summary = self.summarizer(article_text)
    print(article_text, summary)
    await message.channel.send(summary)
    
