from pyrogram import Client, filters
import config
from AarohiX import app

@app.on_message(filters.command("تفعيل_التواصل") & filters.user(config.OWNER_ID))
def enable_communication(client, message):
    message.reply_text("تم تفعيل التواصل مع الأعضاء")

@app.on_message(filters.command("تعطيل_التواصل") & filters.user(config.OWNER_ID))
def disable_communication(client, message):
    message.reply_text("تم تعطيل التواصل مع الأعضاء")


@app.on_message(filters.text & filters.reply & filters.private filters.user(config.OWNER_ID)))
def reply_to_message(client, message):
    replied_message = message.reply_to_message
    message.reply_text(f"لقد ردت على الرسالة التي تم استقبالها: {replied_message.text}")
