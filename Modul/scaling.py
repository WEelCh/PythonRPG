# -------------------

__author__ ='Fabian Stange'

# ---- ---- Import ---- ----
import Modul.loader as loader
# ---- ---- Import END ---- ----

# ---- ---- Description Docstring BEGIN ---- ----
'''
File is used to make percentual generation of:
- spawning of Items,
- spawning of Entities,
- lockCondition of SmallTiles
- Item generation 
- Entity generation 
- scaling of basic attributes 
etc. easier to access and modify. 
'''
# ---- ---- Description Docstring END ---- ----


# ---- ---- code //  ---- ----
keys = [1,1,1,1,2,2,2,3,3,4,5]
lock_condition = [ #6/10 opened || 4/10 locked
    'locked',
    'locked',
    'locked',
    'locked',
    'opened',
    'opened',
    'opened',
    'opened',
    'opened',
    'opened',
]

item_percentage = [ # 6/10 random item || 4/10 Nothing
    None,
    None,
    None,
    None,
    loader.genItem(),
    loader.genItem(),
    loader.genItem(),
    loader.genItem(),
    loader.genItem(),
    loader.genItem(),
]

entity_percentage = [ # 6/10 random entity || 4/10 Nothing
    None,
    None,
    None,
    None,
    None,
    loader.genEntity(),
    loader.genEntity(),
    loader.genEntity(),
    loader.genEntity(),
    loader.genEntity(),
]

def getClassAttributes(type_input):
    
    if type_input == 'Mercenary': 
        player_list = [
        20,    #health = 0
        20,    #max_health = 1
        20,    #stamina = 2
        20,    #max_stamina = 3
        20,    #mana = 4
        20,    #max_mana = 5
        20,    #strength = 6
        20,    #intelligence = 7
        20,    #perception = 8 
        [       #items_backpack = []
            ['Weapon','knob',10],
            ['Weapon','the penetrator',10],
            ['Food','Apple',10,10],
            ['Food','Apple',10,10],
            ['MedicalSupply','Syringe',10,10],
        ]
        
        ]
    elif type_input == 'Illusionist':
        player_list = [
        20,    #health = 0
        20,    #max_health = 1
        20,    #stamina = 2
        20,    #max_stamina = 3
        20,    #mana = 4
        20,    #max_mana = 5
        20,    #strength = 6
        20,    #intelligence = 7
        20,    #perception = 8 
        [       #items_backpack = []
            ['Weapon','knob',10],
            ['Weapon','the penetrator',10],
            ['Food','Apple',10,10],
            ['Food','Apple',10,10],
            ['MedicalSupply','Syringe',10,10],
                ]
        ]
    elif type_input == 'Stinker':
        player_list = [
        20,    #health = 0
        20,    #max_health = 1
        20,    #stamina = 2
        20,    #max_stamina = 3
        20,    #mana = 4
        20,    #max_mana = 5
        20,    #strength = 6
        20,    #intelligence = 7
        20,    #perception = 8 
        [       #items_backpack = []
            ['Weapon','knob',10],
            ['Weapon','the penetrator',10],
            ['Food','Apple',10,10],
            ['Food','Apple',10,10],
            ['MedicalSupply','Syringe',10,10],
                ]
        ]
    elif type_input == 'Scout':
        player_list = [
        20,    #health = 0
        20,    #max_health = 0
        20,    #stamina = 0
        20,    #max_stamina = 0
        20,    #mana = 0
        20,    #max_mana = 0
        20,    #strength = 0
        20,    #intelligence = 0
        20,    #perception = 0 
        [       #items_backpack = []
            ['Weapon','knob',10],
            ['Weapon','the penetrator',10],
            ['Food','Apple',10,10],
            ['Food','Apple',10,10],
            ['MedicalSupply','Syringe',10,10],
                ]
        ]
    return player_list