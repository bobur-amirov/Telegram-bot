import logging
from aiogram import Bot, Dispatcher, executor, types


from check_word import check_words


API_TOKEN = '5080847543:AAFLKGYBh5Ie_uQTGndwkqTIdMkx8RaQJ-4'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Imlo uz botga Xush kelibsiz!")


@dp.message_handler(commands='help')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("""Bu telegram bot sizga: Kiritilgan so'zni to'g'ri yoki noto'g'ri ekanligini aniqlab beradi """)

@dp.message_handler()
async def check_imlo(message: types.Message):
    words = message.text.split()
    for word in words:
        result = check_words(word)

        if result['available']:
            response = f'✅ {word.capitalize()}'
        else:
            response = f'❌ {word.capitalize()}'
            for text in result['matches']:
                response += f"✅ { text.title() }"
        await message.answer(response)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
