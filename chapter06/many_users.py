users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, userinfo in users.items():
    print("Username: " + username)
    print("\tFull name: " + userinfo['first'].title() + " " + userinfo['last'].title())
    print("\tLocation: " + userinfo['location'].title())
