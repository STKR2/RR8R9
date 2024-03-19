from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AarohiX import app
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped
from AarohiX.core.call import Aarohi 
from pytgcalls.exceptions import NoActiveGroupCall, TelegramServerError)
import config

@app.on_message(
    command(["صاعد", "الصاعدين"])
)
async def strcall(client, message):
    assistant = await group_assistant(Aarohi, message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("https://graph.org/file/217aac5f9cd2b05f7ba5a.mp4"), stream_type=StreamType().pulse_stream)
        text = "~ الصاعدين بالأتصال :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k = 0
        for participant in participants:
            info = participant
            if not info.muted:
                mut = "~ جاي يمسلت "
            else:
                mut = "~ ساد المايك "
            user = await client.get_users(participant.user_id)
            k += 1
            text += f"{k} ~ {user.mention} {mut}\n"
        text += f"\n~ عددهم : {len(participants)}\n️"  

        # إضافة زر شفاف في الأسفل
        inline_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("- قناة البوت . ", url=config.SUPPORT_CHAT)],
        ])      

        await message.reply(text, reply_markup=inline_keyboard)
        await asyncio.sleep(7)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply("- ماكو شي مشتغل")
    except TelegramServerError:
        await message.reply("- حدث خطأ.")
    except AlreadyJoinedError:
        text = "~ الصاعدين :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k = 0
        for participant in participants:
            info = participant
            if not info.muted:
                mut = "~ جاي يمسلت "
            else:
                mut = "~ ساد المايك "
            user = await client.get_users(participant.user_id)
            k += 1
            text += f"{k} ~ {user.mention} {mut}\n"
        text += f"\n~ عددهم : {len(participants)}\n️"

        # إضافة زر شفاف في الأسفل
        inline_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("- قناة البوت . ", url=config.SUPPORT_CHAT)],
        ])
        await message.reply(text, reply_markup=inline_keyboard)
