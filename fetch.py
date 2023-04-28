import json  # to make this into a json file
import requests
from bs4 import BeautifulSoup as bs4

quotes = []

x = 1
fresh = True
for page in range(1, 30):
    url = "https://www.goodreads.com/author/quotes/5237.Hunter_S_Thompson?page=" + \
        str(page)
    response = requests.get(url)
    soup = bs4(response.text, "html.parser")

    # Get all the divs with the quotes on this page
    quote_divs = soup.find_all("div", {"class": "quoteText"})

    for div in quote_divs:
        # for some reason this weird dash which I can't seem to find on my keyboard is the correct spacing. Ok update I found that it is called the em dash. Also this is not the first time I am hearing about this, I have a sense of deja vu about this.
        quoteText = div.text.strip().split('―')[0].strip()
        quoteText = quoteText[1:-1]
        # unable to put the ― em dash here as it's not going to (probably) the json correctly. Using hyphen instead
        quoteText = quoteText.replace("\u2014", "-")

        # get text from the spans
        spans = div.find_all("span")
        spanText = []
        for span in spans:
            spanText.append(span.text)
        author = spanText[0]
        title = "" if len(spanText) < 2 else spanText[-1].strip()
        quote = {
            "quote": quoteText,
            "author": spanText[0].strip().replace(",", ""),
            "title": title
        }
        quotes.append(quote)
        x += 1
        if x > 2:
            break  # here to limit while checking, remove later
    break  # here for now while I just check, remove later

# Clear the json file first
with open("quotes.json", "w") as outfile:
    json.dump(quotes, outfile)
