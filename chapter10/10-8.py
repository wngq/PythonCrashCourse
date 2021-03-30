# cats_filename = 'cats.txt'
# dogs_filename = 'dogs.txt'
#
# try:
#     with open(cats_filename) as cats_file_object:
#         cats_contents = cats_file_object.read()
#     with open(dogs_filename) as dogs_file_object:
#         dogs_contents = dogs_file_object.read()
# except FileNotFoundError:
#     print("Sorry, there is a file that does not exist! ")
# else:
#     print(cats_contents)
#     print("---")
#     print(dogs_contents)

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("Sorry, the file " + filename + " does not exist! ")
    else:
        print("The file " + filename + "'s contents are:")
        print(contents)
