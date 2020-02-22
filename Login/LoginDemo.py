""" Login username and Password stored in a Dictionary Data Structure
we will look at adding features to allow:
* new users
* three attempts already in demo
* password restrictions
    - number of Characters
    - Capital Characters
    - require Number
    - require special character
other suggestions may follow
"""
# dictionary Credentials key for Usernames and values for passwords
credentials = {"mmathews":"mypassword", "admin":"password"}
# store username input by user
username = input("What is your username ? ")

if username in credentials.keys():
    count = 0
    while count < 3:
        password = input("What is your Passsword ? ")
        if password ==credentials[username]:
            print("You are in")
            count = 3
        else:
            count = count +1
            print("Attempt ", count)
            print("NO ACCESS wrong password ")
else:
    print("Username NOT VALID")
