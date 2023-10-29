import requests
from bs4 import BeautifulSoup
import os

def fetchandSave(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

def get_url(track):
	with open("lyrics_pages.html", "r") as file:
		text = file.readlines()
		return text[track]

def create_lyrics_file(url, path):
	response = requests.get(url)

	with open(path, "w") as f:
		print("Getting Lyrics for", path.strip(".txt"))
		pass

	soup = BeautifulSoup(response.content, "html.parser")
	for div_x in soup.find_all("div", class_='Lyrics__Container-sc-1ynbvzw-1 kUgSbL'):
		with open(path, "a", encoding="utf-8") as f:
			f.write(div_x.get_text(separator='\n')+"\n\n")

with open("lyrics_pages.html", "r") as file:
	number_of_tracks = len(file.readlines())

album_name = input("Enter album name: ")
if not os.path.exists(album_name):
    os.makedirs(album_name)

for track in range(number_of_tracks-1):
	url = get_url(track).strip()
	path = str(track+1) + ". " + "_".join(url[19:].split("-")[2:]).strip()+".txt"
	create_lyrics_file(url, album_name+"/"+path)