filename = 'pi_digits.txt'
with open(filename) as file_object:  # open()返回的对象只在with代码块内可用
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
