from pyrogram import Client, filters
from LuciferMoringstar_Robot.database.users_chats_db import db
from LuciferMoringstar_Robot.database.ia_filterdb import Media
from LuciferMoringstar_Robot.database._utils import get_size
from translation import LuciferMoringstar

@Client.on_message(filters.command('stats') & filters.incoming)
async def get_ststs(bot, message):
    rju = await message.reply('Fetching stats..')
    total_users = await db.total_users_count()
    totl_chats = await db.total_chat_count()
    files = await Media.count_documents()
    size = await db.get_db_size()
    free = 536870912 - size
    size = get_size(size)
    free = get_size(free)
    await rju.edit(LuciferMoringstar.STATUS_TXT.format(files, total_users, totl_chats, size, free))
