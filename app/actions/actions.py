from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

# все взаимодействие с ботом опизывается тут
# TODO: в будующем возможн опонадобиться деление на логические модули
# -------------------------------------------------------------------

router = Router(name='global')

@router.message(CommandStart())
async def start_chat(message: Message):
    await message.answer('Hi')

