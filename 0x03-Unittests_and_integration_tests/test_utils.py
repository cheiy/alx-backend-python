#!/usr/bin/env python
"""
Module contains class fro testing the utils module
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Dict, Mapping, Sequence, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """
    Class inherits from unittest and implements the
    TestAccessNestedMap.test_access_nested_map
    method
    """
    @parameterized.expand
    def test_access_nested_map(
            self, nested_map: Mapping,
            path: Sequence,
            expected: Union[Dict, int]) -> None:
        """
        Method tests access_nested_map function output
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
