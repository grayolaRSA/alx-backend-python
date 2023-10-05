#!/usr/bin/env python3
"""module for duck typed annotations"""

from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """function to test correct duck notation"""
    if lst:
        return lst[0]
    else:
        return None
