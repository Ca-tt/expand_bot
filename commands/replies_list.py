SHARED_BOT_REPLIES = {
    'help': '\nЕсли есть вопросы или нашёл баг в боте, пиши мне в личку @best_prepod \n\nВыйти в меню: /menu',
}

PARTNER_BOT_REPLIES = {
    'start': 'Привет, партнёр по рекламе!\nЯ — бот-помощник Дамира. Рад познакомиться 🤝\n\nВведи своё имя, чтобы начать работу👇',
}

STUDENT_BOT_REPLIES = {
    'start': 'Привет!\nЯ — бот-помощник Дамира. Рад познакомиться 🤝\n\nВведи своё имя, чтобы начать работу👇',
}

ADMIN_BOT_REPLIES = {
    'start': 'Привет, Дамир! Готов начать работу?',
    'setcommands': "Команды обновлены! Перезапусти бота, чтобы проверить изменения",
}

# merge objects
PARTNER_BOT_REPLIES.update(SHARED_BOT_REPLIES)
STUDENT_BOT_REPLIES.update(SHARED_BOT_REPLIES)
ADMIN_BOT_REPLIES.update(SHARED_BOT_REPLIES)
