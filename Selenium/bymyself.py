from selenium import webdriver
from selenium.webdriver.common.by import By


wd = webdriver.Firefox()

wd.get('https://www.baidu.com')

# element = wd.find_element(By.ID, "kw")
# element.send_keys('曹老板\n')

elements = wd.find_elements(by=By.CLASS_NAME, value='name')
elements1 = wd.find_elements(by=By.TAG_NAME, value='div')


for element in elements1:
    print(element.text)

