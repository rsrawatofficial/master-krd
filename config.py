import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7602120964:AAFP6yo0Vyw9j7f2YfJIPtlA7OvAbUu6NTs")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "15541919"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "fbf0d590575bbaaad9d773d04c8872e4")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "7310262552").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
