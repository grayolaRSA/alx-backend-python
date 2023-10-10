#!/usr/bin/env python3
"""module for async generator"""


import asyncio
import random


async def async_generator() -> float:
    """async generator function"""
    for i in range(10):
        await asyncio.sleep(1)
        rand: float = random.uniform(0, 10)
        yield rand


async def main() -> None:
    """ main function to run async generator function """
    res: float = async_generator()
    return res

if __name__ == "__main__":
    """ initialisation of module """
    asyncio.run(main())
