import selenium
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import pyperclip as pc

path = "/Users/olivierbail/Downloads/chromedriver"

options = webdriver.ChromeOptions()


options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
#options.add_argument("headless")

driver = webdriver.Chrome(path, chrome_options=options)




# Open the website

url = 'https://10fastfingers.com/typing-test/french'



driver.get(url)
time.sleep(5) # Sleep 10 seconds while waiting for the page to load...

ls = []


    
html = driver.page_source
    
soup = BeautifulSoup(html, "lxml")


   
spans=soup.find('div', {'id': 'row1'}).text.split(' ')

#ls.append(spans)
print(spans)
f = len(spans)
i=0
for x in range(f):



    
    inputElement = driver.find_element_by_id("inputfield")

    pc.copy(spans[i])
                    
    inputElement.send_keys(Keys.COMMAND, 'v')
                    
    inputElement.send_keys(Keys.SPACE)
                   

    print('Input sended : ', spans)

    i+=1
#driver.close()
