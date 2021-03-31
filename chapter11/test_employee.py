import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self) -> None:
        self.employee_1 = Employee('bin', 'huang', 10000)

    def test_give_default_raise(self):
        self.employee_1.give_raise()
        self.assertEqual(15000, self.employee_1.package)

    def test_give_custom_raise(self):
        self.employee_1.give_raise(10000)
        self.assertEqual(20000, self.employee_1.package)


unittest.main()
