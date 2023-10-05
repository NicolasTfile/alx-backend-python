#!/usr/bin/env python3

"""
Script to create a tuple with a string and the square of an integer or float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of an integer or float

    Args:
        k (str): The string key
        v (Union[int, float]): The integer or float value

    Returns:
        Tuple: A tuple with the string key and the square of v
    """
    return (k, float(v ** 2))
