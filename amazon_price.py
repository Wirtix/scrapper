from bs4 import BeautifulSoup
import requests
import pandas as pd
from csvreader import reader

'''This program is scrapping data from Amazon website. 
You can paste URLs to url1.csv file and then run this program
TODO addding more infromations which we can get from website
TODO auto url's scrapper
'''

HEADERS = ({'User-Agent':
           'Mozilla/5.0 (X11; Linux x86_64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/44.0.2403.157 Safari/537.36',
                           'Accept-Language': 'en-US, en;q=0.5'})

URL= 'https://www.amazon.pl/LEGO-dziewczynek-minifigurką-odgrywania-71805/dp/B0CFVZ532T/ref=sr_1_1?crid=1SZCEY3M7PKHA&dib=eyJ2IjoiMSJ9.OqwZXu16XrLDFu0dMIns2i4h6dTrao4eNcjQy3CcT8GIssGmiO8yhcCGXz81NGSdLIPC5Lvql5QOZtWPR5PV00BuBYvr94nN-aVYIK6Ek1KtsOPi9tBA85KlUa9vC0hadoxX8PpG47DLkQ0Yooo4qrpNKwYoXKm2N3BMjC0Y-QZ_FozUtE1SI370l0NxGoTJ2LwahktbCbR7TR2m41fAs4lQgxetmXKqv3IuuOP6g4bVWnVIn6Wq0XZPW858lMFs82yPLVsUyVHictM9BUNzUi8RxJn6REhitdSbPM7I1FY.QwLc8XE7ZpMkVYvp98xBboPhzqiXAfFLCezwwQjdBbE&dib_tag=se&keywords=lego+ninjago&qid=1714910942&sprefix=%2Caps%2C121&sr=8-1'

#title importing, TODO scraping from page from serching
'''def FileReader(filename):
        file = open(filename, 'r')
        urls = []
        for line in file:
                urls.append(str(line))

        file.close()
        return urls

def get_doc(url):
        response  = requests.get(url, headers=HEADERS)
        print(response.status_code)
        if response.ok:
                with open('amazon_html_page.html', 'a', encoding='utf8') as file:
                        file.write(response.text)
                doc = BeautifulSoup(response.text, 'html.parser')
                return doc
        
def getnextpage(doc):
        base = 'https://www.amazon.com'
        page = doc.find('ul', class_ = 'a-pagination')
        if not page.find('li', class_='a-disabled a-last'):
                url = base + str(page.find('li', class_ = 'a-last').find('a')['href'])
                print(url)
                return url
        else:
                return
getnextpage()
'''

# reading urls from file
URLS = reader('urls1.csv')
print(URLS)

#write collected data into file
def FileWritting(*args):
        File = open('out.csv', 'a')
        for arg in args:
                File.write(f'{arg},')
        File.write('\n')
        File.close()
#scraping data
def Scrapper(url):

        webpage = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "lxml")
        try:
                title = soup.find('span',
                                attrs={'id':'productTitle'})
                title_value = title.string
                title_string = title_value.strip().replace(',','')
                print(title_value)
        except AttributeError:
                
                title_string = 'NA'

                print('Product Title = ', title_string)


        try:
                price = soup.find('span',
                                attrs={'class':'aok-offscreen'})
                price_value = price.string
                price_string = price_value.strip().replace(',','.')
                print('Product price: ', price_string)
        except AttributeError:
                
                price_string = 'NA'

                print('Product Price = ', price_string)



        try:
                rate_c = soup.find('span',
                                attrs={'id':'acrCustomerReviewText'})
                rate_value = rate_c.string
                rate_count = rate_value.strip()[rate_value.find(':') + 2:]
                print('Number of ratings: ', rate_count)
        except AttributeError:
                
                rate_count = 'NA'

                print('product rate= ', rate_count)


        try:
                rate = soup.find('span',
                                attrs={'class':'a-size-medium a-color-base'})
                rate_string = rate.string[:rate.string.find(' ')].replace(',', '.').strip()
                print('product rate: ', rate_string)
        except AttributeError:
                
                rate = 'NA'

                print('product rate= ', rate)

        
        try:
                avaliable1 = soup.find('span',
                                attrs={'class':"a-size-medium a-color-success"})
                avaliable_value1 = avaliable1.string
                #avaliable_string = avaliable_value.strip()[avaliable_value.find(': ')+1]
                print('avaliability:', avaliable_value1)
        except AttributeError:
                
                avaliable_value1 = 'NA'
                print('product avaliability 2.0 = ', avaliable_value1)

        try:
                brand = soup.find('a',
                                attrs={'class':'a-size-medium a-color-base'})
                brand_string = brand.string
                print('product brand: ', brand_string)
        except AttributeError:
                
                brand = 'NA'

                print('Brand: ', brand)

        print('-'*30)
        FileWritting(title_string, price_string, avaliable_value1, rate_count, rate_string)

for url in URLS['link']:
        if __name__ == '__main__':
                Scrapper(url)

