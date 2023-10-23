from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Firefox()
wd.implicitly_wait(5)
wd.get('https://cdn2.byhy.net/files/selenium/sample1b.html')

'''
1.
根据子元素 和后代元素查找  （1.) 元素1 > 元素2      (2.) 元素1>元素2>元素3>元素4   

2.后代元素的查找
elements = wd.find_elements(By.CSS_SELECTOR, '.plant span')

根据属性值  查找标签
elements = wd.find_elements(By.CSS_SELECTOR, '[href="http://www.miitbeian.gov.cn"]')
如果网页只有一个href属性的话  直接可以写'[href]'


3.可加前置条件指定查询
如： div[class = 'SKnet']
    .plant[name = 'SKnet']
elements = wd.find_elements(By.CSS_SELECTOR, 'div[class = 'SKnet']')

4. 是父元素的第几个子节点  nth-child        
elements = wd.find_elements(By.CSS_SELECTOR, 'span:nth-child(2)')
    倒数子元素  nth-last-child
    
    偶数节点  nth-child(even)
    奇数节点  nth-child(odd)  
    
5、父元素的第几个某类型的子节点
    如：span:nth-of-type(1)  第一个span类型的子元素    
    倒数子元素  span:nth-last-of-type(1)
    

6、相邻节点  后代所有节点
    如：  h3 + span (紧跟h3下面的span)
         h3 ~ span (h3下面 全部的span)
'''

# for element in elements:
#     print(element.get_attribute('outerHTML'))
