from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    integers = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers
