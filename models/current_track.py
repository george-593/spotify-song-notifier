class CurrentTrack:
    def __init__(
        self, name: str, artist: str, album: str, duration: int, url: str, position: str
    ):
        self.name = name
        self.artist = artist
        self.album = album
        self.duration = duration
        self.url = url
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
            url=parts[4],
            position=parts[5],
        )
