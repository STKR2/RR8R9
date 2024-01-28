from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AarohiX import app

#--------------------------

MUST_JOIN = "LOVE_FEELINGS_WILL1"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://te.legra.ph/file/17673c2c6b0ff648e5983.png", caption=f"» ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ʏᴏᴜ'ᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ <a href=\"{link}\">sᴜᴘᴘᴏʀᴛ</a> ʏᴇᴛ, ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛʜᴇɴ ᴊᴏɪɴ <a href=\"{link}\">sᴜᴘᴘᴏʀᴛ</a> ᴀɴᴅ sᴛᴀʀᴛ ᴍᴇ ᴀɢᴀɪɴ ! ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("</> ᴍᴜsɪᴄ ʙᴏᴛ[❣️]", url=f"https://t.me/Alone_Dil_bot?startgroup=true"),
                            ],
                            [
                                InlineKeyboardButton("</> sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ[❣️]", url=link),
                                InlineKeyboardButton("</> ᴄʜᴀɴɴᴇʟ ᴄʜᴀᴛ[❣️]", url=f"https://t.me/AllPremiumBIN"),
                            ],
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
