#!/usr/bin/env python3
'''Function to return a tuple'''
import typing


def to_kv(k: str, v:  typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    Args:
        k (str): string parameter
        v (typing.Union[int, float]): either string or float parameter

    Returns:
        typing.Tuple[str, float]: _description_
    """
    return (k, v*v)
