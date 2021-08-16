import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
API_TOK = 'yor token'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOK)
dp = Dispatcher(bot)


@dp.message_handler(commands="start") #сами кнопочки
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Аккаунт", "FAQ", "Приваты"]
    keyboard.add(*buttons)
    await message.answer("Что вы хотите выбрать?", reply_markup=keyboard)


@dp.message_handler(Text(equals="Аккаунт")) #из API я понял что для новой команды надо создлавать отдельный блок
async def cmd_acc(message: types.Message):
    await message.reply("Вот держи аккаунт: ")  #сюда надо добавить рандомный ак с файла иди бд.


@dp.message_handler(Text(equals="FAQ"))
async def cmd_faq(message: types.Message):
    await message.reply("Привет. Прочитать о моих командах ты можешь тут - ",) #как допишем бота я напишу документацию на команды


@dp.message_handler(Text(equals="Приваты"))
async def cmd_private(message: types.Message):
    await message.reply("Если вы имеете ссылки на золотые фавориты, в которых вы выступаете крысой, то отправьте 1 "
                        "сообщением ссылки: ")


"""
async def cmd_moneylong(message: types.message):
    await message.reply("Какое количество монет вы хотите перевести на ваш аккаунт:")
"""
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
