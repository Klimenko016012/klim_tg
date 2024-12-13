import asyncio
import logging
from gc import callbacks

from aiogram import Bot, Dispatcher, types
from aiogram.filters import callback_data
from aiogram.filters.command import Command
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder

logging.basicConfig(level=logging.INFO)
CHANNEL_ID=2060696046

bot = Bot(token="7860934228:AAH6aDGbFS5eITUcP8kPif8obe3m3rRZqYE")
# Диспетчер
dp = Dispatcher()

region=''
role=''


@dp.message(Command("region"))
async def cmd_start(message: types.Message):
    # очистить мэседж текст от /region и сохранить сам регион в переменную region
    await bot.send_message(message.from_user.id, message.text)
    # await message.answer(message.text)

#     написать пользователю инструкцию как обозначить свою роль


# кнопки
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Подать заявку на волонтерство")],
        [types.KeyboardButton(text="Обратиться за помощью к волонтерам")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Нажмите на подходящую для вас кнопку"
    )
    await message.answer('Здравствуйте')
    await message.answer("С какой целью вы обратились к нам?", reply_markup=keyboard)

# ответ на кнопки
@dp.message(F.text.lower()=='подать заявку на волонтерство')
async def volun(message: types.Message):
    role='volunteer'
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Введите свой номер телефона", request_contact=True)
    )
    builder.row(
        types.KeyboardButton(text="Введите информацию о себе", callback_data='info_1')
    )
    builder.row(
    types.KeyboardButton(
        text="Назад")
    )

    await message.answer(
    "Выберите действие:",
    reply_markup=builder.as_markup(resize_keyboard=True),
    )


@dp.message(F.text.lower()=='обратиться за помощью к волонтерам')
async def help(message: types.Message):
    role='help'
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Введите свой номер телефона", request_contact=True)
    )
    builder.row(
        types.KeyboardButton(text="Введите информацию о себе", callback_data='info_2')
    )
    builder.row(
        types.KeyboardButton(
            text="Назад")
    )

# @dp.message(Command("region"))
# async def cmd_staаrt(message: types.Message):
    # if role=='volunteer'

    # очистить мэседж текст от /regioпгоеn и сохранить сам регион в переменную region
    # await bot.send_message(message.from_user.id, message.text)

    # await message.answer(message.text)
#     написать пользователю инструкцию как обозначить свою роль

# @dp.message(Command("role"))
# async def cmd_start(message: types.Message):
#     очистить мэседж текст от /role и получить голую цифру
#     await bot.send_message(message.from_user.id, message.text)
#     await message.answer(message.text)
# если роль = 2(пострадавший), то составить следующую строку поисква в поисковике: 'контакты спасательных служб по региону' + region
# если роль = 1(волонтер), то составить следующую строку поисква в поисковике: 'как стать волонтером в регионе' + region
#найти код который выведет пользователю первые 5 сайтов

async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)

# Запуск процесса поллинга новых апдейтов
async def main():
    # await send_message(CHANNEL_ID, '<b>Hello!</b>')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

