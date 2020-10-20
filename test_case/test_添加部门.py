from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import unittest

class Mytest(unittest.TestCase):
    def setUp(self):
        print("test start")
    def tearDown(self):
        print("test end")

class add_org(Mytest):
    def test_add_org(self):
        driver = webdriver.Chrome()
        driver.get("https://10.95.14.19")
        driver.find_element_by_name('username').send_keys('admin')
        driver.find_element_by_name('password').send_keys('admin123!@#')
        login =driver.find_element_by_css_selector("button")
        #login =driver.fin_element_by_xpath("/html/body/div/div/section[2]/div[3]/div/form/div[3]/button")
        login.click()
        driver.maximize_window()

        #滑到页面底部,否则定位不到系统管理菜单
        js='var q=document.documentElement.scrollTop=100000'
        driver.execute_script(js)
        time.sleep(3)
        #滑回页面顶部
        js='var q=document.documentElement.scrollTop=0'
        driver.execute_script(js)
        time.sleep(3)

        #切换到系统管理
        systemadmin = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/a[5]/span")
        systemadmin.click()

        #定位添加部门按钮，第一次定位失败由于页面有刷新，页面过时
        addorg = driver.find_element_by_css_selector(".btn.md-raised.cf-btn-primary.add-task-btn.md-button.ng-scope.md-ink-ripple")
        time.sleep(2)
        addorg = driver.find_element_by_css_selector(".btn.md-raised.cf-btn-primary.add-task-btn.md-button.ng-scope.md-ink-ripple")
        addorg.click()

        #输入部门名称，点击添加
        driver.find_element_by_name('orgName').send_keys('org1')
        addaction = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/button[1]")
        addaction.click()

        #断言
        time.sleep(2)
        check = driver.find_elements_by_css_selector(".ng-binding.ng-isolate-scope").pop(0)
        print("文本内容为：" + check.text)
        self.assertTrue(check.text=="org1")





















