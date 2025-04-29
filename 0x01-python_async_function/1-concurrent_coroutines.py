#!/usr/bin/env python3
"""
Defines a function that executes multiple coroutines
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function that executes routines concurrently
    """
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    completed_delays = []
    for completed_task in asyncio.as_completed(delays):
        delay = await completed_task
        completed_delays.append(delay)

    return completed_delays
