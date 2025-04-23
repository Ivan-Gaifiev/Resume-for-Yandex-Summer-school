from time import sleep
import asyncio
async def square_num(num):
    print(num**2)
    await asyncio.sleep(3)
    print("Done")


async def root_num(num):
    print(num**0.5)
    await asyncio.sleep(5)
    print("Done")


async def main():
    t1 = asyncio.create_task(square_num(4))
    t2 = asyncio.create_task(root_num(4))
    i1 = await t1
    i2 = await t2
    asyncio.wait_for(i1, 3)
    asyncio.wait_for(i2,5)
asyncio.run(main())
