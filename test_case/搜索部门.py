from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


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


#查询部门，定位输入框，查询按钮
a = driver.find_element_by_css_selector("input[placeholder='输入关键字'][type='text']").send_keys("org1")

searchButton = driver.find_element_by_css_selector(".btn.btn-default")
print(searchButton)
driver.execute_script("arguments[0].click();", searchButton)