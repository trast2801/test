
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API ='7354419811:AAEk3KUNZVBZTXqT3mGGq5OKCnS79XkrFeI'
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async  def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler(content_types='text')
async def all_massages(message):
    print( 'Введите команду /start, чтобы начать общение.')



if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)