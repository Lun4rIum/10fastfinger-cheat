import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import pyperclip as pc
import os
import subprocess

user = os.getlogin()

path = str(subprocess.run('pwd',capture_output=True).stdout.decode('utf-8'))[:-1] + "/chromedriver"



options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(path, chrome_options=options)


url = 'https://10fastfingers.com/typing-test/french'


driver.get(url)
time.sleep(5)

ls = []

try:
    driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
    
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



