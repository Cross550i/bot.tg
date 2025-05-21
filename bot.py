import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config_reader import config

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()

# Кнопка и клавиатура
button1 = InlineKeyboardButton(text="Напиши один", callback_data="button_click")
button2 = InlineKeyboardButton(text="Напиши два", callback_data="button2_click")
button3 = InlineKeyboardButton(text="Напиши три", callback_data="button3_click")
button4 = InlineKeyboardButton(text="Напиши четыре", callback_data="button4_click")
keyboard = InlineKeyboardMarkup(inline_keyboard=[[button1,button2],[button3,button4]])


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Выбери что нибудь \n два три ", reply_markup=keyboard)

# Хэндлер на команду /go
@dp.message(Command("go"))
async def cmd_start(message: types.Message):
    await message.answer("GO!", reply_markup=keyboard)

# Хэндлер на нажатие кнопки 1
@dp.callback_query(F.data == "button_click")
async def button(callback: types.CallbackQuery):
    await callback.message.answer("😂")

# Хэндлер на нажатие кнопки 2
@dp.callback_query(F.data == "button2_click")
async def button2(callback: types.CallbackQuery):
    await callback.message.answer("Два")

# Хэндлер на нажатие кнопки 3
@dp.callback_query(F.data == "button3_click")
async def button3(callback: types.CallbackQuery):
    await callback.message.answer("Три")

# Хэндлер на нажатие кнопки 4
@dp.callback_query(F.data == "button4_click")
async def button4(callback: types.CallbackQuery):
    await callback.message.answer("Четыре")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


