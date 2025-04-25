#!/usr/bin/env python3
"""
A module that provides a function to get the length of elements in an iterable.
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples with each
    element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple has
        the sequence and its length.
    """
    return [(i, len(i)) for i in lst]
