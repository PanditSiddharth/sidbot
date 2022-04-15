from telegram import *
from telegram.ext import *

bot = Bot(TELEGRAM_TOKEN)

bot_token = TELEGRAM_TOKEN
bot_user_name = "Sidsanalysisbot"
URL = "the heroku app link that we will create later"

updater = Updater(TELEGRAM_TOKEN,use_context=True)

dispatcher = updater.dispatcher
dp = dispatcher 

def function(update:Update,context:CallbackContext):
    bot.send_message(
    chat_id = update.effective_chat.id,
    text = "hi hello"
);
start_value = CommandHandler('start',  function)
dispatcher.add_handler(start_value)


def function1(update:Update,context:CallbackContext):
    bot.send_message(
    chat_id = update.effective_chat.id,
    text = "Bots 2nd Command"
);
start_value1 = CommandHandler('hi',  function1)
dispatcher.add_handler(start_value1)

updater.start_polling()

def welcome(update,context):
    name = from_user.username
    update.message.reply_text("hi welcome")
    dp = updater.dispatcher
dp.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))
updater.start_polling(allowed_updates=Update.ALL_TYPES)

def mimic(update, context):
    context.bot.send_message(update.message.chat.id, update.message.text)
    
dp.add_handler(MessageHandler(Filters.text, mimic)) 

dp.add_handler(MessageHandler(Filters.sticker, mimic)) 

updater.idle()
