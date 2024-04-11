import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", ""))

API_HASH = getenv("API_HASH", "")

BOT_TOKEN = getenv("BOT_TOKEN", "")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "bot")

Muntazer = getenv("muntazer", "")

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 2097152))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "20971520")
)

LOGGER_ID = int(getenv("LOGGER_ID", ""))

OWNER_ID = int(getenv("OWNER_ID", "1854384004"))

BOT_USERNAME = getenv("BOT_USERNAME" , "")

COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/STKR2/RR8R9",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Xl444")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/vvyvv6")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "50000"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 20971520000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 209715200000))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION", "AQBkY4p3iuvhDpb7EVoy9S3sEPtIgwcXupTLrYMn5fEhKKA1k2oyLDpaN_E4ft8vl46lMnOWIXIIsmtsAXjJtEHGmpsv8ONZxVlWODtImC3i-0Kklwb6vZVH348oncJiAFF-FnPiz5qqo3fJBYjeUhn6oNJ4aRB6MO6xAw5HyXfPSVnzOiMDGGKAUaMJv4nzzy1_OxNySl3eVFPicTVC1qgovq9ohY2ueAAF2zklzu3fwCnMqy2SDHEr33uXyvP2PF_K-ioZsKNQvjM5FAakjnmO0032V84ocEgRsPXcNdwALXym5u_ZAvYMTac6TnwGRM-PK8jE2Oj9w3DGU5S6uVzWAAAAAZytwEkA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg"
)
PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg"
)                          
STATS_IMG_URL = getenv(
    "STATS_IMG_URL", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg"
)                       
TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg"
)                            
TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg"
)
STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL","https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg"
)
SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg"
)
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://graph.org/file/8882cbd7cc786826d9ecb.jpg"
)
SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg"
)                                
SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg"
)                               
SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg"
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 2000**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
