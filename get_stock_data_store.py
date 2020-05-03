'''
nb: uses selenium. has to run in windows for now.
'''
from config import *
import os
import pandas as pd
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
timeout = 3


df_stock_codes = pd.read_csv(SandP_stockcodes_filename)
df_stock_codes

base_url = "https://finance.yahoo.com/quote/"

for index, row in df_stock_codes.iterrows():
    #print(row['Symbol'])
url = base_url+ row['Symbol']
url = base_url+"TSLA"
print("url:", url)
driver.get(url)
try:
    element_present = EC.presence_of_element_located((By.ID, 'main'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")
    css_locator = 'div.quote-header-section span[data-reactid="32"]'
    price = driver.find_element_by_css_selector(css_locator).text
    print("price:", price)
    css_locator = 'div.quote-header-section span[data-reactid="33"]'
    price_change = driver.find_element_by_css_selector(css_locator).text
    print("price_change:", price_change)
    css_locator = 'div.quote-header-section span[data-reactid="117"]'
    price_range = driver.find_element_by_xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[5]/td[2]').text
    print("price_range:", price_range)
    css_locator = 'div.quote-header-section span[data-reactid="43"]'
    chart_pattern_detected = driver.find_element_by_xpath('//*[@id="interactive-2col-qsp-m"]/div[3]/div[2]/div[1]/span[1]/span').text
    print("chart_pattern_detected:", chart_pattern_detected)
    overvalued_chart = driver.find_element_by_xpath('//*[@id="quote-summary"]/div[3]/div[1]/div[3]/div[2]/div/div/div')
    overvalued_chart_style = overvalued_chart.get_attribute("style")
    print("overvalued_chart_style:", overvalued_chart_style)
    esg_risk_score = driver.find_element_by_xpath('//*[@id="Col2-3-QuoteModule-Proxy"]/div/section/div[2]/div/div/div[1]').text
esg_risk_score = driver.find_element_by_xpath('//*[@id="Col2-3-QuoteModule-Proxy"]/div/section/div[2]/div/div/div[1]').text
#<div class="Fz(27px) Fw(600) D(ib)">31.4</div>
esg_risk_score = driver.find_element_by_css_selector(".Fz(27px).Fw(600).D(ib)")
print("esg_risk_score:", esg_risk_score)
earnings_date = driver.find_element_by_xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[5]/td[2]/span').text
print("earnings_date:", earnings_date)

driver.quit()









if not os.path.exists(store_filename):
    open(store_filename, 'w').close()
