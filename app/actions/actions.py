from aiogram import Router, F
import json
from aiogram.filters import Command
from os import getenv
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section
)
from app.actions.json import list_household_chores

# все взаимодействие с ботом опизывается тут
# TODO: в будующем возможн опонадобиться деление на логические модули
# -------------------------------------------------------------------

router = Router(name='global')

load_dotenv(find_dotenv())
TOKEN = getenv("BOT_TOKEN")

# экземпляры бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# клавиатура
kb = [
        [KeyboardButton(text="Список дел")],
        [KeyboardButton(text="Обмен")]
    ]
keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# клавиатура при старте чата
@router.message(Command('start'))
async def start_chat(message: Message, users: list[int]):
    await message.answer('Привет!')
    await message.answer('Идёт процесс аунтефикации...')
    existing_user = any(message.from_user.id == usr_id for usr_id in users)

    if (existing_user):
        await message.answer('Вы вошли в ситсему', reply_markup=keyboard)
    else:
        await message.answer('Это бот создавался не для тебя разбийник')

# получение списка дел при клике на кнопку "Список дел"
@router.message(F.text == 'Список дел')
async def show_list(message: Message):
    list_names = '\n''- '.join([item['name'] for item in list_household_chores])
    content = as_list(
        as_marked_section(
            Bold("Список дел:"),
            list_names,
        ),
    )
    await message.answer(**content.as_kwargs())