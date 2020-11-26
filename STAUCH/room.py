# class room
class Room():
    # constants
    directions = ["east", "south", "west", "north"]
    
    # constructor
    def __init__(self, room_name, room_description):
        self.room_name = room_name
        self.description = room_description
        self.linked_rooms = {}
        self.items = None
        self.inhabitant = None
        
    # methods
    def get_room_name(self):
        return self.room_name
    
    def get_description(self):
        return self.description
    
    def get_linked_rooms(self):
        return self.linked_rooms
        
    def show_linked_rooms(self):
        print(self.room_name,"is linked")
        for direction in self.linked_rooms.keys():
            print(direction,":",self.linked_rooms[direction].get_room_name())
    
    def link_room(self,linked_room, link_direction):
        self.linked_rooms[link_direction] = linked_room
    
    def set_inhabitant(self, current_inhabitant):
        self.inhabitant = current_inhabitant
        
    def get_inhabitant(self):
        return self.inhabitant
        
    