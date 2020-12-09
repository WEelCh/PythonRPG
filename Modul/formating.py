# AUTHOR : Elijah Zeidler
# DATE   : 

# --- DOCSTRING -------------------
'''
Handles formating for the project

Functions take contents and visualize 
them in standardized format

'''
# --- IMPORT ----------------------

from Modul import loader

import os, platform
from time import sleep as nap

# --- DECLARATION -----------------

# clear function based on used OS; Linux and Win supported 
system_check = platform.system()
if  (system_check.lower() == 'linux') or (system_check.lower() == 'darwin'): 
    clear=lambda: os.system('clear')
elif(system_check.lower() == 'windows'):
    clear=lambda: os.system('cls')
del system_check

# display formating values
form_y, form_x = loader.getYXFormat()
get_x = lambda : ' '*form_x
x = get_x()


# static lines
upper_line  =lambda  : print(x + '╔'+'═'*121+'╗')
upperT_line =lambda  : print(x + '╔'+'╦'.center(121,'═')+'╗')
middle_line =lambda  : print(x + '╠'+'═'*121+'╣')
midUpT_line =lambda  : print(x + '╠'+'╦'.center(121,'═')+'╣')
midX_line   =lambda  : print(x + '╠'+'╬'.center(121,'═')+'╣')
midDwTT_line=lambda  : print(x + '╠'+'╩'.center(121,'═')+'╣')
lower_line  =lambda  : print(x + '╚'+'═'*121+'╝')

empty_line  =lambda n: [print(x + '║'+' '*121+'║') for i in range(n)]
emptyT_line =lambda n: [print(x + '║'+'║'.center(121)+'║') for i in range(n)]
space_line  =lambda n: [print() for i in range(n)]

input_line  =lambda m: str(input(x+m+' '*37))

# dynamic lines
norm_content=lambda c, c1: print(x+'║ '+c.ljust(58)+' ║ '+c1.ljust(58)+' ║')
mid_content =lambda c: print(x+'║'+c.center(121)+'║')
mid_headline=lambda c: print(x+'║'+c.center(121,'═')+'║')
midT_content=lambda c1, c2: print(x+'║'+c1.center(60)+'║'+c2.center(60)+'║')
di_content  =lambda c1, c2: print(x+'║'+c1.center(60)+' '+c2.center(60)+'║')
tri_content =lambda c1,c2,c3: print(x+'║'+c1.center(40)+c2.center(40)+c3.center(40)+' ║')


# static info-values
_title_  = 'WORK_TITLE_PyRPG'
_date_   = '2020'
_author_ = '  Stange Fabian'+' '*90+'Zeidler Elijah '

# --- SETUP -----------------------

# --- MAIN ------------------------


########
# chunks
########


def _headermenu(path, T = False):
    '''Print header of menu'''

    clear()
    space_line(form_y)

    upper_line()
    empty_line(1)
    mid_content(_title_)
    empty_line(1)
    print(x+'║'+_author_+' ║')
    mid_content(_date_)
    empty_line(1)
    mid_content(''+path)
    if T == True:
        midUpT_line()
    else:
        middle_line()



def _bottom(error,msg:str=''):
    '''Print bottom of standardized format'''

    lower_line()

    if error == True:
        if msg == '':
            message = ' Your Input was invalid:'
        else:
            message = ' '+msg
    else:
        message = ' '*24

    return input_line(message)


###############
# generell menu
###############


def menu (error = False):
    '''Show Menu'''

    _headermenu('MENU')

    empty_line(3)

    mid_content('Continue')
    mid_content('1')
    empty_line(3)
    mid_content('New Game')
    mid_content('2')
    empty_line(3)
    mid_content('Load Game')
    mid_content('3')
    empty_line(3)
    mid_content('Settings')
    mid_content('4')
    empty_line(3)
    mid_content('Leave')
    mid_content('0')

    empty_line(5)

    return _bottom(error)



