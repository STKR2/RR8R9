from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from AarohiX import app

from AarohiX.misc import SUDOERS
from AarohiX.utils.database import add_sudo, remove_sudo
from AarohiX.utils.decorators.language import language
from AarohiX.utils.extraction import extract_user
from AarohiX.utils.inline import close_markup
from config import BANNED_USERS, OWNER_ID


@app.on_message(filters.command(["addsudo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id in SUDOERS:
        return await message.reply_text(_["sudo_1"].format(user.mention))
    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(_["sudo_2"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(filters.command(["delsudo", "rmsudo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id not in SUDOERS:
        return await message.reply_text(_["sudo_3"].format(user.mention))
    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(_["sudo_4"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])



GAMDOP = "https://telegra.ph/file/96d4950c132ab4326559b.jpg"

@app.on_message(filters.command(["sudolist", "listsudo", "sudoers"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
async def sudoers_list(client, message: Message):
    keyboard = [[InlineKeyboardButton(" sᴜᴅᴏʟɪsᴛ ", callback_data="check_sudo_list")]]
    reply_markups = InlineKeyboardMarkup(keyboard)
    await message.reply_photo(photo=GAMDOP, caption="➤ ᴄʜᴇᴄᴋ ᴛᴏ sᴇᴇɴ ᴛʜᴇ ᴍᴀɢɪᴄ ʙʟɪɴɢ ʙʟɪɴɢ ✨.\n\n <u><b>ɴᴏᴛᴇ:</b></u> ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴠɪᴇᴡ.\n\nᴍᴀᴅᴇ ᴡɪᴛʜ 🖤 ʙʏ <a href=\"https://t.me/dil_sagar_121\">ᴅɪʟ❣️</a> ", reply_markup=reply_markups)


@app.on_callback_query(filters.regex("^check_sudo_list$"))
async def check_sudo_list(client, callback_query: CallbackQuery):
    keyboard = []
    if callback_query.from_user.id not in SUDOERS:
        return await callback_query.answer("➤ ʙʜᴏsᴀᴅɪᴋᴇ sᴜᴅᴏ ᴅᴇᴋʜɴᴇɢᴇ ɢᴀᴀɴᴅ ᴍᴇ ᴍᴏᴛᴀ ʟᴜɴᴅ ᴅᴀᴀʟ ᴅᴏᴏɴɢᴀ😂", show_alert=True)
    else:
        user = await app.get_users(OWNER_ID)

        user_mention = (user.first_name if not user.mention else user.mention)
        caption = f"<u><b>🥀 ᴏᴡɴᴇʀ :</b></u>\n ‣ {user_mention}\n\n"
        sudo_users_caption = "<u><b>✨ sᴜᴅᴏ ᴜsᴇʀs :</b></u>\n"

        keyboard.append([InlineKeyboardButton(" ᴏᴡɴᴇʀ ", url=f"tg://openmessage?user_id={OWNER_ID}")])
        keyboard.append([InlineKeyboardButton("« ᴄʟᴏsᴇ »",callback_data="close_data")])
        
        count = 1
        for user_id in SUDOERS:
            if user_id != OWNER_ID:
                try:
                    user = await app.get_users(user_id)
                    user_mention = user.mention if user else f"{count} ɪᴅ: {user_id}"
                    sudo_users_caption += f"{count} ➤ {user_mention}\n"
                 #   button_text = f" sᴜᴅᴏ {count}"
                 #   keyboard.append([InlineKeyboardButton(button_text, url=f"tg://openmessage?user_id={user_id}")])
               #     count += 1
                except:
                    continue

        if keyboard:
            reply_markup = InlineKeyboardMarkup(keyboard)
            caption += sudo_users_caption  # Append sudo users' caption
            await callback_query.message.edit_caption(caption=caption, reply_markup=reply_markup)
