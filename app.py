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
        load_dotenv()

        self.playlist_id = os.getenv("SPOTIFY_PLAYLIST_ID")

        self.applescript = Applescript()
        self.spotify = SpotifyAPI(self.playlist_id)
        self.notifications = Notifications(self.spotify)
        self.previous_track = None

        self.wait_time = 1
        self.last_time = 0

    @rumps.timer(1)
    def monitor(self, sender):

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
            if (
                self.previous_track is not None
                and current_track.uri != self.previous_track.uri
            ):
                # We have a new song playing!
                print("New song detected")
                self.notifications.send_notification(self.previous_track, current_track)
            self.previous_track = current_track
        except exceptions.SpotifyNotRunningError:
            print("Spotify is not running, trying again in 10s")
            self.wait_time = 10
        except Exception as e:
            print(f"Unable to get track: {e}")
            self.wait_time = 10

    def quit_app(self, sender):
        rumps.quit_application()


if __name__ == "__main__":
    app = SpotifyNotifierApp()
    app.run()
