import re
import requests
from bs4 import BeautifulSoup as bs

link_front = "https://yugioh.fandom.com"

def get_card_text(url):
    print(url)
    request = requests.get(url)
    html = request.text
    soup = bs(html)
    # get the card text
    card_text = soup.select('table.collapsible.expanded.navbox-inner td:nth-of-type(1)')[1].text
    card_text = card_text.strip()
    return card_text

