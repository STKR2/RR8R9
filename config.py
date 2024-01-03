import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", ""))

API_HASH = getenv("API_HASH", "")

BOT_TOKEN = getenv("BOT_TOKEN", "")

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", ""))

OWNER_ID = int(getenv("OWNER_ID", "2107529793"))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/stkeditz/AAROHIxMUSICv2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/LOVE_FEELINGS_WILL1")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/LOVE_FEELINGS_WILL1")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION", "")
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
    "START_IMG_URL", "https://graph.org/file/0e425ef0c356dfc82392d.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/f16f757fe9c10f81b67ef.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/e68f585a0a2e4e5dc1164.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/4a7c28726502e24ea0fe0.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/810f874873e1565cf5732.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/16d7dd76f4ce8b8b01fdf.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/53f1a295e172d39eaa39d.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/5d90c3bc7f0d229194a9f.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/5d90c3bc7f0d229194a9f.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/5d90c3bc7f0d229194a9f.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


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
