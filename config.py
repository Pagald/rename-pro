import os, re
from os import environ


BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
OWNER = int(os.environ.get("OWNER"))
BOT_USERNAME = os.environ.get('BOT_USERNAME', "")

FORCE_SUBS = os.environ.get("FORCE_SUBS", "HxBots")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))

DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "renamebot-premium")

STRING = os.environ.get("STRING", "")
BOT_PIC = os.environ.get("BOT_PIC", "https://graph.org/file/cca849a2f63053fa3f622.jpg")





# if you need to add verify system then dm me on telegram

SHORTNER_URL = os.environ.get("SHORTNER_URL", "")
SHORTNER_API = os.environ.get("SHORTNER_API", "")
TOKEN_TIMEOUT = os.environ.get("TOKEN_TIMEOUT", "")
