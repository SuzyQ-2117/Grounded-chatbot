# handles the Fandom API calls - this is the bot's knowledge fetcher

# function for extracting page title into a string
# use requests package to hit the fandom api
# action=query, prop=extracts, format=json
# parse and return the intro extract

import requests
from bs4 import BeautifulSoup

from app.config import WIKI_API_URL

def get_page_extract(title: str) -> str:
    params = {
        "action": "parse",
        "page": title,
        "format": "json",
        "prop": "text"
    }

    response = requests.get(WIKI_API_URL, params=params)
    data = response.json()

    try: 
        raw_html = data["parse"]["text"]["*"]
        soup = BeautifulSoup(raw_html, "html.parser")

        paragraphs = soup.findAll("p")
        # print(f"Found {paragraphs} paragraphs")

        for p in soup.find_all("p"):
            text = p.get_text(strip=True)
            if text and len(text) > 50:  # You can tweak the length filter
                return text

        return "No readable wiki paragraph found."

    except Exception as e:
        print(f"Wiki fetch error: {e}")
        return "No wiki data found."