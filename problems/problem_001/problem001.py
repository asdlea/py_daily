from typing import List


def my_func(k: int, lst: List) -> bool:
    """Type and value checking intentionally left out,
    for the sake of simplicity"""

    p_k = int(k)
    p_lst = [int(x) for x in lst.split(',')]

    if not len(p_lst) > 0:
        raise ValueError("Parameter 'lst' must have at least 2 elements")

    try:
        for x in p_lst:
            for y in p_lst[1:]:
                if x+y == p_k:
                    return True
        return False
    except Exception as e:
        raise(e)


if __name__ == "__main__":
    print(my_func(input("k:"), input("lst (comma separated numbers):")))
