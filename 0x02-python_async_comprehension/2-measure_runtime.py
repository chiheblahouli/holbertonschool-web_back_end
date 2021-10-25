#!/usr/bin/env python3
"""task 2"""

from typing import List
from time import perf_counter
import asyncio

asyn = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """function"""
    i = perf_counter()
    tasks = [asyncio.create_task(asyn()) for j in range(4)]
    await asyncio.gather(*tasks)
    fde = perf_counter() - i
    return fde
