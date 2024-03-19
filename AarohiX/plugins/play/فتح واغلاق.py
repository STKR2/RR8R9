from random import randint
from typing import Optional

from pyrogram import Client,filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message
from pyrogram.types import Message
from pyrogram import filters, Client
from AarohiX import app
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AarohiX.core.call import Dil
from AarohiX.utils.database import *
from pytgcalls.exceptions import NoActiveGroupCall, TelegramServerError


def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await client.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await message.edit(f"**No group call Found** {err_msg}")
    return False


@app.on_message(
    filters.command("فتح الكول") & filters.group & filters.channel
)
async def opengc(client: Client, message: Message):
    flags = " ".join(message.command[1:])
    tex = await message.reply_text(message, "`Processing . . .`")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    assistant = await group_assistant(Anon, message.chat.id)
    args = f"**تم بداء المحادثه\n ⌔ **Chat ID** : `{chat_id}`"
    try:
        if not vctitle:
            await assistant.invoke(
                CreateGroupCall(
                    peer=(await assistant.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n ⌔ **Title:** `{vctitle}`"
            await assistant.invoke(
                CreateGroupCall(
                    peer=(await assistant.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await tex.edit(args)
    except Exception as e:
        await tex.edit(f"**INFO:** `{e}`")


@app.on_message(
    filters.regex("قفل الكول") & filters.group & filters.channel
)
async def end_vc(client: Client, message: Message):
    chat_id = message.chat.id
    assistant = await group_assistant(Anon, message.chat.id)
    if not (
        group_call := (
            await get_group_call(client, message, err_msg=", group call already ended")
        )
    ):
        return
    if message.from_user.id != assistant.user.id:
        return await message.reply_text("Only group assistant can end the call.")
    await client.invoke(DiscardGroupCall(call=group_call))
    await message.reply_text(f"Group call ended in chat ID: `{chat_id}`.")
