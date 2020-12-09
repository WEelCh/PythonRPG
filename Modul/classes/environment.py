# --- ----
__author__='Fabian Stange'

# --- ----
''' 
File to generate and work with tiles and the whole world during a game. 
{ENHANCE DOCSTRING}
'''
# --- ----

# --- BEGIN Imports and Variables ---
from Modul.classes.player import *
import random
from Modul.loader import *
from Modul.classes.item import *
import Modul.scaling as scaling
# --- END Imports and Variables ---

# --- ---- // CODE // ---- ---

# ---
# --- --- --- ---
# CLASS BIGTILE BEGIN
# --- --- --- ---
# ---

class bigTile():

# --- ---
# CONSTRUCTOR 
# --- ---
    def __init__(self,coordinate_x:int,coordinate_y:int,player_obj:object,isnew:int=0):
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
        self.__given_explore_count = player_obj.treatExplorationScore()
        self.__inherited_smallTiles = [0 for i in range(9)]
        if(isnew == 0):
            self.generatebigTile(player_obj)
            self.generateSmallTiles()
        else: 
            self.initializeTile(player_obj)

    
# --- ---
# SET VALUES
# --- ---
    
    def generatebigTile(self,player:object):
        '''
        querying all the necessary elements from the Tile samples and mergin a pair to fill values. 
        values that are changed here: 
        - | __type |
        - | __name |
        '''
        sample_data = loader.getBigTile(player)
        self.__type = sample_data['type']
        self.__name = sample_data['name']
    
    def generateSmallTiles(self):
        '''
        method to generate 9 new tiles for instance. 
        SmallTile generation depends on their given type
        '''
        # generates 9 small tiles that generate themselves upon getting  called
        
        for i in range(9):
            self.__inherited_smallTiles[i] = smallTile(self.__given_explore_count,self.__type)
            
    def initializeTile(self,player:object):
        '''
        ONLY FOR EXISTING TILES. 
        Loads data and creates object BigTile.
        - adjacent smallTiles and their content are loaded as well. 
            -- uses extra method to get restored
        '''
        #readout_data = loader.loadTile
        data_tile = loader.loadTile(self.getCoordinates(),player.getSavegame())
        self.__name = data_tile['big_tile']['name']
        # restores the nine inhereted smallTiles
        for i in range(0,8):
            small_tile = list()
            small_tile.append(data_tile['small_tiles']['name'][i])
            small_tile.append(data_tile['small_tiles']['description'][i])
            small_tile.append(data_tile['small_tiles']['lock_condition'][i])
            if data_tile['small_tiles']['item']['type'][i] != 'None':
                list_item = [
                    data_tile['small_tiles']['item']['type'][i],
                    data_tile['small_tiles']['item']['name'][i],
                    data_tile['small_tiles']['item']['value'][i],
                ]
                small_tile.append(list_item)
            else:
                small_tile.append(None)
            if data_tile['small_tiles']['entity']['type'][i] != 'None':
                list_entity = [
                    data_tile['small_tiles']['entity']['type'][i],
                    data_tile['small_tiles']['entity']['name'][i],
                    data_tile['small_tiles']['entity']['value'][i],
                ]
                small_tile.append(list_entity)
            else:
                small_tile.append(None)
            # calls initialisation of small Tile handing over the collected data
            self.__inherited_smallTiles[i] = smallTile(self.__given_explore_count,self.__type,1,small_tile)
        print('done initializing!')

