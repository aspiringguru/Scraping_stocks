

#setup
D:\2020\coding\Scraping_stocks
#in cmd window ubuntu
cd /mnt/d/2020/coding/Scraping_stocks
conda deactivate
python3 -m venv env
source env/bin/activate
deactivate


use previous project as template.
https://github.com/aspiringguru/stock_analysis/blob/master/ASX_options_selenium_scraping.py



https://www.commsec.com.au/
<input tabindex="1" type="text" id="txt-clientId" autocomplete="off" placeholder="CommSec Client ID">
//*[@id="txt-clientId"]

<input tabindex="1" type="hidden" name="ctl00$cpContent$txtLogin" id="txt-clientId-hidden" autocomplete="off" value="50142048">
<input tabindex="2" name="ctl00$cpContent$txtPassword" type="password" id="password-field" placeholder="Password">
//*[@id="password-field"]

<button tabindex="3" id="btn-login" class="btn btn-primary btn-login btn-carrot">LOGIN</button>
//*[@id="btn-login"]



https://www2.commsec.com.au/Public/HomePage/Login.aspx?LoginResult=LoginFailed
<input name="ctl00$cpContent$txtLogin" type="text" value="50142048" id="ctl00_cpContent_txtLogin" class="LoginID" autocomplete="off" style="line-height: 25px">
//*[@id="ctl00_cpContent_txtLogin"]

<input name="ctl00$cpContent$txtLogin" type="text" value="50142048" id="ctl00_cpContent_txtLogin" class="LoginID" autocomplete="off" style="line-height: 25px">

<input name="ctl00$cpContent$fakepassword" type="text" id="ctl00_cpContent_fakepassword" class="text LoginPassword watermark" autocomplete="off" style="line-height: 25px">
//*[@id="ctl00_cpContent_fakepassword"]

<input name="ctl00$cpContent$txtPassword" type="password" id="ctl00_cpContent_txtPassword" class="text LoginPassword passwordHidden" autocomplete="off" style="line-height: 25px">
//*[@id="ctl00_cpContent_txtPassword"]


<input type="submit" name="ctl00$cpContent$btnLogin" value="Login" id="ctl00_cpContent_btnLogin" class="LargeButton" style="font-size:16px;">
//*[@id="ctl00_cpContent_btnLogin"]
