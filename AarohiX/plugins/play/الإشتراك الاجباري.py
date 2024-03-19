from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AarohiX import app
from config import muntazer

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not muntazer:
        return
    try:
        try:
            chat_id = await bot.resolve_peer(muntazer)
            await bot.get_chat_member(chat_id,msg.from_user.id)
        except UserNotParticipant:
            if muntazer.isalpha():
                link = f"https://t.me/{muntazer}"
            else:
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"~︙اولا عليك  {msg.from_user.mention} \n~︙الأشتراك بقناة البوت \n~︙قناة البوت : {muntazer}.",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("< Team Freedom >", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat {muntazer}!")
