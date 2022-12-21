
import time
import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5806016246:AAE_C1NtmjSpgFRk8pd1v0nHbOkFbVxHn8k")

# Get from my.telegram.org (or @UseTGXBot)
APP_ID = int(os.environ.get("APP_ID", "7880210"))

# Get from my.telegram.org (or @UseTGXBot)
API_HASH = os.environ.get("API_HASH", "1bb4b2ff1489cc06af37cba448c8cce9")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQC7m_aSlwlhua-XDK0rildU0WFwtt31aq0Z8Ruyn3lh3UbzluUzdfdpxDz-IN3juiGGrovcmK-MwiYbobLoSfdUQcilgWSaMaqgNqpii_nUncs6Vu7vIOHp8JcsQ5E0CneipTD3FdhAHGf_lVC9pkVvavH4ijFMZl0pmQnDyKYU-Ogeu5OOo7FOj6j_SUfG2_A3SOk-rJxm_lcTskQ7btlLgqbkMQR3FtpR02leBeBR-52m8AnAFp4mlnPei-CzcmRGg9m1LFcUe_CGcpfD3AhoZOFIXQzogJLTl6cCcjslZCqQ5b9aDGc6d0iZW9Imj2YWMtKte8YG589xI68Mf4VuYbzVEgA")

# Database URL from https://cloud.mongodb.com/
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://bot1:bot1@cluster0.fqzak9o.mongodb.net/?retryWrites=true&w=majority")

# Your database name from mongoDB
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_NAME2 = str(os.environ.get("DATABASE_NAME2", "Unlimited"))

# ID of users that can use the bot commands
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1113630298").split())

# Should bot search for document files in channels
DOC_SEARCH = os.environ.get("DOC_SEARCH", "yes").lower()

# Should bot search for video files in channels
VID_SEARCH = os.environ.get("VID_SEARCH", "yes").lower()

# Should bot search for music files in channels
MUSIC_SEARCH = os.environ.get("MUSIC_SEARCH", "yes").lower()

# To save user details (Usefull for getting userinfo and total user counts)
# May reduce filter capacity :(
# Give yes or no
SAVE_USER = os.environ.get("SAVE_USER", "yes").lower()


# Go to https://dashboard.heroku.com/account, scroll down and press Reveal API
# To check dyno status
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)




class Config(object):




    # OPTIONAL - To set alternate BOT COMMANDS
    ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")
    DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMDD", "del")
    DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMDD", "delall")
    CONNECT_COMMAND = os.environ.get("CONNECT_COMMANDD", "connect")
    DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMANDD", "disconnect")


    # To record start time of bot
    BOT_START_TIME = time.time()


IMDB_TEXT = """**Hey [{user}](https://t.me/{un}) Your ~~{query} movie~~ is Ready** 🍁

__📺 **Movie** : **{title}**
📆 **Year** : {year}
🎙️ **Audio** : {languages}
🏃 **Time** : {runtime} Minutes
🌟 **Rating** : {rating}/10
🔖 **Genres** : {genres}__

**🙋🏼 Request by : [{user}](https://t.me/{un})** """



