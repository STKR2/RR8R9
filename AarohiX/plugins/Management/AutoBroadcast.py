import asyncio
import datetime
from AarohiX import app
from pyrogram import Client
from AarohiX.utils.database import get_served_chats
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_IMG_URL = "https://graph.org/file/59c42465cc959d133b022.jpg"


MESSAGE = f"""🎉 ᴀ ʙɪɢ sʜᴏᴜᴛᴏᴜᴛ ᴛᴏ ᴏᴜʀ ɴᴇᴡᴇsᴛ ᴍᴇᴍʙᴇʀ! 🙏 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ ᴡʜᴇʀᴇ ᴄᴏɴᴠᴇʀsᴀᴛɪᴏɴs ᴄᴏᴍᴇ ᴛᴏ ʟɪғᴇ. 🗣️ ᴅɪᴠᴇ ɪɴ, ɪɴᴛʀᴏᴅᴜᴄᴇ ʏᴏᴜʀsᴇʟғ, ᴀɴᴅ ʟᴇᴛ's ᴋɪᴄᴋ ᴏғғ sᴏᴍᴇ ᴀᴍᴀᴢɪɴɢ ᴄʜᴀᴛs. ᴄʟɪᴄᴋ ᴛʜᴇ ʟɪɴᴋ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ ғᴜɴ – ᴡᴇ'ᴠᴇ ʙᴇᴇɴ ᴡᴀɪᴛɪɴɢ ғᴏʀ ʏᴏᴜ! 🌟 #ᴅɪʟᴄᴏᴍᴍᴜɴɪᴛʏ"

💞ᴊᴏɪɴ » [✘ ᴄʟɪᴄᴋ ᴍᴇ ✘](https://t.me/LOVE_FEELINGS_WILL1) <√ᴊᴏɪɴ ᴏᴜʀ ғᴀᴍɪʟʏ ɢʀᴏᴜᴘ.^>

🚩 ʙᴏᴛ »|| @{app.username}||"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("» ᴀᴅᴅ ᴍᴇ «", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)
                except Exception as e:
                    pass  
    except Exception as e:
        pass  

async def continuous_broadcast():
    while True:
        await send_message_to_chats()
        await asyncio.sleep(50000)  
        
asyncio.create_task(continuous_broadcast())
