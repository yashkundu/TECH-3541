import aiofiles
import json
import typing

async def writeToFileAsync(file: str, obj: typing.Dict):
    async with aiofiles.open(file, 'a+') as f:
        await f.write(json.dumps(obj) + '\n')
