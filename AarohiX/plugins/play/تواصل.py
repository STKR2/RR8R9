from pyrogram import Client, filters
from AarohiX import app
from config import OWNER_ID

# تمكين/تعطيل التواصل
communication_enabled = True

@app.on_message(filters.private & ~filters.command(["تفعيل", "disable"]))
def reply_to_private_messages(client, message):
    global communication_enabled
    if communication_enabled:
        message.reply_text("شكرًا لرسالتك، سأقوم بالرد عليك في أقرب وقت ممكن.")
    else:
        message.reply_text("عذراً، حالياً تم تعطيل التواصل مع البوت.")

@app.on_message(filters.command(["تفعيل"]) & filters.user(OWNER_ID))
def enable_communication(client, message):
    global communication_enabled
    communication_enabled = True
    message.reply_text("تم تمكين التواصل.")

@app.on_message(filters.command(["تعطيل"]) & filters.user(OWNER_ID))
def disable_communication(client, message):
    global communication_enabled
    communication_enabled = False
    message.reply_text("تم تعطيل التواصل.")
