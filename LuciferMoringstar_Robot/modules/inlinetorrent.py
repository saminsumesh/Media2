import asyncio
from pyrogram.errors import QueryIdInvalid
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, InlineQuery, InlineQueryResult, InlineQueryResultArticle, InputTextMessageContent
from LuciferMoringstar_Robot.tool import Searchx1337

@Client.on_inline_query()
async def botToreent(bot: Client,Inline: InlineQuery):
    search_ts = Inline.query
    answers = []

    if search_ts == "":
        answers.append(
            InlineQueryResultArticle(
                title="Search something",
                description="Search to find something",
                input_message_content=InputTextMessageContent(
                    message_text="**Join 🌟**\nhttps://t.me/zacBots",
                    parse_mode="markdown"
                ),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Updates", url="https://t.me/zacBots"),
                        ],
                        [
                            InlineKeyboardButton("Search Torrent", switch_inline_query_current_chat="!0 ")
                        ]
                    ]
                )
            )
        )
    elif search_ts.startswith("!0"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="| Search for torrent on 1337x",
                    description="Search torrent in 1337x",
                    input_message_content=InputTextMessageContent(
                        message_text="| [text]\n Search 1337x on **TELEGRAM** inline",
                        parse_mode="md"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!0 ")
                            ]
                        ]
                    )
                )
            )
    else:
        torrentList = await Searchx1337(search_ts)
        if not torrentList:
            answers.append(
                InlineQueryResultArticle(
                    title="Nothing found for your **SEARCH** on 1337x",
                    description=f"Can't find anything regarding on your {query} in x1337",
                    input_message_content=InputTextMessageContent(
                        message_text=f"Nothing found on {query} in 1337x",
                        parse_mode="md"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [ 
                                InlineKeyboardButton("Try again", switch_inline_query_current_chat="!0 ")
                            ]
                        ]
                    )
                )
            )
        else:
            for i in range(len(torrentList)):
                answers.append(
                    InlineQueryResultArticle(
                        title=f"{torrentList[i]['Name']}",
                        description=f"Seeders: {torrentList[i]['Seeders']}, Leechers: {torrentList[i]['Leechers']}\nSize: {torrentList[i]['Size']}, Downloads: {torrentList[i]['Downloads']}",
                        input_message_content=InputTextMessageContent(
                            message_text=f"**Category:** {torrentList[i]['Category']}\n"
                                         f"**Name:** {torrentList[i]['Name']}\n"
                                         f"**Languages:** {torrentList[i]['Languages']}\n"
                                         f"**Seeders:** {torrentList[i]['Seeders']}\n"
                                         f"**Leechers:** {torrentList[i]['Leechers']}\n"
                                         f"**Magnet:** {torrentList[i]['Magnet']}\n Torrent Generated from @GokuFilterBot",
                            parse_mode="md"
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton("Search Again", switch_inline_query_current_chat="!0 ")
                                ]
                            ]
                        ),
                        thumb_url=torrentList[i]['Poster']
                    )
                )
    try:
        await inline.answer(
            results=answers,
            cache_time=0
        )
        print(f"Answered Successfully - {inline.from_user.first_name}")
    except QueryIdInvalid:
        print(f"Failed to Answer - {inline.from_user.first_name} - Sleeping for 5s")
        await asyncio.sleep(5)
        try:
            await inline.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="Error: Search timed out!",
                switch_pm_parameter="start",
            )
        except QueryIdInvalid:
            print(f"Failed to Answer Error - {inline.from_user.first_name} - Sleeping for 5s")
            await asyncio.sleep(5)

