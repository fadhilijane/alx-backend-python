#!/usr/bin/env python3
'''module that adds a mixed list'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''sum mxd_lst'''
    return sum(mxd_lst)
