#!/usr/bin/env python3
"""
A module that defines a function to_kv which returns a tuple.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of a number.

    Args:
        k (str): A string key.
        v (Union[int, float]): A value that will be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is k,
        and the second is v squared as a float.
    """
    return (k, float(v ** 2))
