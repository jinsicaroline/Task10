class Song:
    def __init__(self, title: str, artist: str, duration: float):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self):
        print(f"Playing {self.title} by {self.artist}")


class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.songs = []

    def add_song(self, song: Song):
        self.songs.append(song)
        print(f"Added {song.title} to {self.name} playlist")

    def remove_song(self, song: Song):
        self.songs.remove(song)
        print(f"Removed {song.title} from {self.name} playlist")

    def play_all(self):
        print(f"Playing all songs in {self.name} playlist")
        for song in self.songs:
            song.play()


class MusicPlayer:
    def __init__(self):
        self.playlists = []

    def create_playlist(self, name: str):
        playlist = Playlist(name)
        self.playlists.append(playlist)
        print(f"Created playlist {name}")
        return playlist

    def delete_playlist(self, playlist: Playlist):
        self.playlists.remove(playlist)
        print(f"Deleted playlist {playlist.name}")

    def add_song_to_playlist(self, song: Song, playlist: Playlist):
        playlist.add_song(song)

    def remove_song_from_playlist(self, song: Song, playlist: Playlist):
        playlist.remove_song(song)



