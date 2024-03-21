import pyrogram
from pyrogram import Client, Filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import OWNER_ID
from AarohiX import app

@app.on_message(Filters.command("muntazer") & Filters.user(OWNER_ID))
def show_keyboard(client, message):
    keyboard = ReplyKeyboardMarkup(
        [
            [KeyboardButton("Option 1"), KeyboardButton("Option 2")],
            [KeyboardButton("Option 3"), KeyboardButton("Option 4")]
        ]
    )
    message.reply_text('Choose an option:', reply_markup=keyboard)
