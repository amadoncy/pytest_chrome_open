import time
from tkinter import Image
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from PIL import Image

from util.captcha_api import YdmVerify

wd = webdriver.Firefox()
wd.implicitly_wait(10)
wd.get('http://218.200.239.185:8888/portalserver/scunioncmccgxsd29.jsp?wlanuserip=100.66.109.81&wlanacname=')

wd.switch_to.frame('topFrame1')


def put_username():
    wd.find_element(By.CSS_SELECTOR, 'input#username.reSize').send_keys('SCXY18781121619')


def put_password():
    wd.find_element(By.CSS_SELECTOR, 'input#passwordIn_1.reSize').click().send_keys('121619')


def click_btn():
    wd.find_element(By.CSS_SELECTOR, 'div#login_btn').click()


def save_captcha(driver):
    img = driver.find_element(By.XPATH, '//*[@id="randomimage"]')
    driver.save_screenshot("./screenshot.png")  # 全屏截图

    left = img.location['x']  # 此处的x和y是图片验证码左上角的点再浏览器中的x轴y轴对应的值
    top = img.location['y']
    right = left + img.size['width']
    bottom = top + img.size['height']

    dpr = driver.execute_script('return window.devicePixelRatio')
    im = Image.open('./screenshot.png')
    image_obj = im.crop((left * dpr, top * dpr, right * dpr, bottom * dpr))  # 按照提供的图片验证码的左上右下的坐标值对图片验证码进行裁剪
    w = image_obj.size[0]  # 图形验证码的宽度
    h = image_obj.size[1]  # 图形验证码的高度
    image = image_obj.convert("RGB")  # 把图片强制转成RGB
    for i in range(0, w):  # 遍历所有长度的点
        for j in range(0, h):  # 遍历所有宽度的点
            temp = 0
            color = image.getpixel((i, j))
            for r in color:
                # 下面的100根据情况设置，因为我发现我们公司的验#证码干扰的线条都是黑色的，我把所有的像素都打印出来后，发现RGB三#原色中（x，y，x）三个值都小于100的貌似都是黑色，所以就用下面的这种笨办法了。
                if r <= 100:
                    temp = temp + 1
                    if temp == 3:
                        image.putpixel((i, j), (209, 207, 242))

    image = image.convert("L")
    image.save("./captcha.png")


def input_captcha(driver):
    """
    输入验证码
    Args:
        driver: driver

    Returns:driver

    """
    save_captcha(driver)
    captcha_input = driver.find_element(By.CSS_SELECTOR, 'input#ps.reSize')
    captcha_input.click()
    captcha_input.clear()
    with open(r'./captcha.png', 'rb') as f:
        s = f.read()
    code = YdmVerify().common_verify(image=s)
    captcha_input.send_keys(code)
    captcha_input.send_keys(Keys.RETURN)
    driver.implicitly_wait(1)
    return driver


if __name__ == '__main__':
    put_username()
    time.sleep(2)
    input_captcha(driver=wd)
    put_password()
