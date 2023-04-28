import json  # to make this into a json file
import requests
from bs4 import BeautifulSoup as bs4

# Clear the json file first
with open("quotes.json", "w") as outfile:
    pass  # Do nothing - this will clear the file

quotes = []

for page in range(1, 30):
    url = "https://www.goodreads.com/author/quotes/5237.Hunter_S_Thompson?page=" + \
        str(page)
    response = requests.get(url)
    soup = bs4(response.text, "html.parser")

    # Get all the divs with the quotes on this page
    quote_divs = soup.find_all("div", {"class": "quoteText"})

    for div in quote_divs:
        # for some reason this weird dash which I can't seem to find on my keyboard is the correct spacing.
        full = []
        for by_dash in div.text.strip().split('―'):
            full.extend(by_dash.split(","))
        quote = {
            "quote": full[0],
            "authorOrTitle": full[-min(len(full)-1, 2):]
        }

        break  # here for checking, remove later
    break  # here for now while I just check, remove later
