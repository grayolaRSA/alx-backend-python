#!/usr/bin/env python3
"""module for mixed sum function"""

from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """function that takes int or float and returns sum as float"""
    total = 0.0

    for num in mxd_list:
        total += num

    return total
