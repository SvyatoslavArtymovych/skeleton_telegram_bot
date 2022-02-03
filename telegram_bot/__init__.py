from .bot import TelegramBot
from .handlers import CommandStartHandler


bot = TelegramBot()

# add handlers
CommandStartHandler(bot)


bot.start_bot()
