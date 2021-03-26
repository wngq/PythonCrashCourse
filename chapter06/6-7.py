person_1 = {
    'first_name': 'bin',
    'last_name': 'huang',
    'age': 29,
    'city': 'nanjing',
}
person_2 = {
    'first_name': 'ziyu',
    'last_name': 'zhang',
    'age': 28,
    'city': 'shenzhen',
}
person_3 = {
    'first_name': 'chao',
    'last_name': 'sun',
    'age': 27,
    'city': 'shandong',
}

people = [person_1, person_2, person_3]
for pp in people:
    # print(pp)
    fullname = pp['last_name'] + " " + pp['first_name']
    age = str(pp['age'])
    city = pp['city']
    print(fullname.title() + ", who is " + age + " years old, " + "is living in " + city.title() + ".")
