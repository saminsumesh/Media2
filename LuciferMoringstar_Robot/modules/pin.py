import asyncio
from pyrogram import Client, filters
from pyrogram.types import (Message)

@Client.on_message(filters.command("pin"))
async def bot_pin(bot: Client, message: Message):
  chat_type = message.chat.type
  reply = message.reply_to_message
  if chat_type == "supergroup":
    if reply:
      user = await bot.get_member(message.chat.id, message.from_user.id)
      if user.status == (("adminstrator") or ("creator")):
        await bot.reply.pin()
        await asyncio.sleep(5)
        await cc.delete()
        cc=await message.reply("Successfully pinned.")
      else:
        await message.reply_text("Sorry You're not an Admin of this chat.")
    else:
      await message.reply_text("Please reply to a message or any file so that i could pin it.")
  else:
   return await message.reply_text("OkDa")
     
  
