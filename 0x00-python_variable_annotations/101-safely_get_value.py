#!/usr/bin/env python3

"""
This script defines a function to safely retrieve a value from a dictionary
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary

    Args:
        dct (Mapping): The input dictionary
        key (Any): The key to look up in the dictionary
        default: The default value to return if the key is not found

    Returns:
        The value associated with the key in the dict, or the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
