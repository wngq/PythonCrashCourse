filename = 'pi_million_digits.txt'
with open(filename) as file_object:  # open()返回的对象只在with代码块内可用
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# print(len(pi_string))
birthday = input("Please input your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("yes")
else:
    print("no")
