import telebot
import config
import random
from telebot import types

foo = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 
	'Yes definitely.', 'You may rely on it.', 'As I see it, yes.', 
	'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 
	'Reply hazy, try again.', 'Ask again later.', 
	'Better not tell you now.', 'Cannot predict now.', 
	'Concentrate and ask again.', "Don't count on it.", 
	'My reply is no.', 'My sources say no.', 'Outlook not so good.', 
	'Very doubtful.']

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	 sti = open('static/Welcome_stick1.webp', 'rb')
	 bot.send_sticker(message.chat.id, sti)

	 # keyboard
	 markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	 item1 = types.KeyboardButton("Take an advice..")

	 markup.add(item1)

	 bot.send_message(message.chat.id, "Welcome, {0.first_name}!\n Ask your destiny a question and push the button below! \nGood Luck!".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Take an advice..':
			bot.send_message(message.chat.id, str(random.choice(foo)))
			bot.send_message(message.chat.id, "***Please ask next your question.***")

#RUN
bot.polling(none_stop=True)
