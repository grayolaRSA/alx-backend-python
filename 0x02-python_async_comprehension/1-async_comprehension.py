#!/usr/bin/env python3
"""module for async comprehension"""


import asyncio
from typing import List
async_gen = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async comprehension coroutine"""
    gen = async_gen()
    result = []
    async for i in gen:
        result.append(i)
    return result


async def main():
    values = await async_comprehension()
    print(values)

if __name__ == "__main__":
    asyncio.run(main())
