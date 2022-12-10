from requests_html import HTMLSession
from telegram import Update
from telegram.ext import CallbackContext 
from module.data import asins


urls = 'https://www.amazon.it/dp/B00FYIUIH8'

def scraper(url: str):
    s = HTMLSession()
    getter = s.get(url)

    getter.html.render(sleep=1)
    
    #get the price
    first_price = getter.html.find('#apex_offerDisplay_desktop')[0].text
    definitive_price = ''
    for p in range(0, len(first_price)):
        if first_price[p] == '€':
            definitive_price += first_price[p]
            break
        else:
            definitive_price += first_price[p]
    
    #get the title
    title_product = getter.html.find('#productTitle')[0].text
    print(title_product)




scraper(urls)