
from pyrogram.types import Message
from AarohiX import app
from strings.filters import command
from AarohiX.core.call import Dil
from AarohiX.utils.database import *
from config import OWNER_ID
from pyrogram import Client, filters
from pyrogram.types import Message

@app.on_message(filters.voice_chat_started)
async def zoharyy(client: Client, message: Message): 
    text = f"- قام {message.from_user.mention}\n - بدعوة : "
    
    if message.voice_chat_started.members:
        for user in message.voice_chat_started.members:
            try:
                text += f"[{user.first_name}](tg://user?id={user.id}) "
            except Exception:
                pass
            
        try:
            await message.reply(text)
        except:
            pass


@app.on_message(filters.video_chat_started)
async def brah(_, msg):
       await msg.reply("‹ تم بدء المحادثة ›")


@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
       await msg.reply("**‹ تم انهاء المحادثة ›**")




@app.on_message(command("احسب", prefixes="/"))
def calculate_math(client, message):   
    expression = message.text.split("احسب ", 1)[1]
    try:        
        result = eval(expression)
        response = f"~ الناتج هو : {result}"
    except:
        response = "~ اكتب هكذا\n احسب 3 + 3 × 4 "
    message.reply(response)


@app.on_message(command(["spg"], ["/", "!", "."]))
async def search(event):
    msg = await event.respond("Searching...")
    async with aiohttp.ClientSession() as session:
        start = 1
        async with session.get(f"https://content-customsearch.googleapis.com/customsearch/v1?cx=ec8db9e1f9e41e65e&q={event.text.split()[1]}&key=AIzaSyCoT1sXlX2gKy4wc-xZmt_L10RjP7SAQds&start={start}", headers={"x-referer": "https://explorer.apis.google.com"}) as r:
            response = await r.json()
            result = ""
            
            if not response.get("items"):
                return await msg.edit("No results found!")
            for item in response["items"]:
                title = item["title"]
                link = item["link"]
                if "/s" in item["link"]:
                    link = item["link"].replace("/s", "")
                elif re.search(r'\/\d', item["link"]):
                    link = re.sub(r'\/\d', "", item["link"])
                if "?" in link:
                    link = link.split("?")[0]
                if link in result:
                    # remove duplicates
                    continue
                result += f"{title}\n{link}\n\n"
            prev_and_next_btns = [Button.inline("▶️Next▶️", data=f"next {start+10} {event.text.split()[1]}")]
            await msg.edit(result, link_preview=False, buttons=prev_and_next_btns)
            await session.close()
