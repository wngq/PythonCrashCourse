def make_car(manufacturer, car_type, **car_info):
    car = {}
    car['manufacturer'] = manufacturer.title()
    car['car_type'] = car_type.title()
    for key, value in car_info.items():
        car[key] = value
    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
