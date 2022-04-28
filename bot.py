# -*- coding: utf-8 -*-

# Telegram
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, User, ChatAction, chat
from telegram.ext import Updater, Filters, MessageHandler, CallbackContext, CommandHandler, CallbackQueryHandler

# QR Code
from pyzbar.pyzbar import decode
#import pyqrcode

# System libraries
import os
from os import listdir
from os.path import isfile, join

from io import BytesIO
from PIL import Image

# Barcodes of Countries
from countries import *

# Get Country Flag
import flag

# Configure TOKEN
from configure import *

# DB
from db import add_user
from db import getLang
from db import change_language
from db import last_seen

import logging

from sqlite3 import OperationalError, IntegrityError

from datetime import date, datetime

import pytz

from bar import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = config["TOKEN"]

CHANNEL_ID = "-1001471707685"

USER_ID = None
USER_FOLLOWED = None


button_ru = [[InlineKeyboardButton(text = "ПОДПИСАТЬСЯ", url="t.me/karrabakh")],[InlineKeyboardButton(text = "Я ПОДПИСАЛСЯ", callback_data = "check")]]

reply_markup_ru = InlineKeyboardMarkup(button_ru)

button_eng = [[InlineKeyboardButton(text = "FOLLOW", url="t.me/karrabakh")],[InlineKeyboardButton(text = "I FOLLOWED", callback_data = "check")]]

reply_markup_eng = InlineKeyboardMarkup(button_eng)

def start(update: Update, context: CallbackContext):
    global USER_ID

    USER_ID = update.effective_user.id
    
    username =  update.effective_user.username
    
    
    time = datetime.now()

    timezone = pytz.timezone("Asia/Yerevan")

    time = timezone.localize(time)

    reg_time = time.strftime("%H:%M:%S")
    
    reg_date = time.strftime("%d/%m/%Y")

    try:
        lang = getLang(USER_ID)
        last_seen(USER_ID)
        if lang == "ru":
            welcome(update, context, "ru")
        elif lang == "eng":
            welcome(update, context, "eng")
        else:
            language(update, context)
    except TypeError:
        try:
            add_user(
                user_id = USER_ID,
                username = username,
                lang = "notSelected",
                reg_date = reg_date,
                reg_time = reg_time,
                last_seen_date = reg_date,
                last_seen_time = reg_time
            )
            
        except IntegrityError:
            add_user(
                user_id = USER_ID,
                username = "integrityError",
                lang = "notSelected",
                reg_date = reg_date,
                reg_time = reg_time,
                last_seen_date = reg_date,
                last_seen_time = reg_time
            )
        language(update, context)

        check_user(update, context)
    except OperationalError:
        try:
            add_user(
                user_id = USER_ID,
                username = username,
                lang = "notSelected",
                reg_date = reg_date,
                reg_time = reg_time,
                last_seen_date = reg_date,
                last_seen_time = reg_time
            )
        except :
            add_user(
                user_id = USER_ID,
                username = "IntegrityError",
                lang = "notSelected",
                reg_date = reg_date,
                last_seen_date = reg_date,
                last_seen_time = reg_time
            )
        
        language(update, context)

        check_user(update, context)
    
def check_user(update: Update, context: CallbackContext):
    chat_id = None
    
    if update.message is not None:
        chat_id = update.message.chat.id
    elif update.callback_query is not None:
        chat_id = update.callback_query.message.chat.id

    status = ["creator", "member", "administrator"]
    user_status = context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=chat_id).status

    for i in status:
        if i == user_status:
            global USER_FOLLOWED
            USER_FOLLOWED = "True" + str(USER_ID)
            
            break
        else:
            USER_FOLLOWED = "False" + str(USER_ID)
    
