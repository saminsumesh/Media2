import time
import re, os
from os import environ
from translation import LuciferMoringstar
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "on"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "off"]:
        return False
    else:
        return default

# ==================================
API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
B_KEYS = environ["BOT_TOKEN"]
BOT_PICS = (environ.get('PICS', 'https://telegra.ph/file/8d4e4693a8a907cb51797.jpg')).split()
SUPPORT = environ.get("SUPPORT", "t.me/ZacSupport")
SPELL_MODE = is_enabled((environ.get('SPELL_CHECK_REPLY', "on")), True)
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", -1001664350806))
DATABASE_URI = environ.get("DATABASE_URI", None)
FORCE = environ.get('AUTH_CHANNEL')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", LuciferMoringstar.FILE_CAPTIONS)
DEV_NAME = environ.get("DEV_NAME", "zacBots")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
WARN_DATA_ID = int(environ.get("WARN_DATA_ID", "0"))
WARN_SETTINGS_ID = int(os.environ.get("WARN_SETTINGS_ID", "0"))
# ==================================
# Empty 😂
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
BUTTONS = {}
CURRENT = int(environ.get("SKIP", 2))
CANCEL = False
FORCES_SUB = int(FORCE) if FORCE and id_pattern.search(FORCE) else FORCE
DATABASE_NAME = environ.get("DATABASE_NAME", 'GokuFiles')
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
# ==================================

team_name = os.environ.get('team_name', 'XD Botz')
team_link = os.environ.get('team_link', 't.me/XD_Botz')

# ==================================
# About Bot 🤖
# ===============≠===================

if environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

class bot_info(object):
    BOT_NAME = None
    BOT_USERNAME = None
    BOT_ID = None
