# PythonRPG
Who knows what lies beneath ||
|| two beginner classes able to be choosen from:
---
## MAGE:
 - higher intelligence
 - health +
 - pre-equipped spells - heal and damage spell
 - ...
## Knight/Warrior:
 - higher strength
 - health ++
 - pre-equipped weapons - shield and short sword
 - ...

> intelligence and strength (maybe some more later) are attributes
> work as multiplier of base damage of a weapon/spell if they hold a specific type
> swords gain strenght*2 for example // -- needs balancing
> effects like fire or electrical deal 1.8 the origin damage of the weapon on enemies with these weaknesses

### Generating the world:
 - everything discovered gets saved and reloaded after new game. 
 - base / camp / housing starts at 0|0 > north 1|0 east 0|1 south -1|0 and west 0|-1 
 - if player travels to these fields, they get generated with a value, written in a dictionary and are available to be read out during the game. 
 