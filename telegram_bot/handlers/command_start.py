from telegram_bot.bot import TelegramBot
from telegram_bot.keybords import kb_start

class Handler():
    def __init__(self, bot_instance: TelegramBot) -> None:
        def command_start(message):
            chat_id = message.from_user.id

            bot_instance.bot.send_message(chat_id, "Hello World", reply_markup=kb_start())

        bot_instance.add_command_handler(
            commands=["start"],
            callback=command_start
        )
