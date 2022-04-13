import asyncio 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from LuciferMoringstar_Robot.database.users_chats_db import db
from LuciferMoringstar_Robot.database.ia_filterdb import Media
from LuciferMoringstar_Robot.database._utils import get_size
from translation import LuciferMoringstar

@Client.on_message(filters.command('stats') & filters.incoming)
async def get_ststs(bot, message):
    nun=await message.reply_text("Connecting to MongoDB")
    await asyncio.sleep(2)
    total_users = await db.total_users_count()
    totl_chats = await db.total_chat_count()
    files = await Media.count_documents()
    size = await db.get_db_size()
    free = 536870912 - size
    size = get_size(size)
    free = get_size(free)
    await nun.edit(
       text=LuciferMoringstar.STATUS_TXT.format(files, total_users, totl_chats, size, free),
       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🪐 Back", callback_data="help"),
                                           InlineKeyboardButton("♻️ Refresh", callback_data="rfrsh")]])
    )

@Client.on_message(filters.command("id") & filters.group)
async def id_user(bot, message):
    id = message.from_user.id
    reply = message.reply_to_message
    chat = message.chat
    if chat not in message:
        await message.reply_text(f"Your Telegram ID: {id}")
    else:
        await message.reply_text(f"Chat ID: {chat}")
