#!/usr/bin/env python3
"""module for sum of list function"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """function to sum list of floats"""
    total = 0.0

    for num in input_list:
        total += num

    return total
