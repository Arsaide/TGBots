import telebot
import requests
import json

bot = telebot.TeleBot('6734028781:AAFZWCODdm5P52Z2gXJeiQGn9ylGf7S97QE')
API = '169d9f1f611682f29c712012e5582e68'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')

    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')
        image = 'sun.png' if temp > 5.0 else 'sunCloud.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Город указан не верно')


bot.polling(none_stop=True)
