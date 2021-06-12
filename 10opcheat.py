import selenium
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



try:
    driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
    parser = argparse.ArgumentParser(description='[COOKIE] : Passed')
    print("[COOKIE] : Passed")
except:
    print("[COOKIE] : No Cookie...")
    pass
        
print("[ELEMENTS] : Loading Elements...")
html = driver.page_source

soup = BeautifulSoup(html, "lxml")
  
spans=soup.find('div', {'id': 'row1'}).text.split(' ')

f = len(spans)
i=0
for x in range(f):



    
    inputElement = driver.find_element_by_id("inputfield")

    cop = pc.copy(spans[i])
                    
    inputElement.send_keys(Keys.COMMAND, 'v')
    print('[Input] : sended :', "'",str(spans[i]),"'", ' | ', '[',i,']',"input sended")
                    
    inputElement.send_keys(Keys.SPACE)
                   

    i+=1

time.sleep(1)
mpm=soup.find('div', {'id': 'auswertung-result'}).text
print(mpm)

#driver.close()
