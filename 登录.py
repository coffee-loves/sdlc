from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://10.95.14.19")
driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('admin123!@#')
login =driver.find_element_by_css_selector("button")
login.click()

