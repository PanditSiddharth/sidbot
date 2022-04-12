from telegram import *
from telegram.ext import *

bot = Bot("5177532718:AAGNPPGUfspoeBGZeNzPQXusu-14qMB-mlU")

updater = Updater("5177532718:AAGNPPGUfspoeBGZeNzPQXusu-14qMB-mlU",use_context=True)

dispatcher = updater.dispatcher
def function(update:Update,context:CallbackContext):
    bot.send_message(
    chat_id = update.effective_chat.id,
    text = "hi hello"
);
start_value = CommandHandler('start',  function)
dispatcher.add_handler(start_value)
updater.start_polling()