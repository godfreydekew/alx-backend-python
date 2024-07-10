#!/usr/bin/env python3
'''
execute multiple coroutines at the same time with async
'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Creates n tasks that wait for a random amount of time between 0, max_delay.
    '''
    x = await asyncio.gather(*[task_wait_random(max_delay) for _ in range(n)])

    return sorted(x)
