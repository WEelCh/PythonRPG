# AUTHOR : Elijah Zeidler & Fabian Stange
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

# --- ---
# FUNCTIONS FORMATTING
# --- ---

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

# --- ---
# XML HANDELING
# --- ---

def getLastSaveGame():
    '''checks for last savegame information
    in meta.xml'''

    tree = ET.parse(setting.path_Data+'meta.xml')
    root = tree.getroot()

    return str(root.find('last_game/value').text)



def getSaveGame(savegame:int):
    '''gives data about the savegame'''

    tree = ET.parse(setting.path_Saves+'savegame_%s.xml'%(str(savegame)))
    root = tree.getroot()

    name = root.find('player/generel/name')
    name = name.text
    clas = root.find('player/generel/class')
    clas = clas.text
    explore = root.find('player/generel/explore_score')
    explore = explore.text
    end  = root.find('player/generel/end_found')
    end = end.text

    return [str(name), str(clas), str(explore), str(end)]

# PLAYER HANDLING

def savePlayer(obj:object, savegame:int):
    '''Saves the Player object'''
    slot = 0
    tree = ET.parse(setting.path_Saves+'savegame_%s.xml'%(str(savegame)))
    root = tree.getroot()

    player = root.find('player')

    general = player.find('general')
    data    = general.find('end_found')
    data.text = str(obj.treatEndFound())
    data    = general.find('explore_score')
    data.text = str(obj.treatExplorationScore())
    data    = general.find('pos')
    data.text = str(obj.getCoordinates())
    data    = general.find('name')
    data.text = str(obj.getName())
    data    = general.find('sex')
    data.text = str(obj.getSex())
    data    = general.find('class')
    data.text = str(obj.getCharClass())

    traits  = player.find('traits')
    data    = traits.find('health')
    data.text = '%s,%s'%(str(obj.treatHealth()[0]),str(obj.treatHealth()[1]))
    data    = traits.find('stamina')
    data.text = '%s,%s'%(str(obj.treatStamina()[0]),str(obj.treatStamina()[1]))
    data    = traits.find('mana')
    data.text = '%s,%s'%(str(obj.treatMana()[0]),str(obj.treatMana()[1]))
    data    = traits.find('strength')
    data.text = str(obj.treatStrength())
    data    = traits.find('intelligence')
    data.text = str(obj.treatIntelligence())
    data    = traits.find('perception')
    data.text = str(obj.treatPerception())

    backpack = player.find('backpack')
    data = backpack.find('keys')
    data.text = str(obj.getKeys())

    for item in backpack.findall('slot/item'):
        item_values = obj.getItemValues(slot)
        if item_values !=None:    
            data = item.find('name')
            data.text = str(item_values[1])
            data = item.find('type')
            data.text = str(item_values[0])
            data = item.find('value')
            data.text = str(item_values[2])
        else:
            data = item.find('name')
            data.text = 'None'
            data = item.find('type')
            data.text = 'None'
            data = item.find('value')
            data.text = 'None'
        slot += 1

    indent(root)
    tree.write(setting.path_Saves+'savegame_%s.xml'%(str(savegame)))



def loadPlayer(savegame:int):
    '''
    Loads the Player
    '''

    tree = ET.parse(setting.path_Saves+'savegame_%s.xml'%(str(savegame)))
    root = tree.getroot()

    player_DATA = { 'general':{
                        'end_found' : None,
                        'explore_score' : None,
                        'pos' : None,
                        'name' : None,
                        'sex' : None,
                        'class' : None},
                    'traits':{
                        'health' : None,
                        'stamina' : None,
                        'mana' : None,
                        'strength' : None,
                        'intelligence' : None,
                        'perception' : None},
                    'backpack':{
                        'keys':0,
                        'items':{
                            'name':[None for i in range(12)],
                            'type':[None for i in range(12)],
                            'value':[None for i in range(12)]}
                            }}

    player = root.find('player')

    general = player.find('general')
    data    = general.find('end_found')
    player_DATA['general']['end_found'] = data.text
    data    = general.find('explore_score')
    player_DATA['general']['explore_score'] = data.text
    data    = general.find('pos')
    player_DATA['general']['pos'] = data.text
    data    = general.find('name')
    player_DATA['general']['name'] = data.text
    data    = general.find('sex')
    player_DATA['general']['sex'] = data.text
    data    = general.find('class')
    player_DATA['general']['class'] = data.text

    traits  = player.find('traits')
    data    = traits.find('health')
    player_DATA['traits']['health'] = data.text
    data    = traits.find('stamina')
    player_DATA['traits']['stamina'] = data.text
    data    = traits.find('mana')
    player_DATA['traits']['mana'] = data.text
    data    = traits.find('strength')
    player_DATA['traits']['strength'] = data.text
    data    = traits.find('intelligence')
    player_DATA['traits']['intelligence'] = data.text
    data    = traits.find('perception')
    player_DATA['traits']['perception'] = data.text

    backpack = player.find('backpack')
    data = backpack.find('keys')
    player_DATA['backpack']['keys'] = data.text

    i = 0
    for item in backpack.findall('slot/item'):
        data = item.find('name')
        player_DATA['backpack']['items']['name'][i] = data.text
        data = item.find('type')
        player_DATA['backpack']['items']['type'][i] = data.text
        data = item.find('value')
        player_DATA['backpack']['items']['value'][i] = data.text
        i += 1
    return player_DATA


