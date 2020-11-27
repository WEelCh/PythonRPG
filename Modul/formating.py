# AUTHOR : Elijah Zeidler
# DATE   : 

# --- DOCSTRING -------------------
'''
Handles the formating for the project

Functions take contents and visualize 
them in standardized format

'''
# --- IMPORT ----------------------

import os

# --- DECLARATION -----------------

clear = lambda : os.system('cls')

# display formating values
form_y, form_x = 6, 44

# static lines
upper_line  =lambda  : print(' '*form_x + '╔'+'═'*120+'╗')
middle_line =lambda  : print(' '*form_x + '╠'+'═'*120+'╣')
lower_line  =lambda  : print(' '*form_x + '╚'+'═'*120+'╝')

empty_line  =lambda n: [print(' '*form_x + '║'+' '*120+'║') for i in range(n)]
space_line  =lambda n: [print() for i in range(n)]

input_line  =lambda m: str(input(' '*form_x+m+' '*36))

# dynamic lines
norm_content=lambda c: print(' '*form_x+'║ '+c+'║')
mid_content =lambda c: print(' '*form_x+'║' +c.center(120)+'║')

# static info-values
_title_  = 'P Y T H O N - R P G'
_date_   = '2020'
_author_ = ' Stange Fabian'+' '*89+'Zeidler Elijah  '

# --- SETUP -----------------------

# --- MAIN ------------------------


def _bottom(error):
    '''Print the bottom of the standardized format'''

    lower_line()

    if error == True:
        message = ' Your Input was invalid:'
    else:
        message = ' '*24

    return input_line(message)



def _headermenu():
    '''Print the header of the menu'''

    upper_line()
    empty_line(1)
    mid_content(_title_)
    empty_line(1)
    norm_content(_author_)
    mid_content(_date_)
    empty_line(1)
    middle_line()



def menu (error = False):
    '''Show the Menu'''

    clear()
    space_line(form_y)
    _headermenu()

    empty_line(4)

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



def settings(error = False):
    '''Show the Settings-menu'''

    clear()
    space_line(form_y)
    _headermenu()

    empty_line(1)

    mid_content('Format Window')
    mid_content('1')
    empty_line(1)
    mid_content('Delete User-Data')
    mid_content('2')
    empty_line(1)
    mid_content('Back')
    mid_content('0')

    empty_line(1)

    return _bottom(error)



# --- SHUT DOWN -------------------

# --- comment ---------------------
'''
deeep 40
'''