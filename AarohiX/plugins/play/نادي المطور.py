
import asyncio
from strings.filters import command
from AarohiX.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import OWNER_ID, SUPPORT_CHAT

@app.on_message(filters.command("نادي المطور", [".", ""]) & filters.group)
async def kstr(client: Client, message: Message):
       chat = message.chat.id
       gti = message.chat.title
       link = await app.export_chat_invite_link(chat)
       usr = await client.get_users(message.from_user.id)
       chatusername = f"@{message.chat.username}"
       user_id = message.from_user.id
       user_ab = message.from_user.username
       user_name = message.from_user.first_name
       buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
       reply_markup = InlineKeyboardMarkup(buttons)
       
       await app.send_message(OWNER_ID, f"- قام {message.from_user.mention}\n- بمناداتك عزيزي المطور\n- ايديه {user_id}\n- اليوزر @{user_ab}\n- ايدي المجموعة {message.chat.id}\n- الرابط {chatusername}",
       reply_markup=reply_markup,
       )
       await message.reply_text(f"~ **تم إرسال النداء الى مطور البوت\n\n~ سينضم المطور بعد قليل \n\n-› Master -› [ freedom ♪](SUPPORT_CHAT)""", disable_web_page_preview=True  
                                
       )
   
