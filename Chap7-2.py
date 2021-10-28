current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

#Runs until the list is empty
unconfirmed_users = ['Tyler', 'Uzi', 'Pac']
confirmed_users = []

#This while loop will run till it is empty
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user)
    confirmed_users.append(current_user)

print(confirmed_users)

#Removing all spefic values from a List

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

print(pets)

#Removes all instances of the values dog and cat in the list
#The .remove() function removes the first instance of the value in the List
#If the value being removed is not in the list it returns a ValueError

while ('cat' in pets) or ('dog' in pets):
    if 'cat' in pets:
        pets.remove('cat')
    if 'dog' in pets:
        pets.remove('dog')


print(pets)


Fruits = {}

name = input("What is your favorite devil fruit?\n")
response = input("Why?\n")

Fruits[name] = response

print(Fruits)
