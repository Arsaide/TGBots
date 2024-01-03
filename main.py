import telebot
import webbrowser

bot = telebot.TeleBot('6769893511:AAFkpVxbHZiS7Lk455FKvB0cqYKkMwSa_6M')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://github.com/Arsaide')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)
