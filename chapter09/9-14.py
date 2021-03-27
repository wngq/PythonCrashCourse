from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


die_1 = Die()
for i in range(3):
    print(die_1.roll_die())
print("---")
die_2 = Die(10)
for i in range(0, 4):
    print(die_2.roll_die())
print("---")
die_3 = Die(20)
for i in range(0, 5):
    print(die_3.roll_die())
