from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery,InlineKeyboardMarkup as Keyboard, InlineKeyboardButton as Button 
from Bot.funcs import read, write
import pyrogram, os

# @BENN_DEV & @BENfiles
users_db = "strings/users.json"
channels_db = "strings/channels.json"
banned_db = "strings/banned.json"
admins_db = "strings/admins.json"
others_db = "strings/others.json"
users = read(users_db)
admins = read(admins_db)
others = read(others_db)
channels = read(channels_db)
banned = read(banned_db)


@Client.on_message(filters.command("admin") & filters.private)
async def admin(client: Client, message: Message):
    user_id = message.from_user.id
    if user_id not in admins:
        await message.reply_text(
            "هذا الأمر يخص المشرفين"
        )
        return # @BENN_DEV & @BENfiles
    markup = Keyboard(keyboard())
    info = await client.get_chat (user_id)
    admin_name = info.first_name
    caption = f"-> مرحبا عزيزي الأدمن ( `{admin_name}` )\n\n-> احصائيات: \n-> الأعضاء : {len(users)}\n-> المحظورين : {len(banned)}\n\n-> أوامر أخرى : \n- حظر + الأيدي\n- رفع حظر + الأيدي\n- رفع ادمن + الأيدي\n- تنزيل ادمن + الأيدي"
    await message.reply_text(
        caption,
        reply_markup=markup
    )
    # @BENN_DEV & @BENfiles

@Client.on_message(filters.regex(r"^(حظر)") & filters.private)
async def ban(client: Client, message: Message):
    user_id = message.from_user.id
    if user_id not in admins:
        await message.reply_text(
            "هذا الأمر يخص المشرفين"
        )
        return
    member = message.text.split()[-1]
    if int(member) in admins:
        await message.reply_text(
            "لا يمكنك حظر هذا المستخدم."
        )
        return
    if int(member) in banned:
        await message.reply_text(
            "تم حظر هذا المستخدم من قبل."
        )
        return
    banned.append(int(member))
    write(banned_db, banned)
    await message.reply_text(
        "تم حظر هذا المستخدم"
    )
    # @BENN_DEV & @BENfiles

@Client.on_message(filters.regex(r"^(رفع حظر)") & filters.private)
async def unban(client: Client, message: Message):
    user_id = message.from_user.id
    if user_id not in admins:
        await message.reply_text(
            "هذا الأمر يخص المشرفين"
        )
        return
    member = message.text.split()[-1]
    if int(member) in banned:
        banned.remove(int(member))
        write(banned_db, banned)
        await message.reply_text(
            "تم رفع الحظر عن هذا المستخدم."
        )
        return # @BENN_DEV & @BENfiles
    await message.reply_text(
        "لم يتم حظر هذا المستخدم من قبل."
    )
    

@Client.on_message(filters.regex(r"^(رفع ادمن)") & filters.private)
async def ban(client: Client, message: Message):
    user_id = message.from_user.id
    if user_id not in admins:
        await message.reply_text(
            "هذا الأمر يخص المشرفين"
        )
        return
    member = message.text.split()[-1]
    if int(member) in admins:
        await message.reply_text(
            "هذا المستخدم مشرف بالفعل."
        )
        return
    if int(member) in banned:
        await message.reply_text(
            "هذا المستخدم تم حظره من قبل يرجى رفع الحظر ثم إعادة المحاوله."
        )
        return
    admins.append(int(member))
    write(admins_db, admins)
    await message.reply_text(
        "تم ترقية المستخدم لرتبة مشرف"
    )
    
    
@Client.on_message(filters.regex(r"^(تنزيل ادمن)") & filters.private)
async def ban(client: Client, message: Message):
    user_id = message.from_user.id
    if user_id not in admins:
        await message.reply_text( # @BENN_DEV & @BENfiles
            "هذا الأمر يخص المشرفين"
        )
        return
    member = message.text.split()[-1]
    if int(member) in admins:
        admins.remove(int(member))
        write(admins_db, admins)
        await message.reply_text(
            "تم تنزيل هذا المستخدم من قائمة المشرفين."
        )
        return
    await message.reply_text(
        "هذا المستخدم ليس من المشرفين."
    )


@Client.on_callback_query(filters.regex(r"^(forward_from_users)$|^(new_members_notice)$"))
async def redefine(client: Client, callback: CallbackQuery):
    data = callback.data
    others["options"][data] = True if not others["options"][data] else False
    write(others_db, others)
    await client.edit_message_reply_markup(
        chat_id=callback.message.chat.id,
        message_id=callback.message.id,# @BENN_DEV & @BENfiles
        reply_markup=Keyboard(keyboard())
    )


@Client.on_callback_query(filters.regex(r"^(add_channel)$"))
async def add_channel(client: Client, callback: CallbackQuery):
    response = await callback.message.chat.ask("أرسل معرف القناه مع مبدوء ب @", filters.regex(r"^(@)"))
    channel = response.text
    try:
        await client.get_chat(channel)
    except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
        await response.reply_text(
            "لم يتم إيجاد هذه الدردشه."
        )
        return
    if channel in channels:
        await response.reply_text(
            "القناه موجوده بالفعل."
        )
        return
    channels.append(channel)
    write(channels_db, channels)
    await response.reply_text(
        "تمت إضافة القناه."
    )


@Client.on_callback_query(filters.regex(r"^(remove_channel)$"))
async def remove_channel(client: Client, callback: CallbackQuery):
    response = await callback.message.chat.ask("أرسل معرف القناه مع مبدوء ب @", filters.regex(r"^(@)"))
    channel = response.text
    if channel not in channels:
        await response.reply_text(
            "لم يتم إيجاد هذه الدردشه."
        )
        return
    channels.remove(channel)
    write(channels_db, channels)
    await response.reply_text(
        "تم حذف القناه."
    )


@Client.on_callback_query(filters.regex(r"^(current_channels)$"))
async def current_channels(client: Client, callback: CallbackQuery):
    caption = "- القنوات الحاليه :\n"
    text = "\n".join(channels)
    caption+=text
    await client.answer_callback_query(callback_query_id=callback.id , text = caption, show_alert=True)


@Client.on_callback_query(filters.regex(r"^(send_storage)$"))
async def send_storage(client: Client, callback: CallbackQuery):
    files_path = "Bot/database"
    files = os.listdir(files_path)
    for file in files:
        file_path = os.path.join(files_path, file)
        await client.send_document(
            callback.message.chat.id,
            document=file_path
        )# @BENN_DEV & @BENfiles

def keyboard():
    keys = [
    [
        Button(
            "- التوجيه من الأعضاء ✅️ -" if others.get("options")["forward_from_users"] else "- التوجيه من الأعضاء ❌️ -",
             callback_data="forward_from_users"), # DONE
        Button(
            "- تنبيه الأعضاء الجدد ✅️ -" if others.get("options")["new_members_notice"] else "- تنبيه الأعضاء الجدد ❌️ -", 
            callback_data="new_members_notice") # DONE
    ],
    [
        Button("- إضافة قناه -", callback_data="add_channel"), # DONE
        Button("- عرض القنوات الحاليه -", callback_data="current_channels"), # DONE
        Button("- حذف قناه -", callback_data="remove_channel") # DONE
    ],
    [
        Button("- التخزين -", callback_data="send_storage") # DONE
    ]
    ]
    return keys
