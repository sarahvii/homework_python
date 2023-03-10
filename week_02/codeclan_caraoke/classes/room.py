class Room:
    def __init__(self, name):
        self.name = name
        self.guest_list = []

    def guest_count(self):
        return len(self.guest_list)
    
    def check_in_guest(self, guest):
        self.guest_list.append(guest)
    
    def check_out_guest(self, guest):
        self.guest_list.remove(guest)