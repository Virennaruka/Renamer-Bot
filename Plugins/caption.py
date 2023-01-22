from pyrogram import Client, filters 
from helper.database import db

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**__GIVE ME A CAPTION TO SET.__\n\nEXAMPLE:- `/SET_CAPTION {FILENAME}\n\n💾 SIZE: {FILESIZE}\n\n⏰ DURATION: {DURATION}`**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("__**✅ CAPTION IS SAVED**__")

    
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("__**😔 YOU DONT HAVE ANY CAPTION**__")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("__**❌️ CAPTION IS DELETED**__")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**YOUR CAPTION:-**\n\n`{caption}`")
    else:
       await message.reply_text("__**😔 YOU DONT HAVE ANY CAPTION**__")
