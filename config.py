import os
from os import environ

# Retrieving environment variables with correct syntax
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", 17319714))  # Provide a default value of 0
API_HASH = os.environ.get("API_HASH", "")
OWNER = int(os.environ.get("OWNER", 0))  # Provide a default value of 0
BOT_USERNAME = os.environ.get('BOT_USERNAME', "")

FORCE_SUBS = os.environ.get("FORCE_SUBS", "HxBots")
LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', 0))  # Provide a default value of 0

DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "renamebot-premium")

STRING = os.environ.get("STRING", "")
BOT_PIC = os.environ.get("BOT_PIC", "https://graph.org/file/cca849a2f63053fa3f622.jpg")

# Shortener settings
SHORTNER_URL = os.environ.get("SHORTNER_URL", "")
SHORTNER_API = os.environ.get("SHORTNER_API", "")
TOKEN_TIMEOUT = os.environ.get("TOKEN_TIMEOUT", "")
