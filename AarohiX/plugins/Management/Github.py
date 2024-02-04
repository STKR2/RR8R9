import aiohttp
from pyrogram import filters
from AarohiX import app as bot

@bot.on_message(filters.command(["github", "git"]))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/git stkeditz")
        return

    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'

    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()

            try:
                url = result.get('html_url', '')
                name = result.get('name', '')
                company = result.get('company', '')
                bio = result.get('bio', '')
                created_at = result.get('created_at', '')
                avatar_url = result.get('avatar_url', '')
                blog = result.get('blog', '')
                location = result.get('location', '')
                repositories = result.get('public_repos', '')
                followers = result.get('followers', '')
                following = result.get('following', '')

                caption = f"""ɢɪᴛʜᴜʙ ɪɴғᴏ ᴏғ {name}
                
ᴜsᴇʀɴᴀᴍᴇ: {username}
ʙɪᴏ: {bio}
ʟɪɴᴋ: [Here]({url})
ᴄᴏᴍᴩᴀɴʏ: {company}
ᴄʀᴇᴀᴛᴇᴅ ᴏɴ: {created_at}
ʀᴇᴩᴏsɪᴛᴏʀɪᴇs: {repositories}
ʙʟᴏɢ: {blog}
ʟᴏᴄᴀᴛɪᴏɴ: {location}
ғᴏʟʟᴏᴡᴇʀs: {followers}
ғᴏʟʟᴏᴡɪɴɢ: {following}"""
            except Exception as e:
                print(str(e))
                pass

    await message.reply_photo(photo=avatar_url, caption=caption)
