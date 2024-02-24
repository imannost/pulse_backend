import asyncio
import logging
import sys
import os

from aiogram import Router, Bot, Dispatcher
from aiogram.types import Message, WebAppInfo, InlineKeyboardMarkup
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


def webapp_builder() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text='donorsearch.org', web_app=WebAppInfo(
            url=os.environ.get('WEB_APP_URL')
        )
    )
    return builder.as_markup()


@router.message(CommandStart())
async def start(message: Message):
    await message.reply(
        """Привет! Я бот, который поможет вам стать донором. Напишите /donor для получения информации о том, как стать донором.\n
        Как стать донором: \n
            1. Посетите веб-сайт donorsearch.org \n
            2. Найдите раздел "Как стать донором" на главной странице \n
            3. Ознакомьтесь с информацией о процессе становления донором на сайте \n
            4. Получите подтверждение о вашем донорстве и начните делать доброе дело! \n
        """,
        reply_markup=webapp_builder())


async def main():
    token = os.environ.get('TOKEN')
    bot = Bot(token)

    dp = Dispatcher()
    dp.include_router(router=router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
