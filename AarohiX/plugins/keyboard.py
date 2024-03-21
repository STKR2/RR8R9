import pyrogram
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
from AarohiX.misc import SUDOERS
from AarohiX import app

admin_keyboard = ReplyKeyboardMarkup([
    ['تفعيل التواصل', '/broadcast', 'حالة التواصل'],
    ['ضع قناة الاشتراك', 'حذف قناة الاشتراك'],
    ['اذاعة للمطورين', 'اذاعة للأساسيين', 'اذاعة للقنوات'],
    ['اذاعة للكل', 'توجيه للكل'],
    ['توجيه للمستخدمين', 'توجيه للجروبات', 'توجيه للقنوات'],
    ['اخفاء الكيبورد ⚒️']
], resize_keyboard=True)

# دالة للتعامل مع أمر /admin
@app.on_message(filters.command("admin") &  filters.private & SUDOERS)
async def admin(client, message):
    await message.reply("لوحة المفاتيح الخاصة بالمطور", reply_markup=admin_keyboard)

# دالة للتعامل مع الأوامر الأخرى
@app.on_message(filters.text & ~filters.command("admin") & filters.private & SUDOERS)
async def handle_commands(client, message):
    # أدخل الكود الخاص بمعالجة الأوامر الأخرى هنا
    pass
