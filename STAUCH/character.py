# characters

class Character():
    
    def __init__(self,character_name, character_description):
        self.character_name = character_name
        self.description = character_description
        self.room = None
        
    def get_name(self):
        return self.character_name
    
    def get_description(self):
        return self.description
    
    def get_room(self):
        return self.room
    
    def set_room(self, current_room):
        self.room = current_room
        
# subclass Enemy

class Enemy(Character):

    def __init__(self, enemy_name, enemy_description,current_room,enemy_weakness):
        super().__init__(enemy_name,enemy_description)
        self.weakness = enemy_weakness
        self.set_room(current_room)
        
# ++++++++++++++++++++++++++++++++++++++++++++++++
# subclass Friend

class Friend(Character):
    
    def __init__(self, friend_name, friend_description, current_room, current_item):
        super().__init__(friend_name,friend_description)
        self.set_room(current_room)
        self.item = current_item
    