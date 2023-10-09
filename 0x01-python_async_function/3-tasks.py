#!/usr/bin/env python3
"""module for tasks function"""


import importlib.util
import asyncio

# Specify the module name including the full path
module_name = '0-basic_async_syntax'
mod_file_pat = './0-basic_async_syntax.py'
# Use importlib.util.module_from_spec() to load the module
module_spec = importlib.util.spec_from_file_location(module_name, mod_file_pat)
module = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(module)


def task_wait_random(max_delay: int) -> asyncio.Task:
    """function to return asyncio task"""
    task: asyncio.Task = asyncio.ensure_future(module.wait_random(max_delay))
    return task


def main() -> None:
    """ main function to run wait_random function """
    task_async: asyncio.Task = task_wait_random()
    return task_async


if __name__ == "__main__":
    """ initialisation of module """
    main()
