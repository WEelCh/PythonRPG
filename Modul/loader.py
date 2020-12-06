# AUTHOR : Elijah Zeidler Fabian Stange
# DATE   : 

# --- DOCSTRING -------------------
'''
Handles all xml related logic
'''
# --- IMPORT ----------------------

import xml.etree.ElementTree as ET
import re
from random import randint,choice

import Modul.setting as setting
###from Modul.classes.environment import bigTile
import Modul.classes.item as Item
import Modul.classes.entity as Entity


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

def saveTile(obj, coord:str, savegame:int):
    '''
    saves old tile
    
    '''

    tree = ET.parse(setting.path_Saves+'savegame_%s.xml'%(str(savegame)))
    root = tree.getroot()

    # check exitstence

    try: # when it exists ... just some changes
        for tile in root.findall('world/region'):
            if tile.attrib['coord'] == pos:
                #changes

                indent(root)
                tree.write(setting.path_Saves+'savegame_%s.xml'%(str(savegame)))
                return
    except: # if no tile at all exists
        pass

    # when it not exists ... new
    data = root.find('world')
    region = ET.SubElement(data, 'region')
    region.attrib['coord'] = pos

    big_tile = ET.SubElement(region, 'big_tile')
    data = ET.SubElement(big_tile, 'name')
    data.text = 'foo'

    small_tiles = ET.SubElement(region, 'small_tiles')
    for i in range(1,11):
        tile = ET.SubElement(small_tiles, 'tile')
        tile.attrib['id'] = str(i)

        data = ET.SubElement(tile, 'name')
        data.text = 'foo'
        data = ET.SubElement(tile, 'description')
        data.text = 'foo'
        data = ET.SubElement(tile, 'lock_condition')
        data.text = 'foo'

        item = ET.SubElement(tile, 'item')
        data = ET.SubElement(item, 'type')
        data.text = 'foo'
        data = ET.SubElement(item, 'name')
        data.text = 'foo'
        data = ET.SubElement(item, 'value')
        data.text = 'foo'

        entity = ET.SubElement(tile, 'entity')
        data = ET.SubElement(entity, 'type')
        data.text = 'foo'
        data = ET.SubElement(entity, 'name')
        data.text = 'foo'
        data = ET.SubElement(entity, 'value')
        data.text = 'foo'

    indent(root)
    tree.write(setting.path_Saves+'savegame_%s.xml'%(str(savegame)))



def loadTile(coords:str, savegame:int):
    '''
    loads new tile
    
    attribute __coords__ holds a string with X/Y coordinates in following format:
    - X_Y
        - and example might be 0_0; -1_80; -90_-90 etc. 
    given coordinates must be found in /saves/$savegame.xml
    will then return the given list as dictionary. 
    
    dict usage --> e.g. region_DATA [small_tiles] [name] [i]
    --> get the i'st name of i'st small tile
    '''

    region_DATA =  {'big_tile':{
                        'name':None},
                    'small_tiles':{
                        'name':[0 for i in range(9)],
                        'description':[0 for i in range(9)],
                        'lock_condition':[0 for i in range(9)],
                        'item':{
                            'type':[0 for i in range(9)],
                            'name':[0 for i in range(9)],
                            'value':[0 for i in range(9)]},
                        'entity':{
                            'type':[0 for i in range(9)],
                            'name':[0 for i in range(9)],
                            'value':[0 for i in range(9)]}
                            }}

    tree = ET.parse(setting.path_Saves+'savegame_%s'%(str(savegame)))
    root = tree.getroot()

    # checks if tile exists
    for region in root.findall('world/region'):
        if region.attrib['coord'] == coords:
            break
    return False # if tile NOT exists

    # if tile exists:
    # loads all the region DATA in region_DATA

    # big_tile
    region_DATA['big_tile']['name'] = region.find('big_tile/name').text

    # small_tile
    for i in range(9):

        for tile in region.findall('small_tiles/tile'):
            if tile.attrib['id'] == str(i):
                break

        region_DATA['small_tiles']['name'][i] = tile.find('name').text
        region_DATA['small_tiles']['description'][i] = tile.find('description').text
        region_DATA['small_tiles']['lock_condition'][i] = tile.find('lock_condition').text
        if tile.find('item/type').text != 'None':
            region_DATA['small_tiles']['item']['type'][i] = tile.find('item/type').text
            region_DATA['small_tiles']['item']['name'][i] = tile.find('item/name').text
            region_DATA['small_tiles']['item']['value'][i] = tile.find('item/value').text
        else:
            region_DATA['small_tiles']['item'][i] = None
        if tile.find('entity/type').text != 'None':
            region_DATA['small_tiles']['entity']['type'][i] = tile.find('entity/type').text
            region_DATA['small_tiles']['entity']['name'][i] = tile.find('entity/name').text
            region_DATA['small_tiles']['entity']['value'][i] = tile.find('entity/value').text
        else:
            region_DATA['small_tiles']['entity'][i] = None

    return region_DATA



