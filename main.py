from client_class import DiscordClientObserver
from summarizer import NeuralTextSummarizer
from scraper import open_extract

import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CH_ID = int(str(os.getenv('BOT_CHANNEL')))

nts = NeuralTextSummarizer()
client = DiscordClientObserver()

client(
  channel_id=CH_ID,
  summarizer=nts.summarize,
  scraper=open_extract).run(TOKEN)
