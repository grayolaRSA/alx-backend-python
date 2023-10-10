#!/usr/bin/env python3
"""module for async comprehension"""


import asyncio
from typing import List
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async comprehension coroutine"""
    # gen: Generator[float, None, None] = async_generator()
    result: List[float] = [i async for i in async_generator()]
    return result
