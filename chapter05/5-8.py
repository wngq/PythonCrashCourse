user_list = ['admin', 'eric', 'john', 'finch', 'root', 'zoe']

for user in user_list:
    if user == 'admin':
        print("Hello " + user + ", would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again.")
