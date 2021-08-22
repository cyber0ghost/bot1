import telegram 
from telegram import *
from telegram.ext import *
import api as Keys

bot = telegram.Bot(token= '1750649064:AAFBnZlsJjPk-X8DyVLjtyyYhoLRYhEVpC4')
print("Bot started..")

bot.send_message(chat_id='-1001568310238', text='bot started successfully')

def start_command(update, contetxt):
     update.message.reply_text('Bot started \ndeveloped by:- @ghostoftheuchia')
def replay_command(update, contetxt):
          bot.send_message(chat_id=update.message.chat_id,
                     text='Request submitted \ndeveloped by:- @ghostoftheuchia')
          bot.forward_message(chat_id='-1001568310238', from_chat_id=update.message.chat_id, message_id=update.message.message_id)
def main():
     updater = Updater(Keys.API_KEY, use_context=True)
     dp = updater.dispatcher

     dp.add_handler(CommandHandler("start", start_command))
     dp.add_handler(CommandHandler("request", replay_command))


     updater.start_polling()
     updater.idle()

main()
