
from bs4 import BeautifulSoup
import requests
import pandas as pd

HEADERS = ({'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/44.0.2403.157 Safari/537.36',
                           'Accept-Language': 'en-US, en;q=0.5'})

URL= 'https://www.amazon.pl/gp/bestsellers'
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")
try:
    title = soup.find('span',
                    attrs={'class':'a-carousel-card'})
    title_value = title.string
    #title_string = title_value.strip().replace(',','')
    print(title_value)
except AttributeError:
                
        title_string = 'NA'
        print('Product Title = ', title_string)

def reader(filename):
    URLS = pd.read_csv(filename, delimiter=';')
    #print(URLS['link'][0])
    #print('----------')
    return URLS

#def urlfinder():

#reader('urls1.csv')