cities = {
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'nearby mountain': 'andes',
    },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountain': 'alaska range',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountain': 'himalaya',
    },
}
for city, city_info in cities.items():
    print(city.title() + " was in " + city_info['country'] + " whose population is " + str(
        city_info['population']) + " and its nearby mountains is " + city_info['nearby mountain'].title() + ".")
