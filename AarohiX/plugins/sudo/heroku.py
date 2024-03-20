

import asyncio
import math
import os
import shutil
import socket
from datetime import datetime

import dotenv
import heroku3
import requests
import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from pyrogram import filters
from strings.filters import command
import config 
from AarohiX import app
from AarohiX.misc import HAPP, SUDOERS, XCB
from AarohiX.utils.database import (get_active_chats,
                                       remove_active_chat,
                                       remove_active_video_chat)
from AarohiX.utils.decorators.language import language
from AarohiX.utils.pastebin import DilBin


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def is_heroku():
    return "heroku" in socket.getfqdn()




@app.on_message(command(["الداينو", "‹ الداينو ›"]) & (OWNER_ID))
@language
async def usage_dynos(client, message, _):
    ### Credits CatUserbot
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(_["heroku_1"])
    else:
        return await message.reply_text(_["heroku_11"])
    dyno = await message.reply_text(_["heroku_12"])
    Heroku = heroku3.from_key(config.HEROKU_API_KEY)
    account_id = Heroku.account().id
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {config.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + account_id + "/actions/get-quota"
    r = requests.get("https://api.heroku.com" + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("Unable to fetch.")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    text = f"""
**~ مرحبا عزيزي المطور **
~ هذا هو استخدامك :
~ الرام المستخدم :`{AppHours}`**ساعة**  `{AppMinutes}`**دقيقة**  [`{AppPercentage}`**%**]
~ المتبقي في حسابك:
~ الإجمالي : `{hours}`**ساعة**  `{minutes}`**دقيقة**  [`{percentage}`**%**]"""
    return await dyno.edit(text)


@app.on_message(command(["‹ تحديث السورس ›", "تحديث السورس"]) & OWNER_ID)
@language
async def update_(client, message, _):
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(_["heroku_1"])
    response = await message.reply_text(_["heroku_13"])
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit(_["heroku_14"])
    except InvalidGitRepositoryError:
        return await response.edit(_["heroku_15"])
    to_exc = f"git fetch origin {config.UPSTREAM_BRANCH} &> /dev/null"
    os.system(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[
        0
    ]  # main git repository
    for checks in repo.iter_commits(
        f"HEAD..origin/{config.UPSTREAM_BRANCH}"
    ):
        verification = str(checks.count())
    if verification == "":
        return await response.edit("~ عزيزي المطور السورس احدث اصدار .")
    updates = ""
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[
            (format // 10 % 10 != 1)
            * (format % 10 < 4)
            * format
            % 10 :: 4
        ],
    )
    for info in repo.iter_commits(
        f"HEAD..origin/{config.UPSTREAM_BRANCH}"
    ):
        updates += f"<b>~ #{info.count()}: [{info.summary}]({REPO_}/commit/{info})~ الملفات -> {info.author}</b>\n\t\t\t\t<b>~ تاريخ إصدار التحديث :</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
    _update_response_ = "~ تم اصدار التحديث !</b>\n~ السورس ~ جاري التنزيل</code>\n<u>التحديثات :</u>\n\n"
    _final_updates_ = _update_response_ + updates
    if len(_final_updates_) > 4096:
        url = await DilBin(updates)
        nrs = await response.edit(
            f"~ تم اصدار التحديث .\n\n~ على سورس فريدوم  </code>\n\n**<u>• الاضافات :</u>**\n\n[اضغط هنا]({url})"
        )
    else:
        nrs = await response.edit(
            _final_updates_, disable_web_page_preview=True
        )
    os.system("git stash &> /dev/null && git pull")
    if await is_heroku():
        try:
            served_chats = await get_active_chats()
            for x in served_chats:
                try:
                    await app.send_message(
                        x,
                        f"~ تم اعادة التشغيل .",
                    )
                    await remove_active_chat(x)
                    await remove_active_video_chat(x)
                except Exception:
                    pass
            await response.edit(
                f"{nrs.text}\n\n~ تم إعادة التشغيل ، n\~ جاري رفع الملفات على البوت الخاص بك .!"
            )
            os.system(
                f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0]*2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
            )
            return
        except Exception as err:
            await response.edit(
                f"{nrs.text}\n\n~ حدث خطا ."
            )
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"AN EXCEPTION OCCURRED AT #UPDATER DUE TO: <code>{err}</code>",
            )
    else:
        served_chats = await get_active_chats()
        for x in served_chats:
            try:
                await app.send_message(
                    x,
                    f"~ لقد قمت باعادة التشغيل انتضر وقت اخر .",
                )
                await remove_active_chat(x)
                await remove_active_video_chat(x)
            except Exception:
                pass
        await response.edit(
            f"{nrs.text}\n\n~ تم اعادة تشغيل البوت !"
        )
        os.system("pip3 install -r requirements.txt")
        os.system(f"kill -9 {os.getpid()} && bash start.sh")
        exit()


@app.on_message(command(["اعادة تشغيل", "‹ اعادة تشغيل البوت ›"]) & SUDOERS)
async def restart_(_, message):
    response = await message.reply_text("~ جاري اعادة تشغيل .")
    served_chats = await get_active_chats()
    for x in served_chats:
        try:
            await app.send_message(
                x,
                f" ~ تم اعادة تشغيل البوت الان حاول لاحقاً .",
            )
            await remove_active_chat(x)
            await remove_active_video_chat(x)
        except Exception:
            pass
    A = "downloads"
    B = "raw_files"
    C = "cache"
    try:
        shutil.rmtree(A)
        shutil.rmtree(B)
        shutil.rmtree(C)
    except:
        pass
    await response.edit(
        "~ تم اعادة تشغيل البوت ."
    )
    os.system(f"kill -9 {os.getpid()} && bash start.sh")
