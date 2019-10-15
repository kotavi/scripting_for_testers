from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('http://google.com')
element = driver.find_element_by_name('q')
element.send_keys('test automation')
element.send_keys(Keys.RETURN)


driver.get('https://www.seleniumhq.org')

element2 = driver.find_element_by_xpath('//*[@id="choice"]/tbody/tr/td[1]/center/a[1]/img')
element2.click()


element3 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '/html/head/title')))
assert element3, "Element was not found"

driver.back()

search_element = driver.find_element_by_xpath('//*[@id="q"]')
assert search_element, "Element was not found"
search_element.send_keys('webdriver')
go_button = driver.find_element_by_id('submit')
go_button.click()

WebDriverWait(driver, 2).until(
            EC.title_contains(('Google Custom Search')))

# Switch to iframe
import time
time.sleep(1)
driver.switch_to.frame('master-1')
link_elements = driver.find_element_by_tag_name('a')
print(link_elements.get_attribute('href'))

driver.back()
driver.close()