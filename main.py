import os

from client_class import DiscordClientPublisher
from summarizer import NeuralTextSummarizer
from scraper import open_extract
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CH_ID = int(str(os.getenv('BOT_CHANNEL')))

nts_listener = NeuralTextSummarizer()
client = DiscordClientPublisher()

#client(
#  channel_id=CH_ID,
#  summarizer=nts_listener.summarize,
#  scraper=open_extract).run(TOKEN)

while True:
  url = input()
  article_text = open_extract(url)
  summary = nts_listener.summarize(article_text)
  print(summary)