def check_user_handler(update: Update, context: CallbackContext):
    global USER_ID

    USER_ID = update.effective_user.id
    
    query = update.callback_query
    query.answer()

    data = query.data

    if data == "check":
        """
        check_user(update, context)
        if USER_FOLLOWED == "True" + str(USER_ID):
            if getLang(USER_ID) == "ru":
                update.effective_message.reply_text(text="Вы успешно получили доступ к боту \!", parse_mode="MarkdownV2")
            elif getLang(USER_ID) == "eng":
                update.effective_message.reply_text(text="_*You have successfully accessed the bot \!*_", parse_mode="MarkdownV2")
        elif USER_FOLLOWED == "False" + str(USER_ID):
            if getLang(USER_ID) == "ru":
                update.effective_message.reply_text(text="_Я все вижу\. Вы не подписались на канал \!_", parse_mode="MarkdownV2")
                update.effective_message.reply_text(text = "🤖 _Чтобы продолжить использование бота\, необходимо подписаться на наш канал 🔥_", reply_markup = reply_markup_ru, parse_mode="MarkdownV2")
            elif getLang(USER_ID) == "eng":
                update.effective_message.reply_text(text="_I see everything\. You have not subscribed to the channel\!_", parse_mode="MarkdownV2")
                update.effective_message.reply_text(text = "🤖 _To continue using the bot \, you need to subscribe to channel\. 🔥_", reply_markup = reply_markup_eng, parse_mode="MarkdownV2")
        """
                
def welcome(update: Update, context: CallbackContext, lang):

    first_name = format_text(update.effective_user.first_name)

    if lang == "ru":
        update.effective_message.reply_text("🚀 Здравствуйте, " + first_name + "\.\n\nДобро пожаловать в *Made in* бот\.\n\n🦾 \- _Этот бот является самым быстрым способом *проверить товар на подлинность*, и  *узнать происхождение* разных продуктов по всему миру, используя лишь  штрих\-код\._\n\n📷 \- _*Всё что нужно сделать, это отправить боту фотографию штрих \(QR\) кода\.*_\n\n🔑 *Доступные команды*:\n\nℹ️ /help \- _информация об использовании_\n\n📙 /language \- _сменить язык_", parse_mode="MarkdownV2")
    elif lang == "eng":
        update.effective_message.reply_text("🚀 Hi, " + first_name + "\.\n\nWelcome to *Made in* bot\.\n\n🦾 \- _This bot is the fastest way to *check the authenticity* of goods and *find out the origin* of different products around the world using only a barcode\._\n\n📷 \- _*All you need to do is send the barcode photo to the bot\.*_\n\n🔑 *Available commands*:\n\nℹ️ /help \- _usage information_\n\n📙 /language \- _change language_", parse_mode="MarkdownV2")

def decode_qr(update: Update, context: CallbackContext):
    global USER_FOLLOWED
    global USER_ID

    USER_ID = update.effective_user.id
    
    check_user(update, context)

    last_seen(USER_ID)
    
    try:
        lang = getLang(USER_ID)
        print("lang")
        if lang == "ru" or lang == "eng":
            if USER_FOLLOWED == "True" + str(USER_ID):
                chat_id = update.message.chat_id

                if update.message.photo:
                    context.bot.sendChatAction(chat_id = chat_id, action = ChatAction.TYPING)
                    id_img = update.message.photo[-1].file_id
                else:
                    return

                foto = context.bot.getFile(id_img)
                new_file = context.bot.get_file(foto.file_id)
                new_file.download("images/qrcode.png")
                try:
                    result = decode(Image.open("images/qrcode.png"))
                    
                    barcode = result[0].data.decode("utf-8")
                    barcode_type = result[0].type

                    country_code = get_country(barcode, barcode_type)

                    if isinstance(country_code, str):
                        if len(country_code) == 2:
                            country_flag = flag.flag(country_code)
                            
                            country_name = get_country_name(country_code, lang)
                            
                            country_full_name = country_name + " " + country_flag
                            text = result_msg(barcode, country_full_name, barcode_type, lang)
                            context.bot.sendMessage(chat_id = chat_id, text=text, parse_mode="MarkdownV2")
                        else:
                            msg = country_not_detected(barcode, barcode_type, lang)
                            context.bot.sendMessage(
                                chat_id=chat_id, text=msg, parse_mode="MarkdownV2")
                    elif isinstance(country_code, list):
                        msg = get_from_list(country_code, barcode, barcode_type, lang)
                        context.bot.sendMessage(
                            chat_id=chat_id, text = msg, parse_mode="MarkdownV2")

                except IndexError:
                    if lang == "ru":
                        context.bot.sendMessage(
                            chat_id=chat_id, text="\u2757 *Что\-то пошло не так \!*\n\n\u26A0\uFE0F _Код на изображении должен быть в центре, не должен быть слишком маленьким и плохого качества\._", parse_mode="MarkdownV2")
                    elif lang == "eng":
                        context.bot.sendMessage(
                            chat_id=chat_id, text="\u2757 *Something went wrong \!*\n\n\u26A0\uFE0F _The code in the image should be in the center, should not be too small and of poor quality\._", parse_mode="MarkdownV2")


                except ValueError:
                    if lang == "ru":
                        context.bot.sendMessage(
                            chat_id=chat_id, text="_*\n\n\u26A0\uFE0F Код не может быть обработан \!*_", parse_mode="MarkdownV2")
                    elif lang == "eng":
                        context.bot.sendMessage(
                            chat_id=chat_id, text="_*\n\n\u26A0\uFE0F The code could not be processed \!*_", parse_mode="MarkdownV2")

                os.remove("images/qrcode.png")
            elif USER_FOLLOWED == "False" + str(USER_ID):
                if getLang(USER_ID) == "ru":
                    update.effective_message.reply_text(text = "🤖 _Чтобы продолжить использование бота\, необходимо подписаться на наш канал 🔥_", reply_markup = reply_markup_ru, parse_mode="MarkdownV2")
                elif getLang(USER_ID) == "eng":
                    update.effective_message.reply_text(text = "🤖 _To continue using the bot \, you need to subscribe to channel\. 🔥_", reply_markup = reply_markup_eng, parse_mode="MarkdownV2")
        else:
            language(update, context)
    except TypeError as e:
        print(e)
        language(update, context)

