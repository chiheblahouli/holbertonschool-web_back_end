#!/usr/bin/env python3
"""mixed"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """sum mixed"""
    return (k, float(v ** 2))
