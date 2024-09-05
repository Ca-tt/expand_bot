# dependencies
from telebot import TeleBot
from telebot.apihelper import ApiTelegramException
from time import sleep

# utils
from utils.Dotenv import Dotenv


class Bot:
    """class to connect and run bot"""

    def __init__(self):
        self.bot_token = Dotenv().bot_token
        self.admin_id = Dotenv().admin_id
        
        self.bot = None
        self.connect_to_bot()
         
        self.username = self.get_bot_data(bot=self.bot, requested_data="username")


    def connect_to_bot(self) -> TeleBot:
        try: 
            self.bot = TeleBot(self.bot_token)
            
        except ApiTelegramException as e:
            if e.error_code == 409:
                print("Бот уже где-то запущен... Ошибка 409")
                self.tell_admin("Бот запущен ёще-то (multiple instances), ошибка 409")
                
                self.bot.stop_bot()
                self.bot.infinity_polling(timeout=10, long_polling_timeout=5)
        
            else:
                print(f"Unexpected error occurred: {e}")
                self.tell_admin('Неизвестная ошибка при запуске бота (else)')
                self.bot.stop_bot()
                self.bot.infinity_polling(timeout=10, long_polling_timeout=5)
                
        except Exception as e:
            print(f"Error occurred: {e}")
            self.tell_admin('exception (not 409)')
            self.bot.stop_bot()
            self.bot.infinity_polling(timeout=10, long_polling_timeout=5)
        
            
        bot_name = self.get_bot_data(bot=self.bot, requested_data="first_name")

        if self.bot:
            print(f"Подключаюсь к боту '{bot_name}'...")
            print_separators()
            self.tell_admin("Начинаю работу...")


    def get_bot_data(self, bot: TeleBot, requested_data: str) -> str:
        """gets bot's name, @username etc"""
        
        all_bot_info = bot.get_me()

        desired_info = getattr(all_bot_info, requested_data)
        return desired_info
    
    def tell_admin(self, message):
        self.bot.send_message(chat_id=self.admin_id, text=message)
        

    # enable bot to listening for commands
    def run_bot(self) -> None:
        bot_username = self.get_bot_data(bot=self.bot, requested_data="username")

        print(f"Бот @{bot_username} подключён! Нажми /start для начала")
        print_separators() 
        
        try:
            self.bot.infinity_polling(timeout=10, long_polling_timeout=5)
            
        except ApiTelegramException as e:
            
            if e.error_code == 409:
                print("Бот уже где-то запущен... Ошибка 409")
                self.tell_admin("Бот запущен ёще-то (multiple instances), ошибка 409")
                
                self.bot.stop_bot()
                self.bot.infinity_polling(timeout=10, long_polling_timeout=5)
            
            else:
                print(f"Unexpected error occurred: {e}")
                self.tell_admin('Неизвестная ошибка при запуске бота (else)')
                self.bot.stop_bot()
                self.bot.infinity_polling(timeout=10, long_polling_timeout=5)
            
        except Exception as e:
            print(f"Error occurred: {e}")
            self.tell_admin('exception (not 409)')
            self.bot.stop_bot()
            self.bot.infinity_polling(timeout=10, long_polling_timeout=5)


def print_separators() -> None:
    print(f"\n {'='*10}")
