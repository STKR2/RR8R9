import os
from pyrogram import Client, filters
from AarohiX import app

ASSISTANT_ID = os.environ.get("ASSISTANT_ID", "5618845741")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5791601466:AAE5OMfuoPbe7xFhBC5dT9YnrAH6VabMdms")

async def get_group_chat_ids(client):
    chat_ids = []
    async for dialog in client.iterate_chat_dialogs():
        if dialog.is_group:
            chat_ids.append(dialog.chat.id)
    return chat_ids

@app.on_message(filters.command("leavegroups") & filters.user(int(ASSISTANT_ID)))
async def leave_groups_handler(client, message):
    chat_ids = await get_group_chat_ids(client)
    for chat_id in chat_ids:
        try:
            await client.leave_chat(chat_id)
            print(f"Left group with ID: {chat_id}")
        except Exception as e:
            print(f"Error leaving group with ID {chat_id}: {e}")
