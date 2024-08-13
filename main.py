import random

from weather import get_weather_today
from answer_list import get_answer, get_sticker

from telebot import types

import requests, bs4, telebot, re

bot = telebot.TeleBot('7380101327:AAFM3Tp0uzrhA1NbP-8htjZrTOkbbwpoBq8')


def getAnekdot():
    url = 'https://anekdot.ru/random/anekdot'
    user_agent_list = (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    )

    headers = {'accept': '*/*',
               'User-agent': random.choice(user_agent_list)}
    web = requests.get(url, headers=headers).text  # Получение кода веб-сайта, где расположены случайные анекдоты

    bs = bs4.BeautifulSoup(web, "html.parser")
    result = str(
        bs.find_all(class_="topicbox")[1].find(class_="text"))  # получаем элемент, в котором написан текст анекдота
    text = result.replace("<br/>", "\n")  # удаляем лишние теги, которые попали в наш текст. заменяем тег переноса на \n
    text = text.split(">")
    text[0] = ""
    text = ''.join(text)
    text = text.split("<")
    text[-1] = ""
    text = ''.join(text)
    return text


# @bot.message_handler(commands=['start'])
# def button_message(message):
#     print(message)
#     keyboard = types.InlineKeyboardMarkup()
#     callback_button_set_foto = types.InlineKeyboardButton(text="👑 Брат 1", callback_data="set_foto")
#     callback_button_get_foto = types.InlineKeyboardButton(text="👑 Брат 2", callback_data="get_foto")
#     keyboard.add(callback_button_set_foto)
#     keyboard.add(callback_button_get_foto)
#     bot.send_message(message.chat.id, 'Мы рады Вас видеть!', reply_markup=keyboard)

# @bot.callback_query_handler(func=lambda callback: callback.data)
# def check_callback_data(callback):
#     if callback.data == 'set_foto':
#         bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text=f'👑 Брат 1',
#                               parse_mode="HTML")
#     elif callback.data == 'get_foto':
#         # tg_id = callback.message.chat.id
#         # keyboard = types.InlineKeyboardMarkup()
#         bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)
#         bot.send_message(callback.message.chat.id, '👑 Брат 2')

@bot.message_handler(content_types=['sticker'])
def send_sticker_id(message):
    print(f'This sticker id: {message.sticker.file_id}')



