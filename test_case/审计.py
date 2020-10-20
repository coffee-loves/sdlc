# encoding=utf-8
from selenium import  webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from test_case.login import Login
import time
import unittest


class Mytest(unittest.TestCase):
    def setUp(self):
        print("test start")
    def tearDown(self):
        self.driver.quit()

class auditBugs(Mytest):
    #必需以test开头，discover才能加载
    def test_auditYes(self):
        driver = webdriver.Chrome()
        driver.get("https://10.95.14.19")
        # 调用登录模块
        Login().user_login(driver)

        # 切换到源代码审计
        driver.find_element_by_link_text("源代码审计").click()
        time.sleep(2)

        # 点击某任务查看按钮
        driver.find_elements_by_css_selector("[title = '查看']").pop(6).click()

        # 点击缺陷总数
        def retryingFindClick(text):
            result = False
            attempts = 0
            while attempts < 5:
                try:
                    driver.find_element_by_link_text(text).click()
                    result = True
                    break
                except:
                    StaleElementReferenceException
                    pass
                attempts = attempts + 1
            return result

        retryingFindClick("4")

        time.sleep(2)
        # 审计操作
        driver.find_element_by_css_selector("[id = 'a_bugs_1_switch']").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#a_bugs_2_switch").click()
        time.sleep(1)
        # 右键
        right_click = driver.find_element_by_css_selector(("#a_bugs_18_span"))
        ActionChains(driver).context_click(right_click).perform()
        # 选择审计项
        time.sleep(2)
        driver.find_elements_by_css_selector("[type = 'radio']").pop().click()
        driver.find_element_by_css_selector(
            ".form-control.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required.ng-valid-maxlength").send_keys(
            "审计为中等级")
        driver.find_element_by_css_selector(".btn.btn-primary").click()



