def noSaveGame(error):
    '''Show Menu-Continue : No Savegame'''

    _headermenu('MENU / CONTINUE')

    empty_line(8)

    mid_content('No last played SaveGame found !')
    empty_line(10)
    mid_content('Back')
    mid_content('0')

    empty_line(9)

    return _bottom(error)



def newGame(error, level, data):
    '''Show Menu-New Game'''

    _headermenu('MAIN / NEW GAME')

    if   level == 1: # SaveGame choice
        empty_line(1)
        mid_content('At wich SaveGame do you wanna save the new game?')
        empty_line(1)
        mid_content('Be aware that old SaveGames can be overwriten by your actions !!!')
        empty_line(1)
        midUpT_line()

        emptyT_line(1)
        midT_content('Savegame 1', 'Savegame 2')
        emptyT_line(1)
        midT_content(data[0][0], data[1][0]) # name
        midT_content(data[0][1], data[1][1]) # class
        emptyT_line(1)
        midT_content('Progress: '+data[0][2],'Progress: '+data[1][2]) # explore
        midT_content('End found: '+data[0][3],'End found: '+data[1][3]) # end_found
        emptyT_line(1)

        midX_line()

        emptyT_line(1)
        midT_content('Savegame 3', 'Savegame 4')
        emptyT_line(1)
        midT_content(data[2][0], data[3][0]) # name
        midT_content(data[2][1], data[3][1]) # class
        emptyT_line(1)
        midT_content('Progress: '+data[2][2],'Progress: '+data[3][2]) # explore
        midT_content('End found: '+data[2][3],'End found: '+data[3][3]) # end_found
        emptyT_line(1)

        midDwTT_line()
        empty_line(1)
        mid_content('Back')
        mid_content('0')
        empty_line(1)

    elif level == 2: # Name choice
        empty_line(1)
        mid_content('Under wich name do you wanna to play?')
        empty_line(1)
        mid_content('Be aware that your name can`t be longer')
        mid_content('then 15 chars!')
        empty_line(1)
        mid_content('Back')
        mid_content('0')
        empty_line(1)

    elif level == 3: # Sex choice
        empty_line(1)
        mid_content('Wich sex do you choose?')
        empty_line(1)
        mid_content('Male')
        mid_content('1')
        empty_line(1)
        mid_content('Female')
        mid_content('2')
        empty_line(1)
        mid_content('Diverse')
        mid_content('3')
        empty_line(1)
        mid_content('Back')
        mid_content('0')
        empty_line(1)

    elif level == 4: # Class choice
        empty_line(1)
        mid_content('As wich class do you wanna to play?')
        empty_line(1)
        midUpT_line()
        emptyT_line(1)
        midT_content('Mercenary', 'Stinker')
        emptyT_line(1)
        midX_line()
        emptyT_line(1)
        midT_content('Scout', 'Illusionist')
        emptyT_line(1)
        midDwTT_line()
        empty_line(1)
        mid_content('Back')
        mid_content('0')
        empty_line(1)

    return _bottom(error)



def loadGame(error, data):
    '''Show Menu-Load Game'''

    _headermenu('MENU / LOAD GAME', T = True)

    emptyT_line(2)
    midT_content('Savegame 1', 'Savegame 2')
    emptyT_line(1)
    midT_content(data[0][0], data[1][0]) # name
    midT_content(data[0][1], data[1][1]) # class
    emptyT_line(1)
    midT_content('Progress: '+data[0][2],'Progress: '+data[1][2]) # explore
    midT_content('End found: '+data[0][3],'End found: '+data[1][3]) # end_found
    emptyT_line(3)

    midX_line()

    emptyT_line(2)
    midT_content('Savegame 3', 'Savegame 4')
    emptyT_line(1)
    midT_content(data[2][0], data[3][0]) # name
    midT_content(data[2][1], data[3][1]) # class
    emptyT_line(1)
    midT_content('Progress: '+data[2][2],'Progress: '+data[3][2]) # explore
    midT_content('End found: '+data[2][3],'End found: '+data[3][3]) # end_found
    emptyT_line(3)

    midDwTT_line()
    empty_line(1)
    mid_content('Back')
    mid_content('0')
    empty_line(1)

    return _bottom(error, msg = 'SaveGame not available!')



