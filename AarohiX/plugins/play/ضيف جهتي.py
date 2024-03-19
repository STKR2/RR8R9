from pyrogram import Client, filters
from AarohiX import app

@app.on_message(filters.command(["اضفني", "ضيفني"]))
async def add_contact(client, message):
    try:
        user_id = message.from_user.id
        first_name = message.from_user.first_name
        phone_number = message.from_user.phone_number
        await app.send_contact(chat_id=user_id, phone_number=phone_number, first_name=first_name)
        await message.reply_text("~ تمت اضافتك الى جهات حساب المساعد .")
    except Exception as e:
        await message.reply_text(f"Error: {e}")
