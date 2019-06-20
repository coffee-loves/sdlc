from selenium import  webdriver
import  time

#login
driver = webdriver.Chrome()
driver.get("https://10.95.14.19")
driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('admin123!@#')
login =driver.find_element_by_css_selector("button")
login.click()
driver.maximize_window()

#滑到页面底部,否则定位不到系统管理菜单
js='var q=document.documentElement.scrollTop=100000'
driver.execute_script(js)
time.sleep(2)
#滑回页面顶部
js='var q=document.documentElement.scrollTop=0'
driver.execute_script(js)
time.sleep(2)

#切换到系统管理
systemadmin = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/a[5]/span")
systemadmin.click()

#不添加该时间，会导致后续定位出现找不到元素
time.sleep(2)

#切换到角色管理,跳转链接
driver.find_element_by_partial_link_text("角色管理").click()
time.sleep(2)

#修改最后一个角色
driver.find_elements_by_css_selector(".icons.iconfont.svg18").pop().click()
driver.find_element_by_css_selector(".btn.md-raised.cf-btn-default.md-button.ng-binding.ng-scope.md-ink-ripple").click()

#退出chrome
time.sleep(2)
driver.quit()

