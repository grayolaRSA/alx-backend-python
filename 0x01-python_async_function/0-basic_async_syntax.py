#!/usr/bin/env python3
""" module for max delay async function"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ async delay function """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main() -> None:
    """ main function to run wait_random function """
    res: float = await wait_random()
    return res

if __name__ == "__main__":
    """ initialisation of module """
    asyncio.run(main())
