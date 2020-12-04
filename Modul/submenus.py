# AUTHOR : Elijah Zeidler
# DATE   : 

# --- DOCSTRING -------------------
'''

'''
# --- IMPORT ----------------------

from Modul import formating, loader

# --- DECLARATION -----------------


# --- SETUP -----------------------


# --- MAIN ------------------------

def continueGame():
    '''Logic for Menu-Continue
    Checks for last savegame and, if exist
    loads savegame'''

    game_value = loader.getSaveGame()

    if game_value == 'None':
        choise = False
        while 'CONTINUE_LOOP':
            choise = formating.noSaveGame(choise)
            if choise == '0':
                break
            else:
                choise = True
    else:
        pass
        #start savegame



def loadGame(choise = False):
    '''Logic for Menu-Load Game'''
    while 'LOADGAME_LOOP':

        choise = formating.loadGame(choise)

        if choise == '0':
            break
        else:
            choise = True



def settings(choise = False):
    '''Logic for Menu-Settings'''
    while 'SETTINGS_LOOP':

        choise = formating.settings(choise)

        if   choise == '0': # Back
            break

        elif choise == '1': # Format Window
            settingsFormat()

        elif choise == '2': # Delete User-Data
            settingsDelete()

        else:
            choise = True # error message


def settingsFormat(choise = False):
    '''Logic for  Menu-Settings-FormatWindow'''
    while 'FORMATWINDOW_LOOP':

        choise = formating.settingsFormatWindow(choise)
        new_form_y, new_form_x, s = '', '', True

        if   choise == '0': # Back
            break

        else: # search for format config
            for i in range(len(choise)):

                if s == True:
                    if choise[i].isdecimal():
                        new_form_y += choise[i]
                    elif choise[i].isspace():
                        s = False
                        continue
                    else:
                        choise = True
                        break

                if s == False:
                    if choise[i].isdecimal():
                        new_form_x += choise[i]
                    else:
                        choise = True
                        break

            if (new_form_y == '') or (new_form_x == ''):
                choise = True
                continue
            elif choise == True:
                continue 

            # if input was ok, overwrite old values
            loader.setYXformat(new_form_y, new_form_x)
            formating.form_y,formating.form_x = loader.getYXformat()


def settingsDelete():
    pass


# --- SHUT DOWN -------------------


# --- comment ---------------------

