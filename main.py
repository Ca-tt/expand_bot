from bot.Bot import Bot
from commands.Commands import Commands
from threading import Thread
import fastapi
import uvicorn
import os

app = fastapi.FastAPI()


@app.on_event("startup")
async def main():
    expand_bot = Bot()
    
    commands = Commands(expand_bot.bot, expand_bot.username)
 
    commands.handle_start() 
    commands.handle_help() 
    commands.setCommands()
    # bot_thread = Thread(target=expand_bot.run_bot, daemon=True)
    # bot_thread.start()
    

    expand_bot.run_bot()

@app.get("/")
async def root():
    return {"message": "Bot is running"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)


""" Render """
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)

