from pyrogram import Client, filters
import pycountry
from AarohiX import app

@app.on_message(filters.command("get_states"))
def get_states(client, message):
    try:
        country_name = message.text.split(' ', 1)[1]
        country = pycountry.countries.get(name=country_name)
        states = pycountry.subdivisions.get(country_code=country.alpha_2)
        states_list = [state.name for state in states]
        states_message = f"States of {country_name}:\n" + "\n".join(states_list)
    except IndexError:
        states_message = "Please provide a country name after the command, like this:\n/get_states Canada"
    except AttributeError:
        states_message = f"I couldn't find the country '{country_name}'. Please make sure it's spelled correctly."
    
    message.reply_text(states_message)
