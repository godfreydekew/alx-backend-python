#!/usr/bin/env python3
'''duck-typed annotations'''
import typing
from types import NoneType


# The types of the elements of the input are not know
def safe_first_element(lst: typing.Sequence[typing.Any]
                       ) -> typing.Union[typing.Any, NoneType]:
    if lst:
        return lst[0]
    else:
        return None
