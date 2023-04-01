from aiogram import types

def currencies():
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(types.InlineKeyboardButton(text="BTCUSDT", callback_data="BTCUSDT"),
                 types.InlineKeyboardButton(text="DOGEUSDT", callback_data="DOGEUSDT"),
                 types.InlineKeyboardButton(text="LTCUSDT", callback_data="LTCUSDT"),
                 types.InlineKeyboardButton(text="ETHUSDT", callback_data="ETHUSDT"),
                 types.InlineKeyboardButton(text="BNBUSDT", callback_data="BNBUSDT"),
                 types.InlineKeyboardButton(text="XRPUSDT", callback_data="XRPUSDT"),
                 types.InlineKeyboardButton(text="ADAUSDT", callback_data="ADAUSDT"),
                 types.InlineKeyboardButton(text="SOLUSDT", callback_data="SOLUSDT"),
                 types.InlineKeyboardButton(text="TRXUSDT", callback_data="TRXUSDT"))
    return keyboard