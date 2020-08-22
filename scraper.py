from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request

# TODO: Check the following as a path for improvement
# http://www.tulane.edu/~howard/NLP/webpages.html

def text_visible(element):
  unwanted_tags = ['style', 'script', 'head', 'title', 'meta', '[document]']
  return not (element.parent.name in unwanted_tags or isinstance(element, Comment))


def extract_html(body):
  soup = BeautifulSoup(body, 'html.parser')
  texts = soup.find_all(text=True)
  visible_texts = filter(text_visible, texts)  
  return u" ".join(t.strip() for t in visible_texts)

def open_extract(url: str) -> str:
  try:
    html = urllib.request.urlopen(url).read()
  except:
    return "I couldn't reach the site"
  return extract_html(html)
