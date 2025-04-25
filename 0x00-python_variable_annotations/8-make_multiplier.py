#!/usr/bin/env python3
"""
A module that defines a function returning a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns the product.
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier

    return multiplier_func
