class Employee():
    def __init__(self, first, last, package):
        self.first = first.title()
        self.last = last.title()
        self.package = package

    def give_raise(self, amount=5000):
        self.package += amount
