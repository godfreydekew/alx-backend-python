#!/usr/bin/env python3
"""0. Parameterize a unit test
"""
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """Parameterize a unit test Class
    """
    @parameterized.expand([
        ("test1", {"a": 1}, ("a",), 1),
        ("test2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("test3", {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self, n: str, np: Mapping, p: Sequence, e: Any) -> None:
        """est that the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(np, p), e)
