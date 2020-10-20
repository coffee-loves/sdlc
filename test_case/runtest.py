# encoding=utf-8
import  unittest,time
from unittest import defaultTestLoader, TestSuite
from test_case.审计 import  auditBugs
from HTMLTestRunner import  HTMLTestRunner


def get_allcase():
    test_dir = 'C:/Users/Administrator/Desktop/自动化/企业版/test_case/'
    discover: TestSuite = unittest.defaultTestLoader.discover(test_dir, pattern='test_添加部门.py')
    return  discover

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(auditBugs("test_auditYes"))
    # test_dir = 'C:/Users/Administrator/Desktop/自动化/企业版/test_case'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_添加部门.py')
    # runner = unittest.TextTestRunner()
    # runner.run(discover)

    now = time.strftime("%Y-%m-%d %H-%M-%S")
    test_report = 'C:/Users/Administrator/Desktop/自动化/企业版/test_report'
    filename = test_report + '/' + now + 'result.html'

    #定义报告存放路径
    fp = open(filename,'wb')
    #定义测试报告
    runner = HTMLTestRunner(stream=fp,title='审计缺陷报告',description= '用例执行情况：')
    # 运行测试用例
#    runner = unittest.TextTestRunner()
    runner.run(get_allcase())
    # 关闭报告文件
    fp.close()


