#!/usr/bin/env python3
'''asynchronous coroutine '''


async def wait_random(max_delay: int = 10):
    '''A asynchronous coroutine that awaits  for a random delay'''
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
