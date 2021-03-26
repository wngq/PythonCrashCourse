def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    # assert isinstance(full_name, str)
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("enter 'q' at any time to qiut")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break
    full_name = get_formatted_name(f_name, l_name)

    print("\nHello, " + full_name + '!')
