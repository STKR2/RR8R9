import re
import os
import asyncio
from AarohiX import app
from datetime import datetime
from AarohiX.core.userbot import assistants
from AarohiX.misc import SUDOERS, mongodb


@app.on_message(filters.command(["تغير الاسم الاول 🪧", "الاسم الاول"], "") & SUDOERS)
async def changefisrt(client: app, message):
   try:
    if message.text == "تغير الاسم الاول 🪧":
      return await message.reply_text("• الان قم بالرد علي الاسم الجديد باستخدام كلمه الاسم الاول •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.update_profile(first_name=name)
    await message.reply_text("**تم تغير اسم الحساب المساعد بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الاسم")


@app.on_message(filters.command(["تغير الاسم التاني 📝", "الاسم التاني"], "") & SUDOERS)
async def changelast(client: app, message):
   try:
    if message.text == "تغير الاسم التاني 📝":
      return await message.reply_text("• الان قم بالرد علي الاسم الجديد باستخدام كلمه الاسم التاني •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.update_profile(last_name=name)
    await message.reply_text("**تم تغير اسم الحساب المساعد بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الاسم ")


@app.on_message(filters.command(["تغير البايو 🔖", "البايو الجديد"], "") & SUDOERS)
async def changebio(client: app, message):
   try:
    if message.text == "تغير البايو 🔖":
      return await message.reply_text("• الان قم بالرد علي البايو الجديد باستخدام كلمة البايو الجديد •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.update_profile(bio=name)
    await message.reply_text("**تم تغير البايو بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير البايو ")


@app.on_message(filters.command(["تغير اسم المستخدم 🔰", "اليوزر"], "") & SUDOERS)
async def changeusername(client: app, message):
   try:
    if message.text == "تغير اسم المستخدم 🔰":
      return await message.reply_text("• الان قم بالرد علي اليوزر الجديد بدون علامة @ باستخدام كلمه اليوزر •")
    name = message.reply_to_message.text
    client = await get_client(1)
    await client.set_username(name)
    await message.reply_text("**تم تغير اسم المستخدم بنجاح .✅**")
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير اسم المستخدم")


@app.on_message(filters.command(["اضافه صوره 🖼️", "الصوره الجديده"], "") & SUDOERS)
async def changephoto(client: app, message):
   try:
    if message.text == "اضافه صوره 🖼️":
      return await message.reply_text("• الان قم بالرد علي الصورة الجديدة بكلمه الصوره الجديده •")
    m = message.reply_to_message
    photo = await m.download()
    client = await get_client(1)
    await client.set_profile_photo(photo=photo)
    await message.reply_text("**تم تغير صوره الحساب المساعد بنجاح .✅**") 
   except Exception as es:
     await message.reply_text(f" حدث خطأ أثناء تغير الصوره")

@app.on_message(filters.command(["• ازاله صوره •"], "") & SUDOERS)
async def changephotos(client: app, message):
       try:
        client = await get_client(1)
        photos = await client.get_profile_photos("me")
        await client.delete_profile_photos([p.file_id for p in photos[1:]])
        await message.reply_text("**تم ازاله صوره بنجاح .✅**")
       except Exception as es:
         await message.reply_text(f" حدث خطأ أثناء ازاله الصوره")
