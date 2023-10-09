#!/usr/bin/env python3
"""
Measures the total execution time for wait_n and return total_time / n
"""

import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)

    Args:
        n (int): The number of times to call wait_n
        max_delay (int): The maximum delay in seconds

    Returns:
        float: The average execution time per call
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start

    average_time_per_call = total_time / n

    return average_time_per_call
