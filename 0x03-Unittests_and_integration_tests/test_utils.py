#!/usr/bin/env python3
"""test module for utils module"""


import unittest
from utils import access_nested_map
from typing import Mapping, Sequence, Callable
from functools import wraps
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """class for unittests for utils module"""

    @parameterized.expand([
        ("Test case 1", {"a": 1}, ("a",), 1),
        ("Test case 2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("Test case 3", {"a": {"b": 2}}, ("a", "b"), 2),
         ])
    def test_access_nested_map(self, name: str, nested_map: Mapping,
                               path: Sequence, expected: any) -> any:
        """method to test access_nested_map method"""

        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
