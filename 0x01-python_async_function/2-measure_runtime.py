#!/usr/bin/env python3
""" task3 """

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time
    """
    t = time.time()
    asyncio.run(wait_n(n, max_delay))
    return ((time.time() - t) / n)
