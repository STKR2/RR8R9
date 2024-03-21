from pyrogram import filters
from pyrogram.types import Message
from strings.filters import command
from AarohiX import app
from AarohiX.core.call import Dil
from AarohiX.utils.database import is_music_playing, music_on
from AarohiX.utils.decorators import AdminRightsCheck
from AarohiX.utils.inline import close_markup


@app.on_message(command(["استمرار", "cresume"]))
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await Dil.resume_stream(chat_id)
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
