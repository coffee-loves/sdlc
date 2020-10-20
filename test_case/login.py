from selenium import webdriver
from test_case import image_str



driver = webdriver.Chrome()
driver.get("https://10.95.14.19:8081")
driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/main/div[2]/div/div[2]/div/form/div[1]/div/div/div[1]/input").send_keys('lianlu')
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/main/div[2]/div/div[2]/div/form/div[2]/div/div/div/div[1]/input').send_keys('123abc~@#')


# login = driver.find_element_by_css_selector("button")
# login.click()
# driver.maximize_window()

        # # 滑到页面底部,否则定位不到系统管理菜单
        # js = 'var q=document.documentElement.scrollTop=100000'
        # driver.execute_script(js)
        # time.sleep(3)
        #
        # # 滑回页面顶部
        # js = 'var q=document.documentElement.scrollTop=0'
        # driver.execute_script(js)
        # time.sleep(3)


