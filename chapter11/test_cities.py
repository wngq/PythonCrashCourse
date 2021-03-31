import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_city_country = city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_ccp = city_country('santiago', 'chile', '5000000')
        self.assertEqual(formatted_ccp, 'Santiago, Chile - population 5000000')


# 在Pycharm里面不能用ctrl+shift+r运行测试代码，因为会以unittests模式运行，当前文件名就不是main了
# ctrl+opt+r，然后再选择要运行的文件
# print(__name__)
unittest.main()
