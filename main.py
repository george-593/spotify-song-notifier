import time

from applescript import Applescript


class Main:
    def __init__(self):
        self.applescript = Applescript()
        self.main()

    def trigger_track_change(self):
        pass

    def main(self):
        while True:
            # Main Loop

            # Use applescript to monitor spotify - do thing when track changes
            curTrack = self.applescript.get_current_track()
            print(f"{curTrack.name} dur: {curTrack.duration} pos: {curTrack.position}")

            time.sleep(1)


main = Main()
