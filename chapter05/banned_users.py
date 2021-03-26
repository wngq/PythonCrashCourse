banned_users=['andrew','carolina','david']
user_1 = 'marie'
user_2 = 'david'

if user_1 not in banned_users:
    print(user_1.title()+", you can post a response if you wish")

if user_2 in banned_users:
    print(user_2.title()+", you cannot...")