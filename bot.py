import os
import time
from datetime import datetime, timedelta
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from config import config
from aiohttp import web
from route import web_server
import pyrogram.utils
import random, asyncio

pyrogram.utils.MIN_CHANNEL_ID = -1002822095762
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "@botskingdomschat")

PORT = Config.PORT

app = Client(
    "approver",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)
self.start_time = time.time()

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username
        self.uptime = Config.BOT_UPTIME
        if Config.WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()
            await web.TCPSite(app, "0.0.0.0", PORT).start()
        print(f"{me.first_name} Is Started.....✨️")
        uptime_seconds = int(time.time() - self.start_time)
        uptime_string = str(timedelta(seconds=uptime_seconds))
        for chat_id in [Config.LOG_CHANNEL, SUPPORT_CHAT]:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time_str = curr.strftime('%I:%M:%S %p')
                await self.send_photo(
                    chat_id=chat_id,
                    photo=Config.START_PIC,
                    caption=(
                        "**I ʀᴇsᴛᴀʀᴛᴇᴅ ᴀɢᴀɪɴ !**\n\n"
                        f"ɪ ᴅɪᴅɴ'ᴛ sʟᴇᴘᴛ sɪɴᴄᴇ​: `{uptime_string}`"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/botskingdoms")]]
                    )
                )
            except Exception as e:
                print(f"Failed to send message in chat {chat_id}: {e}")

Bot().run()
