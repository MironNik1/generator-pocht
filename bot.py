import os
from aiogram import Bot as AioBot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, FSInputFile
from aiogram.filters import CommandStart, Command
from main import generate_email
import logging

admin_id = 1134469599

bot = AioBot(token='7152583569:AAE_UjgoZyhBkh0mNVwzf_KgchcthQRLThM')
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

@dp.message(CommandStart())
async def start(message: Message):
    if message.from_user.id == admin_id:
        await message.reply('Привет, админ!, /generate команда для генерации')
    else:
        await message.reply('У вас нет доступа')

@dp.message(Command('generate'))
async def generate(message: Message):
    kb = [
        [KeyboardButton(text='50'), KeyboardButton(text='250'), KeyboardButton(text='500')]
    ]
    kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kb)
    if message.from_user.id == admin_id:
        await message.reply('Выберите количество почт:', reply_markup=kb)
    else:
        await message.reply('У вас нет доступа')

@dp.message(lambda message: message.text in ['50', '250', '500'])
async def process_generate(message: Message):
    if message.from_user.id == admin_id:
        count = int(message.text)
        for _ in range(1, count + 1):
            email = generate_email()
            with open('emails.txt', 'a') as f:
                f.write(f'{email}\n')
        await message.reply('Почты сгенерированы')
        
        # Отправка файла
        with open('emails.txt', 'rb') as f:
            await message.reply_document(FSInputFile('emails.txt'), caption='emails.txt')
        
        # Удаление файла
        os.remove('emails.txt')
    else:
        await message.reply('У вас нет доступа')

async def main():
    # Запуск бота и прослушивание сообщений
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())