#This simple dictionary stores an alien's color and points

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print("You just earned " + str(alien_0['points']) + " points!")
print(alien_0)
print()

#adds two more key-value pairs to the alien_0 dictionary

alien_0['xCord'] = 0
alien_0['yCord'] = 25
print(alien_0)

#how to change a value in a dictionary

alien_0['yCord'] = 10
print(alien_0)

print()

favoriteLanguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Jen's favorite language is " + favoriteLanguages['jen'].title() + ".")

#person

Ben = {'firstName': 'Ben',
        'lastName': 'Himmel',
        'personality': 'nerd',
        'favRapper': 'Juice Wrld'
}

print("Ben's favorite rapper is " + Ben['favRapper'] + " and he's overrated")

#When you want to loop through the values of the dictionary you use .items()
#THe dictionary's defaultly loops through the keys but you can also use .keys()

for k, v in Ben.items():
    print("\nKey - " + k)
    print("Value - " + v)
    print()

bigList = [Ben, alien_0, favoriteLanguages]

print(bigList)

S
