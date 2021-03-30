import json

filename = '10-12.json'


def get_stored_favorite_number():
    try:
        with open(filename) as file_obj:
            number = json.load(file_obj)
    except FileNotFoundError:
        return None
    else:
        return number


def get_new_favorite_number():
    number = input("Please enter your favorite number: ")
    with open(filename, 'w') as file_obj:
        json.dump(number, file_obj)
    return number


def favorite_number():
    number = get_stored_favorite_number()
    if number:
        print("I know your favorite number! It's " + number + '.')
    else:
        number = get_new_favorite_number()
        print("I know your favorite number! It's " + number + '.')


favorite_number()
