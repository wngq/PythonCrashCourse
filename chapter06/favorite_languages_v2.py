favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c#', 'c', 'c++'],
    'edward': ['ruby', 'go'],
    'Finch': ['perl'],
    'david': ['c++', 'java'],
    'phil': ['python', 'haskell'],
}

for developer, languages in favourite_languages.items():
    if len(languages) == 1:
        print(developer.title() + "'s favourite language is: " + languages[0].title() + ".")
    else:
        print(developer.title() + "'s favourite languages are:")
        for language in languages:
            print("\t" + language.title())
