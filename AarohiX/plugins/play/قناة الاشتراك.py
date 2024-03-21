from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AarohiX import app
from config import Muntazer, OWNER_ID

@app.on_message(filters.private & filters.user(OWNER_ID))
async def must_join_channel(_, message):
    if "‹ قناة الاشتراك ›" in message.text:
        link = f"https://t.me/{Muntazer}"
        await message.reply(
            text=f"~ عزيزي المطور \n~ هذا هي قناة الاشتراك الاجباري @{Muntazer} .",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("~ freedom .", url=link)]
            ])
        )
