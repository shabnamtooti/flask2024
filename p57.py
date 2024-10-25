import asyncio
import datetime
async def f1():
    print('hello')
    await asyncio.sleep(2)
    print('hi')
async def f2():
    print('hello')
    await asyncio.sleep(2)
    print('hi')
async def main():
    await asyncio.gather(f1(),f2())
print(datetime.datetime.now)
asyncio.run(main())
print(datetime.datetime.now)