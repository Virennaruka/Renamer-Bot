from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.utils import not_subscribed
from config import FORCE_SUB

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="🔸JOIN CHANNEL🔸", url=f"https://t.me/{FORCE_SUB}") ]]
    text = "**JOIN THE CHANNEL TO USE THIS BOT **"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          


