#!/usr/bin/env python3
"""
Module contains an annotated function sum_list which takes a list
of floats as an argument and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function takes in a list of floats and returns their sum.
    """
    result: float = 0.0
    for item in input_list:
        result += item
    return float(result)
