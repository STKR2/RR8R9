import pyrogram
import time
from pyrogram import filters
from pyrogram import Client
from AarohiX import app
from AarohiX.misc import SUDOERS

@app.on_message(filters.command("raid", prefixes=".") & SUDOERS)
def spam_command(client, message):
    try:
        message.delete()
    except pyrogram.errors.exceptions.FloodWait as e:
        print(f"Error deleting message: {e}")
        pass

    if message.reply_to_message and message.reply_to_message.text:
        user_to_tag = message.reply_to_message.from_user.mention()
        command_args = message.text.split(".raid", 1)[-1].strip()

        try:
            num_times, text_to_spam = command_args.split(maxsplit=1)
            num_times = int(num_times)
        except ValueError:
            num_times = 1
            text_to_spam = command_args

        for _ in range(num_times):
            message.reply_text(f"{user_to_tag} **{text_to_spam}**")
            time.sleep(1)
    elif message.reply_to_message:
        user_to_tag = message.reply_to_message.from_user.mention()

        for _ in range(5):
            message.reply_to_message.reply_text(f"{user_to_tag} **SPAM!**")
            time.sleep(0.2)
    else:
        message.reply_text("Reply to a message and use the .raid command to spam.")
