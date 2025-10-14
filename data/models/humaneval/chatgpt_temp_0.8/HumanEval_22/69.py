from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers """
    integers = []
    for val in values:
        if isinstance(val, int):
            integers.append(val)
    return integers

