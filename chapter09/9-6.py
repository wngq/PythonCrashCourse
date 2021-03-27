class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + " is a restaurant, which serves " + self.cuisine_type)

    def open_restaurant(self):
        print("The " + self.restaurant_name + " is open! ")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, max_served_number):
        self.number_served += max_served_number


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_name='ice cream'):
        super().__init__(restaurant_name, cuisine_name)
        self.flavors = []

    def show_flavors(self):
        print("\nShowing flavors: ")
        for flavor in self.flavors:
            print(flavor)


ice_cream_stand = IceCreamStand('DQ')
ice_cream_stand.describe_restaurant()
ice_cream_stand.flavors = ['orange', 'apple', 'cheese']
ice_cream_stand.show_flavors()
