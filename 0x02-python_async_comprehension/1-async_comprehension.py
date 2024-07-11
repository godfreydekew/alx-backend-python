#!/usr/bin/env python3
'''
Async Comprehensions
'''
import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    '''
    Collect 10 random numbers from async_generator using
    Async Comprehensions
    '''
    return [x async for x in async_generator()]
