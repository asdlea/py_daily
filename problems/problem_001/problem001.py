from typing import List


def my_func(k: int, lst: List) -> bool:
    """Type and value checking intentionally left out,
    for the sake of simplicity"""

    if not len(lst) > 0:
        raise ValueError("Parameter 'lst' must have at least 2 elements")

    try:
        for x in lst:
            for y in lst[1:]:
                if x+y == k:
                    return True
        return False
    except Exception as e:
        raise(e)


if __name__ == "__main__":
    try:
        print(my_func(
            int(input("k:")),
            [int(x) for x in
                input("lst (comma separated numbers):").split(',')]))
    except Exception as e:
        print(e)
