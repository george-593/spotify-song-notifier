from functools import partial
from mac_notifications import client
from spotify_api import SpotifyAPI

from models.current_track import CurrentTrack


class Notifications:
    def __init__(self, spotify: SpotifyAPI):
        self.spotify = spotify

    def send_notification(self, previous_track, current_track: CurrentTrack) -> None:
        notification = client.create_notification(
            title="New Song Playing",
            text=f"Previous Song: {previous_track.name} by {previous_track.artist}\nCurrent Song: {current_track.name} by {current_track.artist}",
            action_button_str="Add previous to Playlist",
            action_callback=partial(
                self.notification_add_callback, track=previous_track
            ),
        )
        print(f"Notification queued with id: {notification.uid}")

    def notification_add_callback(self, track):
        print("Callback received")
        self.spotify.add_to_playlist(track)
