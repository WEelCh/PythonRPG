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
from random import randint,choice

# --- DECLARATION -----------------



# --- SETUP -----------------------

def indent(elem, level=0):
    '''Copyrigth ERICK M. SPREGEL
    https://stackoverflow.com/users/1489446/erick-m-sprengel'''

    i = '\n' + level*'  '
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + '  '
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

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

    tree = ET.parse(setting.path_Data+'meta.xml')
    root = tree.getroot()

    root[0][0].text = new_y
    root[0][1].text = new_x

    tree.write(setting.path_Data+'meta.xml')



def getSaveGame():
    '''checks for last savegame information
    in meta.xml'''

    tree = ET.parse(setting.path_Data+'meta.xml')
    root = tree.getroot()

    return str(root[1][0].text)


# SAMPLE TILE HANDLING


def getBigTile(player_obj:object):
    '''
    return big_tile data from sample_tiles.xml
    the given object must be an instance of __player__ in order to make the generation adjustable.
    '''
    
    tree = ET.parse(setting.path_Data+'sample_tiles.xml')
    root = tree.getroot()
    
    percentage = randint(0,player_obj.getExplorationScore)
    
    tile_data = dict()
    
    if player_obj.getExplorationScore() == 0:
        for tile in root[2]: # big_tile
            #  defaults to home tile at 0,0
            if tile.get('id') == '00':
                for data in tile:
                    tile_data[data.tag] = data.text
                return tile_data

    if(percentage <= 22) or (player_obj.getEndFound() == True): 
        random_id = range(0,len(root[0]))
        for tile in root[0]: # big_tile
            # read out id length - choose random number for id 
            if tile.get('id') == random_id:
                for values in tile:
                    tile_data[values.tag] = values.text
                return tile_data
    else:
        for tile in root[2]:
            if tile.get('id') == '01':
                for values in tile:
                    tile_data[values.tag]= values.text
                return tile_data



def getSmallTile(search):
    '''
    return small_tile data from sample_tiles.xml
    due to id OR type
    raises a KeyError if id or type does not exist
    '''

    tree = ET.parse(setting.path_Data+'sample_tiles.xml')
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



def loadTile(coords:str, savegame:str,switch:int=0):
    '''
    loads new tile
    
    attribute __coords__ holds a string with X/Y coordinates in following format:
    - X_Y
        - and example might be 0_0; -1_80; -90_-90 etc. 
    given coordinates must be found in /saves/$Player/explored_tiles.xml
    will then return the given list as dictionary. 

    loadTile() must be able to check whether a coordinate is present or not.
    If it is it should return 
    '''
    tree = ET.parse(setting.path_Saves+'savegame_%s'%(str(savegame)))
    root = tree.getroot()
    '''
    for tile in root.findall('world/region'):
        
        if(tile.attrib['coord'] == coords) and (switch == 1):
            return True
        elif(tile.attrib['coord'] == coords) and (switch == 0):
            for data in tile.iter():
                    tile_data[data.tag] = data.text
                return tile_data
        # needs to trigger if the given coordinate is present in savegame/// 
    '''


def genItem(typ):
    '''
    gets Itemdata out off the xml with type 'typ'
    '''

    tree = ET.parse(setting.path_Data+'sample_items.xml')
    root = tree.getroot()

    item_list = []

    for item in root.findall('items/item'):
        if item.attrib['type'] == typ:
            item_list.append(item)
    
    item = choice(item_list)
    
    return item.find('name').text, item.find('value').text



def genEntity(typ):
    '''
    gets Entitydata out off the xml with type 'typ'
    '''

    tree = ET.parse(setting.path_Data+'sample_entities.xml')
    root = tree.getroot()

    entity_list = []

    for entity in root.findall('entities/entity'):
        if entity.attrib['type'] == typ:
            entity_list.append(entity)
    
    entity = choice(entity_list)
    
    return entity.find('name').text, entity.find('value').text



def resetSaveGame(savegame:int):
    '''RESETS the SaveGame with number savegame'''

    tree = ET.parse(setting.path_Saves+'savegame_%d.xml'%(savegame))
    root = tree.getroot()

    root.clear()

    # player init
    player      = ET.SubElement(root, 'player')

    generell    = ET.SubElement(player, 'generell')
    data        = ET.SubElement(generell, 'end_found')
    data.text   = 'None'
    data        = ET.SubElement(generell, 'explore_score')
    data.text   = 'None'
    data        = ET.SubElement(generell, 'pos')
    data.text   = 'None,None'
    data        = ET.SubElement(generell, 'name')
    data.text   = 'None'
    data        = ET.SubElement(generell, 'sex')
    data.text   = 'None'
    data        = ET.SubElement(generell, 'class')
    data.text   = 'None'

    traits      = ET.SubElement(player, 'traits')
    data        = ET.SubElement(traits, 'health')
    data.text   = 'None'
    data        = ET.SubElement(traits, 'stamina')
    data.text   = 'None'
    data        = ET.SubElement(traits, 'mana')
    data.text   = 'None'
    data        = ET.SubElement(traits, 'strength')
    data.text   = 'None'
    data        = ET.SubElement(traits, 'intelligence')
    data.text   = 'None'
    data        = ET.SubElement(traits, 'perception')
    data.text   = 'None'

    backpack    = ET.SubElement(player, 'backpack')
    for slot in range(1,11):
        data                = ET.SubElement(backpack, 'slot')
        data.text           = 'None'
        data.attrib['id']   = str(slot)

    indent(root)
    tree.write(setting.path_Saves+'savegame_%d.xml'%(savegame))

# --- SHUT DOWN -------------------



# --- comment ---------------------

