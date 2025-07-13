import random
import asyncio
import logging 
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from config import *
from config import Config
from functools import wraps 

ADMIN_URL = Config.ADMIN_URL

def check_ban(func):
    @wraps(func)
    async def wrapper(client, message, *args, **kwargs):
        user_id = message.from_user.id
        user = await Botskingdom.col.find_one({"_id": user_id})
        if user and user.get("ban_status", {}).get("is_banned", False):
            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton("Cᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ...!!", url=ADMIN_URL)]]
            )
            return await message.reply_text(
                "Wᴛғ ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ғʀᴏᴍ ᴜsɪɴɢ ᴍᴇ ʙʏ ᴏᴜʀ ᴀᴅᴍɪɴ/ᴏᴡɴᴇʀ . Iғ ʏᴏᴜ ᴛʜɪɴᴋs ɪᴛ's ᴍɪsᴛᴀᴋᴇ ᴄʟɪᴄᴋ ᴏɴ **ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ...!!**",
                reply_markup=keyboard
            )
        return await func(client, message, *args, **kwargs)
    return wrapper

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Start Command Handler
@Client.on_message(filters.private & filters.command("start"))
@check_ban
async def start(client, message: Message):
    user = message.from_user
    await Botskingdom.add_user(client, message)

    # Initial interactive text and sticker sequence
    m = await message.reply_text("**Wᴇᴡ...Hᴏᴡ ᴀʀᴇ ʏᴏᴜ ᴅᴜᴅᴇ \n\nᴡᴀɪᴛ ᴀ ᴍᴏᴍᴇɴᴛ. . .**")
    await asyncio.sleep(0.4)
    await m.edit_text("Iᴀᴍ ᴀɴ Aᴅᴠᴀɴᴄᴇ ʙᴏᴛ ᴅᴜᴅᴇ ⚡")
    await asyncio.sleep(0.5)
    await m.edit_text(">_<")
    await asyncio.sleep(0.5)
    await m.edit_text("**Iᴀᴍ sᴛᴀʀᴛɪɴɢ...!!**")
    await asyncio.sleep(0.4)
    await m.delete()

    # Send sticker after the text sequence
    await message.reply_sticker("CAACAgUAAxkBAAEOtVNoUAphgIzDsgHV10rbfmFKNIgMlwACPQsAApWaqVbHL7SvWBBaITYE")

    # Define buttons for the start message
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(" • Aᴅᴅ ᴍᴇ ᴅᴜᴅᴇ •", url='http://t.me/bots_kingdom_auto_approvalbot?startchannel=true?group=true')
        ],
        [
            InlineKeyboardButton('• ᴜᴘᴅᴀᴛᴇs', url='https://t.me/botskingdoms'),
            InlineKeyboardButton('sᴜᴘᴘᴏʀᴛ •', url='https://t.me/botskingdomsgroup')
        ],
        [
            InlineKeyboardButton('• ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴅᴇᴠᴇʟᴏᴘᴇʀ•', url='https://t.me/botskingdoms')
        ]
    ])

    # Send start message with or without picture
    if Config.START_PIC:
        await message.reply_photo(
            Config.START_PIC,
            caption=Txt.START_TXT.format(user.mention),
            reply_markup=buttons
        )
    else:
        await message.reply_text(
            text=Txt.START_TXT.format(user.mention),
            reply_markup=buttons,
            disable_web_page_preview=True
  ),
            reply_markup=reply_markup,
            message_effect_id=5104841245755180586)  # 🔥
        
        return
      
@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data

    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                 InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')]
            ])
        )

    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                 InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close')]
            ])
        )

    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help'),
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data='about')]
            ])
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
