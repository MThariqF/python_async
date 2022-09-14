import asyncio
import time

get_time = time.time()

async def first():
    task = asyncio.create_task(second())
    print("A")
    print(f"takes {time.time() - get_time} second")
    await asyncio.sleep(1)
    print("B")
    print(f"takes {time.time() - get_time} second")
    result = await task
    print(result)

async def second():
    print(1)
    print(f"takes {time.time() - get_time} second")
    await asyncio.sleep(2)
    print(2)
    print(f"takes {time.time() - get_time} second")
    return ("Done")

asyncio.run(first())
