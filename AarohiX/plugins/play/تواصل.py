import asyncio
from pyrogram import Client, filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

@app.on_message(filters.text & (filters.channel | filters.private))
async def hhhki(client: Client, message: Message):
    msg = message.text
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    usr_id = message.from_user.id
    mention = message.from_user.mention

    # تحقق مما إذا كانت الرسالة قادمة من المالك أو لا
    if message.from_user.id == OWNER_ID:
        # إذا كانت الرسالة قادمة من المالك، يتم فقط إرسالها كما هي للمستخدم المعني
        await app.send_message(OWNER_ID, f"- قام {mention} \n\n- بارسال رسالة للبوت \n\n- {msg}")
    else:
        # إذا كانت الرسالة قادمة من مستخدم عادي، يتم إعادة توجيه الرد إلى المرسل الأصلي
        await app.send_message(OWNER_ID, f"لديك رسالة جديدة من {mention}:\n\n{msg}")
        await app.send_message(message.from_user.id, "تم إرسال رسالتك بنجاح.")

# تفعيل المستمع للردود على الرسائل الواردة للمطور
@app.on_message(filters.text & filters.private & ~filters.me)
async def reply_to_owner(client, message):
    if message.reply_to_message and message.reply_to_message.from_user.id == OWNER_ID:
        await app.send_message(OWNER_ID, f"رد من المستخدم {message.from_user.mention}:\n\n{message.text}")
