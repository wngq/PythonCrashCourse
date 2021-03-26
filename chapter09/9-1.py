class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " is a restaurant, which serve " + self.cuisine_type)

    def open_restaurant(self):
        print("The " + self.restaurant_name + " is open! ")


restaurant_1 = Restaurant('taizi', 'yuecai')

print(restaurant_1.restaurant_name)
print(restaurant_1.cuisine_type)
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
