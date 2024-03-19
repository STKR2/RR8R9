#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/AnonXMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/AnonXMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import platform
import re
import socket
import uuid
import os
import speedtest
import asyncio
import platform
from sys import version as pyver
from datetime import datetime

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid, FloodWait
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from pytgcalls.__version__ import __version__ as pytgver

import config
from config import OWNER_ID
from config import BANNED_USERS, MUSIC_BOT_NAME
from ZeMusic import YouTube, app
from ZeMusic import app as Client
from ZeMusic.core.userbot import assistants
from ZeMusic.misc import SUDOERS, mongodb
from ZeMusic.plugins import ALL_MODULES
from ZeMusic.utils.database import get_served_chats, get_served_users, get_sudoers
from ZeMusic.utils.decorators.language import language, languageCB
from ZeMusic.utils.inline.stats import back_stats_buttons, stats_buttons

loop = asyncio.get_running_loop()

# Commands


@app.on_message(
    filters.command(["《hshdhh》"], "")
    & filters.group
    & ~BANNED_USERS
)
@language
async def stats_global(client, message: Message, _):
    upl = stats_buttons(
        _, True if message.from_user.id in SUDOERS else False
    )
    await message.reply_photo(
        photo=config.STATS_IMG_URL,
        caption=_["gstats_11"].format(config.MUSIC_BOT_NAME),
        reply_markup=upl,
    )


@app.on_message(
    filters.command(["《hsjsnsnsnj》"], "")
    & SUDOERS
)
@app.on_message(filters.command(["/start", "رجوع"], "") & filters.private)
async def kep(client, message):
  kep = ReplyKeyboardMarkup([["《قسم الاذاعه》"], ["《قسم الحساب المساعد》"], ["《قسم الادمنيه》", "《قسم الكولات》"], ["《معلومات السيرفر》", "《فحص سرعه البوت》"], ["المحظورين عام🚨", "المحظورين ميوزك❌"], ["《الاحصائيات والتواصل》"], ["《قسم الاشتراك الاجباري》"], ["نقل ملكية البوت"], ["《قسم النسخه الاحتياطيه》"], ["《قسم السورس》"], ["《الغاء》", "《تنظيف》"], ["《قفل الكيبورد🔒》"]], resize_keyboard=True)
  await message.reply_text("╮⦿ اهـلا بڪ عزيـزي المطـور الاساسـي │⎋ اليك كيب التحكم بالبوت في سورس الميوزك❤️‍🔥", reply_markup=kep)




@app.on_message(
    filters.command(["《hdjsnsnn》"], "")
    & filters.group
    & ~BANNED_USERS
)
@language
async def gstats_global(client, message: Message, _):
    mystic = await message.reply_text(_["gstats_1"])
    stats = await get_global_tops()
    if not stats:
        await asyncio.sleep(1)
        return await mystic.edit(_["gstats_2"])

    def get_stats():
        results = {}
        for i in stats:
            top_list = stats[i]["spot"]
            results[str(i)] = top_list
            list_arranged = dict(
                sorted(
                    results.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )
            )
        if not results:
            return mystic.edit(_["gstats_2"])
        videoid = None
        co = None
        for vidid, count in list_arranged.items():
            if vidid == "telegram":
                continue
            else:
                videoid = vidid
                co = count
            break
        return videoid, co

    try:
        videoid, co = await loop.run_in_executor(None, get_stats)
    except Exception as e:
        print(e)
        return
    (
        title,
        duration_min,
        duration_sec,
        thumbnail,
        vidid,
    ) = await YouTube.details(videoid, True)
    title = title.title()
    final = f"Top Most Played Track on {MUSIC_BOT_NAME}\n\n**Title:** {title}\n\nPlayed** {co} **times"
    upl = get_stats_markup(
        _, True if message.from_user.id in SUDOERS else False
    )
    await app.send_photo(
        message.chat.id,
        photo=thumbnail,
        caption=final,
        reply_markup=upl,
    )
    await mystic.delete()


