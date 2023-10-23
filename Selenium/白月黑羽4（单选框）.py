import time

from selenium import webdriver
from selenium.webdriver.common.by import By

wb = webdriver.Firefox()
wb.implicitly_wait(10)
wb.get('https://cdn2.byhy.net/files/selenium/test2.html')

element = wb.find_element(By.CSS_SELECTOR,
                          '#s_radio input[name="teacher"]:checked')
print(element.get_attribute('value'))

time.sleep(2)
wb.find_element(By.CSS_SELECTOR,
                '#s_radio input[value="小雷老师"]').click()


