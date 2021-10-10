import selenium
from selenium import webdriver
import requests

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/gp/product/B0983M5SHW?pf_rd_r=HHGPWKKVW24FPZGG8K1Z&pf_rd_p=8fe9b1d0-f378-4356-8bb8-cada7525eadd&pd_rd_r=1d84c989-d684-4e83-be9c-22359661f863&pd_rd_w=CrYwg&pd_rd_wg=qgFtM&ref_=pd_gw_unk')

#searchField = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
#searchField.send_keys('$')

#searchField.submit()

#This pulls price of item from the item's store page
itemPricePage = driver.find_element_by_id("price_inside_buybox")

#This pulls price of all items in cart as subtotal
cartSubtotal = driver.find_element_by_id("sc-subtotal-amount-activecart")

def cartFromUrl(url):
    # read images from URL
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    # convert the image to rgb
    image = img.convert('RGB')
     
    # resize the image to 100 x 100
    image = image.resize((100,100))
     
    detected_colors =[]
    for x in range(image.width):
        for y in range(image.height):
            detected_colors.append(closest_colour(image.getpixel((x,y))))
    Series_Colors = pd.Series(detected_colors)
    output=Series_Colors.value_counts()/len(Series_Colors)
    return(output.head(n).to_dict())