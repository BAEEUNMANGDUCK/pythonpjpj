import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

SCOPE = os.getenv("SCOPE")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SPORTIFY_URI = os.getenv("SPORTIFY_URI")

music_data = input('which year do you want to travel to?')
YEAR = music_data.split('-')[0]
URL = f"https://www.billboard.com/charts/hot-100/{music_data}"
print(URL)

response = requests.get(url=URL)
billboard_html =response.text

soup = BeautifulSoup(billboard_html, 'html.parser')


musics = soup.select(selector="li h3#title-of-a-story")

top_100 = []
for music in musics:
    music_title = music.string.replace('\n',"").replace('\t',"")
    top_100.append(music_title)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                scope=SCOPE,
                                                redirect_uri=REDIRECT_URI,
                                                show_dialog=True,
                                                cache_path="token.txt"))



user_id = sp.current_user()['id']

playlist_id = sp.user_playlist_create(user=user_id, name=f"{music_data} Billboard 100", public=False, collaborative=False, description='made by Eunbae')['id']

song_list = []
for song in top_100:
    try:
        results = sp.search(q=f'track: {song} year: {YEAR}')
    except:
        pass
    else:
        track = results['tracks']['items'][0]['uri']
        song_list.append(track)

# track 안에 들어갈 데이터 형식은 array(list)형식이어야 한다!
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=song_list)       