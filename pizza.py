# pizzaQuiz2

# tell the user what's going on 
print ("What Type of Pizza Are You?")
print (" ") 
print ("Take our quiz to find out what type of pizza you are!")
print (" ")

# player information on the player 
player = {
	"name": "unknown",
	"superpower": "unknown",
	"faveColor" : "unknown", 
	"drink" : "unknown"
}

# 
name = raw_input("What is your name? ")
player ["name"] = name


# the chosen superpower will be the players superpower



# pepperoniType = super strength/invisitibility and red/yellow
# cheeseType = super strength/invisibility and blue/orange
# anchovyType = flying/telekinesis and water/tea
# marinaraType = flying/telekinesis and wine/coffee

print (" ") # spacing
superpower = raw_input("Hi, " + player["name"] + "! Choose one superpower: super strength, invisibility, flying, telekinesis: ")
player ["superpower"] = superpower 

# if the player chooses super strength or invisibility we will give them a color prompt. Red/yellow is Pepperoni. Blue/orange is Cheese.
if (player["superpower"] == "super strength") or (player["superpower"] == "invisibility"): 
	print (" ")
	faveColor = raw_input("Woaaaaah, interesting choice. Now that you have " + superpower + "," 
		"which of the following colors speaks to you the most: red, blue, yellow, orange: ")
	player ["faveColor"] = faveColor
	
	if (player["faveColor"] == "red") or (player["faveColor"] == "yellow"):
		print(" ")
		print("Everyone loves you, except ve getarians. " + name + ", you are a Pepperoni Pizza!")
	elif (player["faveColor"] == "blue") or (player["faveColor"] == "orange"):
		print(" ")
		print("Some might say you're a little vanilla, but tell those haters, you are timeless - you're a Cheese Pizza!")

# if the player chooses flying or telekinesis we will give them a drink prompt 
else:
	drink = raw_input("Cool! Now that you have " + superpower + "choose one type of drink: water, wine, coffee, tea. ")
	player ["drink"] = drink

	# water or tea is anchovy. wine or coffee is marinara. 
	if (drink == "water") or (drink == "tea"):
		print(" ")
		print("Not many understand you, but when they do, they LOVE you. You are an Anchovy Pizza!!")
	else: 
		print(" ")
		print(name + ", no need to be cheesy here. You are who you are, you're a Marinara Pizza!!")

 



# if (player["superpower"] == pepperoniType[0]) and (player["faveColor"] == pepperoniType[1]):
	# print "You are Pepperoni Pizza"





	
