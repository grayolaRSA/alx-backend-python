#!/usr/bin/env python3
"""module for async generator"""


import asyncio
import random


async def async_generator() -> int:
    """async generator function"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)