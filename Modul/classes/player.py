# -------------------

__author__ ='Fabian Stange'

# ---- ---- import libraries ---- ----
from Modul.loader import *
import Modul.classes.environment as environment
import Modul.classes.entity as entity
import random
# ---- ---- ---- ----

# ---- ---- global variables ---- ----


# ---- ---- ---- ----


# ---- ---- code //  ---- -----

class Player():

    def __init__(self,list_at:list):
        # --- basic static attributes
        self.__savegame = 1
        self.__end_found = False
        self.__name = 'empty'
        self.__sex = 'empty'
        # --- position on map
        self.__coordinate_X = 0
        self.__coordinate_Y = 0
        # active Big Tile object
        self.__active_tile = None
        # active small Tile object
        self.__active_small_tile = None
        self.__explore_score = 0
        # active entity to interact with 
        self.__active_entity = None
        # --- dynamic attributes of player
        self.__char_class = 'nothing'
        self.__health = 0
        self.__max_health = 0
        self.__stamina = 0
        self.__max_stamina = 0
        self.__mana = 0
        self.__max_mana = 0
        self.__strength = 0 
        self.__intelligence = 0 
        self.__perception = 0
        self.__items_backpack = [None for i in range(12)]
        self.__keys = 0
        self.generatePlayer(list_at)
        self.setActiveTile()

# --- ---
# SET VALUES
# --- ---

    def generatePlayer(self,player_input:list):
        '''
        ## taking values provided by player
        function that takes a list of playerinput to generate the
        characters traits.
        applys:
        - savegame
        - name
        - sex 
        - class
        - health / max health
        - stamina / max stamina
        - strength / intelligence
        - perception
        - predefined items for the class
        '''
        self.__savegame = player_input[0]
        self.__name = player_input[1]
        self.__sex = player_input[2]
        # iterating trough sublist, provided by choosen class
        self.__char_class = player_input[3]
        self.setClassAttributes()

    def setClassAttributes(self):
        '''
        {VALUES REQUIRED}
        an awful method to set the basic attributes for our player
        ### takes four possible classes from menu(creategame) upon initialisation 
        '''
        if self.__char_class == 'Mercenary': 
            self.__health = 20
            self.__max_health = 20
            self.__stamina = 30
            self.__max_stamina = 30
            self.__mana = 10
            self.__max_mana = 10
            self.__strength = 10
            self.__intelligence = 10
            self.__perception = 10
            self.__items_backpack = []
        elif self.__char_class == 'Illusionist':
            self.__health = 20
            self.__max_health = 20
            self.__stamina = 0
            self.__max_stamina = 0
            self.__mana = 0
            self.__max_mana = 0
            self.__strength = 0
            self.__intelligence = 0
            self.__perception = 0 
            self.__items_backpack = []

        elif self.__char_class == 'Stinker':
            self.__health = 0
            self.__max_health = 0
            self.__stamina = 0
            self.__max_stamina = 0
            self.__mana = 0
            self.__max_mana = 0
            self.__strength = 0
            self.__intelligence = 0
            self.__perception = 0 
            self.__items_backpack = []

        elif self.__char_class == 'Scout':
            self.__health = 0
            self.__max_health = 0
            self.__stamina = 0
            self.__max_stamina = 0
            self.__mana = 0
            self.__max_mana = 0
            self.__strength = 0
            self.__intelligence = 0
            self.__perception = 0 
            self.__items_backpack = []

    def initializePlayer(self):
        '''
        {#ONLY FOR SAVEGAME}
        method to import player data after successfully saving the game
        uses given dictionary from loader.py
        '''
        self.__name = 'empty'
        self.__sex = 'empty'
        # --- position on map
        self.__active_coordinates = [0,0]
        self.__explore_score = 0
        # --- dynamic leveling attributes
        self.__level = 0
        self.__experience = 0 
        # --- dynamic attributes of player
        self.__health = 0
        self.__max_health = 0
        self.__stamina = 0
        self.__max_stamina = 0
        self.__mana = 0
        self.__max_mana = 0
        self.__strength = 0 
        self.__intelligence = 0 
        self.__perception = 0
        self.__items_backpack = []
        #
        # must set the last used TILE from given coordinate
        self.setActiveTile()
        

