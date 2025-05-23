#!/usr/bin/env python3
"""
Defines a function that waits fro a random delay
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    A function that waits for random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(10)
    return delay
