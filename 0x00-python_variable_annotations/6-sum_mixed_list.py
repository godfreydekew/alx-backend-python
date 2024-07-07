#!/usr/bin/env python3
'''A function to find sum of ints and floats'''


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    Args:
        mxd_lst (typing.List[typing.Union[int, float]]): list of integers
        and floats

    Returns:
        float: sum of integers and floats
    """
    return sum(mxd_lst)