# SAMPLE TILE HANDLING

def saveTile(obj, coord:str, savegame:int):
    '''saves old tile'''

    tree = ET.parse(setting.path_Saves+'savegame_%s.xml'%(str(savegame)))
    root = tree.getroot()

    # check exitstence

    try: # when it exists ... just some changes
        for tile in root.findall('world/region'):
            if tile.attrib['coord'] == coord:
                #changes

                indent(root)
                tree.write(setting.path_Saves+'savegame_%s.xml'%(str(savegame)))
                return
    except: # if no tile at all exists
        pass

    # when it not exists ... new
    small_tile_list = obj.getSmallTiles()
    data = root.find('world')
    region = ET.SubElement(data, 'region')
    region.attrib['coord'] = coord

    big_tile = ET.SubElement(region, 'big_tile')
    data = ET.SubElement(big_tile, 'name')
    data.text = obj.getName()

    small_tiles = ET.SubElement(region, 'small_tiles')
    for i in range(9):
        tile = ET.SubElement(small_tiles, 'tile')
        tile.attrib['id'] = str(i)

        data = ET.SubElement(tile, 'name')
        data.text = small_tile_list[i].getName()
        data = ET.SubElement(tile, 'description')
        data.text = small_tile_list[i].getDescription()
        data = ET.SubElement(tile, 'lock_condition')
        data.text = small_tile_list[i].getLockCondition()

        item = ET.SubElement(tile, 'item')
        data = ET.SubElement(item, 'type')
        # reads out item object from iterated small tile
        queried_item = small_tile_list[i].getItem()
        
        if(queried_item != None):
            if(queried_item.getType() != 'Key'):
                data.text = queried_item.getType()
                data = ET.SubElement(item, 'name')
                data.text = queried_item.getName()
                data = ET.SubElement(item, 'value')
                data.text = queried_item.getPackedValues()
            elif(queried_item.getType() == 'Key'):
                data.text = queried_item.getType()
                data = ET.SubElement(item, 'name')
                data.text = queried_item.getName()
                data = ET.SubElement(item, 'value')
                data.text = 0
        else:
            data.text = 'None'
            data = ET.SubElement(item, 'name')
            data.text = 'None'
            data = ET.SubElement(item, 'value')
            data.text = 'None'
        entity = ET.SubElement(tile, 'entity')
        data = ET.SubElement(entity, 'type')
        # reads out enity object from iterated small tile
        queried_entity = small_tile_list[i].getEntity()
        
        if queried_entity != None: 
            data.text = queried_entity.getType()
            data = ET.SubElement(entity, 'name')
            data.text = queried_entity.getName()
            data = ET.SubElement(entity, 'value')
            data.text = queried_entity.getPackedValues()
        else:
            data.text = 'None'
            data = ET.SubElement(entity, 'name')
            data.text = 'None'
            data = ET.SubElement(entity, 'value')
            data.text = 'None'
        del queried_entity,queried_item
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

    tree = ET.parse(setting.path_Saves+'savegame_%s.xml'%(str(savegame)))
    root = tree.getroot()

    # checks if tile exists
    cache = True
    for region in root.findall('world/region'):
        if region.attrib['coord'] == coords:
            cache = False
            break
    if cache:
        return False # if tile NOT exists

    # if tile exists:
    # loads all the region DATA in region_DATA

    # big_tile
    data = region.find('big_tile/name')
    region_DATA['big_tile']['name'] = data.text

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

    # load home tile
    if player_obj.treatExplorationScore() == 0:
        for tile in root.findall('pre_defined_tiles/tile'):
            if tile.attrib['id'] == '0':
                for data in tile:
                    tile_data[data.tag] = data.text
                return tile_data

    #  load random tile
    if(percentage <= 22) or (player_obj.treatEndFound() == True):
        cache = []
        for tile in root.findall('big_tiles/tile'):
            cache.append(tile)
        tile = choice(cache)
        for values in tile:
            tile_data[values.tag] = values.text
        return tile_data

    # load end tile
    else:
        for tile in root.findall('pre_defined_tiles/tile'):
            if tile.get('id') == '1':
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

    except: # search name
        for tile in root.findall('small_tiles/tile'):
            if tile.attrib['type'] == typ:
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
        typ = choice(['Weapon','Food','MedicalSupply','Key'])

    tree = ET.parse(setting.path_Data+'sample_items.xml')
    root = tree.getroot()

    item_list = []

    for item in root.findall('items/item'):
        if item.attrib['type'] == typ:
            item_list.append(item)
    
    item = choice(item_list)

    name = item.find('name').text
    value = item.find('value').text

    if ',' in value:
        value = value.split(',')

    if typ == 'Weapon':
        obj = Item.Weapon(name, value)
    elif typ == 'Food':
        obj = Item.Food(name, value[0], value[1])
    elif typ == 'MedicalSupply':
        obj = Item.MedicalSupply(name, value)
    elif typ == 'Key':
        obj = Item.Key()

    return obj



