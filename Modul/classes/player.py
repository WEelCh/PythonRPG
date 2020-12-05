# -------------------

__author__ ='Fabian Stange'

# ---- ---- import libraries ---- ----
import Modul.loader as loader
import Modul.classes.environment as environment
# ---- ---- ---- ----

# ---- ---- global variables ---- ----


# ---- ---- ---- ----


# ---- ---- code //  ---- ----

class Player:

    def __init__(self,list_at:):
        # --- basic static attributes
        self.__savegame = 'emtpy'
        self.__end_found = False
        self.__name = 'empty'
        self.__sex = 'empty'
        # --- position on map
        self.__coordinate_X = 0
        self.__coordinate_Y = 0
        self.__active_tile = None
        self.__explored_tiles = list()
        self.__explore_score = 0
        # --- dynamic leveling attributes
        #self.__level = 0
        #self.__experience = 0 
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
        self.__items_backpack = []
        self.generatePlayer(list_at)

# --- ---
# SETTING VALUES
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

# --- --- ---

    def setClassAttributes(self):
        '''
        {VALUES REQUIRED}
        an awful method to set the basic attributes for our player
        ### takes four possible classes from menu(creategame) upon initialisation 
        '''
        if self.__char_class == 'Mercenary': 
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
        elif self.__char_class == 'Illusionist':
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


    # --- ---
    # RETURN VALUES
    # --- ---
    
    def getName(self):
        '''
        returns player name
        ### is string
        '''
        return self.__name

    def getSavegame(self):
        '''
        returns savegame location of object
        ### is string
        '''
        return self.__savegame
    
    def getSex(self):
        '''
        returns sex of character
        ### is string
        '''
        return self.__sex

    def getHealth(self):
        '''
        returns Health
        ### is int
        '''
        return self._health,self.__max_health
    
    def getStamina(self):
        '''
        returns Stamina
        ### is int
        '''
        return self._stamina,self.__max_stamina
    
    def getMana(self):
        '''
        returns Mana
        ### is int
        '''
        return self._mana,self.__max_mana
    
    def listItems(self):
        '''
        returns items in backpack.
        ### is list
        '''
        return self.__items_backpack

    def listHealth(self):
        '''
        returns Health in visualized form
        ### is string
        '''
        percentage_health = self.__health*100/self.__max_health
        value_max = 20 
        value_left = round(20*percentage_health/100)
        return ('[','#'*value_left,'-'*20-value_left,']')

    def listStamina(self):
        '''
        returns available Stamina in visualized form
        ### is string
        '''
        percentage_stamina = self.__stamina*100/self.__max_stamina
        value_max = 20 
        value_left = round(20*percentage_stamina/100)
        return ('[','#'*value_left,'-'*20-value_left,']')
    
    def listMana(self):
        '''
        returns available Mana in visualized form
        ### is string
        '''
        percentage_mana = self.__mana*100/self.__max_mana
        value_max = 20 
        value_left = round(20*percentage_mana/100)
        return ('[','#'*value_left,'-'*20-value_left,']')
    
    def getStrenght(self):
        '''
        returns the current value for strength
        ### is int
        '''
        return self.__strength
    
    def getIntelligence(self):
        '''
        returns the current value for strength
        ### is int
        '''
        return self.__intelligence
    
    def getPerception(self):
        '''
        returns the current value for perception
        ### is int
        '''
        return self.__perception
    
    def getCoordinates(self):
        '''
        return coordinates as a concatenated string. 
        built as follows: *coordinateX_coordinateY*
        Example: 0_-1;-2_2
        '''
        return self.__coordinate_X+'_'+self.__coordinate_Y
    
    def getExplorationScore(self):
        return self.__explore_score
    
    def getEndFound(self,switch:int=0,new_val=None):
        if switch == 0:
            return self.__end_found
        else:
            self.__end_found = new_val
            
    
    # --- ---
    # UPDATING VALUES
    # --- ---
    
    # --- ---
    # UPDATING ITEMLIST BEGIN

    def checkItems(self,):
        '''
        a method for checking the players inventory.
        If it holds more than 15 items, it will return False,
        otherwise it will return True
        '''
        if(len(self.__items_backpack) < 15): 
            return True
        else:
            False

    def setItem(self,item:object):
        '''
        adds a new item as long as there is enough place for the item. 
        If the backpack - list to be precise - is full, it will ask the player
        to choose, whether to change an existing one or just drop the item
        '''
        if self.checkItems() == True:
            self.__items_backpack.append(item)
            return "Success!\n Item was added to your inventory."
        else:
            self.swapItem()

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
        takes two Items and asks player if he wants to switch the found item with another in his backpack.

        '''
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

    # --- ---
    # UPDATING ITEMLIST END
    
    
    
    # MOVEMENT OF PLAYER
    def CheckTileExplored(self):
        '''
        upon entering a new BigTile this method checks if the new one was already generated before. 
        otherwise it will generate a new one and save the last Tile.
        '''
        
        if self.getCoordinates() in self.__explored_tiles:
            # search in explored_tiles.xml and read out the object to load it.
            loader.loadTile()
            self.__active_tile = 0 #searched object
            pass

        else: 
            # create a new tile based on the coordinates given and safe it as active tile 
            self.__active_tile = environment.bigTile(self.__coordinate_X,self.__coordinate_Y)
        
    def goEast(self):
        loader.saveTile(self.__active_tile,self.getCoordinates(),self.__savegame)
        self.__coordinate_X -= 1
        del self.__active_tile
        self.CheckTileExplored()
    def goWest(self):
        loader.saveTile(self.__active_tile,self.getCoordinates(),self.__savegame)
        self.__coordinate_X += 1
        del self.__active_tile
        self.CheckTileExplored()
    def goNorth(self):
        loader.saveTile(self.__active_tile,self.getCoordinates(),self.__savegame)
        self.__coordinate_Y += 1
        del self.__active_tile
        self.CheckTileExplored()
    def goSouth(self):
        loader.saveTile(self.__active_tile,self.getCoordinates(),self.__savegame)
        self.__coordinate_Y -= 1 
        del self.__active_tile
        self.CheckTileExplored()



# --- interaction with the environment