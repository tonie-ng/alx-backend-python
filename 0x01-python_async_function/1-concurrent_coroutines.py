#!/usr/bin/env python3
"""Task 1"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Executes wait_random n times.
    Param:
        n - number of times to run wit_random
        max_delay: delay in seconds
    Returns: the ist of all the delays (float values)
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    wait_times = await asyncio.gather(*tasks)
    return sorted(wait_times)