def settings(error = False):
    '''Show Menu-Settings'''

    _headermenu('MENU / SETTINGS')

    empty_line(6)

    mid_content('Format Window')
    mid_content('1')
    empty_line(5)
    mid_content('Delete User-Data')
    mid_content('2')
    empty_line(5)
    mid_content('Back')
    mid_content('0')

    empty_line(8)

    return _bottom(error)


def settingsFormatWindow(error):
    '''Show Menu-Setting-Format'''

    _headermenu('MENU / SETTINGS / FORMAT WINDOW')

    empty_line(2)

    mid_content('Y Axes Formating')
    mid_content(str(form_y))
    mid_content('Number of clear lines above the menu.')
    empty_line(2)
    mid_content('X Axes Formating')
    mid_content(str(form_x))
    mid_content('Number of clear spaces besides the menu.')
    empty_line(3)
    mid_content('To change enter your new config below,')
    mid_content('in the format "y x".')
    mid_content('For example: "12 4"')
    empty_line(4)
    mid_content('WARNING: To high values can lead to errors')
    mid_content('in the graphics !')
    empty_line(3)
    mid_content('Back')
    mid_content('0')

    empty_line(3)

    return _bottom(error)


def settingsdeleteuserdata(error):
    ''' '''

    _headermenu('MENU / SETTINGS / DELETE USERDATA')

    empty_line(2)

    mid_content('!!! WARNING !!!')
    empty_line(2)
    mid_content('Be aware that this Action will terminate')
    mid_content('! ALL your Progress !')
    empty_line(3)
    mid_content('! Every Savegame will be irretrievable reseted !')
    empty_line(1)
    mid_content('! Personal settings will be reseted !')
    empty_line(1)
    mid_content('After that, the game will shutdown and needs to be restarted')
    empty_line(3)
    mid_content('If you sill want to continue, please type')
    empty_line(1)
    mid_content('"DeLeTe"')
    empty_line(4)
    mid_content('Back')
    mid_content('0')

    empty_line(3)

    return _bottom(error)

#############
# game format
#############


def _headergame(p:object):
    '''Print header of menu
        p == player'''

    clear()
    space_line(form_y)

    upperT_line()

    norm_content('', p.getName().center(58)) #because new lambda makes no sense
    norm_content('  Region Name: '+p.getBigTileName(), 'Health : '+p.listHealth())
    norm_content('  Type       : '+p.getBigTileType(),'')
    norm_content('', 'Stamina: '+p.listStamina())
    norm_content('  Tile Name  : '+p.getSmallTileName(),'')
    norm_content('', 'Mana   : '+p.listMana())
    norm_content('  SaveGame : '+str(p.getSavegame()), 'Keys   : '+str(p.getKeys()))

    midDwTT_line()



def bigTile(error, p:object):
    'Print Game Main'

    _headergame(p)
    list_names =[
        'Nothing',
        'Nothing',
        'Nothing',
        'Nothing',
        'Nothing',
        'Nothing',
        'Nothing',
        'Nothing',
        'Nothing',
    ]

    empty_line(2)
    tri_content(list_names[0],list_names[1],list_names[2])
    tri_content('entity', 'entity', 'entity')
    tri_content('item', 'item', 'item')
    empty_line(2)
    tri_content(list_names[3],list_names[4],list_names[5])
    tri_content('entity', 'entity', 'entity')
    tri_content('item', 'item', 'item')
    empty_line(2)
    tri_content(list_names[6],list_names[7],list_names[8])
    tri_content('entity', 'entity', 'entity')
    tri_content('item', 'item', 'item')
    empty_line(2)

    mid_headline(' What do you want to do ')

    empty_line(3)
    tri_content('1 : Travel', '2 : Enter', '3 : Inventory')
    empty_line(4)

    middle_line()

    empty_line(1)
    mid_content('0 : Save & Quit')
    empty_line(1)

    return _bottom(error)



