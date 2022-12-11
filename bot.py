from telegram import Update, Bot
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from module.commands import start, help, append, reportlast, delete
import yaml

#get the token
with open("config.yaml", "r") as f:
    yaml_config = yaml.safe_load(f)
token = yaml_config["token"]

up = Updater(token=token, use_context=True)
bot = Bot(token=token)

up.dispatcher.add_handler(CommandHandler('start', start.start))
up.dispatcher.add_handler(CommandHandler('help', help.help))
up.dispatcher.add_handler(CommandHandler('append', append.append))
up.dispatcher.add_handler(CommandHandler('report', reportlast.report))
up.dispatcher.add_handler(CommandHandler('delete', delete.deleteproduct))
up.start_polling()