#!/usr/bin/env python3
""" task_wait_random """

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n
    """
    arr = []
    rslt = []
    for i in range(n):
        arr.append(task_wait_random(max_delay))
    for j in asyncio.as_completed(arr):
        rslt.append(await j)
    return rslt
