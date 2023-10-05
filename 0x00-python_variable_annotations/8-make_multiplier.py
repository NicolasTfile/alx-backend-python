#!/usr/bin/env python3

"""
This script defines a function to create a multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function

    Args:
        multiplier (float): The multiplier value

    Returns:
        Callable: A function that takes a float and returns a float
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