# --- ---
# RETURN VALUES
# --- ---
    
    # ---  static values ---
    
    def getName(self):
        '''
        returns player name
        ### is string
        '''
        return self.__name

    def getSavegame(self):
        '''
        returns savegame location of object
        ### is int
        '''
        return self.__savegame
    
    def getSex(self):
        '''
        returns sex of character
        ### is string
        '''
        return self.__sex

    def getItems(self):
        '''
        returns items in backpack.
        ### is list
        '''
        return self.__items_backpack
    
    def getItemsName(self):
        '''
        returns list of item names 
        ### is list
        '''
        for i in self.__items_backpack:
            pass 
        return [self.__items_backpack[i].getName for i in range(0,len(self.__items_backpack))]
    
    def getCoordinates(self):
        '''
        return coordinates as a concatenated string. 
        built as follows: *coordinateX_coordinateY*
        Example: 0_-1;-2_2
        '''
        return str(self.__coordinate_X)+'_'+str(self.__coordinate_Y)
    
    def getCharClass(self):
        return self.__char_class

    def getMaxHealth(self):
        return self.__max_health
    
    def getMaxStamina(self):
        return self.__max_stamina
    
    def getMaxMana(self):
        return self.__max_mana

    def getEntity(self):
        return self.__active_entity
# --- ---
# UPDATING VALUES
# --- ---
    
    def treatAttackStrength(self):
        '''
        function to work with attack strenght, which is evaluated by weapons and their values in backpack 
        and the given base strength
        '''
        pass

    def treatHealth(self,switch:int=0,new_val=None):
        '''
        returns Health or takes new value based on condition of *switch*
        defaults to return only if no argument is given
        ### return is tuple 
        takes and returns values as follows:
        - [0] current value
        - [1] max value
        
        '''
        if switch == 0:
            return self.__health,self.__max_health
        else:
            self.__health = new_val[0]
            self.__max_health = new_val[1]
    
    def treatStamina(self,switch:int=0,new_val=None):
        '''
        returns Stamina or takes new value based on condition of *switch*
        defaults to return only if no argument is given
        ### is tuple 
        takes and returns values as follows:
        - [0] current value
        - [1] max value
        
        '''
        if switch == 0:
            return self.__stamina,self.__max_stamina
        else:
            self.__stamina = new_val[0]
            self.__max_stamina = new_val[1]
    
    def treatMana(self,switch:int=0,new_val=None):
        '''
        returns Mana or takes new value based on condition of *switch*
        defaults to return only if no argument is given
        ### is tuple 
        takes and returns values as follows:
        - [0] current value
        - [1] max value
        
        '''
        if switch == 0:
            return self.__mana,self.__max_mana
        else:
            self.__mana = new_val[0]
            self.__max_mana = new_val[1]
    
    def treatPerception(self,switch:int=0,new_val=None):
        '''
        returns the current value for perception or takes new value based on condition of *switch*
        defaults to return only if no argument is given
        ### is int
        '''
        if switch == 0:
            return self.__perception
        else:
            self.__perception = new_val
    
    def treatStrength(self,switch:int=0,new_val=None):
        '''
        returns the current value for strength or takes new value based on condition of *switch*
        defaults to return only if no argument is given
        ### is int
        '''
        if switch == 0:
            return self.__strength
        else:
            self.__strength = new_val
    
    def treatIntelligence(self,switch:int=0,new_val=None):
        '''
        returns the current value for strength or takes new value based on condition of *switch*
        defaults to return only if no argument is given
        ### is int
        '''
        if switch == 0:
            return self.__intelligence
        else:
            self.__intelligence = new_val
    
    def treatExplorationScore(self,switch:int=0,new_val=None):
        '''
        returns current score of explored tiles or takes new value based on condition of *switch*
        defaults to return only if no argument is given
        '''
        if switch == 0:
            return self.__explore_score
        else:
            self.__explore_score += new_val
        
    def treatEndFound(self,switch:int=0,new_val=None):
        '''
        returns the current value for End_Found or takes new value based on condition of *switch*
        defaults to return only if no argument is given
        '''
        if switch == 0:
            return self.__end_found
        else:
            self.__end_found = new_val
 
