#!/usr/bin/env python3
'''multiples args'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''creates the multiplier function'''
    return lambda x: x * multiplier
