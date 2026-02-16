import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# token 
TOKEN = "8442272768:AAH7oiEHrdWXNzaYlkHhXsDmUtWWL2M4onQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("✅ ПОБЕДА! Бот запущен на Render и готов к РП!")

async def main():
    print("Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
