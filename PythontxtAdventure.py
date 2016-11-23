# eigen trying to make a text adventure game in python
# you'll have a condition blaahhh

import os
import time
import random
from random import randint

#Character defaults
#Start player in room 0
player_location = 0

def print_header():
    print """
     __       __)                        
(, )  |  /          /)               
   | /| / _  __   _(/  _  __   _  __ 
   |/ |/ (_(_/ (_(_(__(/_/ (__(/_/ (_
   /  |                              
                                     
    """

#Show start screen
print_header()
print """
Welcome to Wanderer.
"""

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
#rooms[] = Room("", "", 0n, 0s, 0e, 0w, 0u, 0d)
rooms[0] = Room("beginning", "you are in a middle of a path. it's hard to tell if it's early morning or late evening. everything seems grey. to your north there are some bushes. to your west there's a small hosue. it seems empty, but in good condition. the door is slightly ajar. to your east there lies a river.", 0, 0, 0, 0, 0, 0)
rooms[1] = Room("river", "the river is wide, but moves slugishly as if the water was packed with something dense.", 0, 0, 1, 0, 0, 0)
rooms[2] = Room("bushes", "the bushes look dense, but comfortable. there seems to be a path crawling between them.", 1, 0, 0, 0, 0, 0)
rooms[3] = Room("house", "there seems to be only one room. it's welll kept. there's a fireplace, a table and a bed in the room.", 0, 0, 0, 1, 0, 0)

class Item:
    #Initialize the item class
    def __init__(self, name, description, location, movable, state):
        self.name = name
        self.description = description
        self.location = location
        self.movable = movable
        self.state = state
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.location, self.movable, self.state)

#Create dictionary of items

items = {}

#item[] = Item("", "", 0, False, "default")
items[1] = Item("matches", "a regular box of matches.", 3, True, "dry")
items[2] = Item("fireplace", "the fireplace seems in good conditon. it's cold, but there are some firewood in it.", 3, False, "cold")
items[3] = Item("bed", "the bed is simple, but made.", 3, False, "made")
items[4] = Item("stone", "a silky smooth and small stone. warm to the touch.", 1, True, "warm")
items[5] = Item("table", "the table is dusty but for a spot in the middle which is shinny clean. there's a box of matches on the table.", 3, False, "default")

#main LOOP

while True:
    #Print header
    

    #Describe location
    print "You are in " + rooms[player_location].introduction + ".\n"
    print rooms[player_location].description
    print

    #Describe the things in the room (Movable items only)
    print "you see the following: "
    for iid in range(1, len(items)+1):
        if items[iid].location == player_location and items[iid].movable == True:
            print items[iid].name

    #Get players command
    command = raw_input("\n> ")

    #Move n,s,e,w,u,d
    if command == "n":
        if rooms[player_location].n != 0:
            player_location = rooms[player_location].n
        else:
            print("you must be confused. there is nothing there.")
    if command == "s":
        if rooms[player_location].s != 0:
            player_location = rooms[player_location].s
        else:
            print("you must be confused. there is nothing there.")
    if command == "e":
        if rooms[player_location].e != 0:
            player_location = rooms[player_location].e
        else:
            print("you must be confused. there is nothing there.")
    if command == "w":
        if rooms[player_location].w != 0:
            player_location = rooms[player_location].w
        else:
            print("you must be confused. there is nothing there.")
    if command == "u":
        if rooms[player_location].u != 0:
            player_location = rooms[player_location].u
        else:
            print("you must be confused. there is nothing there.")
    if command == "d":
        if rooms[player_location].d != 0:
            player_location = rooms[player_location].d
        else:
            print("you must be confused. there is nothing there.")

    #After everything pause before loop repears
    delay = raw_input("\npress ENTER to continue.")