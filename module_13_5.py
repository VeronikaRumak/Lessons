from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import asyncio


print()     # Отступ



bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton
# на ней со следующим текстом: 'Рассчитать' и 'Информация'.

# Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства
# при помощи параметра resize_keyboard.
kb = ReplyKeyboardMarkup(resize_keyboard=True)

button_info = KeyboardButton(text='Информация')
button_calculate = KeyboardButton(text='Рассчитать')

kb.add(button_info)
kb.add(button_calculate)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Измените massage_handler для функции set_age.
# Теперь этот хэндлер будет реагировать на текст 'Рассчитать', а не на 'Calories'.
@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст: ')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)

    data = await state.get_data()
    age = float(data['age'])
    growth = float(data['growth'])
    weight = float(data['weight'])

    man = 10 * weight + 6.25 * growth - 5 * age + 5
    woman = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f"Норма калорий для мужчин: {man}")
    await message.answer(f"Норма калорий для женщин: {woman}")

    await state.finish()


# Используйте ранее созданную клавиатуру в ответе функции start,
# используя параметр reply_markup.
@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)





