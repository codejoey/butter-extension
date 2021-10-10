from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/gp/product/B0983M5SHW?pf_rd_r=HHGPWKKVW24FPZGG8K1Z&pf_rd_p=8fe9b1d0-f378-4356-8bb8-cada7525eadd&pd_rd_r=1d84c989-d684-4e83-be9c-22359661f863&pd_rd_w=CrYwg&pd_rd_wg=qgFtM&ref_=pd_gw_unk')

#searchField = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
#searchField.send_keys('$')

#searchField.submit()

#This pulls price of item from the item's store page
itemPricePage = driver.find_element_by_id("price_inside_buybox")

#This pulls price of all items in cart as subtotal
cartSubtotal = driver.find_element_by_id("sc-subtotal-amount-activecart")