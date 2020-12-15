# Python RPG 
---
Initiated as a project solely for school, we have begun developing this little cmd game right after we declared our inital goals.
We wanted to make a game, focused on travelling trough worlds, experiencing the story of our protagonist whilst also looting and fighting monster with a rather simple combat system. 


## Classes and Scaling
---
## The Character and Classes

Before starting to play you enter all the necessary information and values about your character, mostly these are your sex, name, and some other attributes. 
During that process you also have to choose between four given classes: 
The Mercenary, The Stinker, The Illusionist and the Scout. 
Here, the Mercenary marks the basic and easiest character with a rather balanced loadout and solid stats to begin the game with. 
With further development the class of the Illusionist and some more will gain certain importance and different focuses, like Spell casting, meleed or ranged damage and some more. 
The more time and motivation we got, the more we will  result with. 

### Scaling

Troughout the progress of the game, you need a certain way to improve your character otherwise it will become boring pretty soon. 
In order to fix this possible problem, we've added a simple system to make scaling  dependent on how much you've explored already. We might adjust that whole system troughout game changes and maybe switch to an experience based leveling system later, but right it's mostly focused on this value. 

## World Generation 

You can imagine our world as an cartesian coordinate system. There are four directions you can travel to - North, East, South, West - and each simply changes the active coordinate of our player to the given direction. These coordinates indicate your current position on that system, which is divided into big squares. Each square is a (BigTile) holding the coordinates it was given, and it also yields a theme, like city, military camp, simple environment or certain other areas. Upon discovering these areas 9 smaller tiles within that BigTile are generated. With certain percentage each of these tiles spawns an item and an enemy. The player then could explore them to find loot - later experience trough combat or new items due to trades with friendly npcs- or simply go on to the next tile. 
Upon returning these tiles get loaded again, or a new one gets generated. 

## Future plans: 

- better Ui - maybe even a graphical interface 
- more types of entities 
- new world generation 
- experience system 
- new combat system 
- enhanced character traits 