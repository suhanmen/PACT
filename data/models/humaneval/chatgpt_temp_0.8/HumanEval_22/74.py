from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    """
    return [int(value) for value in values if isinstance(value, int)]
