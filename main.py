import asyncio
from os import getenv
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv
from app.actions.actions import router

#токен

load_dotenv(find_dotenv())
TOKEN = getenv("BOT_TOKEN")

# экземпляры бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()



async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped!')