def genEntity(typ = False):
    '''
    gets Entitydata out off the xml with type 'typ'
    
    possible types are:
    - Enemy
    - Friend
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
        # NOT FINALLY WORKING 
        obj = Entity.Friend(name)
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

    general    = ET.SubElement(player, 'general')
    data        = ET.SubElement(general, 'end_found')
    data.text   = 'None'
    data        = ET.SubElement(general, 'explore_score')
    data.text   = 'None'
    data        = ET.SubElement(general, 'pos')
    data.text   = '0,0'
    data        = ET.SubElement(general, 'name')
    data.text   = 'None'
    data        = ET.SubElement(general, 'sex')
    data.text   = 'None'
    data        = ET.SubElement(general, 'class')
    data.text   = 'None'
    data        = ET.SubElement(general, 'class')
    data.text   = '---'

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
    data.text   = '0'
    for slot in range(12):
        data = ET.SubElement(backpack, 'slot')
        data.attrib['id'] = str(slot)

        item = ET.SubElement(data, 'item')
        data = ET.SubElement(item, 'name')
        data.text = 'None'
        data = ET.SubElement(item, 'type')
        data.text = 'None'
        data = ET.SubElement(item, 'value')
        data.text = 'None'

    # world init

    name = ['Home','Market','Locker','Metro','Lobby','Restaurant',
            'Nuclear power plant','Grammar School','collapsed Skyscraper']
    description = [
                    '\nYou hear the constant strings of rain pattering on your apartments roof, while small leds illumante this hollow room.\n',
                    '\nAs you enter the market you perceive a variety of sounds. This area seems busy and maybe you are able to trade as well.\n',
                    '\nA tremendous bank vault secured by space marines indicating that its probably best to avoid going there. Maybe later.\n',
                    '\nRapid trains once passed these rails, now its just dust and junk paving a way trough the depths of this tunnel.\n',
                    '\nYou enter the halls filled with a diversity of scents indicating that a lot of ppl come here and talk with each other.\n',
                    '\nIn this distopian times a place to relax and nourish thyself next to well laid plates is fairly welcomed. Enjoy.\n',
                    '\nGreat Scientists once maintained this enormous accomplishment that delivered power to the whole city and further.\n',
                    '\nOnce visited by many teenagers and kids this school now represents the fallen Importance of education in this world.\n',
                    '\nMany people worked here before the world fell apart. You ought to find out what caused this destruction at some point.\n'
                    ]


    world       = ET.SubElement(root, 'world')
    region      = ET.SubElement(world, 'region')
    region.attrib['coord'] = '0_0'

    big_tile    = ET.SubElement(region, 'big_tile')
    data        = ET.SubElement(big_tile, 'name')
    data.text = 'Shelter'

    small_tiles = ET.SubElement(region, 'small_tiles')
    for i in range(9):
        tile    = ET.SubElement(small_tiles, 'tile')
        tile.attrib['id'] = str(i)
        data    = ET.SubElement(tile, 'name')
        data.text = name[i-1]
        data    = ET.SubElement(tile, 'description')
        data.text = description[i-1]+'          '
        data    = ET.SubElement(tile, 'lock_condition')
        data.text = 'opened'

        item    = ET.SubElement(tile, 'item')
        data    = ET.SubElement(item, 'type')
        data.text = 'None'
        data    = ET.SubElement(item, 'name')
        data.text = 'None'
        data    = ET.SubElement(item, 'value')
        data.text = 'None'

        entity    = ET.SubElement(tile, 'entity')
        data    = ET.SubElement(entity, 'type')
        data.text = 'None'
        data    = ET.SubElement(entity, 'name')
        data.text = 'None'
        data    = ET.SubElement(entity, 'value')
        data.text = 'None'


    indent(root)
    tree.write(setting.path_Saves+'savegame_%d.xml'%(savegame))



def resetSettings():
    '''RESETS the meta.xml'''

    tree = ET.parse(setting.path_Data+'meta.xml')
    root = tree.getroot()

    # clear formating
    for value in root.findall('cmd_location/value'):
        value.text = '0'

    # clear last savegame
    data = root.find('last_game/value')
    data.text = 'None'

    indent(root)
    tree.write(setting.path_Data+'meta.xml')


# --- SHUT DOWN -------------------



# --- comment ---------------------

