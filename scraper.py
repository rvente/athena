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
    html = urllib.request.urlopen('http://www.nytimes.com/2009/12/21/us/21storm.html').read()
  except:
    print("I couldn't reach the site")
    pass
  return extract_html(html)
