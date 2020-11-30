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

class bigTile:

    def __init__(self,coordinate_y:int,coordinate_x:int):
        self.__coordinate_x = coordinate_x
        self.__coordinate_y = coordinate_y
        self.__type = 'empty'
        self.__description = 'nothing yet'
        self.__inherited_smallTiles = {}
        self.generatedSmallTiles
    
    
    def loadSmallTiles(self):
        pass

    def listSmallTiles(self):
        for key in self.__inherited_smallTiles.keys:
            print(key)
    def generatedSmallTiles(self):
        print('generating Tiles and adding them')
        for i in range(0,8):
            self.__inherited_smallTiles[i] = smallTile()
            self.__inherited_smallTiles[i].generateTile()
    def getSmallTiles(self):
        return self.__inherited_smallTiles


# class holding the smaller tile inherited by bigTiles

class smallTile:
    '''
    this class is for handling and generating objects 
    '''
    def __init__(self):
        self.__type = 'empty'
        self.__name = None
        self.__description = 'empty'
        self.__available_items = []
#generate world
    def generateTile(self):
        '''
        Initializes Tile and gives it any attributes needed
        '''
        self.generateType()
        self.generateItems()
        #further add more stuff lol

    def generateType(self):
        '''
        generates type of content, letting it vary with its content and description
        '''
        self.__type = 'Haus'
        self.__description = 'a house left long time ago, maybe smth can be found here?'


    def setName(self,):
        """
        docstring
        """
        self.__name = 'Haus'
    
    def generateItems(self):
        '''
        generating items for each tile
        '''
        self.__available_items =[i for i in range(0,9)]


#def generateTile(tile:object):
#    if not isinstance(tile,object):
#        raise TypeError
#    if tile.shatter() is 'yes':
#        return searchFailed() # tells player that it disappeared and moves him back to previous positon or simply generates a new tile? 
#    tile.generateType()
#    tile.generateDescription()
#    tile.setItems()
#    tile.setMonsters()

# --- ----
# static generated tile
home = bigTile(0,0)
home.generatedSmallTiles()
print(home)
print(home.getSmallTiles)
# --- ----

world_tiles = {
    'home':home,

    }
# --- ----
