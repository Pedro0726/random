from random import randint, shuffle, choice
# random
 # Python comes with a built in random library. There are a lot of functions included in this random library, so we will only 
 #show you two useful functions for now.
# print("random")
# dice1 = randint(1,7)
# print(f"dice1: {dice1}")
# dice2 = randint(1,7)
# print(f"dice2: {dice2}")
# rolledDoubles = dice1 == dice2
# if rolledDoubles:
#   print("You rolled doubles")
# else: print("Not doubles")


# if dice1 == 1 and dice2 == 1:
#   print("you rolled snake eyes")
# else: print("you did not roll snake eyes")

myList = range(1,51)
print("My new list")
print(list(myList))
myList = list(myList)
shuffle(myList)
print(myList)

var = randint(1,200)
print("new list")
print(var)
if var %2 == 0:
  print("number is even")
else: print("number is odd")

color = ["red", "blue", "pink", "purple"]
random_color = choice(color)
print(f"random color is {random_color}")
