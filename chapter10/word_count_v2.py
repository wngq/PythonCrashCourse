def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # print("Sorry, the file " + filename + " does not exist! ")
        with open('missing_file.txt', 'a') as missing_file_object:
            # 'w'会在打开文件前先清空文件
            missing_file_object.write(filename + '\n')
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filenames = ['alice.txt', 'siddharth.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(filename)
