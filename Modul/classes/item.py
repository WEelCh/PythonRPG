# AUTHOR : Zeidler Elijah
# DATE   : 

# --- DOCSTRING -------------------
'''
Defines the ITEM class and all of it's
SubClasses
'''
# --- IMPORT ----------------------

from random import randint
import Modul.loader as loader

# --- DECLARATION -----------------



# --- SETUP -----------------------

class Item ():
    '''mother class of all ITEM related
    SubClasses'''

    def __init__(self,n):
        self._name  = n


# --- MAIN ------------------------

class Weapon (Item):
    '''weapon
    serves to increeses atk'''

    def __init__(self, n, a):
        super().__init__(n)
        self._atk   = int(a)

    def generate(self,exval):
        '''generates new values'''
        self._name,self._atk = loader.genItem('weapon')

    def getName(self):
        return str(self._name)

    def getAtk(self):
        return int(self._atk)
    def getType(self):
        return 'Weapon'
    
    def getPackedValues(self):
        return '%d'%(self._atk)

class Food (Item):
    '''food
    restores stamina and health'''

    def __init__(self, n, s, h):
        super().__init__(n)
        self._re_stamina    = int(s)
        self._re_health     = int(h)

    def generate(self,exval):
        '''generates new values'''
        self._name,value = loader.genItem('food')
        value = value.split(',')
        self._re_stamina = value[0]
        self._re_health = value[1]

    def getName(self):
        return str(self._name)

    def getReStamina(self):
        return int(self._re_stamina)

    def getReHealth(self):
        return int(self._re_health)
    
    def getType(self):
        return 'Food'
    def getPackedValues(self):
        return '%d,%d'%(self._re_stamina,self._re_health)

class MedicalSupply (Item):
    '''medical supplies
    restores health'''

    def __init__(self, n, h):
        super().__init__(n)
        self._re_health = int(h)

    def getName(self):
        return str(self._name)

    def generate(self,exval):
        '''generates new values'''
        self._name,self._re_health = loader.genItem('medicalsupply')

    def getReHealth(self):
        return int(self._re_health)
    def getType(self):
        return 'MedicalSupply'
    
    def getPackedValues(self):
        return '%d'%(self._re_health)

# --- SHUT DOWN -------------------



# --- comment ---------------------
