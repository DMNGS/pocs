import uasyncio as asyncio

async def main():
    sleep_test()
    print('Sleeping')

async def sleep_test():
    print('Going to sleep')
    await asyncio.sleep(1)
    print('Well rested')
    
asyncio.run(main())