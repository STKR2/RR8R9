from AarohiX import app
from AarohiX.misc import SUDOERS
from pyrogram import * 
from pyrogram.types import *
from AarohiX.utils.admin_check import admin_filter

strict_txt = [
    "ᴅᴏsᴛ ᴋɪ ɢᴀᴀɴᴅ ɴʜɪ ᴍᴀᴀʀ sᴋᴛᴀ.",
    "sᴀᴄʜ ᴍᴇ? ᴀᴘɴᴇ ᴅᴏsᴛ ᴋɪ ɢᴀᴀɴᴅ ᴍᴀᴀʀ ʟᴏᴏɴ.",
    "ᴍᴀɪɴ ᴀᴘɴᴇ ʙᴇsᴛ ғʀɪᴇɴᴅ ᴋᴀ ʟᴜɴᴅ ɴʜɪ ᴋᴀᴀᴛ sᴋᴛᴀ.",
    "ᴍᴀɪɴ ᴜsᴇ ᴊᴀᴀɴᴛᴀ ʜᴏᴏɴ. ᴍᴜᴊʜᴇ sᴀᴍᴀᴊʜɴᴇ ᴋᴀ ᴘʀʏᴀssʜ ᴋʀᴏ ɪsᴋɪ ᴍᴀᴀʀɪ ᴛᴏ ʀᴀɴᴅᴡᴀ ᴍᴀʀʀ ᴊᴀʏᴇɢᴀ."
]

promote = ["promote", "adminship"]
fullpromote = ["fullpromote", "fadmin"]
demote = ["demote", "lelo"]

# ========================================= #

@app.on_message(filters.command(["promote", "demote", "fullpromote"]) & admin_filter)
async def handle_admin_commands(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    
    if not reply:
        return await message.reply(random.choice(strict_txt))

    user_id = reply.from_user.id
    command = message.command[0].lower()

    if command in promote:
        await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
            can_change_info=False,
            can_invite_users=True,
            can_delete_messages=True,
            can_restrict_members=False,
            can_pin_messages=True,
            can_promote_members=False,
            can_manage_chat=True,
            can_manage_video_chats=True,
        ))
        await message.reply("♡ sᴜᴄᴄᴇssғᴜʟʟʏ ᴘʀᴏᴍᴏᴛᴇᴅ!")

    elif command in demote:
        await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
            can_change_info=False,
            can_invite_users=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_chat=False,
            can_manage_video_chats=False,
        ))
        await message.reply("♡ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇᴍᴏᴛᴇᴅ!")

    elif command in fullpromote:
        await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
            can_change_info=True,
            can_invite_users=True,
            can_delete_messages=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_promote_members=True,
            can_manage_chat=True,
            can_manage_video_chats=True,
        ))
        await message.reply("♡ sᴜᴄᴄᴇssғᴜʟʟʏ ғᴜʟʟ ᴘʀᴏᴍᴏᴛᴇᴅ!")
