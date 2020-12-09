# AUTHOR : Elijah Zeidler
# DATE   : 

# --- DOCSTRING -------------------
'''

'''
# --- IMPORT ----------------------

import main_game
from Modul import formating, loader
#from Modul.classes import player

# --- DECLARATION -----------------


# --- SETUP -----------------------


# --- MAIN ------------------------

def continueGame():
    '''Logic for Menu-Continue
    Checks for last savegame and, if exist
    loads savegame'''

    game_value = loader.getLastSaveGame()

    if game_value == 'None':
        choice = False
        while 'CONTINUE_LOOP':
            choice = formating.noSaveGame(choice)
            if choice == '0':
                break
            else:
                choice = True
    else:
        pass
    main_game.game()
        #start savegame



def newGame(choice = False, level = 1):
    '''Logic for Menu-New Game
    Gets Player Data from the User'''
    data = []
    for i in range(1,5):
        data.append(loader.getSaveGame(i))
    player_data = []
    while 'NEWGAME_LOOP':

        choice = formating.newGame(choice, level, data)

        if  choice == '0':
            break

        elif level == 1: # SaveGame choice
            if   choice in list(['1','2','3','4']):
                player_data.append(int(choice))
            else:
                choice = True
                continue

        elif level == 2: # Name choice
            if len(choice) > 15:
                choice = True
                continue
            player_data.append(choice)

        elif level == 3: # Sex choice
            if   choice == '1':
                player_data.append('Male')
            elif choice == '2':
                player_data.append('Female')
            elif choice == '3':
                player_data.append('Diverse')
            else:
                choice = True
                continue

        elif level == 4: # Class choice
            if   choice == '1':
                player_data.append('Mercenary')
            elif choice == '2':
                player_data.append('Stinker')
            elif choice == '3':
                player_data.append('Scout')
            elif choice == '4':
                player_data.append('Illusionist')
            else:
                choice = True
                continue

        level += 1
        if level == 5:
            #activ_player = player.Player(player_data)
            '''START_GAME (activ_player)'''
            break



def loadGame(choice = False):
    '''Logic for Menu-Load Game'''
    data = []
    for i in range(1,5):
        data.append(loader.getSaveGame(i))
    while 'LOADGAME_LOOP':

        choice = formating.loadGame(choice, data)

        if   choice == '1':
            if data[0][1] == '---': # no class
                choice = True

        elif choice == '2':
            if data[1][1] == '---': # no class
                choice = True

        elif choice == '3':
            if data[2][1] == '---': # no class
                choice = True

        elif choice == '4':
            if data[3][1] == '---': # no class
                choice = True

        elif choice == '0':
            break
        else:
            choice = True



def settings(choice = False):
    '''Logic for Menu-Settings'''
    while 'SETTINGS_LOOP':

        choice = formating.settings(choice)

        if   choice == '0': # Back
            break

        elif choice == '1': # Format Window
            settingsFormat()

        elif choice == '2': # Delete User-Data
            settingsDelete()

        else:
            choice = True # error message


def settingsFormat(choice = False):
    '''Logic for  Menu-Settings-FormatWindow'''
    while 'FORMATWINDOW_LOOP':

        choice = formating.settingsFormatWindow(choice)
        new_form_y, new_form_x, s = '', '', True

        if   choice == '0': # Back
            break

        else: # search for format config
            for i in range(len(choice)):

                if s == True:
                    if choice[i].isdecimal():
                        new_form_y += choice[i]
                    elif choice[i].isspace():
                        s = False
                        continue
                    else:
                        choice = True
                        break

                if s == False:
                    if choice[i].isdecimal():
                        new_form_x += choice[i]
                    else:
                        choice = True
                        break

            if (new_form_y == '') or (new_form_x == ''):
                choice = True
                continue
            elif choice == True:
                continue 

            # if input was ok, overwrite old values
            loader.setYXFormat(new_form_y, new_form_x)
            formating.form_y,formating.form_x = loader.getYXFormat()
            formating.x = formating.get_x()


def settingsDelete():
    '''Logic for Menu-Settings-Delete'''
    choice = False
    while 'Delete':

        choice  = formating.settingsdeleteuserdata(choice)

        if choice == 'DeLeTe':
            for i in range(1,5):
                loader.resetSaveGame(i)
            loader.resetSettings()
            formating.clear()
            exit()
        elif choice == '0':
            break
        else:
            choice = True


# --- SHUT DOWN -------------------


# --- comment ---------------------

