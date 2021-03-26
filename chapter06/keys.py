favourite_language = {
    'jen': 'python',
    'sarah': 'c#',
    'edward': 'ruby',
    'david': 'c++',
}

friends = ['david', 'sarah']

for name in favourite_language.keys():
    print(name.title())
    if name in friends:
        print("\tHi " + name.title() +
              ", I know your favourite language is " +
              favourite_language[name].title() +
              ".")
favourite_language = {
    'jen': 'python',
    'sarah': 'c#',
    'edward': 'ruby',
    'david': 'c++',
}