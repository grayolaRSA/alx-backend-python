#!/usr/bin/env python3
"""test module for client side"""

import unittest
from utils import get_json
from unittest.mock import Mock, patch, MagicMock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """class for testing client side Github operations"""

    @patch('utils.get_json')
    @parameterized.expand([
        ("https://api.github.com/orgs/", "google",
         "https://api.github.com/orgs/google"),
        ("https://api.github.com/orgs/", "abc",
         "https://api.github.com/orgs/abc"),
    ])
    def test_org(self, org_url: str, org_name: str, org_name_url: str):
        """method to test GithubOrgClient.org"""
        mock_org = MagicMock()
        org_name_url = org_url + org_name
        mock_org.return_value = get_json(org_name_url)

        with patch('utils.get_json') as mock_get_org:
            mock_get_org.assert_called_once()
