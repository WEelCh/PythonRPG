# -------------------

__author__ ='Fabian Stange'

# ---- ---- import libraries ---- ----


# ---- ---- ---- ----

# ---- ---- global variables ---- ----
import Modul.classes.environment as environment
import  Modul.classes.player as player
from Modul.loader import saveTile
# ---- ---- ---- ----
#saveTile(None,'0_0',1)

list_player = [
    1,
    'fabian',
    'male',
    'Mercenary',
    
]
active_player = player.Player(list_player)
print(active_player.getName(),active_player.getSavegame(),active_player.getSex(),active_player.getCharClass())
print(active_player.listHealth())
active_player.treatHealth(1,[10,active_player.getMaxHealth()])
print(active_player.listHealth())
print(active_player.listMana())
print(active_player.goEast())
print(active_player.getCoordinates())
# ---- ---- code //  ---- ----
