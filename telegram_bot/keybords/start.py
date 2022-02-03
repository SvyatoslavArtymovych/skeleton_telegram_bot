from telebot.types import ReplyKeyboardMarkup

def start():
    kb = ReplyKeyboardMarkup(True)
    kb.row("/start")

    return kb
