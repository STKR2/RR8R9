import pyrogram
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import OWNER_ID
from AarohiX import app

# تعريف الكيبورد المخصص للمطور
developer_keyboard = ReplyKeyboardMarkup(
    [
        ["زر 1"],
        ["زر 2"],
        ["زر 3"],
    ],
    resize_keyboard=True
)

# دالة للرد على الرسائل الخاصة بالمطور
@app.on_message(filters.user(OWNER_ID) & filters.private & filters.text)
async def developer_message(client, message):
    # إرسال لوحة المفاتيح المخصصة للمطور
    await message.reply("أهلا بك! اختر إحدى الخيارات:", reply_markup=developer_keyboard)

# دالة للرد على أمر start للمستخدمين العاديين
@app.on_message(filters.command("start") & ~filters.user(OWNER_ID))
async def start(client, message):
    await message.reply("مرحبًا بك في بوتنا!")
