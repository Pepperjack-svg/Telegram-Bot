# Telegram Chatbot with RiveScript

## Features

- RiveScript integration for AI responses
- User authorization system
- Simple command handling (/start)
- Customizable welcome message

## Setup

1. Clone this repository
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Create a `brain` folder for your RiveScript files
4. Add your Telegram bot token in the code:
   ```python
   TOKEN = 'your_bot_token_here'
   ```
5. Add authorized user IDs:
   ```python
   AUTHORIZED_USERS = {123456789}  # Replace with actual user IDs
   ```

## Usage

1. Start the bot:
   ```
   python app.py
   ```
2. In Telegram:
   - Send `/start` to begin
   - The bot will respond to messages if you're authorized

## File Structure

```
bot.py            - Main bot script
brain/            - RiveScript brain files
README.md         - This file
```

## Customization

- Edit `WELCOME_MESSAGE` to change the welcome text
- Add more RiveScript files in the `brain` folder
- Extend command handlers as needed

## Requirements

- Python 3.x
- telebot library
- rivescript library
