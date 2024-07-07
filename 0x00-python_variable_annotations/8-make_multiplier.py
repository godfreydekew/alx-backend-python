#!/usr/bin/env python3
'''A function to return a callable'''
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    Args:
        multiplier (float): number to be multiplied

    Returns:
        typing.Callable[[float], float]: muiltiplier function
    """
    return lambda x: x * multiplier
