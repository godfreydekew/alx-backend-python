#!/usr/bin/env python3
'''A function to showcase iteratables '''


def element_length(lst: typing.Iterable[typing.Sequence]
                   ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Args:
        lst (typing.Iterable[typing.Sequence]): a iterable list

    Returns:
        typing.List[typing.Tuple[typing.Sequence, int]]: a list of tuples
    """
    return [(i, len(i)) for i in lst]
