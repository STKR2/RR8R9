import asyncio
import os
import shutil
import socket
from datetime import datetime
import urllib3
from git import Repo
from config import BANNED_USERS
from git.exc import GitCommandError, InvalidGitRepositoryError
from pyrogram import filters
from strings.filters import command
from AarohiX import app
from AarohiX.misc import HAPP, SUDOERS, XCB
from AarohiX.utils.database import (
    get_active_chats,
    remove_active_chat,
    remove_active_video_chat,
)
from AarohiX.utils.decorators.language import language
from AarohiX.utils.pastebin import DilBin
from config import OWNER_ID

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def is_heroku():
    return "heroku" in socket.getfqdn()


@app.on_message(command(["‹ سجلات التشغيل ›"]) & filters.user(OWNER_ID))
@language
async def log_(client, message, _):
    try:
        await message.reply_document(document="log.txt")
    except:
        await message.reply_text(_["server_1"])


