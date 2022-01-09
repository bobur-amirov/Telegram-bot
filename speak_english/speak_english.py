import logging
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator
translator = Translator()


from oxford_lookup import get_definitions

API_TOKEN = '5037529288:AAEdno4P4s7mG4qnkIaY0mgy67mXtjaIM4A'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Ikkinchi Speak English telegram botimga Xush kelibsiz!")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("""Bu telegram bot sizga: 
    \nAgar 2 ta yoki undan ko'p so'z kiritsangiz buni tarjiman qilib beradi. \n Agar 2 tadan kam so'z kiritsangiz bo'ning izohli lug'atini aytib beradi""")

@dp.message_handler()
async def translate(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) >= 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text

        lookup = get_definitions(word_id)

        if lookup:
            await message.reply(f"Word: {word_id} \nDefinitions: \n {lookup['definitions']}")
            if lookup.get('audio'):
                await message.reply_voice(lookup['audio'])
        else:
            await message.reply("Bunday so'z mavjud emas")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
