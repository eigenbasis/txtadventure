# eigen trying to make a text adventure game in python
# you'll have a condition blaahhh

import os
import time
import random
from random import randint
import pickle

#Character defaults
inventory = []
condition = []

#Start player in room 1
player_location = 1

def print_header():
    print ("""
     __       __)                        
(, )  |  /          /)               
   | /| / _  __   _(/  _  __   _  __ 
   |/ |/ (_(_/ (_(_(__(/_/ (__(/_/ (_
   /  |                              
                                     
    """)
def help():
    print ("""
Welcome to Wanderer. 
Type GO and direction to move. 
Type TAKE and items name to pick things up.
Type CHECK and items name to get more information about the item.
To use items type USE item's name ON item's name
Type INVENTORY at any point to see your inventory.
Type CONDITION at any point to see your condition.
Type HELP at any point to see this again.
Type LOAD to load your previous game.
The game auto-saves after every move.
""")
#Show start screen
print_header()
help()

delay = raw_input("press ENTER to continue.")


class Room:
	def __init__(self, introduction, description, n, s, e, w, u, d):
		self.introduction = introduction
		self.description = description
		self.n = n
		self.s = s
		self.e = e
		self.w = w
		self.u = u
		self.d = d
	

#Create dictionary of rooms
rooms = {}
#rooms[] = Room(introduction, description, 0n, 0s, 0e, 0w, 0u, 0d)
rooms[1] = Room("beginning", "you are in a middle of a path. it's hard to tell if it's early morning\
 or late evening. everything seems grey. to your north there are some bushes. to your west\
 there's a small hosue. it seems empty, but in good condition. the door is slightly ajar. \
 to your east there lays a river.", 3, 0, 2, 4, 0, 0)
rooms[2] = Room("river", "the river is wide, but moves slugishly as if the water was packed with something\
 dense. it spreads further to the east", 0, 0, 5, 1, 0, 0)
rooms[3] = Room("bushes", "the bushes look dense, but comfortable. there seems to be a path crawling between\
 them to the north.", 7, 1, 0, 0, 0, 0)
rooms[4] = Room("house", "there seems to be only one room. it's well kept. there's a fireplace, a table\
 and a bed in the room.", 0, 0, 1, 0, 0, 0)
rooms[5] = Room("deep river", "you stand knee deep in the river. the water slugs around you dampens your\
 legs. you can see a shore forther to east.", 0, 0, 6, 2, 0, 0)
rooms[6] = Room("shore", "a wide shore with the river to your west and road to north. a man sits on a stump.", 14, 0, 0, 5, 0, 0)
rooms[7] = Room("path", "you push yourself thorugh bushes and come out to a small path that winds through\
 a field further to north. there's a twig stuck in your hair.", 8, 3, 12, 13, 0, 0)
rooms[8] = Room("meadow edge", "you come to an edge of a meadow. it thickens to the north. there's a forest\
to the west and the keeps marking the eadge of a field to the east.", 9, 7, 11, 10, 0, 0)
rooms[9] = Room("meadow", "otherways bare field with some grass stalks in it. a few simple flowers bloom here and there.", 0, 8, 0, 0, 0, 0)
rooms[10] = Room("forest", "it's a forest. green and moist. there's a stone with a frog sitting atop of it.", 0, 13, 8, 0, 0, 0)
rooms[11] = Room("field path", "field runs along the field.", 0, 12, 8, 0, 0, 0)
rooms[12] = Room("field", "there used to be crops here. there are none here now, but there's a big,\
broken cart in the middle of it.", 11, 0, 0, 7, 0, 0)
rooms[13] = Room("field", "it lays barren even though the earth looks rich. a thick forest spreads to north.", 10, 0, 7, 0, 0, 0)
rooms[14] = Room("road", "root riddled cobblestone road twists to north with a cave to the east.", 15, 6, 0, 0, 0, 0)
rooms[15] = Room("cobble road", "the road streatches on. there's a cave to the east with a menecing, gaping hole for an entrance.\
an old house to the north.", 17, 14, 16, 0, 0, 0)
rooms[16] = Room("cave", "moist and damp and dripping. mud slashes against your feet.", 0, 0, 0, 15, 0, 0)
rooms[17] = Room("old hosue", "you would call it 'rustic' if you wanted to sell it. there's an old plum lady sitting on a bench\
 next to it's doors.", 0, 15, 0, 0, 0, 0)
rooms[18] = Room("pending", "the young lady told you", 0, 0, 4, 0, 0, 0)

