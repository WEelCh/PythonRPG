# main file adventure game
# ++++++++++++++++++++++++
import room, player, character
# settings

# creating rooms
kitchen = room.Room("kitchen","a small and smelly room full of dishes")
diningroom = room.Room("diningroom","a room with candles and a round table in the center")
chamber = room.Room("chamber","a small, dark and dusty room")


print(kitchen.get_room_name())
print(kitchen.get_description())
# link rooms
# chamber kitchen diningroom
# bedroom wintergarden bathroom

kitchen.link_room(chamber, "west")
kitchen.link_room(diningroom, "east")
kitchen.show_linked_rooms()

chamber.link_room(kitchen, "east")
chamber.show_linked_rooms()

diningroom.link_room(kitchen, "west")
diningroom.show_linked_rooms()



# create a player

player1 = player.Player("Homer","What a moron")
player1.set_current_room(kitchen)
print(player1.get_player_name())
print(player1.get_current_room().get_room_name())

# create characters
dave = character.Enemy("Dave","a smelly zombie",diningroom,"cheese")
diningroom.set_inhabitant(dave)

esmeralda = character.Friend("Esmeralda Wetterwachs","a haggard old witch",chamber,"dagger")
chamber.set_inhabitant(esmeralda)

#++++++++++++++++++++++++++++++++++++++++++++
# main
#++++++++++++++++++++++++++++++++++++++++++++
command = "go_on"
while command !="quit":
    print("Which direction do you want to go?")
    command = input("east|south|west|north  or quit ")
    player1.move(command)
    print(player1.get_current_room().get_room_name())
    if player1.get_current_room().get_inhabitant()!=None:
        enemy = player1.get_current_room().get_inhabitant()
        print(enemy.get_name(),enemy.get_description())



