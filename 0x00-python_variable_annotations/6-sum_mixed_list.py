#!/usr/bin/env python3
"""
Module contains a type-annotated function sum_mixed_list which
takes in a list of integers and floats and returns their sum as a float
"""
from typing import Union


def sum_mixed_list(mxd_lst: Union[float, int]) -> float:
    """
    Function takes in a list of integers & floats, & returns their sum
    as a float
    """
    result: float = 0.0
    for item in mxd_lst:
        result += item
    return result
