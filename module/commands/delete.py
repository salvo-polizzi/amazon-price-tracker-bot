from telegram import Update
from telegram.ext import CallbackContext 
import sqlite3

def deleteproduct(update: Update, context: CallbackContext):
    asin = context.args[0]
    conn = sqlite3.connect('amaztracker.db')
    cur = conn.cursor()

    try:
        cur.execute('''DELETE FROM prices WHERE asin = ?''', (asin,))
        conn.commit()
        conn.close()
        update.message.reply_text('Il prodotto è stato eliminato correttamente')
    except:
        update.message.reply_text('Il prodotto non è stato eliminato! Controlla di aver scritto correttamente l\'ASIN oppure di aver già eliminato il prodotto')