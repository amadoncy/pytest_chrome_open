import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


response = requests.get('http://39.100.87.106:6888/api/user/login')

wd = webdriver.Firefox()
wd.implicitly_wait(10)

wd.get('http://39.100.87.106:6888/user/login')

element_name = wd.find_element(By.ID, 'username')
element_name.send_keys('admin')

element_password = wd.find_element(By.ID, 'password')
element_password.send_keys('123456')


element_act = wd.find_element(By.XPATH, "//*[@id='getCaptcha']/span")
element_act_send = wd.find_element(By.ID, 'InputCaptcha')
element_act_send.send_keys(element_act.text)

element_sumbit = wd.find_element(By.CSS_SELECTOR, '.ant-form-item-children button')
element_sumbit.click()

try:
    response = requests.get('http://39.100.87.106:6888/user/login')
    assert response.status_code == 200
    print('请求成功')
except AssertionError as e:
    print('请求失败，状态码为', response.status_code)
