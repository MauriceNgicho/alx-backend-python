#!/usr/bin/env python3
"""
Defines an async generator that yields random numbers
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    coroutine that yield a random float between 0 and 10,
    after waiting asynchronously for 1 sec, repeated 10 times
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
