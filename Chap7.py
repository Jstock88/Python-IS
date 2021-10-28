#inputs

#Amusment park

height = input("How tall are you? " )
height = int(height)
if height >= 160:
    print("You are tall enough to ride this ride.")
else:
    print("Get out of here halfling.")


number = input("Enter to see if your number is even or odd. ")
number = int(number)

if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#Using a flag

flag = True
while flag == True:
    message = input("I will repeat what you say. Input quit to stop. ")

    if message == 'quit':
        flag = False
    else:
        print(message)

#Using a break to end a loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)\n"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
