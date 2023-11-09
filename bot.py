# Import necessary libraries
import os
from background import keep_alive
import generator
import telebot

# Set up the bot token
token = os.environ["token"]

# Create a telebot object with the token
qr_gen_bot = telebot.TeleBot(token)


# Define a message handler for the "/start" and "/help" commands
@qr_gen_bot.message_handler(commands=["start", "help"])
def send_welcome(message):
  # Send a welcome message to the user
  qr_gen_bot.send_message(
      message.chat.id,
      f"Hi, {message.from_user.first_name}, send me any text, and I'll create a QR-code"
  )


# Define a message handler for text messages
@qr_gen_bot.message_handler(content_types=["text"])
def get_text_messages(message):
  # Generate the QR code from the text message using the generator module
  generator.generate_code(message.text, message.from_user.username)

  # Send the generated QR code image back to the user as a photo
  qr_gen_bot.send_photo(message.chat.id,
                        photo=open(f"{message.from_user.username}.png", "rb"))

  # Remove the generated PNG file from the server
  os.remove(f"{message.from_user.username}.png")


# Start polling for new messages
keep_alive()
qr_gen_bot.infinity_polling()
