import requests
from bs4 import BeautifulSoup


req = requests.get(url)
article_page = req.content

soup = BeatifulSoup(article_page, 'html5lib')
