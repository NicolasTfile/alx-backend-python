#!/usr/bin/env python3
"""
Waits for a random delay between 0 and max_delay seconds (inclusive)
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return it

    Args:
        max_delay (int, optional): The maximum delay in seconds

    Returns:
        float: The random delay
    """
    delay = random.uniform(0, max_delay)

    await asyncio.sleep(delay)

    return delay
