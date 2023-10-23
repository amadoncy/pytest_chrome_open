from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 实例化驱动
wd = webdriver.Firefox()

# 隐式等待10s   每个findelement、findelements方法都会执行这个策略
wd.implicitly_wait(10)

# 获取网页响应
wd.get('https://www.baidu.com')

element = wd.find_element(By.ID, 'kw')
# \n回车符号
element.send_keys('文朝阳是谁\n')
# element.click()
elements = wd.find_element(By.CLASS_NAME, 'content-right_8Zs40')
print(elements.text)


#  休眠3s  然后清空输入框内容
time.sleep(3)
element.clear()

element = wd.find_element(By.ID, 'kw')
element.send_keys('曹老板是谁\n')


# element = wd.find_element(By.ID, 'su')
# element.click()

elements = wd.find_element(By.CLASS_NAME, 'text-content_2Ev0u ')
print(elements.text)


'''
CSS_SELECTOR 获取内容
elements = wd.find_element(By.CSS_SELECTOR, '.toplist1-tr_4kE4D')
print(elements.get_attribute('outerHTML'))
'''

# 获取input里面内容
# print(element.get_attribute('value'))    元素的文本内容没有完全展示在页面上有问题  这时 value替换innerText texContent


# 跟隐式等待是一个原理底层
# while True:
#     try:
#         elements = wd.find_element(By.CLASS_NAME, 'content-right_8Zs40')
#         print(elements.text)
#         break
#     except Exception :
#         time.sleep(1)


# 执行完自动关闭网页、驱动
# wd.quit()
