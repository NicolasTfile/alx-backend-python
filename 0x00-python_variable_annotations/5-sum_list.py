#!/usr/bin/env python3

"""
This script defines a function to calculate the sum of a list of floats
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate and return the sum of a list of floats

    Args:
        input_list (List[float]): The input list of floating-point numbers

    Returns:
        float: The sum of the numbers in the input list
    """
    return sum(input_list)
