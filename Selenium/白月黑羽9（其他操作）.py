from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Firefox()
wd.get('https://cdn2.byhy.net/files/selenium/test4.html')
wd.implicitly_wait(5)

# 获取窗口大小
wd.get_window_size()
# 改变窗口大小 driver.set_window_size(x, y)
wd.set_window_size(600, 700)

# 获取当前网页title
print(wd.title)
# 获取网站地址栏文本
print(wd.current_url)

# 截屏保存为图片文件
wd.get_screenshot_as_file('1.png')