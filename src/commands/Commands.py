from typing import List

# dependencies
import telebot
from telebot import TeleBot

# static
import commands.commands_list as commands_list
import commands.replies_list as replies_list

# helpers
from users.User import User


class Commands:
    def __init__(self, bot: TeleBot, username: str):
        self.bot = bot
        self.bot_commands = commands_list.ALL_BOT_COMMANDS
        self.username = username

    # /start command
    def handle_start(self):
        command_name = "start"

        @self.bot.message_handler([command_name])
        def reply(message):

            # we got user's info (name, access etc)
            active_user = User(message)
            access_level = active_user.access
            print('access level is: ', access_level)

            # default settings is for 'partner' access
            reply_message = replies_list.PARTNER_BOT_REPLIES
            commands = commands_list.PARTNER_BOT_COMMANDS

            if access_level == 'student':
                print('загружаю настройки студента')
                reply_message = replies_list.STUDENT_BOT_REPLIES
                commands = commands_list.STUDENT_BOT_COMMANDS

            elif access_level == 'admin':
                print('загружаю настройки админа')
                reply_message = replies_list.ADMIN_BOT_REPLIES
                commands = commands_list.ALL_BOT_COMMANDS

            # set commands in burger menu
            self.bot.set_my_commands(commands=commands)
            print(f"new commands are set for {access_level} access level")

            # reply to user based on access level
            self.bot.reply_to(message, reply_message['start'])

            # notifies in terminal if command is handled
            self.notify_me_into_console(command=command_name)

    # /help
    def handle_help(self):
        command_name = 'help'

        @self.bot.message_handler(commands=[command_name])
        def send_help(message):
            help_message = "У бота есть команды: \n\n"
            for command in commands_list.ALL_BOT_COMMANDS:
                help_message += f"/{command.command} "
                help_message += f"{command.description}\n"

            help_message += replies_list.ADMIN_BOT_REPLIES['help']

            self.bot.reply_to(message, help_message)
            self.notify_me_into_console(command=command_name)

    # /setcommands
    def setCommands(self):
        command_name = "setcommands"

        @self.bot.message_handler(commands=[command_name])
        def set_bot_commands(message):
            self.bot.set_my_commands(commands=self.bot_commands)
            self.bot.reply_to(
                message, replies_list.ADMIN_BOT_REPLIES['setcommands']
            )
            self.notify_me_into_console(command=command_name)

    # console printing
    def notify_me_into_console(self, command):
        bot_username = self.username

        print(
            f"Бот @{bot_username} только что ответил на команду '/{command}'. Проверь чат"
        )
