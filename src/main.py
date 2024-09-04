from fastapi import FastAPI, Request
from telebot import TeleBot
import os
from dotenv import load_dotenv
import logging


load_dotenv()


class Dotenv():
    def __init__(self):
        load_dotenv()
        
        self.bot_token = ''
        self.admin_id = ''
        self.student_ids = ''
        
        self.get_env_data()
        
    def get_env_data(self):
        self.bot_token = os.getenv('BOT_TOKEN')
        self.admin_id = int(os.getenv('ADMIN_ID'))
        self.student_ids = [int(item) for item in os.getenv('STUDENT_IDS').split(',')]
        

app = FastAPI()

BOT_TOKEN = Dotenv().bot_token
VERCEL_URL = 'https://expand-telegram-bot.vercel.app'
updates_webhook = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={VERCEL_URL}/webhook"

bot = TeleBot(BOT_TOKEN)


@app.post("/webhook")
async def webhook(request: Request):
    json_str = await request.body()
    update = bot.parse_update(json_str)
    bot.process_new_updates([update])
    return {"status": "ok"}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I'm your bot.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


async def set_webhook():
    try:
        webhook_url = f"{VERCEL_URL}/webhook"
        response = bot.set_webhook(url=webhook_url)
        
        if response:
            logging.info("Webhook set successfully")
        else:
            logging.error("Failed to set webhook")
    except Exception as e:
        logging.error(f"Error setting webhook: {e}")



if __name__ == "__main__":
    import asyncio
    asyncio.run(set_webhook())
