responses = {}

polling_active = True

while polling_active:
    name = input("What's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    responses[name] = place

    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False

for name, place in responses.items():
    print(name.title() + " wants to go to " + place + ".")
