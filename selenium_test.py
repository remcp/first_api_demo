from selenium import webdriver
from selenium.webdriver.common.by import By



# search = "pizza"

# URL = "https://www.jumbo.com/zoeken/?searchType=keyword&searchTerms=" + search
# user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0'}
# driver.get(URL)

# products = driver.find_elements(By.CLASS_NAME,"title-link")
# price = driver.find_elements(By.CLASS_NAME,"current-price")

# combined_prices = []
# for x in range (len(price)):
    
#     combined_price = price[x].text.replace('\n', ',')
#     combined_prices.append(combined_price)
    
 
# for x in range (len(combined_prices)):
#     print(products[x].text)
#     print(combined_prices[x])



def getprices(search):
    driver = webdriver.Chrome()
    URL = "https://www.jumbo.com/zoeken/?searchType=keyword&searchTerms=" + search
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0'}
    driver.get(URL)
    
    products = driver.find_elements(By.CLASS_NAME,"title-link")
    price = driver.find_elements(By.CLASS_NAME,"current-price")
    
    combined_prices = []
    for x in range (len(price)):
    
        combined_price = price[x].text.replace('\n', ',')
        combined_prices.append(combined_price)
    
    pricesandproducts = []
    for x in range (len(combined_prices)):
        pricesandproducts.append(products[x].text)
        pricesandproducts.append(combined_prices[x])
    driver.quit()

    return pricesandproducts
