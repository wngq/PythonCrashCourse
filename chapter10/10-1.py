filename = 'learning_python.txt'
# 第一次打印读取整个文件
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

print("---")
# 第二次打印遍历文件对象
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("---")
# 第三次打印将各行存储在一个列表中，再在with外打印
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
