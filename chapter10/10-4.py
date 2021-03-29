filename = "guest_book.txt"
prompt = "Please enter you name(enter 'q' to quit!): "
write_avtive = True
with open(filename, 'a') as file_object:  # 写入的时候可以只打开一次文件
    while write_avtive:
        name = input(prompt)
        if name != 'q':
            file_object.write(name + '\n')
            print("Hello " + name.title())
        else:
            print("break")
            write_avtive = False
