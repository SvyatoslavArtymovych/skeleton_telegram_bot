from typing import List

from telebot import TeleBot

from config import config

class TelegramBot:
    def __init__(self) -> None:
        self.bot = TeleBot(config.BOT_TOKEN)
        self.bot.parse_mode = "html"

    def start_bot(self):
        self.bot.infinity_polling()

    def add_command_handler(self, commands: List[str], callback):
        self.bot.register_message_handler(
            callback=callback,
            commands=commands
        )

    def add_content_type_handler(self, content_types: List[str], callback):
        self.bot.register_message_handler(
            callback=callback,
            content_types=content_types,
        )

    def add_state_handler(self, state: str, callback):
        self.bot.register_message_handler(
            callback=callback,
            state=state,
        )
