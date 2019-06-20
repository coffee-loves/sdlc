from selenium import  webdriver
import time

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


#切换到源代码审计
driver.find_element_by_link_text("源代码审计").click()
time.sleep(1)

#添加源码内容
driver.find_element_by_link_text("添加源代码").click()
time.sleep(1)
#输入源码名称
driver.find_element_by_css_selector("input#codeName").send_keys("codetest1")
#选择Java语言
driver.find_element_by_css_selector(".glyphicon.glyphicon-plus").click()
time.sleep(1)
driver.find_element_by_css_selector("a[ng-click='addLanguage(group)']").click()
#选择项目
driver.find_element_by_css_selector(".btn.btn-default.dropdown-toggle").click()
time.sleep(1)
A = driver.find_elements_by_css_selector("input[type = 'radio'][name = 'versionRadio']").pop(2).click()
print(len(A))


#退出
#driver.close()