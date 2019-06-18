from selenium import webdriver
import time

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

# def isElementExist(element):
#     flag = True
#     try:
#         driver.find_element_by_class_name(element)
#         return flag
#     except:
#         flag = False
#         return flag

#输入部门名称，点击添加
driver.find_element_by_name('orgName').send_keys('org1')
addaction = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/button[1]")
addaction.click()

#批量删除部门

#修改部门

#查询部门

#增加用户

#增加检测规则模板

#检测规则模板设为默认

#添加检测目标模板

#检测目标模板设为默认

#添加自定义Top模板

#自定义Top模板设为默认

#导出操作日志

#导出异常日志

#批量下载系统日志

#批量禁用基础信息库

#批量禁用基础信息关联

#添加maven

#添加下载文件

#添加标签管理





