#!/usr/bin/env python3
"""module for duck typed annotations"""

from typing import Iterable, List, Union, Tuple, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
