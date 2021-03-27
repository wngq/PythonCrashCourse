from car import Car


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        print("This car can go approximately " + str(range) + " miles on a full charge.")


class ElectricCar(Car):
    def __init__(self, manufacturer, model, year):
        # 初始化父类的属性
        super().__init__(manufacturer, model, year)
        self.battery = Battery()
