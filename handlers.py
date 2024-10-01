from aiogram import F, types, Router
from aiogram.types import Message, ReplyKeyboardMarkup
from aiogram.filters import Command
from bs4 import BeautifulSoup
# TODO: сделать новый проект и установить все зависимости
# TODO: :) <3


import time

# markup = ReplyKeyboardMarkup(resize_keyboard=True)
# markup.row('Test')
# req = requests.get(url, headers=header)
# soup = BeautifulSoup(req.text, "html.parser")
# return site(name_site, soup, url)


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    # while True:
    # TODO: вечный цикл с поиском информации
    await msg.answer("Дарова WW")
        # await time.sleep(2)


@router.message(Command("set_rss"))
async def set_rss(msg: Message):
    await msg.answer("New RSS!")
    new_rss = msg


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Айдишник —> {msg.from_user.id}")
