#!/usr/bin/env python3
"""
Module contains a type-annotated function sum_mixed_list which
takes in a list of integers and floats and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function takes in a list of integers & floats, & returns their sum
    as a float
    """
    result: float = 0.0
    for item in mxd_lst:
        result += item
    return result
