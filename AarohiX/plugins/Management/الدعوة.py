
from config import OWNER_ID
import asyncio
from pyrogram import Client, filters
from AarohiX.utils.database import get_assistant
from pyrogram.types import Message
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX.core.call import Dil


@app.on_message(filters.video_chat_started)
async def brah(_, msg):
       await msg.reply("‹ تم بدء المحادثة ›")


@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
       await msg.reply("**‹ تم انهاء المحادثة ›**")


@app.on_message(filters.video_chat_members_invited)
async def brah3(client, message):
    from_user = message.from_user
    text = f"- قام {from_user.mention}\n - بدعوة : "
    try:
        for user in message.video_chat_members_invited:
            text += f"[{user.first_name}](tg://user?id={user.id}) "
    except Exception as e:
        print(f"An error occurred: {e}")
    try:
        await message.reply(text)
    except:
        pass
