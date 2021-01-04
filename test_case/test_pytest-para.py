import pytest

class TestCase:

    @pytest.mark.parametrize('password',[2,4])  # 2,4各运行一次用例,注意变量名password要加引号
    def test_b(self, password):
        print(password)

if __name__ == '__main__':
    pytest.main()
