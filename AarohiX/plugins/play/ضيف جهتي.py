from pyrogram import Client, filters

# استيراد السمة المحددة من ملف config.py
from config import STRING_SESSION

# تهيئة حساب المساعد باستخدام STRING_SESSION
app = Client(":memory:", string_session=STRING_SESSION)

# استجابة عند استلام الأمر "/addme" أو "/register"
@app.on_message(filters.command(["اضفني", "ضيفني"]))
async def add_contact(client, message):
    try:
        user_id = message.from_user.id
        first_name = message.from_user.first_name
        # استخدام رقم الهاتف إذا كان متاحاً، وإلا استخدام اسم المستخدم
        if message.from_user.phone_number:
            phone_number = message.from_user.phone_number
        else:
            phone_number = None
        # إرسال جهة الاتصال إلى حساب المساعد
        await app.send_contact(chat_id=user_id, phone_number=phone_number, first_name=first_name)
        await message.reply_text("You have been added to the contacts list in the assistant account.")
    except Exception as e:
        await message.reply_text(f"Error: {e}")
