import spotipy
from spotipy.oauth2 import SpotifyOAuth

from models.current_track import CurrentTrack


class SpotifyAPI:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id

        self.scope = "playlist-read-private playlist-read-collaborative playlist-modify-private playlist-modify-public"
        self.spotipy = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope))

    def add_to_playlist(self, track: CurrentTrack):
        if self.playlist_id is None:
            # Change this to a notification?
            print("Playlist ID is not set. Cannot add track to playlist")
            return

        print(track.uri)
        result = self.spotipy.playlist_add_items(self.playlist_id, [track.uri])
        print(result)
