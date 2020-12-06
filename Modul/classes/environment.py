# --- ----
__author__='Fabian Stange'

# --- ----
''' 
File to generate and work with tiles and the whole world during a game. 
{ENHANCE DOCSTRING}
'''
# --- ----

# --- BEGIN Imports and Variables ---
from Modul.player import *
import random
from Modul.loader import *
from Modul.classes.item import *
# --- END Imports and Variables ---

# --- ---- // CODE // ---- ---

# --- ---
# CLASS OF MAIN TILE
# --- ---

class bigTile():

# --- ---
# CONSTRUCTOR 
# --- ---
    def __init__(self,coordinate_x:int,coordinate_y:int,player_obj,isnew:int=0):
        '''
        Constructor to initialize an instance of a bigTile.
        - Takes coordinates to make it available in the set matrix. -- player travels by choosing these coordinates
        - Generates the instance's data and types upon loading - given in constructor. 
        - Generates its inhereted smallTiles when it gets called - 9 in total held in a dictionary for easier access. 
        - more to come i guess // 
        > maybe holding an active attribute making it easier for the game to track where player is located at // 
        '''
        self.__coordinate_x = coordinate_x
        self.__coordinate_y = coordinate_y
        self.__type = 'empty'
        self.__name = 'none'
        self.__given_explore_count = 0
        self.__inherited_smallTiles = list()
        if(isnew is 0):
            self.generatebigTile(player_obj)
            self.generateSmallTiles(player_obj)
        else: 
            self.initializeTile()
    
# --- ---
# SET VALUES
# --- ---

    
    def generatebigTile(self,player:obj):
        '''
        querying all the necessary elements from the Tile samples and mergin a pair to fill values. 
        values that are changed here: 
        - | __type |
        - | __name |
        '''
        sample_data = getBigTile(player)
        self.__type = sample_data['type']
        self.__name = sample_data['name']
    
    def generateSmallTiles(self):
        '''
        method to generate 9 new tiles for instance. 
        SmallTile generation depends on their given type
        '''
        # generates a new small tile that generates upon calling
        
        self.__inherited_smallTiles = [smallTile(self.__given_explore_count,self.__type) for i in range(0,8)]
            
    def initializeTile(self):
        '''
        ONLY FOR EXISTING TILES. 
        Loads data creates object BigTile.
        - adjacent smallTiles and their content are loaded as well. 
            -- use extra method to get restored
        '''
        #readout_data = loader.loadTile
        for i in range(0,8):
            self.__inherited_smallTiles = [smallTile().initializeTile() for i in range(0,8)]

# --- --- 
# RETURN VALUES
# --- --- 
    def getCoordinates(self):
        '''
        method to return both coordinates of the Tile.
        In order to check if player has already been on that Tile or not.  
        '''
        return self.__coordinate_x, self.__coordinate_y
    
    def getType(self):
        '''
        yields Type of given BigTile.
        - necessary for smalltiles, as they depend on this value.
        - for display purpose 
        
        ### is string
        '''
        return self.__type 

    def getName(self):
        '''
        yields Name of given BigTile.
        - for display purpose 
        
        ### is string
        '''
        return self.__name

    def getSmallTiles(self):
        '''
        returns a dictionary of adjacent SmallTiles
        in order to display their name call __inherited_smallTiles.getName()
        
        ### is list with each object 
        
        [9 in total]
        
        used to display them and for later query use
        '''
        return self.__inherited_smallTiles
    
    # getSmallTiles 0- alle bitte
# --- --- 
# Interaction small Tile
# --- --- 

    def querySmallTiles(self,query):
        '''
        PLS LOOP To cope wrong inputs // 
        queries trough inhereted smallTiles listing them in given document 
        and returning the choosen Tile back to player. 
        sets active_small_tile  to selected tile. Allows for interaction directly without querying trough entirye BigTile
        '''
        for Tile in self.__inherited_smallTiles:
            if(Tile.getName() == query):
                return Tile
        # ends with return of newly selected smallTile





# --- --- --- ---
# class holding the smaller tile inherited by bigTiles
# --- --- --- ---



class smallTile():

# --- ---
# CONSTRUCTOR 
# --- ---
    '''
    this class is for handling and generating objects 
    '''
    def __init__(self,counter_explore:int=0,typ:str='none',isnew:int=0):
        self.__type = typ
        self.__name = None
        self.__description = 'empty'
        self.__available_item = None
        self.__available_entity = None
        self.__lock_condition = 'open'
        self.__key_required = 0
        self.__counter_modifier = counter_explore
        if isnew == 0:
            self.generateBasic()
            self.generateItems()
            self.generateEntity()
            self.generatelockCondition()
        else:
            self.initializeTile()

# --- ---
# SET VALUES 
# --- ---

    def generateBasic(self):
        '''
        sets name and description of smallTile read out by loader.getSmallTile()
        '''
        data = getSmallTile(self.__type)
        self.__name = data['name']
        self.__description = data['description']
        
    def generateItems(self):
        '''
        method to generate a new Item - whether its a weapon, food or a medicalSupply.
        
        percentage to generate it, scales with scaling.py
        '''
        self.__available_item = random.choice([None,None,None,None,loader.genItem()])
        pass
    
    def generateEntity(self):
        '''
        method to generate a new Entity - whether its a friend or fiend. 
        
        percentage to generate it, scales with scaling.py
        '''
        self.__available_entity = random.choice(['nothing','nothing','nothing','nothing',loader.genItem()])
    
    def generatelockCondition(self):
        
        '''
        some housings are locked by default upon loading. 
        This method generates this dependency upon first creation and sets a required amount of keys needed
        in order to open it up, if it gets locked. 
        possible values are:
        #### locked 
        #### opened
        - generates required keys if condition is 'locked'
        - if condition is 'opened' no key required
        '''
        if( self.__type.lower() is 'housing') or ( self.__type.lower() is 'dungeon'):
            self.__lock_condition = random.choice(['locked','opened'])
            if(self.__lock_condition == 'locked'):
                self.__key_required = random.randint(1,5)    
        
    def initializeTile(self,data:list):
        '''
        initializes smalltile attributes with previously saved values.
        Takes list to work with 
        
        
        '''
        pass

# --- ---
# SET VALUES 
# --- ---

    def getName(self):
        return self.__name
    
    def getDescription(self):
        return self.__description
    
    def getkeyRequired(self):
        return self.__key_required
    
    def getItem(self):
        '''
        returns item if one was given. 
        returns a message of failure if not 
        '''
        if self.__available_item != None:
            return self.__available_item
        else:
            return self.__available_item
# --- ---
# UDATE VALUES
# --- ---

    def updateLockCondition(self):
        if self.__lock_condition == 'locked':
            self.__lock_condition = 'opened'
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


print(home)
print(home.getName())
print(home.getSmallTiles())
print(home.listSmallTiles())
# --- ----

# --- ----
