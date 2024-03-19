from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AarohiX import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/vvyvv6":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("vvyvv6", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/vvyvv6".isalpha():
                link = "https://t.me/vvyvv6"
            else:
                chat_info = await bot.get_chat("vvyvv6")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"~︙اولا عليك  {msg.from_user.mention} \n~︙الأشتراك بقناة البوت \n~︙قناة البوت : @vvyvv6 .",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("< Team Freedom >", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat @vvyvv6 !")
