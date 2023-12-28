from typing import List

# dependencies
import telebot
from telebot import TeleBot

# helpers
from users.User import User

BOT_COMMANDS: List[telebot.types.BotCommand] = [
    telebot.types.BotCommand("start", "Запустить бота"),
    telebot.types.BotCommand("menu", "Выйти в меню"),
    telebot.types.BotCommand("referal", "500 гривен за друга"),
    telebot.types.BotCommand("homework", "Напомнить домашку"),
    telebot.types.BotCommand("schedule", "Когда следующий урок?"),
    telebot.types.BotCommand("progress", "Записать / посмотреть прогресс"),
    telebot.types.BotCommand("payment", "Узнать остаток уроков"),
    telebot.types.BotCommand("help", "Если что-то пошло не так"),
    telebot.types.BotCommand("settings", "Профиль и настройки"),
    telebot.types.BotCommand("setcommands", "Обновить команды бота"),
]

BOT_REPLIES = {
    'start': 'Привет!\nЯ — бот-помощник Дамира. Рад познакомиться 🤝\n\nВведи своё имя, чтобы начать работу👇',
    'help': '\nЕсли есть вопросы или нашёл баг в боте, пиши мне в личку @best_prepod \n\nВыйти в меню: /menu',
    'setcommands': "Команды обновлены! Перезапусти бота, чтобы проверить изменения",
}


class Commands:
    def __init__(self, bot: TeleBot, username: str):
        self.bot = bot
        self.bot_commands = BOT_COMMANDS
        self.username = username

    # /start
    def handle_start(self):
        command_name = "start"

        @self.bot.message_handler([command_name])
        def reply(message):

            # set user information
            active_user = User(message)

            # reply to user
            self.bot.reply_to(message, BOT_REPLIES['start'])

            # prints if command is handled
            self.notify_me_into_console(command=command_name)

    # /help
    def handle_help(self):
        command_name = 'help'

        @self.bot.message_handler(commands=[command_name])
        def send_help(message):
            help_message = "У бота есть команды: \n\n"
            for command in BOT_COMMANDS:
                help_message += f"/{command.command} "
                help_message += f"{command.description}\n"

            help_message += BOT_REPLIES['help']

            self.bot.reply_to(message, help_message)
            self.notify_me_into_console(command=command_name)

    # /setcommands
    def setCommands(self):
        command_name = "setcommands"

        @self.bot.message_handler(commands=[command_name])
        def set_bot_commands(message):
            self.bot.set_my_commands(commands=self.bot_commands)
            self.bot.reply_to(
                message, BOT_REPLIES['setcommands']
            )
            self.notify_me_into_console(command=command_name)

    # console printing
    def notify_me_into_console(self, command):
        bot_username = self.username

        print(
            f"Бот @{bot_username} только что ответил на команду '/{command}'. Проверь чат"
        )
