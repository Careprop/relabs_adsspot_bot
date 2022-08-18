from aiogram import types, Dispatcher
from create_all import bot, dp
from keyboards import kb_sub


# todo сценарий регистрации
# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    answer = (f'Для использования бота требуется\n'
              f'подписаться на канал\n'
              f'Обязательным условием данного бота\n'
              f'является подписка на канал')
    await bot.send_message(message.from_user.id, answer, reply_markup=kb_sub)


@dp.message_handler(lambda message: 'Перейти на канал' == message.text)
async def channel(message: types.Message):
    await message.answer('ссылка на канал')


@dp.message_handler(lambda message: 'Я подписался' == message.text)
async def sub_valid(message: types.Message):
    answer = (f'<b>Добро пожаловать в AdsSpot!</b>\n'
              f'Во время первой регистрации в боте\n'
              f'действует пробный период - 3 дня\n'
              f'Гайд по сервису: (Ссылка)')
    await message.answer(answer, parse_mode=types.ParseMode.HTML)


# @dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.answer('Нет такой команды')


def register_handlers_auth(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(echo)
