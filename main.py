import time

from applescript import Applescript
import exceptions
from notifications import Notifications


class Main:
    def __init__(self):
        self.applescript = Applescript()
        self.notifications = Notifications()
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
                    and current_track.url != self.previous_track.url
                ):
                    # We have a new song playing!
                    print("New song!")
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


if __name__ == "__main__":
    Main().main()
