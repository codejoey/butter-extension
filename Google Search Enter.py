from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

searchField = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchField.send_keys('$')

searchField.submit()