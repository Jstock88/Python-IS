#This is a program that has a website's current usernames and a list of new
#users that are making an account

currentUsers = ["Drake", "Wolf", "John", "Tyler", "Clancy", "Wyatt", "Ben"]

newUsers = ["Clancy", "Tyler", "Max", "Issac"]

#One of the usernames is the admin of the website and the loop checks if the
#current user is the admin

#This first if statement checks if there are no Usernames in the List

if currentUsers:
    for user in currentUsers:
        if user == "Wolf":
            print("Hello, admin would you like to see your progress report")
        else:
            print("Hello " + user + ", thank you for logging in again")
else:
    print("We need to find some more users!")


print()
#Checks if the new usernames are taken

for user in newUsers:
    if user in currentUsers:
        print("Sorry, that username is taken.")
    else:
        print("The username is available.")
