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
        (KeyError, {}, ("a",)),
        (KeyError, {"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self,
                                         exception_type: Optional[KeyError],
                                         nested_map: Mapping, path: Sequence):
        """method to test key error"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class for unittests for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict, mock_get: Mock):
        """method to test get_json method to mock API request"""
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload

        # with patch('utils.requests.get') as mock_get:
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    """function initiator"""
    unittest.main()
