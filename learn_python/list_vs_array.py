class Node:
    def __init__(self, song_name):
        self.song_name = song_name
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, song_name):
        new_song = Node(song_name)
        if not self.head:
            self.head = new_song  # The first song in the playlist (head)
            return  # We return here because no further actions are needed.
        last_song = self.head
        while last_song.next:  # Keep moving to the next song in the list.
            last_song = last_song.next
        last_song.next = new_song

    def show_playlist(self):
        current_song = self.head
        while current_song:
            print(current_song.song_name)
            current_song = current_song.next


def array_playlist_example():
    playlist = ["Song 1", "Song 2", "Song 3"]
    print("Playlist using an Array:")
    for song in playlist:  # playlist is a list, so we can iterate through it.
        print(song)  # For each song in the array, print its name.


def linked_list_playlist_example():
    playlist = Playlist()
    playlist.add_song("Song 1")  # Adds "Song 1" to the playlist.
    playlist.add_song("Song 2")  # Adds "Song 2" to the playlist.
    playlist.add_song("Song 3")  # Adds "Song 3" to the playlist.
    print("\nPlaylist using a Linked List:")
    playlist.show_playlist()


array_playlist_example()  # First, show the array example.
linked_list_playlist_example()  # Then, show the linked list example.
