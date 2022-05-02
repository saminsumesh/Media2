from random import choice
from config import START_MSG, FORCES_SUB, BOT_PICS, ADMINS, bot_info, DEV_NAME
from pyrogram import Client as LuciferMoringstar_Robot, filters as Worker
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import LuciferMoringstar
from LuciferMoringstar_Robot.database.users_chats_db import db

@LuciferMoringstar_Robot.on_message(Worker.private & Worker.command(["start"]))
async def start_message(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
    if len(message.command) != 2:
        if message.from_user.id not in ADMINS: 
            buttons = [[
             InlineKeyboardButton("Add me to your group", url=f"http://t.me/{bot_info.BOT_USERNAME}?startgroup=true")
             ],[
             InlineKeyboardButton("Updates", url="https://t.me/ZacBots"),
             InlineKeyboardButton("Support", url="https://t.me/ZacSupport"),
             ],[
             InlineKeyboardButton("Help", callback_data="help"),
             InlineKeyboardButton("About", callback_data="about") 
             ]]
        else:
            buttons = [[
             InlineKeyboardButton("Add me to your group", url=f"http://t.me/{bot_info.BOT_USERNAME}?startgroup=true")
             ],[
             InlineKeyboardButton("Updates", url="https://t.me/ZacBots"),
             InlineKeyboardButton("Support", url="https://t.me/ZacSupport"),
             ],[
             InlineKeyboardButton("Help", callback_data="help"),
             InlineKeyboardButton("About", callback_data="about") 
             ]]
        await message.reply_photo(photo = choice(BOT_PICS), caption=LuciferMoringstar.START_TXT.format(mention = message.from_user.mention, bot_name = bot_info.BOT_NAME, bot_username = bot_info.BOT_USERNAME), reply_markup=InlineKeyboardMarkup(buttons))
        
    elif len(message.command) ==2 and message.command[1] in ["subscribe"]:
        invite_link = await bot.create_chat_invite_link(int(FORCE_SUB))
        button=[[
         InlineKeyboardButton("ᴊᴏɪɴ ᴛᴏ ᴜsᴇ ᴍᴇ", url=invite_link.invite_link)
         ]]
        reply_markup = InlineKeyboardMarkup(button)
        await message.reply_photo(
            photo=choice(BOT_PICS),
            caption=f"""<i><b>Hello {message.from_user.mention}. \nYou Have <a href="{invite_link.invite_link}">Not Subscribed</a> To <a href="{invite_link.invite_link}">My Update Channel</a>.So you do not get the Files on Inline Mode, Bot Pm and Group</i></b>""",
            reply_markup=reply_markup
        )
        return
   
@LuciferMoringstar_Robot.on_message(Worker.private & Worker.command(["help"]))
async def help(bot, message):
    button = [[
        InlineKeyboardButton("Autofilter", callback_data="autofilter"),
        InlineKeyboardButton("Pin", callback_data="pin"),
        ],[
        InlineKeyboardButton("Ban", callback_data="ban"),
        InlineKeyboardButton("Mute", callback_data="mute"),
        ],[
        InlineKeyboardButton("Status", callback_data="stats"),
        InlineKeyboardButton("« Back", callback_data="start")
        ]]
    await message.reply_photo(
        photo = choice(BOT_PICS),
        caption=LuciferMoringstar.HELP_MSG.format(mention=message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(button))
      
@LuciferMoringstar_Robot.on_message(Worker.private & Worker.command(["about"]))
async def about(bot, message):
    button = [[
             InlineKeyboardButton("sᴏᴜʀᴄᴇ", url="https://t.me/ippotharam34"),
             InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/zacbots"),
             InlineKeyboardButton("« ʙᴀᴄᴋ", callback_data="start")
             ]]               
    await message.reply_photo(
        photo = choice(BOT_PICS),
        caption=LuciferMoringstar.ABOUT_MSG.format(mention=message.from_user.mention, bot_name=bot_info.BOT_NAME, bot_username=bot_info.BOT_USERNAME, dev_name=DEV_NAME),
        reply_markup=InlineKeyboardMarkup(button))
        
