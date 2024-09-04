#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import fastapi
import uvicorn
import telebot
import os
import time
from telebot import apihelper

API_TOKEN = os.getenv('BOT_TOKEN')
WEBHOOK_HOST = os.getenv('VERCEL_URL')  # Replace with your Vercel domain or custom domain
WEBHOOK_PORT = 8080  # Use port 80 for HTTP
WEBHOOK_LISTEN = '0.0.0.0'  # Usually, this is fine

WEBHOOK_URL_BASE = "https://{}".format(WEBHOOK_HOST)
WEBHOOK_URL_PATH = "/{}/".format(API_TOKEN)

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(API_TOKEN)

app = fastapi.FastAPI(docs=None, redoc_url=None)

@app.post(f'/{API_TOKEN}/')
def process_webhook(update: dict):
    """
    Process webhook calls
    """
    if update:
        update = telebot.types.Update.de_json(update)
        bot.process_new_updates([update])
    else:
        return


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    """
    Handle '/start' and '/help'
    """
    bot.reply_to(message,
                 ("Hi there, I am EchoBot.\n"
                  "I am here to echo your kind words back to you."))


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    """
    Handle all other messages
    """
    bot.reply_to(message, message.text)

def set_webhook_with_retry(bot, url, max_retries=5, base_delay=1):
    """
    Set the webhook with retry logic to handle rate limiting and other errors.
    
    :param bot: The telebot instance.
    :param url: The webhook URL.
    :param max_retries: Maximum number of retry attempts.
    :param base_delay: Base delay for retries in seconds.
    """
    for attempt in range(max_retries):
        try:
            # Attempt to set the webhook
            bot.set_webhook(url=url)
            logger.info("Webhook set successfully.")
            break  # Exit loop if webhook setup is successful
        except apihelper.ApiTelegramException as e:
            # Handle rate limiting and API errors
            error_description = e.result_json.get("description")
            if error_description and "Too Many Requests" in error_description:
                retry_after = int(e.result_json.get("parameters", {}).get("retry_after", base_delay))
                delay = max(retry_after, base_delay)
                logger.warning(f"Rate limited. Retrying after {delay} seconds...")
                time.sleep(delay)  # Wait before retrying
            else:
                logger.error(f"Failed to set webhook: {e}")
                raise  # Re-raise exception if it's not related to rate limiting
        except Exception as e:
            # Handle unexpected errors
            logger.error(f"An unexpected error occurred: {e}")
            raise
        else:
            # Exponential backoff for other errors
            time.sleep(base_delay * (2 ** attempt))  # Increase delay for each attempt



# Remove webhook, it fails sometimes the set if there is a previous webhook
bot.remove_webhook()

# Set webhook with retry logic
# set_webhook_with_retry(
#     bot,
#     url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH
# )

uvicorn.run(
    app,
    host=WEBHOOK_LISTEN,
    port=WEBHOOK_PORT  # Use port 80 for HTTP
)
