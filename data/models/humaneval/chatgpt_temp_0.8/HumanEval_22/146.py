from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers """
    filtered_values = []
    for value in values:
        if isinstance(value, int):
            filtered_values.append(value)
    return filtered_values
