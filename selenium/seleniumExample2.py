from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.phptravels.net/offers')

b_tags = driver.find_elements_by_tag_name('b')

price_list = []

for b in b_tags:
    price_list.append(b.text)
print(price_list)

clean_price_list = []

for price in price_list:
    if price:
        clean_price_list.append(float(price.split('$')[1].replace(',', '')))
print(clean_price_list)
driver.close()
