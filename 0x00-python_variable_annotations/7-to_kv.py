#!/usr/bin/env python3
"""module for mixed sum function"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function to generate tuple"""
    return (k, v * v)
