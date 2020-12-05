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

    def generate(self, exval):
        '''generates new value'''
        self._name,value = loader.genEntity('friend')
        value = value.split(',')
        self._atk = value[0]
        self._health = value[1]

    def getName(self):
        return str(self._name)



class Enemy (Entity):

    def __init__(self, n, a, h):
        super().__init__(n)
        self._atk       = a
        self._health    = h

    def generate(self, exval):
        '''generates new value'''
        self._name,value = loader.genEntity('enemy')
        value = value.split(',')
        self._atk = value[0]
        self._health = value[1]

    def getName(self):
        return str(self._name)

    def getAtk(self):
        return self._atk

    def getHealth(self):
        return self._health

# --- SHUT DOWN -------------------



# --- comment ---------------------

