#!/usr/bin/env python3

"""
This script defines a function to zoom in on elements in a tuple
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in on elements in a tuple by repeating them based on a given factor

    Args:
        lst (Tuple[int, ...]): The input tuple containing integers
        factor (int, optional): The zoom factor (default is 2)

    Returns:
        Tuple[int, ...]: New tuple with elements repeated based on the factor
    """
    zoomed_in: Tuple = tuple(
        item for item in lst
        for i in range(factor)
    )
    return list(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
