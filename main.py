import time

from applescript import Applescript


class Main:
    def __init__(self):
        self.applescript = Applescript()
        self.previous_track = None
        self.main()

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

                self.previous_track = current_track

            except Exception as e:
                print(f"Unable to get track: {e}")
                wait_time = 10

            time.sleep(wait_time)


main = Main()
