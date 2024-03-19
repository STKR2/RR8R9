from pyrogram import Client, filters
from pyrogram.types import Message
from AarohiX import app
from strings.filters import command
from config import OWNER_ID

@app.on_message(command("احسب"))
def calculate_math(client, message):   
    expression = message.text.split("احسب ", 1)[1]
    
    try:        
        result = eval(expression.replace("×", "*").replace("÷", "/"))  # استبدال علامات الضرب والقسمة
        response = f"~ الناتج هو : {result}"
    except:
        response = "~ اكتب بالصيغة الصحيحة مثل: احسب 3 + 3 * 4"
        
    message.reply(response)
