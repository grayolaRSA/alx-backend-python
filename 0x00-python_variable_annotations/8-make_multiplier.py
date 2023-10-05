#!/usr/bin/env python3
"""module for multiplier function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that multiplies floats together"""

    def multiplier_function(value: float) -> float:
        """Function that multiplies a value by the provided multiplier."""
        return value * multiplier

    return multiplier_function
