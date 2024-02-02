import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

RUN = list(map(int, getenv("RUN", "2107529793 5618845741").split()))