def travel(error, p):
    '''Print Travel Menu'''

    _headergame(p)

    names_d = p.getTravelInformation()

    empty_line(2)
    tri_content('', 'NORTH', '')
    tri_content('', names_d[0], '')
    empty_line(3)
    tri_content('WEST', '', 'EAST')
    tri_content(names_d[2], '', names_d[3])
    empty_line(3)
    tri_content('', 'SOUTH', '')
    tri_content('', names_d[1], '')
    empty_line(3)

    mid_headline(' Where do you want to go ')

    empty_line(1)
    tri_content('', '1 : North', '')
    empty_line(1)
    tri_content('2 : West', '', '3 : East')
    empty_line(1)
    tri_content('', '4 : South', '')
    empty_line(2)

    middle_line()

    empty_line(1)
    mid_content('0 : Back')
    empty_line(1)

    return _bottom(error)



def enter(error, p):
    'Print Enter Menu'

    _headergame(p)

    names_St=[
        'None',
        'None',
        'None',
        'None',
        'None',
        'None',
        'None',
        'None',
        'None',
    ]

    empty_line(2)
    tri_content(names_sT[0], names_sT[1], names_sT[2])
    empty_line(4)
    tri_content(names_sT[3], names_sT[4], names_sT[5])
    empty_line(4)
    tri_content(names_sT[6], names_sT[7], names_sT[8])
    empty_line(4)

    mid_headline(' What region to enter ')

    empty_line(1)
    tri_content('1 :'+names_sT[0], '2 :'+names_sT[1], '3 :'+names_sT[2])
    empty_line(1)
    tri_content('4 :'+names_sT[3], '5 :'+names_sT[4], '6 :'+names_sT[5])
    empty_line(1)
    tri_content('7 :'+names_sT[6], '8 :'+names_sT[7], '9 :'+names_sT[8])
    empty_line(2)

    middle_line()

    empty_line(1)
    mid_content('0 : Back')
    empty_line(1)

    return _bottom(error)



def smallTile(error,p):
    '''Print small Tile'''

    _headergame(p)

    empty_line(2)
    tri_content('', p.getSmallTileName(), '')
    tri_content('', p.getSmallTileDescription(), '')
    tri_content('', '', '')
    empty_line(2)
    tri_content('', 'ENTITY', '')
    tri_content('', p.searchEntity(), '')
    tri_content('', '', '')
    empty_line(2)
    tri_content('', 'ITEM', '')
    tri_content('', p.getItemName(), '')
    tri_content('', '', '')
    empty_line(2)

    mid_headline(' What do you want to do ')

    empty_line(1)
    tri_content('1 : Search', '2 : Take', '3 : Inventory')
    empty_line(1)
    tri_content('4 : Talk', '5 : Attack', '6 : Flee')
    empty_line(1)
    tri_content('', '7 : Sleep', '')
    empty_line(2)

    middle_line()

    empty_line(1)
    mid_content('0 : Back')
    empty_line(1)

    return _bottom(error)



def smallTile_search(error, c:str):
    '''Print small Tile search'''

    _headergame(p)

    empty_line(2)
    tri_content('', 'name', '')
    tri_content('', 'dec', '')
    tri_content('', '', '')
    empty_line(2)
    tri_content('', 'ENTITY', '')
    tri_content('', 'name', '')
    tri_content('', 'dec', '')
    empty_line(2)
    tri_content('', 'ITEM', '')
    tri_content('', 'name', '')
    tri_content('', 'value', '')
    empty_line(2)

    mid_headline(' You found... ')

    empty_line(3)
    mid_content(c)
    empty_line(4)

    middle_line()

    empty_line(1)
    mid_content('ENTER')
    empty_line(1)

    return _bottom(error)



