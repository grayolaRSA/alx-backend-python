#!/usr/bin/env python3
"""module for miscellaneous function"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function for un-annnotated function"""
    return [(i, len(i)) for i in lst]
