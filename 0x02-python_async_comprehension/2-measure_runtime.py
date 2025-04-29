#!/usr/bin/env python3
"""
Measure the total runtime of async_comprehension run 4 times in parallel
"""


import asyncio
import time
from typing import Callable
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Runs async_comprehensio 4 times in parallel and return total runtime
    """
    start_time = time.perf_counter()

    # Run coroutines in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    total_time = time.perf_counter() - start_time
    return (total_time)
