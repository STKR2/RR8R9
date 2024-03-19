import importlib.util
from pyrogram import Client, filters

# استيراد STRING_SESSION من ملف config.py
spec = importlib.util.spec_from_file_location("config", "config.py")
config = importlib.util.module_from_spec(spec)
spec.loader.exec_module(config)

# تهيئة حساب المساعد باستخدام STRING_SESSION
app = Client(":memory:", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN, string_session=config.STRING_SESSION)

@app.on_message(filters.command(["اضفني", "ضيفني"]))
async def add_contact(client, message):
    try:
        user_id = message.from_user.id
        first_name = message.from_user.first_name
        # استخدام رقم الهاتف إذا كان متاحاً، وإلا استخدام اسم المستخدم
        if message.from_user.phone_number:
            phone_number = message.from_user.phone_number
        else:
            phone_number = None  # يمكنك استخدام None أو قيمة أخرى حسب الاحتياجات
        await app.send_contact(chat_id=user_id, phone_number=phone_number, first_name=first_name)
        await message.reply_text("~ تم اضافتك الى جهات اتصال حساب المساعد .")
    except Exception as e:
        await message.reply_text(f"Error: {e}")
