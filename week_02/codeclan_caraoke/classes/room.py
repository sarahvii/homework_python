class Room:
    def __init__(self, name):
        self.name = name
        self.guest_list = []

    def guest_count(self):
        return len(self.guest_list)
    
    def add_guest(self, guest):
        self.guest_list.append(guest)
    