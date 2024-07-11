#!/usr/bin/env python3
'''
Run time for four parallel comprehensions
'''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measure the runtime of an asynchronous function.
    '''
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(
        ), async_comprehension(), async_comprehension())
    end = time.perf_counter()
    return (end - start)
