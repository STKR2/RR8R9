#heloo 

import asyncio
from pyrogram import Client, filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message , ReplyKeyboardMarkup , KeyboardButton
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


incoming_messages = {}

# تعريف العملية لتخزين الرسائل الواردة
@app.on_message(filters.private)
async def save_incoming_messages(client: Client, message: Message):
    if message.from_user.id != OWNER_ID:
        incoming_messages[message.message_id] = message

# تعريف العملية لإرسال الرد على الرسائل
@app.on_inline_query()
async def send_reply(client: Client, inline_query):
    # تحقق مما إذا كانت الاستعلامات الفورية تأتي من المطور
    if inline_query.from_user.id == OWNER_ID:
        results = []
        # إضافة الرسائل المحفوظة كخيارات للاستجابة
        for message_id, message in incoming_messages.items():
            results.append(
                await client.send_message(inline_query.from_user.id, f"رسالة من {message.from_user.first_name}: {message.text}")
            )
        await inline_query.answer(results)
    else:
        await inline_query.answer([], switch_pm="لا يمكنك استخدام هذا الأمر.")
