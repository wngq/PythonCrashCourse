favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c#', 'c', 'c++'],
    'edward': ['ruby', 'go'],
    'david': ['c++', 'java'],
    'phil': ['python', 'haskell'],
}
# for developer in favourite_languages.keys():
#     print(developer.title() + "'s favourite languages are:")
#     for language in favourite_languages[developer]:
#         print("\t" + language.title())

for developer, languages in favourite_languages.items():
    print(developer.title() + "'s favourite languages are:")
    for language in languages:
        print("\t" + language.title())
