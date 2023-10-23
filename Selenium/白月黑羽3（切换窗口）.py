import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

wd = webdriver.Firefox()
wd.implicitly_wait(10)

wd.get('https://cdn2.byhy.net/files/selenium/sample3.html')

link = wd.find_element(By.TAG_NAME, 'a')
link.click()
mainWindow = wd.current_window_handle

time.sleep(3)
'''
切换窗口   wd.switch_to.window(handle)

'''
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if 'Bing' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break

print(wd.find_element(By.CSS_SELECTOR, '[property="og:title"]').get_attribute('content'))
print(wd.title)
'''
    切回原来的窗口  mainwidow
'''
wd.switch_to.window(mainWindow)
wd.find_element(By.ID, 'outerbutton').click()

