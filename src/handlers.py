from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message


router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет {message.from_user.full_name}, я твой первый бот!"
    )

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        f"/start - приветстивие\n"
        "/help - список команд\n"
        "/about - о боте"
    )


@router.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer(
        f"Этот первый бот Нурса"       
    )

@router.message(F.text.lower() == "пока")
async def cmd_bye(message: Message):
    await message.answer(
        f"Пока, до следуюших встреч"
    )

@router.message()
async def echo(message: Message):
    await message.answer(
        f"Ты написал {message.text}"
 )