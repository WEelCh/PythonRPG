# -------------------

__author__ ='Fabian Stange'

# ---- ---- import libraries ---- ----
import Modul.loader as loader

# ---- ---- ---- ----

# ---- ---- global variables ---- ----


# ---- ---- ---- ----


# ---- ---- code //  ---- ----

class player:

    def __init__(self,):
        # --- basic static attributes
        self.__name = 'empty'
        self.__sex = 'empty'
        # --- position on map
        self.__coordinate_X = 0
        self.__coordinate_Y = 0
        self.__active_tile = object
        self.__explore_score = 0
        # --- dynamic leveling attributes
        self.__level = 0
        self.__experience = 0 
        # --- dynamic attributes of player
        self.__health = 0
        self.__max_health = 0
        self.__stamina = 0
        self.__max_stamina = 0
        self.__strength = 0 
        self.__intelligence = 0 
        self.__perception = 0
        self.__items_backpack = []

    # --- ---
    # SETTING VALUES
    # --- ---

    def initializePlayer(self):
        '''
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
        self.__strength = 0 
        self.__intelligence = 0 
        self.__perception = 0
        self.__items_backpack = []

    def generatePlayer(self,content_list:list):
        self.__name
    
    # --- ---
    # RETURN VALUES
    # --- ---
    
    def getName(self):
        return self.__name

    def getSex(self):
        return self.__sex

    def listItems(self):
        for i in self.__items_backpack:
            print(i,'===',self.__items_backpack[i])

    def listHealth(self):
        percentage_health = self.__health*100/self.__max_health
        value_max = 20 
        value_left = round(20*percentage_health/100)
        return ('[','#'*value_left,'-'*20-value_left,']')

    def listStamina(self):
        percentage_stamina = self.__stamina*100/self.__max_stamina
        value_max = 20 
        value_left = round(20*percentage_stamina/100)
        return ('[','#'*value_left,'-'*20-value_left,']')
    
    def getCoordinates(self):
        '''
        return coordinates as a concatenated string. 
        built as follows: *coordinateX_coordinateY*
        Example: 0_-1;-2_2
        '''
        return self.__coordinate_X+'_'+self.__coordinate_Y
    
    # --- ---
    # UPDATING VALUES
    # --- ---
    
    # --- ---
    # UPDATING ITEMLIST

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
    # MOVEMENT OF PLAYER
    def CheckTileExplored(self):
        if self.getCoordinates() in self.__explored_tiles:
            # search in explored_tiles.xml and read out the object to load it.
            loader.loadTile()
            self.__active_tile = 0 #searched object
            pass

        else: 
            
    def goEast(self):
        self.__coordinate_X -= 1  
    def goWest(self):
        self.__coordinate_X += 1
    def goNorth(self):
        self.__coordinate_Y += 1
    def goSouth(self):
        self.__coordinate_Y -= 1 



# --- interaction with the environment