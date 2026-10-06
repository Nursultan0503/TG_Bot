from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from src.keyborads import replay_keyboard, inline_keyboard

router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет {message.from_user.full_name}, я твой первый бот!",
        reply_markup=replay_keyboard
    )

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        f"/start - приветстивие\n"
        "/help - список команд\n"
        "/about - о боте",
        "/docs - официальная документация"

    )


@router.message(F.text == "Python")
async def cmd_bye(message: Message):
    await message.answer(
        f"Python: Отличный и понятный язык, который стал стандартом для ИИ и бэкенда."
    )

@router.message(F.text == "Java")
async def cmd_bye(message: Message):
    await message.answer(
        f"Java: Строгий и очень надежный язык, идеален для крупных корпоративных систем."
    )

@router.message(F.text == "JavaScript")
async def cmd_bye(message: Message):
    await message.answer(
        f"JavaScript: Главный язык для веба, именно он делает все сайты интерактивными и живыми."
    )

@router.message(Command('docs'))
async def cmd_docs(message: Message):
    await message.answer(
        f"Выбери язык, чтобы перейти к официальной документации",
        reply_markup=inline_keyboard         
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