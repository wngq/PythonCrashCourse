def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value  # []里面不能用'key'
    return profile


user_profile = build_profile('bin', 'huang', age=30, location='nanjing', field='math')

print(user_profile)