class Item:
    #Initialize the item class
    def __init__(self, name, description, location, movable, state, need_item, interaction, activated):
        self.name = name
        self.description = description
        self.location = location
        self.movable = movable
        self.state = state
        self.need_item = need_item
        self.interaction = interaction
        self.activated = activated
    
#Create dictionary of items

items = {}

#items[] = Item(name, description, location, movable, state, need_item, interaction, activated)
items[1] = Item("matches", "a regular box of matches.", 4, True, "dry", "none", "default", False)
items[2] = Item("fireplace", "the fireplace seems in good conditon. it's cold, but there are some firewood\
 in it.", 4, False, "cold", "matches", "you manage to light the fire, the room fills with warmth", False)
items[3] = Item("bed", "the bed is simple, but made. it looks fit to LAY IN it.", 4, False, \
    "made", "none", "you lay in bed for a while and feel rested", False)
items[4] = Item("stone", "a silky smooth and small stone. warm to the touch.", 2, True, \
    "it's warm to the touch", "none", "default", False)
items[5] = Item("table", "the table is dusty but for a spot in the middle which is shinny clean. \
there's a box of matches on the table.", 4, False, "it's just a table", "none", "there is a box of \
matches on the table", False)
items[6] = Item("twig", "a small twig. dry and brittle.", 3, True, "whole", "none", "none", False)
items[7] = Item("cart", "used to be pulled by horses. they are in different fields now. a showel lies next to it", 12, False, \
    "broken. your stare won't fix them", "none", "something might happen", False)
items[8] = Item("frog", "a weary looking frog sits on a stone and lazily looks at you. it seems a bit hungry.", 10, False,\
    "hunry", "worm", "the frog looks at you and something resembling smile spreads on its face.", False)
items[9] = Item("worm", "a thick and juicy worm", 13, True, "juicy", "showel", "you pick up the worm and show it behind your coral", False)
items[10] = Item("showel", "a tool for digging", 12, True, "whole", "none", "the showel seems sturdy", False)
items[11] = Item("field", "full of rich soil", 13, False, "whole", "showel", "you struck ground and lift revealing a fat worm", False)
items[12] = Item("flower", "simple light blue petals around a twig", 9, True, "whole", "none", "you take the flowe. it shivers \
and rests", False)
items[13] = Item("man", "stumping on a stump. he's grinning and there is something stuck between his oddly edged teeth", \
    6, False, "stumping", "twig", "he showes the twig between his teeth, nudges the thing out, takes a deep breath", False)
items[14] = Item("peach", "the red is almost seeping out of it", 6, True, "whole", "man", "none", False)
items[15] = Item("key", "might be a finger", 6, True, "whole", "man", "none", False)
items[16] = Item("coin", "one side of it is visibly worn", 6, True, "whole", "man", "none", False)
items[17] = Item("mud", "squishy clump of earth", 16, True, "moist", "none", "none", False)
items[18] = Item("lady", "her face has seen better fruits.", 17, False, "plum", "peach", "her skin shrinks, then expands and smoothens", False)

###main LOOP

