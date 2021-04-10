from pygal_maps_world.i18n import COUNTRIES


# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])

# for c_n in COUNTRIES.values():
#     print(c_n)

def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到指定的国家，就返回None
    return None

# print(get_country_code('Zambia'))
