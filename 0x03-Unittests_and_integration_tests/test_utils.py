#!/usr/bin/env python3
"""test module for utils module"""


import unittest
from functools import wraps
import utils
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
        """method to test get_json method to mock API request
        to get a mock HTTP response
        """
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload

        # with patch('utils.requests.get') as mock_get:
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):

    def test_memoize(self):
        """a method to test memoization"""

        class TestClass:

            def a_method(self) -> int:
                """a simple method used to test"""
                return 42

            @utils.memoize
            def a_property(self) -> Callable:
                """another simple method used to model a test property"""
                return self.a_method()

        test_instance = TestClass()

        with patch.object(test_instance, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42

            # Call the property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Assert that a_method is only called once
            mock_a_method.assert_called_once()

            # Assert that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    """function initiator"""
    unittest.main()
