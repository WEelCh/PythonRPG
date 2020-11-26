# --- ----
__author__='Fabian Stange'

# --- ----
''' 
File to generate and work with tiles and the whole world during a game. 
{ENHANCE DOCSTRING}
'''
# --- ----

# --- BEGIN Imports and Variables ---


# --- END Imports and Variables ---

class environmentTile:

    def __init__(self,coordinate_y:int,coordinate_x:int):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.type = 'empty'
        self.description = 'nothing yet'
        self.items = []
        self.monster_presence = []
        self.possibility_to_shatter  = 0.002# probably to be moved to a simple method making it simply disappear and generate a new tile. 

#generate world
def generateTile(tile:object):
    if not isinstance(tile,object):
        raise TypeError
    if tile.shatter() is 'yes':
        return searchFailed() # tells player that it disappeared and moves him back to previous positon or simply generates a new tile? 
    tile.generateType()
    tile.generateDescription()
    tile.setItems()
    tile.setMonsters()

# --- ----
# static generated tile
home = environmentTile(0,0)
generateTile(home)
# --- ----

world_tiles = {
    'home':home,

    }
# --- ----
