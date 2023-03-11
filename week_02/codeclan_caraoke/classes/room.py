class Room:
    def __init__(self, room_name, capacity, entry_fee, till):
        self.room_name = room_name
        self.guest_list = []
        self.playlist = []
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.till = till

    # GUEST_LIST

    def guest_count(self):
        return len(self.guest_list)
    
    def check_in_guest(self, guest):
        self.guest_list.append(guest)
    
    def check_out_guest(self, guest):
        self.guest_list.remove(guest)

    # PLAY_LIST

    def song_count(self):
        return len(self.playlist)
    
    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        self.playlist.remove(song)

    # CAPACITY

    # ENTRY FEE






