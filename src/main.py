import asyncio
import aiohttp
from request import *
import constants
import time
import helpers
from schemas import Restaurant
import datetime


async def getRestaurants(session: aiohttp.ClientSession, endpoint: str, lat: float, lng: float, offset: int):
    res = await HttpRequest(session, endpoint.format(lat=lat, lng=lng, category_id=constants.CATEGORY.BESTSELLER, offset=offset))
    return res


async def process(result):
    data = []
    for merchant in result.searchResult.searchMerchants:
        data.append(Restaurant.from_dict(merchant))
    FILE_PATH = f"data/grab/{datetime.datetime.utcnow().strftime('%Y-%m-%d %H-%M-%S')}/{constants.LAT}-{constants.LNG}/restaurants.ndjson"
    if data:
        await helpers.writeToFileAsync(FILE_PATH, data)

def AsyncDec(func):
    init = time.perf_counter()
    asyncio.run(func)
    final = time.perf_counter()
    print(f"Time taken to run : {final-init} seconds")

@AsyncDec
async def main():
    session = await Session(headers=constants.HEADERS, base_url=constants.BASE_URL)
    res = []

    while len(res) == 0 or res[len(res)-1].searchResult.hasMore:
        tasks = [asyncio.create_task(getRestaurants(session, constants.ENDPOINT.RESTAURANT, constants.LAT, constants.LNG, i)) for i in range(constants.LIMIT)]
        result = await asyncio.gather(*tasks)
        res.extend(result)
    
    await asyncio.gather(*[asyncio.create_task(process(result)) for result in res])



if __name__ == '__main__':
    main()