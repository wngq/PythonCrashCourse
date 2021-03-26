current_users = ['david', 'eric', 'john', 'finch', 'shaw', 'zoe', 'Hb']
new_users = ['eric', 'hB', 'sc', 'Zoe', 'zcg']

# 将current_users中的姓名全部转换成小写
current_users_lowers = [current_user.lower() for current_user in current_users]

for username in new_users:
    if username.lower() in current_users_lowers:
        print(username + " has been used!")
    else:
        print("you can use " + username + " as your username.")
