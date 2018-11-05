from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import requests
from random import choice

"""
scriping html part example:
<span class="price" itemprop="price" data-bind="css: {'merchant': !isHepsiburadaProduct(), 'hepsiburada': isHepsiburadaProduct()}" id="offering-price" content=4289.00>
"""
#page_link = 'https://www.hepsiburada.com/asus-x542ur-gq030-intel-core-i7-7500u-8gb-1tb-gt930mx-freedos-15-6-tasinabilir-bilgisayar-p-HBV000008OBG5'
page_link = input('Enter a link : ')
desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'] 
def random_headers():
        return {'User-Agent': choice(desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

try:
    page =  requests.get(page_link,headers=random_headers())
    if page.status_code == 200:
        # extract
        pass
    else:
        print(page.status_code)
         # notify, try again   
except requests.Timeout as e:
    print("It is time to timeout")
    print(str(e)) 
# other exception


html = BeautifulSoup(page.content, 'lxml')

price = html.find('span',{'class':'price'})

price = price.text.split('\n')  #split price 
offering_price = price[1]
priceCurrency = price[2]

print("{0} {1}".format(offering_price,priceCurrency))