#!/usr/bin/env python3
"""module to measure runtime"""


import asyncio
import time
import importlib.util
from typing import List

# Specify the module name including the full path
module_name = '1-concurrent_coroutines'
mod_file_pat = './1-concurrent_coroutines.py'
# Use importlib.util.module_from_spec() to load the module
module_spec = importlib.util.spec_from_file_location(module_name, mod_file_pat)
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)


def measure_time(n: int, max_delay: int) -> float:
    """function to measure average time for function execution"""
    total_elapsed: float = 0

    for _ in range(n):
        start_time = time.perf_counter()
        asyncio.run(module.wait_n(1, max_delay))
        elapsed = time.perf_counter() - start_time
        total_elapsed += elapsed

    average_time = total_elapsed / n
    return average_time


def main() -> None:
    """ main function to run wait_n function """
    avg_time = measure_time()
    return avg_time


if __name__ == "__main__":
    """ initialisation of module """
    main()
