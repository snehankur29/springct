from selenium import webdriver
from getpass import getpass
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 


#driver = webdriver.Chrome(ChromeDriverManager().install)
driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver')
driver.get('https://demoblaze.com/index.html')

#1 -login with Given Credentials

loginBtn = driver.find_element("id", "login2")
loginBtn.click()


textUsername = driver.find_element("id", "loginusername")
textUsername.send_keys('sctqaautomation@grr.la')
time.sleep(5)

textPassword = driver.find_element("id", "loginpassword")
textPassword.send_keys('Spring@123')
time.sleep(5)

loginBtn1 = driver.find_element(By.XPATH, '//*[@class='btn btn-secondary']')
loginBtn1.click()
time.sleep(5)

# 3 - Select Samsung galaxy s6 and add to cart
selectMobile = driver.find_element("link text","Samsung galaxy s6")
selectMobile.click()
time.sleep(5)

addToCart = driver.find_element("link text","Add to cart")
addToCart.click()
time.sleep(5)

# driver.back()

# 4 Click on Home menu on the top and click on LAPTOP option 
navigateHome = driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[1]/a')
navigateHome.click()

# 5 - Add Dell i7 8 GB to the cart 
navigateToLaptop = driver.find_element("link text","Laptops")
navigateToLaptop.click()

navigateToDellLaptop = driver.find_element("link text","Dell i7 8gb")
navigateToDellLaptop.click()

time.sleep(5)

laptopAddToCart = driver.find_element("link text","Add to cart")
laptopAddToCart.click()
time.sleep(5)

# 6.	Click on Home menu and the top and click on MONITOR option 

navigateHome = driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[1]/a')
navigateHome.click()

navigateToMonitors = driver.find_element("link text","Monitors")
navigateToMonitors.click()

# 7 -	Add Asus Full HD monitor to the cart 

navigateToAsusMonitors = driver.find_element("link text","ASUS Full HD")
navigateToAsusMonitors.click()

monitorAddToCart = driver.find_element("link text","Add to cart")
monitorAddToCart.click()

# Navigate to cart menu

navigateToCart = driver.find_element("id","cartur")
selectMobile.click()

# 7.	Cart will comprise of 3 products,
# sort them as per the cost from Lowest to Highest and print them on console 

dict1 = {'Galaxy': 360, 'Dell': 700, 'ASUS': 230}
sorted_values = sorted(dict1.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]

print(sorted_dict)


# 8.	Fetch price of the items and sum it such that total value should be equal to summed up value 


items = {'Galaxy': 360, 'Dell': 700, 'ASUS': 230}
print(sum(items.values()))


totalPrice = driver.find_element("id","totalp")
print(totalPrice)

a = items
b = totalPrice
if b = a:
  print("both prices are same you can buy this product")
else:
  print("check the price and confirm before place order")

# 9.	Click on Place Order and enter information 
navigateToPlaceOrder = driver.find_element(By.XPATH, '//*[@class='btn btn-success']')
navigateToPlaceOrder.click()

name =input('please enter your name: ')
country =input('please enter your country: ')
city =input('please enter your city: ')
creditcard =input('please enter your creditcard: ')
month =input('please enter your month: ')
year =input('please enter your year: ')

textName = driver.find_element("id", "name")
textName.send_keys(name)

textCountry = driver.find_element("id", "country")
textCountry.send_keys(country)

textCity = driver.find_element("id", "city")
textCity.send_keys(city)

textCreditCard = driver.find_element("id", "card")
textCreditCard.send_keys(creditcard)

textMonth = driver.find_element("id", "month")
textMonth.send_keys(month)

textYear = driver.find_element("id", "year")
textYear.send_keys(year)

navigateToPurchaseOrder = driver.find_element(By.XPATH, '//html/body/div[3]/div/div/div[3]/button[2]']')
navigateToPurchaseOrder.click()

# 10.	Complete purchase and extract ID and Amount 

navigateToExtractID = driver.find_element(By.XPATH, '//*[@class='lead text-muted ']')



# 11.	Print those values on console  
for element in driver.find_elements(By.XPATH, '//*[@class='lead text-muted ']')
  print(element.text)

# print(navigateToExtractID)




























