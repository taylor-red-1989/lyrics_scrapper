import requests
from bs4 import BeautifulSoup


def fetchandSave(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)
    
    
url = input("Enter url: ")
fetchandSave(url, "page.html")


with open("page.html", "r", encoding="utf-8") as f:
    html_doc = f.read()


soup = BeautifulSoup(html_doc, 'html.parser')


with open("lyrics_pages.html", "w") as f:
    pass


with open("lyrics_pages.html", "a") as f:
    for link in soup.find_all("a", class_='u-display_block'):
        f.write(link.get("href") + "\n")
