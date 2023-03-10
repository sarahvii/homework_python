class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.guest_list = []
        self.playlist = []

    def guest_count(self):
        return len(self.guest_list)
    
    def check_in_guest(self, guest):
        self.guest_list.append(guest)
    
    def check_out_guest(self, guest):
        self.guest_list.remove(guest)

    def song_count(self):
        return len(self.playlist)
    
    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        self.playlist.remove(song)

    # def capacity_of_room(self, capacity):
    #     return capacity