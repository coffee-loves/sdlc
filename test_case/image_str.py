from selenium import webdriver
import time
from selenium import webdriver
import re
from PIL import Image
import  pytesseract


# driver = webdriver.Chrome() #打开Chrome浏览器
# # driver.back() //回到上一个页面
# # driver.forward() //切换到下一个页面
# driver.get("http://www.baidu.com") #打开网站
# print(driver.title)
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()
# time.sleep(3)
# # driver.maximize_window() //浏览器窗口最大化
# # driver.set_window_size(800, 720) //设置窗口大小为800*720
# # driver.get_screenshot_as_file("D:/data/test.png")//截图
# # driver.refresh() //重新加载页面
# driver.close() #关闭当前页面
# # driver.quit() //关闭所有由当前测试脚本打开的页面


class VerificationCode:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.find_element = self.driver.find_element_by_css_selector

    def get_pictures(self):
        self.driver.get('https://10.95.14.19:8081')  # 打开登陆页面
        self.driver.save_screenshot('pictures.png')  # 全屏截图
        page_snap_obj = Image.open('pictures.png')
        img = self.driver.find_element_by_css_selector(".el-tooltip")# 验证码元素位置

        time.sleep(1)
        location = img.location
        size = img.size  # 获取验证码的大小参数
        left = location['x']
        top = location['y']
        right = left + size['width']
        bottom = top + size['height']
        image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
        image_obj.show()  # 打开切割后的完整验证码
        #self.driver.close()  # 处理完验证码后关闭浏览器
        return image_obj

    def processing_image(self):
        image_obj = self.get_pictures()  # 获取验证码
        img = image_obj.convert("L")  # 转灰度
        pixdata = img.load()
        w, h = img.size
        threshold = 160
        # 遍历所有像素，大于阈值的为黑色
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0
                else:
                    pixdata[x, y] = 255
        img.show()#打开处理灰度后的图
        return img

    def delete_spot(self):
        images = self.processing_image()
        data = images.getdata()
        w, h = images.size
        black_point = 0
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                mid_pixel = data[w * y + x]  # 中央像素点像素值
                if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                    top_pixel = data[w * (y - 1) + x]
                    left_pixel = data[w * y + (x - 1)]
                    down_pixel = data[w * (y + 1) + x]
                    right_pixel = data[w * y + (x + 1)]
                    # 判断上下左右的黑色像素点总个数
                    if top_pixel < 10:
                        black_point += 1
                    if left_pixel < 10:
                        black_point += 1
                    if down_pixel < 10:
                        black_point += 1
                    if right_pixel < 10:
                        black_point += 1
                    if black_point < 1:
                        images.putpixel((x, y), 255)
                    black_point = 0
        #images.show() #进一步去燥
        #保存图片到文件夹
        images.save("E:/pictures/02.png")
        return images

    def image_str(self):
        image = self.delete_spot()
        #pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"  # 设置pyteseract路径
        result = pytesseract.image_to_string(Image.open(r"E:\pictures\02.png"))  # 图片转文字
        #result = pytesseract.image_to_string(image)
        print("result is ",result)
        resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
        result_six = resultj[0:6]  # 只获取前6个字符
        print("result_six ",result_six)  # 打印识别的验证码
        return result_six


if __name__ == '__main__':
    a = VerificationCode()
    image_result=a.image_str()
    a.driver.find_element_by_xpath(
        "//*[@id='app']/div/div[2]/section/main/div[2]/div/div[2]/div/form/div[1]/div/div/div[1]/input").send_keys(
        'admin')
    a.driver.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/section/main/div[2]/div/div[2]/div/form/div[2]/div/div/div/div[1]/input').send_keys(
        'admin123!@#')
    a.driver.find_element_by_css_selector('.el-input__inner').send_keys(image_result)
    login = a.driver.find_element_by_css_selector("button")
    login.click()















