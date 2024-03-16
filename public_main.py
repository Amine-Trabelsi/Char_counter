import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


Tok = "SECRET_TOKEN_HERE"
TOKEN = getenv(Tok)

# All handlers should be attached to the Dispatcher
dp = Dispatcher()


@dp.message()
async def count_handler(message: Message) -> None:
    """
    This handler is triggered for all messages

    It analyzes the message text and responds with character and vowel count.
    """
    text = message.text
    
    # Count total characters
    total_symbols = len(text)

    # Count vowels (lowercase for case-insensitivity)
    vowels = 'аеёиоуыэюя'
    vowel_count = 0
    for char in text.lower():
        if char in vowels:
            vowel_count += 1

    # Respond with the results
    await message.answer(f"Общее количество символов: {total_symbols}\nКоличество гласных букв: {vowel_count}")


async def main() -> None:
    # Initialize Bot instance
    bot = Bot(Tok)
    # Run event polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())