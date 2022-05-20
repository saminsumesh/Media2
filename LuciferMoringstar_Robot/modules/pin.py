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
      if user.can_pin_message:
        await reply.pin()
        cc=await message.reply_text("Successfully Pinned ✨")
        await asyncio.sleep(5)
        await cc.delete()
      else:
        await message.reply_text(f"Seems like you don't have enough rights in {message.chat.title}")
    else:
      await message.reply_text("Please reply to a message")
  else:
   return await reply.pin()
     
  
