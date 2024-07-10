#!/usr/bin/env python3
'''
A function which spawns wait_random
'''

import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Creates n tasks that wait for a random time between 0 and max_delay.
    '''
    tasks = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])

    return sorted(tasks)
