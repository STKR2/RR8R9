from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from AarohiX import app
import config

@app.on_message(
    command(["اوامر", "الاوامر"])
)
async def mmmezat(client, message):
    await message.reply_text(
        f"""مرحبآ بك عزيزي {message.from_user.mention}في قسم مميزات سورس cr ميوزك\n
        هنا تكتب الاوامر """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- المطور .", user_id=config.OWNER_ID[0]),
                ],
                [
                    InlineKeyboardButton(
                        "- مسح .", callback_data="close"),
                ],
            ]
        ),
    )

@app.on_message(
    command(["المطور","السورس","المصنع"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/402c519808f75bd9b1803.jpg",
        caption=f"""~ Team freedom \n~ Dav Source """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- مطور البوت .", user_id=config.OWNER_ID[0]),
                ],
                [
                   InlineKeyboardButton(
                        "- قناة البوت . ", url=config.SUPPORT_CHANNEL),
                ],       
            ]
        ),
    )
