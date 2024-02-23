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
        text='Click!', web_app=WebAppInfo(
            url=os.environ.get('WEB_APP_URL')
        )
    )
    return builder.as_markup()


@router.message(CommandStart())
async def start(message: Message):
    await message.reply(
        "Hello! Press to start ->",
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
