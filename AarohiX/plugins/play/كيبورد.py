import pyrogram
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import OWNER_ID
from AarohiX import app

# تعريف الكيبورد الخاص بالمطور
admin_keyboard = ReplyKeyboardMarkup([
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

# دالة للتعامل مع الأمر /admin
@app.on_message(filters.command("admin") & filters.user(OWNER_ID))
async def admin(client, message):
    if message.from_user.id == OWNER_ID:
        await message.reply("لوحة الكيبورد الخاصة بالمطور", reply_markup=admin_keyboard)
    else:
        pass

# دالة للتعامل مع الأوامر المرتبطة بباقي السورس
@app.on_message(filters.text & ~filters.command("admin") & filters.user(OWNER_ID))
async def handle_commands(client, message):
    # ادخل هنا التحكم بالأوامر المرتبطة بباقي السورس
    pass
