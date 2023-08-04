#!/usr/bin/env python3
"""
Module defines a type-annonated function that takes a float muliplier as
an argument & returns a function that multiplies a float by the multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Refer to module documentation
    """
    return lambda x: x * multiplier
