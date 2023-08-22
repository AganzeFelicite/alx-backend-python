#!/usr/bin/env python3
"""
some modile on
advanced task
"""


from typing import Union, Mapping, Any, TypeVar


A = TypeVar('A')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[A, None] = None) -> Union[A, Any]:
    """
    add types to this
    provided codes
    """
    if key in dct:
        return dct[key]
    else:
        return default
