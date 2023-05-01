
# (c) Shrimadhav U K | Modifieded By @LISA_FAN_LK

import os
from config import Config
from pyrogram import Client as Clinton

#To inform that the bot is ready to be used
def send_status_message(Warrior):
    Warrior.send_message(
        chat_id=Config.OWNER_ID,
        text='I am READY!✅'
    )

if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Warrior = Clinton("@UploadLinkToFileBot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=plugins)
    with Warrior:
        send_status_message(Warrior)
    Warrior.run()
