# eigen trying to make a text adventure game in python
# you'll have a condition blaahhh

import os
import time
import random
from random import randint

#Character defaults
inventory = []

#Start player in room 1
player_location = 1

def print_header():
    print """
     __       __)                        
(, )  |  /          /)               
   | /| / _  __   _(/  _  __   _  __ 
   |/ |/ (_(_/ (_(_(__(/_/ (__(/_/ (_
   /  |                              
                                     
    """
def help():
    print """
Welcome to Wanderer. 
Type GO and direction to move. 
Type TAKE and items name to pick things up.
Type CHECK and items name to get more information about the item.
To use items type USE item's name ON item's name
Type INVENTORY at any point to see your inventory.
Type HELP at any point to see this again.
"""
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
rooms[1] = Room("beginning", "you are in a middle of a path. it's hard to tell if it's early morning or late evening. everything seems grey. to your north there are some bushes. to your west there's a small hosue. it seems empty, but in good condition. the door is slightly ajar. to your east there lays a river.", 3, 0, 2, 4, 0, 0)
rooms[2] = Room("river", "the river is wide, but moves slugishly as if the water was packed with something dense.", 0, 0, 0, 1, 0, 0)
rooms[3] = Room("bushes", "the bushes look dense, but comfortable. there seems to be a path crawling between them.", 0, 1, 0, 0, 0, 0)
rooms[4] = Room("house", "there seems to be only one room. it's well kept. there's a fireplace, a table and a bed in the room.", 0, 0, 1, 0, 0, 0)

class Item:
    #Initialize the item class
    def __init__(self, name, description, location, movable, state, need_item, interaction):
        self.name = name
        self.description = description
        self.location = location
        self.movable = movable
        self.state = state
        self.need_item = need_item
        self.interaction = interaction
    
#Create dictionary of items

items = {}

#items[] = Item(name, description, location, movable, state, need_item, interaction)
items[1] = Item("matches", "a regular box of matches.", 4, True, "dry", "none", "default")
items[2] = Item("fireplace", "the fireplace seems in good conditon. it's cold, but there are some firewood in it.", 4, False, "cold", "matches", "you manage to light the fire, the room fills with warmth")
items[3] = Item("bed", "the bed is simple, but made.", 4, False, "made", "none", "you lay in bed for a while and feel rested")
items[4] = Item("stone", "a silky smooth and small stone. warm to the touch.", 2, True, "it's warm to the touch", "none", "default")
items[5] = Item("table", "the table is dusty but for a spot in the middle which is shinny clean. there's a box of matches on the table.", 4, False, "it's just a table", "none", "there is a box of matches on the table")

#main LOOP

while True:
    #Print header
    

    #Describe location
    print "You are in " + rooms[player_location].introduction + ".\n"
    print rooms[player_location].description
    print

    #Describe the things in the room (Movable items only)
    #print "you see the following: "
    #for iid in range(1, len(items)+1):
        #if items[iid].location == player_location and items[iid].movable == True:
            #print items[iid].name

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

    #Checking immovable items
    if move[0] == "check":
        for iid in range(1, len(items)+1):
            if move[1] == items[iid].name and items[iid].location == player_location and items[iid].movable == False:
                print items[iid].description

    #Use item
    if move[0] == "use" and move[2] == "on":
        for iid in inventory:
            for iiid in range(1, len(items)+1):
                if move[1] == iid and (move[3] == items[iiid].name and player_location == items[iiid].location and move[1] == items[iiid].need_item):
                    print items[iiid].interaction

    #Get help
    if move[0] == "help":
        print help()

    #Check inventory
    if move[0] == "inventory":
        print inventory
