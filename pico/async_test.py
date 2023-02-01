import uasyncio as asyncio

async def sleep_test():
    print('Going to sleep')
    await asyncio.sleep(1)
    print('Well rested')
    
asyncio.run(sleep_test())