# --- ---
# Update/Modify Itemlist
# --- ---

    def checkItems(self,):
        '''
        a method for checking the players inventory.
        If it holds more than 12 items, it will return False,
        otherwise it will return True
        '''
        items = 0
        for i in self.__items_backpack:    
            if(i != None):
                items +=1
            else:
                True
        return True

    def setItem(self,item:object):
        '''
        adds a new item as long as there is enough place for the item. 
        If the backpack - list to be precise - is full, it will ask the player
        to choose, whether to change an existing one or just drop the item
        
        - returns success message if check passed
        
        - leads to swapItem if no space left
        '''
        if self.checkItems() == True:
            self.__items_backpack.append(item)
            self.__active_small_tile.setItem()
            return "Success!\n Item was added to your inventory."
        else:
            self.swapItem(item)

    def deleteItem(self,item:object):
        '''
        deletes item that was passed trough to that method
        if the given item was not found, it will return "item not found"
        '''
        if item in self.__items_backpack:
            self.__items_backpack.remove(item)
        else:
            return "item not found"    
    
    def swapItem(self,item:object):
        '''
        VISUALIZE WITH LOOP
        takes new item and asks player if he wants to switch the found item with another in his backpack.

        a,b = True
        while a:
            print('It seems like there is not enough space available.\n' \
            'Drop given item or swap it out with another? \n' \
            '[Yes y] || [NO n ]' )
            choice_a = str(input('\n>> '))
            if(choice_a.lower() == "yes") or (choice_a.lower() == 'y'):
                while b:
                    print('Which item to delete?\n enter number or name of it')
                    self.listItems()
                    # should display list of items in the display menu //
                    choice_b = str(input('\n>> '))
                    if(type(choice_b) != int):
                        pass                        
            else:
                pass    
        '''
        # list items first
        self.getItemsName()
        '''
        not done yet ///
        if value was swapped with an existing item, it should delete the item from the active small tile
        - self.__active_small_tile.setItem() used for that process
        '''

    def queryBackpack(self,itemtype:str):
        '''
        #### NOT DONE ####
        method to query the backpack, searching given type
        - itemtype must be a string
        ### is object
        '''
        pass

# --- ---    
# Player Movement
# --- ---
    def CheckTileExplored(self):
        '''
        upon entering a new BigTile this method checks if the new one was already generated before. 
        otherwise it will generate a new one and save the last Tile.
        '''
        
        if loadTile(self.getCoordinates(),self.__savegame) == False:
            # create a new tile based on the coordinates given and safe it as active tile 
            self.__active_tile = environment.bigTile(self.__coordinate_X,self.__coordinate_Y,self)
            self.__explore_score += 1
        else: 
            # search in savegame and read out the object to load it.
            self.__active_tile =  environment.bigTile(self.__coordinate_X,self.__coordinate_Y,self,1)
        
    def goEast(self):

        if(self.__active_entity != None):
            if(self.__active_entity.getType() != 'Friend'):
                return "you cant move rn, there's an enemy"
        saveTile(self.__active_tile,self.getCoordinates(),self.__savegame)
        self.__coordinate_X += 1
        self.__active_tile = None
        self.__active_small_tile = None
        self.CheckTileExplored()
            
    def goWest(self):
        saveTile(self.__active_tile,self.getCoordinates(),self.__savegame)
        self.__coordinate_X -= 1
        self.__active_tile = None
        self.__active_small_tile = None
        self.CheckTileExplored()
        
    def goNorth(self):
        saveTile(self.__active_tile,self.getCoordinates(),self.__savegame)
        self.__coordinate_Y += 1
        self.__active_tile = None
        self.__active_small_tile = None
        self.CheckTileExplored()
    
    def goSouth(self):
        saveTile(self.__active_tile,self.getCoordinates(),self.__savegame)
        self.__coordinate_Y -= 1 
        self.__active_tile = None
        self.__active_small_tile = None
        self.CheckTileExplored()

