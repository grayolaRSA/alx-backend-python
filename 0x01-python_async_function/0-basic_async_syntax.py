#!/usr/bin/env python3
""" module for max delay async function"""

import asyncio
import random


async def wait_random(max_delay: int = 10):
    """ async delay function """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
