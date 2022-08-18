from aiogram.utils import executor
from create_all import dp


async def on_startup(_):
    print('OK')

from models import auth

auth.register_handlers_auth(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
