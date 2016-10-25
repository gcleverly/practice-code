# These are small snippets of code that can be used to scrape info from a website. Using the requests and beautifulSoup
# libraries, it is easy to quickly pull info from a site.


import requests
from bs4 import BeautifulSoup

# Try Google news first
GOOGLE_NEWS_URL = 'http://news.google.com'
response = requests.get(GOOGLE_NEWS_URL)
bs = BeautifulSoup(response.text, 'lxml')

bs.select('span.titletext')  # referring to <span class="title text"> of the HTML
first_title = bs.select('span.titletext')[0]  # trick is to assign to variable
first_title.get_text()

for title in bs.select('span.titletext'):
    print('+', title.get_text())

#Now comb Yahoo financial page to get stock prices
YAHOO_URL = 'http://www.nasdaq.com/symbol/yhoo/after-hours'
resp = requests.get(YAHOO_URL)

bs1 = BeautifulSoup(resp.text, 'lxml')

last_sale = bs1.select('#qwidget_lastsale')[0].get_text()
net_change = bs1.select('#qwidget_netchange')[0].get_text()
percent = bs1.select('#qwidget_percent')[0].get_text()

print(last_sale, net_change, percent)

hours = range_tag[0].get_text()
print(hours)

#Lastly, we can scrape info from Yelp as well
bs2 = BeautifulSoup(response1.text, 'lxml')

title = bs2.select('h1.biz-page-title')[0].get_text()
title.strip()

address = bs2.select('address > span')
print(address)

address_str = ''
for part in address:
    address_str += part.get_text() + '\n'
    print(part.get_text())

print(address_str)

[x.get_text() + '\n' for x in address]

range_tag = bs2.select('span.hour-range')
print(range_tag)

hours = range_tag[0].get_text()
print(hours)

hour_range = range_tag[0].get_text() if range_tag else ''  # this is a better way as [0] may give error
print(hour_range)

address_tag = bs2.select('address')
address = address_tag[0].get_text(strip=True)  # you can strip with get_text as well
print(address)

bs2.select('body')[0].get_text()  # all the text without html
