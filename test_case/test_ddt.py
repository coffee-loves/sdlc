import unittest #ddt仅适用于unit test，不适用于pytest
import ddt
from ddt import ddt, data, file_data, unpack  #文件名不能起为与导入包相同的名字

@ddt
class demotest(unittest.TestCase):
    def setup(self):
        print("this is the setup")

    @data(2, 3)  # 2,3各运行一次用例
    def test_b(self, value):
        print(value)  #两次打印结果分别为2，3
        print("this is test b")

    @data([2, 3], [4, 5])  #[2,3]和[4,5]各运行一次用例
    def testa(self, value):
        print(value) #两次打印结果分别为[2,3],[4,5]
        print("this is test a")

    @data([2, 3], [4, 5])
    @unpack  #加入unpack,分别将[2,3]和[4,5]再次拆分为2，3和4，5
    def testc(self, first, second):
        print(first) #两次打印结果分别为2，4
        print(second)#两次打印结果分别为3，5
        print("this is test c")

    # @file_data('d:/data_dic.json')
    # def test_dic(self, value):
    #     print(value)
    #     print('this is dic')
    #
    # @file_data('d:/data.yml')
    # def test_yml(self, value):
    #     print(value)
    #     print('this is yml')

    def teardown(self):
        print("this is the down")


if __name__ == '__main__':
    unittest.main()
