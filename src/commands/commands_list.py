# dependencies
import telebot


COMMON_BOT_COMMANDS = [
    telebot.types.BotCommand("start", "Запустить бота"),
    telebot.types.BotCommand("menu", "Выйти в меню"),
    telebot.types.BotCommand("referal", "1000 гривен за друга"),
    telebot.types.BotCommand("help", "Если что-то пошло не так"),
]

PARTNER_BOT_COMMANDS = COMMON_BOT_COMMANDS



STUDENT_BOT_COMMANDS = COMMON_BOT_COMMANDS + [
    telebot.types.BotCommand("homework", "Напомнить домашку"),
    telebot.types.BotCommand("schedule", "Когда следующий урок?"),
    telebot.types.BotCommand("progress", "Записать / посмотреть прогресс"),
    telebot.types.BotCommand("payment", "Узнать остаток уроков"),
]

ADMIN_BOT_COMMANDS = [
    telebot.types.BotCommand("settings", "Профиль и настройки"),
    telebot.types.BotCommand("setcommands", "Обновить команды бота"),
]


ALL_BOT_COMMANDS = COMMON_BOT_COMMANDS + PARTNER_BOT_COMMANDS + \
    STUDENT_BOT_COMMANDS + ADMIN_BOT_COMMANDS