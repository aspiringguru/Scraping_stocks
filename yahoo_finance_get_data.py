import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome()
driver.get('https://finance.yahoo.com/quote/TSLA/')

'''
<span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" data-reactid="32">725.15</span>
'''
css_locator = 'div.quote-header-section span[data-reactid="32"]'
price = driver.find_element_by_css_selector(css_locator).text
price
'''
<span class="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)" data-reactid="33">+19.52 (+2.77%)</span>
'''
css_locator = 'div.quote-header-section span[data-reactid="33"]'
price_change = driver.find_element_by_css_selector(css_locator).text
price_change

'''
<td class="Ta(end) Fw(600) Lh(14px)" data-test="DAYS_RANGE-value" data-reactid="117">698.18 - 730.73</td>
'''
css_locator = 'div.quote-header-section span[data-reactid="117"]'
price_range = driver.find_element_by_xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[5]/td[2]').text
price_range
'''
<span data-reactid="53">Bearish</span>
<h5 class="D(ib) Va(m) Fz(12px) Fw(b)" data-reactid="43">Chart Events</h5>
'''
css_locator = 'div.quote-header-section span[data-reactid="43"]'
#chart_pattern_detected = driver.find_element_by_css_selector(css_locator).text
chart_pattern_detected = driver.find_element_by_xpath('//*[@id="interactive-2col-qsp-m"]/div[3]/div[2]/div[1]/span[1]/span').text
chart_pattern_detected


overvalued_chart = driver.find_element_by_xpath('//*[@id="quote-summary"]/div[3]/div[1]/div[3]/div[2]/div/div/div')
#overvalued_chart.get_attribute('innerHTML')
#overvalued_chart.get_attribute('outerHTML')
overvalued_chart.get_attribute("style")

esg_risk_score = driver.find_element_by_xpath('//*[@id="Col2-3-QuoteModule-Proxy"]/div/section/div[2]/div/div/div[1]').text
esg_risk_score

'''
<span data-reactid="159">Apr 28, 2020</span>
//*[@id="quote-summary"]/div[2]/table/tbody/tr[5]/td[2]/span
'''
earnings_date = driver.find_element_by_xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[5]/td[2]/span').text
earnings_date


'''
performance outlook - long term 9 mo +
<svg class="Va(m)! pill:h_Stk(white)! pill:h_Fill(white)! Cur(p)" width="26"
style="fill:#1ac567;stroke:#1ac567;stroke-width:0;vertical-align:bottom;"
height="26" viewBox="0 0 24 24" data-icon="arrow-filled-circle"
data-reactid="87">
<path d="M12 21c-4.97 0-9-4.03-9-9s4.03-9 9-9 9 4.03 9 9-4.03 9-9 9zM8.265 9.783c-.374.38-.35.972.057 1.32.405.35 1.038.327 1.413-.052L11 9.77V17c-.01.26.082.526.295.725.39.366 1.022.367 1.412.003.213-.2.305-.466.284-.728L13 9.77l1.265 1.28c.376.38 1.008.404 1.413.054.406-.35.432-.94.057-1.32L12 6 8.265 9.783z" data-reactid="88"></path></svg>
'''
#perf_out_9mo = driver.find_element_by_xpath('//*[@id="interactive-2col-qsp-m"]/div[3]/div[3]/ul/li[3]/a/div[1]/div[2]/svg')
#perf_out_9mo.get_attribute('class')
#broken, can't get by xpath
'''
<svg class="Va(m)! pill:h_Stk(white)! pill:h_Fill(white)! RotateZ(180deg) Cur(p)" width="26" style="fill:#ff4d52;stroke:#ff4d52;stroke-width:0;vertical-align:bottom;" height="26" viewBox="0 0 24 24" data-icon="arrow-filled-circle" data-reactid="69"><path d="M12 21c-4.97 0-9-4.03-9-9s4.03-9 9-9 9 4.03 9 9-4.03 9-9 9zM8.265 9.783c-.374.38-.35.972.057 1.32.405.35 1.038.327 1.413-.052L11 9.77V17c-.01.26.082.526.295.725.39.366 1.022.367 1.412.003.213-.2.305-.466.284-.728L13 9.77l1.265 1.28c.376.38 1.008.404 1.413.054.406-.35.432-.94.057-1.32L12 6 8.265 9.783z" data-reactid="70"></path></svg>
'''
#this fails.
#css_locator = 'div.quote-header-section span[data-reactid="70"]'
#perf_outlook = driver.find_element_by_css_selector(css_locator).text
