import telebot
from rivescript import RiveScript

# Config
TOKEN = ''  # <-- Your Telegram bot token
AUTHORIZED_USERS = {123456789}  # <-- Replace with actual Telegram user IDs
WELCOME_MESSAGE = "Welcome! How can I assist you today?"

# Initialize RiveScript
brain_bot = RiveScript()
brain_bot.load_directory('brain')
brain_bot.sort_replies()

# Initialize Telegram Bot
bot = telebot.TeleBot(TOKEN)

# Helper: check if user is authorized
def is_authorized(message):
    return message.from_user.id in AUTHORIZED_USERS

# Handle /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    if not is_authorized(message):
        return bot.reply_to(message, "🚫 You are not authorized to use this bot.")
    bot.reply_to(message, WELCOME_MESSAGE)

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if not is_authorized(message):
        return bot.reply_to(message, "🚫 You are not authorized to use this bot.")
    reply = brain_bot.reply("localuser", message.text)
    bot.reply_to(message, reply)

# Run bot
if __name__ == "__main__":
    bot.polling()
