from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    PORT = os.environ.get("PORT", "8080")
    
   # Your other confgs # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "")) # Make Bot Admin In This Channel
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://ibb.co/DH3N4Lyr")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    FSUB_PIC = os.environ.get("FSUB_PIC", "")
    
    
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
