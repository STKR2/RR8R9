import pyrogram
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import OWNER_ID
from AarohiX import app

# تعريف الكيبورد المخصص للمطور
developer_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("Button 1")],
        [KeyboardButton("Button 2")],
        [KeyboardButton("Button 3")],
    ],
    resize_keyboard=True
)

# دالة للرد على الأوامر التي يقوم المطور بإرسالها
@app.on_message(filters.private & filters.text)
async def echo(client, message):
    # التحقق مما إذا كان المستخدم هو المطور
    if message.from_user.id == OWNER_ID:
        # إرسال لوحة المفاتيح المخصصة للمطور
        await message.reply("أهلا بك! اختر إحدى الخيارات:", reply_markup=developer_keyboard)
    else:
        await message.reply("أنت لست مطوراً!")
