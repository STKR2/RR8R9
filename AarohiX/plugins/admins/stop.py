from pyrogram import filters
from pyrogram.types import Message
from strings.filters import command
from AarohiX import app
from AarohiX.core.call import Dil
from AarohiX.utils.database import set_loop
from AarohiX.utils.decorators import AdminRightsCheck
from AarohiX.utils.inline import close_markup
from config 


@app.on_message(
    command(["ايقاف", "اوكف", "كافي", "انهاء"]) 
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Dil.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
