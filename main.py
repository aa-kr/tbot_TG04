import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
import random

from gtts import gTTS
import os

from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.callback_query(F.data == 'news')
async def news(callback: CallbackQuery):
   await callback.answer("Кнопка заменяется опциями", show_alert=True)
   await callback.message.edit_text('Опции подгружаются', reply_markup=await kb.test_keyboard())


@dp.message(F.text == "Привет")
async def test_button(message: Message):
   await message.answer(f'Привет, {message.from_user.first_name}')

@dp.message(F.text == "Пока")
async def test_button(message: Message):
   await message.answer(f'До свидания, {message.from_user.first_name}')


@dp.message(Command('dynamic'))
async def dynamic(message: Message):
   await message.answer('это кнопка',reply_markup=kb.inline_keyboard_tact)


@dp.message(Command('links'))
async def links(message: Message):
   await message.answer('это кнопки',reply_markup=kb.inline_keyboard_test)


@dp.message(Command('help'))
async def help(message: Message):
   await message.answer('Этот бот умеет выполнять команды: \n /start \n /help \n /minitraining')

@dp.message(CommandStart())
async def start(message: Message):
   await message.answer(f'Приветики, {message.from_user.first_name}', reply_markup=kb.main)


async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())
