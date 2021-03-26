def city_country(cityname, country):
    """

    :type country: str
    :type cityname: str
    """
    return cityname.title() + ', ' + country.title()


print(city_country('shanghai', 'china'))
print(city_country('new york', 'America'))
print(city_country('london', 'england'))
