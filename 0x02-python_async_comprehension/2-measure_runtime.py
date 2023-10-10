#!/usr/bin/env python3
"""module to measure runtime"""


import asyncio
import time
from typing import List
from typing import Generator
async_com = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function to measure runtime of async function"""
    total_elapsed: float = 0
    start_time = time.perf_counter()
    await asyncio.gather(async_com(), async_com(), async_com(), async_com())
    total_elapsed = time.perf_counter() - start_time
    return total_elapsed
