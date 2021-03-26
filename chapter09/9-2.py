class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " is a restaurant, which serves " + self.cuisine_type)

    def open_restaurant(self):
        print("The " + self.restaurant_name + " is open! ")


restaurant_1 = Restaurant('taizi', 'yuecai')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('liangliangzhenxia', 'youmendaxia')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('cailinji', 'reganmian')
restaurant_3.describe_restaurant()
