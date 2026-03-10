class CurrentTrack:
    def __init__(
        self, name: str, artist: str, album: str, duration: int, uri: str, position: str
    ):
        self.name = name
        self.artist = artist
        self.album = album
        self.duration = duration
        self.uri = uri
        self.position = position

    @classmethod
    def from_spotify_output(cls, output: str) -> "CurrentTrack":
        parts = output.split("||")
        if len(parts) != 6:
            raise ValueError(f"Invalid spotify output: {output}")

        return cls(
            name=parts[0],
            artist=parts[1],
            album=parts[2],
            duration=int(parts[3]),
            uri=parts[4],
            position=parts[5],
        )

    @property
    def duration_seconds(self):
        return self.duration // 1000

    @property
    def time_remaining(self):
        return int(self.duration_seconds - float(self.position))
