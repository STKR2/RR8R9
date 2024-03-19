from pyrogram import Client, filters
from AarohiX import app

@app.on_message(filters.command(["اضفني", "ضيفني", "سجلني"]))
async def add_me(client, message):
    try:
        await app.add_contact(message.from_user.id, first_name=message.from_user.first_name)
        await message.reply_text("تمت إضافتك إلى جهات الاتصال في الحساب المساعد")
    except Exception as e:
        await message.reply_text(f"حدث خطأ: {e}")
