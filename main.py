from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, ContentTypeFilter
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiogram.utils.markdown as fmt
import logging
import json
import requests
import keyboards as kb


bot_token = ''
bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

def getprice(currency):
    url = "https://api.binance.com/api/v3/ticker/price?symbol=" + currency
    data = requests.get(url).json()
    return data['price']


@dp.message_handler(commands='start')
async def welcome(message: types.Message):
    await message.answer("Hello! I'm your helper in crypto market. I can show you current cryptocurrency prices in real time\nPlease select a currency pair", reply_markup=kb.currencies())

@dp.callback_query_handler()
async def BTCUSDT(callback: types.CallbackQuery):
    await callback.message.answer(f'{callback.data} price is {getprice(callback.data)}')
    await callback.message.answer('You can select a new carrency pair', reply_markup=kb.currencies())
    await callback.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)