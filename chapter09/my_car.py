from car import Car
from electric_car import ElectricCar

my_new_car = Car('toyota', 'lexus', '2017')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print("---Electric Car")
my_tesla = ElectricCar('tesla', 'model 3', 2017)
print(my_tesla.get_descriptive_name())
