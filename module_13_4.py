from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

import asyncio


print()     # Отступ



bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# Группа состояний:
# Импортируйте классы State и StateGroup из aiogram.dispatcher.filters.state.

# Создайте класс UserState наследованный от StateGroup.
class UserState(StatesGroup):
    # Внутри этого класса опишите 3 объекта класса State: age, growth, weight
    # (возраст, рост, вес).
    age = State()
    growth = State()
    weight = State()

# Эта группа(класс) будет использоваться в цепочке вызовов message_handler'ов.


# Напишите следующие функции для обработки состояний:

# Функцию set_age(message):
# Оберните её в message_handler, который реагирует на текстовое сообщение 'Calories'.
@dp.message_handler(text='Calories')
async def set_age(message):

    # Эта функция должна выводить в Telegram-бот сообщение 'Введите свой возраст:'.
    await message.answer('Введите свой возраст: ')

    # После ожидать ввода возраста в атрибут UserState.age при помощи метода set.
    await UserState.age.set()


# Функцию set_growth(message, state):
# Оберните её в message_handler, который реагирует на переданное состояние UserState.age.
@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    # Эта функция должна обновлять данные в состоянии age на message.text
    # (написанное пользователем сообщение). Используйте метод update_data.
    await state.update_data(age=message.text)

    # Далее должна выводить в Telegram-бот сообщение 'Введите свой рост:'.
    await message.answer('Введите свой рост: ')

    # После ожидать ввода роста в атрибут UserState.growth при помощи метода set.
    await UserState.growth.set()


# Функцию set_weight(message, state):
# Оберните её в message_handler,
# который реагирует на переданное состояние UserState.growth.
@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    # Эта функция должна обновлять данные в состоянии age на message.text
    # (написанное пользователем сообщение). Используйте метод update_data.
    await state.update_data(growth=message.text)

    # Далее должна выводить в Telegram-бот сообщение 'Введите свой вес:'.
    await message.answer('Введите свой вес: ')
    # После ожидать ввода роста в атрибут UserState.weight при помощи метода set.
    await UserState.weight.set()


# Функцию send_calories(message, state):
# Оберните её в message_handler,
# который реагирует на переданное состояние UserState.weight.
@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)

    # Далее в функции запомните в переменную data все ранее введённые состояния
    # при помощи state.get_data().
    data = await state.get_data()

    age = float(data['age'])
    growth = float(data['growth'])
    weight = float(data['weight'])

    # Используйте упрощённую формулу Миффлина - Сан Жеора для подсчёта нормы калорий
    # (для женщин или мужчин - на ваше усмотрение).

    # для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;
    # для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.

    # Данные для формулы берите из ранее объявленной переменной data
    # по ключам age, growth и weight соответственно.
    # Результат вычисления по формуле отправьте ответом пользователю в Telegram-бот.

    man = 10 * weight + 6.25 * growth - 5 * age + 5
    woman = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Норма калорий для мужчин: {man}")
    await message.answer(f"Норма калорий для женщин: {woman}")

    # Финишируйте машину состояний методом finish().
    await state.finish()


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)





