# encoding=utf-8
from selenium import  webdriver
import time
from selenium.webdriver.common.keys import Keys
import  os
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
time.sleep(2)
A = driver.find_elements_by_css_selector("input[type = 'radio'][name = 'versionRadio']").pop(1)
A.send_keys(Keys.SPACE)
#选择版本
driver.find_elements_by_css_selector("button#single-button").pop().click()
selectVersion = driver.find_elements_by_css_selector("input[type = 'radio'][name = 'versionRadio']").pop()
selectVersion.send_keys(Keys.SPACE)
#上传文件
#driver.find_element_by_css_selector("#codeUpload").send_keys("C:/Users/Administrator/Desktop/自动化/企业版/uploadDoc/白名单.zip")
driver.find_element_by_css_selector("#codeUpload").click()
os.system("C:/Users/Administrator/Desktop/自动化/企业版/uploadDoc/uploadsript.exe")
time.sleep(2)
#点击下一步
driver.find_element_by_css_selector(".btn.md-raised.cf-btn-primary.add-task-btn.md-button.ng-scope.md-ink-ripple").click()
time.sleep(2)
#点击添加
driver.find_element_by_css_selector(".btn.md-raised.cf-btn-primary.add-task-btn.md-button.ng-binding.md-ink-ripple").click()
#退出
#driver.close()