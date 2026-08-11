import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
from pathlib import Path
import time

BASE_DIR = Path(__file__).parent

User_choice = input("what year song u would like to listen? format:year('YYYY')")

url = f"https://gaana.com/playlist/gaana-dj-catch-up-{User_choice}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

response = requests.get(url=url,headers=headers)
response.raise_for_status()
print(response.status_code)
contents = response.text

soup = BeautifulSoup(contents,"html.parser")
songs = [song.getText() for song in soup.select(".tabContTxtTrack strong a")]

yt = YTMusic(str(BASE_DIR/"browser.json"))

# Verify authentication works
playlists = yt.get_library_playlists()
print(f"Found {len(playlists)} playlists in your library.")

PLAYLIST_NAME = f"{User_choice} trendy songs"

# Check if playlist already exists
playlist_id = None
playlists = yt.get_library_playlists(limit=100)

for p in playlists:
    if p["title"] == PLAYLIST_NAME:
        playlist_id = p["playlistId"]
        break

if playlist_id:
    print("This playlist already exists.")
else:
    playlist_id = yt.create_playlist(
        PLAYLIST_NAME,
        f"Playlist with the hottest songs from {User_choice}",
        privacy_status="PRIVATE",
    )
    print("Playlist created.")

for song in songs:
    try:
        search_song = yt.search(song,filter="songs",limit=1)
        yt.add_playlist_items(playlist_id, [search_song[0]["videoId"]])
        print(f"added song: {song}")
    except Exception as e:
        print(f"{song} song was unable to add because of {e}")
    time.sleep(2)
    

