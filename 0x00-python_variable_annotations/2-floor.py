#!/usr/bin/env python3
"""
Module contains a type-annotated function called floor which takes
a float as argument and returns the floor of the same
"""


def floor(n: float) -> float:
    """
    Function takes a float and returns the floor of this float
    """
    rounded_down: int = n // 1
    return int(rounded_down)
