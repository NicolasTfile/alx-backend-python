#!/usr/bin/env python3

"""
Script defines a function to safely retrieve the first element from a list
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Get the first element from a list safely

    Args:
        lst (Sequence[Any]): The input list of elements of unknown types

    Returns:
        Union[Any, None]: First element of the list or None if list is empty
    """
    if lst:
        return lst[0]
    else:
        return None
