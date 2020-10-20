import pytest
import ddt
#from ddt import data,unpack,file_data

@ddt
class demotest(pytest.TestCase):
    def setup(self):
        print("this is the setup")

    @ddt.data(2, 3)  # 2,3各运行一次用例
    def testb(self, value):
        print(value)
        print("this is test b")

    @ddt.data([2, 3], [4, 5])  #
    def testa(self, value):
        print(value)
        print("this is test a")

    @ddt.data([2, 3], [4, 5])
    @ddt.unpack  #
    def testc(self, first, second):
        print(first)
        print(second)
        print("this is test c")

    @ddt.file_data('d:/data_dic.json')
    def test_dic(self, value):
        print(value)
        print('this is dic')

    @ddt.file_data('d:/data.yml')
    def test_yml(self, value):
        print(value)
        print('this is yml')

    def teardown(self):
        print("this is the down")


if __name__ == '__main__':
    pytest.main()
