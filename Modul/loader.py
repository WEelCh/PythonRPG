# AUTHOR : Elijah Zeidler
# DATE   : 

# --- DOCSTRING -------------------
'''
Handles all xml related logic
'''
# --- IMPORT ----------------------

import xml.etree.ElementTree as ET
import re

# --- DECLARATION -----------------



# --- SETUP -----------------------



# --- MAIN ------------------------

def getYXformat():
    '''gives the Y-Axis and X-Axis
    values from the meta.xml'''

    tree = ET.parse('Modul\\Data\\meta.xml')
    root = tree.getroot()

    Y = int(root[0][0].text)
    X = int(root[0][1].text)
    return Y, X



def setYXformat(new_y, new_x):
    '''changes the Y-Axis and X-Axis
    values at the meta.xml'''

    tree = ET.parse('Modul\\Data\\meta.xml')
    root = tree.getroot()

    root[0][0].text = new_y
    root[0][1].text = new_x

    tree.write('Modul\\Data\\meta.xml')



def getsavegame():
    '''checks for last savegame information
    in meta.xml'''

    tree = ET.parse('Modul\\Data\\meta.xml')
    root = tree.getroot()

    return str(root[1][0].text)


# --- SHUT DOWN -------------------



# --- comment ---------------------

