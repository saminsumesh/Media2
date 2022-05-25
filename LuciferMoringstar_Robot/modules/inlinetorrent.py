from ast import parse
from email import message
from posixpath import split
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, InlineQuery, InlineQueryResult, InlineQueryResultArticle, InputTextMessageContent
#from LuciferMoringstar_Robot.helpers import torrentSEARCH

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
                            InlineKeyboardButton("Search Torrent", switch_inline_query_current_chat="| ")
                        ]
                    ]
                )
            )
        )
    elif search_ts.startwith("|"):
        query = search_ts.split(" ", 1)[-1]
        if (query == "") or (query == " "):
            answers.append(
                InlineQueryResultArticle(
                    title="| Search for torrent on x1337",
                    description="Search torrent in x1337",
                    input_message_content=InputTextMessageContent(
                        message_text="| [text]\n Search x1337 on **TELEGRAM** inline",
                        parse_mode="md"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Search Again", switch_inline_query_current_chat="| ")
                            ]
                        ]
                    )
                )
            )
    else:
        torrentList = await Searchx1337(query)
        if not torrentList:
            answers.append(
                InlineQueryResultArticle(
                    title="Nothing found for your **SEARCH** on x1337",
                    description=f"Can't find anything regarding on your {query} in x1337",
                    input_message_content=InputTextMessageContent(
                        message_text=f"Nothing found on {query} in x1337",
                        parse_mode="md"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [ 
                                InlineKeyboardButton("Try again", switch_inline_query_current_chat="| ")
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
                                    InlineKeyboardButton("Search Again", switch_inline_query_current_chat="| ")
                                ]
                            ]
                        ),
                        thumb_url=torrentList[i]['Poster']
                    )
                )

