from pyrogram import filters
from pyrogram.types import Message
from strings.filters import command
from AarohiX import app
from AarohiX.core.call import Dil
from AarohiX.utils.database import is_music_playing, music_off
from AarohiX.utils.decorators import AdminRightsCheck
from AarohiX.utils.inline import close_markup


@app.on_message(command(["مؤقتا", "cpause"]))
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Dil.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
