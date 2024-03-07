import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram import types

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def echo_message(message: types.Message):
    """В параметры попадает принимаемое сообщение"""
    await message.answer(text=message.text)  # Ответить тем же сообщением


async def main():
    await dp.start_polling(bot)  # Тут можно передавать несколько ботов


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
