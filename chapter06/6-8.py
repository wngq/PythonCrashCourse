pet_1 = {
    'type': 'fish',
    'name': 'john',
    'owner': 'guido',
}

pet_2 = {
    'type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
}

pet_3 = {
    'type': 'dog',
    'name': 'peso',
    'owner': 'eric',
}

pet_4 = {
    'type': 'Adog',
    'name': 'huangbin',
    'owner': 'wq',
}

pets = [pet_1, pet_2, pet_3, pet_4]

vowel = ['a', 'e', 'i', 'o', 'u']

for pet in pets:
    if pet['type'][0].lower() not in vowel:  # 宠物名首字母不是元音
        print(pet['name'].title() + ", owned by " + pet['owner'].title() + ", is a " + pet['type'] + ".")
    else:  # 宠物名首字母是元音
        print(pet['name'].title() + ", owned by " + pet['owner'].title() + ", is an " + pet['type'] + ".")
