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

# دالة للرد على أمر start
@app.on_message(filters.command("start"))
async def start(client, message):
    # التحقق مما إذا كان المستخدم هو المطور
    if message.from_user.id == OWNER_ID:
        # إرسال لوحة المفاتيح المخصصة للمطور
        await message.reply("أهلا بك! اختر إحدى الخيارات:", reply_markup=developer_keyboard)
    else:
        await message.reply("مرحبًا بك في بوتنا!")
