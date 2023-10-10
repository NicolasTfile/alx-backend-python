#!/usr/bin/env python3
"""
Script that collects 10 random numbers using async comprehensions
"""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine that collects 10 random numbers using async comprehensions

    Returns:
        List[float]: A list of 10 random numbers
    """
    return [number async for number in async_generator()]
