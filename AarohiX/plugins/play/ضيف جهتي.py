from strings.filters import command
from AarohiX.core.call import Dil
from pyrogram import Client, filters
from AarohiX import app

@app.on_message(filters.command(["اضفني", "ضيفني", "سجلني"]))
async def add_contact(client, message):
    try:
        if message.from_user.username:
            await app.add_contact(message.from_user.username, message.from_user.first_name)
        else:
            await app.add_contact(message.from_user.id, message.from_user.first_name)
        await message.reply_text("تم اضافتك الى جهات الاتصال في الحساب المساعد")
    except Exception as e:
        await message.reply_text(f"خطأ : {e}")
