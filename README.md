---

### ✅ Updated Python Bot Script (`bot.py`)

```python
import telebot
from rivescript import RiveScript

# Initialize RiveScript
bot = RiveScript()
bot.load_directory('brain') 
bot.sort_replies()

# === CONFIGURE THESE BEFORE RUNNING ===
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
```

---

### 📄 `README.md`

````markdown
# 🤖 Telegram Chatbot with RiveScript

This is a simple Telegram chatbot powered by [RiveScript](https://www.rivescript.com/) and Python, designed to respond to natural-language messages.

---

## 🧠 Features

- Uses **RiveScript** for intelligent conversation handling
- Restricted access via **authorized Telegram user IDs**
- Simple setup and extensible codebase

---

## ⚙️ Requirements

- Python 3.7+
- Telegram account
- Telegram bot token (get from [@BotFather](https://t.me/BotFather))

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/telegram-rivescript-bot.git
   cd telegram-rivescript-bot
````

2. **Install dependencies**

   ```bash
   pip install pyTelegramBotAPI rivescript
   ```

3. **Create RiveScript brain files**

   * Inside the project directory, create a folder named `brain`
   * Add `.rive` files with chatbot logic inside `brain/`
   * Example content for `brain/start.rive`:

     ```
     + hello
     - Hello there! How can I help you?

     + my name is *
     - Nice to meet you, <star>!
     ```

4. **Edit `bot.py`**

   * Replace `TOKEN = ''` with your actual bot token.
   * Replace `AUTHORIZED_USERS = set()` with your Telegram user ID(s):

     ```python
     AUTHORIZED_USERS = {123456789, 987654321}
     ```

---

## ▶️ Running the Bot

```bash
python bot.py
```

Your bot will go live and begin listening for messages from authorized users.

---

## 🔒 Authorization

Only users whose Telegram user IDs are listed in the `AUTHORIZED_USERS` set can use this bot. This adds a basic level of privacy and security.

---

## 📁 File Structure

```
telegram-rivescript-bot/
├── bot.py
├── brain/
│   └── start.rive
└── README.md
```

---

## 📌 Notes

* Make sure your `.rive` files have proper syntax.
* You can test `.rive` replies directly using the RiveScript Python REPL.
* For production use, consider switching from `polling` to `webhook`.

---
