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

class DiscordClientPublisher(discord.Client):
  def __call__(self,
      channel_id: int = None,
      scraper: StringValued = None,
      summarizer: StringValued = None):
    """Setup these callables as listeners, for when a message
    is recieved."""
    
    # ensure we have all listeners we need 
    if not all((channel_id, scraper, summarizer)):
      raise ValueError("Called with insufficient arguments")

    self.scraper    = scraper
    self.summarizer = summarizer
    self.CH_ID      = channel_id

    # return statement to chain into clientInstance(...).run(TOKEN)
    return self

  async def on_ready(self):
    """This is triggered when the bot is joins the chat"""
    channel = self.get_channel(self.CH_ID)
    await channel.send(f'Hello, the time is {human_readable_time_now()}')
    logging.info(f'{self.user.name} has connected to Discord!')
  
  async def on_message(self, message):
    """This is triggered when a message is sent to the channel in CHANNEL_ID"""
    if message.author == self.user:
      return
      
    message_text = message.content
    extractor    = URLExtract()
    urls         = extractor.find_urls(message_text)

    if not urls:
      logging.info('No urls were passed.')
      return

    if len(urls) > 1:
      logging.info('Too many urls were passed.')
      return

    # grab the url, get the article text, and summarized
    (url,) = urls
    logging.info(f'{url} was passed.')
    article_text = self.scraper(url)
    
    summary = self.summarizer(article_text)

    await message.channel.send(summary)
    
