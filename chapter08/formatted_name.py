def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    # assert isinstance(full_name, str)
    return full_name.title()


print(get_formatted_name('bin', 'huang'))
print(get_formatted_name('john', 'hooker', 'lee'))
