from selenium import webdriver
from selenium.webdriver.common.by import By


wd = webdriver.Firefox()
wd.get('https://cdn2.byhy.net/files/selenium/test1.html')


'''
绝对路径：
/html/body/....
相对路径：

后面所有元素  如: 
//div  查找页面全部div  //div/p   所有的div元素里面的 直接子节点 p


'''
elements = wd.find_elements(By.XPATH, '/html/body/div')
for element in elements:
    print(element.text)