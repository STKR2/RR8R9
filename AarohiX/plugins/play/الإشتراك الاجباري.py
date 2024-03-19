from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AarohiX import app
from config import BOT_IMAGE, Muntazer

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not Muntazer:
        return
    try:
        try:
            await app.get_chat_member(Muntazer, msg.from_user.id)
        except UserNotParticipant:
            if Muntazer.isalpha():
                link = "https://t.me/" + Muntazer
            else:
                chat_info = await app.get_chat(Muntazer)
                link = chat_info.invite_link

            try:
                if BOT_IMAGE:
                    # إذا كانت الصورة متوفرة
                    await msg.reply(
                        f"~︙عزيزي {msg.from_user.mention} \n~︙عليك الأشتراك في قناة البوت \n~︙قناة البوت : @{Muntazer}.",
                        reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton("< Team Freedom >", url=link)]
                        ])
                    )
                    await app.send_photo(
                        chat_id=msg.chat.id,
                        photo=BOT_IMAGE,
                        caption=" ",
                        reply_to_message_id=msg.message_id
                    )
                else:
                    # إذا لم تكن الصورة متوفرة
                    await msg.reply(
                        f"~︙عزيزي {msg.from_user.mention} \n~︙عليك الأشتراك في قناة البوت \n~︙قناة البوت : @{Muntazer}.",
                        reply_markup=InlineKeyboardMarkup([
                            [InlineKeyboardButton("< Team Freedom >", url=link)]
                        ])
                    )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat {Muntazer}!")