# --- --- 
# RETURN VALUES
# --- --- 

    def getCoordinates(self):
        '''
        method to return both coordinates of the Tile.
        In order to check if player has already been on that Tile or not.  
        '''
        return str(self.__coordinate_x)+'_'+str(self.__coordinate_y)
    
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
        returns a list of adjacent SmallTiles
        in order to display their name call __inherited_smallTiles.getName()
        
        ### is list with each object 
        
        [9 in total]
        
        used to display them and for later query use
        '''
        return self.__inherited_smallTiles
    
    def getNameSmallTiles(self):
        '''
        returns a list of adjacent SmallTiles
        in order to display their name call __inherited_smallTiles.getName()
        
        ### is list with each object 
        
        [9 in total]
        
        used to display them and for later query use
        '''
        return self.__inherited_smallTiles
    
# --- --- 
# Interaction small Tile
# --- --- 

            

    def querySmallTiles(self,query):
        '''
        query interates trough inhereted smallTiles 
        and returns the choosen Tile back to player. 
        sets player.active_small_tile  to selected tile.
        '''
        try: 
            int(query)
            return self.__inherited_smallTiles[query]
    
        except:    
            for Tile in self.__inherited_smallTiles:
                if(Tile.getName() == query):
                    return Tile
        # ends with return of newly selected smallTile

# ---
# --- --- --- ---
# CLASS SMALLTILE BEGIN
# --- --- --- ---
# ---

class smallTile():

# --- ---
# CONSTRUCTOR 
# --- ---
    '''
    this class is for handling and generating objects 
    '''
    def __init__(self,counter_explore:int=0,typ:str='none',isnew:int=0,data_tile=None):
        '''
        Constructor of SmallTile. 
        Takes: 
        - counter_explore to generate items and entities with scaling.
        - typ in order to generate the right tiles for the mothertile >BigTile<
        - isnew for initializing tile without regenerating
        - data_tile for the process of restoration of already loaded and generated tile 
        '''
        self.__type = typ
        self.__name = None
        self.__description = 'empty'
        self.__available_item = None
        self.__available_entity = None
        self.__lock_condition = 'opened'
        self.__key_required = 0
        self.__counter_modifier = counter_explore
        if isnew == 0:
            self.generateBasic()
            self.generateItems()
            self.generateEntity()
            self.generatelockCondition()
        else:
            self.initializeTile(data_tile)

# --- ---
# SET VALUES 
# --- ---

    def generateBasic(self):
        '''
        sets name and description of smallTile read out by loader.getSmallTile()
        '''
        data = loader.getSmallTile(self.__type)
        self.__name = data['name']
        self.__description = data['description']
        
    def generateItems(self):
        '''
        method to generate a new Item - whether its a weapon, food or a medicalSupply.
        
        percentage to generate it, scales with scaling.py
        '''
        self.__available_item = random.choice(scaling.item_percentage)
        
    def generateEntity(self):
        '''
        method to generate a new Entity - whether its a friend or fiend. 
        
        percentage to generate it, scales with scaling.py
        '''
        self.__available_entity = random.choice(scaling.entity_percentage)
    
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
        if( self.__type.lower() == '') or ( self.__type.lower() == ''):
            self.__lock_condition = random.choice(scaling.lock_condition)
            if(self.__lock_condition == 'locked'):
                self.__key_required = random.randint(1,5)    
        
    def initializeTile(self,data:list):
        '''
        initializes smalltile attributes with previously saved values.
        Takes list to work with 
        
        - data[3] hold either list with item properties or NONE
        - data[4] hold either list with entity properties or NONE
        '''
        self.__name = data[0]
        self.__description = data[1]
        self.__lock_condition = data[2]
        if data[3][0] != None:
            # checks what type of item it is
            if data[3][0] == 'Weapon':
                
                # creates item object WEAPON    
                self.__available_item = Weapon(data[3][1],data[3][2])
            
            elif data[3][0] == 'Food':
                
                # creates item object FOOD    
                food_values = data[3][2].split(',')
                self.__available_item = Food(data[3][1],food_values[0],food_values[1])
            
            elif data[3][0] == 'MedicalSupply':
                
                # creates item object MEDICALSUPPLY
                
                self.__available_item = MedicalSupply(data[3][1],data[3][2])
            elif data[3][0] == 'Key':
                # creates item object KEY
                
                self.__available_item = Key()
        else:
            self.__available_item = None
        
        if data[4][0] != None:
            # checks what type of item it is
            if data[3][0] == 'Friend':
                
                # creates item object WEAPON    
                self.__available_item = Item(data[3][1],data[3][2])
            
            elif data[3][0] == 'Enemy':
                entity_values = data[4][2].split(',')
                self.__available_entity = Entity([data[4][1],entity_values[0],entity_values[1]])
                # creates item object FOOD    
        else:
            self.__available_entity = None

# --- ---
# RETURN VALUES 
# --- ---
    def getItemName(self):
        '''
        returns name of available Item on tile
        '''
        return self.__available_item.getName()
    
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
    
    def getEntity(self):
        '''
        returns item if one was given. 
        returns a message of failure if not 
        '''
        if self.__available_entity != None:
            return self.__available_entity
        else:
            return self.__available_entity

    def getLockCondition(self):
        '''
        returns the current LockCondition
        '''
        return self.__lock_condition
# --- ---
# UDATE VALUES
# --- ---

    def updateLockCondition(self):
        if self.__lock_condition == 'locked':
            self.__lock_condition = 'opened'

    def setItem(self):
        '''
        method to erase an existing item if it was picked up by the player.
        ### // ONLY FOR DEBUGGING //
        returns confirmation that it was deleted 
        '''
        self.__available_item = None
        # confirmation // used for debugging
        return 'item was deleted'

    def setEntity(self):
        '''
        method to erase an existing entity if it was killed by the player.
        ### // ONLY FOR DEBUGGING //
        returns confirmation that it was deleted 
        '''
        self.__available_entity = None
        # confirmation // used for debugging
        return 'entity was deleted'
    


# --- ----

# --- ----
