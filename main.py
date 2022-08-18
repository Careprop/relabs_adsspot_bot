from aiogram.utils import executor
from create_all import dp
from models import auth


async def on_startup(_):
    print('OK')


auth.register_handlers_auth(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
