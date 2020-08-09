from bs4 import BeautifulSoup
import requests

URL = 'https://google.com'
page = requests.get(URL)
print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())