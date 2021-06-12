import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import pyperclip as pc
import os

user = os.getlogin()


path = r"C:/Users/"+str(user)+"/Downloads/chromedriver_win32\chromedriver.exe"

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(path, chrome_options=options)

url = 'https://10fastfingers.com/typing-test/french'
driver.get(url)


time.sleep(3)

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
    inputElement.send_keys(Keys.CONTROL, 'v')
    print('[Input] : sended :', "'",str(spans[i]),"'", ' | ', '[',i,']',"input sended")

    inputElement.send_keys(Keys.SPACE)

    i+=1
