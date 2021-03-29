def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("Sorry, the file " + filename + " does not exist! ")
    else:
        words = contents.split()
        num_words = len(words)
        print(num_words)


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)