def getBigTile(player_obj:object):
    '''
    return big_tile data from sample_tiles.xml
    the given object must be an instance of __player__ in order to make the generation adjustable.
    '''
    
    tree = ET.parse(setting.path_Data+'sample_tiles.xml')
    root = tree.getroot()
    
    percentage = randint(0,player_obj.treatExplorationScore())
    
    tile_data = dict()
    
    if player_obj.treatExplorationScore() == 0:
        for tile in root[2]: # big_tile
            #  defaults to home tile at 0,0
            if tile.get('id') == '00':
                for data in tile:
                    tile_data[data.tag] = data.text
                return tile_data

    if(percentage <= 22) or (player_obj.treatEndFound() == True): 
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



def getSmallTile(typ):
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
        int(typ)

        for tile in root[1]: # small_tile
            if tile.get('id') == typ:
                for data in tile:
                    tile_data[data.tag] = data.text
                return tile_data
        raise KeyError ('No tile with specified id !')

    except:
        for tile in root[1]: # small_tile search
            types = tile.get('type').split(',')
            if typ in types:
                pos_tiles.append(tile)

        if len(pos_tiles) == 0:
            raise KeyError ('No tile with specified type !')

        tile = choice(pos_tiles)

        for data in tile:
            tile_data[data.tag] = data.text
        return tile_data



def genItem(typ = False):
    '''
    gets Itemdata out of the xml with type 'typ'
    '''

    if typ == False:
        typ = choice(['Weapon','Food','MedicalSupplies'])

    tree = ET.parse(setting.path_Data+'sample_items.xml')
    root = tree.getroot()

    item_list = []

    for item in root.findall('items/item'):
        if item.attrib['type'] == typ:
            item_list.append(item)
    
    item = choice(item_list)

    name = item.find('name').text
    value = item.find('value').text

    if '_' in value:
        value = value.split('_')

    if typ == 'Weapon':
        obj = Item.Weapon(name, value)
    elif typ == 'Food':
        obj = Item.Food(name, value[0], value[1])
    elif typ == 'MedicalSupply':
        obj = Item.MedicalSupply(name, value)

    return obj



def genEntity(typ = False):
    '''
    gets Entitydata out off the xml with type 'typ'
    '''

    if typ == False:
        typ = choice(['Friend','Enemy'])

    tree = ET.parse(setting.path_Data+'sample_entities.xml')
    root = tree.getroot()

    entity_list = []

    for entity in root.findall('entities/entity'):
        if entity.attrib['type'] == typ:
            entity_list.append(entity)

    entity = choice(entity_list)

    name = entity.find('name').text
    value = entity.find('value').text

    if '_' in value:
        value = value.split('_')

    if typ == 'Friend':
        obj = 'NOT FINALLY WORKING'
    elif typ == 'Enemy':
        obj = Entity.Enemy(name, value[0], value[1])

    return obj


def resetSaveGame(savegame:int):
    '''RESETS the SaveGame with number savegame'''

    tree = ET.parse(setting.path_Saves+'savegame_%s.xml'%(savegame))
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
    data        = ET.SubElement(backpack, 'keys')
    data.text   = 'foo'
    for slot in range(1,11):
        data = ET.SubElement(backpack, 'slot')
        data.attrib['id'] = str(slot)

        item = ET.SubElement(data, 'item')
        data = ET.SubElement(item, 'name')
        data.text = 'None'
        data = ET.SubElement(item, 'type')
        data.text = 'None'
        data = ET.SubElement(item, 'value')
        data.text = 'None'

    ET.SubElement(root, 'world')

    indent(root)
    tree.write(setting.path_Saves+'savegame_%d.xml'%(savegame))

# --- SHUT DOWN -------------------



# --- comment ---------------------

