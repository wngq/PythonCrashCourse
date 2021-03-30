def word_count(filename, word):
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        print("Sorry, the file " + filename + " does not exist! ")
    else:
        line_list = ''
        for line in lines:
            line_list += line
        count = line_list.lower().count(word)
        print("The number of word '" + word + "' in file " + filename + " is " + str(count))


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    word = 'row'
    word_count(filename, word)
