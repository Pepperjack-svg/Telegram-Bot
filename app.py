import telebot
from rivescript import RiveScript

# Initialize RiveScript
bot = RiveScript()
bot.load_directory('brain') 
bot.sort_replies()

TOKEN = ''  # <- Insert your Telegram bot token here
AUTHORIZED_USERS = set()  # <- Add authorized user IDs like: {123456789}

# Initialize Telegram Bot
telebot_bot = telebot.TeleBot(TOKEN)
WELCOME_MESSAGE = "Welcome! How can I assist you today?"

# Handle /start command
@telebot_bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    
    if user_id not in AUTHORIZED_USERS:
        telebot_bot.reply_to(message, "You are not authorized to use this bot.")
        return
    
    telebot_bot.reply_to(message, WELCOME_MESSAGE)

# Handle regular messages
@telebot_bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    
    if user_id not in AUTHORIZED_USERS:
        telebot_bot.reply_to(message, "You are not authorized to use this bot.")
        return
    
    reply = bot.reply("localuser", message.text)
    telebot_bot.reply_to(message, reply)

# Polling loop
if __name__ == "__main__":
    telebot_bot.polling()