def smallTile_take(error, c:str):
    '''Print small Tile take'''

    _headergame(p)

    empty_line(2)
    tri_content('', 'name', '')
    tri_content('', 'dec', '')
    tri_content('', '', '')
    empty_line(2)
    tri_content('', 'ENTITY', '')
    tri_content('', 'name', '')
    tri_content('', 'dec', '')
    empty_line(2)
    tri_content('', 'ITEM', '')
    tri_content('', 'name', '')
    tri_content('', 'value', '')
    empty_line(2)

    mid_headline(' You took... ')

    empty_line(3)
    mid_content(c)
    empty_line(4)

    middle_line()

    empty_line(1)
    mid_content('ENTER')
    empty_line(1)

    return _bottom(error)



def smallTile_talk(error, c:str):
    '''Print small Tile talk'''

    _headergame(p)

    empty_line(2)
    tri_content('', 'name', '')
    tri_content('', 'dec', '')
    tri_content('', '', '')
    empty_line(2)
    tri_content('', 'ENTITY', '')
    tri_content('', 'name', '')
    tri_content('', 'dec', '')
    empty_line(2)
    tri_content('', 'ITEM', '')
    tri_content('', 'name', '')
    tri_content('', 'value', '')
    empty_line(2)

    mid_headline(' You talk to... ')

    empty_line(3)
    mid_content(c)
    empty_line(4)

    middle_line()

    empty_line(1)
    mid_content('ENTER')
    empty_line(1)

    return _bottom(error)



def smallTile_attack(error, c:str):
    '''Print small Tile attack'''

    _headergame(p)

    empty_line(2)
    tri_content('', 'name', '')
    tri_content('', 'dec', '')
    tri_content('', '', '')
    empty_line(2)
    tri_content('', 'ENTITY', '')
    tri_content('', 'name', '')
    tri_content('', 'dec', '')
    empty_line(2)
    tri_content('', 'ITEM', '')
    tri_content('', 'name', '')
    tri_content('', 'value', '')
    empty_line(2)

    mid_headline(' You attacked... ')

    empty_line(3)
    mid_content(c)
    empty_line(4)

    middle_line()

    empty_line(1)
    mid_content('ENTER')
    empty_line(1)

    return _bottom(error)



def smallTile_flee(error, c:str):
    '''Print small Tile flee'''

    _headergame(p)

    empty_line(2)
    tri_content('', 'name', '')
    tri_content('', 'dec', '')
    tri_content('', '', '')
    empty_line(2)
    tri_content('', 'ENTITY', '')
    tri_content('', 'name', '')
    tri_content('', 'dec', '')
    empty_line(2)
    tri_content('', 'ITEM', '')
    tri_content('', 'name', '')
    tri_content('', 'value', '')
    empty_line(2)

    mid_headline(' You try to flee... ')

    empty_line(3)
    mid_content(c)
    empty_line(4)

    middle_line()

    empty_line(1)
    mid_content('ENTER')
    empty_line(1)

    return _bottom(error)



def smallTile_sleep(error, c:str):
    '''Print small Tile sleep'''

    _headergame(p)

    empty_line(2)
    tri_content('', 'name', '')
    tri_content('', 'dec', '')
    tri_content('', '', '')
    empty_line(2)
    tri_content('', 'ENTITY', '')
    tri_content('', 'name', '')
    tri_content('', 'dec', '')
    empty_line(2)
    tri_content('', 'ITEM', '')
    tri_content('', 'name', '')
    tri_content('', 'value', '')
    empty_line(2)

    mid_headline(' You sleep... ')

    empty_line(3)
    mid_content(c)
    empty_line(4)

    middle_line()

    empty_line(1)
    mid_content('ENTER')
    empty_line(1)

    return _bottom(error)



