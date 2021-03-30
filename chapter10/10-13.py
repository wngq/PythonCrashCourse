import json

filename = 'username_10-13.json'


def get_stored_username():
    try:
        with open(filename) as file_obj:
            username = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("Please enter your new name: ")
    with open(filename, 'w') as file_obj:
        json.dump(username, file_obj)
    return username


def greet_user():
    username = input("Please enter your name: ")
    if username == get_stored_username():
        print("Welcome back, " + username + "!")
    else:
        print("You are not in the system, please register you new name.")
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
