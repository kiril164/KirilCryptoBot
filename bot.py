import telebot

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to KirilCryptoBot! You'll receive BUY/SELL signals here.")

def send_signal_to_user(user_id, signal_text):
    bot.send_message(user_id, signal_text)

# Example usage
# send_signal_to_user(7575059148, "BUY ETH/USDT at 3200")

bot.polling()
