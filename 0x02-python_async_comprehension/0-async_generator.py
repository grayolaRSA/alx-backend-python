#!/usr/bin/env python3
"""module for async generator"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, float]:
    """async generator function"""
    for i in range(10):
        await asyncio.sleep(1)
        rand: float = random.uniform(0, 10)
        yield rand


async def main():
    """main function"""
    gen: float = await async_generator()
    return gen

if __name__ == "__main__":
    asyncio.run(main())
