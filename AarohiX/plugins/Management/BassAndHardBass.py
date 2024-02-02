from pyrogram import Client, filters
from pyrogram.types import Message
from pydub import AudioSegment
import os
from AarohiX import app

@app.on_message(filters.command("bass"))
async def bass_boost_command(client, message):
    try:
        if message.reply_to_message and message.reply_to_message.audio:
            original_audio = message.reply_to_message.audio
            file_id = original_audio.file_id

            audio_path = await client.download_media(file_id)
            boosted_audio = apply_bass_boost(audio_path)

            await message.reply_audio(audio=boosted_audio)

            os.remove(audio_path)
            os.remove(boosted_audio)

        else:
            await message.reply_text("Please reply to an audio file with /bass to apply the bass boost effect.")
    except Exception as e:
        await message.reply_text("🚫")

def apply_bass_boost(audio_path):
    audio = AudioSegment.from_file(audio_path)
    boosted_audio = audio.low_pass_filter(100).high_pass_filter(30).apply_gain(10)
    boosted_audio_path = "dilboosted.mp3"
    boosted_audio.export(boosted_audio_path, format="mp3")

    return boosted_audio_path



#-----------------------------------DJ-----------------------------------#



@app.on_message(filters.command("dj"))
async def bass_boost_command(client, message):
    try:
        if message.reply_to_message and message.reply_to_message.audio:
            original_audio = message.reply_to_message.audio
            file_id = original_audio.file_id

            audio_path = await client.download_media(file_id)
            boosted_audio = apply_bass_boost(audio_path)

            await message.reply_audio(audio=boosted_audio)

            os.remove(audio_path)
            os.remove(boosted_audio)

        else:
            await message.reply_text("Please reply to an audio file with /dj to apply the hard bass boost effect.")
    except Exception as e:
        await message.reply_text("🚫")

def apply_bass_boost(audio_path):
    audio = AudioSegment.from_file(audio_path)
    boosted_audio = audio.low_pass_filter(200).high_pass_filter(70).apply_gain(30)
    boosted_audio_path = "dildj.mp3"
    boosted_audio.export(boosted_audio_path, format="mp3")

    return boosted_audio_path
