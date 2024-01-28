from AarohiX import app as bot
from pyrogram import filters
from pyrogram.errors import RPCError, ChatAdminRequired
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

@bot.on_chat_member_updated(filters.group, group=10)
async def member_has_joined(client: bot, member: ChatMemberUpdated):
    if (
        member.new_chat_member
        and member.new_chat_member.status not in {"banned", "left", "restricted"}
        and not member.old_chat_member
    ):
        pass
    else:
        return

    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        if user.is_bot:
            return
    except ChatAdminRequired:
        return

    try:
        username = user.username
        url = f"https://t.me/{username}" if username else f"tg://openmessage?user_id={user.id}"

        user_button = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    f"⦿ ᴄʟɪᴄᴋ ᴍᴇ ⦿",
                    url=url
                )
            ]
        ])

        caption = (
            f"🎉 **Welcome {user.mention}!** 🌟\n\n"
            f"✨ It's a pleasure to have you with us! "
            f"Feel free to share your thoughts and enjoy the community vibes.\n\n"
            f"📅 Join Date: {get_formatted_datetime()}"
        )
        
        await client.send_photo(
            chat_id=member.chat.id,
            photo="https://graph.org/file/6f913de8bd1fc44d2d7f2.jpg",
            caption=caption,
            reply_markup=user_button,
        )
    except RPCError as e:
        print(e)
        return

@bot.on_chat_member_updated(filters.group, group=20)
async def member_has_left(client: bot, member: ChatMemberUpdated):
    if (
        not member.new_chat_member
        and member.old_chat_member.status not in {"banned", "restricted"}
        and member.old_chat_member
    ):
        pass
    else:
        return

    user = member.old_chat_member.user if member.old_chat_member else member.from_user
    try:
        username = user.username
        url = f"https://t.me/{username}" if username else f"tg://openmessage?user_id={user.id}"

        user_button = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    f"⦿ ɪɴғᴏ ⦿",
                    url=url
                )
            ]
        ])

        caption = (
            f"😢 **Goodbye {user.mention}!** 😔\n\n"
            f"🌈 We'll miss you! If you ever decide to return, our doors are always open.\n\n"
            f"📅 Left Date: {get_formatted_datetime()}"
        )

        await client.send_animation(
            chat_id=member.chat.id,
            animation="https://telegra.ph/file/d28047520fad932521368.mp4",
            caption=caption,
            reply_markup=user_button,
        )
        return
    except RPCError as e:
        print(e)
        return

def get_formatted_datetime():
    now = datetime.utcnow()
    formatted_datetime = now.strftime("%A, %B %d, %Y %H:%M:%S UTC")
    return formatted_datetime
