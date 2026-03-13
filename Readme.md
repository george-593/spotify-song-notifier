# Spotify Song Notifier

A macOS Python utility that watches your currently playing Spotify track and shows a native notification when the song changes, with the notification having a button to add the previous song to a specific playlist

## Features

- Monitors Spotify playback using AppleScript (`osascript`)
- Detects track changes in near real-time (1s polling)
- Sends native macOS notifications with an action button
- Adds the previous track to a configured Spotify playlist via Spotipy
- Menu bar icon that displays the current track

## Requirements

- macOS
- Python 3.10+
- Spotify desktop app installed
- A Spotify Developer application

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```env
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback

SPOTIFY_PLAYLIST_ID=your_playlist_id
```
If `SPOTIFY_PLAYLIST_ID` is missing, notifications still work, but playlist adds are skipped.

4. In the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard):
- Create an app (or use an existing one).
- Add the same redirect URI you put in `SPOTIPY_REDIRECT_URI`.
- Copy client ID and client secret into `.env`.

## How To Run

```bash
python app.py
```

On first run, Spotipy may open a browser window for Spotify OAuth authorization.