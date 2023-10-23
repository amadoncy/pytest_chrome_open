from selenium import webdriver
from selenium.webdriver.common.by import By


wd = webdriver.Firefox()
wd.implicitly_wait(10)

wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')

'''
1.切换到 frame   可以用id or name
    wd.switch_to.frame('frame1')
    
2.可以根据属性切换到frame  
    wd.switch_to.frame(wd.find_element(By.CSS_SELECTOR, '[src="sample1.html"]'))    注意：一定是element  
    
3.切换到frame外部 switch_to.default_content    
'''
wd.switch_to.frame(wd.find_element(By.CSS_SELECTOR, '[src="sample1.html"]'))


elements = wd.find_elements(By.CSS_SELECTOR, '.plant')

for element in elements:
    print(element.get_attribute('outerHTML'))

wd.switch_to.default_content()
wd.find_element(By.ID, 'outerbutton').click()
