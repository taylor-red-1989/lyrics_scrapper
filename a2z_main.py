import requests
from bs4 import BeautifulSoup
import re


def fetchandsave(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://www.azlyrics.com/t/taylorswift.html#33536"
    fetchandsave(url, "artist_page.html")

    with open("artist_page.html", "r", encoding="utf-8") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    with open("full_songs_link_list.html", "w") as f:
        pass

    with open("full_songs_link_list.html", "a") as f:
        for link in soup.find_all("a"):
            if re.search(r'\/lyrics\/', str(link.get("href"))):
                f.write(str(link.get("href")) + "\n")

    with open("full_songs_name_list.html", "w") as f:
        pass

    with open("full_songs_name_list.html", "a") as f:
        for link in soup.find_all("a"):
            if re.search(r'\/lyrics\/', str(link.get("href"))):
                f.write(str(link.text) + "\n")

    with open("full_songs_link_list.html", "r") as f:
        song_number = int(input("Enter song number: "))
        for links in f.readlines()[song_number - 1:song_number]:
            fetchandsave("https://www.azlyrics.com" + links.strip(), "lyric_page.html")

    with open("lyric_page.html", "r", encoding="utf-8") as f:
        html_doc = f.read()

    soup = BeautifulSoup(str(BeautifulSoup(html_doc, 'html.parser').find_all("div", class_="")), 'html.parser')

    with open('full_songs_name_list.html', 'r') as file:
        song_name = "_".join(next((line for i, line in enumerate(file, 1) if i == song_number), None).split())

    with open(song_name+".txt", "w") as f:
        pass

    with open(song_name+".txt", "a") as f:
        f.write(soup.text[10:-8])
