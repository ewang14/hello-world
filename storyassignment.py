# Story Assignment
# Create your own story algorithm. You can modify an example from class (story maker) or create your own. 
# Remember to comment your code and use examples of: - user inputs - variables (int or float, string, boolean) - concatenation

# title and instructions to create a story
print (" ") # add extra line of spacing
print ("Tell us about your last vacation!")
print ("----------------------------------------------------------")
print (" ") # add extra line of spacing 

# story variable dependent on user's input
location = raw_input("Where did you go on your last vacation? ")
time = raw_input("How long were you there for? ")
activity1 = raw_input("What is one cool thing you did there? ")
activity2 = raw_input("What is another activity you did there? ")
faveMemory = raw_input("What was your favorite memory there? ")
food1 = raw_input("What was the most adventurous dish you ate there? ")
activity3 = raw_input("What is one thing you weren't able to do, but want to next time? ")


# this story is made up of strings and user variables. 
myVacation = "I recently went to " + location + " for " + time + ". While I were there, I " + activity1 + "and " \
+ activity2 + ". My favorite memory is when I" + faveMemory + " It was so much fun! I even ate " + food1 + \
"!! Next time I go back I are definitely going to " + activity3 + "."  

#now the full story is shown back to the user
print (" ")
print (myVacation)
