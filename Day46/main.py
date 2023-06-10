import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get('https://www.billboard.com/charts/hot-100/' + date_input+'/')
billboard = response.text

soup = BeautifulSoup(billboard, 'html.parser')
billboard_100_titles = soup.select("li #title-of-a-story")
song_names = [title.getText().strip('\n\t') for title in billboard_100_titles]
print(song_names)



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="{insert client_id}",
                                               client_secret="{insert client_secret}",
                                               show_dialog=False,
                                               cache_path="token.txt",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-library-read playlist-modify-private"))


results = sp.current_user()
user_id = results['id']
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date_input.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date_input} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
