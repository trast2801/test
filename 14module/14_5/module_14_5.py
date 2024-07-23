import asyncio
import os
import sqlite3

import crud_functions
import aiogram
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InputFile
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API =''
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup()
button_1 = KeyboardButton(text= 'Рассчитать')
button_3 = KeyboardButton(text= 'Купить')
button_2 = KeyboardButton(text= 'Информация')
button_4 = KeyboardButton(text= 'Регистрация')
#kb.add(button_1)
#kb.add(button_2)
kb.row(button_1, button_2)
kb.add(button_3)
kb.add(button_4)
kb.resize_keyboard=True

kb_inline = InlineKeyboardMarkup (
    inline_keyboard=[
                    [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
                    [InlineKeyboardButton(text='Формулы расчета', callback_data='formulas')]
    ], resize_keyboard = True
)

kb_inline_product = InlineKeyboardMarkup (
    inline_keyboard=[
                    [InlineKeyboardButton(text='Product1',callback_data ="product_buying")],
                    [InlineKeyboardButton(text='Product2',callback_data ="product_buying")],
                    [InlineKeyboardButton(text='Product3',callback_data ="product_buying")],
                    [InlineKeyboardButton(text='Product4',callback_data ="product_buying")]
    ], resize_keyboard = True
)

class  UserState(StatesGroup):
     age = State()
     growth =  State()
     weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()
@dp.message_handler(commands=['start'])
async  def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def  main_menu(message):
    await message.answer('Выберите опцию', reply_markup=kb_inline)

@dp.message_handler(text = 'Купить')
async def get_buying_list(message):
    records = crud_functions.get_all_products(cursor)
    if records == None:
        print("Для работы следует наполнить БД")
        flag = False
    else:
        for i in records:
            flag = True
            msg = f'Название: {i[0]} | Описание : {i[1]} | Цена {i[2]}'
            file_name = f'photo\\{i[3]}.jpg'
            if os.path.exists(file_name):
                await bot.send_photo(message.chat.id, photo=InputFile(file_name), caption=msg)

            else:
                print('Такого файла не существует')
                flag = False
                break
    if flag:
        await message.answer("Выберите продукт для покупки:", reply_markup=kb_inline_product)
    else:
        await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")

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

@dp.message_handler(text = 'Регистрация')
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state = RegistrationState.username)
async def set_username(message, state):

    if crud_functions.is_included(message.text, cursor):
        await message.answer("Пользователь существует, введите другое имя")
        await RegistrationState.username.set()
    else:
        await state.update_data(username = message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()

@dp.message_handler(state = RegistrationState.email)
async  def set_email(message, state):
    await state.update_data(email = message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state = RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age = message.text)
    data = await  state.get_data()
    crud_functions.add_user(data['username'],data['email'], data['age'], cursor)
    connection.commit()
    await state.finish()
    await message.answer('Регистрация завершена', reply_markup=kb)


if __name__=='__main__':

    try:
        connection = sqlite3.connect('data_base.db')
        cursor = connection.cursor()
        crud_functions.initiate_db(cursor)
        executor.start_polling(dp, skip_updates=True)
    except sqlite3.Error as err:
        print(err)
    finally:
        if connection:
            connection.close()
