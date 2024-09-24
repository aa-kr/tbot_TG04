from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Привет")],
   [KeyboardButton(text="Пока")]
], resize_keyboard=True)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Видео", url='https://ru.freepik.com/videos/kатегории/природа#from_element=videos_categories_block')],
    [InlineKeyboardButton(text="Музыка", url='https://rutube.ru/video/bbddaf4a0e5c12cffa691cca16873a8b/?r=plwd')],
    [InlineKeyboardButton(text="Новости", url='https://dzen.ru/news/')]
])

inline_keyboard_tact = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше", callback_data='news')]
])

test = ["Опция 1", "Опция 2"]

async def test_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in test:
       keyboard.add(InlineKeyboardButton(text=key, url='https://dzen.ru/news/'))
   return keyboard.adjust(2).as_markup()