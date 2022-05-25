import aiohttp
from requests.utils import requote_uri

API_1337X = "https://api.abirhasan.wtf/1337x?query={}&limit={}"

async def Searchx1337(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(requote_uri(API_1337X.format(query, 50))) as res:
            return (await res.json())["results"] if ((await res.json()).get("results", None) is not None) else []
