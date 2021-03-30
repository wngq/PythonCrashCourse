while True:
    try:
        input_1 = input("Please enter the 1st number(enter 'q' to quit): ")
        if input_1 == 'q':
            print("break")
            break
        int_1 = int(input_1)
        input_2 = input("Please enter the 2nd number(enter 'q' to quit): ")
        if input_2 == 'q':
            print("break")
            break
        int_2 = int(input_2)
    except:
        print("Please enter a number!!!")
    else:
        print(int_1 + int_2)
