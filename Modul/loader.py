# AUTHOR : Elijah Zeidler
# DATE   : 

# --- DOCSTRING -------------------
'''
Handles all xml related logic
'''
# --- IMPORT ----------------------

import xml.etree.ElementTree as ET
import re
import Modul.setting as setting
from random import randint

# --- DECLARATION -----------------



# --- SETUP -----------------------



# --- MAIN ------------------------

# FORMAT HANDLING

def getYXFormat():
    '''returns the Y-Axis and X-Axis
    values from the meta.xml'''

    tree = ET.parse(setting.path_Data+'meta.xml')
    root = tree.getroot()

    Y = int(root[0][0].text)
    X = int(root[0][1].text)
    return Y, X



def setYXFormat(new_y, new_x):
    '''changes the Y-Axis and X-Axis
    values at the meta.xml'''

    tree = ET.parse('Modul\\Data\\meta.xml')
    root = tree.getroot()

    root[0][0].text = new_y
    root[0][1].text = new_x

    tree.write('Modul\\Data\\meta.xml')



def getSaveGame():
    '''checks for last savegame information
    in meta.xml'''

    tree = ET.parse('Modul\\Data\\meta.xml')
    root = tree.getroot()

    return str(root[1][0].text)


# SAMPLE TILE HANDLING


def getBigTile(progress_exploration:int):
    '''
    return big_tile data from sample_tiles.xml
    value _progress_exploration_ helps to filter and later implement certain aspects of the game.

    '''

    tree = ET.parse('Data\\sample_tiles.xml')
    root = tree.getroot()

    tile_data = dict()
    if progress_exploration is 0:
        for tile in root[0]: # big_tile
            #  defaults to home tile at 0,0
            if tile.get('id') == 0:
                for data in tile:
                    tile_data[data.tag] = data.text
                return tile_data
    elif( progress_exploration <=20) and (progress_exploration >1):
        pass
    raise KeyError ('No tile with specified id !')



def getSmallTile(search):
    '''
    return small_tile data from sample_tiles.xml
    due to id OR type
    raises a KeyError if id or type does not exist
    '''

    tree = ET.parse('Data\\sample_tiles.xml')
    root = tree.getroot()

    tile_data = dict()
    pos_tiles = list()

    try: # search id
        int(search)

        for tile in root[1]: # small_tile
            if tile.get('id') == search:
                for data in tile:
                    tile_data[data.tag] = data.text
                return tile_data
        raise KeyError ('No tile with specified id !')

    except:
        for tile in root[1]: # small_tile search
            types = tile.get('type').split(',')
            if search in types:
                pos_tiles.append(tile)

        if len(pos_tiles) == 0:
            raise KeyError ('No tile with specified type !')

        rand_select = randint(0,len(pos_tiles)-1)

        for data in pos_tiles[rand_select]:
            tile_data[data.tag] = data.text
        return tile_data



def saveTile(bigtile, pos, savegame):
    '''
    saves old tile
    
    '''

    tree = ET.parse(setting.path_Saves+'savegame_%s'%(str(savegame)))
    root = tree.getroot()

    # check exitstence
    for tile in root.findall('world/region'):
        if pos == str(tile.attrib):

            # when it exists
            tile.find('small_tiles/tile')



def loadTile(coords, savegame):
    '''
    loads new tile
    
    attribute __coordinates__ holds a string with X/Y coordinates in following format:
    - X_Y
        - and example might be 0_0; -1_80; -90_-90 etc. 
    given coordinates must be found in /saves/$Player/explored_tiles.xml
    will then return the given list as dictionary. 
    '''

    tree = ET.parse(setting.path_Saves+'savegame_%s'%(str(savegame)))
    root = tree.getroot()




# --- SHUT DOWN -------------------



# --- comment ---------------------

