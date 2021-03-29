filename = 'pi_digits.txt'
with open(filename) as file_object:  # open()返回的对象只在with代码块内可用
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
