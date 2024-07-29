#!/usr/bin/env python3
"""0. Parameterize a unit test
"""
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """Tests the `access_nested_map` function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests `access_nested_map`'s output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
