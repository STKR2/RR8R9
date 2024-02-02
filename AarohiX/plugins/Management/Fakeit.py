import requests
from pyrogram import Client
from pyrogram import filters
from AarohiX import app

random_user_api_url = 'https://randomuser.me/api/'

@app.on_message(filters.command("fake", prefixes="/"))
def generate_fake_user_by_country(client, message):
    country_name = message.text.split("/fake ", maxsplit=1)[1]
    
    response = requests.get(f'{random_user_api_url}?nat={country_name}')
    
    if response.status_code == 200:
        user_info = response.json()['results'][0]
        first_name = user_info['name']['first']
        last_name = user_info['name']['last']
        email = user_info['email']
        country = user_info['location']['country']
        state = user_info['location']['state']
        city = user_info['location']['city']
        street = user_info['location']['street']['name']
        zip_code = user_info['location']['postcode']
        message.reply_text(f"**Name:** {first_name} {last_name}\n\n**Email:** {email}\n\n**Country:** {country}\n\n**State:** {state}\n\n**City:** {city}\n\n**Address:** {street}\n\n**ZIP Code:** {zip_code}")
    else:
        message.reply_text(f"Failed to generate fake user information for {country_name}.")