@app.on_callback_query(filters.regex("GetStatsNow") & ~BANNED_USERS)
@languageCB
async def top_users_ten(client, CallbackQuery: CallbackQuery, _):
    chat_id = CallbackQuery.message.chat.id
    callback_data = CallbackQuery.data.strip()
    what = callback_data.split(None, 1)[1]
    upl = back_stats_markup(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    mystic = await CallbackQuery.edit_message_text(
        _["gstats_3"].format(
            f"of {CallbackQuery.message.chat.title}"
            if what == "Here"
            else what
        )
    )
    if what == "Tracks":
        stats = await get_global_tops()
    elif what == "Chats":
        stats = await get_top_chats()
    elif what == "Users":
        stats = await get_topp_users()
    elif what == "Here":
        stats = await get_particulars(chat_id)
    if not stats:
        await asyncio.sleep(1)
        return await mystic.edit(_["gstats_2"], reply_markup=upl)
    queries = await get_queries()

    def get_stats():
        results = {}
        for i in stats:
            top_list = (
                stats[i]
                if what in ["Chats", "Users"]
                else stats[i]["spot"]
            )
            results[str(i)] = top_list
            list_arranged = dict(
                sorted(
                    results.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )
            )
        if not results:
            return mystic.edit(_["gstats_2"], reply_markup=upl)
        msg = ""
        limit = 0
        total_count = 0
        if what in ["Tracks", "Here"]:
            for items, count in list_arranged.items():
                total_count += count
                if limit == 10:
                    continue
                limit += 1
                details = stats.get(items)
                title = (details["title"][:35]).title()
                if items == "telegram":
                    msg += f"🔗[Telegram Files and Audios](https://t.me/telegram) ** played {count} times**\n\n"
                else:
                    msg += f"🔗 [{title}](https://www.youtube.com/watch?v={items}) ** played {count} times**\n\n"

            temp = (
                _["gstats_4"].format(
                    queries,
                    config.MUSIC_BOT_NAME,
                    len(stats),
                    total_count,
                    limit,
                )
                if what == "Tracks"
                else _["gstats_7"].format(
                    len(stats), total_count, limit
                )
            )
            msg = temp + msg
        return msg, list_arranged

    try:
        msg, list_arranged = await loop.run_in_executor(
            None, get_stats
        )
    except Exception as e:
        print(e)
        return
    limit = 0
    if what in ["Users", "Chats"]:
        for items, count in list_arranged.items():
            if limit == 10:
                break
            try:
                extract = (
                    (await app.get_users(items)).first_name
                    if what == "Users"
                    else (await app.get_chat(items)).title
                )
                if extract is None:
                    continue
                await asyncio.sleep(0.5)
            except:
                continue
            limit += 1
            msg += f"🔗`{extract}` played {count} times on bot.\n\n"
        temp = (
            _["gstats_5"].format(limit, MUSIC_BOT_NAME)
            if what == "Chats"
            else _["gstats_6"].format(limit, MUSIC_BOT_NAME)
        )
        msg = temp + msg
    med = InputMediaPhoto(media=config.GLOBAL_IMG_URL, caption=msg)
    try:
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=upl
        )
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.GLOBAL_IMG_URL, caption=msg, reply_markup=upl
        )


@app.on_callback_query(filters.regex("TopOverall") & ~BANNED_USERS)
@languageCB
async def overall_stats(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    what = callback_data.split(None, 1)[1]
    if what != "s":
        upl = overallback_stats_markup(_)
    else:
        upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_8"])
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    total_queries = await get_queries()
    blocked = len(BANNED_USERS)
    sudoers = len(SUDOERS)
    mod = len(ALL_MODULES)
    assistant = len(assistants)
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "Yes"
    else:
        ass = "No"
    cm = config.CLEANMODE_DELETE_MINS
    text = f"""**Bot's Stats and Information:**

**Imported Modules:** {mod}
**Served Chats:** {served_chats} 
**Served Users:** {served_users} 
**Blocked Users:** {blocked} 
**Sudo Users:** {sudoers} 
    
**Total Queries:** {total_queries} 
**Total Assistants:** {assistant}
**Auto Leaving Assistant:** {ass}
**Cleanmode duration:** {cm} Mins

**Play Duration Limit:** {play_duration} Mins
**Song Download Limit:** {song} Mins
**Bot's Server Playlist Limit:** {playlist_limit}
**Playlist Play Limit:** {fetch_playlist}"""
    med = InputMediaPhoto(media=config.STATS_IMG_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=upl
        )
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.STATS_IMG_URL, caption=text, reply_markup=upl
        )


