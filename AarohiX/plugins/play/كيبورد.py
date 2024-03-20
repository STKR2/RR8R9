import pyrogram
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import OWNER_ID
from AarohiX import app

# تعريف الكيبورد المخصص للمطور
developer_keyboard = ReplyKeyboardMarkup([
    [('تفعيل_التواصل'), ('/broadcast'), ('حاله التواصل')],
    [('ضع قناة الاشتراك'), ('حذف قناه الاشتراك')],
    [('تفعيل الاشتراك'), ('تعطيل الاشتراك'), ('قناه الاشتراك')],
    [('حاله الاشتراك'), ('الاحصائيات')],
    [('تفعيل اليوتيوب'), ('تعطيل اليوتيوب'), ('حاله اليوتيوب')],
    [('حذف الاعضاء الفيك'), ('حذف الجروبات الفيك')],
    [('الاصدار'), ('تحديث السورس'), ('سرعه السيرفر')],
    [('اذاعه للمستخدمين'), ('اذاعه للجروبات')],
    [('اذاعه للمطورين'), ('اذاعه للاساسيين'), ('اذاعه للقنوات')],
    [('اذاعه للكل'), ('توجيه للكل')],
    [('توجيه للمستخدمين'), ('توجيه للجروبات'), ('توجيه للقنوات')],
    [('اخفاء الكيبورد ⚒️')]],
    resize_keyboard=True,
)

@app.on_message(filters.command("start") & filters.user(OWNER_ID))
async def start(client, message):
    if message.from_user.id == OWNER_ID:
        await message.reply("", reply_markup=developer_keyboard)
    else:
        pass
