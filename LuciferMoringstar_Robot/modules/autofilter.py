import re, asyncio, random
# from pyrogram import Client as LuciferMoringstar_Robot, filters as Worker
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from LuciferMoringstar_Robot.database._utils import get_size, split_list
from LuciferMoringstar_Robot.database.autofilter_db import get_filter_results, get_poster
from config import BUTTONS, bot_info, SPELL_MODE, SUPPORT, BOT_PICS
from translation import LuciferMoringstar


#@LuciferMoringstar_Robot.on_message(Worker.text & Worker.group & Worker.incoming & Worker.chat(AUTH_GROUPS) if AUTH_GROUPS else Worker.text & Worker.group & Worker.incoming)
async def group_filters(client, message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 50:    
        btn = []
        search = message.text
        files = await get_filter_results(query=search)
        if files:
            btn.append([InlineKeyboardButton(text=f"🔮 {search}", callback_data=f"{search}")]
            )
            btn.append([InlineKeyboardButton(f'✨ {message.chat.title}', callback_data="nothing"),
                        InlineKeyboardButton("🎭 IMDb", callback_data="imdbcheck")]
            )
            for file in files:
                file_id = file.file_id
                file_name = file.file_name
                file_size = get_size(file.file_size)
                btn.append([InlineKeyboardButton(text=f'🍭 {file_name}', callback_data=f"lucifermoringstar_robot#{file_id}"),
                            InlineKeyboardButton(text=f'🍬 {file_size}', callback_data=f"lucifermoringstar_robot#{file_id}")]
                )
        else:
            if SPELL_MODE:  
                reply = search.replace(" ", "+")
                reply_markup = InlineKeyboardMarkup([[
                 InlineKeyboardButton("🔮 IMDb", callback_data="imdbcheck"),
                 InlineKeyboardButton("🪐 Reason", callback_data="reason")
                 ]]
                )    
                imdb=await get_poster(search)
                if imdb and imdb.get('poster'):
                    await message.reply_photo(photo=imdb.get('poster'), caption=LuciferMoringstar.GET_MOVIE_7.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), short=imdb.get('short_info'), url=imdb['url']), reply_markup=reply_markup) 
                    return
        if not btn:
            return

        if len(btn) > 6: 
            btns = list(split_list(btn, 6)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="ɴᴏ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀᴠᴀɪʟᴀʙʟᴇ",callback_data="pages"),
                 InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
            )

            imdb=await get_poster(search)
            if imdb and imdb.get('poster'):
                await message.reply_photo(photo=imdb.get('poster'), caption=LuciferMoringstar.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), short=imdb.get('plot'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
            elif imdb:
                await message.reply_photo(photo="https://telegra.ph/file/41cf8373dc58aa7e9a535.jpg", caption=LuciferMoringstar.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), short=imdb.get('plot'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
            else:
                await message.reply_sticker(photo="CAACAgUAAxkBAAEBGPpiiKxk5UD9x7XMVvut4hrZ9yRYKwACWwADO0qzKWJZdSVC-jSFJAQ", caption=LuciferMoringstar.GET_MOVIE_2.format(query=search, mention=message.from_user.mention, chat=message.chat.title), reply_markup=InlineKeyboardMarkup(buttons))
            return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="ɴᴇxᴛ»",callback_data=f"nextgroup_0_{keyword}")]
        )    
        buttons.append(
            [InlineKeyboardButton(text=f"ᴘᴀɢᴇs 1/{data['total']}",callback_data="pages"),
             InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
        )

        imdb=await get_poster(search)
        if imdb and imdb.get('poster'):
            await message.reply_photo(photo=imdb.get('poster'), caption=LuciferMoringstar.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), short=imdb.get('plot'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
        elif imdb:
            await message.reply_photo(photo="https://telegra.ph/file/41cf8373dc58aa7e9a535.jpg", caption=LuciferMoringstar.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), short=imdb.get('plot'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
        else:
            await message.reply_sticker("CAACAgUAAxkBAAEBGPpiiKxk5UD9x7XMVvut4hrZ9yRYKwACWwADO0qzKWJZdSVC-jSFJAQ", caption=LuciferMoringstar.GET_MOVIE_2.format(query=search, mention=message.from_user.mention, chat=message.chat.title), reply_markup=InlineKeyboardMarkup(buttons))



# ---------- Bot PM ---------- #



#@LuciferMoringstar_Robot.on_message(Worker.text & Worker.private & Worker.incoming & Worker.chat(AUTH_GROUPS) if AUTH_GROUPS else Worker.text & Worker.group & Worker.incoming)
async def pm_autofilter(client, message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 50:    
        btn = []
        search = message.text
        files = await get_filter_results(query=search)
        if files:
            btn.append([InlineKeyboardButton(text=f"🔮 {search}", callback_data=f"{search}")]
            )
            for file in files:
                file_id = file.file_id
                file_name = file.file_name
                file_size = get_size(file.file_size)
                btn.append([InlineKeyboardButton(text=f'🍭 {file_name}', callback_data=f"pmfile#{file_id}"),
                            InlineKeyboardButton(text=f'🍬 {file_size}', callback_data=f"pmfile#{file_id}")]
                )
        else:
            await message.reply_photo(
                photo=random.choice(BOT_PICS),
                caption=LuciferMoringstar.ADD_YOUR_GROUP,
                reply_markup=InlineKeyboardMarkup([[
                   InlineKeyboardButton("🔥 Updates", url="https://t.me/xd_botz")
                   ]]
                )
            )
            return
        if not btn:
            return

        if len(btn) > 6: 
            btns = list(split_list(btn, 6)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="ɴᴏ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀᴠᴀɪʟᴀʙʟᴇ",callback_data="pages"),
                 InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
            )


            imdb=await get_poster(search)
            if imdb and imdb.get('poster'):
                await message.reply_photo(photo=imdb.get('poster'), caption=LuciferMoringstar.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), short=imdb.get('plot'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
            elif imdb:
                await message.reply_photo(photo="https://telegra.ph/file/41cf8373dc58aa7e9a535.jpg", caption=LuciferMoringstar.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), short=imdb.get('plot'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
            else:
                await message.reply_sticker("CAACAgUAAxkBAAEBGPpiiKxk5UD9x7XMVvut4hrZ9yRYKwACWwADO0qzKWJZdSVC", caption=LuciferMoringstar.GET_MOVIE_2.format(query=search, mention=message.from_user.mention, chat=bot_info.BOT_NAME), reply_markup=InlineKeyboardMarkup(buttons))

            return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="ɴᴇxᴛ»",callback_data=f"nextgroup_0_{keyword}")]
        )    
        buttons.append(
            [InlineKeyboardButton(text=f"ᴘᴀɢᴇs 1/{data['total']}",callback_data="pages"),
             InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")]
        )

        imdb=await get_poster(search)
        if imdb and imdb.get('poster'):
            await message.reply_photo(photo=imdb.get('poster'), caption=LuciferMoringstar.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), short=imdb.get('plot'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
        elif imdb:
            await message.reply_photo(photo="https://telegra.ph/file/41cf8373dc58aa7e9a535.jpg", caption=LuciferMoringstar.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), short=imdb.get('plot'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
        else:
            await message.reply_sticker("CAACAgUAAxkBAAEBGPpiiKxk5UD9x7XMVvut4hrZ9yRYKwACWwADO0qzKWJZdSVC-jSFJAQ", caption=LuciferMoringstar.GET_MOVIE_2.format(query=search, mention=message.from_user.mention, chat=bot_info.BOT_NAME), reply_markup=InlineKeyboardMarkup(buttons))
