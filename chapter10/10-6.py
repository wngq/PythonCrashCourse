try:
    input_1 = input("Please enter the 1st number: ")
    int_1 = int(input_1)
    input_2 = input("Please enter the 2nd number: ")
    int_2 = int(input_2)
except:
    print("Please enter a number!!!")
else:
    print(int_1 + int_2)
