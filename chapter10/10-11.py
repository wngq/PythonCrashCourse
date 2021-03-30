import json

filename = '10-11.json'

number = input("Please enter you favorite number: ")
with open(filename, 'w') as file_obj:
    json.dump(number, file_obj)

with open(filename) as file_obj:
    number = json.load(file_obj)
    print("I know your favorite number! It's " + number + '.')
