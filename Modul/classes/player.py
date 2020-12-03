# -------------------

__author__ ='Fabian Stange'

# ---- ---- import libraries ---- ----


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
        self.__active_coordinates = [0,0]
        self.__tiles_explored = 0
        # --- dynamic leveling attributes
        self.__level = 0
        self.__experience = 0 
        # --- dynamic attributes of player
        self.__health = 0
        self.__stamina = 0
        self.__strength = 0 
        self.__intelligence = 0 
        self.__items_backpack = []

    def getName(self):
        return self.__name

    def getSex(self):
        return self.__sex

    def listItems(self):
        for i in self.__items_backpack:
            print(i,'===',self.__items_backpack[i])

    # --- updating values
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
        a,b = True
        while a:
            print('It seems like there is not enough space available.\n' \
            'Drop given item or swap it out with another? \n' \
            '[Yes y] || [NO n ]' )
            choice_a = str(input('\n>> '))
            if(choice_a.lower() is "yes") or (choice_a.lower() is 'y'):
                while b:
                    print('Which item to delete?\n enter number or name of it')
                    # should display list of items in the display menu //
                    choice_b = str(input('\n>> '))
                    if(type(choice_b) != int):
                        

            else:
                pass    





    # --- interaction with the environment
    
    def 