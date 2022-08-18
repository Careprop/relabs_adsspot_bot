from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


# todo кнопки модели auth

'''Подписка'''
b_sub1 = KeyboardButton('Перейти на канал')
b_sub2 = KeyboardButton('Я подписался')

kb_sub = ReplyKeyboardMarkup(resize_keyboard=True)

kb_sub.add(b_sub1).add(b_sub2)
