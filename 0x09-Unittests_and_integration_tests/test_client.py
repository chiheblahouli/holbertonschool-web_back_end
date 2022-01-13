#!/usr/bin/env python3
"""test client file """
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """Test class Org Client"""
    @parameterized.expand([("google"),("abc"),])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, income, mock):
        """test org client"""
        fde = GithubOrgClient(income)
        response = fde.org
        self.assertEqual(response, mock.return_value)
        mock.assert_called_once
