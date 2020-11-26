# class player

class Player():
     # constants
    directions = ["east", "south", "west", "north"]
    commands = ["go_on","quit"]
    
    # constructor
    def __init__(self, player_name, player_description):
        self.player_name = player_name
        self.description = player_description
        self.current_room = None
        self.items = None
    
     # methods
    def get_player_name(self):
        return self.player_name
    
    def get_description(self):
        return self.description
    
    def set_current_room(self,current_room):
        self.current_room = current_room
    
    def get_current_room(self):
        return self.current_room
        
    def move(self, direction):
        if direction in self.directions:
            rooms = self.current_room.get_linked_rooms()
            if direction in rooms.keys():
                self.current_room = rooms[direction]
            else:
                print("no way!")
                