while True:
    #Print header
    try:
        #Describe location
        print ("_____________________")
        print ("You are in " + rooms[player_location].introduction + ".\n")
        print (rooms[player_location].description)
        print ("_____________________")

        #Get players command
        move = raw_input("\n> ").lower().split()

        #If they type "go" first they can move
        if move[0] == "go":
            if move[1] == "north":
                if rooms[player_location].n != 0:
                    player_location = rooms[player_location].n
                else:
                    print("there is nowhere to go there")
            if move[1] == "south":
                if rooms[player_location].s != 0:
                    player_location = rooms[player_location].s
                else:
                    print("there is nowhere to go there")
            if move[1] == "east":
                if rooms[player_location].e != 0:
                    player_location = rooms[player_location].e
                else:
                    print("there is nowhere to go there")
            if move[1] == "west":
                if rooms[player_location].w != 0:
                    player_location = rooms[player_location].w
                else:
                    print("there is nowhere to go there")
            if move[1] == "up":
                if rooms[player_location].u != 0:
                    player_location = rooms[player_location].u
                else:
                    print("there is nowhere to go there")
            if move[1] == "down":
                if rooms[player_location].d != 0:
                    player_location = rooms[player_location].d
                else:
                    print("there is nowhere to go there")

        #Taking items in storing them in inventory
        if move[0] == "take":
            for iid in range(1, len(items)+1):
                if move[1] == items[iid].name and items[iid].location == player_location and items[iid].movable == True:
                    inventory.append(items[iid].name)
                if move[1] == items[iid].name and items[iid].location == player_location and items[iid].movable == False:
                    print ("...It won't budge...")

        #Checking items
        if move[0] == "check":
            for iid in range(1, len(items)+1):
                if move[1] == items[iid].name and (items[iid].location == player_location or move[1] in inventory):
                    print ("++++++++++++++++++")
                    print (items[iid].description)
                    print ("++++++++++++++++++")

        #Use item
        if move[0] == "use" and move[2] == "on":
            for iid in inventory:
                for iiid in range(1, len(items)+1):
                    if move[1] == iid and (move[3] == items[iiid].name and player_location == items[iiid].location and move[1] == items[iiid].need_item):
                        print ("+++++++++++++++++++++")
                        print (items[iiid].interaction)
                        print ("+++++++++++++++++++++")
                        items[iiid].activated = True

        #Get help
        if move[0] == "help":
            help()
            continue

        #Check inventory
        if move[0] == "inventory":
            print ("|------------------------|")
            print (inventory)
            print ("|------------------------|")
            continue

        #Check condition
        if move[0] == "condition":
            print ("|------------------------|")
            print (condition)
            print ("|------------------------|")
            continue

        #Load previous game
        if move[0] == "load":
            with open("savefile.dat", "rb") as f:
                inventory, condition, player_location = pickle.load(f)

        ####Random events####
        #Stone rolls in shoe
        if player_location == items[4].location:
            inventory.append("stone")
            print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print ("a small stone rolled in your shoe. it's not unpleasant, but it's there.")
            items[4].location = 0

        #Getting wet
        if player_location == 5:
            condition.append("wet")
    
        #Crossing the river
        if player_location == 6 and move[1] == "east":
            if "swim" in inventory:
                player_location = 6
            else:
                print("you struggle against the stream, but it surrounds you too thightly and takes you with it.")
                print("your body washes on an unknown shore after a day, but no one will find it for years.")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~~~~~~~~~~~~~~")
                print("~~~~~~~~")
                delay = raw_input("press ENTER to move on")
                break

        #Getting dry with fireplace
        if "wet" in condition and items[2].activated == True:
            condition.remove("wet")

        #Rest in bed
        if move[0] == "lay" and move[1] == "in" and move[2] == "bed":
            if "tired" in condition:
                print ("ZZzzzZZZZzzzzZZZZzz")
                print ("you get a bit of a nap and feel rested.")
                print ("ZZzzzZZZZzzzzZZZZzz")
            else:
                print ("..................")
                print ("you lay there for a bit, but are too agitated to fall asleep")
                print ("..................")
            items[3].activated == True
            items[3].description == "the bed is all muffled up"

        #Get twig
        if player_location == 3:
            inventory.append("twig")

        #Learn to swim
        if items[8].activated == True and player_location == 10:
            inventory.append("swim")
            print ("++++++++++++++")
            print ("water seems a lot less of a threat now")
            items[8].activated = False
            if "worm" in inventory:
                inventory.remove("worm")

        #Speak with the man
        if items[13].activated == True and player_location == 6:
            print ("And speaks:")
            time.sleep(2)
            print ("---------------------------------------")
            print ("Thank you. It bothered me for weeks.")
            print ("You can have something off of me.")
            print ("Do you want a peach, a key or a coin?")
            if move[1] == "peach":
                inventory.append("peach")
            if move[1] == "key":
                inventory.append("key")
            if move[1] == "coin":
                inventory.append("coin")
            items[13].activated = False

        #Speak with the old lady
        if items[18].activated == True and player_location == items[18].location:
            print("----------------------")
            print("light shiwer rolls through you")
            print("she smiles a toothless warm")
            print("And speaks:")
            time.sleep(6)
            print("look pass the house.")
            time.sleep(2)
            print("no. not this one")
            items[18].location = 0
            rooms[17].description = "you would call it 'rustic' if you wanted to sell it."
            rooms[4].w = 18




    
        #Remove duplicates in lists and save LAST thing in loop
        inventory = list(set(inventory))
        condition = list(set(condition))

        with open("savefile.dat", "wb") as f:
            pickle.dump([inventory, condition, player_location], f, protocol = 2)

    except IndexError:
        print("XXXxxxxxxxxxxxxXXX")
        print("that means nothing")
        print("XXXxxxxxxxxxxxxXXX")
        continue
