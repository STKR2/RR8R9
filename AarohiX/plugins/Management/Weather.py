from pyrogram import Client, filters
from AarohiX import app

@app.on_message(filters.command("weather"))
def weather(client, message):
    try:
        user_input = message.command[1]
        location = user_input.strip()
        weather_url = f"https://wttr.in/{location}.png"
        
        message.reply_photo(photo=weather_url, caption="Here's the weather for your location")
    except IndexError:
        message.reply_text("Please provide a location. Use /weather NEW YORK")
