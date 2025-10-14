from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any python values only for integers
    :param values: A list of values of any python data type
    :return: A list of integers from the given list
    """
    return [x for x in values if isinstance(x, int)]
