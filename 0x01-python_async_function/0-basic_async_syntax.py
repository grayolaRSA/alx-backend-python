#!/usr/bin/env python3
""" module for max delay async function"""

import asyncio
import random


async def wait_random(max_delay: int = 10):
    """ async delay function """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def main():
    """ main function to run wait_random function """
    res = await asyncio.run(wait_random())
    return res

if __name__ == "__main__":
    """ initialisation of module """
    asyncio.run(main())
