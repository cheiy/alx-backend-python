#!/usr/bin/env python3
"""
Module contains a type-annotated function that takes a string k
and an int OR float v as arguments and returns a tuple. The first element
of the tuple is the string k. The 2nd element is the square of the int/float
v and sould be annotated as a float
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[int, float]:
    """
    Refer to main module documentation
    """
    tup = (k, v*v)
    return tup
