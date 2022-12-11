from telegram import Update
from telegram.ext import CallbackContext 
import sqlite3
import pandas as pd
import json


def report(update: Update, context: CallbackContext):
    
    #create the connection with database
    connect = sqlite3.connect('amaztracker.db')

    results = pd.read_sql_query('''SELECT * FROM prices''', connect).to_string()

    update.message.reply_text(results)

def stampa_tutto():
    connect = sqlite3.connect('amaztracker.db')

    results = pd.read_sql_query('''SELECT * FROM prices''', connect)

    print(results)

#stampa_tutto()