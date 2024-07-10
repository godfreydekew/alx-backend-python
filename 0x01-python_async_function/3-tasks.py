#!/usr/bin/env python3
'''
A function which returns a coroutine object
'''
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    akes an integer max_delay and returns a asyncio.Task.
    '''
    return asyncio.create_task(wait_random(max_delay))
