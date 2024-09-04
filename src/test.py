from utils.Dotenv import Dotenv
from fastapi import FastAPI, Request
from telebot import TeleBot
import logging

app = FastAPI()

BOT_TOKEN = Dotenv().bot_token
VERCEL_URL = 'https://expand-telegram-bot.vercel.app/'
updates_webhook = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={VERCEL_URL}/{BOT_TOKEN}"

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


# Set webhook
async def set_webhook():
    webhook_url = 'https://your-vercel-deployment-url.vercel.app/webhook'
    bot.set_webhook(url=webhook_url)


# Call this function to set the webhook when starting the app
import asyncio
asyncio.run(set_webhook())