@app.on_callback_query(filters.regex("bot_stats_sudo"))
@languageCB
async def overall_stats(client, CallbackQuery, _):
    if CallbackQuery.from_user.id not in SUDOERS:
        return await CallbackQuery.answer(
            "Only for Sudo Users", show_alert=True
        )
    callback_data = CallbackQuery.data.strip()
    what = callback_data.split(None, 1)[1]
    if what != "s":
        upl = overallback_stats_markup(_)
    else:
        upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_8"])
    sc = platform.system()
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    ram = (
        str(round(psutil.virtual_memory().total / (1024.0**3)))
        + " GB"
    )
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}MHz"
    except:
        cpu_freq = "Unable to Fetch"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    mod = len(ALL_MODULES)
    db = pymongodb
    call = db.command("dbstats")
    datasize = call["dataSize"] / 1024
    datasize = str(datasize)
    storage = call["storageSize"] / 1024
    objects = call["objects"]
    collections = call["collections"]
    status = db.command("serverStatus")
    query = status["opcounters"]["query"]
    mongouptime = status["uptime"] / 86400
    mongouptime = str(mongouptime)
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    total_queries = await get_queries()
    blocked = len(BANNED_USERS)
    sudoers = len(await get_sudoers())
    text = f""" **Bot's Stats and Information:**

**Imported Modules:** {mod}
**Platform:** {sc}
**Ram:** {ram}
**Physical Cores:** {p_core}
**Total Cores:** {t_core}
**Cpu Frequency:** {cpu_freq}

**Python Version :** {pyver.split()[0]}
**Pyrogram Version :** {pyrover}
**Py-TgCalls Version :** {pytgver}

**Storage Avail:** {total[:4]} GiB
**Storage Used:** {used[:4]} GiB
**Storage Left:** {free[:4]} GiB

**Served Chats:** {served_chats} 
**Served Users:** {served_users} 
**Blocked Users:** {blocked} 
**Sudo Users:** {sudoers} 

**Mongo Uptime:** {mongouptime[:4]} Days
**Total DB Size:** {datasize[:6]} Mb
**Total DB Storage:** {storage} Mb
**Total DB Collections:** {collections}
**Total DB Keys:** {objects}
**Total DB Queries:** `{query}`
**Total Bot Queries:** `{total_queries} `
    """
    med = InputMediaPhoto(media=config.STATS_IMG_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(
            media=med, reply_markup=upl
        )
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(
            photo=config.STATS_IMG_URL, caption=text, reply_markup=upl
        )


@app.on_callback_query(
    filters.regex(pattern=r"^(TOPMARKUPGET|GETSTATS|GlobalStats)$")
    & ~BANNED_USERS
)
@languageCB
async def back_buttons(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    command = CallbackQuery.matches[0].group(1)
    if command == "TOPMARKUPGET":
        upl = top_ten_stats_markup(_)
        med = InputMediaPhoto(
            media=config.GLOBAL_IMG_URL,
            caption=_["gstats_9"],
        )
        try:
            await CallbackQuery.edit_message_media(
                media=med, reply_markup=upl
            )
        except MessageIdInvalid:
            await CallbackQuery.message.reply_photo(
                photo=config.GLOBAL_IMG_URL,
                caption=_["gstats_9"],
                reply_markup=upl,
            )
    if command == "GlobalStats":
        upl = get_stats_markup(
            _,
            True if CallbackQuery.from_user.id in SUDOERS else False,
        )
        med = InputMediaPhoto(
            media=config.GLOBAL_IMG_URL,
            caption=_["gstats_10"].format(config.MUSIC_BOT_NAME),
        )
        try:
            await CallbackQuery.edit_message_media(
                media=med, reply_markup=upl
            )
        except MessageIdInvalid:
            await CallbackQuery.message.reply_photo(
                photo=config.GLOBAL_IMG_URL,
                caption=_["gstats_10"].format(config.MUSIC_BOT_NAME),
                reply_markup=upl,
            )
    if command == "GETSTATS":
        upl = stats_buttons(
            _,
            True if CallbackQuery.from_user.id in SUDOERS else False,
        )
        med = InputMediaPhoto(
            media=config.STATS_IMG_URL,
            caption=_["gstats_11"].format(config.MUSIC_BOT_NAME),
        )
        try:
            await CallbackQuery.edit_message_media(
                media=med, reply_markup=upl
            )
        except MessageIdInvalid:
            await CallbackQuery.message.reply_photo(
                photo=config.STATS_IMG_URL,
                caption=_["gstats_11"].format(config.MUSIC_BOT_NAME),
                reply_markup=upl,
            )

@Client.on_message(filters.command(["《قسم الحساب المساعد》"], "") & filters.private)
async def helpercn(client, message):
   userbot = await get_client(1)
   me = await userbot.get_me()
   i = f"@{me.username} : {me.id}" if me.username else me.id
   b = await client.get_chat(me.id)
   b = b.bio if b.bio else "لا يوجد بايو"
   kep = ReplyKeyboardMarkup([["فحص المساعد 🎗️"], ["تغير الاسم الاول 🪧", "تغير الاسم التاني 📝"], ["تغير البايو 🔖"], ["تغير اسم المستخدم 🔰"], ["اضافه صوره 🖼️", "• ازاله صوره •"], ["رجوع"], ["《الغاء》"]], resize_keyboard=True)
   await message.reply_text(f"**أهلا بك عزيزي المطور **\n**هنا قسم الحساب المساعد **\n**{me.mention}**\n**{i}**\n**{b}**", reply_markup=kep)
   
@Client.on_message(filters.command(["《قسم الاذاعه》"], "") & filters.private)
async def cast(client: Client, message):
    kep = ReplyKeyboardMarkup([["《اذاعة》", "《اذاعة بالتثبيت》"], ["《اذاعة بالتوجيه》"], ["《اذاعة بالمجموعات》", "《اذاعة بالتثبيت بالمجموعات》"], ["رجوع"], ["《الغاء》"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الاذاعه تحكم بالازار**", reply_markup=kep)

@Client.on_message(filters.command(["《قسم الادمنيه》"], "") & filters.private)
async def cast(client: Client, message):
    kep = ReplyKeyboardMarkup([["رفع ادمن", "تنزيل ادمن"], ["قائمه الأدمنيه"], ["رجوع"], ["《الغاء》"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الادمنيه تحكم بالازار**", reply_markup=kep)

@Client.on_message(filters.command(["《قسم الاشتراك الاجباري》"], "") & filters.private)
async def cast(client: Client, message):
    kep = ReplyKeyboardMarkup([["《تفعيل الاشتراك》", "《تعطيل الاشتراك》"], ["《ضع قناة الاشتراك》", "《حذف قناة الاشتراك》"], ["《قناة الاشتراك》"], ["رجوع"], ["《الغاء》"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا • قسم الاشتراك الاجباري • تحكم بالازار**", reply_markup=kep)

@Client.on_message(filters.command(["《قسم النسخه الاحتياطيه》"], "") & filters.private)
async def cast(client: Client, message):
    kep = ReplyKeyboardMarkup([["الأدمنية", "الجروبات"], ["المستخدمين"], ["رجوع"], ["《الغاء》"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا • قسم النسخه الاحتياطيه •  تحكم بالازار**", reply_markup=kep)
    
@Client.on_message(filters.command(["《قسم السورس》"], "") & filters.private)
async def cast(client: Client, message):
    kep = ReplyKeyboardMarkup([["《مطور السورس》", "《السورس》"], ["《جروب السورس》"], ["رجوع"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا • قسم النسخه الاحتياطيه •  تحكم بالازار**", reply_markup=kep)
        
@Client.on_message(filters.command(["《الاحصائيات والتواصل》"], "") & filters.private)
async def cast(client: Client, message):
    kep = ReplyKeyboardMarkup([["《الاحصائيات》"], ["《تفعيل التواصل》", "《تعطيل التواصل》"], ["رجوع"], ["《الغاء》"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم • الاحصائيات • تحكم بالازار**", reply_markup=kep)
    
@Client.on_message(filters.command(["《قسم الكولات》"], "") & filters.private)
async def cast(client: Client, message):
    kep = ReplyKeyboardMarkup([["الكولات النشطه 🗣️⁩"], ["الفيديوهات النشطه 📢"], ["رجوع"], ["《الغاء》"]], resize_keyboard=True)
    await message.reply_text("**أهلا بك عزيزي المطور **\n**هنا قسم الكولات تحكم بالازار**", reply_markup=kep)
    
@Client.on_message(filters.command(["اذاعه عام ♻️⁩"], "") & SUDOERS)
async def loooo(client: Client, message):
     name = await client.ask(message.chat.id, "• ارسل الان الاذاعه •")
     text = name.text
     await name.reply_text("جاري بدا الاذاعه انتظر بعض الوقت")
     chats = await get_served_chats()
     users = await get_served_users()
     chat = []
     dn = 0
     fd = 0
     for user in users:
         chat.append(int(user["user_id"]))
     for c in chats:
         chat.append(int(c["chat_id"]))
     for i in chat:
         try:
           m = await client.send_message(chat_id=i, text=text)
           dn += 1
         except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
         except Exception as e:
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت الاذاعه بنجاح .✅**\n\n**تمت الاذاعه الي : {dn}**\n**وفشل : {fd}**")

@Client.on_message(filters.command(["توجيه عام 📊"], "") & SUDOERS)
async def looooooo(client: Client, message):
     name = await client.ask(message.chat.id, "• ارسل الان التوجيه •")
     text = name.text
     await name.reply_text("جاري بدا الاذاعه انتظر بعض الوقت")
     chats = await get_served_chats()
     users = await get_served_users()
     chat = []
     dn = 0
     fd = 0
     for user in users:
         chat.append(int(user["user_id"]))
     for c in chats:
         chat.append(int(c["chat_id"]))
     for i in chat:
         try:
           m = await client.forward_messages(i, message.chat.id, name.message_id)
           dn += 1
         except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 200:
                        continue
                    await asyncio.sleep(flood_time)
         except Exception as e:
                    fd += 1
                    continue
     return await message.reply_text(f"**تمت التوجيه بنجاح .✅**\n\n**تمت التوجيه الي : {dn}**\n**وفشل : {fd}**")

@Client.on_message(filters.command("فحص المساعد 🎗️", "") & SUDOERS)
async def userrrrr(client: Client, message):
    mm = await message.reply_text("Collecting stats")
    start = datetime.now()
    u = 0
    g = 0
    sg = 0
    c = 0
    b = 0
    a_chat = 0
    client = await get_client(1)
    Meh=await client.get_me()
    usere = Meh.username
    group = ["supergroup", "group"]
    async for dialog in client.get_dialogs():
        if dialog.chat.type == "private":
            u += 1
        elif dialog.chat.type == "bot":
            b += 1
        elif dialog.chat.type == "group":
            g += 1
        elif dialog.chat.type == "supergroup":
            sg += 1
            user_s = await dialog.chat.get_member(int(Meh.id))
            if user_s.status in ("creator", "administrator"):
                a_chat += 1
        elif dialog.chat.type == "channel":
            c += 1

    end = datetime.now()
    ms = (end - start).seconds
    await mm.edit_text(
        """**ꜱᴛᴀᴛꜱ ꜰᴇᴀᴛᴄʜᴇᴅ ɪɴ {} ꜱᴇᴄᴏɴᴅꜱ ✅**
✅**ʏᴏᴜ ʜᴀᴠᴇ {} ᴘʀɪᴠᴀᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ɢʀᴏᴜᴘꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ꜱᴜᴘᴇʀ ɢʀᴏᴜᴘꜱ.**
🏷️**ʏᴏᴜ ʜᴀᴠᴇ ᴊᴏɪɴᴇᴅ {} ᴄʜᴀɴɴᴇʟꜱ.**
🏷️**ʏᴏᴜ ᴀʀᴇ ᴀᴅᴍɪɴꜱ ɪɴ {} ᴄʜᴀᴛꜱ.**
🏷️**ʙᴏᴛꜱ ɪɴ ʏᴏᴜʀ ᴘʀɪᴠᴀᴛᴇ = {}**
⚠️**ꜰᴇᴀᴛᴄʜᴇᴅ ʙʏ ᴜꜱɪɴɢ @{} **""".format(
            ms, u, g, sg, c, a_chat, b, usere
        )
    )
    
@Client.on_message(filters.command(["تغير الاسم الاول 🪧", "الاسم الاول"], "") & SUDOERS)
async def changefisrt(client: Client, message):
   try:
    if message.text == "تغير الاسم الاول 🪧":
      return await message.reply_text("• الان قم بالرد علي الاسم الجديد باستخدام كلمه الاسم الاول •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.update_profile(first_name=name)
    await message.reply_text("**تم تغير اسم الحساب المساعد بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الاسم")


@Client.on_message(filters.command(["تغير الاسم التاني 📝", "الاسم التاني"], "") & SUDOERS)
async def changelast(client: Client, message):
   try:
    if message.text == "تغير الاسم التاني 📝":
      return await message.reply_text("• الان قم بالرد علي الاسم الجديد باستخدام كلمه الاسم التاني •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.update_profile(last_name=name)
    await message.reply_text("**تم تغير اسم الحساب المساعد بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الاسم ")


@Client.on_message(filters.command(["تغير البايو 🔖", "البايو الجديد"], "") & SUDOERS)
async def changebio(client: Client, message):
   try:
    if message.text == "تغير البايو 🔖":
      return await message.reply_text("• الان قم بالرد علي البايو الجديد باستخدام كلمة البايو الجديد •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.update_profile(bio=name)
    await message.reply_text("**تم تغير البايو بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير البايو ")


@Client.on_message(filters.command(["تغير اسم المستخدم 🔰", "اليوزر"], "") & SUDOERS)
async def changeusername(client: Client, message):
   try:
    if message.text == "تغير اسم المستخدم 🔰":
      return await message.reply_text("• الان قم بالرد علي اليوزر الجديد بدون علامة @ باستخدام كلمه اليوزر •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.set_username(name)
    await message.reply_text("**تم تغير اسم المستخدم بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير اسم المستخدم")


@Client.on_message(filters.command(["اضافه صوره 🖼️", "الصوره الجديده"], "") & SUDOERS)
async def changephoto(client: Client, message):
   try:
    if message.text == "اضافه صوره 🖼️":
      return await message.reply_text("• الان قم بالرد علي الصورة الجديدة بكلمه الصوره الجديده •")
    m = message.reply_to_message
    photo = await m.download()
    client = await get_client(1)
    await client.set_profile_photo(photo=photo)
    await message.reply_text("**تم تغير صوره الحساب المساعد بنجاح .✅**") 
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الصوره")

@Client.on_message(filters.command(["• ازاله صوره •"], "") & SUDOERS)
async def changephotos(client: Client, message):
       try:
        client = await get_client(1)
        photos = await client.get_profile_photos("me")
        await client.delete_profile_photos([p.file_id for p in photos[1:]])
        await message.reply_text("**تم ازاله صوره بنجاح .✅**")
       except Exception as es:
         await message.reply_text(f" حدث خطأ أثناء ازاله الصوره")

@Client.on_message(filters.command(["《تنظيف》"], "") & SUDOERS)
async def clean(client: Client, message):
    try:
        await message.delete()
    except:
        pass
    downloads = os.path.realpath("downloads")
    down_dir = os.listdir(downloads)
    pth = os.path.realpath(".")
    os_dir = os.listdir(pth)

    if down_dir:
        for file in down_dir:
            os.remove(os.path.join(downloads, file))
    if os_dir:
        for lel in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg *.png")
    await message.reply_text("» ᴀʟʟ ᴛᴇᴍᴘ ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴄʟᴇᴀɴᴇᴅ.")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⇆ ʀᴜɴɴɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴩᴇᴇᴅᴛᴇsᴛ...**")
        test.download()
        m = m.edit("**⇆ ʀᴜɴɴɪɴɢ ᴜᴩʟᴏᴀᴅ sᴩᴇᴇᴅᴛᴇsᴛ...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ sʜᴀʀɪɴɢ sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs...**")
    except Exception as e:
        return m.edit(e)
    return result


@Client.on_message(filters.command(["《فحص سرعه البوت》"], "") & SUDOERS)
async def spedtest(client: Client, message):
    m = await message.reply_text("**» ʀᴜɴɴɪɴɢ sᴩᴇᴇᴅᴛᴇsᴛ...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ **sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs** ✯
    
<u>**❥͜͡ᴄʟɪᴇɴᴛ :**</u>
**» __ɪsᴩ :__** {result['client']['isp']}
**» __ᴄᴏᴜɴᴛʀʏ :__** {result['client']['country']}
  
<u>**❥͜͡sᴇʀᴠᴇʀ :**</u>
**» __ɴᴀᴍᴇ :__** {result['server']['name']}
**» __ᴄᴏᴜɴᴛʀʏ :__** {result['server']['country']}, {result['server']['cc']}
**» __sᴩᴏɴsᴏʀ :__** {result['server']['sponsor']}
**» __ʟᴀᴛᴇɴᴄʏ :__** {result['server']['latency']}  
**» __ᴩɪɴɢ :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()


@Client.on_message(filters.command(["《معلومات السيرفر》"], "") & SUDOERS)
async def serverinfoo(client: Client, message):
    sysrep = await message.reply_text(
        f"ɢᴇᴛᴛɪɴɢ {MUSIC_BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs, ɪᴛ'ʟʟ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ..."
    )
    try:
        await message.delete()
    except:
        pass
    sudoers = len(SUDOERS)
    mod = len(ALL_MODULES)
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(socket.gethostname())
    architecture = platform.machine()
    processor = platform.processor()
    mac_address = ":".join(re.findall("..", "%012x" % uuid.getnode()))
    sp = platform.system()
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " ɢʙ"
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}ɢʜᴢ"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}ᴍʜᴢ"
    except:
        cpu_freq = "ғᴀɪʟᴇᴅ ᴛᴏ ғᴇᴛᴄʜ"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    platform_release = platform.release()
    platform_version = platform.version()

    await sysrep.edit_text(
        f"""
➻ <u>**{MUSIC_BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs**</u>

**ᴩʏᴛʜᴏɴ :** {pyver.split()[0]}
**ᴩʏʀᴏɢʀᴀᴍ :** {pyrover}
**ᴩʏ-ᴛɢᴄᴀʟʟs :** {pytgver}
**sᴜᴅᴏᴇʀs :** `{sudoers}`
**ᴍᴏᴅᴜʟᴇs :** `{mod}`

**ɪᴘ :** {ip_address}
**ᴍᴀᴄ :** {mac_address}
**ʜᴏsᴛɴᴀᴍᴇ :** {hostname}
**ᴘʟᴀᴛғᴏʀᴍ :** {sp}
**ᴘʀᴏᴄᴇssᴏʀ :** {processor}
**ᴀʀᴄʜɪᴛᴇᴄᴛᴜʀᴇ :** {architecture}
**ᴘʟᴀᴛғᴏʀᴍ ʀᴇʟᴇᴀsᴇ :** {platform_release}
**ᴘʟᴀᴛғᴏʀᴍ ᴠᴇʀsɪᴏɴ :** {platform_version}

        <b><u>sᴛᴏʀᴀɢᴇ</b><u/>
**ᴀᴠᴀɪʟᴀʙʟᴇ :** {total[:4]} ɢɪʙ
**ᴜsᴇᴅ :** {used[:4]} ɢɪʙ
**ғʀᴇᴇ :** {free[:4]} ɢɪʙ

**ʀᴀᴍ :** {ram}
**ᴩʜʏsɪᴄᴀʟ ᴄᴏʀᴇs :** {p_core}
**ᴛᴏᴛᴀʟ ᴄᴏʀᴇs :** {t_core}
**ᴄᴩᴜ ғʀᴇǫᴜᴇɴᴄʏ :** {cpu_freq}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ᴄʟᴏsᴇ",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        ),
    )


@Client.on_message(filters.command(["《قفل الكيبورد🔒》"], "") & SUDOERS)
async def keplook(client: Client, message):
          m = await message.reply("**- تم اخفاء الازرار بنجاح\n- لو تبي تطلعها مرة ثانية اكتب /caesar**", reply_markup= ReplyKeyboardRemove(selective=True))
          
 
