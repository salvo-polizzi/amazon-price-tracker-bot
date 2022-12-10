from telegram import Update
from telegram.ext import CallbackContext

def help(update: Update, context: CallbackContext):
    update.message.reply_text('I seguenti comandi sono a disposizione:\n\
    - /append: Aggiungi un prodotto da seguire (Codice ASIN)\n \
    - /report: Resoconto dei prezzi fino a 2 settimane dei prodotti che hai seguito')