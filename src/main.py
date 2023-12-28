# bot
from bot.Bot import Bot
from commands.Commands import Commands

def main():
    # invoke and launch bot
    expand_bot = Bot()
    
    commands = Commands(expand_bot.bot, expand_bot.username)
 
    # listen to each command
    commands.handle_start() 
    commands.handle_help() 
    commands.setCommands()

    # run bot     
    expand_bot.run_bot()



if __name__ == "__main__":
    main()
