import httpx
import asyncio

async def request_example():
    async with httpx.AsyncClient(http2=True) as client:
        resp = await client.get("https://google.com")
        print(resp)
        print(resp.http_version)

asyncio.run(request_example())

