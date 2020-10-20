# encoding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select



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

#不添加该时间，会导致后续定位出现找不到元素
time.sleep(2)

#切换到角色管理,跳转链接
solemanage = driver.find_element_by_partial_link_text("角色管理")
solemanage.click()

time.sleep(2)
driver.find_element_by_css_selector(".btn.md-raised.cf-btn-primary.add-task-btn.md-button.ng-scope.md-ink-ripple").click()
driver.find_element_by_css_selector("[name = 'roleName']").send_keys('liantest1')
time.sleep(1)
driver.find_element_by_css_selector("#undefined_1_check").click()
select = Select(driver.find_element_by_tag_name("select"))
#select.deselect_all()
#select.select_by_value("object:1368")
select.select_by_visible_text("部门")

driver.find_element_by_css_selector(".btn.md-raised.add-task-btn.cf-btn-primary.md-button.ng-binding.ng-scope.md-ink-ripple").click()

