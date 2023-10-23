from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

wd = webdriver.Firefox()
wd.implicitly_wait(10)
wd.get('https://cdn2.byhy.net/files/selenium/test2.html')

# select_element = wd.find_element(By.TAG_NAME, 'select')
#
# # 找到 select 下的所有 option 元素
# option_elements = select_element.find_elements(By.TAG_NAME, 'option')
#
# # 打印每个 option 元素的 value
# for option in option_elements:
#     value = option.get_attribute('value')
#     print(value)

select = Select(wd.find_element(By.ID, 'ss_single'))
select.select_by_visible_text('小雷老师')

selects = Select(wd.find_element(By.ID, 'ss_multi'))
# 清除所有 已经选中 的选项
selects.deselect_all()

selects.select_by_visible_text("小雷老师")
selects.select_by_visible_text("小凯老师")

"""   更多用法
1.deselect_by_value
根据选项的value属性值， 去除 选中元素


2.deselect_by_index
根据选项的次序，去除 选中元素


3.deselect_by_visible_text
根据选项的可见文本，去除 选中元素


4.deselect_all
去除 选中所有元素

5.select_by_index
根据选项的 次序 （从1开始），选择元素


6.select_by_visible_text
根据选项的 可见文本 ，选择元素。

比如，下面的HTML，

    <option value="foo">Bar</option>
     就可以根据 Bar 这个内容，选择该选项

 s.select_by_visible_text('Bar')
"""
