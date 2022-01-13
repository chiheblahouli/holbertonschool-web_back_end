#!/usr/bin/env python3
"""mixed"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """sum mixed"""

    return lambda x: x * multiplier
