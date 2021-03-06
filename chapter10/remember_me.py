import json

filename = 'username.json'

try:
    with open(filename) as file_obj:
        username = json.load(file_obj)
except FileNotFoundError:
    username = input("Please enter your name: ")
    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
