import os

API_ID    = os.environ.get("API_ID", "23253271")
API_HASH  = os.environ.get("API_HASH", "83ea976f17a307e2ff5b76823305052f")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7788095464:AAEoZDA080VB-FLUSN_bX1lwc_Fan_EfH-s") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
