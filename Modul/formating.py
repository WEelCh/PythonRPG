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

# --- DECLARATION -----------------

# clear function in relation to OS
system_check = platform.system()
if  (system_check.lower() == 'linux') or (system_check.lower() == 'darwin'): 
    clear=lambda: os.system('clear')
elif(system_check.lower() == 'windows'):
    clear=lambda: os.system('cls')

# display formating values
form_y, form_x = loader.getYXFormat()

# static lines
upper_line  =lambda  : print(' '*form_x + '╔'+'═'*121+'╗')
middle_line =lambda  : print(' '*form_x + '╠'+'═'*121+'╣')
midUpT_line =lambda  : print(' '*form_x + '╠'+'╦'.center(121,'═')+'╣')
midX_line   =lambda  : print(' '*form_x + '╠'+'╬'.center(121,'═')+'╣')
midDwTT_line=lambda  : print(' '*form_x + '╠'+'╩'.center(121,'═')+'╠')
lower_line  =lambda  : print(' '*form_x + '╚'+'═'*121+'╝')

empty_line  =lambda n: [print(' '*form_x + '║'+' '*121+'║') for i in range(n)]
emptyT_line =lambda n: [print(' '*form_x + '║'+'║'.center(121)+'║') for i in range(n)]
space_line  =lambda n: [print() for i in range(n)]

input_line  =lambda m: str(input(' '*form_x+m+' '*37))

# dynamic lines
norm_content=lambda c: print(' '*form_x+'║ '+c+'║')
mid_content =lambda c: print(' '*form_x+'║' +c.center(121)+'║')
midT_content=lambda c1, c2: print(' '*form_x+'║' +c1.center(60)+'║'+c2.center(60)+'║')

# static info-values
_title_  = 'P Y T H O N - R P G'
_date_   = '2020'
_author_ = ' Stange Fabian'+' '*90+'Zeidler Elijah  '

# --- SETUP -----------------------

# --- MAIN ------------------------

# chunks

def _headermenu(path, T = False):
    '''Print header of menu'''

    upper_line()
    empty_line(1)
    mid_content(_title_)
    empty_line(1)
    norm_content(_author_)
    mid_content(_date_)
    empty_line(1)
    mid_content(''+path)
    if T == True:
        midUpT_line()
    else:
        middle_line()



def _bottom(error):
    '''Print bottom of standardized format'''

    lower_line()

    if error == True:
        message = ' Your Input was invalid:'
    else:
        message = ' '*24

    return input_line(message)

# generell menu

def menu (error = False):
    '''Show Menu'''

    clear()
    space_line(form_y)
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

    clear()
    space_line(form_y)
    _headermenu('MENU / CONTINUE')

    empty_line(8)

    mid_content('No last played SaveGame found !')
    empty_line(10)
    mid_content('Back')
    mid_content('0')

    empty_line(9)

    return _bottom(error)



def loadGame(error):
    '''Show Menu-Load Game'''

    clear()
    space_line(form_y)
    _headermenu('MENU / LOAD GAME', T = True)

    emptyT_line(1)
    midT_content('foo', 'foo')
    emptyT_line(1)

    midX_line()

    emptyT_line(1)
    midT_content('foo', 'foo')
    emptyT_line(1)

    midDwTT_line()
    empty_line(1)
    mid_content('Back')
    mid_content('0')
    empty_line(1)

    return _bottom(error)



def settings(error = False):
    '''Show Menu-Settings'''

    clear()
    space_line(form_y)
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

    clear()
    space_line(form_y)
    _headermenu('MENU / SETTINGS / FORMAT WINDOW')

    empty_line(2)

    mid_content('Y Axes Formating')
    mid_content(str(form_y))
    mid_content('Number of clear lines above the menu.')
    empty_line(2)
    mid_content('Y Axes Formating')
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
    pass

# --- SHUT DOWN -------------------

# --- comment ---------------------
'''
GUI deeep 40
'''