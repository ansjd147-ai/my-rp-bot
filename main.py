import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiohttp import web

# Твой токен
TOKEN = "8442272768:AAH7oiEHrdWXNzaYlkHhXsDmUtWWL2M4onQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("✅ ЖИВОЙ! Бот успешно пробился через Render!")

# Микро-сервер для "обмана" Render
async def handle(request):
    return web.Response(text="Bot is running!")

async def main():
    # Создаем веб-сервер, чтобы Render не закрывал приложение
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    
    # Render сам подставит нужный порт, если нет - берем 10000
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    asyncio.create_task(site.start())

    print(f"Сервер запущен на порту {port}. Запуск бота...")
    
    # Запуск бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
