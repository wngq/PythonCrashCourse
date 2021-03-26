favourite_language = {
    'jen': 'python',
    'sarah': 'c#',
    'edward': 'ruby',
    'david': 'c++',
}

developers = ['jen', 'finch', 'David', 'phil']
for developer in developers:
    if developer.lower() in favourite_language.keys():
        print("Thank u, " + developer.title())
    else:
        print(developer.title() + " come")
