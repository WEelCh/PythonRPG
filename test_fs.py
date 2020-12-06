# -------------------

__author__ ='Fabian Stange'

# ---- ---- import libraries ---- ----


# ---- ---- ---- ----

# ---- ---- global variables ---- ----
import Modul.classes.environment as environment
import  Modul.classes.player as player
# ---- ---- ---- ----
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
active_player.set
print(active_player.getCoordinates())

# ---- ---- code //  ---- ----