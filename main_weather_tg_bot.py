import requests
import datetime
from config import tg_bot_token, open_weather_token 
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Hey, buddy. Write me the name of the city and I will send you an up-to-date weather report.")


if __name__ == '__main':
    executor.start_polling(dp)