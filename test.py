from selenium import webdriver
import time

driver = webdriver.Chrome() #打开Chrome浏览器
# driver.back() //回到上一个页面
# driver.forward() //切换到下一个页面
driver.get("http://www.baidu.com") #打开网站
print(driver.title)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
# driver.maximize_window() //浏览器窗口最大化
# driver.set_window_size(800, 720) //设置窗口大小为800*720
# driver.get_screenshot_as_file("D:/data/test.png")//截图
# driver.refresh() //重新加载页面
driver.close() #关闭当前页面
# driver.quit() //关闭所有由当前测试脚本打开的页面

