from pyrogram import Client, filters
from faker import Faker
from AarohiX import app

fake = Faker()

@app.on_message(filters.command("fakeit"))
def generate_info(client, message):
    name = fake.name()
    address = fake.address()
    country = fake.country()
    phone_number = fake.phone_number()
    email = fake.email()
    city = fake.city()
    state = fake.state()
    zipcode = fake.zipcode()

    info_message = (
        f"**Full Name:** {name}\n"
        f"**Address:** {address}\n"
        f"**Country:** {country}\n"
        f"**Phone Number:** {phone_number}\n"
        f"**Email:** {email}\n"
        f"**City:** {city}\n"
        f"**State:** {state}\n"
        f"**zipcode:** {zipcode}"
    )

    message.reply_text(info_message)
