from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
import asyncio
from crud_functions import get_all_products, add_user, is_included

print()     # Отступ


bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


calories_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий',
                              callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта',
                              callback_data='formulas')]
    ]
)

inline_kb_products = InlineKeyboardMarkup(row_width=2)
for i in range(1, 5):
    inline_kb_products.add(InlineKeyboardButton(text=f'Товар {i}',
                                                callback_data='product_buying'))

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_info = KeyboardButton(text='Информация')
button_registration = KeyboardButton(text='Регистрация')
kb.add(button_info, button_registration)

kb_after_registration = ReplyKeyboardMarkup(resize_keyboard=True)
button_info = KeyboardButton(text='Информация')
button_buy = KeyboardButton(text='Купить')
button_calories = KeyboardButton(text='Рассчитать')
button_exit = KeyboardButton(text='Выйти')
kb_after_registration.add(button_info, button_buy, button_calories, button_exit)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=calories_kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина-Сан Жеора:\n'
                              'Для мужчин: 10 * вес + 6.25 * рост - 5 * возраст + 5\n'
                              'Для женщин: 10 * вес + 6.25 * рост - 5 * возраст - 161')


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


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    i = 0
    for product in products:
        product_name = product[0]
        product_description = product[1]
        product_price = product[2]
        await message.answer(f'Название: {product_name} | '
                             f'Описание: {product_description} | '
                             f'Цена: {product_price}')

        path_list = ['Images/Мяч_1.jpg', 'Images/Мяч_2.jpg',
                     'Images/Мяч_3.jpg', 'Images/Мяч_4.jpg']
        path = path_list[i]
        with open(path, 'rb') as img:
            await message.answer_photo(img)
        i += 1

    await message.answer('Выберите товар для покупки:', reply_markup=inline_kb_products)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели мяч!')


# Напишите новый класс состояний RegistrationState с следующими объектами класса State:
# username, email, age, balance(по умолчанию 1000).
class RegistrationState(StatesGroup):
    user_name = State()
    email = State()
    age = State()


# Функции цепочки состояний RegistrationState:
# sing_up(message):
# Оберните её в message_handler, который реагирует на текстовое сообщение 'Регистрация'.
@dp.message_handler(text='Регистрация')
async def sing_up(message):
    # Эта функция должна выводить в Telegram-бот сообщение
    # "Введите имя пользователя (только латинский алфавит):".
    await message.answer('Введите имя пользователя (только латинский алфавит): ')
    # После ожидать ввода возраста в атрибут RegistrationState.username при помощи метода set.
    await RegistrationState.user_name.set()


# set_username(message, state):
# Оберните её в message_handler, который реагирует на состояние RegistrationState.username.
@dp.message_handler(state=RegistrationState.user_name)
async def set_username(message, state):
    # Если пользователя message.text ещё нет в таблице,
    # то должны обновляться данные в состоянии username на message.text.
    username = message.text

    if is_included(username):
        # Если пользователь с таким message.text есть в таблице,
        # то выводить "Пользователь существует, введите другое имя"
        await message.answer('Пользователь существует, введите другое имя')
        # и запрашивать новое состояние для RegistrationState.username.
        return

    # Далее выводится сообщение "Введите свой email:" и принимается новое состояние RegistrationState.email.
    await state.update_data(username=username)
    await message.answer('Введите свой email: ')
    await RegistrationState.email.set()


# set_email(message, state):
# Оберните её в message_handler, который реагирует на состояние RegistrationState.email.
@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    # Эта функция должна обновляться данные в состоянии RegistrationState.email на message.text.
    await state.update_data(email=message.text)
    # Далее выводить сообщение "Введите свой возраст:":
    await message.answer('Введите свой возраст: ')
    # После ожидать ввода возраста в атрибут RegistrationState.age.
    await RegistrationState.age.set()


# set_age(message, state):
# Оберните её в message_handler, который реагирует на состояние RegistrationState.age.
@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    # Эта функция должна обновляться данные в состоянии RegistrationState.age на message.text.
    await state.update_data(age=message.text)
    # Далее брать все данные (username, email и age) из состояния и записывать в таблицу Users
    data = await state.get_data()
    # при помощи ранее написанной crud-функции add_user.
    add_user(data['username'], data['email'], data['age'])

    await message.answer('Регистрация завершена!', reply_markup=kb_after_registration)
    # В конце завершать приём состояний при помощи метода finish().
    await state.finish()


@dp.message_handler(text='Выйти')
async def log_out(message):
    await message.answer('Вы вышли из меню регистрации.', reply_markup=kb)


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью и продающий товары.',
                         reply_markup=kb)


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
