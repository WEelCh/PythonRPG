# AUTHOR : Zeidler Elijah
# DATE   : 

# --- DOCSTRING -------------------
'''
Defines the ITEM class and all of it's
SubClasses
'''
# --- IMPORT ----------------------

from random import randint

# --- DECLARATION -----------------



# --- SETUP -----------------------

class Item ():
    '''mother class of all ITEM related
    SubClasses'''

    def __init__(self, i):
        self._id = i


    pass

# --- MAIN ------------------------

class Weapon (Item):
    '''weapon'''

    def __init__(self,i):
        super.__init__(i)



class Food (Item):
    '''food'''

    def __init__(self, i):
        super.__init__(i)



class MedicalSupplies (Item):
    '''medical supplies'''

    def __init__(self,i):
        super.__init__(i)



class Support (Item):
    '''support'''

    def __init__(self,i):
        super.__init__(i)


# --- SHUT DOWN -------------------



# --- comment ---------------------

'''
weapons (+atk)
food (+stamina) ((+health))
medical supplies (+health)

support (etc key, story)

'''