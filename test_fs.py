# -------------------

__author__ ='Fabian Stange'

# ---- ---- import libraries ---- ----


# ---- ---- ---- ----

# ---- ---- global variables ---- ----
import Modul.classes.environment as environment
import  Modul.classes.player as player
from Modul.loader import saveTile,resetSaveGame,savePlayer
# ---- ---- ---- ----
#saveTile(None,'0_0',1)
choice = input('yes or no')

if choice == 'yes':
    resetSaveGame(1)
    resetSaveGame(2)
    resetSaveGame(3)
    resetSaveGame(4)
else:    
    list_player = [
        1,
        None,#'fabian',
        None,#'male',
        None#'Mercenary',
        
    ]
    active_player = player.Player(list_player)
    active_player.initializePlayer(1)
    print(active_player.getCoordinates())
    print(active_player.getName(),active_player.getSavegame(),active_player.getSex(),active_player.getCharClass(),active_player.getItemsName())
    print(active_player.listHealth())
    active_player.treatHealth(1,[10,active_player.getMaxHealth()])
    print(active_player.listHealth())
    print(active_player.listMana())
    print(active_player.goEast())
    print(active_player.getCoordinates())
    for i in range(90):
        print(active_player.goNorth())
        print(active_player.getActiveTileName())
        print(active_player.getCoordinates())
    print('END')
    savePlayer(active_player,1)
# ---- ---- code //  ---- ----