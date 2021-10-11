import selenium
from selenium import webdriver
import requests

#This pulls price of all items in cart as subtotal
def cartFromUrl(url):
    # The requests.Response() Object contains the server's response to the HTTP request.
    #response = requests.get(url)
    driver = webdriver.Chrome()
    driver.get(url)

    #This pulls price of all items in cart as subtotal
    cartSubtotal = driver.find_element_by_id("sc-subtotal-amount-activecart")

    return(cartSubtotal)

#This pulls price of item from the item's store page
def itemFromUrl(url):
    # The requests.Response() Object contains the server's response to the HTTP request.
    #response = requests.get(url)
    driver = webdriver.Chrome()
    driver.get(url)

    #This pulls price of item from the item's store page
    itemPricePage = driver.find_element_by_id("price_inside_buybox")
    
    return(itemPricePage)

"""
driver = webdriver.Chrome()
driver.get('https://www.amazon.com/gp/product/B0983M5SHW?pf_rd_r=HHGPWKKVW24FPZGG8K1Z&pf_rd_p=8fe9b1d0-f378-4356-8bb8-cada7525eadd&pd_rd_r=1d84c989-d684-4e83-be9c-22359661f863&pd_rd_w=CrYwg&pd_rd_wg=qgFtM&ref_=pd_gw_unk')

https://www.amazon.com/gp/product/B0983M5SHW?pf_rd_r=HHGPWKKVW24FPZGG8K1Z&pf_rd_p=8fe9b1d0-f378-4356-8bb8-cada7525eadd&pd_rd_r=1d84c989-d684-4e83-be9c-22359661f863&pd_rd_w=CrYwg&pd_rd_wg=qgFtM&ref_=pd_gw_unk
https://www.amazon.com/adidas-Racer-Adapt-Black-White/dp/B08CYBQ39N/ref=pd_sbs_1/147-0007094-2613048?pd_rd_w=7HWkT&pf_rd_p=3676f086-9496-4fd7-8490-77cf7f43f846&pf_rd_r=8CS97ABE29E3CKRDR13G&pd_rd_r=9e0287bb-e18f-41c3-be7b-711bc4e0884e&pd_rd_wg=nzxE0&pd_rd_i=B08CYBQ39N&psc=1

#searchField = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
#searchField.send_keys('$')

#searchField.submit()

#This pulls price of item from the item's store page
itemPricePage = driver.find_element_by_id("price_inside_buybox")

#This pulls price of all items in cart as subtotal
cartSubtotal = driver.find_element_by_id("sc-subtotal-amount-activecart")
"""
