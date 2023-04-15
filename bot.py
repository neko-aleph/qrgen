import os
import generator
import telebot

token = "**********************************************"
qr_gen_bot = telebot.TeleBot(token)


@qr_gen_bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    qr_gen_bot.send_message(message.chat.id,
                            f"Привет, {message.from_user.first_name}, отправь мне любой текст, и я сгенерирую из него QR-код")


@qr_gen_bot.message_handler(content_types=["text"])
def get_text_messages(message):
    generator.generate_code(message.text, message.from_user.username)
    qr_gen_bot.send_photo(message.chat.id, photo=open(f"{message.from_user.username}.png", "rb"))
    os.remove(f"{message.from_user.username}.png")


qr_gen_bot.infinity_polling()