def text_reply(update: Update, context: CallbackContext):
    global USER_ID
    USER_ID = update.effective_user.id
    chat_id = update.message.chat_id
    
    try:
 
        lang = getLang(USER_ID)
        last_seen(USER_ID)
        if lang == "null":
            language(update, context)
        elif lang == "ru":
            context.bot.send_message(
                    chat_id=chat_id, text="_*❗️Пожалуйста, пришлите фотографию штрих кода\.*_\n\n📍 /help \- _помощь в использовании_", parse_mode="MarkdownV2")
        elif lang == "eng":
            context.bot.send_message(
                    chat_id=chat_id, text="_*❗️Please send a photo of the barcode\.*_\n\n📍 /help \- _help in using_", parse_mode="MarkdownV2")
    except TypeError:
        language(update, context)
        last_seen(USER_ID)
        
    """
    global USER_ID

    USER_ID = update.effective_user.id
    check_user(update, context)
    global USER_FOLLOWED

    if USER_FOLLOWED == "True" + str(USER_ID):
        chat_id = update.message.chat_id
        context.bot.send_message(
                chat_id=chat_id, text="_*❗️Пожалуйста, пришлите фотографию штрих кода\.*_", parse_mode="MarkdownV2")
        qr_text = update.message.text
        url = pyqrcode.create(qr_text)
        url.png("images/created_qrcode.png", scale=15)
        context.bot.sendChatAction(chat_id = chat_id, action = ChatAction.UPLOAD_DOCUMENT)
        with open("images/created_qrcode.png", "rb") as file:
            context.bot.send_document(chat_id = chat_id, document=file)
    
    elif USER_FOLLOWED == "False" + str(USER_ID):
        update.effective_message.reply_text(text = "🤖 _Чтобы продолжить использование бота\, необходимо подписаться на наш канал 🔥_", reply_markup = reply_markup, parse_mode="MarkdownV2")
    """

def language(update: Update, context: CallbackContext):
    chat_id = -1
    
    if update.message is not None:
        chat_id = update.message.chat.id
    elif update.callback_query is not None:
        chat_id = update.callback_query.message.chat.id

    buttons = [[InlineKeyboardButton(text = "Русский 🇷🇺", callback_data="ru"), InlineKeyboardButton(text = "English 🇬🇧", callback_data = "eng")]]
    reply_markup = InlineKeyboardMarkup(buttons)
    context.bot.sendMessage(chat_id = chat_id, text = "_Выберите свой язык\!\nChoose your language\. 🔽_", reply_markup = reply_markup,  parse_mode="MarkdownV2")

