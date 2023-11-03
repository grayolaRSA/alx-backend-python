#!/usr/bin/env python3
"""test module for utils module"""


import unittest
from functools import wraps
from unittest.mock import Mock, patch, MagicMock
from utils import access_nested_map, get_json
from typing import Mapping, Sequence, Optional, Callable, Dict, List
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """class for unittests for utils module"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
         ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: any):
        """method to test access_nested_map method"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ("Exception 1", KeyError, {}, ("a",)),
        ("Exception 2", KeyError, {"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, name: str,
                                         exception_type: Optional[KeyError],
                                         nested_map: Mapping, path: Sequence):
        """method to test key error"""
        with self.assertRaises(exception_type):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    """function initiator"""
    unittest.main()
