filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # print("Sorry, the file " + filename + " does not exist! ")
        pass
    else:
        print("The file " + filename + "'s contents are:")
        print(contents)
