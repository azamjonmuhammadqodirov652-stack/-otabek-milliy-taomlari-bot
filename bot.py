
import os
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )
    markup.add("🍽️ Меню", "📞 Контакты")

    bot.send_message(
        message.chat.id,
        "Ассалому алейкум! Otabek Milliy Taomlariga xush kelibsiz!",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "🍽️ Меню")
def menu(message):
    bot.send_message(
        message.chat.id,
        "🍚 Ош\n🍢 Шашлык\n🍜 Лагман\n🍗 Курица KFC\n🌯 Лаваш\n\nЗаказ учун taom nomini yozing."
    )

@bot.message_handler(func=lambda message: message.text == "📞 Контакты")
def contacts(message):
    bot.send_message(
        message.chat.id,
        "Заказ бериш учун telefon raqamimizni shu yerga qo‘shamiz."
    )

bot.infinity_polling()
