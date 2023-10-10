#!/usr/bin/env python3
"""module for async comprehension"""


import asyncio
from typing import List
from typing import Generator
async_gen = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async comprehension coroutine"""
    gen: Generator[float, None, None] = async_gen()
    result: List[float] = []
    async for i in gen:
        result.append(i)
    return result


async def main():
    """main function"""
    values = await async_comprehension()
    print(values)

if __name__ == "__main__":
    asyncio.run(main())
