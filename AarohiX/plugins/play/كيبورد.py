import pyrogram
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import OWNER_ID
from AarohiX import app

# تعريف الكيبورد المخصص للمطور
developer_keyboard = ReplyKeyboardMarkup([
	[('تفعيل التواصل'),('/broadcast'),('حاله التواصل')],
	[('ضع قناة الاشتراك'),('حذف قناه الاشتراك')],
	[('تفعيل الاشتراك'),('تعطيل الاشتراك'),('قناه الاشتراك')],
	[('حاله الاشتراك'),('الاحصائيات')],
	[('تفعيل اليوتيوب'),('تعطيل اليوتيوب'),('حاله اليوتيوب')],
	[('حذف الاعضاء الفيك'),('حذف الجروبات الفيك')],
	[('الاصدار'),('تحديث السورس'),('سرعه السيرفر')],
	[('اذاعه للمستخدمين'),('اذاعه للجروبات')],
	[('اذاعه للمطورين'),('اذاعه للاساسيين'),('اذاعه للقنوات')],
	[('اذاعه للكل'),('توجيه للكل')],
	[('توجيه للمستخدمين'),('توجيه للجروبات'),('توجيه للقنوات')],
	[('توجيه للاساسيين'),('توجيه للمطورين')],
	[('رفع مطور'),('تنزيل مطور'),('عرض المطورين')],
	[('رفع مطور اساسي'),('تنزيل مطور اساسي')],
	[('عرض الاساسيين'),('مسح الاساسيين'),('مسح المطورين')],
	[('نسخه احتياطيه اساسيه'),('نسخه احتياطيه 2')],
	[('حظر عضو'),('الغاء حظر عضو'),('عرض المحظورين')],
	[('تغيير مالك البوت'),('تغيير اسم البوت')],
	[('تفعيل البوت'),('تعطيل البوت'),('حاله البوت')],
	[('مسح المحظورين'),('تغيير داتابيس البوت')],
	[('اخفاء الكيبورد ⚒️')]],
	resize_keyboard=True,
)

# دالة للاستجابة عند الضغط على زر 1
@app.on_message(filters.user(OWNER_ID) & filters.private & filters.text & filters.regex(r'^زر 1$'))
async def button_one(client, message):
    # استدعاء دالة أخرى تتعامل مع الإذاعة أو أي عملية أخرى
    await broadcast_function(message)

# دالة للاستجابة عند الضغط على زر 2
@app.on_message(filters.user(OWNER_ID) & filters.private & filters.text & filters.regex(r'^زر 2$'))
async def button_two(client, message):
    # استدعاء دالة أخرى تتعامل مع ملفات أخرى في السورس
    await another_function(message)

# دالة للاستجابة عند الضغط على زر 3
@app.on_message(filters.user(OWNER_ID) & filters.private & filters.text & filters.regex(r'^زر 3$'))
async def button_three(client, message):
    # استدعاء دالة أخرى تتعامل مع ملفات أخرى في السورس
    await another_function(message)

# دالة للرد على الرسائل الخاصة بالمطور
@app.on_message(filters.user(OWNER_ID) & filters.private & filters.text)
async def developer_message(client, message):
    # إرسال لوحة المفاتيح المخصصة للمطور
    await message.reply("أهلا بك! اختر إحدى الخيارات:", reply_markup=developer_keyboard)

# دالة للاستجابة عند استخدام المستخدم لأمر /admin
@app.on_message(filters.command("admin") & ~filters.user(OWNER_ID))
async def admin_command(client, message):
    # يمكنك هنا وضع الاستجابة المخصصة لأمر /admin
    await message.reply("هذا الأمر مخصص للمطور!")

# دالة للرد على أمر start للمستخدمين العاديين
@app.on_message(filters.command("start") & ~filters.user(OWNER_ID))
async def start(client, message):
    await message.reply("مرحبًا بك في بوتنا!")
