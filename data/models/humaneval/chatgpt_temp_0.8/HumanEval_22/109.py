from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers """
    integers = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers
