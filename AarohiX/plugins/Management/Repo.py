from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AarohiX import app as bot
import requests
from config import BOT_USERNAME
from AarohiX.utils.errors import capture_err

start_txt = """**
➤ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴡᴏʀʟᴅ ᥫᩣ
 
 ⦿ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ɴ ᴠᴘs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ !
 
 ⦿ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ !
 
 ⦿ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ !
 
 ⦿ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴅᴍ ᴍᴇ !
**"""

@bot.on_message(filters.command(["repo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("⦿ ᴀᴅᴅ ᴍᴇ ⦿", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/AAROHI_SUPPORT_CHAT"),
          InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/dil_sagar_121"),
        ],
        [
          InlineKeyboardButton("ᴠ1 ᴍᴜsɪᴄ", url=f"https://github.com/stkeditz/AAROHIxMUSIC"),
          InlineKeyboardButton("︎ᴠ2 ᴍᴜsɪᴄ", url=f"https://github.com/stkeditz/AAROHIxMUSICv2"),
        ],
        [
          InlineKeyboardButton("ᴍᴀñᴀɢᴇᴍᴇɴᴛ", url=f"https://github.com/BadshahAk/AnsiRobot"),
          InlineKeyboardButton("ᴄʜᴀᴛ ʙᴏᴛ", url=f"https://github.com/stkeditz/AAROHIxCHATBOT"),
        ],
        [
          InlineKeyboardButton("sᴛʀɪɴɢ ʙᴏᴛ", url=f"https://github.com/stkeditz/AAROHIxSTRINGBOT"),
          InlineKeyboardButton("ᴅᴘᴢ sᴛᴏʀᴇ", url=f"https://t.me/dil_dpz_stocks"),
        ],
        [
          InlineKeyboardButton("ᴄᴄ ᴄʜᴀᴛ", url="https://t.me/heruko_cc"),
          InlineKeyboardButton("ᴀʟᴏɴᴇ ɢʀᴏᴜᴘ", url=f"https://t.me/LOVE_FEELINGS_WILL1"),
        ],
        [
          InlineKeyboardButton("ʟᴀᴛᴇ ɴɪɢʜᴛ︎", url=f"https://t.me/Late_Night_Chatters"),
          InlineKeyboardButton("ᴅᴜɴɪʏᴀ", url=f"https://t.me/dil_ki_duniya"),
        ],
        [
          InlineKeyboardButton("ᴅɪʟ ғᴇᴇʟɪɴɢs", url=f"https://t.me/Dil_Feelings_Will"),
          InlineKeyboardButton("ʟᴏᴠᴇ ғᴇᴇʟɪɴɢs", url=f"https://t.me/LOVE_FEELINGS_WILL_121"),
        ],
        [
          InlineKeyboardButton("ᴅɪʟ sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/alonegroup121"),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/d3e94fa78cb489c1effbd.jpg",
        caption=start_txt,
        reply_markup=reply_markup,
    )



#-------------------------------------------------------#


@bot.on_message(filters.command("repo", prefixes="@"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/stkeditz/AAROHIxMUSICv2/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[ʀᴇᴘᴏ](https://github.com/stkeditz/AAROHIxMUSICv2) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/alonegroup121)
| ᴄᴏɴᴛʀɪʙᴜᴛᴏʀs |
----------------
{list_of_users}"""
        await bot.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await bot.send_message(message.chat.id, text="Failed to fetch contributors.")

