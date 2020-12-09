# AUTHOR : Elijah Zeidler
# DATE   : 

# --- DOCSTRING -------------------
'''

'''
# --- IMPORT ----------------------

from Modul import loader, formating
from Modul.classes import player

# --- DECLARATION -----------------



# --- SETUP -----------------------

def initGame(attr:list):
    '''player'''

    p = player.Player(attr)
    return p

# --- MAIN ------------------------

def game ():
    '''Logic for BIG TILE'''
    p = initGame([1,'Dev', 'Male', 'Mercenary'])
    choice = False
    while 'BIG_TILE':

        choice = formating.bigTile(choice, p)

        if   choice == '1': # Travel
            while 'travel':
                choice = formating.travel(choice, p)
                if   choice in '1234' and len(choice)==1:
                    if choice == '1':
                        p.goNorth()
                    elif choice == '2':
                        p.goWest()
                    elif choice == '3':
                        p.goEast()
                    elif choice == '4':
                        p.goSouth()
                elif choice == '0':
                    break
                else:
                    choice = True

        elif choice == '2': # Enter
            while 'enter':
                choice = formating.enter(choice,p)
                if   choice in '123456789' and len(choice)==1:
                    p = game_smallTile(choice,p)
                    break
                elif choice == '0':
                    break
                else:
                    choice = True

        elif choice == '3': # Inventory
            game_inventory()

        elif choice == '0': # Save & Quit
            # format . leave
            break # leave game

        else: # error
            choice = True
            continue



def game_smallTile(tile_no,p):
    ''' Logic for SMALL TILE'''
    choice = False
    while 'SMALL_TILE':

        choice = formating.smallTile(choice)

        if   choice == '1': # Search
            '''DEBUGG check game data for item'''
            c = p.getItemName()
            formating.smallTile_search(False, c)

        elif choice == '2': # Take
            '''DEBUGG check game data for item'''
            c = p.searchItem()
            formating.smallTile_take(False, c)

        elif choice == '3': # Inventory
            game_inventory()

        elif choice == '4': # Talk
            '''DEBUGG check game data for entity'''
            c = p.searchEntity()
            formating.smallTile_talk(False, c)

        elif choice == '5': # Attack
            '''DEBUGG check game data for entity'''
            c = p.searchEntity()
            formating.smallTile_attack(False, c)

        elif choice == '6': # Flee
            '''DEBUGG check for flee'''
            c = 'flee_status'
            formating.smallTile_flee(False, c)

        elif choice == '7': # Sleep
            '''DEBUGG check for sleep'''
            c = p.playerRest()
            formating.smallTile_sleep(False, c)

        elif choice == '0': # Back
            '''DEBUGG check for enemy- status
            if no enemy --> break
            if enemy --> not possible'''
            break

    return p



def game_inventory():
    '''Logic for Inventory'''
    choice = False
    while 'INVENTORY':

        choice = formating.inventory(choice)
        '''
        if   choice == '1': # Eat
            while 'eat':
                choice = formating.inventory_eat(choice)
                """DEBUGG check for eadability"""
                if choice in '123456789' and len(choice)==1:
                    pass
                elif choice in ['10','11','12']:
                    pass
                elif choice == '0':
                    break
                else:
                    choice = True
        '''
        if choice == '1': # Use
            while 'use':
                choice = formating.inventory_use(choice)
                '''DEBUGG check for useability'''
                if choice in '123456789' and len(choice)==1:
                    pass
                elif choice in ['10','11','12']:
                    pass
                elif choice == '0':
                    break
                else:
                    choice = True

        elif choice == '2': # Discard
            while 'discard':
                choice = formating.inventory_discard(choice)
                '''DEBUGG check'''
                if choice in '123456789' and len(choice)==1:
                    pass
                elif choice in ['10','11','12']:
                    pass
                elif choice == '0':
                    break
                else:
                    choice = True

        elif choice == '4': # diary
            game_diary()

        elif choice == '0': # Back
            break

        else:
            choice = True



def game_diary():
    '''Logic for Diary'''
    choice = False
    while 'diary':

        choice = formating.inventory_diary(choice)

        if choice in '123456789' and len(choice) == 1:
            '''DEBUGG load the shitty logs'''
            pass
        elif choice == '0':
            break
        else:
            choice = True

# --- SHUT DOWN -------------------



# --- comment ---------------------


