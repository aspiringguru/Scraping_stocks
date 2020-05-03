'''
note to self > use ubuntu conda environment.
cd /mnt/d/2020/coding/Scraping_stocks

https://github.com/geduldig/TwitterAPI
pip install TwitterAPI
'''

from TwitterAPI import TwitterAPI
from config import *
print("twitter_consumer_key:"+ twitter_consumer_key)

api = TwitterAPI(twitter_consumer_key, twitter_consumer_secret, \
        twitter_access_token_key, twitter_access_token_secret)
print("api:", api)

r = api.request('statuses/update', {'status':'I am back. Did you miss me?'})
print(r.status_code)


file = open('notebooks/AUDUSD%3DX_close_bollinger_breakouts.png', 'rb')
data = file.read()
r = api.request('statuses/update_with_media', {'status':'chart for #AUDUSD'}, {'media[]':data})
print(r.status_code)
