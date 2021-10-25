#!/usr/bin/env python3
""" task0 """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:

    """ function basic async"""

    rand_uni = random.uniform(0, max_delay)
    await asyncio.sleep(rand_uni)
    return rand_uni
