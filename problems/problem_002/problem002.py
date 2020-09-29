from typing import List
import numpy as np


def my_func(lst: List) -> List:
    """Type and value checking intentionally left out,
    for the sake of simplicity"""
    res = []
    for i, x in enumerate(lst):
        res.insert(i, np.floor_divide(np.prod(lst, dtype=np.int64), x))
    return res


def my_func_nodivision(lst: List) -> List:
    """Type and value checking intentionally left out,
    for the sake of simplicity"""
    res = []
    for i, x in enumerate(lst):
        tmp_lst = lst.copy()
        del tmp_lst[i]
        res.insert(i, np.prod(tmp_lst))
    return res
