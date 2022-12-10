from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text(text="Ciao sono il bot che scannerizza i prezzi su amazon")