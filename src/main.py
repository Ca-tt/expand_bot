from bot.Bot import Bot
from commands.Commands import Commands


def main():
    expand_bot = Bot()
    
    commands = Commands(expand_bot.bot, expand_bot.username)
 
    commands.handle_start() 
    commands.handle_help() 
    commands.setCommands()

    expand_bot.run_bot()



if __name__ == "__main__":
    main()

