#!/usr/bin/env python3
"""
A module that defines a duck-typed function for safe access of first element.
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists, otherwise None.

    Args:
        lst (Sequence[Any]): A sequence of elements.

    Returns:
        Union[Any, None]: First element if present, else None.
    """
    if lst:
        return lst[0]
    else:
        return None
