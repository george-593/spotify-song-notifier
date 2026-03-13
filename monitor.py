import time
import exceptions
import os
from dotenv import load_dotenv

from applescript import Applescript
from notifications import Notifications
from spotify_api import SpotifyAPI


class Monitor:
    def __init__(self):
        load_dotenv()

        self.playlist_id = os.getenv("SPOTIFY_PLAYLIST_ID")

        self.applescript = Applescript()
        self.spotify = SpotifyAPI(self.playlist_id)
        self.notifications = Notifications(self.spotify)
        self.previous_track = None

    def trigger_track_change(self):
        pass

    def main(self):
        while True:
            # Main Loop
            wait_time = 1

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
                    self.notifications.send_notification(
                        self.previous_track, current_track
                    )

                self.previous_track = current_track
            except exceptions.SpotifyNotRunningError:
                print("Spotify is not running, trying again in 10s")
                wait_time = 10
            except Exception as e:
                print(f"Unable to get track: {e}")
                wait_time = 10

            time.sleep(wait_time)


# To run the application without taskbar
if __name__ == "__main__":
    Monitor().main()