def inventory(error, p):
    '''Print inventory'''

    _headergame(p)

    names_iT = p.getItemsName()

    empty_line(1)
    tri_content('SLOT I', 'SLOT II', 'SLOT III')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)
    tri_content('SLOT IV', 'SLOT V', 'SLOT VI')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)
    tri_content('SLOT VII', 'SLOT VIII', 'SLOT IX')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)
    tri_content('SLOT X', 'SLOT XI', 'SLOT XII')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)

    mid_headline(' What do you want to do ')

    empty_line(3)
    di_content('1 : Use', '2 : Discard')
    mid_content('4 : Diary')
    empty_line(4)

    middle_line()

    empty_line(1)
    mid_content('0 : Back')
    empty_line(1)

    return _bottom(error)


'''
def inventory_eat(error, p):
    """Print inventory_eat"""

    _headergame(p)

    names_iT = p.getItemsName()

    empty_line(1)
    tri_content('Slot I', 'Slot II', 'Slot III')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)
    tri_content('Slot IV', 'SLOT V', 'SLOT VI')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)
    tri_content('SLOT VII', 'SLOT VIII', 'SLOT IX')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)
    tri_content('SLOT X', 'SLOT XI', 'SLOT XII')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)

    mid_headline(' Which Item do you want to eat ')

    empty_line(3)
    mid_content('Item from Slot')
    mid_content('(1-12)')
    empty_line(3)

    middle_line()

    empty_line(1)
    mid_content('0 : Back')
    empty_line(1)

    return _bottom(error)
'''


def inventory_use(error,p):
    '''Print inventory_use'''

    _headergame(p)

    names_iT = p.getItemsName()

    empty_line(1)
    tri_content('Slot I', 'Slot II', 'Slot III')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)
    tri_content('Slot IV', 'SLOT V', 'SLOT VI')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)
    tri_content('SLOT VII', 'SLOT VIII', 'SLOT IX')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)
    tri_content('SLOT X', 'SLOT XI', 'SLOT XII')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)

    mid_headline(' Which Item do you want to use ')

    empty_line(3)
    mid_content('Item from Slot')
    mid_content('(1-12)')
    empty_line(3)

    middle_line()

    empty_line(1)
    mid_content('0 : Back')
    empty_line(1)

    return _bottom(error)



def inventory_discard(error, p):
    '''Print inventory_discard'''

    _headergame(p)

    names_iT = p.getItemsName()

    empty_line(1)
    tri_content('Slot I', 'Slot II', 'Slot III')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)
    tri_content('Slot IV', 'SLOT V', 'SLOT VI')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)
    tri_content('SLOT VII', 'SLOT VIII', 'SLOT IX')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)
    tri_content('SLOT X', 'SLOT XI', 'SLOT XII')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(1)

    mid_headline(' Which Item do you want to discard ')

    empty_line(3)
    mid_content('Item from Slot')
    mid_content('(1-12)')
    empty_line(3)

    middle_line()

    empty_line(1)
    mid_content('0 : Back')
    empty_line(1)

    return _bottom(error)



def inventory_diary(error):
    '''Print inventory_diary'''

    _headergame(p)

    empty_line(2)
    tri_content('ENTRY I', 'ENTRY II', 'ENTRY III')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(2)
    tri_content('ENTRY IV', 'ENTRY V', 'ENTRY VI')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(2)
    tri_content('ENTRY VII', 'ENTRY VIII', 'ENTRY IX')
    tri_content('name', 'name', 'name')
    tri_content('', '', '')
    empty_line(2)

    mid_headline(' Which diary do you want to read ')

    empty_line(4)
    mid_content('Diary from Slot')
    mid_content('(1-9)')
    empty_line(3)

    middle_line()

    empty_line(1)
    mid_content('0 : Back')
    empty_line(1)

    return _bottom(error)



##############
# transistions
##############



# --- SHUT DOWN -------------------

# --- comment ---------------------
'''
GUI deeep 40
'''