@bot.message_handler(commands=['start', 'menu'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    item1 = types.KeyboardButton("\U0001F5C2 Google disk")
    item2 = types.KeyboardButton("🤖 Полезные боты")
    item3 = types.KeyboardButton("😂 Анекдот")
    item4 = types.KeyboardButton("☀️ Погода")
    markup.add(item1, item2, item3, item4)
    bot.delete_message(chat_id=message.chat.id, message_id=message.id)
    bot.send_message(message.chat.id, 'Меню', reply_markup=markup)


@bot.message_handler(content_types='new_chat_members')
def new_member(message):
    bot.reply_to(message, f"""👫 Добро пожаловать {message.json['new_chat_member']['first_name']}
❗️За валовку ДА❗️
         🧑🏻‍💻 👨🏻‍💻 👩🏻‍💻""")


@bot.message_handler(content_types=['left_chat_member'])
def new_member(message):
    bot.reply_to(message, "☠️ Жаль этого добряка ☠️\n‍‍               🧖‍♂️ RIP 🧖🏻‍♀️️️")


@bot.message_handler(content_types=['text'])
def read_message(message):
    mention = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    print(message)
    if message.text.lower() in ('😂 анекдот', 'анекдот', 'funny', 'смешная история', 'душнила расмеши'):
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        bot.send_message(message.chat.id, getAnekdot())
    if message.text.lower() in ('спасибо'):
        bot.reply_to(message, "Мое величество радо помочь :)")
    if message.text.lower() in ('гугл', '\U0001F5C2 google disk'):
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        bot.send_message(message.chat.id, 'Google disk:\n1) <a href="https://clck.ru/3CGeyv">Google DOC</a>'

                         , parse_mode="HTML")

    if message.text.lower() in ('🤖 полезные боты', 'боты'):
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        bot.send_message(message.chat.id, '🤖🤖🤖Нужные Боты:'
                         + '\n1) <a href="https://t.me/woody_transport_bot">Помощник ЦТС</a>'
                         + '\n2) <a href="https://t.me/SDConciergeBot">Выручалка</a>'
                         + '\n3) <a href="https://t.me/SmsSdvorBot">СД рассылка</a>'
                         + '\n4) <a href="https://t.me/TechsupITLabs_bot">АйТи лабс</a>'
                         + '\n5) <a href="https://t.me/HelperKS_bot">Консьержи</a>'
                         , parse_mode="HTML")

    if message.text.lower() in ("☀️ погода", "погода"):
        if message.from_user.id != 2041043245:
            bot.delete_message(chat_id=message.chat.id, message_id=message.id)
            bot.send_message(message.chat.id, get_weather_today())
        else:

            bot.send_message(chat_id=message.chat.id, text=f"{mention} Хрен тебе. иди работай", parse_mode="Markdown")
            bot.send_sticker(message.chat.id,
                             "CAACAgIAAyEFAASFMqiDAAIDZWaw0YTvAyYtnQABcmhiRis3qyvdmwACQU4AAsaR2EvtbI86Vge8HDUE")
    if message.text.lower() in ('доброе утро', 'добрый день', 'добрый вечер', 'доброе'):
        bot.send_message(chat_id=message.chat.id, text=f"{mention} {get_answer()}", parse_mode="Markdown")



    if message.text.lower() in ('тест'):
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        stiker = ""
        text = f"{mention} А вам, ХРЕН!!!"
        if message.from_user.id == 1027239230:  # Брат
            stiker = "CAACAgIAAyEFAASFMqiDAAIGpmazIDdpmdGQpGkK2rTI-QiVvu8OAAJoAQACUomRI53qQjsP3UDlNQQ"
            text = f"{mention}, Кого сажаем на фьючерс? :)"
        elif message.from_user.id == 5105851865:
            stiker = "CAACAgIAAyEFAASFMqiDAAIF82aya8orhlt7rbahZxMWeM1nbF32AAJ2AAOWn4wOoD2tRP6OloA1BA"
            text = f"{mention}, Я твой сладкий ужин :)"

        bot.send_message(chat_id=message.chat.id, text=text,
                         parse_mode="Markdown")
        if stiker != "": bot.send_sticker(message.chat.id, stiker)

    if re.findall(".*фьючерс.*",message.text,re.IGNORECASE) and message.from_user.id != 1027239230:
        bot.reply_to(message, text=f"{mention}, фьючерс нужно заслужить",parse_mode="Markdown")
        bot.send_sticker(message.chat.id,get_sticker())

    if message.text.lower() in ("малкони"):
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        bot.send_message(chat_id=message.chat.id, text=f"{mention} Тссссс не буди этого алкаша 🤫🤫🤫", parse_mode="Markdown")
        bot.send_photo(chat_id=message.chat.id, photo=open('photo/photo_2024-08-07_15-32-58.jpg', 'rb'))

    if message.text.lower() in ("анкета кту"):
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        bot.send_message(chat_id=message.chat.id, text=f"{mention} Больше оплат, больше выплат 💪💪💪",
                         parse_mode="Markdown")
        bot.send_document(chat_id=message.chat.id, document=open('docs/Анкета КТУ.docx', 'rb'))
    if message.text.lower() in  ("карточка"):

        bot.delete_message(chat_id=message.chat.id, message_id=message.id)
        bot.send_message(chat_id=message.chat.id, text=f"{mention} Лови, не потеряй 😉",
                         parse_mode="Markdown")
        bot.send_document(chat_id=message.chat.id, document=open('docs/Карточка Поставка.pdf', 'rb'))
        bot.send_document(chat_id=message.chat.id, document=open('docs/Карточка СД.pdf', 'rb'))
        bot.send_document(chat_id=message.chat.id, document=open('docs/Карточка СД.Комплектация.pdf', 'rb'))



if __name__ == '__main__':
    bot.infinity_polling(none_stop=True)
