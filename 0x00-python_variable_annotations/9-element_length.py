#!/usr/bin/env python3
'''guessing type module'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''gives the length of list'''
    return[(i, len(i)) for i in lst]
