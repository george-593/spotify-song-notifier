import rumps
import time
import exceptions
import os
from dotenv import load_dotenv

from applescript import Applescript
from notifications import Notifications
from spotify_api import SpotifyAPI


class SpotifyNotifierApp(rumps.App):
    def __init__(self):
        super(SpotifyNotifierApp, self).__init__("🎵")

        # Track Monitoring
        load_dotenv()

        self.playlist_id = os.getenv("SPOTIFY_PLAYLIST_ID")

        self.applescript = Applescript()
        self.spotify = SpotifyAPI(self.playlist_id)
        self.notifications = Notifications(self.spotify)
        self.track = None

        self.wait_time = 1
        self.last_time = 0

        # RUMPS Menu
        self.track_item = rumps.MenuItem("No Track")

        self.menu = [self.track_item]

    def on_track_change(self, current_track):
        self.track_item.title = f"{current_track.name} by {current_track.artist}"
        self.notifications.send_notification(self.track, current_track)

    @rumps.timer(1)
    def monitor_spotify(self, sender):

        # Return early if wait_time is > 1 and we havent reached that limit yet
        now = time.time()
        if self.wait_time > 1 and now - self.last_time < self.wait_time:
            return
        self.last_time = now

        self.wait_time = 1
        # Use applescript to monitor spotify - do thing when track changes
        try:
            current_track = self.applescript.get_current_track()
            print(
                f"{current_track.name} time remaining: {current_track.time_remaining}"
            )
            if self.track is not None and current_track.uri != self.track.uri:
                # We have a new song playing!
                print("New song detected")
                self.on_track_change(current_track)

            self.track = current_track
        except exceptions.SpotifyNotRunningError:
            print("Spotify is not running, trying again in 10s")
            self.wait_time = 10
        except Exception as e:
            print(f"Unable to get track: {e}")
            self.wait_time = 10


if __name__ == "__main__":
    app = SpotifyNotifierApp()
    app.run()
