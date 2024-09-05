from bot.Bot import Bot
from commands.Commands import Commands
import fastapi
import uvicorn
from os import getenv

PORT = int(getenv("PORT", 8000))

app = fastapi.FastAPI()


@app.on_event("startup")
async def main():
    expand_bot = Bot()
    
    commands = Commands(expand_bot.bot, expand_bot.username)
 
    commands.handle_start() 
    commands.handle_help() 
    commands.setCommands()

    expand_bot.run_bot()



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)

