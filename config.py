import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    START_MSG = os.environ.get("START_MSG", "<b>ഹായ് {},\nനിങ്ങൾക്ക് വേണ്ട song കിട്ടാൻ /song ഇങ്ങനെ കമാൻഡ് ടൈപ്പ് ചെയ്ത ശേഷം space ഇട്ട ശേഷം പാട്ടിന്റെ വരി ടൈപ്പ് ചെയ്തു കൊടുക്കുക 💖💞,</b>\n\nSend me Any Songs name with /song command")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/5a57db69c5e31750fcc89.jpg")
    OWNER = os.environ.get("OWNER", "AB_Mediaw") 
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
