#!/usr/bin/env python3
'''
Async Generator function
'''
import asyncio
import random


async def async_generator() -> float:
    '''
    Yields numbers from 0 to 10.
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
