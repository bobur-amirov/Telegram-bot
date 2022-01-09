import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2061035974:AAGfbn7RjpzBxS6LK9puc3dYEdDJtE7udIA'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Birinchi telegram botimga xush kelibsiz!")


@dp.message_handler()
async def echo(message: types.Message):
    try:
        response = wikipedia.summary(message.text)
        await message.answer(response)
    except:
        await message.answer("Bu mavzu mavjud emas!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
