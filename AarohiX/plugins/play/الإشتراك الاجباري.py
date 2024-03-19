from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AarohiX import app
from config import SUPPORT_CHAT

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not SUPPORT_CHAT:
        return
    try:
        try:
            chat_info = await bot.get_chat(SUPPORT_CHAT)
            await bot.get_chat_member(chat_info.id, msg.from_user.id)
        except UserNotParticipant:
            if SUPPORT_CHAT.isalpha():
                link = f"https://t.me/{SUPPORT_CHAT}"
            else:
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"~︙اولا عليك  {msg.from_user.mention} \n~︙الأشتراك بقناة البوت \n~︙قناة البوت : {SUPPORT_CHAT}.",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("< Team Freedom >", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat {SUPPORT_CHAT}!")
