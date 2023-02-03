from aiogram import Bot, Dispatcher, executor, types
TOKEN = '6047830942:AAHdyTwJd_K9HiCWeUoXrMfvyEd68Nm2yS8'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ бот, который может показать тебе, сколько стоит та или иная валюта прямо сейчас")
@dp.message_handler()      
async def echo(message: types.Message):
   await message.answer(message.text)
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)