import asyncio
import base64
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait

from main import LuciferMoringstar
from config import CHANNEL_ID


@LuciferMoringstar.on_message(filters.private & ~filters.command(['start','batch']))
async def channel_post(client: Client, message: Message):
    reply_text = await message.reply_text("Подождите...!", quote = True)
    try:
        post_message = await message.copy(chat_id = CHANNEL_ID, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await message.copy(chat_id = CHANNEL_ID, disable_notification=True)
    except:
        await reply_text.edit_text("Что-то не так..!")
        return
    string = f"get-{post_message.message_id}"
    string_bytes = string.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Ссылка", url=f'https://telegram.me/share/url?url={link}')]])
    await reply_text.edit(f"<b>Ссылка на загрузку</b>\n\n{link}", reply_markup=reply_markup, disable_web_page_preview = True)


@LuciferMoringstar.on_message(filters.private & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Перешлите это сообщение в канал (или заметки)..", chat_id = message.from_user.id, filters=filters.forwarded, timeout=30)
        except:
            return
        if first_message.forward_from_chat:
            if first_message.forward_from_chat.id == CHANNEL_ID:
                f_msg_id = first_message.forward_from_message_id
                break
        await first_message.reply_text("Переадресация только с назначенного канала...", quote = True)
        continue
    while True:
        try:
            second_message = await client.ask(text = "Перешлите последнее сообщение из канала (или заметок)..", chat_id = message.from_user.id, filters=filters.forwarded, timeout=30)
        except:
            return
        if second_message.forward_from_chat:
            if second_message.forward_from_chat.id == CHANNEL_ID:
                s_msg_id = second_message.forward_from_message_id
                break
        await second_message.reply_text("Доступно только подписчикам...", quote = True)
        continue
    string = f"get-{f_msg_id}-{s_msg_id}"
    string_bytes = string.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Ссылка", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>Ссылка на скачивание</b>\n\n{link}", quote=True, reply_markup=reply_markup)
