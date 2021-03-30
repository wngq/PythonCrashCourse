def word_count(filename, word):
    try:
        with open(filename) as file_object:
            contents = file_object.read()  # read()返回的是bytes
    except FileNotFoundError:
        print("Sorry, the file " + filename + " does not exist! ")
    else:
        count = contents.lower().count(word)
        print("The number of word '" + word + "' in the file " + filename + " is " + str(count))


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    word = 'row'
    word_count(filename, word)
