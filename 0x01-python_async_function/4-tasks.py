#!/usr/bin/env python3
"""
Defines a function that returns a new task
"""


import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    Return a new task
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delays.append(delay)

    return (delays)
