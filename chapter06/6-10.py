favourite_number = {
    'zrq': [11, 12, 13, 5],
    'hb': [44, 23, 67],
    'zcg': [22, 44, 67, 9, 2],
    'zzy': [1, 0, 3],
    'lyx': [7, 5],
}

for name, numbers in favourite_number.items():
    print(name.title() + "'s favourite number are: ")
    for number in numbers:
        print("\t" + str(number))
