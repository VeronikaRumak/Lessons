from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
import asyncio
from crud_functions import get_all_products

print()     # Отступ


bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
# С текстом 'Рассчитать норму калорий' и callback_data='calories'
# С текстом 'Формулы расчёта' и callback_data='formulas'
inline_kb = InlineKeyboardMarkup(row_width=2)
inline_button_calculate = InlineKeyboardButton(text='Рассчитать норму калорий',
                                               callback_data='calories')
inline_button_formulas = InlineKeyboardButton(text='Формулы расчёта',
                                              callback_data='formulas')
inline_kb.add(inline_button_calculate, inline_button_formulas)

# Создайте клавиатуру ReplyKeyboardMarkup с 3 кнопками KeyboardButton:
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_info = KeyboardButton(text='Информация')
button_calculate = KeyboardButton(text='Рассчитать')
button_buy = KeyboardButton(text='Купить')
kb.add(button_info)
kb.add(button_calculate)
kb.add(button_buy)

# Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4"
inline_kb_products = InlineKeyboardMarkup(row_width=2)
for i in range(1, 5):
    inline_kb_products.add(InlineKeyboardButton(text=f'Товар {i}',
                                                callback_data='product_buying'))


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Создайте новую функцию main_menu(message), которая:
# Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
# Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb)


# Создайте новую функцию get_formulas(call), которая:
# Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
# Будет присылать сообщение с формулой Миффлина-Сан Жеора.
@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина-Сан Жеора:\n'
                              'Для мужчин: 10 * вес + 6.25 * рост - 5 * возраст + 5\n'
                              'Для женщин: 10 * вес + 6.25 * рост - 5 * возраст - 161')


# Измените функцию set_age и декоратор для неё:
# Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
# Теперь функция принимает не message, а call.
# Доступ к сообщению будет следующим - call.message.
@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
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


# Создайте новую функцию get_buying_list(message), которая:
# Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Купить'.
@dp.message_handler(text='Купить')
# Сама функция будет выводить надписи 'Название: Product<number>
# | Описание: описание <number> | Цена: <number * 100>' 4 раза.
async def get_buying_list(message):
    products = get_all_products()
    for product in products:
        product_name = product[0]
        product_description = product[1]
        product_price = product[2]
        await message.answer(f'Название: {product_name} | '
                             f'Описание: {product_description} | '
                             f'Цена: {product_price}')
        # После каждой надписи выводите картинки к продуктам.
        path = f'Images/Мяч_{i}.jpg'
        with open(path, 'rb') as img:
            await message.answer_photo(img)

    # В конце выведите ранее созданное Inline меню с надписью
    # "Выберите продукт для покупки:".
    await message.answer('Выберите товар для покупки:', reply_markup=inline_kb_products)


# Создайте новую функцию send_confirm_message(call), которая:
# Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'product_buying'.
# Будет присылать сообщение "Вы успешно приобрели продукт!"
@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели мяч!')


# Используйте ранее созданную клавиатуру в ответе функции start,
# используя параметр reply_markup.
@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью и продающий товары.',
                         reply_markup=kb)


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
