import asyncio
from pyrogram import Client, filters
from pyrogram.types import (Message)

@Client.on_message(filters.command("pin"))
async def bot_pin(bot: Client, message: Message):
  user = await bot.get_chat_member(message.chat.id, message.from_user.id)
  if user.can_pin_messages:
    if message.reply_to_message:
      dd=await message.reply_to_message.pin()
      await message.reply_text(f"Successfully pinned message: {dd.link}")
    else:
      await message.reply("Please reply to a message")
  else:
    await message.reply(f"Seems that you don't have enough rights to pin message in {message.chat.title}")
