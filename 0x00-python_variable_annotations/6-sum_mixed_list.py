#!/usr/bin/env python3

"""
A script to calculate the sum of a list containing integers and floats
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate and return the sum of a list containing integers and floats

    Args:
        mxd_lst: The input list containing integers and floats

    Returns:
        Sum of the numbers in the input list as a floating-point number
    """
    return sum(mxd_lst)
