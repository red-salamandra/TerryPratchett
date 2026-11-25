import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
	chatId = message.chat.id
	text = message.text.lower
	bot.send_message(chatId, "теперь тут терри пратчетт")

@bot.message_handler(content_types=['text'])
def send_message(message):
	chatId = message.chat.id
	text = message.text.lower()
	print(text)
	if text == "лови терри пратчетта":
		bot.send_message(chatId, "поймал!")
	elif text == "не люблю терри пратчетта":
		bot.send_message(chatId, "лох")
	elif text == "терри пратчетт":
		bot.send_message(chatId, "терри прачетт")

bot.polling()
