# Telegram Bot

# Подключение необходимых модулей (библиотек) - - - - - - - - - -
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton # Модули для формирования клавиатуры

# - - - - - - - Объявление констант - - - - - - - - - - -
TOKEN = " " # 
bot = Bot (token=TOKEN)
dp = Dispatcher()

class ButtonNext:
    HELLO = "Строка приветствия"
    GET_HELP = "Получение помощи о программе"
    HANDS = "Средства для прокачки рук"
    LEGS = "Средства для прокачки ног"

# - - - Объявление функций - - - - - - - - - - - - - - -
def get_on_start_kb(): # Функция для формирования клавиатуры
    # - - - Функция для формерования первого ряда кнопок
    button_hello = KeyboardButton(text=ButtonNext.HELLO) # Объявление кнопки приветствия
    button_help = KeyboardButton(text=ButtonNext.GET_HELP) # Объявление кнопки
    # Функция для формерования второго ряда кнопок
    button_hands = KeyboardButton(text=ButtonNext.HANDS) # Объявление кнопки
    button_legs =KeyboardButton(text=ButtonNext.LEGS) # Объявление кнопки
    # - - - - - - Собственно создание клавиатуры
    button_first_row = [button_hello, button_help] # Создание массива кнопок
    button_second_row = [button_hands, button_legs] # Создание массива кнопок
    markup = ReplyKeyboardMarkup (keyboard=[button_first_row, button_second_row]) # Создание клавиатуры
    return markup


# - - - - - Объявление ассинхронных функций - - - - - - - - - - - -
@dp.message (CommandStart())
async def handle_start(message: types.Message):
    #button_hello = KeyboardButton(text="Строка приветствия") # Объявление кнопки приветствия
    #button_help = KeyboardButton(text="Получение помощи о программе") # Объявление кнопки
    #button_row = [button_hello, button_help] # Создание массива кнопок
    #markup = ReplyKeyboardMarkup (keyboard=[button_row]) # Разметка клаваитуры
    await message.answer(text=f"Программа начала свою работу,{message.from_user.full_name} !!!!! \n Как дела?",
                         parse_mode=ParseMode.HTML,
                         reply_markup=get_on_start_kb())

@dp.message (F.text == ButtonNext.GET_HELP)
@dp.message (Command("help"))
async def handle_help(message:types.Message):
    text="Я просто Эхо-Бот и я ничего еще не умею!!!!"
    await message.answer(text=text)

@dp.message(Command("buy"))
async def handle_buy(message: types.Message):
    text = "Товар куплен!!!! Спасибо за Вам за покупку. \n Мы ждем Вас снова в нашей компании!"
    await message.answer(text=text)


@dp.message(Command("price"))
async def handle_price(message: types.Message):
    text = "Стоимость товара: 10р"
    await message.answer(text=text)


@dp.message(Command("info"))
async def handle_info(message: types.Message):
    text = "Информация о товаре: товар явялется новым, доставка осуществляется в течении нескольких дней"
    await message.answer(text=text)

@dp.message(Command("quont"))
async def handle_quont(message: types.Message):
    text = "Колличество товара: 4"
    await message.answer(text=text)

@dp.message()
async def echo_message(message: types.Message):
  #  await message.answer(text="Wait a second...")
 #   await message.answer(text="Внимание мошенники!...")
    await bot.send_message(chat_id=message.chat.id,
                         text="Start processing...")
#    await bot.send_message(chat_id=message.chat.id, text="Deleted message...", reply_to_message_id=message.message_id)
    await message.answer(text=message.text)
    await message.reply(text=message.text)
    try:
      await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Something new...")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling (bot)

if (__name__ == "__main__"):
    asyncio.run (main())
