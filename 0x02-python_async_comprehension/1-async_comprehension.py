#!/usr/bin/env python3
"""
Collect 10 random from async_generator using async comprehension
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random floats from async_generator using async comprehension
    and return them as  a list
    """
    return [i async for i in async_generator()]
