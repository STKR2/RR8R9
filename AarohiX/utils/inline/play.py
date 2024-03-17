
import math
from config import SUPPORT_CHAT, OWNER_ID
from pyrogram.types import InlineKeyboardButton

from AarohiX.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            )
        ],
        [
            InlineKeyboardButton(
                text="", url=f"tg://openmessage?user_id={OWNER_ID}",
            ),
            InlineKeyboardButton(
                text="「 الدعم 」", url=SUPPORT_CHAT,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="‹ استمرار ›", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="‹ مؤقتا ›", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="‹ ايقاف ›", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(
                text="「 الدعم 」", url=SUPPORT_CHAT,
            )
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="‹ أستمرار › ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="‹ مؤقتا ›", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="‹ ايقاف ›", callback_data=f"ADMIN Stop|{chat_id}")
        ],
        [
            InlineKeyboardButton(
                text="", url=f"tg://openmessage?user_id={OWNER_ID}",
            ),
            InlineKeyboardButton(
                text="「 الدعم 」", url=SUPPORT_CHAT,
            )
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"DilPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"DilPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
