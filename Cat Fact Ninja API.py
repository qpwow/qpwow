import requests
import telebot




bot_token = '5818879181:AAGTIlkIG0suvCBxi_uRfklLwYiHUC9LdDg'
cat_api_url = 'https://catfact.ninja/fact'
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['cats'])
def send_cat_fact(message):
   response = requests.get(cat_api_url)
   if response.status_code == 200:
       cat_fact = response.json()['fact']
       bot.send_message(message.chat.id, cat_fact)
   else:
       bot.send_message(message.chat.id, 'Не удалось получить факт о котах :(')


bot.polling()

