from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default="5527818445:AAE7TLprBfyUuQvYZsaOesQ0F-9C2sl2I80")
    
    
    API_ID = int(config("API_ID", default="6435225"))
    API_HASH = config("API_HASH", default="4e984ea35f854762dcde906dce426c2d")
    OWNER_ID = int(config("OWNER_ID", default=6259443940))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default="-1002092954715"))
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="",
        ).split(None)
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="",
        ).split(None)
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default="",
        ).split(None)
    ]
    GENIUS_API_TOKEN = config("GENIUS_API",default=None)
 #   AuDD_API = config("AuDD_API",default=None)
    RMBG_API = config("RMBG_API",default=None)
    DB_URI = config("DB_URI", default="mongodb+srv://knight_rider:GODGURU12345@knight.jm59gu9.mongodb.net/?retryWrites=true&w=majority")
    DB_NAME = config("DB_NAME", default="Paradox")
    BDB_URI = config("BDB_URI",default=None)
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="paradoxdump")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="ghost_kun")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE",default='Asia/Kolkata')
    BOT_USERNAME = "deds3c_bot"
    BOT_ID = "5527818445"
    BOT_NAME = "DedSeC"
    owner_username = "corpsealone"


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "5527818445:AAE7TLprBfyUuQvYZsaOesQ0F-9C2sl2I80"
    API_ID = 6435225  # Your APP_ID from Telegram
    API_HASH = "4e984ea35f854762dcde906dce426c2d"  # Your APP_HASH from Telegram
    OWNER_ID = 6259443940  # Your telegram user id defult to mine
    MESSAGE_DUMP = -1002092954715  # Your Private Group ID for logs
    DEV_USERS = [6810396528]
    SUDO_USERS = [6810396528]
    WHITELIST_USERS = []
    DB_URI = "mongodb+srv://knight_rider:GODGURU12345@knight.jm59gu9.mongodb.net/?retryWrites=true&w=majority"  # Your mongo DB URI
    DB_NAME = "Paradox"  # Your DB name
    NO_LOAD = []
    GENIUS_API_TOKEN = ""
    RMBG_API = ""
    PREFIX_HANDLER = ["!", "/","$"]
    SUPPORT_GROUP = "paradoxdump"
    SUPPORT_CHANNEL = "ghost_kun"
    VERSION = "VERSION"
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = ""
    WORKERS = 8
