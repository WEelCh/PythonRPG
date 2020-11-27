# AUTHOR : 
# DATE   : 

# --- DOCSTRING -------------------
'''
Executeable Main Document of the
"PythonRPG"

'''
# --- IMPORT ----------------------

from Modul import formating, submenus

from time import sleep

# --- DECLARATION -----------------

choise = False # takes user input & error status

# --- SETUP -----------------------

# --- MAIN ------------------------
while 'MAIN_LOOP':

    choise = (formating.menu(choise))

    if   choise == '0': # Exit
        break

    elif choise == '1': # Continue
        pass

    elif choise == '2': # New Game
        pass

    elif choise == '3': # Load Game
        pass

    elif choise == '4': # Settings
        pass

    else:
        choise = True # error message


# --- SHUT DOWN -------------------

exit()

# --- comment ---------------------

