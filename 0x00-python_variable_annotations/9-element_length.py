#!/usr/bin/env python3
"""Eleement"""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length"""
    return [(elemnt, len(elemnt)) for elemnt in lst]
