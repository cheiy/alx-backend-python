#!/usr/bin/env python3
"""
Module contains function that returns an element's length
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Finds the length of a list of elements
    """
    return [(i, len(i)) for i in lst]
