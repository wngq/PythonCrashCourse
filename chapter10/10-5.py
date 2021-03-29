filename = 'stdout_file_for_10_5.txt'
prompt = "Why do u like programming?(enter 'q' to quit!): "

with open(filename, 'a') as file_object:  # 写入的时候可以只打开一次文件
    while True:
        reason = input(prompt)
        if reason != 'q':
            file_object.write(reason + '\n')
        else:
            print('break')
            break
