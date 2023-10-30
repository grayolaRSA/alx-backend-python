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
        ("Test case 1", {"a": 1}, ("a",), 1),
        ("Test case 2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("Test case 3", {"a": {"b": 2}}, ("a", "b"), 2),
         ])
    def test_access_nested_map(self, name: str, nested_map: Mapping,
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


class TestGetJson(unittest.TestCase):
    """class for unittests for get_json function"""

    @patch('utils.requests.get')
    @parameterized.expand([
        ("Test 1", "http://example.com", {"payload": True}),
        ("Test 2", "http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, name: str, test_url: str, test_payload: Dict):
        """method to test get_json method"""
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload

        with patch('utils.requests.get') as mock_get:
            mock_get.return_value = mock_response

            result = get_json(test_url)

            self.assertEqual(result, test_payload)

            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """class for memoize methods"""

    def test_memoize(self):
        """method to test cacheing of method returns"""

        def memoize(func):
            """memoize function to cache results"""
            cache = {}

            @wraps(func)
            def wrapper(*args, **kwargs):
                key = str(args) + str(kwargs)

                if key not in cache:
                    cache[key] = func(*args, **kwargs)

                return cache[key]

            return wrapper

        class TestClass:
            """test class for memoize methods"""

            def a_method(self):
                """a test method"""
                return 42

            @memoize
            def a_property(self):
                """another test method"""
                return self.a_method()

            @patch('TestClass.a_method')
            def test_a_property(self):
                """test method for a_property"""
                mock_property = MagicMock
                mock_property.return_value = self.a_method()

                with patch('a_method') as mock_property:
                    mock_property.assert_called_once()


if __name__ == '__main__':
    unittest.main()
