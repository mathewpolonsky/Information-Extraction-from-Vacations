import logging
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(dotenv_path=find_dotenv(), verbose=True)


logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv('API'))
dp = Dispatcher(bot, storage=MemoryStorage())


class GetFile(StatesGroup):
    file = State()


def predicit():
    pass


# Хэндлер на команду /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await GetFile.file.set()
    await message.answer("Отправьте csv файл для обработки")


@dp.message_handler(content_types=['document'], state=GetFile.file)
async def service_set_command(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    path = f'./static/csv_files/{file_id}.csv'
    destination_file = await bot.download_file(file.file_path, path)
    print(destination_file)
    new_file_path = 'static/csv_files/изображение.png' #сюда передаем путь до сгенирированного csv
    await message.reply_document(open(new_file_path, 'rb')) #


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())