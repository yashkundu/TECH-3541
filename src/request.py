import aiohttp
import typing
import asyncio
import sys

class Session:
    async def __init__(self, headers: typing.Dict, base_url: str):
        async with aiohttp.ClientSession(headers=headers, base_url=base_url) as session:
            self.__session = session

    @property
    def session(self):
        return self.session


class HttpRequest:

    def __init__(self, session: aiohttp.ClientSession, endpoint: str, max_retries = 5, back_off = 0.5):
        self.__session = session
        self.__endpoint = endpoint
        self.__max_retries = max_retries
        self.__back_off = back_off

    
    async def make_request(self) -> typing.Any:
        while True:
            try:
                async with self.__session.get(self.__endpoint) as res:
                    if res.status >= 400:
                        raise Exception(res.status)
                    result = await res.json()
                    return result
            except Exception as e:
                if self.__max_retries == 0:
                    print(f"Request to {self.__endpoint} cannot be done.", e , file=sys.stderr)
                    return
                self.__max_retries -= 1
                print(f"Retrying request to {self.__endpoint}")
                self.__back_off *= 2
                await asyncio.sleep(self.__back_off//2)
