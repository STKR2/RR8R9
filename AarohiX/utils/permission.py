from time import time
from AarohiX.misc import SUDOERS as SUDO
from functools import wraps
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import ChannelPrivate, ChatWriteForbidden, UserNotParticipant
from pyrogram.raw import functions
from pyrogram.raw.types import InputChannelEmpty, InputPeerChannel
from pyrogram.types import ChatPermissions, ChatMember, User
from pyrogram import enums

# Assuming admins_in_chat is a global variable defined somewhere in your code
admins_in_chat = {}

async def member_permissions(chat_id: int, user_id: int, app: Client):
    perms = []
    try:
        member = await app.get_chat_member(chat_id, user_id)
        if member.status == "member":
            if member.can_post_messages:
                perms.append("can_post_messages")
            if member.can_edit_messages:
                perms.append("can_edit_messages")
            if member.can_delete_messages:
                perms.append("can_delete_messages")
            if member.can_restrict_members:
                perms.append("can_restrict_members")
            if member.can_promote_members:
                perms.append("can_promote_members")
            if member.can_change_info:
                perms.append("can_change_info")
            if member.can_invite_users:
                perms.append("can_invite_users")
            if member.can_pin_messages:
                perms.append("can_pin_messages")
            if member.can_manage_video_chats:
                perms.append("can_manage_video_chats")
        return perms
    except UserNotParticipant:
        # Handle the case when the user is not a participant in the chat
        return []
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error in member_permissions: {e}")
        return []


async def authorised(func, subFunc2, client, message, *args, **kwargs):
    try:
        await func(client, message, *args, **kwargs)
    except ChatWriteForbidden:
        await message.chat.leave()
    except Exception as e:
        try:
            await message.reply_text(str(e))
        except AttributeError:
            await message.reply_text("An error occurred.")
        print(f"Error in authorised: {e}")
    return subFunc2


async def unauthorised(message: Message, permission, subFunc2):
    text = f"You don't have the required permission to perform this action.\n**Permission:** __{permission}__"
    try:
        await message.reply_text(text)
    except ChatWriteForbidden:
        await message.chat.leave()
    return subFunc2


# Update the list_admins function
async def list_admins(chat_id: int, client: Client):
    if chat_id in admins_in_chat:
        interval = time() - admins_in_chat[chat_id]["last_updated_at"]
        if interval < 3600:
            return admins_in_chat[chat_id]["data"]

    try:
        admins_in_chat[chat_id] = {
            "last_updated_at": time(),
            "data": [
                member.user.id
                async for member in client.get_chat_members(
                    chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS
                )
            ],
        }
        return admins_in_chat[chat_id]["data"]
    except ChannelPrivate:
        return


def adminsOnly(permission):
    def subFunc(func):
        @wraps(func)
        async def subFunc2(client, message: Message, *args, **kwargs):
            chatID = message.chat.id
            if not message.from_user:
                # For anonymous admins
                if message.sender_chat and message.sender_chat.id == message.chat.id:
                    return await authorised(
                        func,
                        subFunc2,
                        client,
                        message,
                        *args,
                        **kwargs,
                    )
                return await unauthorised(message, permission, subFunc2)
            # For admins and sudo users
            userID = message.from_user.id
            permissions = await member_permissions(chatID, userID, client)
            if userID not in SUDO and permission not in permissions:
                return await unauthorised(message, permission, subFunc2)
            return await authorised(func, subFunc2, client, message, *args, **kwargs)

        return subFunc2

    return subFunc
