import asyncio
from pyrogram import Client, filters
from pyrogram.types import (Message)

@Client.on_message(filters.command("pin"))
async def bot_pin(bot: Client, message: Message):
  chat_type = message.chat.type
  reply = message.reply_to_message
  if chat_type == "supergroup":
    if reply:
      user = await bot.get_chat_member(message.chat.id, message.from_user.id)
      if user.status != (("adminstrator") or ("owner")):
        await message.reply_text("Poda Poi admin avh")
      else:
        await bot.pin()
        print("sussess")
    else:
      await message.reply_text("Please reply to a message or any file so that i could pin it.")
  else:
   return await message.reply_text("OkDa")
     
  
