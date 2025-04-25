#!/usr/bin/env python3
"""
A module that provides a function that add an int and float.
"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Takes a list of integers and floats and returns their sum.

    Args:
        numbers (List[Union[int, float]]): A list of integers and/or floats.

    Returns:
        float: The sum of the numbers.
    """
    return (sum(mxd_list))
