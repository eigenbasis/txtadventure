# eigen trying to make a text adventure game in python
# you'll have a condition

import os
import time
import random
from random import randint


#global variables
condition = ["unknown"]
inventory = ["bag"]
print("This is an introduction about where you are")

def getcmd(cmdlist):
	cmd = input("> ")
	if cmd in cmdlist:
		return cmd
	else:
		print("Nothing happens")
		return getcmd(cmdlist)

def start(inventory):
	print("These are your choices")
	print("1: bushes")
	print("2: river")
	print("3: home")
	#list the choices

	cmdlist = [1, 2, 3,]
	cmd = getcmd(cmdlist)

	if cmd == 1:
		bushes(inventory)
	elif cmd == 2:
		river(inventory, condition)
	elif cmd == 3:
		print("You walk in a house. It seems cosy")
		house(inventory, condition)
	
def bushes(inventory):
	print ("There are a lot of branches, but you see a small path.")
	print ("1: take the path")
	print ("2: turn back")

	cmdlist = [1, 2,]
	cmd = getcmd(cmdlist)

	if cmd == 1:
		print ("You follow the path")
	elif cmd == 2:
		start(inventory)

def river(inventory, condition):
	print ("You step into the river")
	print("A smooth rock falls in your shoe")
	time.sleep(1)
	print("It's not unpleasant, but it's there")
	inventory.append("smooth stone")
	time.sleep(1)
	print("The current seems quite strong")
	print("1: turn back")
	print("2: cross the river")
	cmdlist = [1, 2,]
	cmd = getcmd(cmdlist)
	if cmd == 1:
		print("You turn back and leave the current behidn you")
		start(inventory)
	elif cmd == 2:
		print("You've stepped into the river and your feet has gotten wet")
		condition.append("wet")
		print(condition)
		print("1: get back")
		print("2: continue one")
		cmdlist = ["1", "2",]
		cmd = getcmd(cmdlist)
		if cmd == 1:
			start(inventory)
		elif cmd == 2:
			print("You try to get across, but the current swoops you away")
			print("Your body will wash out 5 days later")
			print("But no one will find it for months")

	

def house(inventory, condition):
	print ("There's a heart, a bed and a table")
	print ("1: check the heart")
	print ("2: lay in bed")
	print ("3: search the table")
	print ("4: get out")
	cmdlist = [1, 2, 3, 4,]
	cmd = getcmd(cmdlist)
	if cmd == 1:
		print ("The heart is cold, but there's some firewood in it")
		print ("1: try to start a fire")
		print ("2: turn back")
		cmdlist = [1, 2,]
		cmd = getcmd(cmdlist)
		if cmd == 1:
			if "matches" in inventory:
				print ("You manage to light a fire")
				time.sleep(2)
				print ("The room fills with warmth and you feel a little better")
				condition.append("dry")
				house(inventory, condition)
			else:
				print ("You don't have anything to start the fire with")
				house(inventory, condition)
	if cmd == 2:
		if "tired" in condition:
			condition.append("rested")
			condition.remove("tired")
			print ("you are now rested")
		else:
			print ("you lay there pondering aimlessly and get up after a while")
			house(inventory, condition)
	if cmd == 3:
		inventory.append("matches")
		print ("you found a box of matches and stash it in your pocket")
		house(inventory, condition)
	if cmd == 4:
		start(inventory)

start(inventory)