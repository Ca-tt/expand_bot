import json
import os
import time
from http.server import BaseHTTPRequestHandler
from telebot import types
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from telebot import TeleBot, types
import os
from dotenv import load_dotenv
import logging

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = TeleBot(BOT_TOKEN, threaded=False)


@bot.message_handler()
def main(msg):
    bot.send_message(msg.chat.id, msg.text)


class handler(BaseHTTPRequestHandler):
    server_version = 'WebhookHandler/1.0'

    def do_GET(self):
        time.sleep(1.5)
        bot.set_webhook(os.getenv('VERCEL_URL'))
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        cl = int(self.headers['Content-Length'])
        post_data = self.rfile.read(cl)
        body = json.loads(post_data.decode())

        bot.process_new_updates([types.Update.de_json(body)])

        self.send_response(204)
        self.end_headers()