# --- ---
# Player Interaction
# --- ---

    def changeLockCondition(self):
        '''
        changes opened/closed condition if needed keys are available.
        '''
        if self.__keys >= self.__active_small_tile.getkeyRequired():
            self.__keys -= self.__active_small_tile.getkeyRequired()
            self.__active_small_tile.updateLockCondition()
        
    def searchItem(self):
        '''
        method to let player search for an item in active_small_tile
        - returns nothing if active_small_tile doesnt hold an item
        - returns 
        '''
        if self.__active_small_tile.getItem() == None:
            return 'nothing found'  
        else:
            return self.setItem(self.__active_small_tile.getItem())

    def setActiveTile(self):
        '''
        method to set active Big tile upon loading the character for the first time // or smth like that
        '''
        # loads given tile
        self.__active_tile = environment.bigTile(self.__coordinate_X,self.__coordinate_Y,self,1)

    def listSmallTiles(self):
        '''
        returns available small tiles on big tile.
        
        ### is tuple/list
        '''
        return self.__active_tile.listSmallTiles()    

    def setActiveSmallTile(self,query):
        '''
        triggers query to select active small tile to work with. 
        FOR UI >> Must return what new active _ small Tile is 
        ### query is string or integer
        - string must be a name 
        '''
        self.__active_small_tile =  self.__active_tile.querySmallTiles(query)
        return self.__active_small_tile.getName()

    def playerRest(self):
        '''
        method to let player rest in order to restore stamina (and health)
        - with a given percentage the player has an encounter with a random enemy
        interrupting his resting. 
        - restores stamina to maximum 
        - if player rests on type"shelter" they restores uninterrupted all the time
        '''
        if self.__active_entity != None:
            return 'sleep not possible, theres an entity here'

        if self.__active_tile.getType() == 'shelter':
            self.treatStamina(1,[self.__max_stamina,self.__max_stamina])
            return 'successfully restored'
        else:
            if random.choice([i for i in randint(0,20)] <=10):
                self.__active_entity = genEntity('Enemy')




    '''
    adds interaction with environment // active Tile
    - check if entity is enemy or player to allow/disallow travelling
    - if entity is present no movement is allowed 
    - query backpack ///
    - explore(active_tile._small_tile) -- results in combat or nothing
    - rest - lets the person rest -- stamina restore / slight health --  and with a certain percentage a monster might spawn during that process/ 
    - active_small_tile to directly interact with the queried smallTile from a bigTile
    ////
    - searchItem(active_tile._small_tile) -- results with item / nothing ### done ### 
    - unlock - if tile.smalltile[] locked >> check if enough owned ### done ### 
    '''

# --- ---
# Player Combat
# --- ---

# --- ---
# VISUALIZING VALUES
# --- ---
    # --- visualize values ---
    
    def listHealth(self):
        '''
        returns Health in visualized form
        ### is string
        '''
        percentage_health = self.__health*100/self.__max_health
        value_max = 20 
        value_left = round(20*percentage_health/100)
        return ('[','█'*value_left,'░'*(value_max-value_left),']')

    def listStamina(self):
        '''
        returns available Stamina in visualized form
        ### is string
        '''
        percentage_stamina = self.__stamina*100/self.__max_stamina
        value_max = self.__max_stamina 
        value_left = round(20*percentage_stamina/100)
        return ('[','█'*value_left,'░'*(value_max-value_left),']')
    
    def listMana(self):
        '''
        returns available Mana in visualized form
        ### is string
        '''
        percentage_mana = self.__mana*100/self.__max_mana
        value_max = self.__max_mana
        value_left = round(20*percentage_mana/100)
        return ('[','█'*value_left,'░'*(value_max - value_left),']')
    