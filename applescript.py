import subprocess
from models.current_track import CurrentTrack
import exceptions


class Applescript:
    def __init__(self):
        pass

    def _run_applescript(self, script: str):
        result = subprocess.run(
            ["/usr/bin/osascript", "-"], input=script, capture_output=True, text=True
        )
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            raise Exception(f"AppleScript error: {result.stderr}")

    def hello_world(self):
        script = """
tell application "TextEdit"
    activate
    make new document
    set text of front document to "hello world"
end tell
        """
        res = self._run_applescript(script)
        print(res)

    def get_current_track(self):
        script = """
if application "Spotify" is running then
    tell application "Spotify"
        return (name of current track) & "||" & (artist of current track) & "||" & (album of current track) & "||" & (duration of current track) & "||" & (spotify url of current track) & "||" & (player position)
    end tell
else
    return ""
end if
    """
        result = self._run_applescript(script)

        if not result:
            raise exceptions.SpotifyNotRunningError()

        return CurrentTrack.from_spotify_output(result)
