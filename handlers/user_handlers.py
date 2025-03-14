from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from database.database import DICT_STORIES_RU
from keyboards.keyboards import keyboard
from services.services import generate_story


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=DICT_STORIES_RU['/start'], reply_markup=keyboard)


@router.message(Command(commands='/help'))
async def process_help_command(message: Message):
    await message.answer(text=DICT_STORIES_RU['/help'], reply_markup=keyboard)


@router.message()
async def process_generate_backstory(message: Message):
    await message.answer(text=generate_story())

