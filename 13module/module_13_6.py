import asyncio

import aiogram
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API =''
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup()
button_1 = KeyboardButton(text= 'Рассчитать')
button_2 = KeyboardButton(text= 'Информация')
#kb.add(button_1)
#kb.add(button_2)
kb.row(button_1, button_2)
kb.resize_keyboard=True

kb_inline = InlineKeyboardMarkup (
    inline_keyboard=[
                    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
                    [InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')]
    ], resize_keyboard = True
)

class  UserState(StatesGroup):
     age = State()
     growth =  State()
     weight = State()

@dp.message_handler(commands=['start'])
async  def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def  main_menu(message):
    await message.answer('Выберите опцию', reply_markup=kb_inline)

@dp.callback_query_handler(text='calories')
async def all_massages(call):
    await call.message.answer('введите свой возраст')
    await UserState.age.set()

@dp.callback_query_handler(text='formulas')
async  def get_formulas(call):
    msg = (' Упрощенный вариант формулы Миффлина-Сан Жеора:\n'
           ' для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n '
           ' для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.\n')
    await call.message.answer(msg)


@dp.message_handler(text='Рассчитать')
async def  main_menu(message):
    pass
@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('введите свой рост')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data (growth = message.text)
    await  message.answer ('Введите свой вес')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):

    await state.update_data(weight = message.text)
    data = await  state.get_data()

    callor_men = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    callor_women = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161
    msg = (f' Ваша норма каллорий (муж) = {callor_men}\n'
           f' Ваша норма каллорий (жен) = {callor_women}')

    await message.answer(msg)
    # 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.


if __name__=='__main__':

    executor.start_polling(dp, skip_updates=True)