def buttons_handler(update: Update, context: CallbackContext):
    global USER_FOLLOWED
    global USER_ID

    USER_ID = update.effective_user.id

    last_seen(USER_ID)

    query = update.callback_query
    query.answer()

    data = query.data
    
    if data == "ru":
        try:
            lang = getLang(USER_ID)
            if lang != "null":
                update.effective_message.reply_text(text = "_🇷🇺 Ваш язык был успешно изменен\._", parse_mode="MarkdownV2")
        except TypeError:
            pass
        
        
        change_language("ru", USER_ID)
        
        welcome(update, context, "ru")
        
        if USER_FOLLOWED == "False" + str(USER_ID):
            update.effective_message.reply_text(text = "🤖 _Чтобы продолжить использование бота\, необходимо подписаться на канал 🔥_", reply_markup = reply_markup_ru, parse_mode="MarkdownV2")
    
    elif data == "eng":
        try:
            lang = getLang(USER_ID)
            if lang != "null":
                update.effective_message.reply_text(text = "_🇬🇧 Your language has been successfully changed\._", parse_mode="MarkdownV2")
        except TypeError:
            pass
        
        change_language("eng", USER_ID)
        
        welcome(update, context, "eng")

        if USER_FOLLOWED == "False" + str(USER_ID):
            update.effective_message.reply_text(text = "🤖 _To continue using the bot \, you need to subscribe to channel\. 🔥_", reply_markup=reply_markup_eng, parse_mode="MarkdownV2")
    elif data == "check":
        check_user(update, context)
        if USER_FOLLOWED == "True" + str(USER_ID):
            if getLang(USER_ID) == "ru":
                update.effective_message.reply_text(text="🎉 Вы успешно получили доступ к боту\!", parse_mode="MarkdownV2")
            elif getLang(USER_ID) == "eng":
                update.effective_message.reply_text(text="_*🎉 You have successfully accessed the bot\!*_", parse_mode="MarkdownV2")
        elif USER_FOLLOWED == "False" + str(USER_ID):
            if getLang(USER_ID) == "ru":
                update.effective_message.reply_text(text="_Я все вижу 🙃\. Вы не подписались на канал \!_", parse_mode="MarkdownV2")
                update.effective_message.reply_text(text = "🤖 _Чтобы продолжить использование бота\, необходимо подписаться на наш канал 🔥_", reply_markup = reply_markup_ru, parse_mode="MarkdownV2")
            elif getLang(USER_ID) == "eng":
                update.effective_message.reply_text(text="_I see everything 🙃\. You have not subscribed to the channel\!_", parse_mode="MarkdownV2")
                update.effective_message.reply_text(text = "🤖 _To continue using the bot\, you need to subscribe to channel\. 🔥_", reply_markup = reply_markup_eng, parse_mode="MarkdownV2")

def help(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    global USER_ID
    USER_ID = update.effective_user.id
    chat_id = update.message.chat_id
    last_seen(USER_ID)
    try:
        lang = getLang(USER_ID)
        if lang == "null":
            language(update, context)
        elif lang == "ru":
            context.bot.send_message(
                    chat_id=chat_id, text=info_ru, parse_mode="MarkdownV2")
        elif lang == "eng":
            context.bot.send_message(
                    chat_id=chat_id, text=info_eng, parse_mode="MarkdownV2")
    except TypeError as e:
        print(e)
        language(update, context)
    
def main():
    updater = Updater(
        token=TOKEN,
        request_kwargs={'read_timeout': 20, 'connect_timeout': 20},
        use_context=True
    )

    updater.dispatcher.add_handler(MessageHandler(Filters.photo, decode_qr))
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(buttons_handler))
    updater.dispatcher.add_handler(CallbackQueryHandler(check_user_handler))
    updater.dispatcher.add_handler(CommandHandler("language", language))
    updater.dispatcher.add_handler(CommandHandler("help", help))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, text_reply))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
