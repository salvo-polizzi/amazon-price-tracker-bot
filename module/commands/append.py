from requests_html import HTMLSession
from telegram import Update
from telegram.ext import CallbackContext 
import datetime
import sqlite3

#get the asins of products
#asins = []

""" with open("data/asins.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        asins.append(row[0]) """



def scraper(url: str, asin: str):

    s = HTMLSession()
    getter = s.get(url)

    #getter.html.render(sleep=1)
    
    
    #get the price
    first_price = getter.html.find('#apex_offerDisplay_desktop')[0].text
    definitive_price = ''
    for p in range(0, len(first_price)):
        if first_price[p] == '€':
            break
        else:
            definitive_price += first_price[p]
    definitive_price.replace(',','.').strip()
    
    #get the title
    title_product = getter.html.find('#productTitle')[0].text.strip()
    
    if len(title_product) >= 10:
        title_product = title_product[0:9]
    #print(title_product)

    #get the date
    date = datetime.date.today()

    tupla_product = (date, asin, title_product, definitive_price)
    return tupla_product

def append(update: Update,context: CallbackContext):

    asins = context.args[0]

    #connect to the database
    connection = sqlite3.connect('amaztracker.db')
    cursor = connection.cursor()

    #create the table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS prices(date, asin, title, price)''')

    #scraping product given by context arguments
    try:
        asins_list = cursor.execute('''SELECT asin FROM prices''').fetchall()
        if (asins,) in asins_list:
            update.message.reply_text('Hai già inserito questo prodotto!')
            return
        list_product = scraper(f'https://www.amazon.it/dp/{asins}', asins)
    except:
        update.message.reply_text('Il Codice ASIN che hai inserito è scorretto oppure è già stato inserito. Prova a reinserirlo!')
        return

    #inserting new values into the database
    cursor.execute('''INSERT INTO prices VALUES(?,?,?,?)''', list_product) 
    
    update.message.reply_text('Il nuovo prodotto è stato aggiunto')
    connection.commit()
    connection.close()


