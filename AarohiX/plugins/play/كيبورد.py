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

# دالة للاستجابة عند استخدام المطور لأمر /admin
@app.on_message(filters.command("admin") & filters.user(OWNER_ID))
async def start_2(client, message):
    # إرسال لوحة المفاتيح المخصصة للمطور
    await message.reply("", reply_markup=developer_keyboard)

# دالة للرد على الرسائل الخاصة بالمطور
@app.on_message(filters.user(OWNER_ID) & filters.private & ~filters.command)
async def developer_message(client, message):
    # التحقق مما إذا كانت الرسالة تحتوي على "/admin" قبل الرد عليها
    if "/admin" in message.text:
        # إرسال لوحة المفاتيح المخصصة للمطور
        await message.reply("", reply_markup=developer_keyboard)
