
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
    try:
        inviter_id = message.sender_chat_member.inviter_id
        inviter = await client.get_users(inviter_id)
        inviter_text = f"- قام {inviter.mention} بدعوة: "
    except Exception as e:
        print(f"An error occurred while fetching inviter: {e}")
        inviter_text = "- لم يتم العثور على معلومات المُدعو."

    try:
        invited_text = ""
        for user in message.video_chat_members_invited:
            invited_text += f"[{user.first_name}](tg://user?id={user.id}) "
    except Exception as e:
        print(f"An error occurred while fetching invited users: {e}")
        invited_text = "- لم يتم العثور على المستخدمين المُدعوين."

    text = inviter_text + invited_text

    try:
        await message.reply(text)
    except Exception as e:
        print(f"An error occurred while replying to message: {e}")
