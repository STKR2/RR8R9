from pyrogram import Client, filters
from pyrogram.types import Message
from AarohiX import app
from config import OWNER_ID



@app.on_message(filters.video_chat_started)
async def brah(_, msg):
       await msg.reply("‹ تم بدء المحادثة ›")


@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
       await msg.reply("**‹ تم انهاء المحادثة ›**")


@app.on_message(filters.video_chat_members_invited)
async def brah3(app :app, message:Message):
           text = f"- قام {message.from_user.mention}\n - بدعوة : "
           x = 0
           for user in message.voice_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ")
           except:
             pass

