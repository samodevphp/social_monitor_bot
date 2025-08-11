import telebot
import os
from utils.fetch_posts import fetch_from_sources
from utils.filter_content import clean_post
from utils.buttons import post_buttons
from config import BOT_TOKEN, CHANNEL_ID

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "أرسل رابط حساب سوشيال ميديا لبدء المتابعة.")

@bot.message_handler(func=lambda m: m.text.startswith("http"))
def add_link(message):
    link = message.text
    bot.reply_to(message, f"تم إضافة الرابط: {link}")

def check_and_post():
    posts = fetch_from_sources()
    for post in posts:
        filtered_text = clean_post(post['text'])
        bot.send_message(CHANNEL_ID, filtered_text, reply_markup=post_buttons(post['url']))

if __name__ == "__main__":
    bot.polling()
