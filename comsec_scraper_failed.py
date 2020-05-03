
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from config import *
'''
config.py excluded from repo by .gitignore, sample content below.
userid="foo"
password="blah"

'''
#driver = webdriver.Chrome(ChromeDriverManager().install())
#download driver from > https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome()


driver.get('https://www.commsec.com.au/')
#use chrome > inspect > copy element to get html.
'''
<input tabindex="1" type="text" id="txt-clientId" autocomplete="off" placeholder="CommSec Client ID">
//*[@id="txt-clientId"]

<input tabindex="2" name="ctl00$cpContent$txtPassword" type="password" id="password-field" placeholder="Password">

<button tabindex="3" id="btn-login" class="btn btn-primary btn-login btn-carrot">LOGIN</button>
'''


formElem_clientID = driver.find_element_by_id('txt-clientId')
formElem_clientID.send_keys(userid)
formElem_password = driver.find_element_by_id('password-field')
formElem_password.send_keys(password)
#submit fails when using click. needs mouse simulator?
#formElem_submit = driver.find_element_by_id('btn-login')
#formElem_submit.click()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'btn-login')))
element.click()
'''
this loads page with 201 error code, all subsequent attempts to locate elements fail.
comsec anti screen scraping method seems successful.
https://stackoverflow.com/questions/59442126/handshake-failed-returned-1-ssl-error-code-1-net-error-202

<input type="text" class="search" autocomplete="off" placeholder="Stock code or site search"
    aria-describedby="search-help" aria-autocomplete="list">
//*[@id="search-container"]/input

'''
#search_elem = driver.find_element_by_xpath('//*[@id="search-container"]/input')
search_elem = driver.find_element_by_class_name('search')

'''
<span>View Holdings</span>
'''
elem_view = driver.find_element_by_xpath("//div[text()='View Holdings']")

#<input id="submit" class="actionbutton" value="Go" type="submit" onclick="trackAsxCode()">
submitButton = driver.find_element_by_id('submit')
submitButton.click()
#this retrieves table of options on the stock.


#https://docs.scrapy.org/en/latest/intro/tutorial.html
