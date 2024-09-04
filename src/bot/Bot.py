# dependencies
import telebot

# utils
from utils.Dotenv import Dotenv


class Bot:
    """class to connect and run bot"""

    def __init__(self):
        self.bot_token = Dotenv("BOT_TOKEN").load_env_data()
        self.bot = self.connect_to_bot(bot_token=self.bot_token) 
        self.username = self.get_bot_data(bot=self.bot, requested_data="username")

    # connect to bot
    def connect_to_bot(self, bot_token: str) -> telebot.TeleBot:
        bot = telebot.TeleBot(bot_token)
        bot_name = self.get_bot_data(bot=bot, requested_data="first_name")

        if bot:
            print(f"Подключаюсь к боту '{bot_name}'...")
            print_separators()

        return bot
    
    # get bot's name, @username etc
    def get_bot_data(self, bot: telebot.TeleBot, requested_data: str) -> str:
        all_bot_info = bot.get_me()

        desired_info = getattr(all_bot_info, requested_data)
        return desired_info

    # enable bot to listening for commands
    def run_bot(self) -> None:
        bot_username = self.get_bot_data(bot=self.bot, requested_data="username")

        print(f"Бот @{bot_username} подключён! Нажми /start для начала")
        print_separators() 

        # terminate previous instance
        # if self.bot.polling():
        #     self.bot.stop_polling()

        self.bot.polling()


def print_separators() -> None:
    print(f"\n {'='*10}")

# class end
