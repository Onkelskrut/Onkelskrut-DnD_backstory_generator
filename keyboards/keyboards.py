from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from database.database import DICT_STORIES_RU


button = KeyboardButton(text=DICT_STORIES_RU['button_pers_generate'])

keyboard = ReplyKeyboardMarkup(
    keyboard=[[button]],
    resize_keyboard=True
)

