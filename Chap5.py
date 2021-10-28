Zelda = [value for value in range(3,33,3)]

#if statements are similar to how java works

if Zelda[1] == 6:
    print(True)
else:
    print(False)


#Just like java, python uses the != comparison to show not equal to.
palace = "Jabar"

if palace != "Jabar":
    print("Bruh")
else:
    print("NOOOOOO")


#You can use all of the regual math comparison functions like greater than, less than,
#Python uses "and" and "or" unlike java

Uno = 15
Dos = 17

if (Uno > 10) and (Dos < 10):
    print(True)
else:
    print(False)


#Use the keywords 'in' and 'not in' to determine if a value is in a list or not
if (3 in Zelda) and (4 not in Zelda):
    print(True)
else:
    print(False)


#You can run conditional tests outside of if statements by using the == comparison

Eren = "hot"

print(Eren == "hot")


#You can have one line if statements that only run when the if statement is True

if Eren == "hot":
    print(True)

if Eren != "cool":
    print("Eren sucks")


#Python's "eilf" statements are the java equilivent of "if else" statements.

age = 15

if age < 4:
    print("You eat free!!")
elif age >= 14:
    print("That will be $5")
else:
    print("That will be $10")


#Alien colors

alien_color = "yellow"
alien_color2 = "green"
alien_color3 = "red"

if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

if alien_color2 == "green":
    print("You earned 5 points!")
elif alien_color2 == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

if alien_color3 == "green":
    print("You earned 5 points!")
elif alien_color3 == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")


#Stages of Life

age = 13

if age >= 65:
    print("The person is an elder")
elif age < 65 and age >= 20:
    print("This person is an adult")
elif age < 20 and age >= 13:
    print("This person is a teenager")
elif age < 13 and age >= 4:
    print("This person is a kid")
elif age < 4 and age >= 2:
    print("This person is a toddler")
else:
    print('This person is a baby')

print()

#Favorite fruits

fav_fruits = ["pineapple", "peach", "strawberry"]

if "pineapple" in fav_fruits:
    print("You really like pineapple!")
if "apple" in fav_fruits:
    print("You really like apple")
if "blueberry" in fav_fruits:
    print("You really like blueberry!")
if "peach" in fav_fruits:
    print("You really like peach!")
if "tomato" in fav_fruits:
    print("You really like tomato!")

print()
#Requested toppings

requested_toppings = ['mushrooms', 'green peppers', 'hot sauce']

# Checks if the list is empty
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished your pizza!")
else:
    print("Are you sure you want a plain pizza?")


#Hello Admin

currentUsers = ["Dr. TC", "Wolf", "Salem", "Samuel", "Clancy"]

newUsers = ["Salem", "Samuel", "Savage 21", "Flower Boy"]

if currentUsers:
    for user in currentUsers:
        if user == "Wolf":
            print("Hello, admin would you like to see your progress report")
        else:
            print("Hello " + user + ", thank you for logging in again")
else:
    print("We need to find some more users!")

#Checks if the username is taken
for user in newUsers:
    if user in currentUsers:
        print("Sorry, that username is taken.")
    else:
        print("The username is available.")
