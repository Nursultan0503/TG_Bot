from aiogram.types import (ReplyKeyboardMarkup,
                            KeyboardButton,
                            InlineKeyboardButton,
                            InlineKeyboardMarkup)

replay_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Python")],
    [KeyboardButton(text="Java")],
    [KeyboardButton(text="JavaScript")]
])



inline_keyboard = InlineKeyboardMarkup(inline_keyboard=(
    [InlineKeyboardButton(text="Документация Python", url="https://en.wikipedia.org/wiki/Python_(programming_language)")],
    [InlineKeyboardButton(text="Документация JS", url="https://en.wikipedia.org/wiki/Java_(programming_language)")],
    [InlineKeyboardButton(text="Документация Java", url="https://en.wikipedia.org/wiki/JavaScript")]
    
))