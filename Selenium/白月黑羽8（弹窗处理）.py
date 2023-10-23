from selenium import webdriver
from selenium.webdriver.common.by import By
import time


wd = webdriver.Firefox()
wd.get('https://cdn2.byhy.net/files/selenium/test4.html')
wd.implicitly_wait(10)
#
#
# wd.find_element(By.ID, 'b1').click()
# print(wd.switch_to.alert.text)
#
# time.sleep(3)
# wd.switch_to.alert.accept()
# time.sleep(3)
#
# wd.find_element(By.ID, 'b2').click()
# print(wd.switch_to.alert.text)
# wd.switch_to.alert.accept()
#
# time.sleep(3)
# wd.find_element(By.ID, 'b2').click()
# print(wd.switch_to.alert.text)
# wd.switch_to.alert.dismiss()

wd.find_element(By.ID, 'b3').click()

alert_content = wd.switch_to.alert
alert_content.send_keys('您是否想要学习selenium')
wd.switch_to.alert.accept()


wd.find_element(By.ID, 'b3').click()
alert_content = wd.switch_to.alert
alert_content.send_keys('您是否想要学习selenium')
wd.switch_to.alert.dismiss()