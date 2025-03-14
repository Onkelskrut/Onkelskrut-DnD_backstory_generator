from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from database.database import DICT_STORIES_RU
from keyboards.keyboards import keyboard
from random import choice


router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=DICT_STORIES_RU['/start'], reply_markup=keyboard)


@router.message(Command(commands='/help'))
async def process_help_command(message: Message):
    await message.answer(text=DICT_STORIES_RU['/help'], reply_markup=keyboard)


@router.message()
async def process_generate_backstory(message: Message):
    await message.answer(text=f'Сегодня ты {choice(DICT_STORIES_RU['character_traits']).lower()} {choice(DICT_STORIES_RU['race_list'])} - {choice(DICT_STORIES_RU['profession_list'])}, {choice(DICT_STORIES_RU['appearance_features'])}, {choice(DICT_STORIES_RU['features'])}. {choice(DICT_STORIES_RU['pre_histories'])}, {choice(DICT_STORIES_RU['motivation'])}. Среди твоих страхов {choice(DICT_STORIES_RU['phobias'])}, но будь отважен и ты сможешь все преодолеть! Вперед! К приключениям!!!')

