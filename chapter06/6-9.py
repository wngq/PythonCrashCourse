favorite_places = {
    'hb': ['chengdu', 'shanghai', 'hangzhou'],
    'sc': ['chengdu', 'beijing'],
    'zxy': ['xian', 'xinjiang', 'nanjing']
}

for name, places in favorite_places.items():
    print(name.title() + " likes :")
    for place in places:
        print("\t" + place.title())
