import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7609528498:AAGqcl_h-Cygc4v_oiXqD4cbp-yGypVcakY")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "27900743"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "ebb06ea8d41420e60b29140dcee902fc")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "7804396225").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "https://api.masterapi.tech")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility
