from functools import partial
from mac_notifications import client

from models.current_track import CurrentTrack


class Notifications:
    def __init__(self) -> None:
        pass

    def send_notification(
        self, previous_track: CurrentTrack, current_track: CurrentTrack
    ) -> None:
        print("sending notification")

        notification = client.create_notification(
            title="New Song Playing",
            text=f"Previous Song: {previous_track.name} by {previous_track.artist}\nCurrent Song: {current_track.name} by {current_track.artist}",
            action_button_str="Add previous to Playlist",
            action_callback=partial(self.notification_add_callback),
        )
        print(f"Notification queued with id: {notification.uid}")

    def notification_add_callback(self):
        print("Callbac received")
