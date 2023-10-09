#!/usr/bin/env python3
"""
Async routine to spawn task_wait_random n times with the specified max_delay
and return a list of delays in ascending order
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay

    Args:
        n (int): The number of times to spawn task_wait_random
        max_delay (int): The maximum delay in seconds

    Returns:
        List[float]: A list of delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    return [await task for task in asyncio.as_completed(tasks)]
