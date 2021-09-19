# Search for a a song by its lyrics. Will find the song using the Genius API and add that song to your saved tracks using the Spotify API

import lyricsgenius
import spotipy
from spotipy.oauth2 import SpotifyOAuth


genius = lyricsgenius.Genius("8GC4daouq1qHKUuH7FHAlL6mM4TbKdavUtTkvVd8kQIKdraxffPpKrYoWj52PxF7")


lyrics_to_search = input()

request = genius.search_genius_web(lyrics_to_search)


song = request['sections'][0]['hits'][0]['result']['title']
artist = request['sections'][0]['hits'][0]['result']['primary_artist']['name']

print(song)
print(artist)

"""
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = "59a69adac6544298bf4b976c001f0310",
client_secret = "0557f90b87eb404ebae99e8cd4ac6519"), redirect_uri = "http://localhost:8765/callback", scope = "user-library-read")

results = sp.search(q = 'song')
"""