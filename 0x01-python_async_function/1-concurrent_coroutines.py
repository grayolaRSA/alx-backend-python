#!/usr/bin/env python3
"""module for wait_n async function"""


import importlib.util
import asyncio
import random
from typing import List

# Specify the module name including the full path
module_name = '0-basic_async_syntax'
mod_file_pat = './0-basic_async_syntax.py'
# Use importlib.util.module_from_spec() to load the module
module_spec = importlib.util.spec_from_file_location(module_name, mod_file_pat)
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ function to return list of delays """
    delays: List[float] = []
    tasks = [module.wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    delays.extend(results)
    delays.sort()

    return delays


async def main() -> None:
    """ main function to run wait_n function """
    res: List[float] = await wait_n()
    return res

if __name__ == "__main__":
    """ initialisation of module """
    asyncio.run(main())
