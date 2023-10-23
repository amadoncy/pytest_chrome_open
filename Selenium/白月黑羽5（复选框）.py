from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Firefox()
wd.implicitly_wait(10)
wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

'''
先点击已选择复选框的框框 取消掉（确保选择的是小雷老师）
element = wd.find_element(By.CSS_SELECTOR, '#s_checkbox :checked')
element.click()


element = wd.find_element(By.CSS_SELECTOR, '#s_checkbox [value="小雷老师"]')
element.click()
print(element.get_attribute('value'))
'''

elements = wd.find_elements(By.CSS_SELECTOR, '#s_checkbox :checked')

# 这里确定是已经点击过复选框人的值
for element in elements:
    element.click()
    print(element.get_attribute('value'))

wd.find_element(By.CSS_SELECTOR, '#s_checkbox [value="小雷老师"]').click()