rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
}
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + '.')
print("")
for river in rivers.keys():
    print(river.title())
print()
for country in rivers.values():
    print(country.title())
