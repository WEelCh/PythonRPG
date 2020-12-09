# AUTHOR : Zeidler Elijah
# DATE   : 

# --- DOCSTRING -------------------
'''
Defines the ENTITY class and all of it's
SubClasses
'''
# --- IMPORT ----------------------

import Modul.loader as loader

# --- DECLARATION -----------------



# --- SETUP -----------------------

class Entity ():

    def __init__(self, n):
        self._name = n

# --- MAIN ------------------------

class Friend (Entity):

    def __init__(self, n):
        super().__init__(n)
        self._type = 'Friend'
        self._atk = 0
        self._health = 10
    def generate(self, exval):
        '''generates new value'''
        self._name,value = loader.genEntity('friend')
        value = value.split(',')
        self._atk = int(value[0])
        self._health = int(value[1])
        

    def getType(self):
        return self._type
   
    def getName(self):
        return str(self._name)
   
    def getPackedValues(self):
        return '%d,%d'%(self._atk,self._health)


class Enemy (Entity):

    def __init__(self, n, a, h):
        super().__init__(n)
        self._atk       = int(a)
        self._health    = int(h)
        self._max_health    = int(h)
        self._type = 'Enemy'

    def generate(self, exval):
        '''generates new value'''
        self._name,value = loader.genEntity('enemy')
        value = value.split(',')
        self._atk = value[0]
        self._health = value[1]
        

    def getType(self):
        return self._type

    def getName(self):
        return str(self._name)

    def getAtk(self):
        return self._atk

    def getHealth(self):
        return self._health
    
    def UpdateHealth(self,value:int):
        if value >= self._max_health:
            return 'death'
        elif self._health - value == 0 :
            return 'death'
        else:
            self._health = self._health - value
        
    
    def getPackedValues(self):
        return '%d,%d'%(self._atk,self._health)
# --- SHUT DOWN -------------------



# --- comment ---------------------
'''
possible class for later on:
- Trader
- Companion
- passiveMobs (only enemy after fighting)
'''
