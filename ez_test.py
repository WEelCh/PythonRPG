'''
from Modul.classes.item import Weapon

food1 = Weapon(0,0,0)
food1.generate(0)

print(food1.getatk())
'''

import Modul.loader as loader

loader.resetSaveGame(1)