import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


# 在Pycharm里面不能用ctrl+shift+r运行测试代码，因为会以unittests模式运行，当前文件名就是不是main了
# ctrl+opt+r，然后再选择要运行的文件
# print(__name__)
unittest.main()
