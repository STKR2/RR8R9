from pyrogram import Client, filters
from AarohiX.core.userbot import Userbot
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import LOGGER_ID as LOG_ID
from AarohiX import app


userbot = Userbot()


async def new_message(chat_id: int, message: str, reply_markup=None):
    await app.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)

@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}"
        chat_id = message.chat.id
        riruru = f" <b><u>~ تم اضافة البوت الى مجموعة جديدة </u></b> :\n\n~ الأيدي : {chat_id}\nᴄʜᴀᴛ ~ المستخدم  : {username}\n~ اسم المجموعة : {title}\n\n~ بواسطة : {added_by}"
        reply_markup = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            message.from_user.first_name,
            user_id=message.from_user.id
        )
    ]
])

        
        await new_message(LOG_ID, riruru, reply_markup)

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(client: Client, message: Message):
    if (await client.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}"
        chat_id = message.chat.id
        rirurubye = f"✫ <b><u>~ تم ازالة البوت من مجموعة جديدة </u></b> :\n\n~ الأيدي : {chat_id}\n~ رابط المجموعة : {username}\n~ اسم المجموعة : {title}\n\n~ بواسطة : {remove_by}"
        reply_markup = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            message.from_user.first_name,
            user_id=message.from_user.id
        )
    ]
])

        
        await new_message(LOG_ID, rirurubye, reply_markup)
        await userbot.one.start()
        await userbot.one.leave_chat(chat_id)
