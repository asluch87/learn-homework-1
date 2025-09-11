
"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import ephem
import logging


logging.basicConfig(filename='bot.log', level=logging.INFO)

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')



def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    logging.info(f'Пользователь написал: {user_text}')  # Логируем в файл
    update.message.reply_text(user_text)  # Исправлено: отвечаем тем же текстом

def main():
     mybot = Updater("8332173903:AAH0hSG3_kXsZnU_5BgYRv7bg9lFdYsolo8", use_context=True)
     dp = mybot.dispatcher
     dp.add_handler(CommandHandler("start", greet_user))
     dp.add_handler(MessageHandler(Filters.text, talk_to_me))

     mybot.start_polling()
     mybot.idle()
logging.info('Бот стартовал')

if __name__ == "__main__":
    main()