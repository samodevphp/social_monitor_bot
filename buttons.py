from telebot import types

def post_buttons(url):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📄 عرض المنشور", url=url))
    return markup
