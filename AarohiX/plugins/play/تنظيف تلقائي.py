import os
import glob
import asyncio
import time
from config import OWNER_ID
from AarohiX import app
from pyrogram import Client, filters


last_cleanup_time = 0

async def delete_temp_files():
    global last_cleanup_time
    while True:
        await asyncio.sleep(7200)  # انتظر ساعتين (7200 ثانية)

        current_time = time.time()

        # إذا مرت أكثر من ساعتين من آخر عملية تنظيف
        if current_time - last_cleanup_time >= 7200:
            # حذف الملفات *.webm, *.jpg, *.png بعد ساعتين
            files_to_delete = glob.glob("*.webm") + glob.glob("*.jpg") + glob.glob("*.png")
            for file_path in files_to_delete:
                os.remove(file_path)

            last_cleanup_time = current_time
            print("تم حذف الملفات بنجاح .")

@app.on_message(filters.command(["‹ تنظيف سجلات التشغيل ›"], "") & filters.user(OWNER_ID))
async def clean(client: Client, message):
    global last_cleanup_time

    try:
        await message.delete()
    except:
        pass

    downloads = os.path.realpath("downloads")
    down_dir = os.listdir(downloads)
    pth = os.path.realpath(".")
    
    if down_dir:
        for file in down_dir:
            os.remove(os.path.join(downloads, file))

    # حذف الملفات *.webm, *.jpg, *.png عندما يتم طلب الأمر "تنظيف"
    files_to_delete = glob.glob("*.webm") + glob.glob("*.jpg") + glob.glob("*.png")
    for file_path in files_to_delete:
        os.remove(file_path)

    last_cleanup_time = time.time()
    await message.reply_text("~ تم حذف كافة الملفات .")

# بدء عملية حذف الملفات بعد ساعتين
asyncio.ensure_future(delete_temp_files())
