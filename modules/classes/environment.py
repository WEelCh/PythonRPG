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
        '''
        Constructor to initialize an instance of a bigTile.
         - Takes coordinates to make it available in the set matrix. -- player travels by choosing these coordinates
         - Generates the instance's data and types upon loading - given in constructor. 
         - Generates its inhereted smallTiles when it gets called - 9 in total held in a dictionary for easier access. 
         - more to come i guess // 
         # maybe holding an active attribute making it easier for the game to track where player is located at // 
        '''
        self.__coordinate_x = coordinate_x
        self.__coordinate_y = coordinate_y
        self.__type = 'empty'
        self.__name = 'none'
        self.__description = 'nothing yet'
        self.__inherited_smallTiles = {}
        self.generatedSmallTiles()
        self.generatebigTile()
        self.setPlayerExploration()
    
    def generatebigTile(self):
        '''
        setting all the necessary 
        '''
        # ---
        # reading out and setting necessary attributes for the mother tile 
        # ---
        '''
        self.__type = 
        self._name =
        self.__description = 

        '''
    def setPlayerExploration(self):
        '''
        increasing the players count of explored tiles as this attribute contributs to the later world_generation
        making it more difficult but also making more weapons available.
        the character also skills with increasing counter of explorations
        '''

        return active_player.exploration += 1 

    def loadSmallTiles(self):
        pass

    def listSmallTiles(self):
        for key in self.__inherited_smallTiles.keys:
            print(key,'\n')
    def generatedSmallTiles(self):
        print('generating Tiles and adding them')
        for i in range(0,8):
            self.__inherited_smallTiles['test',+i] = smallTile()
            self.__inherited_smallTiles['test',+i].generateTile()
    def getSmallTiles(self):
        return self.__inherited_smallTiles
    def getName(self):
        return self.__type 




# --- --- --- ---
# class holding the smaller tile inherited by bigTiles
# --- --- --- ---

# --- --- --- ---
# --- --- --- ---
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
home.
print(home)
print(home.getName())
print(home.getSmallTiles())
# --- ----

world_tiles = {
    'home':home,

    }
# --- ----
