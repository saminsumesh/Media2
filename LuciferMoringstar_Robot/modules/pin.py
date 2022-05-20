import asyncio
from pyrogram import Client, filters
from pyrogram.types import (Message)

@Client.on_message(filters.command("pin"))
async def bot_pin(bot: Client, message: Message):
  member = await bot.get_chat_member(message.chat.id, message.from_user.id) 
  if member.can_pin_messages:
    if message.reply_to_message:
      await message.reply_to_message.pin()
      await message.reply_text("Pinned Successfully")
    else:
      await message.reply("Reply to a message to pin")
  else:
    await message.reply("You don't have permission to do this")
