# * @author        @dil_sagar_121
# * @date          2024-01-31 12:13:32
# * @projectName   AarohiX
# * Copyright ©stkeditz All rights reserved
import os

from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters

from AarohiX import app

# dilop

COMMAND_HANDLER = "/"

# baaki Sab topi


__MODULE__ = "write"
__HELP__ = """
Command: <code>/write</code> [reply to msg or after cmd]
Desc: For those of you who are lazy to write.
"""


def text_set(text):
    lines = []
    if len(text) <= 55:
        lines.append(text)
    else:
        all_lines = text.split("\n")
        for line in all_lines:
            if len(line) <= 55:
                lines.append(line)
            else:
                k = len(line) // 55
                lines.extend(line[((z - 1) * 55) : (z * 55)] for z in range(1, k + 2))
    return lines[:25]


@app.on_message(filters.command(["handwrite"], COMMAND_HANDLER))
async def handwrite(client, message):
    if message.reply_to_message and message.reply_to_message.text:
        txt = message.reply_to_message.text
    elif len(message.command) > 1:
        txt = message.text.split(None, 1)[1]
    else:
        return await message.reply(
            "Please reply to message or write after command to use write CMD."
        )
    nan = await message.reply_text("Processing...")
    try:
        img = Image.open("AarohiX/assets/kertas.jpg")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("AarohiX/assets/assfont.ttf", 30)
        x, y = 150, 140
        lines = text_set(txt)
        line_height = font.getbbox("hg")[3]
        for line in lines:
            draw.text((x, y), line, fill=(1, 22, 55), font=font)
            y = y + line_height - 5
        file = f"write_{message.from_user.id}.jpg"
        img.save(file)
        if os.path.exists(file):
            await message.reply_photo(
                photo=file, caption=f"<b>Written By :</b> {client.me.mention}"
            )
            os.remove(file)
            await nan.delete()
    except Exception as e:
        return await message.reply(e)
