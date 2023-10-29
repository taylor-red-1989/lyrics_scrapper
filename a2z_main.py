import requests
from bs4 import BeautifulSoup
import re

def fetchandSave(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)


url = "https://www.azlyrics.com/t/taylorswift.html#33536"
fetchandSave(url, "page.html")


with open("page.html", "r", encoding="utf-8") as f:
    html_doc = f.read()


soup = BeautifulSoup(html_doc, 'html.parser')


with open("lyrics_pages.html", "w") as f:
    pass

with open("lyrics_pages.html", "a") as f:
    for link in soup.find_all("a"):
        if re.search(r'\/lyrics\/', str(link.get("href"))):
            f.write(str(link.text) + " = " + str(link.get("href")) + "\n")
