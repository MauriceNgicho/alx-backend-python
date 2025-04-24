#!/usr/bin/env python3
"""
A module that provides a function that sums a list
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list and return the results.

    Args:
        input_list (list): A list to be summed up.

    Returns:
        float: The result of the summed up list.
    """
    return sum(input_list)
