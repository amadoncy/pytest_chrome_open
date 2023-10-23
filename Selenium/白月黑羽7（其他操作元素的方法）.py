from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


wd = webdriver.Firefox()
wd.get('https://www.baidu.com')
wd.implicitly_wait(10)


ac = ActionChains(wd)
ac.move_to_element(
    wd.find_element(By.CSS_SELECTOR, '[name="tj_briicon"]')
).perform()