#!/usr/bin/env python3
"""
Regular function that returns an asyncio.Task for wait_random(max_delay)
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for wait_random(max_delay) and return it

    Args:
        max_delay (int): The maximum delay in seconds for wait_random

    Returns:
        asyncio.Task: An asyncio.Task for wait_random(max_delay)
    """
    return asyncio.create_task(wait_random(max_delay))
