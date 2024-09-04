from bot.Bot import Bot
from commands.Commands import Commands
import fastapi
import os
import telebot

app = fastapi.FastAPI()

# Initialize the bot
expand_bot = Bot()
commands = Commands(expand_bot.bot, expand_bot.username)
commands.handle_start() 
commands.handle_help() 
commands.setCommands()

@app.on_event("startup")
async def startup():
    # Set the webhook with your Vercel deployment URL
    webhook_url = f"https://{os.environ['VERCEL_URL']}/webhook"
    expand_bot.bot.set_webhook(webhook_url)

@app.post("/webhook")
async def webhook(update: dict):
    # Process the incoming update
    expand_bot.bot.process_new_updates([telebot.types.Update.de_json(update)])
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "Bot is running"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
